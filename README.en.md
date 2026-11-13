# HaloTV 3.0.6

An unofficial derivative of [Aerial](https://github.com/pengchujin/aerial-tv), maintained by Null_. Free to download and use; retains upstream MIT license and copyright notices. No affiliation or endorsement by upstream, Apple or television vendors.

[Website](https://halo-tv.pages.dev/) · [Downloads](https://github.com/Null9797/halo-tv/releases/latest) · [Quark mirror](https://pan.quark.cn/s/a14e3ab2dd41) · [Installation guide](INSTALL.md)

![HaloTV 3.0.6 desktop](screenshots/home-3.0.jpg)

Standard and Guard require Android 5.0+ (versionCode 187); choose one. Lite supports Android 4.0+ (versionCode 43), without video wallpapers or the full performance modes. All display version 3.0.6. New control center, categorized settings, customizable Dock and information layouts, flip clock, child quiz and elder modes, phone management and validated HaloTV-only update uploads.

2.1.4 full builds detect the latest stable GitHub Release and can upgrade with the existing signing identity. Older Lite builds without an update checker need one manual upgrade. 3.0 checks the website first and falls back to GitHub; downloads do not silently install.

[Source archive](https://github.com/Null9797/halo-tv/releases/download/v3.0.6-halo/HaloTV-3.0.6-source.zip) · [Checksums](SHA256SUMS.txt) · [Release notes](RELEASE_NOTES.md). Automated tests passed (325 per full flavor, 37 Lite); this does not certify every television firmware or codec. See [Chinese README](README.md) for features and screenshots.

Static imagery: Bing; archive by [YanGN](https://github.com/ygnstudio/bing_wallpaper_archive). Video catalogue references [Aerial Views](https://github.com/theothernt/AerialViews), videos from Apple. Media rights remain with their respective owners.

### Latest 3.0.6 release
Full build 189 / Lite build 45. Full builds improve Home event filtering and safe guard rebinding, add a fallback for installers that immediately dismiss their confirmation activity without a result, and prevent a completed upgrade from reopening the previous app or input. Lite also returns home after a validated requested upgrade. 716 automated test executions passed. Package identity, signing and edition checks remain enforced. No announcement popup is sent for this release; firmware-specific permissions and behavior still require device validation.
