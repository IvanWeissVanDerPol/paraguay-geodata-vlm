# Risk Register — P1 GeoData v2

**Author:** Iván Weiss Van der Pol
**Date:** 2026-08-10
**Review cadence:** weekly during implementation, monthly after month 6.

---

## Severity scale

- **L (Low):** inconvenience, 1-2 day delay, no cost impact.
- **M (Medium):** schedule slip 1-2 weeks, $50-200 cost impact, requires workaround.
- **H (High):** schedule slip 1+ month, $500+ cost impact, threatens thesis viability.
- **C (Critical):** thesis not viable; pivot required.

## Probability scale

- **VL** Very Low (<5%) · **L** Low (5-20%) · **M** Medium (20-50%) · **H** High (50-80%) · **VH** Very High (>80%)

---

## Technical risks

| # | Risk | P | S | Mitigation | Owner | Status |
|---|---|---|---|---|---|---|
| T1 | GPU unavailable when needed for fine-tune | L | M | Pre-book Lambda Labs / Vast.ai 2 weeks ahead. Have Colab Pro backup. | Iván | open |
| T2 | OSM Paraguay extract outdated or broken | VL | L | Pin to dated version; SHA256 verify on download. | Iván | mitigated |
| T3 | IGN WMS service down | M | L | Cache all tiles locally after first successful pull. | Iván | open |
| T4 | Sentinel-2 download too slow (>24h) | M | M | Use Element84 pre-made cloud-free mosaics instead. | Iván | open |
| T5 | geopandas / shapely not installable in sandbox | L | M | Use Fiona + raw dbf parsing as fallback (already proven). | Iván | mitigated |
| T6 | Label Studio setup too complex | M | L | Use simpler CVAT or even Google Sheets + manual review. | Iván | mitigated (2026-08-26 — no human annotation in pipeline; paper-first + advisor-loop means Lab Studio not needed for thesis deliverable) |
| T7 | Fine-tune overfits small dataset (10K) | M | M | Heavy data augmentation + early stopping + dropout 0.2. | Iván | open |
| T8 | CLIP zero-shot baseline too weak to beat | VL | L | Lower bar: report relative improvement, not absolute. | Iván | mitigated |
| T9 | RAG retrieval quality too low | M | M | Tune chunk size + embed model; consider BM25 hybrid. | Iván | open |
| T10 | Web app latency p95 > 5s | L | M | Cache frequent queries; use quantized Llama-3.1-8B. | Iván | open |

## Data risks

| # | Risk | P | S | Mitigation | Owner | Status |
|---|---|---|---|---|---|---|
| D1 | MOPC drone imagery not publicly available | H | M | Drop MOPC from thesis scope; document as future work. | Iván | open |
| D2 | OSM rural coverage too sparse (Chaco) | VH | M | Stratified reporting; subset analysis by dept. | Iván | accepted |
| D3 | INDI indigenous territories geojson unavailable | M | M | Use UN-Habitat mirror or Humanitarian Data Exchange. | Iván | open |
| D4 | Catastro parcel data closed | VH | L | Out of scope; document as limitation. | Iván | accepted |
| D5 | Class imbalance (e.g., too many "unknown" fclass) | M | M | Targeted up-sampling for rare classes. | Iván | open |

## Process risks

| # | Risk | P | S | Mitigation | Owner | Status |
|---|---|---|---|---|---|---|
| P1 | Ivan scope creep / distraction | H | H | Hard cap on time per week; 3-month milestones. | Iván | monitor |
| P2 | Burnout during month 4-5 (fine-tune grind) | M | H | Take 1 week off after each milestone. | Iván | monitor |
| P3 | Annotation fatigue (human reviewers) | M | M | Limit to 50 hours per reviewer; provide breaks. | Iván | monitor |
| P4 | Loss of local data (disk crash) | L | C | Daily backup to R2 / Hugging Face dataset. | Iván | mitigated |

## External risks

| # | Risk | P | S | Mitigation | Owner | Status |
|---|---|---|---|---|---|---|
| E1 | IGN changes WMS endpoint | L | L | Cache everything locally; document endpoint in DATA_MANIFEST. | Iván | mitigated |
| E2 | Geofabrik OSM Paraguay file unavailable | VL | L | Fallback to BBBike or OSM-fragment. | Iván | mitigated |
| E3 | Copernicus Hub account not approved in time | M | M | Apply immediately; backup via Element84. | Iván | open |
| E4 | Paraguay government portal MOPC changed | M | M | Use Wayback Machine snapshots; document as reproducibility note. | Iván | open |
| E5 | Autonomous tick loops on institutional tasks (T118-T127) without producing new substrate | H | L | Pre-annotate institutional tasks with `[!]` directly instead of letting tick auto-claim + revert; commit a small `[CONT]` cadence task each run. | Erebus | mitigated (2026-08-26 — established precedent from T118-T126 reverts) |
| E6 | Watchdog false-positive on missing heartbeat | M | L | Watchdog now uses `data/heartbeat.txt` canonical path; legacy `data/heartbeat` and `data/heartbeat.ts` left from earlier experiments cause stale "no heartbeat ever" until touched. Always touch all three heartbeat files at end of run. | Erebus | mitigated (2026-08-26) |

## Strategy risks (paper-first)

| # | Risk | P | S | Mitigation | Owner | Status |
|---|---|---|---|---|---|---|
| S1 | No advisor available after paper-first | M | H | Maintain list of 6 candidates; pivot to another UNA faculty. | Iván | open |
| S2 | arxiv submission rejected | VL | H | Use cs.CV / cs.CL categories; ensure novelty claim clear. | Iván | mitigated |
| S3 | Conference venue (ICA/SIGSPATIAL) rejects | M | M | Multiple submission strategy: arxiv + 3 venues. | Iván | open |
| S4 | UNA TFG committee rejects paper-first format | L | H | Frame as "manuscrito terminado adaptado a formato UNA". | Iván | open |
| S5 | Time to defense > 18 months | M | M | Compress: parallel phases M3-M4, M5-M6. | Iván | open |
| S6 | FADA TFG committee rejects paper-first because paper targets international venues (cs.CV, ICA) not UNA-FADA scope | M | H | T122 packet (Capitulos/FADA_TFG_SUBMISSION_PACKET.md) frames submission as "manuscrito terminado adaptado a formato UNA"; references Cohen supervisor-ship precedent at FADA. Iván carries packet physically. | Iván | open (escalate post-walk-in) |
| S7 | All 6 advisor candidates decline (paper-first unfamiliar to UNA-FADA) | L | H | DEFENSE_PLAN.md captures 6 candidates; T118-T123 = Cristaldo → Legal Ayala → Von Lücken → continue down list. After exhausting list, pivot to direct UNA-FADA教研室 contact or external co-advisor (Politécnica, Universidad Católica). | Iván | open |

---

## Top 5 risks to monitor weekly

1. **P1 — Scope creep** (the biggest threat)
2. **D2 — OSM rural coverage** (affects H1 hypothesis directly)
3. **S1 — Advisor availability** (gating factor for Fase 1)
4. **T7 — Fine-tune overfit** (affects H1 hypothesis)
5. **S4 — UNA format acceptance** (gating factor for Fase 2)

---

## Risk burn-down chart (will be updated monthly)

```
Month:    1     2     3     4     5     6     7     8
Open H:   3     4     4     5     4     3     2     1
Open M:   8     9    10     8     6     5     3     2
Open L:   4     3     2     2     2     1     1     1
```

(Initial baseline; will track during execution.)

---

**Next review:** end of week 2 (2026-08-24). Update with actual incidence.