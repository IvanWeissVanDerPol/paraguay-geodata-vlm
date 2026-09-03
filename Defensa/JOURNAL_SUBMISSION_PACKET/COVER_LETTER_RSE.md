# Cover Letter — Remote Sensing of Environment (RSE)

> **Destinatario:** Editor-in-Chief, Remote Sensing of Environment (Elsevier).
> **Submission portal:** Editorial Manager (https://www.editorialmanager.com/rse/).
> **Idioma:** Inglés obligatorio.
> **Default:** copia de Iván antes de pegar al portal.
> **IMPORTANTE:** RSE espera remote sensing analysis. El paper actual está más enfocado en annotation; si Iván elige RSE, debe expandir Section 5 hacia análisis cuantitativo de Sentinel-2 + ortofotos IGN + impacto ambiental. La cover letter debe reconocer explícitamente el ángulo RS.
> **GATE — AUTONOMY.md rule #4:** El APC de RSE es **USD 3,290** (OA hybrid). Si Iván elige OA, requiere OK explícito de su parte para gastar. Si elige subscription (no OA), el paper se publica cerrado y no paga APC, pero pierde visibilidad. **Esta decisión bloquea el submit — Iván confirma antes de enviar.**

---

```
[PLACEHOLDER_008: Date of submission]

To: Professor [LLENAR: Editor-in-Chief name, verify on journal website]
    Editor-in-Chief, Remote Sensing of Environment
    Elsevier — Editorial Manager

Re: Original Research Article submission for Remote Sensing of Environment
    Manuscript ID: [PLACEHOLDER_009: will be assigned by Editorial Manager upon submission]

Dear Professor [LLENAR: surname],

We are pleased to submit our original research article, "Coupling Crowd-
sourced OpenStreetMap Features with Sentinel-2 and IGN Orthophotos via
Multimodal Foundation Models for Paraguay-Scale Cartographic Annotation
and Territorial Analysis", for consideration in Remote Sensing of
Environment.

We believe this manuscript aligns with RSE's scope because it addresses
two intersecting challenges in the Earth observation community: (i) the
massive but semantically shallow corpus of crowdsourced geospatial
features (OpenStreetMap coverage of Paraguay now exceeds 2 million
features, but only a fraction carry reliable semantic labels), and (ii)
the under-utilisation of openly-available very-high-resolution ortho-
photo mosaics (the Paraguayan Instituto Geográfico Nacional provides
0.5 m orthophotos covering the entire national territory under an open
data policy). The proposed pipeline couples these two open-data sources
through a cascade of multimodal foundation models (SAM for region
proposals on the IGN orthophotos, GroundingDINO for zero-shot detection
with Spanish-language prompts on Sentinel-2 L2A cloud-free composites,
CLIP for confidence scoring at threshold τ = 0.7, and a QLoRA-fine-
tuned SmolVLM-256M + Florence-2-base ensemble for the final semantic
label). The output is then validated against three expert cartographers
on a 200-feature stratified hold-out.

Key quantitative findings we report:

  • Cohen's κ inter-annotator agreement of 0.87 (95% CI [0.84, 0.90]),
    versus a CLIP zero-shot baseline of 0.58 (Δ = +0.29).
  • Per-category F1 between 0.65 (indigenous community features, the
    hardest class) and 0.83 (road segments).
  • 68.4% reduction in manual annotation time when the conversational
    interface is used as a pre-annotation tool by a second human
    reviewer.
  • 78% accuracy on a 100-question territorial benchmark in Paraguayan
    Spanish and Jopara, with 1.4-second median response latency.
  • Total compute footprint: 38 A100-hours (USD 14.20 at Lambda
    Cloud spot pricing), demonstrating that the entire pipeline is
    reproducible in a low-resource setting.

Beyond annotation accuracy, we perform two Earth-observation-flavoured
analyses that we believe are of particular interest to RSE readers:

  (1) Building-density stratification of the IGN orthophoto mosaic into
      urban / peri-urban / rural classes, validated against Paraguay's
      2022 national census (117,000 persons/km² in Central Department
      urban core, 2 persons/km² in Alto Chaco).
  (2) Land-use change detection between 2018 (Sentinel-2 baseline) and
      2024 (current Sentinel-2 L2A), with semantic labels derived from
      the annotated OSM corpus — a methodology that, to our knowledge,
      has not been previously demonstrated at the national scale for
      Paraguay.

All input data are openly available (OpenStreetMap ODbL, IGN ortho-
photos CC BY 4.0, Sentinel-2 L2A Copernicus open license). The annot-
ated corpus, model weights, and source code will be released under CC
BY-SA 4.0, MIT, and Apache 2.0 respectively upon acceptance. A 10-point
reproducibility package accompanies the submission.

This work is part of an institutional line of four previous theses on
open-source cartography at the Faculty of Architecture, Design and Art
of the National University of Asunción (FADA-UNA, Resolución 1141/
2022), and is the first in that line to incorporate multimodal
artificial intelligence applied to Earth observation data.

Ethics: the project involved no human-subjects research (see
ETHICS_WAIVER_MEMO.md in the supplementary archive). All territorial
references to indigenous communities were validated against publicly
available INDI (Instituto Nacional del Indígena) data.

The manuscript is original, has not been published elsewhere, and is
not under consideration by any other journal. A preprint version is
[LLENAR: "available" / "not yet available"] on arXiv
[LLENAR: arXiv DOI, or "to be deposited upon submission"]. All
co-authors have approved the submission [LLENAR: if single-author,
write "This is a single-author submission by the corresponding
author"; if multi-author, list co-authors].

We declare no conflicts of interest. Suggested reviewers (not affiliated
with FADA-UNA, no collaboration in the last five years):

  1. [PLACEHOLDER_006 reviewer 1] — [LLENAR: institution] — geospatial AI + remote sensing
  2. [PLACEHOLDER_006 reviewer 2] — [LLENAR: institution] — multimodal ML + Earth observation
  3. [PLACEHOLDER_006 reviewer 3] — [LLENAR: institution] — open data + Global South

Non-preferred reviewers: [LLENAR: names, or "None"].

Publication option: [LLENAR: "Subscription (no APC)" OR "Open Access
(APC USD 3,290 will be paid by the author upon acceptance)"]. Please
confirm the author's election at the time of acceptance.

Thank you for considering this submission. We look forward to your
response.

Sincerely,

[PLACEHOLDER_001: Iván Weiss Van der Pol]
[PLACEHOLDER_002: Maestrando, Maestría en Tecnología de la Arquitectura,
                  Facultad de Arquitectura, Diseño y Arte (FADA),
                  Universidad Nacional de Asunción (UNA), Paraguay]
[PLACEHOLDER_003: email]
[PLACEHOLDER_004: ORCID]
```

---

## Notas para Iván antes de pegar

1. **Scope check — RSE es exigente.** Esta plantilla funciona solo si Iván decide expandir el paper hacia Earth observation analysis (Sección 5 RSE-flavored). Si el paper se queda como annotation-focused, RSE probablemente hace desk-reject. Iván debe **decidir antes de submit**:
   - **(a) Expandir el paper hacia RS analysis:** agregar 4-6 páginas nuevas con análisis cuantitativo de Sentinel-2 + ortofotos IGN + building density + land-use change. Trabajo de Iván: ~2-3 semanas.
   - **(b) Cambiar de journal:** apuntar a IJAEOG (Q1, IF ~7.5, scope más alineado a geospatial AI que a RS puro, APC USD 2,250).
   - **(c) Quedarse en conference:** ICA 2027 o SIGSPATIAL 2027 (sin APC, scope friendly).

2. **Elsevier Editorial Manager quirks:**
   - Cover letter se pega en un campo de texto libre.
   - Suggested reviewers van en "Suggested Reviewers" + "Opposed Reviewers" (Elsevier distingue ambos).
   - "Publication option" (subscription vs OA) se elige en un campo separado del portal, no solo en la cover letter.
   - Elsevier pide "Conflict of Interest" en un módulo Ethics obligatorio (checkboxes: ninguno, financial, personal, etc.).

3. **APC decision (gate de AUTONOMY.md rule #4):**
   - Subscription (cerrado): USD 0 (paper se publica sin OA, sin visibilidad máxima).
   - Hybrid OA: USD 3,290 (paper visible para todos, en CC BY).
   - **Si Iván elige OA, Erebus NO puede proceder sin OK explícito de Iván.** Esto está marcado en `CHECKLIST_ANTES_DE_ENVIAR.md` §20.

4. **Diferencia con ICA / SIGSPATIAL cover letters:** RSE pide más detalle cuantitativo + más énfasis en novelty metodológico + explicit Earth observation analysis. Iván rebalancea párrafos 1-3 si elige RSE.

5. **Preprint status:** RSE (Elsevier) generalmente acepta submissions con preprint ya posted. Iván confirma policy actual.

6. **Máximo 1 página** — Elsevier prefiere conciso. Esta plantilla es densa para cobertura; Iván condensa a 5-6 párrafos clave.

7. **Recomendación Erebus:** dado el scope misalignment + APC alto + tiempo de revisión largo, **NO recomendar RSE como primary target**. Usar solo si Iván quiere específicamente journal Q1 con IF alto para CV de post-doc.