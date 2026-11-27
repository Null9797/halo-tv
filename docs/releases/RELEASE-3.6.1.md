# HaloTV 3.6.1 正式版

## 新增功能

- **儿童模式定时休息**　可分别设置每日总时长、单次观看时长和休息间隔。到达单次时长后，可选「强制休息」或继续使用「答题续看」。休息结束后自动解锁，单次时长或休息间隔设为 0 可关闭定时休息。电视和手机管理页均可设置。 [#82](https://github.com/Null9797/halo-tv/issues/82)

## 修复与优化

- **天气更易读**　突出当前温度，分开显示最高和最低温。自动定位匹配到城市后，城市名称和预报使用同一地点的坐标。 [#92](https://github.com/Null9797/halo-tv/issues/92)
- **本地视频壁纸**　启用壁纸声音时，等待首帧就绪后再出声。康佳 V560 冷开机的音量表现待原机复测。 [#84](https://github.com/Null9797/halo-tv/issues/84)
- **遥控器焦点**　打开设置时聚焦当前分类，首个选项按左键回到分类。改善信号源设置、隐藏应用与控制中心返回时的焦点，以及 PIN 面板和长应用文件夹的方向键操作。 [Aerial #1766](https://github.com/pengchujin/aerial-tv/issues/1766) · [Aerial #1748](https://github.com/pengchujin/aerial-tv/issues/1748)
- **动态壁纸与待机**　改善待机后的播放恢复，取帧按设备能力选择路径，减少重复读帧。 [Aerial #1759](https://github.com/pengchujin/aerial-tv/issues/1759) · [Aerial #1789](https://github.com/pengchujin/aerial-tv/issues/1789)
- **音量与电视兼容**　收到音量键松手事件时取消待执行的连调，并记录按键诊断。优化开机守护和信号源回退顺序，补充部分创维、TCL 和国美固件的兼容路径。 [Aerial #1783](https://github.com/pengchujin/aerial-tv/issues/1783) · [Aerial #1787](https://github.com/pengchujin/aerial-tv/issues/1787) · [Aerial #1712](https://github.com/pengchujin/aerial-tv/issues/1712)
- **Lite**　改善旧显卡的时钟数字显示。跨日后会继续检查尚未更新的每日壁纸。 [Aerial #1658](https://github.com/pengchujin/aerial-tv/issues/1658) · [Aerial #1750](https://github.com/pengchujin/aerial-tv/issues/1750)

本版整合了 Aerial 2.19、2.20、2.21 的应用端改动及 2.18 的衔接补丁。 [上游版本记录](https://github.com/pengchujin/aerial-tv/releases)

升级请选择当前已安装的版别。Standard／Guard 内部版本号为 294，Lite 为 139。三版通过签名校验和 Android TV 模拟器复测，1,839 项单元测试通过。厂商实体遥控和 HDMI-CEC 的表现仍以真机验证为准。 [HaloTV 官网下载](https://halo-tv.pages.dev/#download)
