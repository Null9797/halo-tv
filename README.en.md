# HaloTV · 3.3.1 official release

HaloTV is a free, open-source derivative of [Aerial](https://github.com/pengchujin/aerial-tv), maintained by Null_. It is not an official upstream release. Thanks to the original author and contributors; original copyright and MIT license are retained.

Control Center now provides Announcements & Feedback across Standard, Guard and Lite. Users can choose a problem category, review device/app information and decide whether to attach diagnostics. A phone can supplement the private report with a description and up to two images, or view the author's reply. Submission requires consent; there is no automatic screenshot capture, background upload or polling. Common network addresses and secret fields are filtered. Reports remain accessible for 30 days and expired rows are removed on subsequent submissions. Keep receipt links private.

Full builds use `app.halotv.launcher` (code 238, Android 5.0+); Lite uses `app.halotv.launcher.lite` (code 94, Android 4.0+). Choose the same edition to update existing independent installs, including feedback test builds 237 / 93. IDs, signer and startup artwork are preserved. Website-first APK downloads retain GitHub fallback. Lite does not include the full accessibility guard service.

Three Release builds, 1,220 host test executions and 8 backend tests passed. Lint reports no Error/Fatal findings; warnings remain. APK identity/signature/integrity and the production feedback submission/reply flow were checked. No TV or emulator was operated; device-specific layout and network behavior still require testing. No new remote announcement is sent.

[3.3.1 downloads](https://github.com/Null9797/halo-tv/releases/tag/v3.3.1-halo) · [Website](https://halo-tv.pages.dev/#download) · [Changes and verification](docs/releases/RELEASE-3.3.1.md) · [Full application source](https://github.com/Null9797/halo-tv/releases/download/v3.3.1-halo/HaloTV-3.3.1-source.zip)

Cross-package configuration import has been removed since 3.2.4. Android does not transfer private data or permissions across package names. Aerial and independent HaloTV can coexist, but do not enable both guards together.

The Bing archive is provided by [YanGN](https://github.com/ygnstudio/bing_wallpaper_archive); the video catalogue references [Aerial Views](https://github.com/theothernt/AerialViews) with Apple-hosted media. Media rights remain with their owners. See LICENSE and NOTICE.md.
