# HaloTV 3.5.4 正式版

- **遥控器 · 三版** 主桌面、设置和弹窗会过滤同一次短按产生的重复方向信号，保留快按和长按连续移动。
- **在线视频预览 · Standard／Guard** 在图库窗口内独立合成预览，打开图库时隐藏下层扫码面板。换片时保留对应封面，补齐老系统的 HTTPS 分段读取。预览亮度待小米盒子原机对比。 [#56](https://github.com/Null9797/halo-tv/issues/56)
- **旧盒子 4K 壁纸 · Standard／Guard** Android 5／6 手动试播 4K 时，有效封面保留到首帧，减少从其他应用返回桌面时的黑屏。 [#55](https://github.com/Null9797/halo-tv/issues/55)
- **本地视频冷启动 · Standard／Guard** 暴风 MST_6A838 在适用的 SDR 视频上等应用窗口收到实际视频帧再撤封面，解码失败时回退。 [#58](https://github.com/Null9797/halo-tv/issues/58)
- **全部应用背景 · Standard／Guard** 拦截带异常右侧绿条的壁纸静帧，避免把绿条带入全部应用背景。播放中的绿条待原机复测。 [#54](https://github.com/Null9797/halo-tv/issues/54)
- **必应图片屏保** 优化旧 Android 的 HTTPS 连接。Standard／Guard 在归档源失败时尝试必应日图，Lite 同步连接兼容修正。 [#76](https://github.com/Null9797/halo-tv/issues/76)
- **Aerial 2.17 整合** 合入桌面守护的前台识别、小米背光、海尔信号源、Sony 静音状态和部分应用图标等兼容改进。

Standard／Guard 内部号 **281**，Lite **128**。升级请选择电视当前使用的版别。三版共 1,607 项主机测试通过，另有 31 项守护工具测试通过。上述机型问题仍需原机复测。

感谢 Aerial 原作者和提供复测资料的用户。 [HaloTV 官网](https://halo-tv.pages.dev/)
