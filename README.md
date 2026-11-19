<p align="center"><img src="screenshots/halo-independent-3.1.png" width="128" alt="HaloTV Logo"></p>
<h1 align="center">HaloTV · 3.3.7 正式版</h1>
<p align="center">让电视桌面，回到你喜欢的样子。</p>
<p align="center"><a href="https://halo-tv.pages.dev/">官方网站</a> · <a href="https://github.com/Null9797/halo-tv/releases/tag/v3.3.7-halo">3.3.7 正式版</a> · <a href="https://github.com/Null9797/halo-tv/releases/latest">最新正式版</a> · <a href="INSTALL.md">安装教程</a></p>

**HaloTV 基于 [Aerial](https://github.com/pengchujin/aerial-tv) 二次开发，由 Null_ 整理发布，非 Aerial 原作者或官方发行版。感谢原作者和所有开源贡献者。保留原版权与 MIT 许可，免费分享。**

## 3.3.7 更新内容

- **在线动态壁纸与屏保**：Android 5.0–6.0 不再一律限制为 1080p。会检测 4K SDR HEVC 解码能力；无法解码或播放失败时可回退，诊断会显示选项、实际片源分辨率与回退原因。桌面画布不变。对应 [#55](https://github.com/Null9797/halo-tv/issues/55)。
- **Dock**：静态与动态壁纸下，液态玻璃底板更通透。动态壁纸直接透出视频，只用已有取样缓慢调整淡色，不增加取帧。与 [#52](https://github.com/Null9797/halo-tv/issues/52) 相关，仅调整通透和配色，未加入实时折射。
- **桌面流畅度**：切换应用排数时共用位移动画，动态壁纸取帧避开切排过程。
- **儿童模式**：修正观看计时在前后台切换时的计算。到点后用已有权限尝试显示答题；系统不允许时按情况提醒，手动回桌面仍可答题。

Standard / Guard 内部号 `263`，Lite `117`。沿用独立包名和签名，可覆盖同类型独立版并保留数据。Lite 使用系统默认桌面。

已完成主机回归，厂商固件相关表现仍待真机确认。[完整更新说明](docs/releases/RELEASE-3.3.7.md) · [构建与代码检查](docs/releases/VERIFICATION-3.3.7.json)

## 下载

**3.3.7 已进入正式在线更新通道：官网下载优先，GitHub 备用。也可手动下载覆盖安装。**

| 类型 | 官网下载 | GitHub 备用 | 适用范围 |
|---|---|---|---|
| Standard | [下载](https://halo-tv.pages.dev/updates/HaloTV-3.3.7-standard.apk) | [下载](https://github.com/Null9797/halo-tv/releases/download/v3.3.7-halo/HaloTV-3.3.7-standard.apk) | Android 5.0+，优先尝试 |
| Guard | [下载](https://halo-tv.pages.dev/updates/HaloTV-3.3.7-guard.apk) | [下载](https://github.com/Null9797/halo-tv/releases/download/v3.3.7-halo/HaloTV-3.3.7-guard.apk) | Android 5.0+，限制第三方 HOME 的固件可尝试 |
| Lite | [下载](https://halo-tv.pages.dev/updates/HaloTV-3.3.7-lite.apk) | [下载](https://github.com/Null9797/halo-tv/releases/download/v3.3.7-halo/HaloTV-3.3.7-lite.apk) | Android 4.0+，老设备；不含完整版动态桌面 |

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
- [3.3.7 完整应用源码](https://github.com/Null9797/halo-tv/releases/download/v3.3.7-halo/HaloTV-3.3.7-source.zip) · [3.3.7 文件校验值](docs/releases/SHA256SUMS-3.3.7.txt)。不公开签名私钥。

完整源码与安装包放在 [Releases](https://github.com/Null9797/halo-tv/releases)，历史版本仍可查阅；[文档目录](docs/README.md) 汇总说明。

[官方网站](https://halo-tv.pages.dev/) · [网盘](https://pan.quark.cn/s/a14e3ab2dd41)（实际内容以网盘为准）

## 问题反馈

请先查阅 [现有 GitHub Issues](https://github.com/Null9797/halo-tv/issues)，再[提交问题](https://github.com/Null9797/halo-tv/issues/new?template=bug_report.yml)。请附上电视型号、Android 版本、HaloTV 版本、安装类型和复现步骤。
