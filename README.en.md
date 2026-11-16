# HaloTV · 3.2.6 official release

HaloTV is a free, open-source derivative of [Aerial](https://github.com/pengchujin/aerial-tv), maintained by Null_. It is not an official upstream release. Thanks to the original author and contributors; original copyright and MIT license are retained.

3.2.6 fixes excess space below Dock icons in selected-only app-name mode, restoring the compact plate and two-row spacing in Standard, Guard and Lite. All-names and large-title layouts remain separate. It retains the update, Settings and announcement-reading improvements from 3.2.5, the previously integrated Aerial 1.98 baseline, independent package IDs, signer and artwork.

Full builds use `app.halotv.launcher` (code 226, Android 5.0+); Lite uses `app.halotv.launcher.lite` (code 82, Android 4.0+). Select the same edition to update existing independent installs, including the 225 / 81 test builds. The independent TV feed uses website-first APK downloads with GitHub fallback.

All three release builds and 1,105 host test executions passed. Lint has no Error/Fatal findings but retains warnings. APK signatures and integrity were checked. No emulator or TV was operated; firmware-specific behavior still requires device testing. If an older updater cannot download or install this release, use the website APK with phone upload, USB or ADB; the improved updater takes effect after installing 3.2.6.

[3.2.6 downloads](https://github.com/Null9797/halo-tv/releases/tag/v3.2.6-halo) · [Website](https://halo-tv.pages.dev/#download) · [Changes and verification](docs/releases/RELEASE-3.2.6.md) · [Full application source](https://github.com/Null9797/halo-tv/releases/download/v3.2.6-halo/HaloTV-3.2.6-source.zip)

Cross-package configuration import has been removed since 3.2.4. Android does not transfer private data or permissions across package names. Aerial and independent HaloTV can coexist, but do not enable both guards together.

The Bing archive is provided by [YanGN](https://github.com/ygnstudio/bing_wallpaper_archive); the video catalogue references [Aerial Views](https://github.com/theothernt/AerialViews) with Apple-hosted media. Media rights remain with their owners. See LICENSE and NOTICE.md.
