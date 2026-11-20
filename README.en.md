# HaloTV · 3.5 official release

HaloTV is a free, open-source derivative of [Aerial](https://github.com/pengchujin/aerial-tv), maintained by Null_. It is not an official upstream release. Thanks to the original author and contributors; original copyright and MIT license are retained.

## 3.5 changes

- **Desktop Dynamic Island** (Standard / Guard) shows background music, uploads from your phone, and update downloads. Choose bottom left, top centre, or top right. The feature is off by default.
- To enable it, open **HaloTV Settings → Desktop Dynamic Island**. For music, allow notification access for Halo TV Home Guard, pick a music app, and enable background playback in that app. The player must publish the track title and playing state through Android MediaSession.
- Keep Auto and 1080p available for aerial video and explain when 4K is unavailable. [#55](https://github.com/Null9797/halo-tv/issues/55)
- Keep a valid local video poster visible until the first rendered frame on Android 5/6. TV validation is pending. [#58](https://github.com/Null9797/halo-tv/issues/58)
- Fix Windows ADB text decoding and add verified single-owner detection for the desktop guard tool. [#59](https://github.com/Null9797/halo-tv/issues/59)

Standard / Guard: code 270, Android 5.0+. Lite: code 118, Android 4.0+, with its existing feature set. Install the matching edition over an existing independent installation to retain its settings.

[Downloads](https://github.com/Null9797/halo-tv/releases/tag/v3.5-halo) · [Website](https://halo-tv.pages.dev/#download) · [Changes](docs/releases/RELEASE-3.5.md) · [Verification](docs/releases/VERIFICATION-3.5.json) · [Application source](https://github.com/Null9797/halo-tv/releases/download/v3.5-halo/HaloTV-3.5-source.zip)

Cross-package configuration import has been removed since 3.2.4. Android does not transfer private data or permissions across package names. Aerial and independent HaloTV can coexist, but do not enable both guards together.

The Bing archive is provided by [YanGN](https://github.com/ygnstudio/bing_wallpaper_archive); the video catalogue references [Aerial Views](https://github.com/theothernt/AerialViews) with Apple-hosted media. Media rights remain with their owners. See LICENSE and NOTICE.md.

## Report a problem

Search [GitHub Issues](https://github.com/Null9797/halo-tv/issues) before [filing a report](https://github.com/Null9797/halo-tv/issues/new?template=bug_report.yml). Include the TV model, Android version, HaloTV version, edition, and steps to reproduce.
