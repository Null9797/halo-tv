# HaloTV 独立版桌面守护诊断与修复工具

本工具只识别 `app.halotv.launcher`，用于 Android 5.0 及以上的 HaloTV 独立 Standard / Guard 版。它不负责安装 APK，不适用于旧包名或 Lite 的默认桌面配置。

**不要用上游 Aerial 的 `tools/install.sh` 给 HaloTV 独立版修复守护。** 上游脚本面向 Aerial 的包名，可能下载、安装 Aerial，并向旧包授权；它不能替代本工具。保留上游脚本是为了保留原项目来源，不能据此认为它们也适用于独立版。

## 使用

电脑需要已安装 `adb`（Android platform-tools）及 Python 3。电视需已开机，与电脑连接同一局域网，并由用户开启、授权 ADB。工具不会打开 ADB、修改无线网络，也不会把 ADB 改为持久开启。

在 HaloTV 源码目录中运行：

```bash
# 默认只读取诊断，不修改电视设置。
TV=192.0.2.10 bash tools/halo-guard.sh

# 看完诊断后，由用户主动运行修复模式。
TV=192.0.2.10 bash tools/halo-guard.sh --repair
```

电视使用 Android 无线调试配对端口时，先按系统要求完成 `adb pair`，再用 `TV=电视IP:实际连接端口`。本工具不会自动切换到 5555，也不会替用户确认配对。

已有且只有一个已授权 ADB 设备时，可以省略 `TV`。多台设备连接时必须指定。`ADB=/完整路径/adb` 可指定不在 PATH 中的 adb。Windows 用户可通过能运行 Bash、Python 3 和 adb 的环境运行；也可直接执行 `python tools/halo_guard.py`，并设置同样的 `TV` 环境变量。

## 输出如何理解

- **机型与 SDK**：只读取厂商、型号、Android SDK，不采集序列号、MAC、Wi-Fi 名称、账号、手机设置网址或令牌。
- **系统默认 HOME**：系统当前解析出的桌面。Guard 版依靠无障碍接管 Home，此处仍为系统桌面不代表守护一定失败。
- **守护已登记**：组件在 `enabled_accessibility_services` 中。它只表示设置里登记过，不能证明系统已经绑定服务。
- **守护已实际绑定**：`dumpsys accessibility` 的 Bound services / mBoundServices 区域包含 HaloTV 正确组件。工具不会把 Enabled services 区域误当成实际绑定。
- **无法确认**：部分厂商不提供可识别的 dumpsys 格式。此时即使设置已登记，工具也不会宣称已经运行。
- **旧包守护同时登记**：旧 `app.orchard.tv` 可能是 Aerial 原版，也可能是旧 HaloTV。两边同时接管 Home 可能争抢，工具只报告，绝不自动移除或停用。请用户明确决定保留哪个守护。

独立版的 Android 应用身份与 Kotlin 类命名空间不同，这是正常的。完整组件名是：

```text
应用包：app.halotv.launcher
主界面：app.halotv.launcher/app.orchard.tv.MainActivity
桌面守护：app.halotv.launcher/app.orchard.tv.guard.HomeGuardService
通知监听：app.halotv.launcher/app.orchard.tv.guard.RevivalListener
```

不能把独立包名与 `.guard.HomeGuardService` 或 `.MainActivity` 短类名直接拼接；那会指向并不存在的新命名空间类。旧应用拥有的权限也不会自动转移给独立版。

## `--repair` 做什么

1. 仅对已安装的 `app.halotv.launcher` 按需授予安全设置写入、悬浮窗、使用统计和通知使用权。
2. Android SDK 33 及以上，先检查受限设置 AppOp 是否可用；仅在固件支持时请求允许。厂商自启动、关联启动 AppOp 同样先检查是否存在，未知项跳过。
3. 读取当前无障碍列表，保留所有已有组件，只追加正确的 HaloTV 守护组件；读取失败或列表格式异常时不覆盖它。必要时打开无障碍总开关，并再次读取验证系统是否保留设置。
4. 打开 HaloTV，调用应用原有的守护初始化。它不修改默认桌面，不合成 Home 按键，不禁用系统应用，不卸载任何软件，不强制停止旧包，不更改网络或 ADB 开关，不重启电视。
5. 等待服务绑定后再次读取状态。命令返回成功、组件已经登记和服务实际绑定是三种不同状态，输出分别说明。

修复过程中电视会显示 HaloTV，请在用户允许操作电视时运行。ADB 权限命令仍可能被固件拒绝；工具会显示失败原因，无法代替厂商的手动自启动/关联启动开关。即使当前已经绑定，也应在之后分别验证按 Home 和冷启动，不能据此保证所有型号、所有固件永久生效。

修复模式会先查询当前 Android 用户，仅允许已确认的主用户 `0`。多用户电视当前不是用户 0，或固件不能可靠返回当前用户时，工具只诊断并中止修复，不会猜测用户或给其他用户写入设置。厂商绑定输出缺少完整括号、只返回显示名称、指向其他用户或格式不可识别时，一律标记为“无法确认”。

退出码：`0` 为完成诊断或确认服务绑定；`2` 为连接/环境问题；`3` 为未安装目标应用或不适用；`4` 为修复后仍未确认真实绑定。默认诊断退出 `0` 仅表示读取完成，**不表示守护健康**。

## 离线回归测试

```bash
python3 -m unittest tools/test_halo_guard.py -v
```

所有 ADB 调用都由临时 stub 替代，不会连接真实电视或网络。测试覆盖只读默认行为、新包名与完整组件、保留其他服务、旧包不被改动、受限设置与厂商 AppOp 按需授权、通知授权静默失败、固件拒写、无法确认绑定及异常列表不执行 shell 文本等情形。
