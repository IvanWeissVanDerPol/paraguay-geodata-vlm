# ADVISOR SHORTLIST TABLE — 6 candidatos × 7 columnas

**Fecha:** 2026-09-01
**Trigger:** usar esta tabla para decidir a quién contactar primero y cómo personalizar el email.
**Source:** `DEFENSE_PLAN.md` §"Lista de advisors candidatos" + Google Scholar verification pendiente (Iván).

---

## Tabla principal

| # | Advisor | Facultad | Área de investigación | Hook para este trabajo | Co-authorship framing | Probabilidad | Email (a buscar) |
|---|---|---|---|---|---|---|---|
| 1 | **Juan Carlos Cristaldo** | FADA-UNA | Cartografía abierta + mapeo participativo (4 tesis previas: 2019, 2019, 2021, 2023) | Este trabajo ES la 5ta tesis de su línea + primera que incorpora IA multimodal | "Co-autor en la versión final del paper + director de tesis en FADA-UNA; usted ya tiene 4 tesis en la línea, esta sería la primera con componente IA" | **ALTA** | `[PLACEHOLDER_003_cristaldo]` |
| 2 | **Horacio Legal Ayala** | FP-UNA | Computer vision + image processing | Trabajo tiene componente CV fuerte (Florence-2, SAM, CLIP sobre tiles Sentinel-2 + IGN WMS) | "Co-autor secundario en el paper (CV methods section); director de tesis o co-director en FP-UNA Ing. Informática" | **MEDIA-ALTA** | `[PLACEHOLDER_003_legal_ayala]` |
| 3 | **Christian Von Lücken** | FP-UNA | NLP + MOEA (multi-objective evolutionary algorithms) | El paper tiene interfaz conversacional en español/jopara (Cap. 5 §136) + 60% de las preguntas benchmark son en jopara | "Co-autor en el paper (conversational interface section); director o co-director en FP-UNA" | **MEDIA** | `[PLACEHOLDER_003_von_lucken]` |
| 4 | **Diego Stalder** | FP-UNA | Deep learning forecasting | El fine-tune de Florence-2 sobre el corpus paraguayo es exactamente forecasting sobre datos tabulares + visuales (Cap. 4 §4.4) | "Co-autor en el paper (fine-tuning section); director o co-director en FP-UNA" | **MEDIA** | `[PLACEHOLDER_003_stalder]` |
| 5 | **César Yegros** | FP-UNA | Biomedical engineering | Hook marginal — solo si Iván extiende con componente de voz (STT/TTS en jopara); actualmente NO en el paper | "Co-autor conditional en extension paper (voice component); co-director si la línea se expande" | **BAJA-MEDIA** | `[PLACEHOLDER_003_yegros]` |
| 6 | **Juan Pane** | FP-UNA | NLP sentiment analysis | Hook alternativo — solo si Iván pivota el paper a análisis de sentimiento sobre topónimos indígenas (no es el caso actual) | "Co-autor conditional en pivot paper; P3 alternative" | **BAJA** | `[PLACEHOLDER_003_pane]` |

---

## Columnas explicadas

### Hook para este trabajo
Por qué este advisor en particular podría firmar. Cada uno viene de un ángulo diferente:
- Cristaldo: extensión directa de su línea (más fuerte)
- Legal Ayala: componente técnico específico (CV)
- Von Lücken: componente técnico específico (NLP/conversacional)
- Stalder: componente técnico específico (DL/fine-tune)
- Yegros: componente conditional (voz, no está en el paper actual)
- Pane: pivote alternativo (sentimiento, no es el paper actual)

### Co-authorship framing
Cómo ofrecer la co-autoría. NO es lo mismo ofrecer "lead author with co-authorship" (caso Cristaldo, donde Iván ya hizo todo el trabajo) que "joint equality" (caso Von Lücken, donde el componente NLP es suficientemente grande para joint).

**Regla general:**
- Si el advisor es el "primary hook" (su línea se extiende directamente) → lead author + co-authorship en acknowledgments.
- Si el advisor es un "secondary specialist" (su componente es 1 sección del paper) → co-authorship con sección destacada.
- Si el advisor es un "pivot alternative" (no es el paper actual) → conditional co-authorship en paper futuro.

### Probabilidad
Estimación basada en:
- Cercanía temática (¿el trabajo es su línea?)
- Historial de firma de tesis previas (¿ha firmado 4+ tesis en su línea?)
- Disponibilidad típica (¿está overloaded o acepta nuevos tesistas?)
- Compatibilidad institucional (FADA vs FP-UNA)

**Probabilidad NO es probabilidad de que el advisor acepte; es probabilidad de que acepte DADO que el paper está terminado.** Si el paper NO está terminado, probabilidad cae a ~0% para todos.

---

## Orden de contacto (defendido)

**1 → 2 → 3 → 4 → 5 → 6.** Razón:

1. **Cristaldo primero** porque:
   - Es la línea directa (4 tesis previas sobre el mismo tema). El trabajo encaja PERFECTAMENTE.
   - Está en FADA-UNA (la facultad donde Iván quiere hacer la maestría, según FADA_TFG_SUBMISSION_PACKET.md).
   - Si acepta, FADA_TFG_SUBMISSION_PACKET.md ya tiene su nombre como director de record → cero retrabajo.

2. **Legal Ayala segundo** porque:
   - Componente CV es el segundo más fuerte después de cartografía.
   - Está en FP-UNA (compatible con Ing. Informática si Iván pivota de FADA a FP-UNA).
   - Si Cristaldo declina, Legal Ayala es el segundo más probable.

3. **Von Lücken tercero** porque:
   - Componente NLP/conversacional es el tercero.
   - Si Legal Ayala declina, Von Lücken cubre el ángulo NLP/jopara que es único de este paper.
   - Compatible con FP-UNA.

4. **Stalder cuarto** porque:
   - Componente DL/fine-tune es el cuarto.
   - Si Von Lücken declina, Stalder cubre el ángulo fine-tune.
   - Compatible con FP-UNA.

5. **Yegros quinto** porque:
   - Hook marginal (voz, no en el paper actual).
   - Solo si Iván decide extender el paper con componente de voz.
   - **NO enviar hasta que Iván decida si la extensión de voz es parte del scope.**

6. **Pane sexto** porque:
   - Pivote alternativo (sentimiento, no es el paper).
   - Solo si Iván decide pivotar el paper completo a análisis de sentimiento (no es el plan actual).
   - **NO enviar hasta que Iván decida si el pivote es parte del scope.**

---

## Política de pivote

- **Esperar 14 días** por respuesta del advisor actual antes de enviar follow-up.
- **Esperar 7 días más** después del follow-up antes de pivotear al siguiente.
- **Total por advisor:** 21 días (3 semanas) antes de mover al siguiente.
- **Si los 6 advisors decline:** activar Plan B (ver `DECLINE_PIVOT_PLAN.md` §"Plan B: director externo por convenio").

---

## Datos que Iván debe verificar antes de enviar (para cada advisor)

1. **Email institucional actual** — buscar en directorio oficial; puede haber cambiado desde el último contacto.
2. **Disponibilidad reciente** — LinkedIn / Google Scholar / último paper (¿está overloaded?).
3. **Cambio de filiación** — ¿sigue en FADA/FP-UNA? (algunos advisors se jubilaron o cambiaron de universidad).
4. **Papers recientes para citar** — buscar 1-2 papers 2024-2026 para el párrafo 2 (hook).
5. **Tesis previas dirigidas** — verificar el número (ej. Cristaldo=4 según DEFENSE_PLAN.md, pero ¿sigue siendo exacto?).

**Tiempo de búsqueda por advisor:** ~10 minutos (LinkedIn + Scholar + directorio).

---

## Cross-refs

- `DEFENSE_PLAN.md` §"Lista de advisors candidatos" — fuente de esta tabla
- `EMAIL_01..06_*.md` — los emails individuales derivados de esta tabla
- `FOLLOWUP_CADENCE.md` — timing de seguimiento
- `DECLINE_PIVOT_PLAN.md` — qué hacer si todos decline
- `SUCCESS_HANDOFF_PACKET.md` — qué hacer si alguno acepta
- `Capitulos/FADA_TFG_SUBMISSION_PACKET.md` — packet paralelo (Cristaldo como director de record)
- `Defensa/MOPC_FILING_PACKET/ANEXO_TECNICO.md` — Cristaldo ya mencionado como director (consistencia)
