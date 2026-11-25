<div align="center">
  <img src="website/images/brand/halotv.png" alt="HaloTV Logo" width="120" height="120">
  <h1>HaloTV</h1>
  <p><strong>你的电视，你的桌面。</strong></p>
  <p>免费开源的 Android TV 桌面 · 3.6 正式版</p>
  <p><a href="https://halo-tv.pages.dev/"><strong>官方网站</strong></a> · <a href="#夸克网盘下载"><strong>网盘下载</strong></a> · <a href="#下载与安装"><strong>下载与安装</strong></a> · <a href="docs/README.md">文档</a> · <a href="https://github.com/Null9797/halo-tv/issues">Issues</a> · <a href="docs/README.en.md">English</a></p>
</div>

[![HaloTV 主桌面实拍，展示电视上的桌面快捷栏、玻璃 Dock 与音乐灵动岛](website/images/showcase/main.jpg)](website/images/showcase/main.jpg)

HaloTV 基于 [Aerial](https://github.com/pengchujin/aerial-tv) 二次开发，由 Null_ 整理发布。感谢原作者与所有开源贡献者，保留原版权和 [MIT 许可](LICENSE)。

<a name="下载"></a>

## 下载与安装

### 夸克网盘下载

[打开夸克网盘分享](https://pan.quark.cn/s/1eeb43d9a7cd) · [到官网一键复制链接](https://halo-tv.pages.dev/#quark-download)

```text
https://pan.quark.cn/s/1eeb43d9a7cd
```

1. 复制链接，用夸克网盘 App 打开分享。也可以从分享页打开 App。
2. 登录后选择 Standard、Guard 或 Lite，保存到自己的网盘。
3. 从网盘下载 APK，按[安装教程](INSTALL.md)安装到电视。

保留原分享链接。新版上传后，打开同一分享即可查看，再转存需要的安装包。

通过此链接下载，维护者可能获得推广收益。

### 官网与 GitHub 直链

首次安装可按设备选择。已在使用独立版时，选择相同类型覆盖安装即可保留设置。

| 版本 | 适合的设备 | 官网下载 | GitHub 备用 |
| :--- | :--- | :--- | :--- |
| **Standard** | Android 5.0+，大多数电视优先尝试 | [APK](https://halo-tv.pages.dev/updates/HaloTV-3.6-standard.apk) | [APK](https://github.com/Null9797/halo-tv/releases/download/v3.6-halo/HaloTV-3.6-standard.apk) |
| **Guard** | Android 5.0+，可尝试用于限制第三方桌面的固件 | [APK](https://halo-tv.pages.dev/updates/HaloTV-3.6-guard.apk) | [APK](https://github.com/Null9797/halo-tv/releases/download/v3.6-halo/HaloTV-3.6-guard.apk) |
| **Lite** | Android 4.0+，老旧或低配置设备 | [APK](https://halo-tv.pages.dev/updates/HaloTV-3.6-lite.apk) | [APK](https://github.com/Null9797/halo-tv/releases/download/v3.6-halo/HaloTV-3.6-lite.apk) |

[安装教程](INSTALL.md) · [3.6 正式版](https://github.com/Null9797/halo-tv/releases/tag/v3.6-halo) · [最新正式版](https://github.com/Null9797/halo-tv/releases/latest) · [SHA-256 校验值](docs/releases/SHA256SUMS-3.6.txt)

电视端可通过「控制中心 → 软件更新」获取新版，优先从官网下载，失败时尝试 GitHub。Standard 和 Guard 使用同一个包名，二选一。Lite 使用独立包名，Android 5.0 及以上支持主动开启轻量桌面守护。

## 日常体验

- **桌面灵动岛**（Standard / Guard）显示后台音乐、手机上传与更新进度，可设在左下、顶部居中或右上。
- **自定义桌面**提供玻璃 Dock、两种图标圆弧、焦点样式、时钟天气及壁纸与屏保设置。
- **遥控器与家人使用**支持快捷控制中心、儿童名单与趣味答题、长辈大图标和休息提醒。
- **手机与电视互联**可在同一网络下扫码设置、传输媒体或推送通过校验的更新包。

## 实机画面

| 控制中心 | 桌面灵动岛设置 | 儿童趣味答题 |
| :---: | :---: | :---: |
| [![控制中心](website/images/showcase/control.jpg)](website/images/showcase/control.jpg) | [![桌面灵动岛设置](website/images/showcase/settings.jpg)](website/images/showcase/settings.jpg) | [![儿童趣味答题](website/images/showcase/quiz.jpg)](website/images/showcase/quiz.jpg) |

[全部实拍](docs/GALLERY.md) · [翻页时钟](website/images/showcase/flip.jpg) · [静态壁纸](website/images/showcase/wallpaper.jpg) · [动态壁纸](website/images/showcase/wallpaper-dynamic.jpg)

实机图集原图为 1920 × 1080，包含历次构建的画面。界面随电视和个人设置而异。

## 3.6 更新内容

### 新增功能

- **桌面快捷栏** 可从信号源、网络、清理后台、电源和更换壁纸中选最多 3 项。快捷图标和设置图标一起常驻、淡出或隐藏。
- **一键换壁纸** 从桌面快捷栏或控制中心直接随机换同类型壁纸。Standard／Guard 支持静态和动态壁纸，Lite 支持静态壁纸。
- **家长出题** 三版均支持在手机「儿童与长辈 → 家长出题」验证密码后自建、导入和导出题库。最多 6 套、合计 80 题，答题优先使用选中的题库。 [#33](https://github.com/Null9797/halo-tv/issues/33)
- **儿童与长辈模式** 支持开机进入指定模式。已配置并设置家长密码后，可从普通桌面的控制中心直接进入，退出仍需验证家长密码。
- **灵动岛音乐面板** Standard／Guard 选中音乐胶囊后长按确认键，可播放、暂停和切歌。
- **更新提醒** 检测到可用新版时，控制中心「软件更新」显示橙色提醒点。

### 优化与修复

- **手机管理中心** 放大桌面预览，集中显示上传、安装包推送、打赏和诊断反馈入口。按桌面、壁纸、图标、家庭等分类设置电视。
- **控制中心与公告** 调整家庭模式和关于入口。打赏、联系作者和 GitHub 反馈入口集中展示，普通和重要公告在主桌面弹窗提醒。
- **儿童答题** 弹题前尝试暂停前台播放器，答完由用户自行恢复。优化跨午夜计时、遥控器操作及长题干和选项显示。
- **日常稳定性** 改善快捷栏焦点、大时钟避让、壁纸切换和预览刷新，补强下载中断恢复和已下载更新包的保留逻辑。
- **电视应用图标** 适配搜剧 TV 和看剧 AI TV 的横向卡片，保留已选择的自定义图标。 [#66](https://github.com/Null9797/halo-tv/issues/66)
- **本地视频冷启动** Standard／Guard 补强暴风 MST_6A838 对本地 SDR 视频轨道的识别和首帧诊断，两份实验素材仍待原机复测。 [#58](https://github.com/Null9797/halo-tv/issues/58)
- **创维桌面守护** Standard／Guard 增加创维 85A5F Mini 实体 Home 键所打开的系统桌面识别，同步改进守护诊断工具。待原机复测。 [#78](https://github.com/Null9797/halo-tv/issues/78)
- **当贝黑屏排查** Standard／Guard 新增启动无窗口焦点的诊断记录，方便定位 DBSmart1 首次打开黑屏。 [#79](https://github.com/Null9797/halo-tv/issues/79)

Standard / Guard 内部号 `292`，Lite `137`。 [完整更新说明](docs/releases/RELEASE-3.6.md) · [累计更新记录](RELEASE_NOTES.md) · [构建验证](docs/releases/VERIFICATION-3.6.json)

## 安装帮助与问题反馈

[常见问题](FAQ.md) · [守护诊断工具](docs/HALO_GUARD_TOOL.md) · [文档目录](docs/README.md) · [官网更新与守护指引](https://halo-tv.pages.dev/help/update-and-setup.html)

独立版可以与 Aerial 共存，权限与数据各自独立。同一时间建议只启用一个桌面守护。旧包无法通过独立版覆盖，3.2.4 起移除了旧版配置导入。默认桌面、开机启动和守护效果由厂商固件与授权共同决定。

先查阅 [现有 GitHub Issues](https://github.com/Null9797/halo-tv/issues)，再 [提交问题](https://github.com/Null9797/halo-tv/issues/new?template=bug_report.yml)。请附上电视型号、Android 版本、HaloTV 版本、安装类型和复现步骤。

## 开源与致谢

- 上游为 [pengchujin/aerial-tv](https://github.com/pengchujin/aerial-tv)。请参阅 [LICENSE](LICENSE) 和 [NOTICE](docs/NOTICE.md)。
- Bing 壁纸归档由 [YanGN](https://github.com/ygnstudio/bing_wallpaper_archive) 提供。在线媒体目录参考 [Aerial Views](https://github.com/theothernt/AerialViews)，视频来自 Apple。媒体版权归各权利人所有。
- HaloTV 与 Aerial 原作者、Apple 或电视厂商无隶属或背书关系。

[3.6 完整应用源码](https://github.com/Null9797/halo-tv/releases/download/v3.6-halo/HaloTV-3.6-source.zip) · [全部历史版本](https://github.com/Null9797/halo-tv/releases)
