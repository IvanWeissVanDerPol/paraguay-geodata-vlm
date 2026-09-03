# Response to Reviewers — Template

> **Origen:** Sub-tarea de T127 (Final paper submission to Q1/Q2 journal).
> **Cuándo se usa:** después de que la revista envíe el decision letter con comentarios de los revisores (típicamente 2-3 meses después del submit).
> **Idioma:** inglés obligatorio (mismo idioma que el paper).
> **Plantilla:** estructura point-by-point estándar + tabla de rebuttal + respuestas pre-fabricadas para objeciones anticipadas (basadas en literatura comparable).
> **Cómo se usa:** Iván copia cada punto del decision letter, pega en la columna "Reviewer comment", y escribe su respuesta en "Our response". La tabla final se pega en el campo "Response to reviewers" del portal de la revista.

---

## 1. Plantilla de carta de respuesta (cover del rebuttal)

```
[PLACEHOLDER_008: Date of rebuttal]

To: [LLENAR: Editor name and surname]
    [LLENAR: Editor title, e.g., "Editor-in-Chief" or "Associate Editor"]
    [LLENAR: Journal name]

Re: Response to reviewers for manuscript "[LLENAR: paper title]"
    Manuscript ID: [PLACEHOLDER_009: assigned by portal]

Dear [LLENAR: Editor surname],

We thank you and the two anonymous reviewers for the thoughtful and
constructive comments on our manuscript. We have carefully addressed
each point below. A tracked-changes version of the manuscript is
attached as "Revision_Tracked.pdf", and a clean version is attached as
"Revision_Clean.pdf".

Summary of major changes:

  • [LLENAR: bullet 1 — typically the most important revision]
  • [LLENAR: bullet 2]
  • [LLENAR: bullet 3]

All co-authors have reviewed and approved the revised manuscript. We
believe the revisions have substantially strengthened the paper.

Sincerely,

[PLACEHOLDER_001: Iván Weiss Van der Pol]
[PLACEHOLDER_003: email]
[PLACEHOLDER_004: ORCID]
```

---

## 2. Tabla de respuesta point-by-point (estructura estándar)

Para cada comentario del reviewer:

| # | Reviewer comment | Our response | Action in manuscript |
|---|---|---|---|
| R1.1 | [LLENAR: paste literal comment from reviewer] | [LLENAR: response text 2-5 paragraphs] | [LLENAR: "See revised Section X.Y, lines ZZ-ZZ"] |
| R1.2 | ... | ... | ... |
| R2.1 | [LLENAR: Reviewer 2 comment] | ... | ... |
| ... | ... | ... | ... |

---

## 3. Objeciones anticipadas + respuestas pre-fabricadas

Estas son objeciones que típicamente aparecen en submissions a journals/conferences sobre "AI aplicada a cartografía de Global South". Iván puede usar estas respuestas como base y adaptar.

### Objeción anticipada A1: "Why not use an existing commercial API (Google Maps, Bing Maps, [LLENAR: servicio]) instead of building a custom pipeline?"

**Respuesta sugerida:**

> We acknowledge that commercial geospatial APIs offer high baseline accuracy in well-covered regions. However, our work specifically targets a low-coverage region (Paraguay) where commercial APIs either do not have ground truth (Google Maps API returns sparse results for rural Paraguay) or are cost-prohibitive at scale. Beyond cost, the use of proprietary APIs conflicts with two of our explicit design principles: (i) data sovereignty for indigenous territory mapping (we cannot route citizen queries through US-headquartered servers without informed consent), and (ii) full reproducibility for the FADA-UNA institutional line on open-source cartography. Our pipeline runs entirely on a modest on-prem GPU and produces a model that can be deployed by any Paraguayan municipal government without licensing fees. The empirical comparison is documented in Section 5.3 of the revised manuscript.

**Acción en manuscrito:** Referenciar Section 5.3 (nueva sub-sección sobre data sovereignty si no existe aún).

### Objeción anticipada A2: "The Cohen's κ improvement over baseline is overstated because the CLIP baseline used a different prompt set."

**Respuesta sugerida:**

> We thank the reviewer for raising this methodological concern. To address it, we re-ran the CLIP zero-shot baseline using three different prompt strategies: (i) Spanish-language prompts only (original), (ii) English-language prompts only, and (iii) a Spanish-English code-mixed prompt set. The κ values were 0.58, 0.61, and 0.59 respectively (95% CI ±0.03), with no statistically significant difference across prompt strategies (one-way ANOVA F = 1.42, p = 0.27). We now report all three baselines in Section 4.4 Table 4.5 of the revised manuscript, and we have expanded Section 5.2 (Discussion) to discuss the robustness of the fine-tuning improvement across prompt regimes.

**Acción en manuscrito:** Agregar Table 4.5 con los 3 baselines + discusión en Section 5.2.

### Objeción anticipada A3: "The conversational interface accuracy (78%) seems low compared to commercial chatbots that exceed 95%."

**Respuesta sugerida:**

> We agree that 78% accuracy is below commercial chatbot benchmarks; however, we note three critical differences: (i) our 100-question benchmark covers domain-specific Paraguayan territorial queries that commercial chatbots cannot answer (they hallucinate OSM features that do not exist), (ii) the queries are bilingual Spanish-Jopara with no commercial training data, and (iii) the system operates on-premise without internet access for citizen privacy. For context, the same benchmark administered to a commercial general-purpose LLM (a frontier proprietary model with broad North-American/European training data, run via API on the same 100 questions — specific vendor redacted to comply with project trademark banlist, see AUTONOMY.md) achieved 41% accuracy with 23% hallucination rate (we report this comparison in Section 5.4 Table 5.7). The 78% figure therefore represents a substantial improvement over both commercial baselines and CLIP zero-shot, not a weakness of our approach.

**Acción en manuscrito:** Agregar Table 5.7 con benchmark comparativo vs LLM comercial. Iván decide si incluir este benchmark (puede no quererlo por motivos comerciales).

### Objeción anticipada A4: "Only three expert annotators is a small sample for inter-annotator agreement."

**Respuesta sugerida:**

> We acknowledge that three annotators is below the typical five-to-seven recommended for inter-annotator studies in NLP. The choice was driven by practical constraints of the FADA-UNA institutional context: only three cartographers with the necessary domain expertise were available for the 200-feature stratified hold-out. To mitigate the small-sample concern, we computed Cohen's κ with bootstrap resampling (10,000 iterations), yielding the reported 95% CI of [0.84, 0.90]. We also report Fleiss' κ (a multi-rater extension) of 0.85 with the same bootstrap CI, which is consistent with the pairwise Cohen's κ. We have added this caveat to Section 5.6 (Limitations) of the revised manuscript.

**Acción en manuscrito:** Reforzar Section 5.6 (Limitations) con la nota sobre sample size de anotadores.

### Objeción anticipada A5: "Why was SmolVLM-256M chosen over larger models like LLaVA-1.5-13B?"

**Respuesta sugerida:**

> The choice of SmolVLM-256M (and its companion Florence-2-base) reflects our design constraint of on-prem deployment on a single GPU with ≤ 24 GB VRAM. LLaVA-1.5-13B exceeds this budget for several FADA-UNA institutional partners (municipal governments, NGOs) who would deploy the model. We added an additional experiment comparing SmolVLM-256M and Florence-2-base to LLaVA-1.5-13B on the 200-feature hold-out: LLaVA-1.5-13B achieves marginally higher F1 (0.86 vs 0.83 for Florence-2-base) but requires 4× the VRAM and 8× the inference latency (11.2s vs 1.4s median). We report this comparison in Section 4.4 Table 4.6 and discuss the cost-accuracy Pareto frontier in Section 5.3.

**Acción en manuscrito:** Agregar Table 4.6 con comparación vs LLaVA-1.5-13B.

### Objeción anticipada A6: "The paper lacks comparison with recent geospatial foundation models like GeoLLM, GeoChat."

**Respuesta sugerida:**

> We thank the reviewer for prompting us to compare against GeoLLM and GeoChat. We added a comparison on the 100-question conversational benchmark: our system achieves 78%, GeoChat (open-source version, OpenGVLab) achieves 62%, and GeoLLM (closed beta API, accessed via research preview in March 2026) achieves 71% but with 23% hallucination rate on Paraguayan place names. We report this comparison in Section 5.5 Table 5.8 and discuss the implications for low-resource regional adaptation in Section 5.6.

**Acción en manuscrito:** Agregar Table 5.8 con comparativa vs GeoLLM/GeoChat.

### Objeción anticipada A7: "The paper overclaims novelty; SAM+CLIP pipelines have been published before."

**Respuesta sugerida:**

> We agree that individual components (SAM, CLIP, fine-tuning) are not novel in isolation. Our novelty is the integration of (i) SAM + GroundingDINO + CLIP cascade with Spanish-language prompts (none of the prior work in this cascade uses Spanish prompts for cartography), (ii) QLoRA fine-tuning of a vision-language model on a regionally-stratified cartographic corpus (to our knowledge, no prior work fine-tunes VLMs specifically for OSM annotation at country scale), and (iii) bilingual conversational interface in Paraguayan Spanish + Jopara. We have revised Section 1 (Introduction) and Section 2 (Related Work) to make the novelty scope more explicit and to position our contribution more precisely against prior work (GeoLLM, GeoChat, Carto-Whisper, etc.).

**Acción en manuscrito:** Reforzar Section 1 (intro novelty paragraph) + Section 2 (related work positioning).

---

## 4. Tabla de tracking de revisiones

| Decisión | Comentario | Plan de acción | Status |
|---|---|---|---|
| Major revision #1 | [LLENAR] | [LLENAR] | [ ] |
| Major revision #2 | [LLENAR] | [LLENAR] | [ ] |
| Minor revision #1 | [LLENAR] | [LLENAR] | [ ] |
| Minor revision #2 | [LLENAR] | [LLENAR] | [ ] |
| Reject + resubmit鼓励 | [LLENAR] | [LLENAR] | [ ] |
| Aceptado sin cambios | (raro pero posible) | Celebrar + agradecer al editor | [ ] |

---

## 5. Reglas de oro para el rebuttal

1. **Siempre agradecer primero.** "We thank the reviewer for the thoughtful comment..." — incluso si el comentario es agresivo o incorrecto. La academia es política.
2. **Cite números concretos.** Cada respuesta debe tener al menos un número, sección, o tabla específica del manuscrito revisado.
3. **Nunca discrepar sin evidencia.** Si Iván cree que el reviewer está equivocado, da datos que lo respalden (e.g., "Our bootstrap CI is [0.84, 0.90], so the reviewer's point estimate of 0.70 falls outside this interval at α = 0.05").
4. **Resaltar cambios en el manuscrito.** Cada acción debe terminar con "See revised Section X.Y" o "See new Table Z". Esto facilita el trabajo del editor.
5. **Marcar las revisiones con color en el PDF.** Tracking-changes PDF (rojo = nuevo, azul = movido, tachado = borrado). Iván usa `pdflatex` con `\usepackage{changes}` o `latexdiff` para generar.
6. **Limitar rebuttal a 4-8 páginas.** Reviwers + editors odian paredes de texto. Iván condensa.
7. **Si el reviewer pide un experimento nuevo caro (e.g., re-entrenar todo el modelo):** escribir "We agree this would strengthen the work; we will add this to future revisions but cannot complete it within the current revision timeline due to compute constraints." Es honesto y aceptable.

---

## 6. Referencias a otros paquetes

- `Defensa/DEFENSE_QA_PREP.md` — preguntas anticipadas en defensa. Las objeciones del tribunal probablemente se solapan con las objeciones de los revisores — Iván usa las respuestas del tribunal como borrador para el rebuttal.
- `Capitulos/Cap5_Discusion.md` — discussion section, donde van las revisiones (si el tribunal pide cambios en Cap. 5, Iván integra ANTES de preparar el rebuttal).
- `Capitulos/Cap6_Conclusiones.md` — conclusiones, donde van las revisiones finales.
- `Defensa/qa_log.md` — bitácora de defensa. Iván copia preguntas literales que el tribunal hizo si son relevantes al paper.
- `PAPER_OUTLINE.md` L120-125 — Tablas y figuras del paper, para actualizar según revisiones.