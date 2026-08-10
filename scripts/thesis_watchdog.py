#!/usr/bin/env python3
"""
thesis_watchdog.py — Check heartbeat and trigger work if stale.

Logic:
- Read data/heartbeat.txt for last work timestamp
- If < 15 min old: do nothing (someone is working)
- If 15 min - 6 hours: log warning
- If > 6 hours: trigger a tick (start a fresh session)
- If > 24 hours: trigger urgent resume via WhatsApp

The watchdog itself doesn't do work — it just signals. The actual work
happens in a separate cron job (thesis-auto-resume) that runs when the
watchdog detects staleness.

Run modes:
    python3 scripts/thesis_watchdog.py                # normal check
    python3 scripts/thesis_watchdog.py --check-only    # just report status
    python3 scripts/thesis_watchdog.py --force        # force a resume signal
"""
import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HEARTBEAT = ROOT / "data" / "heartbeat.txt"
HEARTBEAT_LOG = ROOT / "data" / "heartbeat.log"
RESUME_FLAG = ROOT / "data" / "resume_needed.flag"

# Thresholds (seconds)
WARN_THRESHOLD = 15 * 60          # 15 min
RESUME_THRESHOLD = 6 * 60 * 60    # 6 hours
URGENT_THRESHOLD = 24 * 60 * 60   # 24 hours


def parse_heartbeat():
    """Read heartbeat.txt and return datetime, or None if missing."""
    if not HEARTBEAT.exists():
        return None
    text = HEARTBEAT.read_text().strip()
    try:
        # ISO 8601
        return datetime.fromisoformat(text.replace("Z", "+00:00"))
    except Exception:
        return None


def age_seconds(ts):
    if ts is None:
        return None
    now = datetime.now(timezone.utc)
    return (now - ts).total_seconds()


def human_age(secs):
    if secs is None:
        return "never"
    if secs < 60:
        return f"{int(secs)}s"
    if secs < 3600:
        return f"{int(secs // 60)}m {int(secs % 60)}s"
    if secs < 86400:
        h = int(secs // 3600)
        m = int((secs % 3600) // 60)
        return f"{h}h {m}m"
    return f"{int(secs // 86400)}d"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check-only", action="store_true",
                    help="Just report status, no action")
    ap.add_argument("--force", action="store_true",
                    help="Force a resume signal (manual override)")
    args = ap.parse_args()

    last_work = parse_heartbeat()
    age = age_seconds(last_work)

    print("=" * 60)
    print("🐕 Thesis Watchdog")
    print("=" * 60)
    if last_work:
        print(f"Last work:    {last_work.isoformat()}")
    else:
        print(f"Last work:    NEVER (heartbeat missing)")
    print(f"Age:          {human_age(age)}")
    print(f"Now:          {datetime.now(timezone.utc).isoformat()}")
    print()

    # Decision logic
    if args.force:
        action = "force-resume"
        reason = "manual override"
    elif age is None:
        action = "urgent-resume"
        reason = "no heartbeat ever recorded"
    elif age < WARN_THRESHOLD:
        action = "ok"
        reason = f"work is recent ({human_age(age)} ago)"
    elif age < RESUME_THRESHOLD:
        action = "warn"
        reason = f"no work for {human_age(age)} (threshold: 15min-6h)"
    elif age < URGENT_THRESHOLD:
        action = "resume"
        reason = f"stale {human_age(age)} — resume needed (threshold: 6h)"
    else:
        action = "urgent-resume"
        reason = f"very stale {human_age(age)} — urgent resume (threshold: 24h)"

    print(f"Decision:     {action}")
    print(f"Reason:       {reason}")
    print()

    # Report only mode
    if args.check_only:
        return 0 if action == "ok" else 1

    # Touch heartbeat for the watchdog itself
    subprocess.run(["bash", "scripts/thesis-heartbeat.sh", f"watchdog: {action}"],
                   cwd=str(ROOT), check=True, timeout=15)

    # Act based on decision
    if action in ("resume", "urgent-resume", "force-resume"):
        # Set the resume flag
        RESUME_FLAG.parent.mkdir(parents=True, exist_ok=True)
        RESUME_FLAG.write_text(json.dumps({
            "flagged_at": datetime.now(timezone.utc).isoformat(),
            "reason": reason,
            "last_work": last_work.isoformat() if last_work else None,
            "age_seconds": age,
        }, indent=2))
        print(f"🚨 RESUME FLAG SET → {RESUME_FLAG.relative_to(ROOT)}")
        print(f"   The next 'thesis-auto-resume' cron tick will pick this up.")
        print(f"   (Every 15 min; cron job ID will be created)")
    elif action == "warn":
        # Don't set flag, just log
        print(f"⚠️  WARN: {reason}")
        print(f"   No resume triggered yet; will trigger after 6h of staleness.")
    else:
        print(f"✅ OK: {reason}")
        if RESUME_FLAG.exists():
            # Clear stale flag if work resumed
            RESUME_FLAG.unlink()
            print(f"   Cleared stale resume flag.")

    return 0


if __name__ == "__main__":
    sys.exit(main())