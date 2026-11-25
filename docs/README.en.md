<div align="center">
  <img src="../website/images/brand/halotv.png" width="112" height="112" alt="HaloTV logo">
  <h1>HaloTV</h1>
  <p><strong>Your TV, your home screen.</strong></p>
  <p>Free, open-source launcher for Android TV · Release 3.6</p>
  <p><a href="https://halo-tv.pages.dev/">Website</a> · <a href="../README.md">简体中文</a> · <a href="../INSTALL.md">Installation guide</a> · <a href="https://github.com/Null9797/halo-tv/issues">Issues</a></p>
</div>

[![HaloTV launcher on a TV, with its quick shortcuts, glass dock and music capsule](../website/images/showcase/main.jpg)](../website/images/showcase/main.jpg)

HaloTV is a community-maintained derivative of [Aerial](https://github.com/pengchujin/aerial-tv), published by Null_. Thanks to the original author and contributors. HaloTV retains the original copyright and [MIT license](../LICENSE).

## Download and install

| Edition | Use case | Website | GitHub |
| --- | --- | --- | --- |
| **Standard** | Android 5.0+; try this first | [APK](https://halo-tv.pages.dev/updates/HaloTV-3.6-standard.apk) | [APK](https://github.com/Null9797/halo-tv/releases/download/v3.6-halo/HaloTV-3.6-standard.apk) |
| **Guard** | Android 5.0+; try it on firmware that restricts third-party launchers | [APK](https://halo-tv.pages.dev/updates/HaloTV-3.6-guard.apk) | [APK](https://github.com/Null9797/halo-tv/releases/download/v3.6-halo/HaloTV-3.6-guard.apk) |
| **Lite** | Android 4.0+; designed for older or lower-powered TVs | [APK](https://halo-tv.pages.dev/updates/HaloTV-3.6-lite.apk) | [APK](https://github.com/Null9797/halo-tv/releases/download/v3.6-halo/HaloTV-3.6-lite.apk) |

Install the matching edition over an existing independent installation to retain its settings. Aerial and independent HaloTV can coexist with separate permissions and data. Use only one desktop guard at a time. Cross-package configuration import was removed in 3.2.4.

[Website downloads](https://halo-tv.pages.dev/#download) · [Release 3.6](https://github.com/Null9797/halo-tv/releases/tag/v3.6-halo) · [Application source](https://github.com/Null9797/halo-tv/releases/download/v3.6-halo/HaloTV-3.6-source.zip)

## What's new in 3.6

### New features

- Customize up to three desktop shortcuts. Shuffle the current wallpaper type from the desktop or Control Center.
- Create, import and export custom question banks from the phone management page. [#33](https://github.com/Null9797/halo-tv/issues/33)
- Set Kids or Senior mode to start on boot. Enter a configured mode from the normal desktop and verify the parent PIN when exiting.
- Long-press the music capsule for playback controls on Standard / Guard. Control Center shows a dot when an update is available.

### Improvements and fixes

- Streamlined phone management and Control Center. Improved quiz playback handling, wallpaper switching, update recovery and TV app icon layout. [#66](https://github.com/Null9797/halo-tv/issues/66)
- Improved cold-start video track detection and Skyworth Home handling on the reported devices. Added startup diagnostics for the reported Dangbei black screen. [#58](https://github.com/Null9797/halo-tv/issues/58) · [#78](https://github.com/Null9797/halo-tv/issues/78) · [#79](https://github.com/Null9797/halo-tv/issues/79)

Build 292 for Standard / Guard and 137 for Lite. Upgrade using the same edition. Affected TV models still need hardware retests.

[TV screenshots](GALLERY.md) · [Release notes](releases/RELEASE-3.6.md) · [Build verification](releases/VERIFICATION-3.6.json)

Screenshot credit: HaloTV 3.5-series test build captured on a TV.

## Support and credits

Search [existing Issues](https://github.com/Null9797/halo-tv/issues) before [reporting a problem](https://github.com/Null9797/halo-tv/issues/new?template=bug_report.yml). Include the TV model, Android version, HaloTV version, edition and reproduction steps.

The Bing archive is provided by [YanGN](https://github.com/ygnstudio/bing_wallpaper_archive). The video catalogue references [Aerial Views](https://github.com/theothernt/AerialViews) with Apple-hosted media. Media rights remain with the respective owners. See [LICENSE](../LICENSE) and [NOTICE](NOTICE.md).
