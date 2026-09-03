# Cover Letter — ACM SIGSPATIAL 2027

> **Destinatario:** Program Committee, 35th ACM SIGSPATIAL International Conference on Advances in Geographic Information Systems.
> **Track recomendado:** Main track (los papers no van por track en SIGSPATIAL, pero Iván selecciona keywords en el portal).
> **Idioma:** Inglés obligatorio.
> **Default:** copia de Iván antes de pegar al portal de ACM (precision conference system — link típico https://sigspatial2027.submissions.com/).
> **Personalizar antes de pegar:** `[LLENAR]` y `[PLACEHOLDER_NNN]` según §2 del `README.md` del paquete.

---

```
[PLACEHOLDER_008: Date of submission]

To: ACM SIGSPATIAL 2027 Program Committee
    via the Precision Conference System submission portal

Re: Submission to the 35th ACM SIGSPATIAL International Conference on
    Advances in Geographic Information Systems (SIGSPATIAL 2027)
    Research Paper — Main Track

Dear Program Committee Members,

We are delighted to submit our paper, "Semi-Automated Annotation of
Paraguay's Open Cartographic Corpus with Multimodal Foundation Models
and a Conversational Interface for Territorial Reflection", for
consideration at SIGSPATIAL 2027.

This work makes three contributions that we believe are directly relevant
to the SIGSPATIAL community:

  (1) A reproducible, open-source pipeline for semantic annotation of
      crowdsourced geospatial features using a cascade of four multi-
      modal foundation models (SAM for region proposals, GroundingDINO
      for zero-shot detection with Spanish-language prompts, CLIP for
      confidence scoring at threshold τ = 0.7, and a QLoRA-fine-tuned
      SmolVLM-256M + Florence-2-base ensemble for the final semantic
      label).

  (2) An empirical study of geographic-bias correction in foundation
      models applied to cartography: we measure Cohen's κ inter-
      annotator agreement on a 200-feature stratified hold-out against
      three expert cartographers, comparing a CLIP zero-shot baseline
      (κ = 0.58), our fine-tuned ensemble (κ = 0.87, 95% CI [0.84,
      0.90]), and a recenter on the regional-vs-global pretraining
      data ratio.

  (3) A public-domain conversational web interface ("Pregúntale al mapa
      del Paraguay") that answers natural-language geospatial queries
      against the annotated corpus in Paraguayan Spanish and Jopara,
      built on Llama-3.1-8B-Instruct with retrieval-augmented generation
      over a Chroma vector index of the annotated features. The agent
      achieves 78% accuracy on a 100-question benchmark with 1.4-second
      median response latency.

The dataset, model weights, and source code will be released under
permissive open licenses upon acceptance (CC BY-SA 4.0 for the
annotated corpus, Apache 2.0 for the source code, MIT for the model
weights). A reproducibility package is included with the supplementary
archive.

The work is part of an institutional line of four previous theses on
open-source cartography at the Faculty of Architecture, Design and Art
of the National University of Asunción (FADA-UNA, Resolución 1141/
2022). The project was carried out under ethics waiver
[LLENAR: protocol number or "no human-subjects research, see
ETHICS_WAIVER_MEMO.md in the supplementary archive"].

The manuscript has not been submitted concurrently to any other venue
[LLENAR: or "A version of this manuscript has been deposited on arXiv
as preprint [arXiv:XXXX.XXXXX]; please see the submission portal for
the DOI."]. All co-authors have approved the submission [LLENAR: if
single-author, write "This is a single-author submission by the
corresponding author"; if multi-author, list co-authors].

We declare no conflicts of interest. The following suggested reviewers
are not affiliated with FADA-UNA and have not collaborated with the
author(s) in the past five years:

  1. [PLACEHOLDER_006 reviewer 1] — [LLENAR: institution] — geospatial AI
  2. [PLACEHOLDER_006 reviewer 2] — [LLENAR: institution] — multimodal ML
  3. [PLACEHOLDER_006 reviewer 3] — [LLENAR: institution] — open geospatial data

Non-preferred reviewers (with whom the author has direct professional
collaboration in the past five years): [LLENAR: names, or "None"].

We confirm the manuscript complies with the ACM SIGSPATIAL 2027
template (12 pages + 2 pages references), uses the official ACM Master
Article Template with the SIGCONF proceedings style, and includes a
copyright box on the first page. The paper is original and has not been
published elsewhere.

Thank you for considering this submission. We would be honoured to
present the work at SIGSPATIAL 2027.

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

1. **ACM usa "Precision Conference System"** — la cover letter se pega en un campo "Cover Letter" del sistema. Algunos años ACM pide un archivo `.pdf` separado además.
2. **Copyright box:** las ACM papers llevan un copyright box en la primera página con el texto generado automáticamente por el template ACM. Iván NO edita esto — lo gestiona ACM al aceptar.
3. **Keywords:** SIGSPATIAL pide 3-6 keywords en el portal. Recomendados para este paper:
   - `OpenStreetMap`
   - `Multimodal foundation models`
   - `Semantic annotation`
   - `Low-coverage regions`
   - `Vision-language models`
   - `Crowdsourced geospatial data`
4. **ACM Open:** Iván decide si pagar ACM Open (USD ~600 OA fee) o dejar el paper cerrado. Si Iván elige OA, agregar al final de la cover letter: *"The author elects to publish this paper under ACM Open Access (CC BY 4.0) and assumes the associated APC."*
5. **Si Iván tiene advisor co-autor:** agregar línea "[PLACEHOLDER_005: Co-author name + affiliation]" y cambiar "We"/"our" por "I"/"my" donde corresponda.
6. **Suggested reviewers** van en un campo separado del portal, no solo en la cover letter. Iván duplica.
7. **Diferencia clave con ICA:** SIGSPATIAL papers suelen ser más técnicos (más detalle metodológico) y menos aplicados. Iván enfatiza la pipeline arquitectura + el bias-correction empirical study en lugar del applied case study.
8. **Máximo 1 página.** Esta plantilla es larga para cobertura completa; Iván condensa a 5-6 párrafos.