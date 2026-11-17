# HaloTV · 3.3.2 official release

HaloTV is a free, open-source derivative of [Aerial](https://github.com/pengchujin/aerial-tv), maintained by Null_. It is not an official upstream release. Thanks to the original author and contributors; original copyright and MIT license are retained.

All three editions introduce a new light, static first-open welcome with handwritten greeting artwork, the HaloTV halo/star/horizon and visible Aerial attribution. The complete screen appears immediately; one remote confirmation enters the desktop. Completion is retained across restarts and normal updates. Announcements & Feedback and the private feedback service from 3.3.1 remain available, with explicit submission consent, optional diagnostics, phone supplements and author replies.

Full builds use `app.halotv.launcher` (code 241, Android 5.0+); Lite uses `app.halotv.launcher.lite` (code 97, Android 4.0+). Choose the same edition to update existing independent installs, including welcome test builds 239/95 and 240/96. IDs, signer and startup artwork are preserved. Website-first APK downloads retain GitHub fallback. Lite does not include the full accessibility guard service.

Three Release builds, 1,231 host test executions passed. Lint reports no Error/Fatal findings; warnings remain. APK identity/signature/integrity and static native rendering were checked. No TV or emulator was operated; device-specific layout and network behavior still require testing. No new remote announcement is sent.

[3.3.2 downloads](https://github.com/Null9797/halo-tv/releases/tag/v3.3.2-halo) · [Website](https://halo-tv.pages.dev/#download) · [Changes and verification](docs/releases/RELEASE-3.3.2.md) · [Full application source](https://github.com/Null9797/halo-tv/releases/download/v3.3.2-halo/HaloTV-3.3.2-source.zip)

Cross-package configuration import has been removed since 3.2.4. Android does not transfer private data or permissions across package names. Aerial and independent HaloTV can coexist, but do not enable both guards together.

The Bing archive is provided by [YanGN](https://github.com/ygnstudio/bing_wallpaper_archive); the video catalogue references [Aerial Views](https://github.com/theothernt/AerialViews) with Apple-hosted media. Media rights remain with their owners. See LICENSE and NOTICE.md.
