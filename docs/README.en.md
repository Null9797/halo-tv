<div align="center">
  <img src="../website/images/brand/halotv.png" width="112" height="112" alt="HaloTV logo">
  <h1>HaloTV</h1>
  <p><strong>Your TV, your home screen.</strong></p>
  <p>Free, open-source launcher for Android TV · Release 3.5.4</p>
  <p><a href="https://halo-tv.pages.dev/">Website</a> · <a href="../README.md">简体中文</a> · <a href="../INSTALL.md">Installation guide</a> · <a href="https://github.com/Null9797/halo-tv/issues">Issues</a></p>
</div>

[![HaloTV launcher on a TV, with its glass dock and music capsule](../website/images/showcase/main.jpg)](../website/images/showcase/main.jpg)

HaloTV is a community-maintained derivative of [Aerial](https://github.com/pengchujin/aerial-tv), published by Null_. Thanks to the original author and contributors. HaloTV retains the original copyright and [MIT license](../LICENSE).

## Download and install

| Edition | Use case | Website | GitHub |
| --- | --- | --- | --- |
| **Standard** | Android 5.0+; try this first | [APK](https://halo-tv.pages.dev/updates/HaloTV-3.5.4-standard.apk) | [APK](https://github.com/Null9797/halo-tv/releases/download/v3.5.4-halo/HaloTV-3.5.4-standard.apk) |
| **Guard** | Android 5.0+; try it on firmware that restricts third-party launchers | [APK](https://halo-tv.pages.dev/updates/HaloTV-3.5.4-guard.apk) | [APK](https://github.com/Null9797/halo-tv/releases/download/v3.5.4-halo/HaloTV-3.5.4-guard.apk) |
| **Lite** | Android 4.0+; designed for older or lower-powered TVs | [APK](https://halo-tv.pages.dev/updates/HaloTV-3.5.4-lite.apk) | [APK](https://github.com/Null9797/halo-tv/releases/download/v3.5.4-halo/HaloTV-3.5.4-lite.apk) |

Install the matching edition over an existing independent installation to retain its settings. Aerial and independent HaloTV can coexist with separate permissions and data. Use only one desktop guard at a time. Cross-package configuration import was removed in 3.2.4.

[Website downloads](https://halo-tv.pages.dev/#download) · [Release 3.5.4](https://github.com/Null9797/halo-tv/releases/tag/v3.5.4-halo) · [Application source](https://github.com/Null9797/halo-tv/releases/download/v3.5.4-halo/HaloTV-3.5.4-source.zip)

## What's new in 3.5.4

- Directional input on all three editions now filters duplicate events from the same tap while retaining deliberate repeated taps and hold-to-repeat.
- Online preview rendering is contained in the gallery window. The setup QR panel is hidden during preview. [#56](https://github.com/Null9797/halo-tv/issues/56)
- Old Android 5/6 devices retain the valid poster until the first frame when manually trying 4K. [#55](https://github.com/Null9797/halo-tv/issues/55)
- Compatible SDR videos on the reported Baofeng model wait for a presented texture frame during a cold start. [#58](https://github.com/Null9797/halo-tv/issues/58)
- Frames with a corrupted green right edge are filtered when composing the All Apps background. [#54](https://github.com/Null9797/halo-tv/issues/54)
- Legacy HTTPS compatibility was improved. Standard / Guard can use Bing daily photos if the screensaver archive source fails. [#76](https://github.com/Null9797/halo-tv/issues/76)
- Merged selected Aerial 2.17 changes for the desktop guard, TV controls, inputs and icons.

Build 281 for Standard / Guard and 128 for Lite. Upgrade using the same edition. Affected TV models still need hardware retests.

[TV screenshots](GALLERY.md) · [Release notes](releases/RELEASE-3.5.4.md) · [Build verification](releases/VERIFICATION-3.5.4.json)

Screenshot credit: HaloTV 3.5-series test build captured on a TV.

## Support and credits

Search [existing Issues](https://github.com/Null9797/halo-tv/issues) before [reporting a problem](https://github.com/Null9797/halo-tv/issues/new?template=bug_report.yml). Include the TV model, Android version, HaloTV version, edition and reproduction steps.

The Bing archive is provided by [YanGN](https://github.com/ygnstudio/bing_wallpaper_archive). The video catalogue references [Aerial Views](https://github.com/theothernt/AerialViews) with Apple-hosted media. Media rights remain with the respective owners. See [LICENSE](../LICENSE) and [NOTICE](NOTICE.md).
