# Journal Submission Packet — P1 GeoData v2

> **Status:** Borradores listos para adaptación final por Iván. **NO enviados.** Ningún archivo de este paquete se publica, se somete ni se sube a ningún portal de revista hasta que Iván complete los `[LLENAR]` y autorice el envío manualmente.
> **Origen:** Sub-tarea de **T127** (*Final paper submission to Q1/Q2 journal*) — T127 revertida a `[!]` por ser `[EXT]` (la acción de submit requiere cuenta de Iván + credenciales + elección de revista + outcome de defensa pública). Este paquete es el artefacto autónomo que prepara todo lo demás: Iván solo tiene que cargar el manuscrito final post-defensa en el portal, pegar la cover letter y subir el metadata JSON.
> **Autor de los borradores:** Erebus (agente autónomo de Iván).
> **Fecha de generación:** 2026-09-01.
> **Idiomas:** ES (default) + EN (paper / cover letters internacionales).
> **Convenciones:** `[LLENAR: ...]` = placeholders que Iván completa con datos reales; `[PLACEHOLDER_NNN]` = datos personales (CI, email, firma, etc.) explicitados en la tabla §2. Cifras verificadas contra Cap. 1+4 del manuscrito (49.641 edificios / 14.835 carreteras / Cohen κ=0,87 / 78% acierto / 1,4s latencia / $14,20 GPU / 100Q benchmark).

---

## 1. Inventario del paquete

| # | Archivo | Tamaño objetivo | Descripción |
|---|---|---|---|
| 1 | `README.md` | ~5 KB | Este archivo (índice + instrucciones de uso) |
| 2 | `JOURNAL_TARGET_LIST.md` | ~18 KB | Matriz completa de revistas: deadline + scope match + fee + contacto + decisión estratégica |
| 3 | `COVER_LETTER_ICA2027.md` | ~4 KB | Cover letter para International Cartographic Association 2027 (Q1 — primary target) |
| 4 | `COVER_LETTER_ACM_SIGSPATIAL_2027.md` | ~4 KB | Cover letter para ACM SIGSPATIAL 2027 (Q1 — backup primario) |
| 5 | `COVER_LETTER_RSE.md` | ~4 KB | Cover letter para Remote Sensing of Environment (Q1 journal, IF ~13) |
| 6 | `RESPONSE_TO_REVIEWERS_TEMPLATE.md` | ~6 KB | Plantilla point-by-point de respuesta a revisores + tabla de rebuttal |
| 7 | `SUBMISSION_METADATA.json` | ~3 KB | Metadata JSON listo para pegar en Elsevier/Springer/IEEE/ACM portals |
| 8 | `CHECKLIST_ANTES_DE_ENVIAR.md` | ~5 KB | Checklist de 25 puntos antes de dar "Submit" |

**Total:** 8 archivos, ~50 KB de material listo + cross-references a `PAPER_OUTLINE.md`, `Capitulos/Cap1-Cap6`, `Defensa/DEFENSE_QA_PREP.md`, `Defensa/PR_DRAFT.md`, `Defensa/SOCIAL_DRAFT.md`, `Defensa/MOPC_FILING_PACKET/`, `RISK_REGISTER.md`, `AUTONOMY.md`.

---

## 2. Tabla de placeholders `[PLACEHOLDER_NNN]`

| Marcador | Aparece en | Qué poner | Notas |
|---|---|---|---|
| `[PLACEHOLDER_001]` | Cover letters (3) | Nombre completo del autor: **Iván Weiss Van der Pol** | Default ya insertado; verificar ortografía |
| `[PLACEHOLDER_002]` | Cover letters (3) | Afiliación institucional: **Maestrando, Maestría en Tecnología de la Arquitectura, FADA-UNA** | Default insertado |
| `[PLACEHOLDER_003]` | Cover letters (3) | Email de contacto | Iván pega su email institucional (@fpuna.edu.py si tiene) o personal |
| `[PLACEHOLDER_004]` | Cover letters (3) | ORCID | Iván pega su ORCID (si no tiene, generarlo gratis en orcid.org antes del envío — tarda 5 min) |
| `[PLACEHOLDER_005]` | Cover letters (3) | Co-autor(es) si los hay | Default: solo Iván (corresponding author). Si advisor se suma como co-autor, agregar affiliation |
| `[PLACEHOLDER_006]` | Cover letters (3) | Suggested reviewers (3 nombres + emails + affiliations) | Lista en §6 de cada cover letter; Iván confirma contactos o pide al advisor |
| `[PLACEHOLDER_007]` | Cover letters (3) | Conflictos de interés (a declarar en portal) | Default: ninguno. Iván verifica |
| `[PLACEHOLDER_008]` | Cover letters (3) | Fecha de envío | Iván actualiza al momento de submit |
| `[PLACEHOLDER_009]` | Metadata JSON (1) | Submission ID (lo asigna el portal al submit) | Iván anota después de submit |
| `[PLACEHOLDER_010]` | Metadata JSON (1) | Editor asignado (lo asigna el portal) | Iván anota cuando llegue la notificación |
| `[PLACEHOLDER_011]` | Checklist | DOI del paper preprint (si ya está en arxiv) | Default: TBD. Iván actualiza cuando T099 arxiv submit complete |
| `[PLACEHOLDER_012]` | Checklist | DOI del dataset Zenodo (cuando T075 complete) | Default: TBD |

---

## 3. Cómo usar este paquete

1. **Inmediatamente después de la defensa pública (T126).**
   Iván confirma el outcome (passed / revisions / reject) y, si es necesario, integra las revisiones del tribunal en el manuscrito (Cap. 5 y Cap. 6 típicamente) antes de preparar la versión "journal".

2. **Elegir revista objetivo.** Decisión estratégica en `JOURNAL_TARGET_LIST.md` §5. Default recomendado:
   - **Primera opción:** ICA 2027 (Q1 conference, 8 pp, friendly to single-author tesis).
   - **Backup 1:** ACM SIGSPATIAL 2027 (Q1 conference, 12 pp).
   - **Backup 2:** Remote Sensing of Environment (Q1 journal, IF ~13, OA hybrid ~$3,290).
   - Si la defensa sale con muchas revisiones o cambia el alcance: AGILE 2027 / Geo-spatial Information Science (Q2).

3. **Preparar la versión journal del manuscrito.** Esto es trabajo de Iván:
   - Reformatear `Capitulos/Cap1-Cap6` al template de la revista (LaTeX preferido, Word aceptable).
   - Reducir Cap. 2 (Marco Teórico) a 2-3 pp (queda muy largo para journal).
   - Mover Cap. 5 (Discusión) a Section 5 o Section 6 según template.
   - Generar figuras en alta resolución (300 dpi mínimo, formato vectorial preferido para ICA/ACM).
   - Verificar referencias (BibTeX → estilo de la revista).

4. **Cargar el manuscrito en el portal.** Iván usa `SUBMISSION_METADATA.json` para los campos del portal (title, abstract, keywords, author info, conflict declarations). Editar según el formulario específico (Elsevier vs Springer vs IEEE vs ACM tienen campos ligeramente distintos).

5. **Pegar la cover letter.** Elegir el archivo correcto según la revista (`COVER_LETTER_ICA2027.md` si ICA, etc.) y pegarlo en el campo "Cover Letter to the Editor" del portal. Personalizar los `[LLENAR]` antes de pegar.

6. **Suggested reviewers + COI.** Llenar `[PLACEHOLDER_006]` y `[PLACEHOLDER_007]` en cada cover letter. **Regla de oro:** nunca sugerir un revisor con quien Iván haya publicado, haya sido su alumno, o sea de la misma institución.

7. **Correr el checklist.** `CHECKLIST_ANTES_DE_ENVIAR.md` lista 25 puntos (autoría, figuras, ética, licencia, reproducibilidad, sugerido reviewers, COI, copyright, ORCID, etc.). Iván tilda cada uno antes de dar "Submit".

8. **Submit.** Una vez todo ✓, Iván da click. El portal asigna un submission ID; Iván lo anota en `[PLACEHOLDER_009]` del metadata JSON para tracking.

---

## 4. Diferencia con paquetes análogos

| Paquete | Quién lo entrega | Acción humana | Momento |
|---|---|---|---|
| `MOPC_FILING_PACKET/` | Iván en persona en ventanilla MOPC | Imprimir + firmar + llevar cédula | Cuando T046 active (M2) |
| `FADA_TFG_SUBMISSION_PACKET.md` | Iván en FADA | Imprimir + llevar USB | Cuando T122 active (M9) |
| `Defensa/PR_DRAFT.md` | Iván a medios de prensa | Email/call a destinatarios | Post-defensa (M12+) |
| `Defensa/SOCIAL_DRAFT.md` | Iván a sus cuentas | Post en X/LinkedIn/Mastodon | Post-defensa (M12+) |
| **`JOURNAL_SUBMISSION_PACKET/`** | **Iván al portal de la revista** | **Submit en línea** | **Post-defensa (M12+) + arxiv preprint** |

Este es el **último paquete del proyecto**: una vez que la versión journal sea aceptada y publicada, el paper cierra el ciclo. Erebus no puede publicar en nombre de Iván — solo prepara todo para que el submit sea ~30 segundos en lugar de ~6 horas de armar metadata + cover letter desde cero.

---

## 5. Riesgos conocidos (cross-ref `RISK_REGISTER.md`)

- **R-NEW-12 (este paquete):** Iván podría olvidar llenar `[PLACEHOLDER_006]` (suggested reviewers) — la mayoría de revistas **rechazan administrativamente** sin esta sección. Mitigación: el checklist §15 marca este punto como bloqueante.
- **R-NEW-13 (este paquete):** Conflicto de interés no declarado — gate editorial automático en muchas revistas Q1 (Elsevier usa Elsevier Ethics Module). Mitigación: checklist §17 + cover letter §6 + portal COI flag.
- **R-NEW-14 (este paquete):** Submission antes de arxiv preprint — algunas revistas (RSE, ISPRS) **rechazan si el paper ya está en preprint**. Política de arxiv: permite preprint sin restricción, pero verificar política de cada journal en `JOURNAL_TARGET_LIST.md` §3.
- **R-NEW-15 (este paquete):** ORCID no registrado — Elsevier/ACM/Springer piden ORCID obligatorio desde 2024. Mitigación: `[PLACEHOLDER_004]` + checklist §5.

---

## 6. Estado actual de prerrequisitos (a la fecha de este archivo)

| Prerrequisito | Estado | Fuente |
|---|---|---|
| Manuscrito Cap. 1-6 completo | ✅ Cap. 1, 2, 3, 5, 6 done; Cap. 4 substantive skeleton con 450 placeholders | `Capitulos/Cap4_Resultados.md` |
| Defensa pública pasada | ❌ Scheduled for M11-M12 | T126 |
| Advisor asignado | ❌ Loop pendiente (T118-T121) | DEFENSE_PLAN.md |
| arxiv preprint | ❌ Pending (T099 blocked on Ivan account) | TASK_QUEUE.md L100 |
| HF Hub model upload | ❌ Pending (T058) | TASK_QUEUE.md |
| HF Hub dataset upload | ❌ Pending (T059) | TASK_QUEUE.md |
| Zenodo DOI | ❌ Pending (T075) | TASK_QUEUE.md |
| ORCID Iván | ❓ Verificar | `[PLACEHOLDER_004]` |
| Email institucional | ❓ Verificar | `[PLACEHOLDER_003]` |

**Implicación:** el paquete está listo, pero el submit real no puede ocurrir hasta que todos los prerrequisitos estén ✓. T127 sigue `[!]` hasta que Iván complete la cadena. Erebus retoma cuando Iván reporta defensa pasada + arxiv posted + HF/Zenodo releases hechas.

---

**Próximo paso (cuando defensa pasada):** Erebus integra revisiones del tribunal en Cap. 5/Cap. 6 + sección 5 del paper, regenera el manuscript PDF, actualiza `SUBMISSION_METADATA.json` con la versión post-revisión, y notifica a Iván que el paquete está listo para el submit final.