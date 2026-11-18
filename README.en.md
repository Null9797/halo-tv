# HaloTV · 3.3.6 official release

HaloTV is a free, open-source derivative of [Aerial](https://github.com/pengchujin/aerial-tv), maintained by Null_. It is not an official upstream release. Thanks to the original author and contributors; original copyright and MIT license are retained.

## 3.3.6 changes

- Improve Home Guard on Standard and Guard at boot, after missed Home events, and after service or process restarts.
- Integrate Aerial 2.1 fixes for system screensavers, video wallpaper capture and selected TV inputs, including older TCL inputs on Lite.
- Fix weather refresh, phone video uploads and uploaded video cover refresh.
- Collect diagnostics on demand, copy the report and open HaloTV GitHub Issues.

Standard / Guard: code 259, Android 5.0+. Lite: code 115, Android 4.0+, using Android's default Home mechanism. Install the matching edition over an existing independent installation to retain its settings.

Host regression checks passed. OEM-specific behavior still requires TV validation.

[Downloads](https://github.com/Null9797/halo-tv/releases/tag/v3.3.6-halo) · [Website](https://halo-tv.pages.dev/#download) · [Changes](docs/releases/RELEASE-3.3.6.md) · [Verification](docs/releases/VERIFICATION-3.3.6.json) · [Application source](https://github.com/Null9797/halo-tv/releases/download/v3.3.6-halo/HaloTV-3.3.6-source.zip)

Cross-package configuration import has been removed since 3.2.4. Android does not transfer private data or permissions across package names. Aerial and independent HaloTV can coexist, but do not enable both guards together.

The Bing archive is provided by [YanGN](https://github.com/ygnstudio/bing_wallpaper_archive); the video catalogue references [Aerial Views](https://github.com/theothernt/AerialViews) with Apple-hosted media. Media rights remain with their owners. See LICENSE and NOTICE.md.

## Report a problem

Search [GitHub Issues](https://github.com/Null9797/halo-tv/issues) before [filing a report](https://github.com/Null9797/halo-tv/issues/new?template=bug_report.yml). Include the TV model, Android version, HaloTV version, edition, and steps to reproduce.
