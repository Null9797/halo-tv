#!/usr/bin/env bash
# HaloTV independent-edition guard diagnostics. No APK download or system launcher changes.
# TV=192.168.0.130 bash tools/halo-guard.sh           # read-only diagnostics
# TV=192.168.0.130 bash tools/halo-guard.sh --repair  # explicitly grant/repair HaloTV guard
set -euo pipefail
command -v python3 >/dev/null || { echo '需要 Python 3，请安装后重试。' >&2; exit 2; }
exec python3 "$(dirname "$0")/halo_guard.py" "$@"
