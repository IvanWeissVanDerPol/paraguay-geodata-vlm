# TASK QUEUE — P1 GeoData v2

**This is the master backlog.** Autonomous ticks pick the next `[ ]` task, work it, mark `[x]`, and continue. No prompting required.

**Date created:** 2026-08-10
**Last tick:** never (initial state)
**Tasks total:** 67
**Tasks done:** 0
**Tasks remaining:** 67

---

## Legend

- `[ ]` pending · `[~]` in-progress (claimed by current tick) · `[x]` done · `[!]` blocked
- `[P0]` critical path · `[P1]` important · `[P2]` nice-to-have
- `[M1]` month 1 (Aug 2026) · `[M2]` month 2 · `[M3]` month 3 · `[M4]` month 4 · `[M5]` month 5 · `[M6]` month 6 · `[M7]` month 7
- `[GPU]` needs GPU · `[NO-GPU]` CPU-only OK · `[EXT]` needs external (creds, internet)
- `[W]` writes code/paper · `[D]` writes docs · `[R]` runs experiment · `[A]` automation/tooling

---

## Phase 0 — Setup & foundations [M1]

- [x] [P0][M1][NO-GPU][A] Create TASK_QUEUE.md, PROGRESS.md, autonomous_tick.py, weekly_review.py — `AUTONOMY`
- [x] [P0][M1][NO-GPU][A] Schedule daily tick cron job (06:00 UTC) and weekly review cron (Sun 18:00 UTC)
- [x] [P0][M1][NO-GPU][A] Create thesis-active-autonomy skill for fresh-session resume
- [x] [P0][M1][NO-GPU][A] Test autonomous tick dry-run end-to-end (pick task → execute → mark done → log)
- [x] [P0][M1][NO-GPU][D] Document the autonomous system in AUTONOMY.md
- [x] [P0][M1][NO-GPU][A] Add `make tick` (single tick), `make tick-dry`, `make weekly` targets to Makefile

## Phase 1 — Data pipeline [M1-M2]

- [x] [P0][M1][EXT][A] Register Copernicus dataspace account (5 min) — link emailed to Erebus
- [x] [P0][M1][EXT][A] Register HuggingFace write token — link emailed
- [x] [P0][M1][EXT][A] Register GitHub personal access token (repo scope) — link emailed
- [ ] [P1][M1][EXT][A] Register AWS free tier (alt to Copernicus) — link emailed
- [ ] [P1][M1][EXT][A] Register Google Cloud + activate Cloud Storage API — link emailed
- [x] [P0][M1][NO-GPU][A] Build scripts/fetch_ign_wms.py — IGN raster WMS puller  <!-- Wrote WMS fetcher; cannot test in sandbox (no DNS to ign.gob.py) -->
- [ ] [P0][M1][EXT][R] Download IGN raster tiles for 17 deptos + Asunción (~2 GB)
- [ ] [P0][M2][EXT][R] Download Sentinel-2 L2A cloud-free mosaic for Paraguay (via Element84 or Copernicus)
- [ ] [P1][M1][EXT][R] Download WorldPop Paraguay 2020 UN-adjusted (~50 MB)
- [ ] [P1][M2][EXT][R] Download CHIRPS daily precipitation 2024-2026 (~200 MB/year)
- [ ] [P1][M2][EXT][R] Download Google Open Buildings v3 for Paraguay tiles (~100 MB)
- [ ] [P1][M2][EXT][R] Download INDI indigenous territories GeoJSON (UN-Habitat mirror)
- [ ] [P2][M2][EXT][R] File MOPC drone imagery access request (Ley 5282/2014) — 15-day SLA
- [x] [P0][M1][NO-GPU][A] Build scripts/data_inventory.py — full SHA256 + size + license table  <!-- Working in sandbox -->
- [ ] [P0][M1][NO-GPU][D] Update DATA_MANIFEST.md with actual download dates + sizes

## Phase 2 — Annotation pipeline [M2-M3]

- [ ] [P0][M2][GPU][A] Build scripts/run_sam.py — SAM mask generator on raster tiles
- [ ] [P0][M2][GPU][A] Build scripts/run_grounding_dino.py — GroundingDINO detector with text prompts
- [ ] [P0][M2][GPU][A] Build scripts/run_clip.py — CLIP zero-shot scorer
- [ ] [P0][M2][GPU][R] Run auto-annotation on 10K building features (sample + score)
- [ ] [P0][M2][GPU][R] Run auto-annotation on 10K road features
- [ ] [P0][M2][GPU][R] Run auto-annotation on 10K landuse features
- [ ] [P0][M2][GPU][R] Run auto-annotation on 5K water features
- [ ] [P0][M2][GPU][R] Run auto-annotation on 5K natural features
- [ ] [P0][M3][NO-GPU][A] Set up Label Studio (Docker) + import 50K auto-annotated features
- [ ] [P0][M3][NO-GPU][R] Human review pass on 5K low-confidence features (1-3 categories)
- [ ] [P0][M3][NO-GPU][W] Export reviewed annotations to data/processed/annotations_v1.geojson
- [ ] [P0][M3][NO-GPU][A] Build scripts/inter_annotator_agreement.py — Cohen's κ + bootstrap CI

## Phase 3 — Fine-tuning [M4-M5]

- [ ] [P0][M4][GPU][A] Build scripts/train.py — generic QLoRA fine-tune loop (transformers + peft)
- [ ] [P0][M4][GPU][R] Fine-tune SmolVLM-256M-Instruct with QLoRA (3 epochs, batch 8)
- [ ] [P0][M4][GPU][R] Fine-tune Florence-2-base with QLoRA (5 epochs, batch 4)
- [ ] [P0][M4][GPU][R] Evaluate models on held-out test set (F1 macro, accuracy top-1)
- [ ] [P0][M4][GPU][R] Compute Cohen's κ inter-annotator agreement (target ≥ 0.85)
- [ ] [P0][M4][NO-GPU][D] Write model card (MODEL_CARD.md) for HuggingFace Hub
- [ ] [P0][M5][EXT][A] Upload fine-tuned model to HuggingFace Hub (paraguay-cartography-florence-2)
- [ ] [P0][M5][EXT][A] Upload annotated dataset to HuggingFace Hub (paraguay-cartography-annotated)
- [ ] [P0][M5][EXT][A] Mint Zenodo DOI for dataset snapshot

## Phase 4 — Conversational agent [M5-M6]

- [ ] [P0][M5][GPU][A] Build scripts/build_rag_index.py — Chroma vector index over annotated features
- [ ] [P0][M5][GPU][A] Build backend/ — FastAPI serving model + RAG agent
- [ ] [P0][M5][GPU][R] Test agent on 10 sample questions from BENCHMARK_QUESTIONS.md
- [ ] [P0][M6][GPU][R] Run full 100-question benchmark (record answers + latencies)
- [ ] [P0][M6][NO-GPU][R] Have 2 external reviewers score all 100 answers (Cohen's κ)
- [ ] [P0][M6][NO-GPU][W] Implement web app frontend (Next.js 16 + Tailwind v4)
- [ ] [P0][M6][EXT][A] Deploy web app to local_only / HF Spaces / VPS

## Phase 5 — Paper writing [M6-M7]

- [ ] [P0][M6][NO-GPU][W] Draft paper Section 2 (Related Work) — 30 refs minimum
- [ ] [P0][M6][NO-GPU][W] Draft paper Section 3 (Method) — pipeline + RAG detail
- [ ] [P0][M6][NO-GPU][W] Draft paper Section 4 (Experiments) — all tables + figures
- [ ] [P0][M6][NO-GPU][W] Draft paper Section 5 (Discussion) — limitations + future work
- [ ] [P0][M6][NO-GPU][W] Draft paper Section 1 (Introduction) — context + gap + contributions
- [ ] [P0][M6][NO-GPU][W] Draft paper Abstract (250 words) — problem + method + results
- [ ] [P0][M6][NO-GPU][W] Draft paper Section 6 (Conclusion) — recap + release statement
- [ ] [P0][M6][NO-GPU][D] Generate all figures (pipeline diagram, confusion matrix, benchmark chart)
- [ ] [P0][M6][NO-GPU][D] Generate all tables (dataset summary, model comparison, benchmark)
- [ ] [P0][M6][NO-GPU][W] Compile final 8-page paper (ICA format)
- [ ] [P0][M7][EXT][A] Submit paper to arxiv (cs.CV, cs.CL, cs.CY categories)
- [ ] [P0][M7][EXT][A] Submit paper to ICA 2027 / ACM SIGSPATIAL 2027
- [ ] [P1][M7][EXT][D] Write blog post / press release for Paraguayan tech press
- [ ] [P1][M7][EXT][D] Tweet thread / LinkedIn post announcing paper

## Phase 6 — Thesis manuscript (Cap. 1-6) [M7]

- [ ] [P0][M7][NO-GPU][W] Write Cap. 1 (Introducción) — UNA format, ~20 pages
- [ ] [P0][M7][NO-GPU][W] Write Cap. 2 (Marco Teórico) — ~40 pages, expand from paper Section 2
- [ ] [P0][M7][NO-GPU][W] Write Cap. 3 (Marco Metodológico) — already in METHODOLOGY.md, expand to ~30 pages
- [ ] [P0][M7][NO-GPU][W] Write Cap. 4 (Resultados) — ~40 pages, expand from paper Section 4
- [ ] [P0][M7][NO-GPU][W] Write Cap. 5 (Discusión) — ~20 pages, expand from paper Section 5
- [ ] [P0][M7][NO-GPU][W] Write Cap. 6 (Conclusiones) — ~10 pages, expand from paper Section 6
- [ ] [P0][M7][NO-GPU][D] Format manuscript per UNA-FADA template
- [ ] [P0][M7][NO-GPU][D] Build defense slides (45 min + 15 Q&A) — see DEFENSE_PLAN.md
- [ ] [P0][M7][NO-GPU][D] Rehearse defense with cron timer

## Phase 7 — Advisor outreach + defense [M8-M12]

- [ ] [P0][M8][EXT][A] Email advisor #1 (Cristaldo) — see DEFENSE_PLAN.md template
- [ ] [P0][M8][EXT][A] Email advisor #2 if #1 declines (Legal Ayala)
- [ ] [P0][M8][EXT][A] Email advisor #3 if #2 declines (Von Lücken)
- [ ] [P0][M8][EXT][A] Continue down list of 6 advisors until one accepts
- [ ] [P0][M9][NO-GPU][D] Submit thesis topic to FADA TFG committee for approval
- [ ] [P0][M9][NO-GPU][D] Formal enrollment as tesista at UNA
- [ ] [P0][M10][NO-GPU][D] Thesis committee review + revisions
- [ ] [P0][M11][NO-GPU][D] Public defense scheduling
- [ ] [P0][M12][NO-GPU][D] Public defense (45 min + Q&A)
- [ ] [P0][M12][EXT][D] Final paper submission to Q1/Q2 journal

---

## Maintenance tasks (run continuously)

- [ ] [P0][CONT][NO-GPU][A] Weekly: review PROGRESS.md, identify blockers, escalate
- [ ] [P0][CONT][NO-GPU][A] Weekly: update RISK_REGISTER.md with new risks + close resolved
- [ ] [P1][CONT][NO-GPU][W] Weekly: commit progress to git (small atomic commits)
- [ ] [P1][CONT][NO-GPU][D] Monthly: review THESIS_COST_BREAKDOWN.md, track actual spend
- [ ] [P2][CONT][EXT][R] Monthly: re-run sanity_check.py + report any degradation

---

## Special: When blocked, do this

When a task hits a blocker (creds missing, GPU unavailable, etc.), the tick:

1. Marks the task as `[!]` with a comment explaining the block
2. Records it in PROGRESS.md "Blockers" section
3. Picks the NEXT non-blocked task
4. Continues indefinitely

When Iván returns and resolves the blocker, the next tick picks up where it left off.

---

## Auto-prioritization

The tick script picks the next task by:
1. Filter `[ ]` (pending, not blocked)
2. Filter by current month (M1 → M7 by date)
3. Sort by priority (P0 > P1 > P2)
4. Pick the first

If no task is pending in the current month, fall back to:
- Next month's P0 tasks
- Maintenance tasks (CONT)
- Out-of-order P0/P1 if they're unblocking

---

**End of queue. Total: 67 tasks across 7 months + ongoing maintenance.**