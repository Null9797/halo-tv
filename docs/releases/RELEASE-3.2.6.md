# HaloTV 3.2.6 · 恢复紧凑 Dock

修复 3.2.5 中选择“App 名称 → 只显示选中”后，Dock 图标底部多出大块留白的问题。Standard、Guard、Lite 同步修正。

## 本次调整

- “只显示选中”恢复旧版紧凑 Dock，不再为图标底部额外预留整行名称空间；双排 Dock 同步恢复紧凑间距。
- “全部显示”继续保留图标下方名称区域；“大标题”继续在 Dock 上方显示名称，三种模式独立选择。
- 保留 3.2.5 的更新下载及安装兼容、系统设置入口、遥控器公告翻页与全屏阅读等修复。

## 升级说明

Standard / Guard 内部号 **226**，Lite **82**，高于 3.2.5 正式包及 Dock 修复测试包（225 / 81）。使用原独立包名与发布签名，选择与当前类型一致的安装包覆盖升级，无需卸载，保留应用数据、Logo 和启动图。

电视进入“控制中心 → 软件更新 → 检查更新”获取新版，官网下载优先、GitHub 备用，安装仍需电视确认。若旧版更新器下载或安装失败，可从官网下载同类型 APK，通过手机推送、U 盘或 ADB 安装。

## 检查范围

三个 Release 构建、**1,105 项主机测试**（Standard 476、Guard 476、Lite 153）通过；Lint 无 Error/Fatal，仍有警告。安装包签名、包名、版本、ZIP 完整性、对齐及完整版 dex 元数据通过检查。

按要求未运行模拟器或操作电视，画面及厂商兼容效果仍需真机反馈。本次未新增远程公告，现有公告内容与发送范围保持不变。

## 下载与开源

Standard / Guard 最低 Android 5.0，同包名、二选一；Lite 最低 Android 4.0。完整应用源码见附件 `HaloTV-3.2.6-source.zip`，校验值见 `SHA256SUMS-3.2.6.txt`。GitHub 自动生成的 Source code 为发布材料仓库快照。

HaloTV 基于 [Aerial](https://github.com/pengchujin/aerial-tv) 二次开发，非上游官方发行版；沿用此前整合的 Aerial 1.98 基础，感谢原作者与贡献者，保留原版权及 MIT 许可。Bing 壁纸归档由 YanGN 提供，视频目录参考 Aerial Views，媒体版权归各权利人。

[官方网站](https://halo-tv.pages.dev/#download) · [项目仓库](https://github.com/Null9797/halo-tv) · [网盘](https://pan.quark.cn/s/a14e3ab2dd41)（内容以实际页面为准）
