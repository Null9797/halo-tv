# Halo TV 2.1.3

Halo TV 由 Null_ 基于 [Aerial](https://github.com/pengchujin/aerial-tv) 开源项目二次开发，感谢原作者及贡献者。Halo TV 并非 Aerial 原作者的官方发行版。

- 改进上传视频的封面生成和显示，打开控制中心时尝试保留当前视频画面。
- 上传视频壁纸搭配翻页时钟时尝试保留暂停画面，以改善屏保进出时闪屏和短暂模糊。
- 修正壁纸画面并发保存时的临时文件冲突；补齐 Lite 部分多语言文案。
- Standard 和 Guard 各 150 项单元测试通过，Lite 单元测试及 lint 通过；已在 Android TV 模拟器验证视频上传及翻页时钟切换。新改动尚未完成实体电视回归，Android 4.x 真机尚未验证。
- Standard / Guard 面向 Android 5.0 及以上，Lite 面向 Android 4.0–4.4；受固件限制无法安装 Standard 时可尝试 Guard。Guard 的守护需按应用说明授权。
- 旧版电视端更新器兼容用 `aerial-universal` 别名，文件内容与对应 HaloTV 安装包相同。无法从电视访问 GitHub 时，可使用电脑下载后通过 U 盘安装。
- 上传视频封面和 4K 播放取决于上传设备、电视系统及解码器，并非所有设备均可保证效果。
