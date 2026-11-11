# HaloTV 3.0.3 安装指南

官网：https://halo-tv.pages.dev/

网盘：https://pan.quark.cn/s/a14e3ab2dd41

推荐优先从官网下载 Standard / Guard / Lite，GitHub Releases 作为备用。3.0.3 正式版内部号 181，Lite 内部号 39。


本指南适用于支持 Android TV / Google TV 的电视或电视盒子。菜单因品牌、固件版本和地区而异；不支持 Android APK 的系统无法使用本项目。**如果电视没有明确提供 ADB 调试，不要尝试未知工程码、关闭系统安全服务或修改系统分区。**

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

## 5. 安装 APK

先从 GitHub Releases 下载一个 APK。Standard 和 Guard 同包名，只安装一个。

macOS / Linux：

```shell
adb install -r "$HOME/Downloads/HaloTV-3.0.3-standard.apk"
```

Windows PowerShell：

```powershell
adb install -r "$env:USERPROFILE\Downloads\HaloTV-3.0.3-standard.apk"
```

选择 Guard 时，把文件名换成 `HaloTV-3.0.3-guard.apk`。看到 `Success` 即表示 Android 安装器接受了安装。随后在电视的应用列表打开 Halo TV。

可选：用 ADB 打开已安装的应用：

```shell
adb shell monkey -p app.orchard.tv 1
```

## 6. 选择桌面和屏保

- **Standard**：按 Home 键，在 Android 的桌面选择器中选 Halo TV；确认要作为长期桌面后，再选择“始终”。也可从系统默认应用设置里更改主屏幕应用。
- **Guard**：此构建不注册常规 HOME 桌面入口。打开 Halo TV，按其设置页提示配置守护桌面。某些设备会要求无障碍服务、使用情况访问或其他系统授权；只有理解授权用途并确认要使用守护功能后再逐项启用。
- 在 Halo TV 设置里选择翻页时钟等屏保，并设定空闲进入时间。2.0 已移除屏保后自动待机选项。

## 7. 更新提示、变体切换与卸载

本版本会定期查询 `Null9797/halo-tv` 的最新正式 Release；联网并打开 Halo TV/控制中心时会检查更新。发现新版本后选择下载，电视系统安装器会显示确认界面。应用只选取与当前 flavor 匹配的 APK，不会静默安装。发布者必须继续使用相同签名证书，否则 Android 会拒绝覆盖更新。

- 安装新版本时使用 `adb install -r <APK路径>`，这会尝试保留应用数据。
- Standard 与 Guard 共用包名，安装另一个变体会替换当前变体，不能并行使用。
- 卸载前先在电视中切回原桌面。随后可在「设置 → 应用 → Halo TV → 卸载」操作；也可运行 `adb uninstall app.orchard.tv`。该命令只卸载 Halo TV，不要将包名替换成系统应用。
- 安装完成后可在开发者选项关闭 ADB 调试；应用运行不要求电脑一直连接。

## 8. 让 AI 助手代为安装

请使用能够在本机执行命令的 AI 编程助手（例如 Codex、Claude Code 或其他本地代理）。纯网页聊天无法直接访问你的电脑或电视。将电视 IP、APK 文件路径和以下提示词交给助手：

```text
请通过我电脑上的 Android Platform Tools 用 ADB 安装这个 Halo TV APK。
电视 IP：<电视 IP>
APK 文件路径：<APK 完整路径>

先运行 adb version 并确认 APK 文件存在。连接方式请按电视的开发者选项判断：
如果电视显示无线调试配对码，先 adb pair <IP:配对端口>，然后 adb connect <IP:连接端口>；
如果电视只开放传统网络 ADB，再尝试 adb connect <IP:5555>。
运行 adb devices -l 确认目标状态为 device 后，再运行 adb install -r "<APK路径>"。
若电视要求授权、配对码或安装确认，请暂停，让我在电视上亲自确认。
安装后告诉我如何打开 Halo TV 和选择默认桌面。不要卸载其他应用、关闭系统验证、
停用系统安装器、改写系统设置或授予持续权限；这些步骤只有在我另行明确要求后才执行。
```

## 故障排查

| 现象 | 建议处理 |
|---|---|
| `failed to connect` | 核对 IP、端口、同一局域网和调试开关。Android 11+ 优先使用当前无线调试页显示的端口并重新配对。 |
| `unauthorized` | 在电视上确认 RSA 指纹授权；不要绕过授权。 |
| `no devices/emulators found` | 先检查 `adb devices -l`，并重新连接；多设备时用 `-s` 指定电视。 |
| `INSTALL_FAILED_USER_RESTRICTED` | 检查电视安装确认框和厂商“通过 ADB 安装”策略。本项目不建议关闭系统验证或停用系统安装器。 |
| `INSTALL_FAILED_VERSION_DOWNGRADE` | 已安装版本可能比此包版本新。先确认包来源和设置备份；不要盲目卸载。 |
| `INSTALL_FAILED_UPDATE_INCOMPATIBLE` | 现有应用的签名与此 APK 不同。先联系发布者确认，不要为了覆盖而清除数据或卸载。 |
| 安装成功但 Home 键仍回原桌面 | Standard 需要在系统里选为默认桌面；Guard 需完成应用内守护设置。厂商限制可能导致无法接管。 |


## HaloTV 3.0.3 更新与手机推送

2.1.4 正式版通过最新 GitHub Release 发现 3.0.3；旧版网络无法访问 GitHub 时，在手机从官网或网盘下载同版本类型包，使用 U 盘或 ADB 覆盖安装。2.1.4 Lite 无内置在线检查入口，先手动升级 3.0.3。

3.0.3：控制中心 → 软件更新，检查更新、在线下载；默认优先官网，GitHub 备用。自动下载默认关闭，可手动打开，下载完成后仍需确认安装。手机推送：扫描设置中的二维码，同一局域网打开手机管理中心 → 推送安装包更新，选择同包名、同签名、更高内部号的 HaloTV APK。上传完成回到电视 → 软件更新 → 手动更新，确认安装。只支持 HaloTV 自身更新。

AI 安装指令：

```text
请帮我把 HaloTV 3.0.3 安装到我的安卓电视或安卓电视盒子。官网是 https://halo-tv.pages.dev/，GitHub 仓库是 https://github.com/Null9797/halo-tv。请优先从官网下载适合设备的最新包：Android 5.0 及以上优先 Standard，固件拒绝第三方桌面时尝试 Guard；Android 4.0–4.4 用 Lite。一步步指导我开启 ADB 调试、查看 IP 并确认连接，下载后用 ADB 覆盖安装，保留已有设置。安装成功后验证版本与运行情况，再根据我的授权配置默认桌面和必要的守护权限。遇到错误请解释并继续排查，不删除系统桌面或其他应用。
```
