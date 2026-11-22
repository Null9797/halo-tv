<div align="center">
  <img src="website/images/brand/halotv.png" alt="HaloTV Logo" width="120" height="120">
  <h1>HaloTV</h1>
  <p><strong>你的电视，你的桌面。</strong></p>
  <p>免费开源的 Android TV 桌面 · 3.5.2 正式版</p>
  <p><a href="https://halo-tv.pages.dev/"><strong>官方网站</strong></a> · <a href="#下载与安装"><strong>下载与安装</strong></a> · <a href="docs/README.md">文档</a> · <a href="https://github.com/Null9797/halo-tv/issues">Issues</a> · <a href="docs/README.en.md">English</a></p>
</div>

[![HaloTV 主桌面实拍，展示电视上的玻璃 Dock、壁纸与音乐灵动岛](website/images/showcase/main.jpg)](website/images/showcase/main.jpg)

HaloTV 基于 [Aerial](https://github.com/pengchujin/aerial-tv) 二次开发，由 Null_ 整理发布。感谢原作者与所有开源贡献者，保留原版权和 [MIT 许可](LICENSE)。

<a name="下载"></a>

## 下载与安装

首次安装可按设备选择。已在使用独立版时，选择相同类型覆盖安装即可保留设置。

| 版本 | 适合的设备 | 官网下载 | GitHub 备用 |
| :--- | :--- | :--- | :--- |
| **Standard** | Android 5.0+，大多数电视优先尝试 | [APK](https://halo-tv.pages.dev/updates/HaloTV-3.5.2-standard.apk) | [APK](https://github.com/Null9797/halo-tv/releases/download/v3.5.2-halo/HaloTV-3.5.2-standard.apk) |
| **Guard** | Android 5.0+，可尝试用于限制第三方桌面的固件 | [APK](https://halo-tv.pages.dev/updates/HaloTV-3.5.2-guard.apk) | [APK](https://github.com/Null9797/halo-tv/releases/download/v3.5.2-halo/HaloTV-3.5.2-guard.apk) |
| **Lite** | Android 4.0+，老旧或低配置设备 | [APK](https://halo-tv.pages.dev/updates/HaloTV-3.5.2-lite.apk) | [APK](https://github.com/Null9797/halo-tv/releases/download/v3.5.2-halo/HaloTV-3.5.2-lite.apk) |

[安装教程](INSTALL.md) · [3.5.2 正式版](https://github.com/Null9797/halo-tv/releases/tag/v3.5.2-halo) · [最新正式版](https://github.com/Null9797/halo-tv/releases/latest) · [SHA-256 校验值](docs/releases/SHA256SUMS-3.5.2.txt) · [网盘](https://pan.quark.cn/s/a14e3ab2dd41)（以网盘页面显示为准）

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

图集采集自 HaloTV 3.5 系列测试构建，原图为 1920 × 1080。界面随电视和个人设置而异。

## 3.5.2 更新内容

- **Standard／Guard** 优化 Android 5/6 本地视频壁纸冷启动。首帧交接前保持静态封面，封面未就绪时使用不透明兜底。新增封面交接诊断，暴风电视需复测断电启动。 [#58](https://github.com/Null9797/halo-tv/issues/58)
- **Standard／Guard** 为识别到 4K 输出及厂商 HEVC 解码器、但系统未报告 4K 支持的 Android 5/6 设备加入「试播 4K SDR」。自动档沿用设备能力判断。手动试播解码失败、首帧超时或持续掉帧时回退到 1080p。小米盒子 3 Pro 待实机验证。 [#55](https://github.com/Null9797/halo-tv/issues/55)
- **Standard／Guard** 儿童答题出现时，可请求支持 Android 媒体会话的前台播放器暂停。答题结束回原应用后，尝试继续同一播放内容。需开启通知使用权。
- **全版本** 将日期、星期和农历并排放在时间下方，适配左侧、右侧与居中布局。应用图标填满底板，去掉图标上的版本号。
- **Lite** 加入在线图片屏保，支持缓存轮播。原普通时钟配置自动切换为翻页时钟。电视端和手机扫码页均可设设置图标位置。
- **Lite** 加入可选桌面守护和状态诊断，Android 5.0 及以上可主动授权。Lite 本体仍支持 Android 4.0 及以上，守护实际效果取决于电视固件。

Standard / Guard 内部号 `278`，Lite `125`。 [完整更新说明](docs/releases/RELEASE-3.5.2.md) · [累计更新记录](RELEASE_NOTES.md) · [构建验证](docs/releases/VERIFICATION-3.5.2.json)

## 安装帮助与问题反馈

[常见问题](FAQ.md) · [守护诊断工具](docs/HALO_GUARD_TOOL.md) · [文档目录](docs/README.md) · [官网更新与守护指引](https://halo-tv.pages.dev/help/update-and-setup.html)

独立版可以与 Aerial 共存，权限与数据各自独立。同一时间建议只启用一个桌面守护。旧包无法通过独立版覆盖，3.2.4 起移除了旧版配置导入。默认桌面、开机启动和守护效果由厂商固件与授权共同决定。

先查阅 [现有 GitHub Issues](https://github.com/Null9797/halo-tv/issues)，再 [提交问题](https://github.com/Null9797/halo-tv/issues/new?template=bug_report.yml)。请附上电视型号、Android 版本、HaloTV 版本、安装类型和复现步骤。

## 开源与致谢

- 上游为 [pengchujin/aerial-tv](https://github.com/pengchujin/aerial-tv)。请参阅 [LICENSE](LICENSE) 和 [NOTICE](docs/NOTICE.md)。
- Bing 壁纸归档由 [YanGN](https://github.com/ygnstudio/bing_wallpaper_archive) 提供。在线媒体目录参考 [Aerial Views](https://github.com/theothernt/AerialViews)，视频来自 Apple。媒体版权归各权利人所有。
- HaloTV 与 Aerial 原作者、Apple 或电视厂商无隶属或背书关系。

[3.5.2 完整应用源码](https://github.com/Null9797/halo-tv/releases/download/v3.5.2-halo/HaloTV-3.5.2-source.zip) · [全部历史版本](https://github.com/Null9797/halo-tv/releases)
