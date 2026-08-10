# 🔧 GIT WORKFLOW — P1 GeoData v2

**This is how Erebus commits work and how Iván syncs with GitHub.**

**GitHub repo:** https://github.com/IvanWeissVanDerPol/paraguay-geodata-vlm (created 2026-08-10, public)

---

## TL;DR

- **Erebus auto-commits** every tick (atomic commits, conventional format)
- **Erebus never pushes** to remote — only Iván triggers push
- **Sync when you want** with `make git-sync` (safe) or `make git-push` (when ready)

---

## Repo on GitHub

**URL:** https://github.com/IvanWeissVanDerPol/paraguay-geodata-vlm
**Created:** 2026-08-10 (initial state: empty)
**Visibility:** public

The first push seeds the repo with all local commits (4 atomic conventional commits ready to go). After that, the workflow is:
- Erebus auto-commits locally (never pushes)
- Ivan triggers sync with `make git-sync` (fetch + rebase + status)
- Ivan pushes with `make git-push` when ready

## Architecture

```
Erebus tick (06:00 UTC daily)
   ↓
Work happens (writes code/docs)
   ↓
scripts/autonomous_tick.py invokes scripts/git_commit.py
   ↓
git add -A (excluding secrets via .gitignore)
   ↓
Secret leak check (refuses if tokens found)
   ↓
Pre-commit hook runs (syntax, JSON validity, size check)
   ↓
git commit -m "<conventional-commit-message>"
   ↓
Commit landed locally. Push is YOUR call.
```

---

## Conventional commit format

```
<type>(<scope>): <subject>

[optional body]

[optional footer]
```

**Types:**
- `feat` — new feature (new script, new capability)
- `fix` — bug fix
- `docs` — documentation only
- `data` — data download / annotation
- `exp` — experiment (training run, eval)
- `test` — add/fix tests
- `chore` — tooling, deps, config
- `paper` — paper sections
- `thesis` — thesis manuscript chapters

**Scopes:**
- `queue` — TASK_QUEUE.md
- `progress` — PROGRESS.md
- `risk` — RISK_REGISTER.md
- `methodology`, `proposal`, `paper`, `benchmark`, `defense`, `autonomy`, `ethics`
- `annotation`, `training`, `agent`, `web`, `api`
- `tick`, `weekly`, `sanity`, `creds`, `install`
- `init` — initial commit

**Examples seen so far:**

```
feat(init): Initial thesis scaffold: 87 tasks, autonomy, git workflow
chore(queue): T029 — Document the autonomous system in AUTONOMY.md
```

---

## Daily commands (Erebus runs these automatically)

```bash
# After tick work:
make commit                # or git_commit.py directly (auto-detect type/scope)
make commit-dry            # show what would be committed
```

---

## Iván's commands (manual)

```bash
# First-time setup (one-time)
make git-first-push           # push the local repo to the empty GitHub repo

# Status check (run anytime)
make git-status            # working tree state + branch info
make git-log               # last 20 commits
make git-branches          # all branches

# Sync with remote
make git-sync              # fetch + rebase + status (safe, no push)
make git-fetch             # only fetch, no rebase
make git-push              # push local commits to remote

# Conflict resolution
make git-resolve           # auto-resolve conflicts (PROGRESS/TASK_QUEUE/RISK)
make git-resolve-dry       # show what would be resolved

# Branch management
make git-branch-feat NAME=annotation-pipeline
# creates: feat/annotation-pipeline
git checkout main
git merge feat/annotation-pipeline

# Hooks
make git-install-hooks     # install pre-commit hook
```

---

## Branch strategy

```
main                    ← always stable, Iván pushes here
├── feat/annotation     ← experimental branches
├── feat/training
├── feat/web-app
├── docs/cap-2
└── fix/conflict-x
```

**Default workflow:**
1. Erebus commits directly to main (small atomic commits)
2. If something risky needs testing, Iván creates a branch: `make git-branch-feat NAME=my-feature`
3. Iván merges back to main when ready

**Why no PRs?** Solo project. The pre-commit hook + secret leak check provides the safety net that PR reviews would normally give.

---

## Conflict resolution

Conflicts only happen if:
- Iván committed something AND pushed it
- Erebus committed something in parallel
- Both touched the same file

**Likely conflict files:**
- `PROGRESS.md` — both added entries
- `TASK_QUEUE.md` — both marked tasks done
- `RISK_REGISTER.md` — both added risks

**Auto-resolver handles these:**

```bash
make git-resolve
```

It will:
1. ✅ Auto-resolve `PROGRESS.md` (concatenate entries, dedupe by date)
2. ✅ Auto-resolve `TASK_QUEUE.md` (union of checkboxes)
3. ✅ Auto-resolve `RISK_REGISTER.md` (union of risks)
4. ✅ Auto-resolve `.md` docs (prefer longer version)
5. ⚠️  Mark Python code for manual resolution
6. ⚠️  Mark JSON/YAML for manual resolution

**Manual resolution:**
```bash
nano <conflicted-file>     # edit
git add <conflicted-file>
git rebase --continue      # or git commit to finish merge
```

---

## Secret safety

The system refuses to commit:

| File pattern | Action |
|---|---|
| `secrets/creds.json` | Refused (matches `secrets/creds\.json$`) |
| `.env` | Refused (matches `\.env$`) |
| `.env.local` | Refused (matches `\.env\.local$`) |
| `secrets/*.key` / `*.pem` / `*.age` | Refused |
| `secrets/credentials.*` | Refused |

The system ALSO scans content for known token patterns:
- `hf_[A-Za-z0-9_]{20,}` — HuggingFace
- `ghp_[A-Za-z0-9_]{20,}` — GitHub PAT
- `AKIA[A-Z0-9]{16}` — AWS access key
- `sk-[A-Za-z0-9]{20,}` — OpenAI / Anthropic

Example files (`.env.example`, `creds.schema.json`, `PROGRESS.md`, `README.md`) are exempted since they intentionally contain placeholder tokens.

**Bypass (only if you know what you're doing):**
```bash
git commit --no-verify
```

---

## Pre-commit hook checks

Every commit runs:

1. **Secret leak check** (see above)
2. **Python syntax** — `ast.parse()` on staged .py files
3. **JSON validity** — `json.load()` on staged .json files
4. **Markdown size** — warn if > 200 KB

If any check fails, the commit is aborted. To skip:
```bash
git commit --no-verify
```

---

## Cron schedule

| Job | When | What |
|---|---|---|
| `thesis-daily-tick` | 06:00 UTC daily | Auto-commits each tick's work |
| `thesis-weekly-review` | Sun 18:00 UTC | Reviews progress (no commit) |
| `thesis-git-maintenance` | Sun 23:00 UTC | gc + prune + reflog + fsck |

---

## Disaster recovery

### "I lost work"

Check reflog:
```bash
git reflog
# find the commit hash, then:
git checkout <hash>
git checkout -b recovery/$(date +%s)
```

### "I committed a secret"

```bash
# Remove from latest commit (rewrites history; only safe if not pushed)
git rm --cached secrets/creds.json
git commit --amend --no-edit

# Rotate the credential at the source (HuggingFace, GitHub, etc.)
# Update secrets/creds.json with new value
```

### "Commits diverge from remote"

```bash
make git-resolve          # auto-resolve safe files
git rebase origin/main    # replay local commits on top
# fix any remaining conflicts
git rebase --continue
make git-push             # push
```

### "Repo is corrupted"

```bash
git fsck --no-progress
# if errors, restore from:
# - remote (make git-fetch + git reset --hard origin/main)
# - backup (you have one, right?)
# - the original commits (git reflog)
```

---

## File-level .gitignore rules

| Path | Rule |
|---|---|
| `.venv/` | ignored |
| `data/processed/*` | ignored (regenerated) |
| `data/raw/*/osm/extracted/` | ignored (1.2 GB, regenerated from zip) |
| `data/raw/*/{ign,sentinel2,worldpop,openbuildings,indi,mopc,chirps}/*` | ignored (regenerated) |
| `data/raw/*/SHA256SUMS` | ignored (regenerated) |
| `secrets/creds.json` | **NEVER committed** |
| `secrets/*.key`, `*.pem`, `*.age` | **NEVER committed** |
| `logs/*` | ignored |
| `checkpoints/`, `*.safetensors`, `*.bin`, `*.pt`, `*.pth` | ignored (large) |
| `__pycache__/`, `*.pyc` | ignored |

---

## Stats

```
✅ Initial commit: 47e8bb8
✅ Auto-commit 1: ef8e667
✅ Repo size: 612 KB (excluding .git/)
✅ Working tree: clean
✅ Pre-commit hook: installed + tested
✅ Cron: thesis-git-maintenance scheduled
```

---

**Last updated:** 2026-08-10
**Maintained by:** Erebus (autonomously) + Iván (manual sync)