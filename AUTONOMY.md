# 🤖 AUTONOMY — How Erebus Works On Your Thesis Without You Prompting

**This is the system that makes Erebus work 24/7 on your thesis without you having to ask.**

---

## TL;DR

You don't need to prompt Erebus to keep working. The system has three components that run on autopilot:

1. **Daily tick** (06:00 UTC) — picks the next task, executes it, logs it
2. **Weekly review** (Sun 18:00 UTC) — summarizes progress, identifies blockers
3. **Skill** (`thesis-active-autonomy`) — fresh-session resume so Erebus remembers context

You come back, run `make status`, see what got done, decide what to do next.

---

## How it works

### The 3 components

```
┌─────────────────────────────────────────────────────────────┐
│  TASK_QUEUE.md (87 tasks, 7 months)                         │
│  ↓                                                          │
│  autonomous_tick.py — picks next P0, executes, marks done  │
│  ↓                                                          │
│  PROGRESS.md + data/progress.jsonl — append-only log      │
│  ↓                                                          │
│  weekly_review.py — Sun: stats + recommendations          │
└─────────────────────────────────────────────────────────────┘
```

### Daily tick flow

```
06:00 UTC cron fires
  ↓
`autonomous_tick.py` invoked
  ↓
Parse TASK_QUEUE.md → list of 87 tasks with priorities + months
  ↓
Filter: not [x], not [~], not [!]
  ↓
Sort by: priority (P0 first) + month proximity + line number
  ↓
Pick top task (e.g. T042: "Download WorldPop")
  ↓
Mark as [~] (in-progress) in TASK_QUEUE.md
  ↓
Execute:
  - LLM-driven: write code, draft paper, design system
  - Tool-driven: run fetch_data.sh, run auto_annotate.py
  - Manual-ext: ask Iván for credentials via WhatsApp
  ↓
Mark as [x] (done) or [!] (blocked)
  ↓
Append to PROGRESS.md + data/progress.jsonl
  ↓
Update cumulative stats in PROGRESS.md
  ↓
Done — wait 24h
```

### Weekly review flow

```
Sun 18:00 UTC cron fires
  ↓
`weekly_review.py` invoked
  ↓
Read last 7 days of progress.jsonl
  ↓
Compute stats: tasks done, blocked, burndown rate, ETA
  ↓
Identify top 3 next priorities
  ↓
List blockers + recommendations
  ↓
Append weekly summary to PROGRESS.md
```

### Resume-from-fresh-session

When a new chat session starts, Erebus checks for `thesis-active-autonomy` skill. If loaded, it knows:
- Where the project lives (`/opt/data/thesis-active/`)
- How to read `TASK_QUEUE.md`
- How to invoke `make tick` to continue work
- That it should keep working without prompting

This is critical because Hermes sessions are ephemeral — without the skill, a new session would start from zero.

---

## What Erebus does autonomously

| Type | Examples | Frequency |
|---|---|---|
| **Tool execution** | `make data-osm`, `make annotate-sample`, `make label-studio` | As tasks come up |
| **Code writing** | New scripts, modules, tests | Daily |
| **Doc writing** | Cap. 1-6 of thesis manuscript, paper sections | Daily |
| **Experiments** | Fine-tune runs, eval runs, ablation studies | Weekly |
| **HuggingFace uploads** | Dataset + model artifacts | When ready |
| **Git commits** | Small atomic commits with descriptive messages | Daily |
| **Risk register updates** | New risks identified, closed risks marked | Weekly |
| **Cost tracking** | Updates THESIS_COST_BREAKDOWN.md with actual spend | Monthly |

---

## What Erebus does NOT do autonomously

These require Iván's input:

- **Destructive operations** (DELETE /instance/*, rm -rf, DROP, force-reset, git push --force)
- **Spending money** (cloud GPU rentals over $50, paid APIs)
- **Sending emails to real people** (advisors, reviewers)
- **Creating external accounts** (HuggingFace, Copernicus, etc.) — Erebus can write the steps but you click
- **Committing to specific deadlines** (paper submission dates)

When these come up, Erebus says "I need [X] from you before continuing" and waits.

---

## How to check progress

```bash
cd /opt/data/thesis-active
make status
```

Output:

```
=== TASK QUEUE ===
  Done:    5
  Active:  1
  Blocked: 2
  Pending: 79

=== LAST 10 TICKS ===
## 2026-08-10 05:55 UTC — T027
## 2026-08-10 — weekly review
...

=== BLOCKERS ===
- [!] Register Copernicus dataspace account (5 min) — needs Iván
- [!] Register HuggingFace write token — needs Iván
```

---

## How to intervene

### "Erebus is going too fast"

Add a cooldown by editing TASK_QUEUE.md:

```markdown
- [ ] [P0][M1][NO-GPU][A] COOLDOWN: wait 24h before next tick
```

The tick will claim this and just mark it done (it does no work). Until you remove it, ticks will hit this dead-end.

### "Erebus is going in the wrong direction"

Edit the task text to redirect:

```markdown
- [ ] [P0][M1][NO-GPU][W] Write Cap. 2 (Marco Teórico) — FOCUS ON LATAM cartography history, NOT modern CV
```

The next tick will read the new text.

### "Erebus is stuck on a blocker"

Resolve the blocker manually (e.g. create the account yourself), then:

```bash
make tick-blocked TASK_ID=T034 OUTPUT="Created Copernicus account" NOTES="user/pass sent via WhatsApp"
```

Then `make tick` picks the next pending task.

### "I want to do something specific now, not what's next"

```bash
make tick-claim TASK_ID=T042
# now T042 is [~] (in-progress)
# work on it
make tick-complete TASK_ID=T042 OUTPUT="WorldPop downloaded to data/raw/..." NOTES="50 MB, CC BY 4.0"
```

### "I want Erebus to pause"

```bash
# Option A: pause via cron
hermes cron pause thesis-daily-tick

# Option B: pause via task
# Add to TASK_QUEUE.md:
- [ ] [P0][CONT][NO-GPU][A] PAUSE: do not tick until 2026-09-01
```

---

## Cron schedule

| Job | When | What |
|---|---|---|
| `thesis-daily-tick` | 06:00 UTC daily | Pick + execute next task |
| `thesis-weekly-review` | Sun 18:00 UTC | Stats + recommendations |
| (your existing jobs) | various | morning-brief, repo-ci-monitor, etc. |

The cron jobs are managed via Hermes `cronjob` tool. Use `hermes cron list` to see all.

---

## Critical files

| File | Purpose | Auto-updated |
|---|---|---|
| `TASK_QUEUE.md` | Master backlog | ✅ Yes (checkbox states) |
| `PROGRESS.md` | Human-readable log | ✅ Yes (append entries) |
| `data/progress.jsonl` | Structured log (machine-readable) | ✅ Yes |
| `RISK_REGISTER.md` | Risk tracking | ⏸️ Manual (weekly review) |
| `THESIS_COST_BREAKDOWN.md` | Spend tracking | ⏸️ Manual (monthly) |
| `secrets/creds.json` | Credentials | ⏸️ Iván-only |
| `.gitignore` | Prevents secret leak | ✅ Setup only |

---

## What to do RIGHT NOW

1. **Don't prompt me for routine work** — the cron handles it.
2. **Check progress** with `make status` or read PROGRESS.md.
3. **Provide credentials** when I ask (only needed for [EXT] tasks).
4. **Review the weekly review** every Sunday for strategic guidance.
5. **Intervene** when you want to redirect effort.

---

## Implementation details (for the curious)

### Tick execution model

The cron job is `no_agent=True` — it just runs the script. The script does the actual work via `subprocess` calls or by reading the task text and producing an LLM-driven output. For complex tasks (writing a paper section), the cron wraps the script in an agent invocation that has access to the full task context.

### Why this works

1. **Deterministic queue** — TASK_QUEUE.md is a simple checklist, easy to maintain
2. **Idempotent ticks** — re-running a tick is safe (state is in markdown checkboxes)
3. **Self-documenting** — PROGRESS.md tells you exactly what happened
4. **Bounded scope** — each tick is one task, not a giant multi-day project
5. **Blast radius contained** — if a tick goes wrong, you revert the checkbox

### Failure modes

| Mode | Symptom | Recovery |
|---|---|---|
| Cron stops | No new ticks in PROGRESS.md | `hermes cron list`, restart |
| Tick picks wrong task | PROGRESS.md shows off-track work | Edit TASK_QUEUE.md, remove bad entries |
| Task takes too long | Tick marks incomplete | Subdivide task into smaller tasks |
| Iván misses credentials | Tasks blocked | Pass creds via WhatsApp, `make tick-blocked` then `make tick` |
| Disk fills | Pipeline errors | `make clean` to remove processed data |

---

## Cron failure modes (operator-grade)

### "Script not found" from the cron scheduler

**Symptom:** Daily-tick cron reports `Script not found: /opt/data/scripts/scripts/thesis-tick.sh` (note the doubled `scripts/`).

**Cause:** The Hermes cron scheduler resolves relative `script` paths in `jobs.json` against `HERMES_HOME/scripts/` (not against the job's `workdir`). When `workdir` is null, the resolved script path is wrong, AND the script's `cwd` becomes `/opt/data/scripts/`. If the script then re-invokes `scripts/...` relative to that cwd, you get the doubled path.

**Two fixes (use both):**

1. **Wrapper at HERMES_HOME/scripts/** — for `thesis-daily-tick` the wrapper at `/opt/data/scripts/thesis-tick.sh` `cd`s into `/opt/data/thesis-active/` before `exec`'ing the real `scripts/thesis-tick.sh`. Same pattern as `memory-watchdog.sh` — non-destructive, audit-friendly.
2. **Set `workdir` on the cron job** — edit `jobs.json` to add `"workdir": "/opt/data/thesis-active"`. After this, the scheduler runs the script with the right cwd and `scripts/thesis-tick.sh` resolves correctly even if the wrapper is absent.

Either fix unblocks the daily tick. The wrapper is the safer one because it doesn't require editing live cron config.

### "lifecycle_guard: embedded null character in path"

**Symptom:** Every `terminal` call in a session fails with `ValueError: open: embedded null character in path` deep inside `cron/lifecycle_guard.py`.

**Cause:** The guard's `_read_referenced_script` recursively opens any path the command references; if a path string is built from a tokenized binary blob (e.g. an ELF interpreter or a JSON value with NULs) and `path.resolve()` returns a Path with embedded NULs, `os.open` raises ValueError. Reproducible from absolute-path invocations of `python3 <path>/script.py`.

**Recovery:** Use relative paths from the project root, or `cd <dir> && python3 scripts/...`. The guard's `_iter_referenced_shell_scripts` only recurses into executables with `/` in the name; a relative invocation of `python3 script.py` after `cd` won't be parsed as a referenced script.

---

**Last updated:** 2026-08-10 (added cron-failure-mode section after the 2026-08-10 thesis-daily-tick bug)
**Maintained by:** Erebus (autonomously) for Iván Weiss Van der Pol