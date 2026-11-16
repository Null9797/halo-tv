# HaloTV · 3.2.7 official release

HaloTV is a free, open-source derivative of [Aerial](https://github.com/pengchujin/aerial-tv), maintained by Null_. It is not an official upstream release. Thanks to the original author and contributors; original copyright and MIT license are retained.

3.2.7 fixes recursive Settings launch after family mode is disabled while a PIN remains stored, hardens system-tile launches, and removes completed notices from Control Center while retaining unread or snoozed notices. Compact Dock and earlier updater improvements remain. Independent IDs, signer and artwork are retained.

Full builds use `app.halotv.launcher` (code 229, Android 5.0+); Lite uses `app.halotv.launcher.lite` (code 85, Android 4.0+). Select the same edition to update existing independent installs, including the 228 / 84 test builds. The independent TV feed uses website-first APK downloads with GitHub fallback.

All three release builds and 1,111 host test executions passed. Lint has no Error/Fatal findings but retains warnings. APK signatures and integrity were checked. The Settings fix was verified on a TCL MT5879 using test build 228; the 3.2.7 version rebuild was not reinstalled on that TV. Standard and Lite still require device testing. No emulator was run. If an older updater cannot download or install this release, use the website APK with phone upload, USB or ADB; the improved updater takes effect after installing 3.2.7.

[3.2.7 downloads](https://github.com/Null9797/halo-tv/releases/tag/v3.2.7-halo) · [Website](https://halo-tv.pages.dev/#download) · [Changes and verification](docs/releases/RELEASE-3.2.7.md) · [Full application source](https://github.com/Null9797/halo-tv/releases/download/v3.2.7-halo/HaloTV-3.2.7-source.zip)

Cross-package configuration import has been removed since 3.2.4. Android does not transfer private data or permissions across package names. Aerial and independent HaloTV can coexist, but do not enable both guards together.

The Bing archive is provided by [YanGN](https://github.com/ygnstudio/bing_wallpaper_archive); the video catalogue references [Aerial Views](https://github.com/theothernt/AerialViews) with Apple-hosted media. Media rights remain with their owners. See LICENSE and NOTICE.md.
