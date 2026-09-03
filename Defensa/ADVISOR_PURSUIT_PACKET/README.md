# ADVISOR_PURSUIT_PACKET — T118-T121 (split from M8 advisor-email loop)

**Author:** Iván Weiss Van der Pol
**Created:** 2026-09-01 (Erebus thesis-tracker-daily tick)
**Trigger:** when Iván está listo para Fase 1 (DEFENSE_PLAN.md): paper en arxiv + dataset HF + código GH + manuscrito UNA completo.
**Status:** substrate completo; ejecución (envío real de emails) sigue siendo acción de Iván.

---

## 1. ¿Qué es este paquete?

Es el **documento entregable** que Iván usa para ejecutar la Fase 1 del DEFENSE_PLAN.md: contactar hasta 6 advisors hasta que uno acepte la co-firma sobre trabajo terminado.

**Incluye:**
- 6 emails personalizados (uno por advisor en la lista corta), cada uno con: hook de investigación específico, referencia a trabajos previos del advisor, framing de co-autoría ajustado a la facultad, llamada a la acción concreta.
- Plan de cadencia de seguimiento (Day 3 / Day 7 / Day 14 / Day 30) — 4 follow-ups por advisor.
- Plan de pivote por declinación (qué enviar al siguiente advisor si el actual dice no).
- Paquete de hand-off post-aceptación (qué envía Iván al advisor cuando dice sí).
- Checklist de 50 ítems en 6 gates para no enviar emails con datos faltantes o formato incorrecto.

**No incluye (y por qué):**
- ❌ Envío real de emails — Iván los envía (regla AUTONOMY.md #5: "NO emails to real people").
- ❌ Cuentas de email institucionales — Iván abre su propio correo desde UNA-FADA o su proveedor personal.
- ❌ Datos personales del advisor (cédulas, teléfonos, emails directos) — todos los placeholders son `[PLACEHOLDER_NNN]`; Iván busca en OPAC/Google Scholar y llena.
- ❌ Submission a ningún portal — no aplica aquí; el portal es el cliente de correo de Iván.

---

## 2. Tabla de placeholders

| ID | Tipo | Uso | Aparece en |
|---|---|---|---|
| `[PLACEHOLDER_001]` | nombre del advisor | saludo formal | EMAIL_01..06 |
| `[PLACEHOLDER_002]` | título académico (Dr./Mg./Ing./Prof.) | saludo | EMAIL_01..06 |
| `[PLACEHOLDER_003]` | email del advisor | campo `Para:` | EMAIL_01..06 |
| `[PLACEHOLDER_004]` | referencia a trabajo previo del advisor | párrafo 2 (hook) | EMAIL_01..06 |
| `[PLACEHOLDER_005]` | facultad/departamento del advisor | encabezado | EMAIL_01..06 |
| `[PLACEHOLDER_006]` | URL arxiv del paper | firma | EMAIL_01..06 |
| `[PLACEHOLDER_007]` | URL Hugging Face dataset | firma | EMAIL_01..06 |
| `[PLACEHOLDER_008]` | URL Hugging Face modelo | firma | EMAIL_01..06 |
| `[PLACEHOLDER_009]` | URL GitHub repo | firma | EMAIL_01..06 |
| `[PLACEHOLDER_010]` | ORCID de Iván | firma | EMAIL_01..06 |
| `[PLACEHOLDER_011]` | teléfono de Iván | pie | EMAIL_01..06 |
| `[PLACEHOLDER_012]` | cédula de Iván (solo Cristaldo para MOPC) | anexo | EMAIL_01 (si Cristaldo) |
| `[PLACEHOLDER_013]` | fecha tentativa de defensa | cuerpo | FOLLOWUP_CADENCE + SUCCESS_HANDOFF |
| `[PLACEHOLDER_014]` | semestre de inscripción | cuerpo | SUCCESS_HANDOFF |
| `[PLACEHOLDER_015]` | horario disponible para reunión | cuerpo | SUCCESS_HANDOFF |
| `[PLACEHOLDER_016]` | nombre del comité TFG-FADA (si Iván lo conoce) | cuerpo | SUCCESS_HANDOFF |
| `[PLACEHOLDER_017]` | número de tesis previas del advisor (en su línea) | cuerpo | EMAIL_01..06 |
| `[PLACEHOLDER_018]` | título exacto del paper | cuerpo | EMAIL_01..06 |
| `[PLACEHOLDER_019]` | abstract corto (1-2 frases) del paper | cuerpo | EMAIL_01..06 |
| `[PLACEHOLDER_020]` | nombre del dataset | cuerpo | EMAIL_01..06 |

**Total:** 20 placeholders. Todos se llenan con datos que Iván ya tiene o busca en 5 minutos (OPAC, arxiv, Google Scholar).

---

## 3. Instrucciones de uso (5 pasos)

### Paso 1 — Verificar Fase 1 triggers (15 min)
Antes de abrir CUALQUIER email, correr el checklist del DEFENSE_PLAN.md §"Checkpoint criteria para Fase 1":
- [ ] Paper en arxiv con DOI
- [ ] Dataset en HF Hub con DOI
- [ ] Modelo en HF Hub
- [ ] Código en GH con LICENSE + README + tests
- [ ] Manuscrito completo en formato UNA (6 capítulos)
- [ ] Al menos 1 presentación interna ensayada con cronómetro (usar `make rehearse`)

Si falta alguno: NO enviar emails. Seguir construyendo. La estrategia paper-first es lo que hace que el advisor firme.

### Paso 2 — Llenar placeholders por advisor (30 min para los 6)
Por cada advisor en orden (1→6):
1. Buscar email institucional en directorio FP-UNA (`https://www.pol.una.py/directorio/`) o FADA (`https://www.arquitectura.una.py/docentes/`). Si no aparece, LinkedIn o ResearchGate.
2. Buscar 1-2 papers recientes del advisor en Google Scholar para citarlos en el párrafo 2 (hook).
3. Llenar placeholders 001-005 + 017 (datos básicos del advisor).
4. Llenar placeholders 006-012 (datos de Iván que ya tiene en `Capitulos/FADA_TFG_SUBMISSION_PACKET.md`).

### Paso 3 — Personalizar el campo "asunto" (5 min)
Cada email tiene un asunto genérico. Iván puede ajustarlo si quiere (ej. agregar el nombre del advisor o un detalle específico). NO obligatorio.

### Paso 4 — Enviar email #1 y registrar (10 min)
1. Enviar `EMAIL_01_cristaldo.md` desde el correo de Iván.
2. Anotar fecha/hora de envío en `Defensa/qa_log.md` (nueva sección "Advisor pursuit").
3. Iniciar timer de cadencia (ver `FOLLOWUP_CADENCE.md`).

### Paso 5 — Esperar respuesta o pivote
- Si responde en 14 días: usar `SUCCESS_HANDOFF_PACKET.md` (siguiente paso = co-firma).
- Si no responde en 14 días: enviar `FOLLOWUP_CADENCE.md` Day 14.
- Si declina: ir a `EMAIL_02_legal_ayala.md` + `DECLINE_PIVOT_PLAN.md`.

**Costo total estimado de la fase:** 1 hora de búsqueda + 1 hora de personalización + 30 minutos de envío + 14 días de espera. Si el advisor #1 acepta, la fase termina. Si no, el ciclo se repite para #2 → #3 → ... → #6 con cadencia.

---

## 4. Diferencia con otros paquetes

| Paquete | Familia | Cuándo se usa | Quién ejecuta |
|---|---|---|---|
| `MOPC_FILING_PACKET/` | institutional filing | Iván lleva documentos al Ministerio de Obras Públicas | Iván imprime + camina a MOPC |
| `FADA_TFG_SUBMISSION_PACKET.md` | institutional submission | Iván lleva tema de tesis al comité TFG-FADA | Iván imprime + camina a FADA |
| `PR_DRAFT.md` | press release | Iván envía a paraguaytech.com.py / MITIC press | Iván envía desde su correo |
| `SOCIAL_DRAFT.md` | social media | Iván postea en red social X / red profesional LinkedIn | Iván postea desde su cuenta |
| `JOURNAL_SUBMISSION_PACKET/` | journal submission | Iván pega metadata + cover letter en portal de revista | Iván pega en portal Open Journal Systems |
| **`ADVISOR_PURSUIT_PACKET/` (este)** | **advisor email loop** | **Iván envía 1-6 emails + sigue cadencia hasta que uno acepte** | **Iván envía desde su correo** |

Este paquete es el más interactivo de todos: requiere decisión humana (a quién contactar primero, cuándo pivotear), búsqueda de datos del advisor (no incluidos aquí), y manejo de respuesta (acepta/declina/ignora). Los demás paquetes son más "fire-and-forget": se imprime/envía/postea y listo.

---

## 5. Riesgos nuevos

| ID | Riesgo | Mitigación |
|---|---|---|
| R-NEW-16 | Iván envía email a dirección incorrecta y no llega | Verificar email institucional en 2 fuentes (directorio FP-UNA + LinkedIn/Scholar) antes de enviar |
| R-NEW-17 | Advisor responde con condiciones inaceptables (ej. "te firmo pero quiero reescribir Cap. 4") | Definir antes de enviar qué condiciones son aceptables vs deal-breakers (ver SUCCESS_HANDOFF_PACKET §"Condiciones negociables") |
| R-NEW-18 | Iván contacta advisor #2 sin esperar respuesta de #1 y queda mal | Política de espera: 14 días para respuesta + 7 días para follow-up antes de pivotear (ver FOLLOWUP_CADENCE §"Pivot timing") |
| R-NEW-19 | Advisor acepta pero FADA no reconoce su firma (ej. advisor externo sin convenio) | Verificar antes de enviar que advisor pertenece a FADA-FP-UNA o tiene convenio vigente (ver ADVISOR_SHORTLIST_TABLE §"Filiación institucional") |
| R-NEW-20 | Iván envía emails a los 6 y todos declinan → no hay director | Plan B documentado en DECLINE_PIVOT_PLAN §"Plan B: director externo por convenio" |

---

## 6. Prerrequisitos (estado al 2026-09-01)

- ✅ DEFENSE_PLAN.md existe con lista de 6 advisors
- ✅ DEFENSE_PLAN.md tiene plantilla genérica de email
- ✅ Defensa/PR_DRAFT.md existe (referencia a FADA + Cristaldo)
- ✅ Defensa/SOCIAL_DRAFT.md existe
- ✅ Defensa/MOPC_FILING_PACKET/ existe (6 archivos)
- ✅ Defensa/JOURNAL_SUBMISSION_PACKET/ existe (8 archivos)
- ✅ Defensa/slides.html existe (21 slides, 22KB)
- ✅ Defensa/DEFENSE_QA_PREP.md existe (30+ preguntas anticipadas)
- ❌ Paper en arxiv — pendiente (T099 bloqueado en credenciales de Iván)
- ❌ Dataset en HF Hub — pendiente (T075 bloqueado en credenciales de Iván)
- ❌ Modelo en HF Hub — pendiente (mismo)
- ❌ Defensa scheduling — pendiente (T125 bloqueado en T122-T124)
- ❌ Code freeze en GH — pendiente (commits locales sí, remote push no)

**Substrate listo al 100%. Solo falta ejecución humana.**

---

## 7. Archivos del paquete

1. `README.md` (este) — índice
2. `ADVISOR_SHORTLIST_TABLE.md` — tabla de los 6 advisors con probabilidad + facultad + área + hook + framing
3. `EMAIL_01_cristaldo.md` — FADA cartografía, prioridad ALTA, primer contacto
4. `EMAIL_02_legal_ayala.md` — FP-UNA CV/image processing, prioridad MEDIA-ALTA, segundo contacto
5. `EMAIL_03_von_lucken.md` — FP-UNA NLP/MOEA, prioridad MEDIA, tercer contacto
6. `EMAIL_04_stalder.md` — FP-UNA DL forecasting, prioridad MEDIA, cuarto contacto
7. `EMAIL_05_yegros.md` — FP-UNA biomedical, prioridad BAJA-MEDIA, quinto contacto
8. `EMAIL_06_pane.md` — FP-UNA NLP sentiment, prioridad BAJA, sexto contacto (alternativa)
9. `FOLLOWUP_CADENCE.md` — cadencia Day 3/7/14/30 + pivot timing
10. `DECLINE_PIVOT_PLAN.md` — qué enviar al siguiente advisor + Plan B
11. `SUCCESS_HANDOFF_PACKET.md` — qué enviar al advisor que acepta + condiciones negociables
12. `CHECKLIST_ANTES_DE_ENVIAR.md` — 50 ítems / 6 gates

**Total:** 12 archivos.

---

**Próximo paso de Iván:** verificar Fase 1 triggers (DEFENSE_PLAN.md §Checkpoint), llenar placeholders 001-012 para los 6 advisors, enviar email #1.
