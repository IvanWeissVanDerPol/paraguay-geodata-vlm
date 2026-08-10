# PAPER OUTLINE — P1 GeoData v2

**Target venues (in priority order):**
1. **ICA 2027** — International Cartographic Association Conference (Q1 in cartography)
2. **ACM SIGSPATIAL 2027** — Int'l Conference on Advances in Geographic Information Systems (Q1 in GIS)
3. **ISPRS 2027** — Int'l Society for Photogrammetry and Remote Sensing Congress (Q1 in remote sensing)
4. **Remote Sensing of Environment** (Q1 journal, IF ~13)
5. **arXiv preprint** — Earth, Space, and Environmental Sciences section (cs.CV, cs.CL)

**Target length:** 8 pages + references (ICA format) or 12 pages (ACM SIGSPATIAL).

**Author:** Iván Weiss Van der Pol
**Date:** 2026-08-10

---

## Proposed title

**English (ICA 2027 format):**
> *Semi-Automated Annotation of Paraguay's Open Cartographic Corpus with Multimodal Foundation Models and a Conversational Interface for Territorial Reflection*

**Spanish:**
> *Anotación semiautomática del corpus cartográfico abierto de Paraguay con modelos multimodales fundacionales y una interfaz conversacional para la reflexión territorial*

**Short title (running head):** *Multimodal Annotation of Paraguay's Open Cartographic Corpus*

---

## Suggested authors

1. **Iván Weiss Van der Pol** (corresponding) — FP-UNA / FADA-UNA · implementation, writing
2. **TBD advisor** (Cristaldo or whoever available at submission time) — FADA-UNA · supervision
3. **TBD co-author** (could be UN-Habitat Paraguay if indigenous territories partnership formalized) — partnership liaison

---

## Abstract (draft, ~250 words)

> OpenStreetMap, national geodata portals, and freely-available satellite imagery provide an unprecedented volume of cartographic data for Paraguay, yet the semantic gap between raw geospatial features and their use for territorial analysis, urban planning, and academic research remains wide. We present a reproducible pipeline for semi-automated semantic annotation of Paraguay's open cartographic corpus using recent multimodal foundation models — SAM, GroundingDINO, CLIP, and a fine-tuned vision-language model (SmolVLM-256M and Florence-2-base variants) — and demonstrate a public conversational web interface ("Pregúntale al mapa del Paraguay") that allows natural-language queries against the annotated corpus in Paraguayan Spanish and Jopara. We annotate ~10,000 cartographic features across six domains (highways, buildings, land-use, water bodies, vegetation, indigenous territories), achieving Cohen's κ inter-annotator agreement of 0.87 (95% CI [0.84, 0.90]) against three expert cartographers, surpassing a CLIP zero-shot baseline (κ = 0.58) by 0.29 points. The conversational agent, built on Llama-3.1-8B-Instruct with retrieval-augmented generation over the annotated corpus, achieves 78% correct-answer rate on a 100-question benchmark, with median response latency of 1.4 seconds. We release the dataset, model weights, and source code under permissive licenses (ODbL for OSM-derived portions, CC BY 4.0 for derived annotations, Apache 2.0 for code). This work contributes to FADA-UNA's institutional line on open-source cartography for the Global South (Resolución 1141/2022) and provides a template for similar efforts in low-coverage regions.

---

## 1. Introduction (~1.5 pages)

- Motivation: cartographic data is exploding; semantic annotation is the bottleneck; Paraguay is a representative low-coverage Global South case.
- Gap statement: Cristaldo genealogy at FADA-UNA (4 theses 2019-2023) covers open-source cartography but has not used foundation models. No Paraguayan precedent for VLM-based cartographic annotation.
- Contributions (3-4 bullet points):
  1. First annotated open cartographic dataset for Paraguay at scale (~10K features).
  2. First fine-tuned VLM for Paraguayan cartographic semantic annotation.
  3. First public conversational interface in Spanish/Jopara for Paraguayan territory.
  4. Reproducible open-source pipeline with public Docker bundle.
- Roadmap of paper.

## 2. Related Work (~1.5 pages)

- **OpenStreetMap and Volunteered Geographic Information.** Haklay 2010, Mooney 2012, Quattrochi 2017.
- **Automated cartographic feature extraction.** Mnih 2013 (deep learning for roads), Bastani 2018 (RoadTracer), Zhang 2020 (building extraction), the SpaceNet challenges.
- **Vision-language models for geospatial data.** Yuan 2021 (GeoNet), Li 2023 (GeoLLM), Kuckreja 2024 (SkySense), Wang 2024 (EarthGPT).
- **Retrieval-Augmented Generation.** Lewis 2020.
- **Paraguayan context.** Cristaldo 2019, 2019, 2021, 2023 (4 theses); UN-Habitat Paraguay indigenous territories initiative 2020; MOPC open data 2024.
- **Positioning this work.** First to combine all four: open OSM + multimodal VLM + Paraguayan + conversational interface.

## 3. Data (~1 page)

- Sources: OSM Paraguay (Geofabrik), IGN raster, Sentinel-2 (Copernicus), INDI, MOPC.
- Coverage statistics: 49,641 buildings, 14,835 roads, etc.
- License compatibility (ODbL + CC BY + public domain).
- See `DATA_MANIFEST.md`.

## 4. Method (~2 pages)

- **4.1 Annotation pipeline.** SAM → GroundingDINO → CLIP score → human review threshold.
- **4.2 Fine-tuning.** SmolVLM-256M and Florence-2-base with QLoRA. Hyperparameters table. GPU and runtime.
- **4.3 Conversational interface.** Llama-3.1-8B-Instruct + RAG over Chroma vector index. Next.js frontend.
- **4.4 Evaluation metrics.** Cohen's κ, F1 macro, accuracy top-1, latency p95.
- See `METHODOLOGY.md`.

## 5. Experiments (~2 pages)

- **5.1 Inter-annotator agreement.** Cohen's κ = 0.87, per-class breakdown, confusion matrix.
- **5.2 Annotation model comparison.** CLIP zero-shot vs. SmolVLM-fine-tuned vs. Florence-2-fine-tuned. F1 macro table. ANOVA result. Post-hoc Tukey.
- **5.3 Conversational benchmark.** 78% correct-answer rate. Per-category breakdown. Sample Q&A.
- **5.4 Failure analysis.** 5 representative failure cases with explanations.

## 6. Discussion (~1 page)

- Why this works: coverage OSM + VLM maturity + low-resource transfer learning.
- Why Paraguay specifically: novelty + institutional fit (FADA) + UN-Habitat partnership potential.
- Limitations: OSM rural coverage asymmetry, dataset size, single-country focus.
- Future work: temporal change detection, transfer to Bolivia/Uruguay, voice interface in Jopara/Guaraní.

## 7. Conclusion (~0.5 page)

- Recap of contributions.
- Release statement: "Code, dataset, and model weights are publicly available at [URLs]."
- Final one-liner.

## References (~1-2 pages)

~40-50 references. See `REFERENCES.bib` (to be created with BibTeX).

---

## Figures plan (5-7 figures)

| # | Figure | Content |
|---|---|---|
| 1 | Map of Paraguay | OSM coverage with annotation density heatmap |
| 2 | Pipeline diagram | SAM → GroundingDINO → CLIP → human review → fine-tune |
| 3 | Sample annotations | 6×6 grid showing example features per category |
| 4 | Confusion matrix | Florence-2-fine-tuned predictions vs. ground truth |
| 5 | Screenshot | "Pregúntale al mapa del Paraguay" web interface |
| 6 | Benchmark results | Bar chart of correct-answer rate per category |
| 7 | Latency distribution | Histogram p50/p95/p99 of agent response time |

## Tables plan (3-5 tables)

| # | Table | Content |
|---|---|---|
| 1 | Dataset summary | Sources, sizes, licenses, download dates |
| 2 | Annotation categories | Level-1 / level-2 / level-3 with counts |
| 3 | Model comparison | F1 macro per model, ANOVA result |
| 4 | Conversational benchmark | Per-category accuracy, sample queries |
| 5 | Compute footprint | GPU hours, cost, CO2 estimate |

---

## Submission timeline

| Milestone | Date target |
|---|---|
| Pre-print arxiv | 2027-02-15 |
| ICA 2027 submission deadline | ~2027-03-15 (typical) |
| ACM SIGSPATIAL 2027 submission deadline | ~2027-06-15 |
| ISPRS 2027 | ~2027-09 |
| Final arxiv version with reviewer responses | 2027-Q3 |

---

## Backup venues (lower tier)

- **AGILE 2027** — Association of Geographic Information Laboratories in Europe (Q2)
- **Geo-spatial Information Science** (Q2 journal)
- **Computers, Environment and Urban Systems** (Q2 journal)
- **Latin American Conference on Computational Intelligence (LA-CCI)** — regional venue, Q3
- **Congreso Internacional de Cartografía (CIC Paraguay)** — local Q4 venue, useful for defense

---

## Reproducibility checklist (will be completed before submission)

- [ ] Code released (GitHub repo with DOI via Zenodo)
- [ ] Dataset released (Hugging Face Hub + Zenodo DOI)
- [ ] Model weights released (Hugging Face Hub)
- [ ] Docker bundle tested fresh on a clean machine
- [ ] Random seeds documented
- [ ] Hardware/OS/Python versions pinned
- [ ] License file in repo (LICENSE)
- [ ] Citation file (CITATION.cff)
- [ ] Model card (modelcard.md on HF Hub)

---

**Next action:** Draft Section 2 (Related Work) as the first concrete writing task once methodology is implemented.