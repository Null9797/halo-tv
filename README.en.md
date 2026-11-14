# HaloTV 3.2.2

HaloTV is a free, open-source derivative of [Aerial](https://github.com/pengchujin/aerial-tv), maintained by Null_. It is not an official upstream release. Thanks to the original author and contributors; original copyright and MIT license are retained.

## This release

This update separates data import from desktop takeover. It verifies the new guard or default Home before requesting a trusted bridge to stop, checks its response, adds a resumable migration review, distinguishes the independent service label, and offers a permission-dependent repair for a stale legacy boot entry. Lite reviews default Home and remains without the full guard. [Release notes](docs/releases/RELEASE-3.2.2.md).

Standard / Guard use `app.halotv.launcher` (code **218**, Android 5.0+). Lite uses `app.halotv.launcher.lite` (code **73**, Android 4.0+). All show **3.2.2** and retain the independent signing identity introduced in 3.1. Lite is a synchronized version release and does not include the full HomeGuardService or full video desktop implementation.

The core guard fixes passed automated tests; affected TVs have not all been tested. Manufacturer restrictions still apply. A registered accessibility service is not proof of binding, and a running service does not guarantee Home/boot interception on every device.

## Upgrade and migration

Existing independent users can update the same edition in place. Older package names must first use the matching [3.1 bridge](https://github.com/Null9797/halo-tv/releases/tag/v3.1-halo), then install Independent and import data. Configure Home, screen saver and guard permissions again; Android does not transfer system permissions across package names. Only uninstall the old HaloTV after verifying the independent app. Never automatically uninstall `app.orchard.tv`: it may be Aerial. Both apps may coexist, but only one launcher guard should be enabled.

A migration reminder is provided for older clients with remote-announcement support and a reachable feed. Clients without that feature cannot receive a remote popup. Installation and uninstallation remain user-confirmed.

[Website](https://halo-tv.pages.dev/) · [Downloads](https://github.com/Null9797/halo-tv/releases/tag/v3.2.2-halo) · [Install](INSTALL.md) · [Migration](MIGRATION-3.1.md) · [Guard tool](docs/HALO_GUARD_TOOL.md) · [Source](https://github.com/Null9797/halo-tv/releases/download/v3.2.2-halo/HaloTV-3.2.2-source.zip)

[YanGN Bing archive](https://github.com/ygnstudio/bing_wallpaper_archive) supplies the Bing catalogue; the online video catalogue references [Aerial Views](https://github.com/theothernt/AerialViews), with Apple-hosted media. Rights remain with their respective owners; code licensing does not grant media rights.

Source archives and APKs are maintained in [Releases](https://github.com/Null9797/halo-tv/releases), including historical versions. See the [documentation index](docs/README.md) for release notes and maintenance guides.
