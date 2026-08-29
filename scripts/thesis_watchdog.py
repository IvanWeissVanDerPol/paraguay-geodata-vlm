#!/usr/bin/env python3
"""
thesis_watchdog.py — Check heartbeat and trigger work if stale.

Logic:
- Read data/heartbeat.txt for last work timestamp
- If < 15 min old: do nothing (someone is working)
- If 15 min - 6 hours: log warning
- If > 6 hours: trigger a tick (start a fresh session)
- If > 24 hours: trigger urgent resume via Mensaje

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
HEARTBEAT_DIR = ROOT / "data"
RESUME_FLAG = ROOT / "data" / "resume_needed.flag"

# Canonical heartbeat paths AND all heartbeat* siblings — read freshest.
# Different cron scripts touch different filenames over time, so a single-path
# read can produce false-positive stale alerts. We accept the freshest valid
# ISO-8601 timestamp across the whole data/heartbeat* family.
HEARTBEAT_FILES = [
    ROOT / "data" / "heartbeat",
    ROOT / "data" / "heartbeat.txt",
    ROOT / "data" / "heartbeat.ts",
    ROOT / "data" / "heartbeat.timestamp",
    ROOT / "data" / "heartbeat.touch",
    ROOT / "data" / "heartbeat_watchdog",
]

# Thresholds (seconds)
WARN_THRESHOLD = 15 * 60          # 15 min
RESUME_THRESHOLD = 6 * 60 * 60    # 6 hours
URGENT_THRESHOLD = 24 * 60 * 60   # 24 hours


def _parse_iso(text):
    """Parse ISO-8601, return timezone-aware datetime or None.

    Multi-line files are common (e.g. data/heartbeat is sometimes written
    with one timestamp per line by different cron scripts). Return the
    freshest valid timestamp found anywhere in the text.
    """
    candidates = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            candidates.append(datetime.fromisoformat(line.replace("Z", "+00:00")))
        except Exception:
            continue
    if not candidates:
        return None
    return max(candidates)


def parse_heartbeat():
    """Read every data/heartbeat* file and return the freshest timestamp.

    Returns None only if no heartbeat-shaped file contains a valid timestamp.
    """
    candidates = []
    for path in HEARTBEAT_FILES:
        if not path.exists():
            continue
        try:
            ts = _parse_iso(path.read_text())
        except Exception:
            ts = None
        if ts is not None:
            candidates.append((path, ts))
    if not candidates:
        return None
    # Freshest wins.
    candidates.sort(key=lambda kv: kv[1], reverse=True)
    return candidates[0][1]


def parse_heartbeat_sources():
    """Diagnostic: return list of (path, ts) for every heartbeat file parsed.

    Useful for `--check-only` and PROGRESS.md annotations — surfaces drift
    when one cron path goes stale while another is fresh. For multi-line
    files, shows the freshest valid timestamp found in the file.
    """
    sources = []
    for path in HEARTBEAT_FILES:
        if not path.exists():
            continue
        try:
            ts = _parse_iso(path.read_text())
        except Exception:
            ts = None
        sources.append({"path": str(path.relative_to(ROOT)), "ts": ts.isoformat() if ts else None})
    return sources


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
        print(f"Last work:    {last_work.isoformat()}  (freshest across heartbeat* files)")
    else:
        print(f"Last work:    NEVER (heartbeat missing)")
    print(f"Age:          {human_age(age)}")
    print(f"Now:          {datetime.now(timezone.utc).isoformat()}")
    # Surface per-file drift so PROGRESS.md annotations can spot the source.
    sources = parse_heartbeat_sources()
    if sources:
        print()
        print("Heartbeat sources:")
        for s in sources:
            mark = "✓" if s["ts"] else "✗"
            print(f"  {mark} {s['path']:<35} {s['ts'] or '(unparseable)'}")
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


def _selftest():
    """Lock in heartbeat-parsing semantics so future drift is caught.

    Run with: python3 scripts/thesis_watchdog.py --selftest
    """
    import tempfile

    # Case 1: simple ISO-8601 string.
    assert _parse_iso("2026-08-29T06:09:04Z") == datetime(2026, 8, 29, 6, 9, 4, tzinfo=timezone.utc)
    # Case 2: with explicit offset.
    assert _parse_iso("2026-08-29T06:09:04+00:00") == datetime(2026, 8, 29, 6, 9, 4, tzinfo=timezone.utc)
    # Case 3: empty.
    assert _parse_iso("") is None
    assert _parse_iso("   \n  \n") is None
    # Case 4: garbage.
    assert _parse_iso("not a timestamp") is None
    # Case 5: multi-line — freshest wins.
    text = "2026-08-29T02:18:06+00:00\n2026-08-29T04:09:57+00:00\n"
    parsed = _parse_iso(text)
    assert parsed == datetime(2026, 8, 29, 4, 9, 57, tzinfo=timezone.utc), parsed
    # Case 6: multi-line with garbage.
    text = "garbage\n2026-08-28T01:00:00Z\nmore garbage\n2026-08-29T01:00:00Z\n"
    parsed = _parse_iso(text)
    assert parsed == datetime(2026, 8, 29, 1, 0, 0, tzinfo=timezone.utc), parsed

    # Case 7: parse_heartbeat() picks freshest across multiple files.
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        # Override module-level paths for the test.
        global HEARTBEAT_FILES
        original = HEARTBEAT_FILES
        HEARTBEAT_FILES = [
            root / "hb1",
            root / "hb2",
            root / "hb3",
        ]
        try:
            (root / "hb1").write_text("2026-08-28T06:00:00Z")  # stale
            (root / "hb2").write_text("2026-08-29T03:00:00Z")  # fresh
            (root / "hb3").write_text("not a timestamp")        # unparseable
            freshest = parse_heartbeat()
            assert freshest == datetime(2026, 8, 29, 3, 0, 0, tzinfo=timezone.utc), freshest
            # Case 8: missing files don't crash.
            (root / "hb2").unlink()
            assert parse_heartbeat() == datetime(2026, 8, 28, 6, 0, 0, tzinfo=timezone.utc)
            (root / "hb1").unlink()
            assert parse_heartbeat() is None
        finally:
            HEARTBEAT_FILES = original

    print("✅ thesis_watchdog._selftest passed (8 cases).")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if _selftest() is None else 1)
    sys.exit(main())