# HaloTV · 3.2.4 public test

HaloTV is a free, open-source derivative of [Aerial](https://github.com/pengchujin/aerial-tv), maintained by Null_. It is not an official upstream release. Thanks to the original author and contributors; original copyright and MIT license are retained.

3.2.4 integrates the Aerial 1.98 runtime changes while retaining HaloTV features, settings and artwork. Cross-package configuration import, bridge installation and guard handover are removed. Existing independent installations can be updated in place with the same edition and release signer. Full builds use `app.halotv.launcher` (code 221, Android 5.0+); Lite uses `app.halotv.launcher.lite` (code 77, Android 4.0+). Upstream Lite remained 1.30 in the 1.98 release.

**This is a prerelease for manual testing. Stable remains 3.2.3; its automatic update feed is unchanged.** All three release builds and 1,080 host test executions passed. Lint has no Error/Fatal findings but retains warnings. APK signatures and integrity were verified. No emulator or TV was operated; firmware-specific behavior still requires device testing.

[3.2.4 test downloads](https://github.com/Null9797/halo-tv/releases/tag/v3.2.4-halo-test) · [Stable](https://github.com/Null9797/halo-tv/releases/latest) · [Website](https://halo-tv.pages.dev/#download) · [Change and verification details](docs/releases/RELEASE-3.2.4.md) · [Source](https://github.com/Null9797/halo-tv/releases/download/v3.2.4-halo-test/HaloTV-3.2.4-source.zip)

3.2.4 no longer imports data from older package names. Android does not transfer private data or permissions across packages. Aerial and independent HaloTV can coexist, but do not enable both launcher guards together.

The Bing archive is provided by [YanGN](https://github.com/ygnstudio/bing_wallpaper_archive); the video catalogue references [Aerial Views](https://github.com/theothernt/AerialViews) with Apple-hosted media. Media rights remain with their owners. See LICENSE and NOTICE.md.
