#!/usr/bin/env python3
"""
git_commit.py — Atomic commit per tick for P1 GeoData v2.

Conventional commits format:
    <type>(<scope>): <subject>

    [optional body]

    [optional footer]

Types used:
- docs: documentation only changes
- feat: new feature (new script, new capability)
- fix: bug fix
- refactor: code change that neither fixes nor adds
- data: data download / annotation
- exp: experiment (training run, eval)
- test: add/fix tests
- chore: tooling, dependencies, config
- paper: paper sections
- thesis: thesis manuscript chapters

Scopes:
- queue: TASK_QUEUE.md
- progress: PROGRESS.md
- risk: RISK_REGISTER.md
- methodology, proposal, paper, etc.
- annotation, training, agent, web, api

Run:
    python3 scripts/git_commit.py --type feat --scope annotation --subject "Add SAM mask generator" --task T042
    python3 scripts/git_commit.py  # auto-detect from last tick in PROGRESS.md
"""
import argparse
re = __import__("re")
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def run(cmd, check=True, capture=True):
    """Run a git command in the project root."""
    r = subprocess.run(
        ["git", "-C", str(ROOT)] + cmd,
        capture_output=True if capture else None,
        text=True,
        timeout=60,
    )
    if check and r.returncode != 0:
        if capture:
            print(f"❌ git {' '.join(cmd)}: {r.stderr.strip()[:300]}")
        sys.exit(1)
    return r


def has_changes():
    """Check if there are staged or unstaged changes."""
    r = run(["status", "--porcelain"], check=False)
    return bool(r.stdout.strip())


def staged_files():
    """Return list of staged files."""
    r = run(["diff", "--cached", "--name-only"], check=False)
    return [f for f in r.stdout.strip().split("\n") if f]


def all_changed_files():
    """Return all changed files (staged + unstaged + untracked)."""
    r = run(["status", "--porcelain"], check=False)
    files = []
    for line in r.stdout.strip().split("\n"):
        if not line.strip():
            continue
        # Format: "XY filename" or "XY orig -> dest"
        parts = line[3:].strip().split(" -> ")
        files.append(parts[-1] if parts else line[3:])
    return files


def secret_leak_check(files):
    """Fail if any staged file looks like a secret."""
    bad_patterns = [
        re.compile(r"secrets/creds\.json$"),
        re.compile(r"\.env$"),
        re.compile(r"\.env\.local$"),
        re.compile(r"secrets/.*\.key$"),
        re.compile(r"secrets/.*\.pem$"),
        re.compile(r"secrets/.*\.age$"),
        re.compile(r"hf_[A-Za-z0-9_]{20,}"),  # HF tokens
        re.compile(r"ghp_[A-Za-z0-9_]{20,}"),  # GitHub PAT
        re.compile(r"AKIA[A-Z0-9]{16}"),  # AWS access key
        re.compile(r"sk-[A-Za-z0-9]{20,}"),  # OpenAI / Anthropic
    ]
    leaked = []
    for f in files:
        # Skip example/template files (they intentionally contain fake tokens)
        if any(s in f for s in (".example", "EXAMPLE", "template", "TEMPLATE",
                                  "creds.schema.json", "PROGRESS.md", "README")):
            continue
        p = ROOT / f
        if not p.exists() or p.is_dir():
            continue
        try:
            content = p.read_text(errors="replace")
        except Exception:
            continue
        for pat in bad_patterns:
            if pat.search(content) or pat.search(f):
                leaked.append((f, str(pat.pattern)))
    return leaked


def stage_all():
    """Stage all changes (excluding secrets via .gitignore)."""
    run(["add", "-A"])


def unstage_if_too_big(files, max_size_mb=10):
    """Unstage any file larger than max_size_mb (should be in .gitignore anyway)."""
    big = []
    for f in files:
        p = ROOT / f
        if not p.exists():
            continue
        if p.stat().st_size > max_size_mb * 1024 * 1024:
            run(["reset", "HEAD", "--", f], check=False)
            big.append(f)
    return big


def detect_type_from_files(files):
    """Auto-detect commit type from changed files."""
    if any("scripts/" in f for f in files):
        return "feat"
    if any(".md" in f for f in files):
        return "docs"
    if any("data/" in f for f in files):
        return "data"
    if any("test" in f.lower() for f in files):
        return "test"
    if any("requirements" in f or "Makefile" in f for f in files):
        return "chore"
    return "chore"


def detect_scope_from_files(files):
    """Auto-detect scope from changed files."""
    scopes = {
        "queue": "TASK_QUEUE.md",
        "progress": "PROGRESS.md",
        "risk": "RISK_REGISTER.md",
        "data": "DATA_MANIFEST.md",
        "proposal": "FORMAL_PROPOSAL.md",
        "methodology": "METHODOLOGY.md",
        "paper": "PAPER_OUTLINE.md",
        "benchmark": "BENCHMARK_QUESTIONS.md",
        "defense": "DEFENSE_PLAN.md",
        "autonomy": "AUTONOMY.md",
        "ethics": "ETHICS_WAIVER_MEMO.md",
        "makefile": "Makefile",
        "docker": "docker-compose.yml",
        "annotation": "auto_annotate.py",
        "training": "train.py",
        "agent": "agent_",
        "web": "web/",
        "api": "backend/",
        "sanity": "sanity_check.py",
        "tick": "autonomous_tick.py",
        "weekly": "weekly_review.py",
        "creds": "creds",
        "install": "install.sh",
    }
    for scope, pattern in scopes.items():
        if any(pattern in f for f in files):
            return scope
    return "misc"


def make_commit_message(args, files):
    """Build conventional commit message."""
    type_ = args.type or detect_type_from_files(files)
    scope = args.scope or detect_scope_from_files(files)
    subject = args.subject or f"Update {len(files)} file(s)"

    header = f"{type_}({scope}): {subject}"
    if len(header) > 72:
        header = header[:69] + "..."

    body_parts = []
    if args.body:
        body_parts.append(args.body)

    if files and not args.body:
        body_parts.append("Changed files:")
        for f in files[:20]:
            body_parts.append(f"  - {f}")
        if len(files) > 20:
            body_parts.append(f"  ... and {len(files) - 20} more")

    if args.task:
        body_parts.append(f"Task: {args.task}")

    if args.closes:
        body_parts.append(f"Closes: {args.closes}")

    if args.co_author:
        body_parts.append("")
        body_parts.append(f"Co-authored-by: {args.co_author}")

    body = "\n\n".join(body_parts)
    msg = header + ("\n\n" + body if body else "")

    return msg, type_, scope


def commit(msg):
    """Create the commit."""
    r = run(["commit", "-m", msg], check=False)
    if r.returncode == 0:
        return True, r.stdout
    return False, r.stderr


def get_last_commit():
    r = run(["log", "-1", "--pretty=%h %s"], check=False)
    return r.stdout.strip() if r.returncode == 0 else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--type", help="Commit type (feat/fix/docs/data/exp/test/chore/paper/thesis)")
    ap.add_argument("--scope", help="Commit scope")
    ap.add_argument("--subject", help="Short subject line")
    ap.add_argument("--body", help="Longer description")
    ap.add_argument("--task", help="Task ID (e.g. T042)")
    ap.add_argument("--closes", help="Issue/PR this closes")
    ap.add_argument("--co-author", help="Co-author 'Name <email>'")
    ap.add_argument("--dry-run", action="store_true", help="Show what would be committed")
    ap.add_argument("--no-stage", action="store_true", help="Don't auto-stage; commit already-staged files")
    ap.add_argument("--amend", action="store_true", help="Amend the previous commit")
    args = ap.parse_args()

    print(f"📝 git_commit.py — atomic commit for P1 GeoData v2\n")

    # Detect changes
    if not has_changes() and not args.amend:
        print("✅ No changes to commit.")
        return 0

    # Stage everything (unless --no-stage)
    if not args.no_stage:
        stage_all()

    files = staged_files()
    if not files and not args.amend:
        print("❌ Nothing staged after git add -A.")
        return 1

    # Secret leak check
    leaks = secret_leak_check(files)
    if leaks:
        print("❌ SECRET LEAK DETECTED. Refusing to commit.")
        for f, pat in leaks:
            print(f"   {f}  matches  {pat}")
        print("\nUnstage these files and check .gitignore:")
        for f, _ in leaks:
            run(["reset", "HEAD", "--", f], check=False)
        return 2

    # Unstage oversized files
    big = unstage_if_too_big(files, max_size_mb=10)
    if big:
        print(f"⚠️  Unstaged {len(big)} file(s) > 10 MB:")
        for f in big:
            print(f"   - {f}")

    files = staged_files()

    # Build commit message
    msg, type_, scope = make_commit_message(args, files)

    if args.dry_run:
        print("🔍 DRY-RUN — would commit:\n")
        print("─" * 70)
        print(msg)
        print("─" * 70)
        print(f"\nFiles ({len(files)}):")
        for f in files[:10]:
            print(f"  {f}")
        if len(files) > 10:
            print(f"  ... +{len(files) - 10} more")
        return 0

    # Commit
    print(f"📝 {type_}({scope}): {args.subject or 'Update'}")
    ok, out = commit(msg)
    if not ok:
        print(f"❌ Commit failed: {out}")
        return 1

    # Show result
    last = get_last_commit()
    print(f"\n✅ Committed: {last}")
    print(f"\nNext: 'make git-sync' (Ivan-only) to push to GitHub.")
    return 0


if __name__ == "__main__":
    sys.exit(main())