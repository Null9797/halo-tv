# HaloTV 3.1.1

本次提供 Standard、Guard、Lite 三个安装包，统一采用 HaloTV 新包名与专属发布签名。文件名不再含 independent。已安装 3.1 独立版的用户可覆盖升级；旧包名用户请先使用 3.1 过渡版完成迁移，不能把新包名当作旧应用的原地覆盖。

## 修复与调整
- 手机端天气：改进城市输入、输入法确认、点击提交和失败重试；显示提交结果；家庭模式需要授权时可验证家长密码后继续。城市设置统一提交到 UI 线程，旧定位/天气请求不能覆盖新选择。
- 壁纸与遥控：分类内分别保存状态，重复选择当前分类不会重置滚动；选项按值保留身份，减少切换静态/动态页面时焦点错误复用。重复应用同一壁纸不再反复重建背景。
- 本地视频：缩略图不再额外打开硬件视频解码器；全屏壁纸选择页释放桌面解码器供预览使用，避免单解码通道设备争用、卡死。异步背景结果会核对当前壁纸和版本，过时画面不再覆盖新选择。
- 在线视频：明确正常播放速度，避免播放时并行解码第二份视频；玻璃背景取样减为每个视频一次。错误重试有间隔和次数限制；自动画质遇到持续严重掉帧时，可回退至 1080p，手动指定的画质保持不变。
- 新默认值：设置图标淡出、农历日期开启、经典玻璃滑动焦点、空闲自动清理开启、柔和按键声音。Lite 同步增加柔和声音与空闲清理。已保存的设置不会强制覆盖。

## 版本与兼容
- Standard / Guard：`app.halotv.launcher`，versionCode **195**，Android 5.0+。
- Lite：`app.halotv.launcher.lite`，versionCode **51**，Android 4.0+；不包含正式版动态视频桌面与 HomeGuardService。
- 三个包的 versionName 均为 **3.1.1**，与 3.1 独立版保持相同的专属签名。
- 官网优先提供更新包，GitHub 备用。官网保留 3.1 客户端旧下载路径的跳转，安装包仍需在电视上确认安装。

## 验证范围
执行 Standard、Guard、Lite 的自动测试、Android Lint、Release 编译、包名/版本/签名/ZIP/对齐校验，并验证手机天气页面的提交与失败反馈。本轮未覆盖所有电视固件的实机视频解码和遥控操作，不能保证每种设备上都完全消除卡顿。若仍异常，请反馈机型、Android 版本、安装类型和视频格式。

## 开源与来源
HaloTV 基于 [Aerial](https://github.com/pengchujin/aerial-tv) 二次开发，由 Null_ 整理与发布，非上游官方版本。感谢原作者与贡献者，保留原版权和 MIT 许可。Bing 壁纸归档由 [YanGN](https://github.com/ygnstudio/bing_wallpaper_archive) 提供；在线视频目录参考 [Aerial Views](https://github.com/theothernt/AerialViews)，视频来自 Apple，素材版权归各权利人；代码许可不代替素材授权。

[官网](https://halo-tv.pages.dev/) · [仓库](https://github.com/Null9797/halo-tv) · [网盘](https://pan.quark.cn/s/a14e3ab2dd41)
