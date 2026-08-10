#!/usr/bin/env bash
# thesis-tick.sh — Cron entry point for daily autonomous tick.
# Runs the python tick script which picks the next task, executes it,
# and updates PROGRESS.md. The script handles everything; this is just
# a thin wrapper to ensure proper working directory + activation.

set -euo pipefail

# Resolve project root from script location
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

cd "$PROJECT_ROOT"

# Activate venv
if [[ -f ".venv/bin/activate" ]]; then
    source .venv/bin/activate
fi

# Run the tick
python3 scripts/autonomous_tick.py 2>&1 | tee -a logs/tick.log || true

# Optional: append a one-liner status
STATUS=$(grep -c "^- \[x\]" TASK_QUEUE.md 2>/dev/null || echo 0)
echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] Tick complete. Done tasks: $STATUS"