# HaloTV · 3.3.4 official release

HaloTV is a free, open-source derivative of [Aerial](https://github.com/pengchujin/aerial-tv), maintained by Null_. It is not an official upstream release. Thanks to the original author and contributors; original copyright and MIT license are retained.

## 3.3.4 changes

- Add narrowly scoped local 1080p SDR video composition compatibility for reported MiTV-ASTR0 devices; retain existing 4K/HDR and other-device output.
- Back off consecutive unreadable frame copies, retain valid fallback imagery, bound return covers and ignore stale output-release callbacks.
- Persist the existing keep-ADB choice and perform bounded startup checks, respecting opt-out, permission revocation and shutdown.
- Improve diagnostics for actual HOME resolution and required permissions.
- Route TCL inputs with real hardware IDs / complete input IDs; avoid stale ports, guessed offsets and generic file handlers.
- Fix empty/corrupt wallpaper catalog caches, retry behavior and cache-write failures hiding valid results.
- Filter invalid catalog entries before pagination and remove duplicate date keys; shared with Lite and phone management.

Retains the 3.3.3 held-volume and completed-welcome fixes. Standard / Guard: code 246, Android 5.0+. Lite: code 102, Android 4.0+. Lite receives the catalog fixes, without full video-wallpaper or accessibility-guard features. Existing independent IDs, signer, logo and static welcome remain unchanged.

Host regression checks passed; device-specific playback, HOME and HDMI behavior still requires hardware confirmation. Firmware restrictions cannot be guaranteed bypassed.

[Downloads](https://github.com/Null9797/halo-tv/releases/tag/v3.3.4-halo) · [Website](https://halo-tv.pages.dev/#download) · [Changes](docs/releases/RELEASE-3.3.4.md) · [Verification](docs/releases/VERIFICATION-3.3.4.json) · [Application source](https://github.com/Null9797/halo-tv/releases/download/v3.3.4-halo/HaloTV-3.3.4-source.zip)

Cross-package configuration import has been removed since 3.2.4. Android does not transfer private data or permissions across package names. Aerial and independent HaloTV can coexist, but do not enable both guards together.

The Bing archive is provided by [YanGN](https://github.com/ygnstudio/bing_wallpaper_archive); the video catalogue references [Aerial Views](https://github.com/theothernt/AerialViews) with Apple-hosted media. Media rights remain with their owners. See LICENSE and NOTICE.md.
