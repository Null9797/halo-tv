# HaloTV 3.5.2 正式版

- **Standard／Guard** 优化 Android 5/6 本地视频壁纸冷启动。首帧交接前保持静态封面，封面未就绪时使用不透明兜底。新增封面交接诊断，暴风电视需复测断电启动。 [#58](https://github.com/Null9797/halo-tv/issues/58)
- **Standard／Guard** 为识别到 4K 输出及厂商 HEVC 解码器、但系统未报告 4K 支持的 Android 5/6 设备加入「试播 4K SDR」。自动档沿用设备能力判断。手动试播解码失败、首帧超时或持续掉帧时回退到 1080p。小米盒子 3 Pro 待实机验证。 [#55](https://github.com/Null9797/halo-tv/issues/55)
- **Standard／Guard** 儿童答题出现时，可请求支持 Android 媒体会话的前台播放器暂停。答题结束回原应用后，尝试继续同一播放内容。需开启通知使用权。
- **全版本** 将日期、星期和农历并排放在时间下方，适配左侧、右侧与居中布局。应用图标填满底板，去掉图标上的版本号。
- **Lite** 加入在线图片屏保，支持缓存轮播。原普通时钟配置自动切换为翻页时钟。电视端和手机扫码页均可设设置图标位置。
- **Lite** 加入可选桌面守护和状态诊断，Android 5.0 及以上可主动授权。Lite 本体仍支持 Android 4.0 及以上，守护实际效果取决于电视固件。

Standard／Guard 内部号 **278**，Lite **125**。沿用独立版包名和签名，可按原版别覆盖升级。

感谢 Aerial 原作者、开源贡献者和提供复测反馈的用户。 [Aerial 项目](https://github.com/pengchujin/aerial-tv) · [HaloTV 官网](https://halo-tv.pages.dev/)
