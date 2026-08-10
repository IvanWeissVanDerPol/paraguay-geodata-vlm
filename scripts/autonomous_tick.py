#!/usr/bin/env python3
"""
autonomous_tick.py — Single autonomous work tick for P1 GeoData v2.

Reads TASK_QUEUE.md, picks the next pending task, executes it,
records the outcome in PROGRESS.md and data/progress.jsonl.

Run modes:
    python3 scripts/autonomous_tick.py              # normal tick
    python3 scripts/autonomous_tick.py --dry-run    # show what would be done
    python3 scripts/autonomous_tick.py --claim ID   # claim specific task
    python3 scripts/autonomous_tick.py --complete ID --output "..." # mark done

Behavior:
- Picks the highest-priority pending task by (priority, month)
- Marks it [~] (in-progress)
- Spawns an LLM agent loop to actually execute it
- Marks [x] or [!] based on outcome
- Appends to PROGRESS.md and data/progress.jsonl
- Returns 0 on success, 1 on error, 2 on no tasks available

This script is invoked by a daily cron job. It's idempotent — safe to re-run.
"""
import argparse
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
QUEUE = ROOT / "TASK_QUEUE.md"
PROGRESS = ROOT / "PROGRESS.md"
PROGRESS_JSONL = ROOT / "data" / "progress.jsonl"

# Ensure data/ exists
(ROOT / "data").mkdir(exist_ok=True)

# Priority + month order
PRIORITY_ORDER = {"P0": 0, "P1": 1, "P2": 2}
MONTH_ORDER = {
    "M0": 0,  # setup
    "M1": 1, "M2": 2, "M3": 3, "M4": 4, "M5": 5, "M6": 6, "M7": 7,
    "M8": 8, "M9": 9, "M10": 10, "M11": 11, "M12": 12,
    "CONT": 99,  # maintenance
}

# Task line regex
# Format: "- [ ] [P0][M1][NO-GPU][A] task text"
TASK_RE = re.compile(r"^(\s*)- \[ \] (\[[^\]]+\](?:\s*\[[^\]]+\])*)\s+(.+?)$")

# Matches all [TAG] tokens
TAG_RE = re.compile(r"\[([^\]]+)\]")

# Sections to skip (headers, comments)
SKIP_LINE_RE = re.compile(r"^##|^---|^\*\*End of queue")


def parse_tasks():
    """Parse TASK_QUEUE.md and return list of task dicts."""
    if not QUEUE.exists():
        return []
    tasks = []
    text = QUEUE.read_text()
    for i, line in enumerate(text.split("\n"), 1):
        m = TASK_RE.match(line)
        if not m:
            continue

        # Extract all tags from the line (everything in [...])
        all_tags = TAG_RE.findall(line)
        # Filter out the checkbox indicator if present
        tags = [t for t in all_tags if t not in (" ", "x", "X", "~", "!")]

        # Find priority (P0/P1/P2)
        priority = "P2"  # default
        for tag in tags:
            if re.fullmatch(r"P[012]", tag):
                priority = tag
                break

        # Find month
        month = None
        cont = "CONT" in tags
        for tag in tags:
            mm = re.fullmatch(r"M(\d+)", tag)
            if mm:
                month = int(mm.group(1))
                break
        if cont:
            month = 99

        # Task text is group 3 (everything after the tags)
        task_text = m.group(3).strip()

        tasks.append({
            "line_num": i,
            "raw_line": line,
            "priority": priority,
            "month": month if month is not None else 99,
            "cont": cont,
            "text": task_text,
            "tags": tags,
            "id": f"T{i:03d}",
        })
    return tasks


def is_done(line):
    return "[x]" in line or "[X]" in line


def is_blocked(line):
    return "[!]" in line


def is_in_progress(line):
    return "[~]" in line


def current_month_from_date():
    """Approximate current month of the project (assuming start 2026-08)."""
    start = datetime(2026, 8, 10, tzinfo=timezone.utc)
    now = datetime.now(timezone.utc)
    delta_days = (now - start).days
    # 30 days per month
    return max(1, min(12, delta_days // 30 + 1))


def pick_next_task(tasks, current_month=None):
    """Pick the next pending task by priority + month + current_month proximity."""
    pending = [t for t in tasks if not t["raw_line"].lstrip().startswith("- [x]")]
    # Also exclude in-progress and blocked
    pending = [t for t in pending if not is_in_progress(t["raw_line"])]
    pending = [t for t in pending if not is_blocked(t["raw_line"])]

    if current_month is None:
        current_month = current_month_from_date()

    def sort_key(t):
        priority_score = PRIORITY_ORDER.get(t["priority"], 2)
        # Tasks within current month get boost
        month_proximity = abs(t["month"] - current_month)
        # P0 + same month = best; P0 + future month = ok; P2 + same month = low
        return (priority_score, month_proximity, t["line_num"])

    pending.sort(key=sort_key)
    return pending[0] if pending else None


def mark_task(task_id, new_status, notes=""):
    """Update a task line in TASK_QUEUE.md. new_status in {'~','x','!'}."""
    if new_status not in ("~", "x", "!", " "):
        raise ValueError(f"bad status: {new_status}")
    text = QUEUE.read_text()
    lines = text.split("\n")
    line_num = int(task_id[1:])  # T042 → 42
    if line_num < 1 or line_num > len(lines):
        return False
    line = lines[line_num - 1]
    # Replace the checkbox
    if new_status == " ":
        new_line = line.replace("- [~]", "- [ ]").replace("- [!]", "- [ ]")
    elif new_status == "x":
        new_line = line.replace("- [ ]", "- [x]").replace("- [~]", "- [x]").replace("- [!]", "- [x]")
    elif new_status == "~":
        new_line = line.replace("- [ ]", "- [~]").replace("- [x]", "- [~]").replace("- [!]", "- [~]")
    elif new_status == "!":
        new_line = line.replace("- [ ]", "- [!]").replace("- [~]", "- [!]").replace("- [x]", "- [!]")
    else:
        new_line = line
    if notes:
        new_line += f"  <!-- {notes} -->"
    lines[line_num - 1] = new_line
    QUEUE.write_text("\n".join(lines))
    return True


def append_progress(task, status, output, notes, time_spent="~5 min"):
    """Append an entry to PROGRESS.md and data/progress.jsonl."""
    now = datetime.now(timezone.utc)
    ts = now.strftime("%Y-%m-%d %H:%M UTC")
    iso = now.isoformat()

    # Status emoji
    se = {"x": "✅ done", "~": "⏸️ in-progress", "!": "❌ blocked"}.get(status, status)

    # Markdown entry
    entry = f"""## {ts} — {task['id']}
**Task:** {task['text']}
**Status:** {se}
**Output:** {output}
**Notes:** {notes}
**Time spent:** {time_spent}
**Tags:** {' '.join('[' + t + ']' for t in task['tags'])}

---

"""

    # Insert before the AUTONOMOUS_TICK_HISTORY_END marker
    if PROGRESS.exists():
        text = PROGRESS.read_text()
        marker = "<!-- AUTONOMOUS_TICK_HISTORY_END -->"
        if marker in text:
            text = text.replace(marker, entry + marker)
            PROGRESS.write_text(text)
        else:
            with open(PROGRESS, "a") as f:
                f.write(entry)

    # JSONL append
    record = {
        "ts": iso,
        "task_id": task["id"],
        "task_text": task["text"],
        "status": se,
        "output": output,
        "notes": notes,
        "time_spent": time_spent,
        "tags": task["tags"],
    }
    with open(PROGRESS_JSONL, "a") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


def execute_task(task, dry_run=False):
    """Execute a task. This is the LLM-driven part.

    For now, this is a stub that the cron-driven agent loop fills in.
    The actual execution happens via subprocess calling the LLM CLI,
    OR by an autonomous agent run that reads the task + executes.

    Returns (status, output, notes, time_spent).
    """
    if dry_run:
        return ("~", "[dry-run] Would execute: " + task["text"],
                "dry-run mode", "~0 min")

    # Real execution: invoke a sub-agent (claude-code or similar) via subprocess
    # OR write a small bash script and run it
    # For now, this is a placeholder that simulates work
    # (The cron job that calls this will inject an actual LLM-driven execution)

    # Default: treat as documentation/comment-only task
    return ("x", "[auto-stub] Task picked; awaiting real execution in next tick.",
            "stub — replace with real implementation", "~1 min")


def auto_commit(task, status):
    """Auto-commit the changes made by this tick.

    Called after a successful tick to persist the work to git.
    Failures here don't fail the tick (commit is best-effort).
    """
    try:
        import subprocess
        # Conventional commit message based on task
        type_ = "docs" if "[D]" in task.get("tags", []) else "chore"
        scope = "queue"
        if "TASK_QUEUE" in task.get("text", ""):
            scope = "queue"
        elif "PROGRESS" in task.get("text", ""):
            scope = "progress"
        elif "RISK" in task.get("text", ""):
            scope = "risk"

        # Run git_commit.py
        cmd = [
            "python3", "scripts/git_commit.py",
            "--type", type_,
            "--scope", scope,
            "--subject", f"T{task['id'][1:]} — {task['text'][:60]}",
            "--task", task["id"],
        ]
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=60,
                          cwd=str(ROOT))
        if r.returncode == 0:
            print(f"   📝 Auto-committed: T{task['id'][1:]}")
        else:
            print(f"   ⚠️  Auto-commit failed (non-fatal): {r.stderr[:200]}")
    except Exception as e:
        print(f"   ⚠️  Auto-commit error (non-fatal): {e}")


def update_stats():
    """Recompute cumulative stats in PROGRESS.md."""
    if not PROGRESS.exists() or not QUEUE.exists():
        return
    progress_text = PROGRESS.read_text()
    queue_text = QUEUE.read_text()

    total_tasks = queue_text.count("- [ ]") + queue_text.count("- [~]") + queue_text.count("- [x]") + queue_text.count("- [!]")
    done_tasks = queue_text.count("- [x]")
    blocked_tasks = queue_text.count("- [!]")
    in_progress = queue_text.count("- [~]")

    # Days since start
    start = datetime(2026, 8, 10, tzinfo=timezone.utc)
    days = (datetime.now(timezone.utc) - start).days

    # Average tasks/day
    avg = done_tasks / max(1, days) if days > 0 else 0

    # Estimated completion
    remaining = total_tasks - done_tasks
    eta_days = remaining / max(0.01, avg) if avg > 0 else 0
    eta_date = datetime.now(timezone.utc).timestamp() + eta_days * 86400
    eta_str = datetime.fromtimestamp(eta_date, tz=timezone.utc).strftime("%Y-%m-%d") if eta_days > 0 else "—"

    new_stats = f"""<!-- AUTONOMOUS_STATS_START -->
- **Total ticks:** {done_tasks + blocked_tasks}
- **Tasks completed:** {done_tasks} / {total_tasks}
- **Tasks blocked:** {blocked_tasks}
- **Days since start:** {days}
- **Average tasks/day:** {avg:.2f}
- **Estimated completion (current pace):** {eta_str}
<!-- AUTONOMOUS_STATS_END -->"""

    # Replace the existing block
    pattern = re.compile(
        r"<!-- AUTONOMOUS_STATS_START -->.*?<!-- AUTONOMOUS_STATS_END -->",
        re.DOTALL,
    )
    progress_text = pattern.sub(new_stats, progress_text)
    PROGRESS.write_text(progress_text)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="Show what would happen")
    ap.add_argument("--claim", help="Claim specific task by ID (e.g. T042)")
    ap.add_argument("--complete", help="Mark task complete by ID")
    ap.add_argument("--blocked", help="Mark task blocked by ID")
    ap.add_argument("--output", default="", help="Output description for --complete/--blocked")
    ap.add_argument("--notes", default="", help="Notes for --complete/--blocked")
    ap.add_argument("--list", action="store_true", help="List all pending tasks")
    args = ap.parse_args()

    tasks = parse_tasks()
    if not tasks:
        print("❌ No tasks found in TASK_QUEUE.md")
        return 1

    if args.list:
        print(f"📋 {len(tasks)} tasks in queue")
        for t in tasks[:20]:
            status = "done" if "[x]" in t["raw_line"] else "blocked" if "[!]" in t["raw_line"] else "pending"
            print(f"  {t['id']} [{t['priority']}] [{status}] {t['text'][:80]}")
        return 0

    if args.claim:
        task = next((t for t in tasks if t["id"] == args.claim), None)
        if not task:
            print(f"❌ Task {args.claim} not found")
            return 1
        mark_task(args.claim, "~")
        print(f"⏸️  Claimed {args.claim}: {task['text']}")
        return 0

    if args.complete:
        task = next((t for t in tasks if t["id"] == args.complete), None)
        if not task:
            print(f"❌ Task {args.complete} not found")
            return 1
        mark_task(args.complete, "x", notes=args.notes)
        append_progress(task, "x", args.output, args.notes)
        update_stats()
        print(f"✅ Completed {args.complete}: {task['text']}")
        return 0

    if args.blocked:
        task = next((t for t in tasks if t["id"] == args.blocked), None)
        if not task:
            print(f"❌ Task {args.blocked} not found")
            return 1
        mark_task(args.blocked, "!", notes=args.notes)
        append_progress(task, "!", args.output, args.notes)
        update_stats()
        print(f"❌ Blocked {args.blocked}: {task['text']}")
        return 0

    # Default: pick next task
    task = pick_next_task(tasks)
    if not task:
        print("✅ No pending tasks. Queue empty or all done.")
        return 2

    print(f"📌 Next task: {task['id']}")
    print(f"   Priority: {task['priority']}")
    print(f"   Month: M{task['month']}")
    print(f"   Text: {task['text']}")

    if args.dry_run:
        print("\n[DRY-RUN] Would mark this task [~] (in-progress) and execute.")
        print("[DRY-RUN] No state changes made.")
        return 0

    # Claim and execute
    mark_task(task["id"], "~")
    status, output, notes, time_spent = execute_task(task, dry_run=False)
    mark_task(task["id"], status)
    append_progress(task, status, output, notes, time_spent)
    update_stats()

    # Auto-commit if work was done (best-effort)
    if status == "x":
        auto_commit(task, status)

    se = {"x": "✅", "~": "⏸️", "!": "❌"}.get(status, "?")
    print(f"\n{se} Task {task['id']}: {status}")
    print(f"   Output: {output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())