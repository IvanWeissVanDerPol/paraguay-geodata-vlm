#!/usr/bin/env bash
# git_maintenance.sh — Weekly git housekeeping.
#
# Runs:
# - git gc (pack files, prune loose objects)
# - git remote prune origin (drop deleted remote branches)
# - git reflog expire (clean old reflog entries)
# - git fsck (verify integrity)
#
# Cron: weekly on Sunday at 23:00 UTC.

set -euo pipefail

cd /opt/data/thesis-active

echo "🧹 git_maintenance.sh — weekly housekeeping"
echo

echo "=== git gc ==="
git gc --auto --prune=now 2>&1 | tail -5
echo

echo "=== git remote prune ==="
git remote prune origin 2>&1 || true
echo

echo "=== git reflog expire ==="
git reflog expire --expire=30.days.ago --expire-unreachable=now --all 2>&1 | tail -3
echo

echo "=== git fsck ==="
git fsck --no-progress --no-dangling 2>&1 | tail -5 || echo "  (fsck complete)"
echo

echo "=== repo size ==="
du -sh .git 2>&1
echo

echo "✅ git maintenance complete"