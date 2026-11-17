<p align="center"><img src="screenshots/halo-independent-3.1.png" width="128" alt="HaloTV Logo"></p>
<h1 align="center">HaloTV · 3.3.2 正式版</h1>
<p align="center">让电视桌面，回到你喜欢的样子。</p>
<p align="center"><a href="https://halo-tv.pages.dev/">官方网站</a> · <a href="https://github.com/Null9797/halo-tv/releases/tag/v3.3.2-halo">3.3.2 正式版</a> · <a href="https://github.com/Null9797/halo-tv/releases/latest">最新正式版</a> · <a href="INSTALL.md">安装教程</a></p>

**HaloTV 基于 [Aerial](https://github.com/pengchujin/aerial-tv) 二次开发，由 Null_ 整理发布，非 Aerial 原作者或官方发行版。感谢原作者和所有开源贡献者。保留原版权与 MIT 许可，免费分享。**

## 3.3.2 正式发布

三版同步采用全新浅色静态欢迎页：手写「你好」、HaloTV 品牌光环与清晰的 Aerial 致谢。打开即完整展示，按一次遥控器确认进入桌面；完成状态会保存，后续正常启动和更新不会反复弹出。

保留 3.3.1 的「公告与反馈」及已启用的私密反馈服务，可主动提交问题、扫码补充描述/图片、查看作者回复。上传前由用户确认，不自动截屏、不常驻上传或轮询。

Standard / Guard 内部号 **241**，Lite **97**，可覆盖同类型独立版及欢迎页测试包（239/95、240/96），保留设置、上传素材、独立签名与启动图。三版构建、**1,231 项主机测试**通过，Lint 无 Error/Fatal（仍有警告），签名和安装包完整性已核验。本轮未操作电视或模拟器。[完整更新与验证范围](docs/releases/RELEASE-3.3.2.md)

![HaloTV 3.3.2 静态欢迎页原生绘制预览](website/images/welcome-3.3.2.jpg)

欢迎页为电脑原生绘制预览，真机字体与固件兼容仍需实际使用验证。

## 下载

**3.3.2 已进入正式在线更新通道：官网下载优先，GitHub 备用。也可手动下载覆盖安装。**

| 类型 | 官网下载 | GitHub 备用 | 适用范围 |
|---|---|---|---|
| Standard | [下载](https://halo-tv.pages.dev/updates/HaloTV-3.3.2-standard.apk) | [下载](https://github.com/Null9797/halo-tv/releases/download/v3.3.2-halo/HaloTV-3.3.2-standard.apk) | Android 5.0+，优先尝试 |
| Guard | [下载](https://halo-tv.pages.dev/updates/HaloTV-3.3.2-guard.apk) | [下载](https://github.com/Null9797/halo-tv/releases/download/v3.3.2-halo/HaloTV-3.3.2-guard.apk) | Android 5.0+，限制第三方 HOME 的固件可尝试 |
| Lite | [下载](https://halo-tv.pages.dev/updates/HaloTV-3.3.2-lite.apk) | [下载](https://github.com/Null9797/halo-tv/releases/download/v3.3.2-halo/HaloTV-3.3.2-lite.apk) | Android 4.0+，老设备；不含完整版动态桌面 |

Standard 与 Guard 同包名、二选一；升级选择与当前一致的类型。Lite 使用另一包名。安装新版独立版时保留现有应用数据，无需先卸载。

## 独立版与使用说明

从 3.2.4 起已移除旧版/过渡版配置导入，不再维护跨包迁移流程。旧版本说明仅作为历史资料保留；旧包名不能通过新 APK 原地覆盖。独立版可以与 Aerial 共存，系统权限和私有数据各自独立。请勿同时启用两个桌面守护。

- 玻璃 Dock、大/小圆弧图标、经典玻璃滑动焦点与自定义图标。
- 可调整位置的时间、日期、农历和天气，翻页时钟及屏保。
- 儿童应用名单、观看限额与趣味答题；长辈大图标和休息提醒。
- 手机同网扫码管理、上传素材与验证后的更新包推送。
- 在线更新、性能模式及常用系统入口；具体能力受电视系统限制。

![HaloTV 桌面](screenshots/home-3.0.jpg)

3.0 系列实机素材展示现有功能；部分画面保留采集时的版本编号，实际外观依用户设置而定。

[安装教程](INSTALL.md) · [常见问题](FAQ.md) · [守护诊断工具](docs/HALO_GUARD_TOOL.md) · [累计更新记录](RELEASE_NOTES.md)

厂商对默认桌面、开机启动和无障碍守护的限制不同，不能保证所有电视零闪烁或守护永久有效。请按当前独立包名配置权限；不要用上游 Aerial 的安装脚本给 HaloTV 授权。

## 开源与致谢

- 基于 [pengchujin/aerial-tv](https://github.com/pengchujin/aerial-tv)，感谢 Aerial 原作者和贡献者；保留 [LICENSE](LICENSE) 与 [NOTICE](NOTICE.md)。
- Bing 壁纸归档由 [YanGN](https://github.com/ygnstudio/bing_wallpaper_archive) 提供。
- 在线视频目录参考 [Aerial Views](https://github.com/theothernt/AerialViews)，视频来自 Apple；媒体版权归各权利人，代码许可不代替素材授权。
- 与 Aerial 原作者、Apple、电视厂商无隶属或背书关系。
- [3.3.2 完整应用源码](https://github.com/Null9797/halo-tv/releases/download/v3.3.2-halo/HaloTV-3.3.2-source.zip) · [3.3.2 文件校验值](docs/releases/SHA256SUMS-3.3.2.txt)。不公开签名私钥。

完整源码与安装包放在 [Releases](https://github.com/Null9797/halo-tv/releases)，历史版本仍可查阅；[文档目录](docs/README.md) 汇总说明。

[官方网站](https://halo-tv.pages.dev/) · [网盘](https://pan.quark.cn/s/a14e3ab2dd41)（实际内容以网盘为准）
