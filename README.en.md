<div align="center">
  <img src="website/images/brand/halotv.png" width="112" height="112" alt="HaloTV logo">
  <h1>HaloTV</h1>
  <p><strong>Your TV, your home screen.</strong></p>
  <p>Free, open-source launcher for Android TV · Release 3.5</p>
  <p><a href="https://halo-tv.pages.dev/">Website</a> · <a href="README.md">简体中文</a> · <a href="INSTALL.md">Installation guide</a> · <a href="https://github.com/Null9797/halo-tv/issues">Issues</a></p>
</div>

[![HaloTV launcher on a TV, with its glass dock and music capsule](website/images/showcase/main.jpg)](website/images/showcase/main.jpg)

HaloTV is a community-maintained derivative of [Aerial](https://github.com/pengchujin/aerial-tv), published by Null_. Thanks to the original author and contributors. HaloTV retains the original copyright and [MIT license](LICENSE).

## Download and install

| Edition | Use case | Website | GitHub |
| --- | --- | --- | --- |
| **Standard** | Android 5.0+; try this first | [APK](https://halo-tv.pages.dev/updates/HaloTV-3.5-standard.apk) | [APK](https://github.com/Null9797/halo-tv/releases/download/v3.5-halo/HaloTV-3.5-standard.apk) |
| **Guard** | Android 5.0+; try it on firmware that restricts third-party launchers | [APK](https://halo-tv.pages.dev/updates/HaloTV-3.5-guard.apk) | [APK](https://github.com/Null9797/halo-tv/releases/download/v3.5-halo/HaloTV-3.5-guard.apk) |
| **Lite** | Android 4.0+; designed for older or lower-powered TVs | [APK](https://halo-tv.pages.dev/updates/HaloTV-3.5-lite.apk) | [APK](https://github.com/Null9797/halo-tv/releases/download/v3.5-halo/HaloTV-3.5-lite.apk) |

Install the matching edition over an existing independent installation to retain its settings. Aerial and independent HaloTV can coexist with separate permissions and data. Use only one desktop guard at a time. Cross-package configuration import was removed in 3.2.4.

[Website downloads](https://halo-tv.pages.dev/#download) · [Release 3.5](https://github.com/Null9797/halo-tv/releases/tag/v3.5-halo) · [Application source](https://github.com/Null9797/halo-tv/releases/download/v3.5-halo/HaloTV-3.5-source.zip)

## What's new in 3.5

**Desktop Dynamic Island** (Standard / Guard) displays background music, phone uploads and update downloads. It is off by default. Enable it under **HaloTV Settings → Desktop Dynamic Island** and choose a position. Music requires notification access for Halo TV Home Guard, background playback in the selected player, and Android MediaSession support.

- Keep Auto and 1080p available for aerial video and explain when 4K is unavailable. [#55](https://github.com/Null9797/halo-tv/issues/55)
- Keep a local video poster visible until the first rendered frame on Android 5/6. TV validation is pending. [#58](https://github.com/Null9797/halo-tv/issues/58)
- Fix Windows ADB text decoding and add single-owner detection for the guard tool. [#59](https://github.com/Null9797/halo-tv/issues/59)

[TV screenshots](screenshots/README.md) · [Release notes](docs/releases/RELEASE-3.5.md) · [Build verification](docs/releases/VERIFICATION-3.5.json)

Screenshot credit: HaloTV 3.5-series test build captured on a TV.

## Support and credits

Search [existing Issues](https://github.com/Null9797/halo-tv/issues) before [reporting a problem](https://github.com/Null9797/halo-tv/issues/new?template=bug_report.yml). Include the TV model, Android version, HaloTV version, edition and reproduction steps.

The Bing archive is provided by [YanGN](https://github.com/ygnstudio/bing_wallpaper_archive). The video catalogue references [Aerial Views](https://github.com/theothernt/AerialViews) with Apple-hosted media. Media rights remain with the respective owners. See [LICENSE](LICENSE) and [NOTICE](NOTICE.md).
