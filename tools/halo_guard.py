#!/usr/bin/env python3
"""Diagnose/repair only the independent HaloTV guard; no APK installer or TV takeover."""
import argparse
import os
import re
import shlex
import shutil
import subprocess
import sys
import time

PACKAGE = "app.halotv.launcher"
LEGACY = "app.orchard.tv"
GUARD = PACKAGE + "/app.orchard.tv.guard.HomeGuardService"
LISTENER = PACKAGE + "/app.orchard.tv.guard.RevivalListener"
HOME = PACKAGE + "/app.orchard.tv.MainActivity"
SERVICE_KEY = "enabled_accessibility_services"
LISTENER_KEY = "enabled_notification_listeners"
COMPONENT = re.compile(r"[A-Za-z0-9_.]+/[A-Za-z0-9_.$]+")
ERROR = re.compile(r"(^|\n)\s*(?:error[: ]|exception|securityexception|unknown |not found|bad |failure|failed\b|permission deni(?:al|ed)\b|no uid for\b|java\.)", re.I)


def canonical(value):
    if not COMPONENT.fullmatch(value):
        return None
    package, name = value.split("/", 1)
    return package + "/" + (package + name if name.startswith(".") else name)


def component_list(value):
    return [item.strip() for item in value.split(":") if item.strip() not in ("", "null")]


def contains(value, component):
    return any(canonical(item) == component for item in component_list(value))


def bound_state(dump, component, user=None):
    """Inspect only bound-service containers: enabled/registered is not evidence of binding."""
    # Do not mistake another Android user's binding for the current owner's guard. Most TVs
    # expose one user; multi-user/vendor dumps need an explicit current-user-aware inspection.
    if len(re.findall(r"(?im)^\s*User\s+state\[", dump)) > 1:
        return None
    explicit_user = re.search(r"(?im)^\s*User\s+state\[[^\n]*\bid\s*=\s*(\d+)", dump)
    if explicit_user and (user is None or int(explicit_user.group(1)) != user):
        return None
    headings = list(re.finditer(r"(?im)^\s*(?:mBoundServices|Bound\s+services)\s*[:=]\s*", dump))
    if not headings:
        return None
    unrecognized = False
    for heading in headings:
        rest = dump[heading.end():]
        if rest.startswith(("{", "[")):
            opening = rest[0]
            closing = "}" if opening == "{" else "]"
            depth = 0
            end = len(rest)
            closed = False
            for i, char in enumerate(rest):
                if char == opening:
                    depth += 1
                elif char == closing:
                    depth -= 1
                    if depth == 0:
                        end = i + 1
                        closed = True
                        break
            if not closed:
                return None
            section = rest[:end]
        else:
            # Some vendors print one component per indented line rather than a container.
            section = re.split(r"(?im)^\s*(?:m\w+|Enabled\s+services|Binding\s+services|User\s+state)\s*[:=]", rest, maxsplit=1)[0]
        components = COMPONENT.findall(section)
        if any(canonical(item) == component for item in components):
            return True
        if not components and re.search(r"[A-Za-z0-9\u4e00-\u9fff]", section):
            unrecognized = True
    return None if unrecognized else False


def safe_error(value):
    value = re.sub(r"\x1b\[[0-9;]*m", "", value)
    value = re.sub(r"(?:\d{1,3}\.){3}\d{1,3}", "<IP>", value)
    value = re.sub(r"(?:[0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}", "<MAC>", value)
    return " ".join(value.strip().split())[:240] or "命令未返回详细原因"


class Adb:
    def __init__(self):
        requested = os.environ.get("ADB", "adb")
        self.executable = shutil.which(requested)
        if not self.executable:
            raise RuntimeError("找不到 adb，请先安装 Android platform-tools，或用 ADB=/完整路径/adb 指定。")
        self.serial = ""
        self.user = None

    def run(self, args, timeout=20):
        # Server-side commands do not select a transport. In particular, connect must work
        # before that transport exists, including on older platform-tools.
        selected = self.serial and args[:1] not in (["connect"], ["devices"])
        command = [self.executable] + (["-s", self.serial] if selected else []) + args
        try:
            result = subprocess.run(command, capture_output=True, text=True, timeout=timeout)
            output = (result.stdout + result.stderr).replace("\r", "").strip()
            return result.returncode == 0 and not ERROR.search(output), output
        except subprocess.TimeoutExpired:
            return False, "ADB 命令超时，请检查电视是否开机、调试是否仍开启。"
        except OSError as error:
            return False, str(error)

    def shell(self, *args):
        # adb shell joins arguments into a remote shell command. Quote every value, including
        # service lists read from the TV, instead of letting a component name become shell code.
        return self.run(["shell", " ".join(shlex.quote(str(arg)) for arg in args)])

    def connect(self):
        target = os.environ.get("TV", "").strip()
        if target:
            self.serial = target if ":" in target else target + ":5555"
            ok, output = self.run(["connect", self.serial], timeout=12)
            if not ok:
                print("ADB 连接提示：" + safe_error(output))
        else:
            ok, output = self.run(["devices"])
            devices = [line.split()[0] for line in output.splitlines() if re.search(r"\sdevice$", line)] if ok else []
            if len(devices) != 1:
                raise RuntimeError("请指定电视地址：TV=电视IP bash tools/halo-guard.sh。已有多台设备时也需指定。")
            self.serial = devices[0]
        ok, output = self.run(["get-state"])
        if not ok or output != "device":
            if "unauthorized" in output:
                raise RuntimeError("电视尚未授权这台电脑。请在电视弹窗选择“允许 USB 调试”，再运行。")
            raise RuntimeError("未建立 ADB 连接。确认电视开机、同一局域网及 ADB 开启；无线调试设备请先 adb pair，并提供调试页的实际端口。")


def read(adb, *args):
    ok, output = adb.shell(*args)
    return output if ok else ""


def current_user(adb):
    for command in (("am", "get-current-user"), ("cmd", "activity", "get-current-user")):
        ok, output = adb.shell(*command)
        if ok and re.fullmatch(r"\d+", output):
            return int(output)
    return None


def resolved_home(adb, combined=False):
    args = ["cmd", "package", "resolve-activity", "--brief", "-a", "android.intent.action.MAIN", "-c", "android.intent.category.HOME"]
    if combined:
        args += ["-c", "android.intent.category.LAUNCHER"]
    args += ["-c", "android.intent.category.DEFAULT"]
    ok, output = adb.shell(*args)
    components = COMPONENT.findall(output) if ok else []
    return components[-1] if components else "系统未返回可解析的桌面"


def supported_op(adb, names):
    for name in names:
        ok, output = adb.shell("appops", "get", PACKAGE, name)
        if ok and not re.search(r"unknown|invalid|not recognized|not found", output, re.I):
            match = re.search(r":\s*(allow|ignore|deny|default|foreground|errored)\b", output, re.I)
            return name, match.group(1).lower() if match else "default"
    return None, "unsupported"


def snapshot(adb):
    package = read(adb, "dumpsys", "package", PACKAGE)
    state = {
        "package": package,
        "enabled": read(adb, "settings", "get", "secure", SERVICE_KEY),
        "global": read(adb, "settings", "get", "secure", "accessibility_enabled"),
        "listeners": read(adb, "settings", "get", "secure", LISTENER_KEY),
        "bound": bound_state(read(adb, "dumpsys", "accessibility"), GUARD, adb.user) if adb.user == 0 else None,
        "secure": bool(re.search(r"android\.permission\.WRITE_SECURE_SETTINGS:\s*granted=true", package)),
    }
    state["registered"] = contains(state["enabled"], GUARD)
    return state


def show_snapshot(state, title):
    print("\n" + title)
    print("  WRITE_SECURE_SETTINGS：" + ("已授予" if state["secure"] else "未确认授予"))
    print("  无障碍总开关：" + ("开" if state["global"] == "1" else "关或无法读取"))
    print("  HaloTV 守护登记：" + ("已登记" if state["registered"] else "未登记"))
    bound = {True: "已实际绑定", False: "尚未绑定", None: "固件未提供可识别的绑定信息，无法确认"}[state["bound"]]
    print("  HaloTV 守护运行：" + bound)
    print("  通知使用权登记：" + ("已登记" if contains(state["listeners"], LISTENER) else "未登记"))
    entries = [item for item in component_list(state["enabled"]) if canonical(item)]
    print("  已登记无障碍组件：" + ("；".join(entries) if entries else "未返回有效组件"))
    if any(item.startswith(LEGACY + "/") and item.endswith("HomeGuardService") for item in entries):
        print("  注意：旧包的守护也在登记列表，可能互相争抢。旧包可能是 Aerial 或旧 HaloTV，请自行确认；本工具不会停用它。")
    wrong = PACKAGE + "/.guard.HomeGuardService"
    if wrong in entries:
        print("  注意：列表含有错误的独立包短类名。正确类名为 " + GUARD + "，本工具不会删除其他登记项。")


def mutation(adb, description, *args):
    ok, output = adb.shell(*args)
    print("  " + description + ("：命令已执行，稍后读回确认" if ok else "：失败，" + safe_error(output)))
    return ok


def merge_setting(adb, key, component):
    ok, current = adb.shell("settings", "get", "secure", key)
    if not ok:
        print("  无法读取 " + key + "，为保留其他服务，本次不写入。")
        return False
    entries = component_list(current)
    if any(not canonical(item) for item in entries):
        print("  " + key + " 列表格式异常，为避免覆盖其他服务，本次不写入。")
        return False
    if not any(canonical(item) == component for item in entries):
        if not mutation(adb, "登记 HaloTV 组件（保留其他服务）", "settings", "put", "secure", key, ":".join(entries + [component])):
            return False
    ok, after = adb.shell("settings", "get", "secure", key)
    retained = {canonical(item) for item in component_list(after)}
    if not ok or component not in retained:
        print("  系统未保留 HaloTV 组件，可能受受限设置或厂商策略限制。")
        return False
    if not {canonical(item) for item in entries}.issubset(retained):
        print("  警告：读回时其他无障碍/通知组件发生变化，请检查电视上的无障碍设置。")
        return False
    return True


def repair(adb, sdk, before):
    print("\n开始修复独立版守护（仅此模式会修改设置）")
    if not before["secure"]:
        mutation(adb, "安全设置写入权限", "pm", "grant", PACKAGE, "android.permission.WRITE_SECURE_SETTINGS")
    operations = [
        ("悬浮窗", ["SYSTEM_ALERT_WINDOW", "android:system_alert_window"]),
        ("使用统计", ["GET_USAGE_STATS", "android:get_usage_stats"]),
    ]
    if sdk >= 33:
        operations.append(("受限设置许可", ["ACCESS_RESTRICTED_SETTINGS", "android:access_restricted_settings"]))
    operations += [
        ("厂商自启动", ["APP_AUTO_START"]),
        ("厂商关联启动", ["APP_ASSOC_START", "ASSOC_START"]),
    ]
    for description, names in operations:
        name, mode = supported_op(adb, names)
        if not name:
            print("  " + description + "：固件不支持此 AppOp，跳过。")
        elif mode == "allow":
            print("  " + description + "：已允许，不重复修改。")
        else:
            mutation(adb, description, "appops", "set", PACKAGE, name, "allow")
            _, verified = supported_op(adb, [name])
            print("    读回：" + ("已允许" if verified == "allow" else "未确认允许，仍需在电视系统设置中确认。"))
    if not contains(read(adb, "settings", "get", "secure", LISTENER_KEY), LISTENER):
        if not mutation(adb, "通知使用权", "cmd", "notification", "allow_listener", LISTENER):
            print("  通知授权命令不可用，尝试仅追加 HaloTV 通知组件。")
        # A zero exit status is not enough: older firmwares silently ignore this command.
        if not contains(read(adb, "settings", "get", "secure", LISTENER_KEY), LISTENER):
            merge_setting(adb, LISTENER_KEY, LISTENER)
    if merge_setting(adb, SERVICE_KEY, GUARD):
        if read(adb, "settings", "get", "secure", "accessibility_enabled") != "1":
            mutation(adb, "无障碍总开关", "settings", "put", "secure", "accessibility_enabled", "1")
    # Initialize the app's existing recovery/account logic. Never synthesize HOME or change the
    # default launcher; the owner has explicitly asked to repair this app's guard.
    mutation(adb, "打开 HaloTV 完成守护初始化", "am", "start", "-W", "-n", HOME)


def main():
    parser = argparse.ArgumentParser(description="HaloTV 独立版守护诊断工具。默认只读；--repair 明确授权修复。")
    parser.add_argument("--repair", action="store_true", help="仅修复已安装的独立版守护权限和服务登记，并打开 HaloTV")
    args = parser.parse_args()
    adb = Adb()
    adb.connect()
    adb.user = current_user(adb)
    print("HaloTV 独立版桌面守护" + ("诊断与修复" if args.repair else "只读诊断"))
    model = read(adb, "getprop", "ro.product.model")
    maker = read(adb, "getprop", "ro.product.manufacturer")
    sdk_text = read(adb, "getprop", "ro.build.version.sdk")
    sdk = int(sdk_text) if sdk_text.isdigit() else 0
    print("机型：" + safe_error(maker + " " + model) + "；Android SDK：" + (str(sdk) if sdk else "未知"))
    print("当前 Android 用户：" + (str(adb.user) if adb.user is not None else "无法确认"))
    installed = read(adb, "pm", "path", PACKAGE)
    legacy = read(adb, "pm", "path", LEGACY)
    print("独立包：" + PACKAGE)
    print("旧包 app.orchard.tv：" + ("已安装（可能是 Aerial 或旧 HaloTV；不会修改）" if legacy.startswith("package:") else "未检出"))
    if not installed.startswith("package:"):
        print("未检测到独立版 HaloTV。不会给旧包授权，也不会下载或安装任何软件。")
        return 3
    before = snapshot(adb)
    for label in ("versionName", "versionCode"):
        found = re.search(r"\b" + label + r"=([^\s]+)", before["package"])
        print(label + "：" + (found.group(1) if found else "未读取到"))
    print("系统默认 HOME：" + resolved_home(adb))
    print("HOME+LAUNCHER 组合：" + resolved_home(adb, combined=True))
    show_snapshot(before, "当前守护状态")
    if not args.repair:
        print("\n以上仅为读取结果，未修改电视设置。需要修复时主动加 --repair；已登记不等于已绑定。")
        return 0
    if adb.user != 0:
        print("修复已中止：仅允许已确认的 Android 主用户 0；其他用户或无法确认当前用户时不会授予权限、写入设置或启动应用。")
        return 3
    if sdk and sdk < 21:
        print("此工具面向 Android 5.0+ 的独立 Standard/Guard。旧系统 Lite 不使用本守护服务。")
        return 3
    repair(adb, sdk, before)
    try:
        wait_seconds = min(10.0, max(0.0, float(os.environ.get("HALO_GUARD_WAIT_SECONDS", "4"))))
    except ValueError:
        wait_seconds = 4.0
    if wait_seconds:
        time.sleep(wait_seconds)
    after = snapshot(adb)
    show_snapshot(after, "修复后读回与绑定验证")
    if after["bound"] is True and after["registered"] and after["global"] == "1":
        print("\n已确认独立版守护实际绑定。厂商仍可能在重启/待机后限制后台，建议之后分别验证 Home 与冷启动。")
        return 0
    print("\n尚未确认守护实际绑定，不能据此声称已修复。请在系统中检查允许受限设置、无障碍、通知使用权、自启动和关联启动。")
    print("本工具未改变默认桌面、系统应用、网络或 ADB 开关，也未重启电视。")
    return 4


if __name__ == "__main__":
    try:
        sys.exit(main())
    except RuntimeError as error:
        print(str(error), file=sys.stderr)
        sys.exit(2)
