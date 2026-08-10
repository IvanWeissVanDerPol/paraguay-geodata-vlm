#!/usr/bin/env bash
# thesis-weekly.sh — Cron entry point for weekly review.
# Runs weekly_review.py which summarizes the past week and writes
# recommendations to PROGRESS.md.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

cd "$PROJECT_ROOT"

if [[ -f ".venv/bin/activate" ]]; then
    source .venv/bin/activate
fi

python3 scripts/weekly_review.py 2>&1 | tee -a logs/weekly.log || true