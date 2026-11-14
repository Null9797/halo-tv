# HaloTV 3.1.2 安装、升级与守护配置

[官网](https://halo-tv.pages.dev/) · [GitHub Releases](https://github.com/Null9797/halo-tv/releases/tag/v3.1.2-halo) · [网盘](https://pan.quark.cn/s/a14e3ab2dd41)

Standard / Guard：Android 5.0+，内部号 **197**；Lite：Android 4.0+，内部号 **52**。三个包均显示 **3.1.2**，使用 HaloTV 独立包名和专属签名。

- 新用户：Android 5.0+ 优先 Standard；固件明确拒绝第三方 HOME 桌面时尝试 Guard；Android 4.0–4.4 使用 Lite。
- 已安装独立版：下载与当前类型一致的包覆盖升级，尝试保留数据。
- 仍是旧包名：先安装 [3.1 同类型过渡版](https://github.com/Null9797/halo-tv/releases/tag/v3.1-halo)，再安装独立版、导入资料、重新配置权限。确认正常后才卸载旧 HaloTV。详见 [迁移说明](MIGRATION-3.1.md)。

不要同时启用两套桌面守护。旧 `app.orchard.tv` 可能是 Aerial 或旧 HaloTV，不能只凭包名自动卸载它。新包名不等于旧应用的原地覆盖。

菜单因品牌、固件和地区而异，不支持 Android APK 的系统无法安装。不明工程选项请勿改动；电视没有开放 ADB 时，以厂商支持为准。

## 1. 电视与电脑接入同一网络

在电视的「设置 → 网络」查看当前 IPv4 地址，例如 `192.168.1.25`。电视和电脑需在同一个家庭局域网；不要通过公网暴露电视的 ADB 端口。

## 2. 开启开发者选项和 ADB 调试

### Android TV / Google TV 通用入口

1. 打开「设置 → 系统」或「设备偏好设置 → 关于」。
2. 找到「Android TV OS build」「内部版本号」或「Build」，连续按遥控器确认键约 7 次，直到提示已开启开发者选项。
3. 返回系统设置 →「开发者选项」，开启「USB 调试」或「ADB 调试」。如果电视支持 Android 11+ 的「无线调试」，可以直接用配对码方式连接。
4. 连接电脑后，在电视授权本电脑的调试请求。

Google 的 ADB 文档说明 Android 11 及更新版本支持无线配对；电视厂商可隐藏或禁用该功能：[Android Developers：ADB over Wi‑Fi](https://developer.android.com/tools/adb#connect-to-a-device-over-wi-fi-android-11)。
TCL 通用 Android 设备的开发者选项步骤也见 [TCL 官方说明](https://www.tcl.com/global/en/support/faq/10877)；电视菜单仍可能因型号和软件版本不同而变化。

### 常见品牌路径（仅供菜单定位，入口会因地区、系统和型号改变）

| 品牌 / 系统 | 建议步骤 | 证据与限制 |
|---|---|---|
| Google TV / 原生 Android TV | 设置 → 系统（或设备偏好设置）→ 关于 → 连按 Android TV OS build / Build 约 7 次；返回开发者选项开启 USB/ADB 调试。Android 11+ 若有无线调试，可用配对码。 | [Android Developers 官方说明](https://developer.android.com/studio/run/device)；厂商可隐藏该入口。 |
| TCL / 雷鸟 Google TV | 先试通用 Android TV 路径。 | TCL 菜单因地区和固件不同；见 [TCL USB debugging FAQ](https://www.tcl.com/eu/en/support/faq/15199)。 |
| TCL / 雷鸟部分国行固件 | 上游 Aerial 社区对部分机型记录为：设置 → 关于 → 本机信息，在页面内快速按遥控器 ↑、↓、←、→，进入“更多”后只寻找 ADB 开关。 | 来自 [上游 Aerial 机型说明](https://github.com/pengchujin/aerial-tv/blob/main/docs/devices/adb-by-brand.md)，不是通用 TCL 按键码；不匹配就停止，不进入其他工程选项。 |
| 小米 / Redmi 电视、盒子 | 设置 → 关于 → 连按“产品型号”约 7 次启用开发者选项；部分国行固件随后在设置 → 账号与安全 → ADB 调试中开启。 | [小米官方说明](https://www.mi.com/global/support/article/KA-06513/)；菜单名称依型号变化。 |
| Sony BRAVIA / 海信 Android TV | 通常采用 Android TV 通用路径。 | VIDAA 系统不是 Android TV；必须先确认系统版本/平台。 |
| OPPO / 一加电视 | 上游社区记录的部分机型：设置 → 系统 → 关于本机 → 设备型号，按 ↑、↑、→、→ 后确认，再在开发者选项打开 USB/ADB 调试。 | 仅为特定型号社区记录；若无提示或不匹配，不要试其他组合。 |
| 海尔 / 模卡、部分创维及其他国行电视 | 以本机说明书或厂商支持为准。 | 上游记录的某些海尔机型需进入工厂菜单；本指南不建议盲目操作工厂菜单，不明选项请勿更改。 |
| Amazon Fire TV / Fire TV Stick | 设置 → My Fire TV（或 Device & Software）→ Developer Options → ADB Debugging；IP 在 About → Network。 | [Amazon 官方 ADB 说明](https://developer.amazon.com/docs/fire-tv/connecting-adb-to-device.html)。此 APK 在 Fire TV 的桌面和屏保功能未经验证。 |
| Samsung Tizen / LG webOS / Hisense VIDAA | 无 Android TV 的 ADB APK 安装方式。 | 不能安装此 Android APK。 |

ADB 入口来自 Android/TCL/小米/Amazon 官方资料及上游 Aerial 的社区机型笔记。社区序列只适用于其记录的固件，不保证在同品牌其他机型有效。
该清单不是所有型号的完整列表。菜单不存在时，可能是厂商没有向该机型开放 ADB。

## 3. 安装 Android Platform Tools

下载 Google 官方的 [Android SDK Platform Tools](https://developer.android.com/tools/releases/platform-tools)，解压到电脑。打开终端或 PowerShell，切换到其中 `platform-tools` 目录，然后确认：

```shell
adb version
```

macOS 可将 `platform-tools` 目录加入 PATH，或在该目录运行 `./adb`。Windows PowerShell 在当前目录运行 `.\adb.exe`。下文假设命令已在 PATH 中。

## 4. 连接电视

### Android 11 及更新版本：无线调试配对

在电视开发者选项打开「无线调试」，选择「使用配对码配对设备」。电视会显示 IP、配对端口、一次性配对码；关闭配对弹窗前同时记下无线调试页显示的连接端口。

```shell
adb pair 192.168.1.25:37123
# 按提示输入电视显示的一次性配对码
adb connect 192.168.1.25:41267
adb devices -l
```

上面的 IP 和端口只是示例。必须使用电视当前屏幕显示的值；配对端口与连接端口可能不同，也可能在重启或断开网络后改变。

### 旧版 Android TV 或传统网络 ADB

某些电视开启 ADB 调试后会在本地网络开放 TCP 5555：

```shell
adb connect 192.168.1.25:5555
adb devices -l
```

如果电视屏幕显示了其它端口，使用屏幕上的端口。不要把 `5555` 当作所有电视的固定端口。

### 首次授权

`adb devices -l` 应显示电视序列号和 `device`。如果显示 `unauthorized`，看电视屏幕上的 RSA 授权对话框，确认这是自己的电脑后再允许。若没有弹窗，可在开发者选项中撤销 USB 调试授权后重新连接。

如果电脑同时连接了多台设备，后续命令加 `-s <设备序列号>`，避免把 APK 装到错误设备。

## 5. 安装独立版 APK

只选一个当前类型对应的 APK。Standard 与 Guard 共用独立包名，不能同时安装；手机推送要求类型一致。

macOS / Linux：

```shell
adb install -r "$HOME/Downloads/HaloTV-3.1.2-standard.apk"
```

Windows PowerShell：

```powershell
adb install -r "$env:USERPROFILE\Downloads\HaloTV-3.1.2-standard.apk"
```

Guard 改为 `HaloTV-3.1.2-guard.apk`，Lite 改为 `HaloTV-3.1.2-lite.apk`。显示 `Success` 说明安装器接受了安装，随后打开应用检查版本。

Standard / Guard 的完整启动组件：

```shell
adb shell am start -n app.halotv.launcher/app.orchard.tv.MainActivity
```

Lite 的完整启动组件：

```shell
adb shell am start -n app.halotv.launcher.lite/app.orchard.tv.lite.HomeActivity
```

应用 ID 与代码类命名空间不同是正常的。不要把新包名与 `.MainActivity` / `.guard.HomeGuardService` 短类名拼接。

## 6. 默认桌面、屏保和守护

- Standard：若系统允许，先在默认应用/主屏幕设置中选 HaloTV。系统原生 HOME 选择通常更直接。
- Guard：不注册普通 HOME 入口，按控制中心内的引导配置桌面守护。
- Lite：主要依靠系统默认桌面选择，不包含正式版 HomeGuardService。
- 壁纸与屏保从 HaloTV 控制中心进入，按需设置翻页时钟等屏保。

**独立版不会继承旧版的权限。** 无障碍、通知使用权、自启动、关联启动、使用统计和悬浮窗等需要按当前电视提供的入口重新确认。Android 13+ 若限制侧载应用的无障碍，检查应用信息中是否提供“允许受限设置”。系统不提供或拒绝时，应用无法保证突破。

服务已登记不等于实际绑定，当前绑定也不代表冷启动后一定有效。请分别测试 Home、短待机唤醒和冷启动；在方便停止播放时再测试重启。

### 独立版专用 ADB 诊断

不要用上游 Aerial `tools/install.sh` 修复独立版：它面向旧包并可能下载 Aerial。使用本仓库本版源码中的工具，电脑需有 ADB 和 Python 3。

```shell
# 只读诊断，不改电视设置
TV=电视IP bash tools/halo-guard.sh

# 阅读结果并明确需要修复后，主动执行；这会打开电视上的 HaloTV
TV=电视IP bash tools/halo-guard.sh --repair
```

工具保留其他无障碍服务，只按需处理独立版，不修改默认桌面，不卸载/禁用系统应用，不改变网络或持久打开 ADB。无法确认服务实际绑定时会明确提示。多用户或未知用户不自动修复。详见 [工具说明](docs/HALO_GUARD_TOOL.md)。

## 7. 更新、手机推送与卸载

独立版使用独立更新清单，默认官网优先、GitHub 备用。旧更新清单保留指向过渡版，避免把不同包名当作普通覆盖包。旧 Lite 没有更新入口时需手动安装一次对应过渡版。

电视：控制中心 → 软件更新 → 检查更新。自动下载默认关闭；开启后下载完成仍需电视确认安装。

手机：与电视同一网络，扫码打开管理中心 → 推送安装包更新 → 选择相同类型、包名、签名且内部号更高的 HaloTV APK。完成后回到电视的软件更新 → 手动更新确认安装。过渡版另支持经过校验的对应独立包迁移，不接受任意其他应用。

需要卸载独立版时，先在电视系统设置切回其他默认桌面、停止相关守护，再在应用管理卸载 HaloTV。确认目标确为独立版时也可使用：

```shell
# Standard / Guard 独立版
adb uninstall app.halotv.launcher
# Lite 独立版
adb uninstall app.halotv.launcher.lite
```

卸载会删除该包私有数据。不要将命令中的包名改成系统应用；不要将旧 `app.orchard.tv` 直接等同于 HaloTV，它也可能是 Aerial。安装成功后可以关闭 ADB，日常运行不要求电脑保持连接。

## 8. 可交给本地 AI 助手的安装指令

```text
请帮我把 HaloTV 3.1.2 安装到安卓电视或电视盒子。官网 https://halo-tv.pages.dev/，GitHub https://github.com/Null9797/halo-tv。请先确认电视 Android 版本和当前 HaloTV 包名/类型；5.0+优先Standard，固件拒绝HOME应用时试Guard，4.0–4.4用Lite。独立包是app.halotv.launcher或app.halotv.launcher.lite；旧包用户先按3.1迁移指南安装对应过渡版，不能盲目卸载app.orchard.tv。请一步步指导我开启ADB、查看IP与端口，按系统要求配对和确认连接。下载后核对来源、版本、包名、签名，用ADB安装，尽量保留现有数据。打开验证成功后，再根据我的授权配置默认桌面及守护。独立版的类仍是app.orchard.tv.MainActivity。遇到错误解释并排查，不删除或停用系统桌面、不修改网络、不自动卸载Aerial或旧HaloTV。
```

纯网页聊天通常不能直接操作本地电视；需要可在自己电脑执行 ADB 的本地代理。配对、RSA授权和安装确认按电视系统要求完成。

## 故障排查

| 现象 | 检查方向 |
|---|---|
| failed to connect / unauthorized | 核对同一网络、当前IP、实际调试端口及电视RSA授权；无线调试需要先配对。 |
| INSTALL_FAILED_USER_RESTRICTED | 检查电视确认框及厂商安装策略，不盲目关闭系统验证。 |
| INSTALL_FAILED_UPDATE_INCOMPATIBLE | 包名或签名不匹配；先分清过渡版、独立版和当前类型，不盲目卸载。 |
| INSTALL_FAILED_VERSION_DOWNGRADE | 内部号不够高；确认发布版本，不仅看显示名称。 |
| 守护显示开启但Home回系统 | 查实际绑定、受限设置、自启动和旧守护并存；使用只读诊断工具，不反复切开关。 |
| 次日/冷启动后失效 | 查看厂商待机强停及恢复权限，当前运行不能证明重启后有效。 |
| 旧版收不到迁移弹窗 | 远程公告需要客户端本来支持、公告未关闭且联网；没有该能力的版本不能远程补加。 |
