# Thesis Pick — Iván's Decision Matrix

**Strategy:** Solo, paper-first, no advisor gate, no bureaucracy.
**Date:** 2026-08-10
**Author:** Erebus (Hermes agent)

---

## The 4 realistic solo-doable paths

| Path | Title (Spanish) | Faculty | Bureaucracy | Data access | Novelty | Time to arxiv | Q1 publishable? |
|---|---|---|---|---|---|---|---|
| **P1** | GeoData v2 — Anotación semiautomática con modelos multimodales del corpus cartográfico abierto de Paraguay | FADA | **0/5** (public OSM/IGN/Sentinel-2) | **Trivial** — `paraguay-geodata` repo already has it | **High** (no Paraguayan precedent) | ~5-6 mo | Likely (ICA/SIGSPATIAL/Remote Sensing) |
| **P3-light** | Jopara NLP sobre corpus público paraguayo (sintético + Twitter público + GuaraníBERT) | FP-UNA | **0/5** (no human subjects, public data) | Easy (HF + public tweets + Díaz 2025 corpus) | **High** (extends Díaz 2025) | ~4-6 mo | Possible (LREC/Cognitive Computation) |
| **P3-self** | Auto-etnografía: detección de sintomatología depresiva en mis propias conversaciones de Telegram (1 sujeto = yo) | FP-UNA + FCM | **1/5** (self-IRB waiver, UNA may still ask) | **Trivial** — my own data | **Very high** (first self-study Jopara MH) | ~5-7 mo | Possible (JMIR Mental Health, Digital Health) |
| **P3-Karamanu** | Chagas heatmap / vigilancia basada en datos abiertos SENEPA-MSPBS | FCM | **0/5** (aggregate public health, no IRB) | Moderate (need SENEPA + satellite) | Medium (precedent exists in Mexico/Brazil) | ~4-5 mo | Q2 (PLOS NTD, Geospatial Health) |

## Decision criteria (in priority order)

1. **Bureaucracy = 0.** Hard constraint from you.
2. **Data accessibility = trivial.** I have it now or can pull it this week.
3. **Novelty = high.** Q1 publishable. No Paraguayan precedent.
4. **Time to arxiv = 4-6 months.** Not 12.
5. **Q1 publishable** as stretch goal.

## Scoring (1-5, higher = better)

| Path | Buro=0 | Data | Novelty | Speed | Q1 | **Total** |
|---|---|---|---|---|---|---|
| **P1** | 5 | 5 | 4 | 4 | 4 | **22** |
| **P3-light** | 5 | 4 | 4 | 5 | 3 | **21** |
| **P3-self** | 3 | 5 | 5 | 3 | 3 | **19** |
| **P3-Karamanu** | 5 | 3 | 2 | 5 | 2 | **17** |

## Recommendation: **P1 GeoData v2**

**Why it wins:**
- Zero bureaucracy. Public data. No human subjects.
- You already have the data (`paraguay-geodata` repo deployed at paraguay-geodata.com).
- Strong Paraguayan novelty — nobody in UNA has applied CV/LLM to OSM Paraguay.
- Existing 4-thesis Cristaldo genealogy at FADA = you walk in with a finished paper and they'll co-sign for the defensa because it directly extends their lineage.
- Methodology is clean: SAM + GroundingDINO + Llama-3.2-Vision → fine-tune → "Pregúntale al mapa del Paraguay" web app.
- Publication venues: ICA (Int'l Cartographic Association), ACM SIGSPATIAL, Remote Sensing of Environment, ISPRS.
- FADA's official research line (Resolución 1141/2022) explicitly funds this.

**Runner-up: P3-light** if you ever want a language/NLP thesis. We can do both eventually.

---

## What we start building TODAY (next 7 days)

Working dir: `/opt/data/thesis-active/`

### Week 1 — Data + IRB + Methodology skeleton
1. ✅ Lock P1 GeoData v2 (this document)
2. 📋 IRB/ethics review → conclude **NO IRB needed** (no human subjects) — write formal `ETHICS_WAIVER_MEMO.md`
3. 📋 Formal UNA-format title + pregunta + objetivos + hipótesis (`FORMAL_PROPOSAL.md`)
4. 📋 Data manifest (`DATA_MANIFEST.md`) — list every dataset, license, source URL, SHA256
5. 📋 Methodology v0 (`METHODOLOGY.md`) — Chapter 3 skeleton
6. 📋 Reproducibility plan (`REPRODUCIBILITY.md`) — Docker bundle, seeds, hardware
7. 📋 Paper outline (`PAPER_OUTLINE.md`) — target venue: ICA 2027 or ACM SIGSPATIAL 2027
8. 📋 Latency/failure register (`RISK_REGISTER.md`)
9. 📋 Self-review + advisor-cosign plan (`DEFENSE_PLAN.md`) — what to do when thesis is done

### Week 2-4 — Data pipeline + baseline
- Pull OSM Paraguay extract (Geofabrik)
- Pull IGN raster tiles
- Build annotation pipeline (SAM + GroundingDINO)
- Generate ~10K annotated features

### Month 2-3 — Model training + web app
- Fine-tune SmolVLM/Florence-2 on annotated features
- Build "Pregúntale al mapa" Next.js app

### Month 4-5 — Validation + paper draft
- 200-feature inter-annotator test
- arxiv preprint submission
- Workshop paper draft for ICA 2027

### Month 6+ — Walk in, advisor co-signs, defensa
- Show up at FADA with finished manuscript
- Cristaldo (or whoever available) co-signs
- Defensa scheduled

---

## Status: STARTED

→ See `/opt/data/thesis-active/THESIS_PICK.md` (this file)
→ Next: `ETHICS_WAIVER_MEMO.md`, `FORMAL_PROPOSAL.md`, `DATA_MANIFEST.md`, `METHODOLOGY.md`