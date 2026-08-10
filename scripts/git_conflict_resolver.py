#!/usr/bin/env python3
"""
git_conflict_resolver.py — Handle merge conflicts intelligently.

Common conflict scenarios in this project:
1. PROGRESS.md — both sides appended entries; resolve by concatenating
2. TASK_QUEUE.md — both sides marked tasks done; resolve by union
3. RISK_REGISTER.md — both sides added risks; resolve by union
4. Code files (scripts/*.py) — manual resolution required
5. Docs (.md) — heuristic: prefer larger file

Strategy:
- Detect conflict type by file extension + content pattern
- Auto-resolve safe cases
- Flag manual cases for Ivan
- Apply resolution
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def run(cmd, cwd=None):
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=60,
                       cwd=cwd or str(ROOT))
    return r.returncode, r.stdout, r.stderr


def conflicted_files():
    """Return list of files with merge conflicts."""
    code, out, err = run(["git", "diff", "--name-only", "--diff-filter=U"])
    if code != 0:
        return []
    return [f for f in out.strip().split("\n") if f]


def detect_type(path):
    """Return one of: queue, progress, risk, code, doc, other."""
    name = Path(path).name
    if name == "TASK_QUEUE.md":
        return "queue"
    if name == "PROGRESS.md":
        return "progress"
    if name == "RISK_REGISTER.md":
        return "risk"
    if name.endswith(".py"):
        return "code"
    if name.endswith(".md"):
        return "doc"
    if name.endswith(".json") or name.endswith(".yml") or name.endswith(".yaml"):
        return "config"
    return "other"


def split_conflict_blocks(content):
    """Split file content into conflict segments + clean segments.

    Returns list of (kind, text) tuples where kind is 'clean', 'ours', 'theirs', 'base'.
    """
    segments = []
    pattern = re.compile(
        r"^<<<<<<< .*?\n(.*?)^=======\n(.*?)^>>>>>>> .*?\n",
        re.DOTALL | re.MULTILINE,
    )
    pos = 0
    for m in pattern.finditer(content):
        # Clean text before
        if m.start() > pos:
            segments.append(("clean", content[pos:m.start()]))
        # The conflict
        ours = m.group(1)
        theirs = m.group(2)
        # Check for base marker
        if "|||||||" in ours or "|||||||" in theirs:
            # Diff3-style; we keep ours/theirs and ignore base
            segments.append(("conflict", (ours, theirs)))
        else:
            segments.append(("conflict", (ours, theirs)))
        pos = m.end()
    # Trailing clean text
    if pos < len(content):
        segments.append(("clean", content[pos:]))
    return segments


def resolve_progress(ours, theirs):
    """Resolve PROGRESS.md conflict by concatenating entries.

    Each entry starts with '## YYYY-MM-DD'. We dedupe by exact-match.
    """
    # Find the latest common entry header
    ours_entries = re.split(r"(?=^## \d{4}-\d{2}-\d{2})", ours, flags=re.MULTILINE)
    theirs_entries = re.split(r"(?=^## \d{4}-\d{2}-\d{2})", theirs, flags=re.MULTILINE)

    # First entries might be preamble (before any '## ')
    ours_preamble = ours_entries[0] if not ours_entries[0].startswith("## ") else ""
    theirs_preamble = theirs_entries[0] if not theirs_entries[0].startswith("## ") else ""

    # Collect all date entries, dedupe by header line
    seen = set()
    merged = []
    for entry in ours_entries + theirs_entries:
        if not entry.strip():
            continue
        first_line = entry.split("\n")[0]
        if first_line in seen:
            continue
        seen.add(first_line)
        merged.append(entry)

    preamble = ours_preamble or theirs_preamble
    return preamble + "".join(merged)


def resolve_queue(ours, theirs):
    """Resolve TASK_QUEUE.md by taking union of checkboxes."""
    # Split into lines, dedupe identical lines
    seen = set()
    merged = []
    for line in (ours + theirs).split("\n"):
        # Preserve order from ours first, then theirs
        if line in seen:
            continue
        seen.add(line)
        merged.append(line)
    return "\n".join(merged)


def resolve_doc(ours, theirs):
    """Resolve doc conflicts: prefer longer version (usually has more content)."""
    if len(theirs) > len(ours) * 1.1:
        return theirs
    return ours


def resolve_code(ours, theirs):
    """Code conflicts: refuse auto-resolution, mark for manual."""
    return None


def resolve_file(path):
    """Resolve a single conflicted file."""
    p = ROOT / path
    if not p.exists():
        return "missing", "file not found"

    content = p.read_text()
    type_ = detect_type(path)

    if type_ == "code":
        return "manual", "Python file requires manual resolution"

    if type_ == "config":
        return "manual", f"{type_} requires manual resolution"

    if type_ not in ("queue", "progress", "risk", "doc"):
        return "manual", f"unknown type {type_}"

    # Find conflict blocks and resolve each
    segments = split_conflict_blocks(content)
    if not any(k == "conflict" for k, _ in segments):
        return "no-conflict", "already resolved"

    resolver = {
        "queue": resolve_queue,
        "progress": resolve_progress,
        "risk": resolve_queue,  # same as queue: union of lines
        "doc": resolve_doc,
    }.get(type_)

    if not resolver:
        return "manual", "no resolver"

    # Resolve each conflict block
    new_segments = []
    for kind, text in segments:
        if kind == "clean":
            new_segments.append(text)
        elif kind == "conflict":
            ours, theirs = text
            resolved = resolver(ours, theirs)
            if resolved is None:
                return "manual", "resolver returned None"
            new_segments.append(resolved)

    new_content = "".join(new_segments)
    p.write_text(new_content)
    return "resolved", f"applied {type_} resolver"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--auto", action="store_true",
                    help="Auto-resolve what can be resolved, leave others for manual")
    ap.add_argument("--dry-run", action="store_true",
                    help="Show what would be done without applying")
    args = ap.parse_args()

    files = conflicted_files()
    if not files:
        print("✅ No conflicts.")
        return 0

    print(f"🔀 {len(files)} conflicted file(s):")
    for f in files:
        type_ = detect_type(f)
        print(f"  • {f}  (type: {type_})")
    print()

    resolved = 0
    manual = []

    for f in files:
        if args.dry_run:
            type_ = detect_type(f)
            print(f"  [DRY-RUN] {f}: type={type_}, would attempt auto-resolve")
            continue

        status, msg = resolve_file(f)
        if status == "resolved":
            # Stage the resolved file
            run(["git", "add", f])
            print(f"  ✅ {f}: {msg}")
            resolved += 1
        elif status == "no-conflict":
            print(f"  ⏭️  {f}: {msg}")
        else:
            print(f"  ⚠️  {f}: {msg}")
            manual.append(f)

    print()
    print(f"📊 Resolved: {resolved}")
    print(f"   Manual:   {len(manual)}")
    if manual:
        print(f"\n🚧 Manual resolution needed:")
        for f in manual:
            print(f"   - {f}")
        print(f"\nResolve with: nano {manual[0]}")
        print(f"Then: git add {manual[0]}")
        print(f"Finally: git rebase --continue  (or git commit to finish merge)")

    return 0 if not manual else 4


if __name__ == "__main__":
    sys.exit(main())