# HaloTV · 3.3 official release

HaloTV is a free, open-source derivative of [Aerial](https://github.com/pengchujin/aerial-tv), maintained by Null_. It is not an official upstream release. Thanks to the original author and contributors; original copyright and MIT license are retained.

3.3 improves video-wallpaper transitions between Home, screensavers and external apps, reduces redundant rendering and background image work, and adds guided guard repair and permission checks. Relevant Aerial 1.99 changes (upstream Lite 1.31) are integrated. Control Center pairs HaloTV Settings with Home Guard Settings, and Software Update with a permanent Announcements entry. A red badge marks eligible unread notices; acknowledgment clears it, while snooze retains it.

Full builds use `app.halotv.launcher` (code 236, Android 5.0+); Lite uses `app.halotv.launcher.lite` (code 92, Android 4.0+). Select the same edition to update existing independent installs, including 3.2.8 test builds up to 235 / 91. IDs, signer and artwork are preserved. Website-first APK downloads retain GitHub fallback.

All three release builds and 1,199 host test executions passed. Lint has no Error/Fatal findings but retains warnings. APK identities, signatures and integrity were checked. No TV or emulator was operated for this release; device-specific behavior still requires testing. Lite does not include the full accessibility guard service. No new remote announcement is sent.

[3.3 downloads](https://github.com/Null9797/halo-tv/releases/tag/v3.3-halo) · [Website](https://halo-tv.pages.dev/#download) · [Changes and verification](docs/releases/RELEASE-3.3.md) · [Full application source](https://github.com/Null9797/halo-tv/releases/download/v3.3-halo/HaloTV-3.3-source.zip)

Cross-package configuration import has been removed since 3.2.4. Android does not transfer private data or permissions across package names. Aerial and independent HaloTV can coexist, but do not enable both guards together.

The Bing archive is provided by [YanGN](https://github.com/ygnstudio/bing_wallpaper_archive); the video catalogue references [Aerial Views](https://github.com/theothernt/AerialViews) with Apple-hosted media. Media rights remain with their owners. See LICENSE and NOTICE.md.
