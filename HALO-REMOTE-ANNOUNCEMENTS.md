# HaloTV 远程公告使用说明

HaloTV 3.0 系列包含公告能力。此功能是文字通知，不是远程执行代码或静默安装；没有内置公告功能的更早版本不能接收弹窗。

3.0.6 发布时，按维护者要求不发送公告弹窗；官网与仓库根目录公告源均设置为 `enabled: false`，`announcements: []`。后续是否启用须另行明确安排。正常版本检查不受影响。

## 电视上的行为

- 控制中心仅在存在适用公告时显示「公告与提醒」，存在未读公告时显示「有新公告」。
- `info` 普通公告只显示入口提示，不自动弹窗。
- `important` 重要公告会等到 HaloTV 桌面获得焦点、稳定显示约 1.5 秒后弹出。设置页、其他应用、屏保、儿童/长辈模式中不自动弹出。
- 「我知道了」和「不再提醒」都会记住当前公告的 ID 与修订号，后续不会再自动弹出这一版公告；仍可在控制中心查看。
- 「明天再提醒」或按返回键，会将自动提醒推迟 24 小时，之后在下次合适的检查/回到桌面时提醒。
- 同一公告没有收到操作回应时，每次程序运行最多自动展示一次，避免返回应用时反复弹出。
- 「查看说明」是可选按钮，只能打开 HaloTV 官网或本项目 GitHub 仓库下的 HTTPS 页面，且必须由用户点击。
- 入口展示按重要公告优先、同类按配置数组顺序。需要同时发布多条时，建议将当前最需要用户阅读的一条放在前面；此版本不是公告历史列表。

## 公告从哪里读取

优先：`https://halo-tv.pages.dev/announcements.json`

官网不可用或返回无效配置时，备用：`https://raw.githubusercontent.com/Null9797/halo-tv/main/announcements.json`

源文件分别是仓库的 `website/announcements.json` 和根目录 `announcements.json`。
发布公告时请同步两份，随后将 `website/` 部署到 Cloudflare Pages，并将根目录配置提交至 GitHub 的 `main` 分支。
只发布网站配置不需要重新打包 APK。只更新 GitHub 备用配置时，若官网仍提供有效的旧配置，客户端会继续以官网为准。

当前发布配置为 `enabled: false`，官网与根目录保持一致。

## 配置示例

下面是一条普通公告示例，正式发布前请替换标题、正文和时间。不要直接把示例当成正式通知发布。

```json
{
  "schema": 1,
  "enabled": true,
  "announcements": [
    {
      "id": "halo-service-notice",
      "revision": 1,
      "kind": "info",
      "title": "HaloTV 使用提示",
      "body": "这里填写第一段正文。\n\n这里填写第二段正文。",
      "variants": ["guard", "standard", "lite"],
      "minVersion": "3.0.6",
      "maxVersion": null,
      "minCode": null,
      "maxCode": null,
      "startsAt": "2026-11-11T00:00:00Z",
      "expiresAt": "2026-12-11T00:00:00Z",
      "detailsUrl": "https://github.com/Null9797/halo-tv"
    }
  ]
}
```

需要自动弹出的重要通知，将 `kind` 改为 `important`。一旦用户确认，修改正文并不会让同一个修订号再次弹出；确有必要重新通知时增加 `revision`。

## 字段规则

| 字段 | 用法 |
| --- | --- |
| `schema` | 固定为 `1` |
| `enabled` | 总开关；`false` 会撤下服务器公告 |
| `announcements` | 最多 20 条，整个文件不超过 64 KB |
| `id` | 稳定 ID，1–64 个英文字母、数字、点、下划线或短横线 |
| `revision` | 1–1000000 的整数，需要重新提示时递增 |
| `kind` | `info` 或 `important` |
| `title` / `body` | 纯文字，标题最多 100 字符，正文最多 6000 字符；正文可用 `\n\n` 分段 |
| `variants` | `guard` / `standard` / `lite`；不写或空数组表示全部 |
| `minVersion` / `maxVersion` | 可选显示版本范围，包含边界；如 `3.0.6` |
| `minCode` / `maxCode` | 可选内部号范围，包含边界；正式版与 Lite 内部号独立，建议分开配置 |
| `startsAt` / `expiresAt` | 可选 UTC 时间，格式严格为 `YYYY-MM-DDTHH:mm:ssZ`；北京时间减 8 小时，过期后不再显示 |
| `detailsUrl` | 可选，限 `https://halo-tv.pages.dev/…` 或 `https://github.com/Null9797/halo-tv/…` |
| 单条 `enabled` | 可选，`false` 撤下这一条 |

版本/内部号/日期/机型分支条件会同时生效。此版本不按电视型号或设备 ID 定向，不采集接收者信息。

## 资源占用与发布检查

复用现有检查更新的时机，默认有效配置缓存约 3 小时，失败后间隔约 10 分钟才重试；没有新增长连接、轮询服务或推送 SDK。进入控制中心或手动检查更新可能提前触发检查。公告使用本地缓存，网络不可用不会阻止桌面启动。

发布后用浏览器直接打开两条 JSON 地址，确认是 JSON 而不是网页或 404。官网应提供 `application/json`，建议低缓存时间。撤下公告后，离线电视仍可能暂时显示上次缓存，因此重要通知建议设置合理的到期时间。不能保证所有离线设备即时收到或撤回。

本轮通过本地构建、自动测试和静态检查；尚未在真实电视验证公告视觉效果及线上收取链路。安装后建议先用一条仅针对测试内部号的普通公告验证，再测试重要公告、返回键稍后提醒及确认后不重复。
