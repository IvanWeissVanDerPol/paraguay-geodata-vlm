# Checklist Antes de Enviar — Submission a Revista/Conferencia

> **Cuándo usar:** justo antes de dar "Submit" en el portal de la revista/conferencia. Iván tilda cada item; cualquier item sin tildar bloquea el submit.
> **Origen:** Sub-tarea de T127 (Final paper submission to Q1/Q2 journal).
> **Cross-references:** `JOURNAL_TARGET_LIST.md`, `SUBMISSION_METADATA.json`, `COVER_LETTER_*.md`, `RESPONSE_TO_REVIEWERS_TEMPLATE.md`, `AUTONOMY.md`, `RISK_REGISTER.md`.

---

## A. Autoría y afiliaciones (gate 1)

- [ ] **A1.** Nombre completo del autor verificado: "Iván Weiss Van der Pol" (sin typos, acentos correctos).
- [ ] **A2.** Afiliación institucional completa: FADA-UNA, Asunción, Paraguay.
- [ ] **A3.** Email de contacto institucional o personal vigente (verificar que Iván lo revisa — el portal envía notificaciones críticas a este email por 3-6 meses).
- [ ] **A4.** ORCID registrado y verificado en orcid.org. (Si Iván no tiene, generarlo AHORA — tarda 5 min, evita desk-reject en Elsevier/ACM/Springer.)
- [ ] **A5.** Co-autores (si los hay) confirmados y agregados con sus ORCIDs.
- [ ] **A6.** Corresponding author flag correctamente asignado a Iván.

## B. Manuscrito y formato (gate 2)

- [ ] **B1.** Manuscript en el template oficial de la revista (LaTeX preferido, Word aceptable).
- [ ] **B2.** Page limit respetado: 8 pp (ICA) / 12 pp (SIGSPATIAL) / variable (journals Q1).
- [ ] **B3.** Título en inglés correcto, sin caracteres especiales problemáticos (e.g., acentos → verificar que el PDF renderiza).
- [ ] **B4.** Abstract ≤ 250 palabras (ICA pide ≤ 200) — verificar límite específico.
- [ ] **B5.** Keywords en el formato del portal (algunos piden 3-5, otros 5-8).
- [ ] **B6.** Figuras en alta resolución: 300 dpi mínimo, formato vectorial (PDF/SVG) preferido para ICA/ACM.
- [ ] **B7.** Captions de figuras auto-contenidas (cada caption explica la figura sin requerir texto principal).
- [ ] **B8.** Tablas en formato editable (no imágenes), con captions arriba.
- [ ] **B9.** Referencias en el estilo de la revista (BibTeX .bst específico o Word style).
- [ ] **B10.** DOI URLs en referencias (no links rotos).
- [ ] **B11.** PDF compilado final revisado (sin warnings de LaTeX/Word, sin "[PLACEHOLDER]" o "[LLENAR]" residuales).
- [ ] **B12.** Páginas numeradas, copyright box presente (ACM), copyright transfer agreement firmado (Elsevier/Springer).

## C. Cover letter (gate 3)

- [ ] **C1.** Cover letter escrita siguiendo `COVER_LETTER_<TARGET>.md` como base.
- [ ] **C2.** Todos los `[LLENAR]` y `[PLACEHOLDER_NNN]` reemplazados con datos reales.
- [ ] **C3.** Co-autores listados (si aplica) con afiliaciones correctas.
- [ ] **C4.** Suggested reviewers (3 nombres + emails + afiliaciones) copiados al campo separado del portal, no solo en la cover letter.
- [ ] **C5.** Non-preferred reviewers (si los hay) declarados con razón válida.
- [ ] **C6.** Cover letter ≤ 1 página (algunos portals limitan caracteres).
- [ ] **C7.** Sin errores ortográficos o gramaticales — Iván lee en voz alta para verificar.

## D. Conflictos de interés (gate 4)

- [ ] **D1.** Módulo COI del portal completado (Elsevier Ethics Module / ACM COI form).
- [ ] **D2.** Conflictos financieros declarados (si Iván recibió funding de alguna organización que pueda tener interés en el paper — generalmente no).
- [ ] **D3.** Conflictos personales declarados (e.g., Iván es reviewer de la misma revista → declararlo).
- [ ] **D4.** Conflictos institucionales declarados (e.g., FADA-UNA tiene convenio con la revista → declararlo).
- [ ] **D5.** Suggested reviewers verificados contra lista de co-autores previos + colegas FADA — ninguno debe ser conflict.

## E. Datos y reproducibilidad (gate 5)

- [ ] **E1.** Code repository público en GitHub con DOI Zenodo.
- [ ] **E2.** Dataset público en Hugging Face Hub con DOI Zenodo.
- [ ] **E3.** Model weights públicos en Hugging Face Hub.
- [ ] **E4.** License file (LICENSE) en repo de código.
- [ ] **E5.** Citation file (CITATION.cff) en repo de código.
- [ ] **E6.** Model card (modelcard.md) en Hugging Face Hub.
- [ ] **E7.** README del repo completo (instalación + uso + ejemplos).
- [ ] **E8.** Random seeds documentados en el paper + repo.
- [ ] **E9.** Hardware / OS / Python versions pinned (e.g., `requirements.txt` con versiones exactas).
- [ ] **E10.** Docker bundle (si existe) tested fresh en una máquina limpia por Iván o un colega.
- [ ] **E11.** Supplementary archive con scripts de análisis + datos intermedios subido a Zenodo.
- [ ] **E12.** Preprint en arXiv (si ya está subido — `[PLACEHOLDER_011]`).

## F. Ética y compliance (gate 6)

- [ ] **F1.** ETHICS_WAIVER_MEMO.md subido como supplementary.
- [ ] **F2.** Si hay datos de comunidades indígenas: declaración FPIC en el paper.
- [ ] **F3.** Si hay datos personales: GDPR / Ley 6538/2020 Paraguay compliance verificada.
- [ ] **F4.** Si hay datos de menores: explícitamente excluidos.
- [ ] **F5.** Si hay imágenes de terceros: permisos de uso documentados.

## G. Decisión de financiamiento (gate 7 — REVISAR CON CUIDADO)

- [ ] **G1.** Si la revista tiene APC (Elsevier journals): Iván confirmó opción (subscription vs OA).
- [ ] **G2.** Si eligió OA: Iván confirmó OK explícito de pago (AUTONOMY.md rule #4). **Sin este OK, NO submit.**
- [ ] **G3.** Registro del APC en `THESIS_COST_BREAKDOWN.md` cuando se haga el cargo.
- [ ] **G4.** Si la conferencia tiene registration fee: Iván tiene presupuesto (USD 400-1,200).

## H. Pre-submit sanity check final (gate 8)

- [ ] **H1.** Iván lee TODO el manuscrit + cover letter una última vez. (Lectura crítica, no skim.)
- [ ] **H2.** Iván lee TODAS las figuras + tablas + verificar que cada número del texto coincide con la tabla/figura correspondiente.
- [ ] **H3.** Iván relee abstract — ¿representa fielmente el contenido del paper?
- [ ] **H4.** Iván verifica que las referencias citadas en el texto están TODAS en la lista de referencias.
- [ ] **H5.** Iván verifica que NO hay referencias en la lista que no se citen en el texto.
- [ ] **H6.** Iván verifica formato de fechas, números, unidades (español vs inglés según revista).
- [ ] **H7.** Iván verifica acknowledgments — todas las personas/organizaciones que ayudaron están mencionadas.
- [ ] **H8.** Iván abre el PDF final en 3 lectores diferentes (Adobe Acrobat, browser, mobile) — verifica que se ve bien en todos.
- [ ] **H9.** Iván verifica que el PDF pesa < 50 MB (límite común de portales).
- [ ] **H10.** Iván confirma que el sistema de submission está abierto (algunos cierran 1-2 horas antes del deadline).
- [ ] **H11.** Iván tiene un backup local del manuscrit + cover letter + metadata ANTES de submit.
- [ ] **H12.** Iván confirma que la decisión de defensa (T126) ya está integrada en el manuscrit (revisiones del tribunal reflejadas en Cap. 5/Cap. 6).

## I. Post-submit (gate 9 — para después, no bloquea)

- [ ] **I1.** Anotar Submission ID en `[PLACEHOLDER_009]` de `SUBMISSION_METADATA.json`.
- [ ] **I2.** Anotar fecha de submit en `[PLACEHOLDER_008]`.
- [ ] **I3.** Configurar recordatorio en calendario para el expected decision date (típicamente +3 meses).
- [ ] **I4.** Notificar al advisor (cuando lo haya) que el paper está submitted.
- [ ] **I5.** Si aceptan: notificar a FADA-UNA + actualizar Cap. 6 con la publicación.
- [ ] **I6.** Si piden revisions: usar `RESPONSE_TO_REVIEWERS_TEMPLATE.md` como base.
- [ ] **I7.** Si rechazan: evaluar contrapropuesta de otra revista del `JOURNAL_TARGET_LIST.md`.

---

## Resumen visual

| Gate | Items | Bloquea submit? |
|---|---|---|
| A. Autoría | A1-A6 (6 items) | ✅ Sí |
| B. Manuscrito | B1-B12 (12 items) | ✅ Sí |
| C. Cover letter | C1-C7 (7 items) | ✅ Sí |
| D. COI | D1-D5 (5 items) | ✅ Sí |
| E. Datos + reproducibilidad | E1-E12 (12 items) | ✅ Sí (recomendado) |
| F. Ética | F1-F5 (5 items) | ✅ Sí |
| G. Financiamiento | G1-G4 (4 items) | ✅ Sí (especialmente G2) |
| H. Pre-submit sanity | H1-H12 (12 items) | ✅ Sí |
| I. Post-submit | I1-I7 (7 items) | ❌ No (post) |

**Total: 70 items, 63 bloqueantes + 7 post-submit.**

---

## Notas finales

- **Tiempo estimado para completar todos los gates:** ~3-4 horas si Iván tiene el manuscrit listo, ~2-3 días si tiene que formatear el manuscrito al estilo de la revista.
- **Re-running this checklist** después de un reject + resubmit: solo Gate C, D, I cambian.
- **Si Iván quiere ver el checklist automatizado:** este markdown se puede convertir a un script Python que Iván corre localmente y le pregunta item por item. Erebus no genera ese script sin pedido explícito (no está en TASK_QUEUE.md).

**Recordatorio crítico:** este checklist es la última línea de defensa antes del submit. Iván NO se apura. Si un item no se puede tildar, **mejor esperar 1 semana y arreglarlo** que submitear con un item pendiente. Los journals hacen desk-reject por detalles pequeños (formato, COI no declarado, ethics memo faltante) que Iván puede prevenir.