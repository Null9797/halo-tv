# HaloTV quiz input repair — 2026-11-15 (local test build)

Based on the published 3.2.2 sources. Independent Standard/Guard use code 219;
Lite uses code 74. Keep versionName 3.2.2 pending the user's release decision.
Future public updates must account for these test codes. No artwork changes.

## Findings

- Home embeds the native QuizPanel below a Compose PIN. The native descendants
  remained focusable while the PIN was visible, and queued focus restoration or
  size changes could compete with the PIN's initial focus. This is consistent
  with the reported unresponsive modal; it does not establish that every reported
  freeze is an ANR.
- Focused action buttons used a purple fill and a similar purple border.
- Size changes rebuilt the quiz, losing visual answer selection and posting a
  fresh focus request. Native button key handling did not explicitly tie an OK
  release to the same control that received its down event.
- The service overlay used a separate EditText PIN flow, relying on a keyboard
  that many TV remotes/overlay windows cannot operate.
- Lite rebuilt all answer controls after every selection. Its manual focus
  highlight also remained visible behind the parental modal.

## Changes

- Suspend native focus, keys and touches immediately when opening Home's PIN;
  keep the AndroidView's Compose focus target disabled until the PIN closes.
  Restore focus on cancel, without changing answers or question number.
- Use light gold action focus with dark text and a thick purple outline.
  Lite now uses the same contrast, with checks separate from its focus outline.
- Keep D-pad navigation inside the quiz; consume OK only when down/up belong to
  the same attached, focused control. Cancel presses on page changes, loss of
  window focus, detachment, or modal suspension.
- Coalesce size-change rebuilds and reject stale queued focus requests. Restore
  selected-answer visuals and submit availability after a rebuild/PIN cancel.
- Provide a native 0–9 keypad, delete key, wrong-PIN message and Back handling in
  the service overlay. Arrow PINs still use direct remote arrows. Preserve partial
  PIN input across resizing; verify once before exiting children's mode.
- Ignore held-number repeats in both existing PIN implementations.
- Update Lite answer controls in place. Suspend the underlying quiz while a
  higher sheet is open, then restore its focus when the sheet closes.

## Regression coverage

Host-side Robolectric tests exercise the real native quiz and Compose PIN
together: opening after submit, repeated open/cancel/verify, keyboard focus
exclusion, five-question navigation, answer persistence, contrast colors,
canceled/unpaired OK releases, native numeric/arrow PINs, wrong PIN recovery,
resizing, Lite control retention and held-number input.

Per the user's instruction, no emulator or television was operated. TV firmware,
overlay permission behavior and physical remote timing still require user testing.
Do not claim that all device-specific freezes are ruled out. No publication or
remote announcement is part of this fix.

Final verification: Standard 501, Guard 501, Lite 154 host tests passed (1,156
total). All three release APKs built, with zero Lint Error/Fatal findings;
existing warnings remain (344 / 345 / 425). APK certificate, identity, version,
ZIP CRC and alignment were checked. A concurrent test run hit the existing
PhoneServerRecoveryTest fixed-port assertion (8792 rather than 8791); serial
execution passed, without changing phone-server production behavior.

## 3.2.3 release

The fixes are included in the 3.2.3 independent release (Standard/Guard code 220, Lite code 76). The earlier test-build results above are retained as history. See releases/RELEASE-3.2.3.md for the combined release scope. No TV/emulator validation is implied.
