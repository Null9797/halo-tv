# HaloTV · 3.3.5 official release

HaloTV is a free, open-source derivative of [Aerial](https://github.com/pengchujin/aerial-tv), maintained by Null_. It is not an official upstream release. Thanks to the original author and contributors; original copyright and MIT license are retained.

## 3.3.5 changes

- Add linked small/default/large Dock and icon sizes in TV and phone settings.
- Align corner clock information and status controls with the selected Dock size.
- Refresh online static wallpaper immediately when another image replaces the same wallpaper ID.
- Version backdrop, frost, thumbnail and phone-preview caches, including identical file timestamps.
- Reject stale, cancelled and out-of-order requests across wallpaper types and automatic rotation; preserve the valid image on failure.
- Preserve existing rotation categories for older phone clients and update rotation state after a successful manual selection.

Standard / Guard: code 250, Android 5.0+. Lite: code 106, Android 4.0+. All three include the Dock and online-static-wallpaper changes within their existing feature scope. Independent IDs, signer, artwork and existing settings are preserved.

Host regression checks passed. No TV or emulator was operated in this release; hardware behavior remains unverified. Issue #46 still requires device feedback.

[Downloads](https://github.com/Null9797/halo-tv/releases/tag/v3.3.5-halo) · [Website](https://halo-tv.pages.dev/#download) · [Changes](docs/releases/RELEASE-3.3.5.md) · [Verification](docs/releases/VERIFICATION-3.3.5.json) · [Application source](https://github.com/Null9797/halo-tv/releases/download/v3.3.5-halo/HaloTV-3.3.5-source.zip)

Cross-package configuration import has been removed since 3.2.4. Android does not transfer private data or permissions across package names. Aerial and independent HaloTV can coexist, but do not enable both guards together.

The Bing archive is provided by [YanGN](https://github.com/ygnstudio/bing_wallpaper_archive); the video catalogue references [Aerial Views](https://github.com/theothernt/AerialViews) with Apple-hosted media. Media rights remain with their owners. See LICENSE and NOTICE.md.
