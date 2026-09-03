# Cover Letter — ICA 2027

> **Destinatario:** Editor-in-Chief, 32nd International Cartographic Conference (ICA) 2027.
> **Track recomendado:** "Open Data and Crowdsourced Geospatial Information" o "AI/ML for Cartography".
> **Idioma:** Inglés obligatorio.
> **Default:** copia de Iván antes de pegar al portal del conference management system.
> **Personalizar antes de pegar:** `[LLENAR]` y `[PLACEHOLDER_NNN]` según §2 del `README.md` del paquete.

---

```
[PLACEHOLDER_008: Date of submission]

To: ICA 2027 Program Committee
    c/o International Cartographic Association
    [Conference submission portal: papers.icc2027.org or equivalent]

Re: Submission to 32nd International Cartographic Conference (ICA 2027)
    Track: [LLENAR: "Open Data and Crowdsourced Geospatial Information" or "AI/ML for Cartography"]

Dear Members of the Program Committee,

I am pleased to submit our manuscript entitled "Semi-Automated Annotation
of Paraguay's Open Cartographic Corpus with Multimodal Foundation Models
and a Conversational Interface for Territorial Reflection" for
consideration at the 32nd International Cartographic Conference (ICA
2027).

The work addresses a structural gap in the Global-South cartographic
corpus: although Paraguay's OpenStreetMap coverage now exceeds 2 million
features (~49,641 buildings, ~14,835 road segments catalogued), the
semantic annotation that gives those features meaning for territorial
analysis, urban planning, and academic research remains a slow, manual
process. Our pipeline integrates four multimodal foundation models
(SAM, GroundingDINO, CLIP, and a QLoRA-fine-tuned vision-language model
based on SmolVLM-256M and Florence-2-base) to automate that annotation
at scale, and validates the result against three expert cartographers
on a 200-feature stratified hold-out. We achieve Cohen's κ inter-
annotator agreement of 0.87 (95% CI [0.84, 0.90]), a 0.29-point
improvement over a CLIP zero-shot baseline (κ = 0.58). A companion
conversational web interface ("Pregúntale al mapa del Paraguay") answers
natural-language queries against the annotated corpus in Paraguayan
Spanish and Jopara, reaching 78% accuracy on a 100-question benchmark
with 1.4-second median latency.

The contributions we believe are most relevant to the ICA community are:

  1. A reproducible, open-source pipeline that integrates SAM, GroundingDINO,
     CLIP, and QLoRA fine-tuning for semantic annotation of crowdsourced
     geospatial features in a low-coverage region.

  2. Empirical evidence that fine-tuning a small vision-language model on
     10,000 regionally-stratified features corrects the geographic bias of
     foundation models pre-trained on predominantly North-American and
     European imagery (the LAION-2B corpus contains less than 2% of images
     labelled Paraguay).

  3. A bilingual conversational interface (Spanish / Jopara) designed for
     on-premise deployment, addressing data sovereignty concerns that are
     particularly salient for indigenous territory mapping and citizen
     science in the Global South.

  4. The annotated corpus itself (released under CC BY-SA 4.0), a public
     good for cartographic research in Paraguay and adjacent low-coverage
     regions.

This work is part of an institutional line of four previous theses on
open-source cartography and participatory mapping at the Faculty of
Architecture, Design and Art of the National University of Asunción
(FADA-UNA, Resolución 1141/2022), and is the first in that line to
incorporate multimodal artificial intelligence. The project was carried
out under ethics waiver [LLENAR: protocol number from FADA ethics
committee, if applicable; otherwise "no human-subjects research, see
ETHICS_WAIVER_MEMO.md in the supplementary archive"].

The manuscript is original, has not been published elsewhere, and is not
under consideration by any other journal or conference. It has been
prepared in accordance with the ICA 2027 template (8 pages + 2 pages
references). All co-authors have approved the submission [LLENAR: if
single-author, write "This is a single-author submission by the
corresponding author"; if multi-author, list co-authors].

We have no conflicts of interest to declare. Suggested reviewers (who
are not collaborators of the authors and are not affiliated with FADA-
UNA) are listed in the submission portal. We respectfully request that
the following NOT review the manuscript due to direct professional
collaboration in the last five years: [LLENAR: names, or write "None"].

Suggested reviewers:

  1. [PLACEHOLDER_006 reviewer 1]
     [LLENAR: full name and title]
     [LLENAR: institution, department, country]
     [LLENAR: email]
     Expertise: geospatial AI, crowdsourced cartography

  2. [PLACEHOLDER_006 reviewer 2]
     [LLENAR: full name and title]
     [LLENAR: institution, department, country]
     [LLENAR: email]
     Expertise: multimodal foundation models, remote sensing

  3. [PLACEHOLDER_006 reviewer 3]
     [LLENAR: full name and title]
     [LLENAR: institution, department, country]
     [LLENAR: email]
     Expertise: open data, Global South, indigenous territories

We confirm that the data, code, and model weights associated with this
submission will be released under permissive open licenses (ODbL for
OSM-derived portions, CC BY-SA 4.0 for the annotated corpus, Apache 2.0
for the source code, and the MIT license for the model weights) upon
acceptance. A reproducibility checklist (10 points) is included in the
supplementary archive and will be made available on GitHub at
[LLENAR: github.com/iweiss-vdp/paraguay-cartography-annotation, or
actual repository URL upon acceptance] and on Hugging Face Hub at
[LLENAR: huggingface.co/iweiss-vdp or actual HF Hub URL].

We thank the Program Committee for considering this submission and look
forward to the opportunity to present the work at ICA 2027.

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

1. **Quitar todos los `[LLENAR]` y `[PLACEHOLDER_NNN]`** y reemplazarlos con datos reales.
2. **Si Iván tiene advisor co-autor:** cambiar "We" por "I" en los párrafos que hablan de authorship, listar co-autor en línea "[PLACEHOLDER_005: Co-author name + affiliation]".
4. **Suggested reviewers:** la sección va también en el campo "Suggested Reviewers" del portal, no solo en la cover letter. Iván debe duplicar.
5. **"NOT review"** (non-preferred reviewers): algunas revistas permiten este campo; Iván lo llena si tiene razones (e.g. un revisor que rechazó su paper anterior sin fundamento).
6. **Adjuntar en el portal:** la cover letter se pega en el campo "Cover Letter" o se sube como archivo `.txt` / `.pdf` separado según las instrucciones del CMS de ICA.
7. **No incluir datos personales no necesarios** (CI, teléfono, dirección). Solo email + ORCID + afiliación.
8. **Máximo 1 página** — esta plantilla es larga para asegurar cobertura; Iván puede condensar a 4-5 párrafos si el portal limita caracteres.