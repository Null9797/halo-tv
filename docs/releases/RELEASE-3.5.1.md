# HaloTV 3.5.1 正式版

- 修复壁纸页按 Home 返回时短暂闪出设置页的问题。普通入口重开后回到「静态壁纸」，本地照片和视频快捷入口保留各自的定位。 [#69](https://github.com/Null9797/halo-tv/issues/69) · [#71](https://github.com/Null9797/halo-tv/issues/71)
- 修复 Android 5.0–5.1 的翻页时钟大数字可能不显示的问题。 [#72](https://github.com/Null9797/halo-tv/issues/72)
- 修复切换动态壁纸后 Dock 和菜单继续沿用上一部影片的玻璃配色。 [#63](https://github.com/Null9797/halo-tv/issues/63)
- 补齐 Android 5/6 上 Apple 在线视频缩略图所需的证书信任。预览偏暗或串入二维码仍待确认。 [#56](https://github.com/Null9797/halo-tv/issues/56)
- 合入 Aerial 2.15 的手机图标库搜索、网格展示和部分机型兼容改进，清理已停用的实验性刷新率代码。

Standard / Guard 内部号 **274**，Lite **121**。三版沿用独立包名和签名，按原版别覆盖升级即可保留设置。三版共通过 1,536 项主机单测，并在 Android TV 模拟器验证同版别覆盖安装。暴风电视冷开机残影和老盒子的在线 4K 协商继续等待对应机型复测。 [#58](https://github.com/Null9797/halo-tv/issues/58) · [#55](https://github.com/Null9797/halo-tv/issues/55)

感谢 Aerial 原作者、开源贡献者和提供日志与录屏的用户。 [Aerial 项目](https://github.com/pengchujin/aerial-tv) · [HaloTV 官网](https://halo-tv.pages.dev/)
