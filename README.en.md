# HaloTV · 3.3.7 official release

HaloTV is a free, open-source derivative of [Aerial](https://github.com/pengchujin/aerial-tv), maintained by Null_. It is not an official upstream release. Thanks to the original author and contributors; original copyright and MIT license are retained.

## 3.3.7 changes

- Detect 4K SDR HEVC capability on Android 5.0–6.0 for aerial wallpapers and screensavers, with 1080p fallback and playback diagnostics ([#55](https://github.com/Null9797/halo-tv/issues/55)).
- Make the liquid glass Dock more transparent. Video uses a subtle tint from existing samples, without new frame captures or real-time refraction (related to [#52](https://github.com/Null9797/halo-tv/issues/52)).
- Share row transition motion and defer wallpaper frame capture until the app grid settles.
- Correct children's viewing time across app switches and improve authorized quiz delivery and reminders.
- These changes are for Standard / Guard. Lite has the same feature set as before.

Standard / Guard: code 263, Android 5.0+. Lite: code 117, Android 4.0+, using Android's default Home mechanism. Install the matching edition over an existing independent installation to retain its settings.

Host regression checks passed. OEM-specific behavior still requires TV validation.

[Downloads](https://github.com/Null9797/halo-tv/releases/tag/v3.3.7-halo) · [Website](https://halo-tv.pages.dev/#download) · [Changes](docs/releases/RELEASE-3.3.7.md) · [Verification](docs/releases/VERIFICATION-3.3.7.json) · [Application source](https://github.com/Null9797/halo-tv/releases/download/v3.3.7-halo/HaloTV-3.3.7-source.zip)

Cross-package configuration import has been removed since 3.2.4. Android does not transfer private data or permissions across package names. Aerial and independent HaloTV can coexist, but do not enable both guards together.

The Bing archive is provided by [YanGN](https://github.com/ygnstudio/bing_wallpaper_archive); the video catalogue references [Aerial Views](https://github.com/theothernt/AerialViews) with Apple-hosted media. Media rights remain with their owners. See LICENSE and NOTICE.md.

## Report a problem

Search [GitHub Issues](https://github.com/Null9797/halo-tv/issues) before [filing a report](https://github.com/Null9797/halo-tv/issues/new?template=bug_report.yml). Include the TV model, Android version, HaloTV version, edition, and steps to reproduce.
