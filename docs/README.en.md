<div align="center">
  <img src="../website/images/brand/halotv.png" width="112" height="112" alt="HaloTV logo">
  <h1>HaloTV</h1>
  <p><strong>Your TV, your home screen.</strong></p>
  <p>Free, open-source launcher for Android TV · Release 3.6.1</p>
  <p><a href="https://halo-tv.pages.dev/">Website</a> · <a href="../README.md">简体中文</a> · <a href="../INSTALL.md">Installation guide</a> · <a href="https://github.com/Null9797/halo-tv/issues">Issues</a></p>
</div>

[![HaloTV launcher on a TV, with its quick shortcuts, glass dock and music capsule](../website/images/showcase/main.jpg)](../website/images/showcase/main.jpg)

HaloTV is a community-maintained derivative of [Aerial](https://github.com/pengchujin/aerial-tv), published by Null_. Thanks to the original author and contributors. HaloTV retains the original copyright and [MIT license](../LICENSE).

## Download and install

| Edition | Use case | Website | GitHub |
| --- | --- | --- | --- |
| **Standard** | Android 5.0+; try this first | [APK](https://halo-tv.pages.dev/updates/HaloTV-3.6.1-standard.apk) | [APK](https://github.com/Null9797/halo-tv/releases/download/v3.6.1-halo/HaloTV-3.6.1-standard.apk) |
| **Guard** | Android 5.0+; try it on firmware that restricts third-party launchers | [APK](https://halo-tv.pages.dev/updates/HaloTV-3.6.1-guard.apk) | [APK](https://github.com/Null9797/halo-tv/releases/download/v3.6.1-halo/HaloTV-3.6.1-guard.apk) |
| **Lite** | Android 4.0+; designed for older or lower-powered TVs | [APK](https://halo-tv.pages.dev/updates/HaloTV-3.6.1-lite.apk) | [APK](https://github.com/Null9797/halo-tv/releases/download/v3.6.1-halo/HaloTV-3.6.1-lite.apk) |

Install the matching edition over an existing independent installation to retain its settings. Aerial and independent HaloTV can coexist with separate permissions and data. Use only one desktop guard at a time. Cross-package configuration import was removed in 3.2.4.

[Website downloads](https://halo-tv.pages.dev/#download) · [Release 3.6.1](https://github.com/Null9797/halo-tv/releases/tag/v3.6.1-halo) · [Application source](https://github.com/Null9797/halo-tv/releases/download/v3.6.1-halo/HaloTV-3.6.1-source.zip)

## What's new in 3.6.1

### New features

- Set a continuous viewing limit and a timed rest in Kids mode. Pick a timed break or the existing quiz option. [#82](https://github.com/Null9797/halo-tv/issues/82)

### Fixes and improvements

- Separate current temperature from the daily high and low. When automatic location matches a city, use that city's coordinates for the forecast. [#92](https://github.com/Null9797/halo-tv/issues/92)
- Wait for the first video wallpaper frame before enabling sound. The reported Konka model needs a cold-start retest. [#84](https://github.com/Null9797/halo-tv/issues/84)
- Improved remote focus, wallpaper playback after standby, signal-source fallbacks and volume-key handling. Lite retries an out-of-date daily wallpaper after a date rollover.

Build 294 for Standard / Guard and 139 for Lite. Upgrade with the same edition.

[TV screenshots](GALLERY.md) · [Release notes](releases/RELEASE-3.6.1.md) · [Build verification](releases/VERIFICATION-3.6.1.json)

Screenshot credit: HaloTV 3.5-series test build captured on a TV.

## Support and credits

Search [existing Issues](https://github.com/Null9797/halo-tv/issues) before [reporting a problem](https://github.com/Null9797/halo-tv/issues/new?template=bug_report.yml). Include the TV model, Android version, HaloTV version, edition and reproduction steps.

The Bing archive is provided by [YanGN](https://github.com/ygnstudio/bing_wallpaper_archive). The video catalogue references [Aerial Views](https://github.com/theothernt/AerialViews) with Apple-hosted media. Media rights remain with the respective owners. See [LICENSE](../LICENSE) and [NOTICE](NOTICE.md).
