#!/usr/bin/env bash
# thesis-heartbeat.sh — Touch the heartbeat file (called after any work).
#
# Usage:
#   bash scripts/thesis-heartbeat.sh           # touch with current timestamp
#   bash scripts/thesis-heartbeat.sh "msg"     # touch + log a reason

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

HEARTBEAT="$PROJECT_ROOT/data/heartbeat.txt"
HEARTBEAT_LOG="$PROJECT_ROOT/data/heartbeat.log"

NOW=$(date -u +%Y-%m-%dT%H:%M:%SZ)
MSG="${1:-work-in-progress}"

# Touch heartbeat
echo "$NOW" > "$HEARTBEAT"

# Append to log
echo "$NOW  $MSG" >> "$HEARTBEAT_LOG"

# Trim log to last 1000 lines
if [[ -f "$HEARTBEAT_LOG" ]] && [[ $(wc -l < "$HEARTBEAT_LOG") -gt 1000 ]]; then
    tail -n 500 "$HEARTBEAT_LOG" > "$HEARTBEAT_LOG.tmp"
    mv "$HEARTBEAT_LOG.tmp" "$HEARTBEAT_LOG"
fi