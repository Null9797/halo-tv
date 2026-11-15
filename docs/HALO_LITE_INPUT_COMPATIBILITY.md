# Lite source-picker compatibility test — 2026-11-15

Base: 3.2.2 quiz input repair, commit 59d6a4a. Independent Lite code 75,
versionName 3.2.2. Standard/Guard remain unchanged. Local test delivery only.

## Report and limits

A user reported that an older Sharp TV can change inputs from its own settings
but not from HaloTV Lite Control Center. Exact model, Android version and
device logs were not supplied. This is a compatibility improvement, not a
claim that the reporter's hardware was reproduced or validated.

The existing code had a fixed Foxconn activity and an implicit MStar SOURCE_INFO
intent. Resolving with flags 0 does not establish that startActivity will accept
the same implicit intent: DEFAULT may be missing. There was no usable settings
fallback on the failed-input path. A successful OEM picker also left Halo's
Control Center behind it on most routes.

## Changes

- Explicitly start accessible components from the MStar SOURCE_INFO action,
  including matching filters without DEFAULT. Retain the documented Foxconn and
  SourceInfoActivity routes and handle launch rejection by trying another route.
- Discover renamed public source-picker activities only inside the two known
  enabled system firmware packages. Exclude private, disabled, permission-gated,
  factory, engineering, reset, calibration, debug and upgrade activities.
- Detect firmware capabilities rather than relying on SHARP manufacturer/model
  strings. Keep the original priority of other OEM input services/broadcasts.
- On MStar firmware, expose a small input page with a native picker action and
  a system-settings fallback. If other firmware has no recognized route, show
  that same usable fallback instead of claiming the TV has no inputs.
- Close Control Center after a successful native launch. Settings fallback
  still goes through the existing parental authorization callback.
- Focus the first input action when the input page opens; provide all new
  labels/help in the existing five languages.

No port IDs were guessed, no private methods or ADB/root calls were added,
and no firmware settings are written by this change. Opening the system page
does not assert that HaloTV itself has selected a port.

## Evidence

- Upstream report for Foxconn/MStar Sharp CVTM648:
  https://github.com/pengchujin/aerial-tv/issues/1048
- Upstream report for Sharp LCD_xxSFFOC470A and SourceInfoActivity:
  https://github.com/pengchujin/aerial-tv/issues/1342
- Android's implicit/default category and explicit intent behavior:
  https://developer.android.com/guide/components/intents-filters

The historical reports concern Android 6 firmware, not the unidentified older
TV in this report. Runtime component detection and the system-settings fallback
address that uncertainty; only testing on the affected TV can confirm results.

## Validation scope

Host-side tests cover no-DEFAULT matching, missing action filters, non-exported
and rejected activities, bounded discovery, system-app restrictions, blocked
factory/private pages, parent authorization for settings, and closing Control
Center after launch. No emulator or TV is used, per the user's standing request.

Final results: all 172 Lite host tests passed (including 18 new source-picker
checks across SDK 23 and 28), release build succeeded, Lint reported zero
Error/Fatal findings and 426 warnings. Package identity, code 75, independent
certificate, APK ZIP CRC and alignment were verified. Android 4.x runtime and
the affected Sharp firmware remain unverified; minSdk is still 14.

## 3.2.3 release

The fixes are included in the 3.2.3 independent release (Standard/Guard code 220, Lite code 76). The earlier test-build results above are retained as history. See releases/RELEASE-3.2.3.md for the combined release scope. No TV/emulator validation is implied.
