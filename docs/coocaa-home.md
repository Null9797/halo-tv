# 创维 / 酷开机型：Home 键回落到原厂桌面（Coocaa home props 补丁）

**EN (TL;DR)** — On Skyworth/Coocaa Android 8.0 TV firmware the Home key is resolved from
`persist.service.homepage.pkg` / `.cls` instead of `CATEGORY_HOME`, and the firmware rewrites
those two properties in the middle of boot. Result: a third-party launcher shows up after boot,
but pressing Home returns to the stock Coocaa home page. The patch adds `CoocaaHomeProps.claim()`
and calls it from `BootReceiver.onBoot()` and `MainActivity.onCreate()`, so the values are
re-asserted every time Halo is actually shown.

上游以源码 zip 发布，仓库里没有源码树，所以这个 PR 不带树结构改动，只提供可直接
`git apply` 的补丁 + 本文档。

## 现象

- 开机后能自动进入 Halo（Halo 自带 `guard.BootReceiver` 的 `BOOT_COMPLETED` 生效）；
- 但**按 HOME 键**会回到酷开首页，而不是 Halo；
- `setprop persist.service.homepage.pkg app.orchard.tv` 手动写入后，HOME 立刻正常，
  直到下一次开机又被改回去。

## 机型与环境

| 项 | 值 |
|---|---|
| 整机 | 创维 65B20 |
| 机型 / 设备 / 硬件 | `5S851_B20` / `sky848_9s60` / `m7221` |
| 系统 | Android 8.0.0（API 26） |
| 固件 | `021.007.060` |
| ABI | `armeabi-v7a` |
| root | 无（`su` 不存在，`adb root` 无效，`ro.build.type=user`） |

## 根因

该固件的 framework 不通过 `CATEGORY_HOME` 解析 Home，而是读两个 persist 属性：

```
persist.service.homepage.pkg
persist.service.homepage.cls
persist.service.starthomepage = 1
sky.current.apk / sky.current.actname        （同一套机制的副本）
```

原厂值：

```
com.tianci.movieplatform
com.coocaa.homepage.vast.HomePageActivity
```

复现与证据：

1. 冷启动，`/proc/uptime` 65s 时属性已经是 `app.orchard.tv`（Halo 的 `onCreate` 写过），
   此时 HOME 正常；
2. 固件在开机流程里**不止一次**改写这两个属性，某一次改写晚于 Halo 的 `onCreate`，
   之后就回落酷开首页；
3. Halo 诊断日志（`-Pdiag` 构建）里的原文：

```
home(boot): props were com.tianci.movieplatform/com.coocaa.homepage.vast.HomePageActivity, set -> app.orchard.tv
BOOT_COMPLETED handled in 32 ms
```

4. 属性直接指向 `app.orchard.tv` / `app.orchard.tv.MainActivity` 即可，**不需要中转包**
   （曾做过 `com.ccos.tv.homepage` 中转 + `com.coocaa.tvhome` 守护，均已废弃）。

## 在这台机器上已实测无效的做法（避免重复走弯路）

| 做法 | 结果 |
|---|---|
| `pm set-home-activity` / `cmd package set-home-activity` | 返回 `Success`，HOME 行为不变 |
| 自建中转包 + 守护包：开机广播、`am startservice`、延时闹钟 | 广播投递成功（`Deliver #16`），接收器不执行；`dumpsys alarm` 里 REASSERT 恒为 0 |
| `pm disable-user` 禁用酷开首页 | 被 `LaboratoryActivity` 顶替，仍然不是 Halo |
| `adb root` / `su` | 固件为 `user` 版，均不可用，且无对应 root 固件 |
| 后台直接 `startActivity` 拉起首页 | 被静默拦截 |

## 补丁内容

`patches/coocaa-home-2.1.3.patch`（基于 2.1.3 源码），共 3 个文件：

1. **新增** `app/src/main/java/app/orchard/tv/guard/CoocaaHomeProps.kt`
   - 反射 `android.os.SystemProperties` 读写两个属性（普通应用没有 `setprop` 权限，
     但 `SystemProperties.set` 在这台机器上可用，无需 root）；
   - 值已正确则直接 return，不产生无谓写入；
   - 写入后回读校验并记一条诊断日志；
   - 任何异常只记一次、绝不抛出——写属性失败不能影响开机与桌面启动。

2. `guard/BootReceiver.kt` · `onBoot()` **第一行** 调用 `claim(context, "boot")`
   - 放在 `GuardSetup.ensureEnabled()` 之前，确保后续任何分支提前 return 时属性也已写回。

3. `MainActivity.kt` · `onCreate()` 在 `DiagLog.catchCrashes()` 之后调用
   `claim(this, "onCreate")`
   - 每次 Halo 真正被显示（开机、按 HOME、从其它应用返回）都会再校正一次。

应用方式（在 2.1.3 源码树根目录）：

```bash
git apply patches/coocaa-home-2.1.3.patch
./gradlew --no-daemon -Pdiag assembleStandardRelease
```

## 验证

```bash
adb shell getprop persist.service.homepage.pkg   # app.orchard.tv
adb shell getprop persist.service.homepage.cls   # app.orchard.tv.MainActivity
adb shell am start -n app.orchard.tv/app.orchard.tv.MainActivity
adb pull /sdcard/Android/data/app.orchard.tv/files/aerial-diag.log
```

关键日志：

```
home(onCreate): props were com.tianci.movieplatform/com.coocaa.homepage.vast.HomePageActivity, set -> app.orchard.tv
```

实测结果：冷启动后可自动进入 Halo；从酷开首页按 HOME、从设置按 HOME 均回到 Halo；
断电重启后属性仍为 Halo。

## 已知残留

- 开机后**第一次**按 HOME 偶尔会落到`com.tianci.appstore.gz` 的商店首页
  （`AppStoreHomeActivityV3` / `AppDetailActivityV2`），再按一次才回 Halo。
  判断是固件在一次按键里没走属性路由，属固件行为，本补丁未覆盖。

## 合并建议（给上游）

- 本补丁为与已测 APK 保持一致，`claim()` 未做“属性非空才写”的守卫。若上游希望
  避免在非酷开机型写入两个无意义的 persist 属性，建议合并时加一行判断：
  仅当 `pkg` 当前值非空（即该固件确实使用这套机制）时才写。
- 也可考虑把 `claim()` 收进现有的 guard 配置里做成开关，默认只在酷开系机型打开。
