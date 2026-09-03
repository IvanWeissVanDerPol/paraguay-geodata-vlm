# THESIS STATE — Research-Tracker Weekly Snapshot

> **Audience:** Iván + the autonomous agent (Erebus). This file is the **single
> canonical weekly snapshot** of the thesis project. It supersedes scattering
> the same numbers across `PROGRESS.md`, `TASK_QUEUE.md`, and `RISK_REGISTER.md`.
>
> **Cadence:** regenerated at every Sunday 18:00 UTC weekly review tick
> (`make weekly` → `scripts/weekly_review.py → thesis-weekly.sh`). A fresh
> snapshot overwrites the previous one — history lives in git, not in this file.
>
> **Scope:** This is the **substrate** repo (`paraguay-geodata-vlm` =
> `/opt/data/thesis-active`). The actual thesis (`satellite-paraguay` =
> `/opt/data/work/satellite-paraguay`) is tracked separately; see
> `THESIS_ARCHITECTURE.md` for the cross-repo map.

---

## 0. Identity

| Field | Value |
|---|---|
| Path (official) | *Multi-Temporal Satellite Computer Vision for Paraguay: A Foundation-Model Approach to Land-Use, Climate, and Environmental Justice* |
| Substrate codename | **P1 GeoData v2** (this repo's working name; data + infra only) |
| Author | Iván Weiss Van Der Pol |
| Institution | Universidad Nacional de Asunción — FADA |
| Adviser (target) | Prof. Dr. Juan Carlos Cristaldo (pending co-sign) |
| Strategy | Paper-first, solo, no advisor gate, no bureaucracy |
| Target venues | ICA 2027, ACM SIGSPATIAL 2027, Remote Sensing of Environment |
| Submission mode | arxiv preprint → workshop paper → Q1 journal |

---

## 1. Headline numbers (this week)

| Metric | Value | Source |
|---|---|---|
| Tasks completed (TASK_QUEUE.md) | **44 / 87** (`[x]`) | `TASK_QUEUE.md` |
| Tasks pending | **43** (`[ ]`) | `TASK_QUEUE.md` |
| Tasks blocked | **0** (`[!]`) | `TASK_QUEUE.md` |
| Total ticks executed (all-time) | **44** | `data/progress.jsonl` |
| Ticks in last 7 days | **0** (system stalled since 2026-08-14) | `data/progress.jsonl` |
| Days since last tick | **20** (as of 2026-09-03) | `data/heartbeat` |
| Real work vs auto-stub ticks | **2 real / 42 stub** | `data/progress.jsonl` |
| Real deliverables in repo | scripts/, DATA_MANIFEST.md, PROGRESS.md, RISK_REGISTER.md, METHODOLOGY.md, FORMAL_PROPOSAL.md, ETHICS_WAIVER_MEMO.md, DEFENSE_PLAN.md, PAPER_OUTLINE.md, TASK_QUEUE.md, AUTONOMY.md, INDEX.md, THESIS_PICK.md, THESIS_ARCHITECTURE.md, THESIS_COST_BREAKDOWN.md | this repo |

---

## 2. Task queue — phase status

| Phase | Scope | Done | Pending | % |
|---|---|---|---|---|
| Phase 0 | Setup & foundations [M1] | 6 | 0 | 100% |
| Phase 1 | Data pipeline [M1-M2] | 11 | 5 | 69% |
| Phase 2 | Annotation pipeline [M2-M3] | 12 | 0 | 100% |
| Phase 3 | Fine-tuning [M4-M5] | 9 | 0 | 100% |
| Phase 4 | Conversational agent [M5-M6] | 6 | 0 | 100% |
| Phase 5 | Paper writing [M6-M7] | 2 | 10 | 17% |
| Phase 6 | Thesis manuscript [M7] | 0 | 9 | 0% |
| Phase 7 | Advisor outreach + defense [M8-M12] | 0 | 10 | 0% |
| Maintenance | Continuous | 0 | 5 | 0% |
| **Total** | | **44** | **39** | **53%** |

---

## 3. Completed (with real output, not stubs)

> Only the 2 ticks that wrote actual content — the other 42 marked themselves
> `done` via the auto-stub path without producing artifacts. **Treat the queue
> completion percentage as inflated until verified.**

| Task | Real output | Verified |
|---|---|---|
| T025 | `TASK_QUEUE.md`, `PROGRESS.md`, `scripts/autonomous_tick.py`, `scripts/weekly_review.py` written | ✅ (this repo) |
| T039 | `scripts/fetch_ign_wms.py` (9.5KB, 18 deptos, WMS probing, manifest output) | ⚠️ not run (sandbox DNS) |
| T047 | `scripts/data_inventory.py` ran → INVENTORY.json + INVENTORY.md (8 datasets / 102 files / 1.19 GB) | ✅ |

Everything else in `TASK_QUEUE.md` marked `[x]` was an **auto-stub tick** — the
script claimed the task without producing the file. Re-execution is required for
every "done" item not on the table above.

---

## 4. Blockers

**None currently flagged.** But three latent blockers identified:

1. **Auto-tick dishonesty.** 42 / 44 "done" ticks wrote `[auto-stub] Task
   picked; awaiting real execution in next tick.` and marked `[x]`. The
   autonomous system has been silently inflating completion. Until
   `autonomous_tick.py` is fixed to refuse `[x]` when output is the stub
   string, **trust no queue state without verifying the file exists**.
2. **Watchdog drift.** Last heartbeat is `2026-08-13T18:14:15+0000` (`.thesis_heartbeat`)
   or `2026-08-14T10:51` (`data/progress.jsonl` last record) — 20 days ago.
   `scripts/thesis_watchdog.py` was patched 2026-08-28 to read freshest across
   6 paths but the underlying tick loop has not run since then.
3. **Kanban dispatch broken.** All 12+ dispatched tasks have been returning
   `crashed` / `protocol_violation` since 2026-08-13 because
   `git worktree add` cannot resolve the working tree branch reference. This
   task itself is the 4th attempt on `t_d6e060e3`.

---

## 5. Critical path — next 3 actions

These are the **only** three things that move the thesis forward this week:

1. **Revert the auto-stub ticks** for at least Phase 5 paper-writing tasks
   (T091-T100). Those 10 pending items are what blocks Section 1/4/5/6 of the
   paper, the figures/tables, and the 8-page compile. Without them the paper
   cannot be submitted.
2. **Fix the tick script** (`scripts/autonomous_tick.py` line that writes the
   stub string) so it requires a non-stub output before flipping `[x]`. One-line
   guard, ~5 min change, prevents the next 20 days of drift.
3. **Decide scope between the two repos.** Either (a) keep `paraguay-geodata-vlm`
   as a substrate and move all writing to `satellite-paraguay`, or (b) re-merge.
   This repo's `Capitulos/` and `Defensa/` directories were deleted in the
   most recent main commit (`0e1bbb8`); that commit also added a banner pointing
   evaluators to `satellite-paraguay`. Confirm and commit to the split.

---

## 6. Risk register — open items (L/M/H)

From `RISK_REGISTER.md`. Top 5 by severity × probability:

| # | Risk | P | S | Status |
|---|---|---|---|---|
| T1 | GPU unavailable for fine-tune | L | M | open |
| T3 | IGN WMS service down | M | L | open |
| T4 | Sentinel-2 download too slow | M | M | open |
| T7 | Fine-tune overfits small (10K) dataset | M | M | open |
| T9 | RAG retrieval quality too low | M | M | open |
| D1 | MOPC drone imagery not public | H | M | open |
| D3 | INDI indigenous geojson unavailable | M | M | open |
| D5 | Class imbalance (too many "unknown") | M | M | open |

Two accepted-as-future-work: D2 (OSM Chaco sparsity), D4 (Catastro closed).

---

## 7. Spend & burn-rate

| Metric | Value |
|---|---|
| Thesis spend (10d) | **$3,441** (Sonnet-equiv, actual) |
| Run-rate | **$10,323 / month** |
| Prior estimate | $680 / month (off by 15× — see memory entry) |
| Tasks/day (recent) | 0.00 (stalled 20d) |

`THESIS_COST_BREAKDOWN.md` is the canonical spend ledger; do not duplicate.

---

## 8. Cross-repo status

| Repo | Role | Last commit | State |
|---|---|---|---|
| `paraguay-geodata-vlm` (this) | substrate + autonomy | `0e1bbb8` (2026-09-03) | clean tree, behind remote by ~13k deletions |
| `satellite-paraguay` | thesis (6 papers + manuscript) | unknown from this repo | separate cadence |

Read `THESIS_ARCHITECTURE.md` first if you are a fresh agent or evaluator.

---

## 9. Definition of done for THIS file

A weekly tick should overwrite this file in-place when:
- A new `## 1. Headline numbers` row should reflect the post-tick queue state
- Section 3 (`Completed`) should add any newly-verified rows
- Section 4 (`Blockers`) should add/resolve
- Section 5 (`Critical path`) should rotate to the next 3 actions
- Sections 6/7/8 are stable — only update on material change

**Do not** append a "history" section here — git log is the history. The
weekly cron (`thesis-weekly.sh`) writes to `logs/weekly.log` for trend data.

---

*Last regenerated by task `t_d6e060e3` on 2026-09-03. Source data:
`TASK_QUEUE.md`, `PROGRESS.md`, `RISK_REGISTER.md`, `data/progress.jsonl`,
`THESIS_ARCHITECTURE.md`, `THESIS_COST_BREAKDOWN.md`, `.thesis_heartbeat`.*