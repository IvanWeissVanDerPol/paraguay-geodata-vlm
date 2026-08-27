#!/usr/bin/env python3
"""
weekly_review.py — Weekly summary of autonomous progress.

Reads PROGRESS.md and data/progress.jsonl, computes:
- Tasks completed this week
- Tasks still blocked
- Top 3 priorities for next week
- Recommended actions
- Risk register updates needed

Run: make weekly
"""
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
QUEUE = ROOT / "TASK_QUEUE.md"
PROGRESS = ROOT / "PROGRESS.md"
PROGRESS_JSONL = ROOT / "data" / "progress.jsonl"
RISK_REGISTER = ROOT / "RISK_REGISTER.md"


def load_records():
    if not PROGRESS_JSONL.exists():
        return []
    records = []
    for line in PROGRESS_JSONL.read_text().splitlines():
        s = line.strip()
        if not s:
            continue
        # Skip non-JSON log lines (e.g. watchdog notices, partial writes).
        # Defensive: don't let one malformed entry crash the weekly review.
        try:
            records.append(json.loads(s))
        except json.JSONDecodeError:
            continue
    # Only keep tick-style records (have ts + status + task_id); skip
    # watchdog summary entries that use alternate schemas.
    return [r for r in records if {"ts", "status", "task_id"} <= r.keys()]


def parse_tasks():
    if not QUEUE.exists():
        return []
    text = QUEUE.read_text()
    tasks = []
    for line in text.split("\n"):
        if not line.lstrip().startswith("- [") or "[P" not in line:
            continue
        tags = re.findall(r"\[([^\]]+)\]", line)
        priority = next((t for t in tags if re.fullmatch(r"P[012]", t)), "P2")
        status = "pending"
        if "[x]" in line or "[X]" in line:
            status = "done"
        elif "[!]" in line:
            status = "blocked"
        elif "[~]" in line:
            status = "in-progress"
        # Text
        m = re.match(r"^\s*- \[[ xX~!]\] (?:\[[^\]]+\]\s*)+(.+?)$", line)
        text_only = m.group(1).strip() if m else line
        tasks.append({
            "priority": priority,
            "status": status,
            "text": text_only,
            "tags": tags,
        })
    return tasks


def main():
    records = load_records()
    tasks = parse_tasks()

    print("=" * 70)
    print(f"📊 WEEKLY REVIEW — {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    print("=" * 70)

    # Last 7 days
    cutoff = datetime.now(timezone.utc) - timedelta(days=7)
    recent = [r for r in records
              if datetime.fromisoformat(r["ts"]).replace(tzinfo=timezone.utc) > cutoff]

    # All-time stats
    done_tasks = [t for t in tasks if t["status"] == "done"]
    blocked_tasks = [t for t in tasks if t["status"] == "blocked"]
    pending_tasks = [t for t in tasks if t["status"] == "pending"]
    in_progress = [t for t in tasks if t["status"] == "in-progress"]

    print(f"\n📈 All-time stats:")
    print(f"  Total tasks: {len(tasks)}")
    print(f"  Done:        {len(done_tasks)} ({len(done_tasks)/len(tasks)*100:.0f}%)")
    print(f"  Blocked:     {len(blocked_tasks)}")
    print(f"  In-progress: {len(in_progress)}")
    print(f"  Pending:     {len(pending_tasks)}")

    print(f"\n📅 Last 7 days:")
    print(f"  Ticks:       {len(recent)}")
    done_recent = [r for r in recent if "done" in r["status"]]
    blocked_recent = [r for r in recent if "blocked" in r["status"]]
    print(f"  Completed:   {len(done_recent)}")
    print(f"  Blocked:     {len(blocked_recent)}")

    # Tasks by priority (pending)
    by_priority = Counter(t["priority"] for t in pending_tasks)
    print(f"\n📌 Pending tasks by priority:")
    for p in ["P0", "P1", "P2"]:
        print(f"  {p}: {by_priority.get(p, 0)}")

    # Top 3 next tasks
    pending_sorted = sorted(
        pending_tasks,
        key=lambda t: ({"P0": 0, "P1": 1, "P2": 2}.get(t["priority"], 2), t["text"])
    )
    print(f"\n🎯 Top 3 next tasks (by priority):")
    for t in pending_sorted[:3]:
        print(f"  [{t['priority']}] {t['text'][:80]}")

    # Blockers
    if blocked_tasks:
        print(f"\n🚧 Current blockers ({len(blocked_tasks)}):")
        for t in blocked_tasks[:5]:
            print(f"  [{t['priority']}] {t['text'][:80]}")

    # Recent task distribution
    if recent:
        by_day = defaultdict(int)
        for r in recent:
            day = r["ts"][:10]
            by_day[day] += 1
        print(f"\n📆 Ticks per day (last 7):")
        for day in sorted(by_day.keys()):
            print(f"  {day}: {by_day[day]}")

    # Burndown estimate
    if recent:
        days_active = max(1, (datetime.now(timezone.utc) - datetime.fromisoformat(records[0]["ts"]).replace(tzinfo=timezone.utc)).days)
        rate = len(done_recent) / days_active
        remaining = len(pending_tasks)
        if rate > 0:
            eta_days = remaining / rate
            eta_date = datetime.now(timezone.utc) + timedelta(days=eta_days)
            print(f"\n⏱️  Burndown estimate:")
            print(f"  Rate: {rate:.2f} tasks/day")
            print(f"  Remaining: {remaining}")
            print(f"  ETA: {eta_date.strftime('%Y-%m-%d')} ({eta_days:.0f} days)")

    # Recommendations
    print(f"\n💡 Recommendations for next week:")
    if blocked_tasks:
        print(f"  → Resolve {len(blocked_tasks)} blocked task(s) — see blockers above")
    p0_pending = [t for t in pending_tasks if t["priority"] == "P0"]
    if p0_pending:
        print(f"  → Focus on {len(p0_pending)} P0 tasks: see top 3 above")
    if not records:
        print(f"  → Run 'make tick' daily to start building momentum")
    if not any("EXT" in t["text"] for t in done_tasks):
        print(f"  → Reminder: many tasks need [EXT] credentials (Copernicus, HF, GH)")
        print(f"     Pass secrets/creds.json to Erebus when ready")

    # Risk register sync
    if RISK_REGISTER.exists():
        risks_text = RISK_REGISTER.read_text()
        # Risks have IDs like T1, D2, P3, E4, S5 (single letter + digits)
        risk_ids = re.findall(r"\|\s*([TDESP]\d+)\s*\|", risks_text)
        print(f"\n⚠️  Risk register: {len(risk_ids)} risks tracked")

    # Write weekly summary section
    weekly_section = f"""## {datetime.now(timezone.utc).strftime('%Y-%m-%d')} — weekly review
- Completed this week: {len(done_recent)}
- Blocked: {len(blocked_recent)}
- Top priority: {pending_sorted[0]['text'][:60] if pending_sorted else 'none'}

"""
    if PROGRESS.exists():
        text = PROGRESS.read_text()
        # Insert before DAILY_SUMMARY block
        marker = "<!-- AUTONOMOUS_DAILY_SUMMARY_START -->"
        if marker in text:
            text = text.replace(marker, weekly_section + marker, 1)
            PROGRESS.write_text(text)

    print(f"\n{'=' * 70}")
    print(f"✅ Weekly review written to PROGRESS.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())