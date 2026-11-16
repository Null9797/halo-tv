# HaloTV · 3.2.5 official release

HaloTV is a free, open-source derivative of [Aerial](https://github.com/pengchujin/aerial-tv), maintained by Null_. It is not an official upstream release. Thanks to the original author and contributors; original copyright and MIT license are retained.

3.2.5 improves update retries, slow-network handling and installer compatibility; corrects system Settings tile routing; restores the selected-icon caption and adds a separate large-title option; and provides remote-controlled, full-screen announcement reading without an external browser. It retains the Aerial 1.98 baseline previously integrated in HaloTV, independent package IDs, signer and artwork.

Full builds use `app.halotv.launcher` (code 224, Android 5.0+); Lite uses `app.halotv.launcher.lite` (code 80, Android 4.0+). Select the same edition to update existing independent installs, including the 223 / 79 test builds. The independent TV feed uses website-first APK downloads with GitHub fallback.

All three release builds and 1,105 host test executions passed. Lint has no Error/Fatal findings but retains warnings. APK signatures and integrity were checked. No emulator or TV was operated; firmware-specific behavior still requires device testing. If an older updater cannot download or install this release, use the website APK with phone upload, USB or ADB; the improved updater takes effect after installing 3.2.5.

[3.2.5 downloads](https://github.com/Null9797/halo-tv/releases/tag/v3.2.5-halo) · [Website](https://halo-tv.pages.dev/#download) · [Changes and verification](docs/releases/RELEASE-3.2.5.md) · [Full application source](https://github.com/Null9797/halo-tv/releases/download/v3.2.5-halo/HaloTV-3.2.5-source.zip)

Cross-package configuration import has been removed since 3.2.4. Android does not transfer private data or permissions across package names. Aerial and independent HaloTV can coexist, but do not enable both guards together.

The Bing archive is provided by [YanGN](https://github.com/ygnstudio/bing_wallpaper_archive); the video catalogue references [Aerial Views](https://github.com/theothernt/AerialViews) with Apple-hosted media. Media rights remain with their owners. See LICENSE and NOTICE.md.
