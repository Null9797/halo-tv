<div align="center">
  <img src="website/images/brand/halotv.png" alt="HaloTV Logo" width="120" height="120">
  <h1>HaloTV</h1>
  <p><strong>你的电视，你的桌面。</strong></p>
  <p>免费开源的 Android TV 桌面 · 3.6.1 正式版</p>
  <p><a href="https://halo-tv.pages.dev/"><strong>官方网站</strong></a> · <a href="#夸克网盘下载"><strong>网盘下载</strong></a> · <a href="#下载与安装"><strong>下载与安装</strong></a> · <a href="docs/README.md">文档</a> · <a href="https://github.com/Null9797/halo-tv/issues">Issues</a> · <a href="docs/README.en.md">English</a></p>
</div>

[![HaloTV 主桌面实拍，展示电视上的桌面快捷栏、玻璃 Dock 与音乐灵动岛](website/images/showcase/main.jpg)](website/images/showcase/main.jpg)

HaloTV 基于 [Aerial](https://github.com/pengchujin/aerial-tv) 二次开发，由 Null_ 整理发布。感谢原作者与所有开源贡献者，保留原版权和 [MIT 许可](LICENSE)。

<a name="下载"></a>

## 下载与安装

### 夸克网盘下载

[打开夸克网盘分享](https://pan.quark.cn/s/96c264d59e08) · [到官网一键复制分享内容](https://halo-tv.pages.dev/#quark-download)

```text
我用夸克网盘给你分享了「HaloTV 电视桌面软件」，点击链接或复制整段内容，打开「夸克APP」即可获取。
/~6e093cYlwa~:/
链接：https://pan.quark.cn/s/96c264d59e08
```

1. 复制上方整段分享内容，打开夸克 App 查看。也可以直接打开分享页。
2. 登录后选择 Standard、Guard 或 Lite，保存到自己的网盘。
3. 从网盘下载 APK，按[安装教程](INSTALL.md)安装到电视。

保留原分享链接，之后可回去查看已上传的新版。转存前先核对 APK 版本，网盘尚未更新时可用下方直链下载当前正式版。

### 官网与 GitHub 直链

首次安装可按设备选择。已在使用独立版时，选择相同类型覆盖安装即可保留设置。

| 版本 | 适合的设备 | 官网下载 | GitHub 备用 |
| :--- | :--- | :--- | :--- |
| **Standard** | Android 5.0+，大多数电视优先尝试 | [APK](https://halo-tv.pages.dev/updates/HaloTV-3.6.1-standard.apk) | [APK](https://github.com/Null9797/halo-tv/releases/download/v3.6.1-halo/HaloTV-3.6.1-standard.apk) |
| **Guard** | Android 5.0+，可尝试用于限制第三方桌面的固件 | [APK](https://halo-tv.pages.dev/updates/HaloTV-3.6.1-guard.apk) | [APK](https://github.com/Null9797/halo-tv/releases/download/v3.6.1-halo/HaloTV-3.6.1-guard.apk) |
| **Lite** | Android 4.0+，老旧或低配置设备 | [APK](https://halo-tv.pages.dev/updates/HaloTV-3.6.1-lite.apk) | [APK](https://github.com/Null9797/halo-tv/releases/download/v3.6.1-halo/HaloTV-3.6.1-lite.apk) |

[安装教程](INSTALL.md) · [3.6.1 正式版](https://github.com/Null9797/halo-tv/releases/tag/v3.6.1-halo) · [最新正式版](https://github.com/Null9797/halo-tv/releases/latest) · [SHA-256 校验值](docs/releases/SHA256SUMS-3.6.1.txt)

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

## 3.6.1 更新内容

### 新增功能

- **儿童模式定时休息**　可分别设置每日总时长、单次观看时长和休息间隔。到达单次时长后，可选「强制休息」或继续使用「答题续看」。休息结束后自动解锁，单次时长或休息间隔设为 0 可关闭定时休息。电视和手机管理页均可设置。 [#82](https://github.com/Null9797/halo-tv/issues/82)

### 修复与优化

- **天气更易读**　突出当前温度，分开显示最高和最低温。自动定位匹配到城市后，城市名称和预报使用同一地点的坐标。 [#92](https://github.com/Null9797/halo-tv/issues/92)
- **本地视频壁纸**　启用壁纸声音时，等待首帧就绪后再出声。康佳 V560 冷开机的音量表现待原机复测。 [#84](https://github.com/Null9797/halo-tv/issues/84)
- **遥控器焦点**　打开设置时聚焦当前分类，首个选项按左键回到分类。改善信号源设置、隐藏应用与控制中心返回时的焦点，以及 PIN 面板和长应用文件夹的方向键操作。 [Aerial #1766](https://github.com/pengchujin/aerial-tv/issues/1766) · [Aerial #1748](https://github.com/pengchujin/aerial-tv/issues/1748)
- **动态壁纸与待机**　改善待机后的播放恢复，取帧按设备能力选择路径，减少重复读帧。 [Aerial #1759](https://github.com/pengchujin/aerial-tv/issues/1759) · [Aerial #1789](https://github.com/pengchujin/aerial-tv/issues/1789)
- **音量与电视兼容**　收到音量键松手事件时取消待执行的连调，并记录按键诊断。优化开机守护和信号源回退顺序，补充部分创维、TCL 和国美固件的兼容路径。 [Aerial #1783](https://github.com/pengchujin/aerial-tv/issues/1783) · [Aerial #1787](https://github.com/pengchujin/aerial-tv/issues/1787) · [Aerial #1712](https://github.com/pengchujin/aerial-tv/issues/1712)
- **Lite**　改善旧显卡的时钟数字显示。跨日后会继续检查尚未更新的每日壁纸。 [Aerial #1658](https://github.com/pengchujin/aerial-tv/issues/1658) · [Aerial #1750](https://github.com/pengchujin/aerial-tv/issues/1750)

Standard / Guard 内部号 `294`，Lite `139`。 [完整更新说明](docs/releases/RELEASE-3.6.1.md) · [累计更新记录](RELEASE_NOTES.md) · [构建验证](docs/releases/VERIFICATION-3.6.1.json)

## 安装帮助与问题反馈

[常见问题](FAQ.md) · [守护诊断工具](docs/HALO_GUARD_TOOL.md) · [文档目录](docs/README.md) · [官网更新与守护指引](https://halo-tv.pages.dev/help/update-and-setup.html)

独立版可以与 Aerial 共存，权限与数据各自独立。同一时间建议只启用一个桌面守护。旧包无法通过独立版覆盖，3.2.4 起移除了旧版配置导入。默认桌面、开机启动和守护效果由厂商固件与授权共同决定。

先查阅 [现有 GitHub Issues](https://github.com/Null9797/halo-tv/issues)，再 [提交问题](https://github.com/Null9797/halo-tv/issues/new?template=bug_report.yml)。请附上电视型号、Android 版本、HaloTV 版本、安装类型和复现步骤。

## 开源与致谢

- 上游为 [pengchujin/aerial-tv](https://github.com/pengchujin/aerial-tv)。请参阅 [LICENSE](LICENSE) 和 [NOTICE](docs/NOTICE.md)。
- Bing 壁纸归档由 [YanGN](https://github.com/ygnstudio/bing_wallpaper_archive) 提供。在线媒体目录参考 [Aerial Views](https://github.com/theothernt/AerialViews)，视频来自 Apple。媒体版权归各权利人所有。
- HaloTV 与 Aerial 原作者、Apple 或电视厂商无隶属或背书关系。

[3.6.1 完整应用源码](https://github.com/Null9797/halo-tv/releases/download/v3.6.1-halo/HaloTV-3.6.1-source.zip) · [全部历史版本](https://github.com/Null9797/halo-tv/releases)
