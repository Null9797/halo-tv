# HaloTV · 3.3.3 official release

HaloTV is a free, open-source derivative of [Aerial](https://github.com/pengchujin/aerial-tv), maintained by Null_. It is not an official upstream release. Thanks to the original author and contributors; original copyright and MIT license are retained.

## 3.3.3 changes

- Fix held remote volume keys failing to adjust continuously on some TVs.
- Preserve completed welcome onboarding so existing users can enter Home directly after updating.

Standard / Guard: code 243, Android 5.0+. Lite: code 99, Android 4.0+. Update using the same edition; existing independent IDs, signer and data are retained.

[Downloads](https://github.com/Null9797/halo-tv/releases/tag/v3.3.3-halo) · [Website](https://halo-tv.pages.dev/#download) · [Changes](docs/releases/RELEASE-3.3.3.md) · [Verification](docs/releases/VERIFICATION-3.3.3.json) · [Application source](https://github.com/Null9797/halo-tv/releases/download/v3.3.3-halo/HaloTV-3.3.3-source.zip)

Cross-package configuration import has been removed since 3.2.4. Android does not transfer private data or permissions across package names. Aerial and independent HaloTV can coexist, but do not enable both guards together.

The Bing archive is provided by [YanGN](https://github.com/ygnstudio/bing_wallpaper_archive); the video catalogue references [Aerial Views](https://github.com/theothernt/AerialViews) with Apple-hosted media. Media rights remain with their owners. See LICENSE and NOTICE.md.
