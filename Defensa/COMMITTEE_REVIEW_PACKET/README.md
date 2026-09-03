# COMMITTEE REVIEW PACKET — Paquete de auto-auditoría pre-comité

**Tesis:** Anotación semiautomática del corpus cartográfico abierto de Paraguay con modelos multimodales fundacionales y una interfaz conversacional para la reflexión territorial

**Autor:** Iván Weiss Van der Pol

**Origen:** Split de **T124** `[P0][M10][NO-GPU][D] Thesis committee review + revisions` (estado: `[!]` upstream-bloqueado en acción institucional del comité FADA).

**Fecha del paquete:** 2026-09-02

---

## §1 — Alcance del paquete

El comité FADA-FP-UNA revisará el manuscrito UNA-FADA (Cap. 1–6 + anexos) y producirá un dictamen con observaciones. Esas observaciones pueden ser:

- **Tipo A — Solicitudes de revisión mayor** (re-experimentación, re-análisis, re-escritura de sección): típicamente 1–4 ítems que pueden retrasar la defensa 1–3 meses.
- **Tipo B — Solicitudes de revisión menor** (aclaraciones, correcciones tipográficas, citas adicionales, figuras mejoradas): típicamente 3–15 ítems que se responden en 2–4 semanas.
- **Tipo C — Observaciones de fondo** (cuestionamiento de hipótesis, debilidades metodológicas, comparaciones faltantes): las más difíciles, requieren respuesta sustantiva.

**Este paquete NO reemplaza al comité.** Lo que hace es:

1. **Predecir** los 20–30 puntos de revisión más probables basados en (a) el manuscrito actual, (b) la literatura comparable, (c) los criterios formales del reglamento FADA, (d) las objeciones anticipadas en `DEFENSE_QA_PREP.md` y `JOURNAL_SUBMISSION_PACKET/RESPONSE_TO_REVIEWERS_TEMPLATE.md`.
2. **Preparar** respuestas pre-fabricadas con anclaje a sección/página/figura/tabla específica del manuscrito, para que Iván pueda responderlas en minutos (no horas) cuando aparezcan en el dictamen.
3. **Categorizar** cada punto por tipo (A/B/C), por capítulo afectado, y por esfuerzo de respuesta estimado (minutos / horas / días).
4. **Documentar** las decisiones tomadas en el manuscrito, con justificación metodológica — para que Iván pueda defender cada trade-off con datos, no con improvisación.

El paquete sigue el patrón **ext-publication-draft-split** aplicado previamente a T046a (MOPC), T101a (PR), T102a (social), T113 (Cap.4 esqueleto), T127 (journal), T118-T121 (advisor): el lado de la **acción externa** (revisión real del comité) permanece `[!]`; el lado de la **preparación autónoma** se entrega en este paquete.

---

## §2 — Tabla de placeholders

| ID | Placeholder | Archivo donde se usa | Cómo llenar |
|----|-------------|----------------------|-------------|
| `PLACEHOLDER_001` | Nombre del director de tesis (en el manuscrito final) | Todos | Iván pone "Dr. [Nombre]" o "[Pendiente FADA]" según defensa del director |
| `PLACEHOLDER_002` | Nombre del comité evaluador (3 nombres típicos en FADA) | `COMMITTEE_COMPOSITION.md` | Iván recibe los nombres al presentar el packet T122 |
| `PLACEHOLDER_003` | Fecha tentativa de presentación oral de la tesis | `COMMITTEE_COMPOSITION.md` | Secretaría Académica FADA |
| `PLACEHOLDER_004` | Número de dictamen FADA | `RESPONSE_LOG_TEMPLATE.md` | Iván recibe esto tras entrega |
| `PLACEHOLDER_005` | Plazo formal para respuesta a observaciones (días) | `RESPONSE_LOG_TEMPLATE.md` | Reglamento FADA-FP-UNA (típicamente 15–30 días) |
| `PLACEHOLDER_006` | Logos / membretes oficiales FADA-FP-UNA | `RESPONSE_LOG_TEMPLATE.md` | Descargar de la web institucional |
| `PLACEHOLDER_007` | Cédula de identidad del autor | `RESPONSE_LOG_TEMPLATE.md` | Solo en el header formal, no en cuerpo |
| `PLACEHOLDER_008` | ORCID del autor | Todos | Público |
| `PLACEHOLDER_009` | Dirección postal institucional para notificación | `RESPONSE_LOG_TEMPLATE.md` | UNA-FADA |
| `PLACEHOLDER_010` | Email institucional del comité | `RESPONSE_LOG_TEMPLATE.md` | Secretaría FADA |

> Los demás archivos del paquete no requieren placeholders: son contenido pre-fabricado que Iván personaliza solo si cambia el contexto.

---

## §3 — Instrucciones de uso (5 pasos)

1. **Hoy / pre-FADA:** leer `TOP_25_LIKELY_OBJECTIONS.md` (las 25 objeciones más probables con respuesta pre-fabricada). Marcar cuáles le generan duda — esas son las que Iván debe reforzar.
2. **Tras recibir dictamen (15 días plazo FADA):** abrir `RESPONSE_LOG_TEMPLATE.md`, copiar la estructura, pegar cada observación del comité en la columna "Observación literal".
3. **Para cada observación:** buscar en `TOP_25_LIKELY_OBJECTIONS.md` si está pre-fabricada. Si sí → usar la respuesta como base. Si no → usar `RESPONSE_FRAMEWORK.md` para estructurar la respuesta en 4 pasos (acknowledge → cite → justify → offer).
4. **Validar antes de entregar:** correr el `CHECKLIST_ANTES_DE_ENTREGAR.md` (35 ítems / 5 gates). Items marcados 🔴 bloqueantes, 🟡 recomendables.
5. **Tras defensa aprobada:** archivar el paquete completo en `Defensa/COMMITTEE_REVIEW_PACKET/answered_<DICTAMEN_ID>/` con la respuesta enviada + respuesta original del comité + versión final del manuscrito revisado.

Tiempo total estimado: **4–8 horas** si las observaciones están pre-fabricadas (vs. 3–5 días si Iván las responde desde cero). Esto se traduce en 2–4 semanas de diferencia en el plazo total hasta la defensa pública (T126).

---

## §4 — Matriz de diferencias vs. otros paquetes

| Paquete | Cuándo se usa | Quién recibe | Output final |
|---------|---------------|--------------|--------------|
| `MOPC_FILING_PACKET/` (T046a) | Pre-defensa, para pedir imágenes dron MOPC | MOPC (institución externa) | PDF impreso + SFP-020 firmado |
| `FADA_TFG_SUBMISSION_PACKET.md` (T122) | M9 — primera entrega al comité | Secretaría FADA | Manuscrito impreso + cover letter |
| `ADVISOR_PURSUIT_PACKET/` (T118-T121) | M8 — antes de tener director | 6 advisors candidatos | 6 emails personalizados |
| `JOURNAL_SUBMISSION_PACKET/` (T127) | Post-defensa, para journal | Editor de revista Q1/Q2 | Cover letter + metadata JSON + paper |
| **`COMMITTEE_REVIEW_PACKET/` (T124-split)** | **M10 — tras recibir dictamen del comité** | **Comité FADA** | **Respuesta a observaciones + manuscrito revisado** |
| `PR_DRAFT.md` (T101) | Post-acceptance | Medio de prensa | Press release |
| `SOCIAL_DRAFT.md` (T102) | Post-acceptance | Redes sociales | 4 posts |

**Posición en el timeline:** este paquete se ejecuta **después** de `FADA_TFG_SUBMISSION_PACKET.md` (cuando el comité ya revisó) y **antes** de `JOURNAL_SUBMISSION_PACKET/` (cuando el paper está limpio). Es el último filtro de calidad antes de la versión camera-ready.

---

## §5 — Riesgos nuevos introducidos

- **R-NEW-26**: Iván entrega la respuesta demasiado tarde (después del plazo FADA). Mitigación: `RESPONSE_LOG_TEMPLATE.md` tiene campo "Plazo formal" en rojo, Iván anota fecha + 5 días hábiles como deadline interno.
- **R-NEW-27**: El comité pide re-experimentación que requiera GPU rentada (>USD 50). Mitigación: `BUDGET_REVISION_PLAN.md` tiene Plan B (re-análisis con datos ya producidos) + escalación a Iván si Plan B no aplica.
- **R-NEW-28**: El comité cuestiona la ausencia de un director formal (vinculado a R-NEW-21 advisor pursuit). Mitigación: el paquete asume que Iván aceptó advisor ANTES de T124 (FADA-FP-UNA requiere director de tesis formal para registrar revisión).
- **R-NEW-29**: Una observación del comité contradice un dato publicado en preprint arxiv (T099). Mitigación: `ARXIV_UPDATE_PLAN.md` documenta cómo actualizar el preprint sin retractar.
- **R-NEW-30**: El comité exige reducir extensión del manuscrito (Cap. 1–6 = 26k palabras es excesivo para tesis FP-UNA estándar). Mitigación: `MANUSCRIPT_TRIM_PLAN.md` propone rutas de poda por capítulo (objetivo: 18–20k palabras).

---

## §6 — Prerrequisitos del paquete

| Prerrequisito | Estado | Notas |
|---------------|--------|-------|
| Manuscrito UNA-FADA completo (Cap. 1–6) | ✅ `Capitulos/Cap1_..Cap6_..md` | 26,301 palabras verificado 2026-09-01 |
| `FADA_TFG_SUBMISSION_PACKET.md` entregado | ❌ Iván | T123, no iniciado |
| Director de tesis asignado | ❌ Iván | T118-T121, packet listo pero sin enviar |
| Dictamen del comité recibido | ❌ Iván | T124, upstream |
| `DEFENSE_QA_PREP.md` (banco de Q&A) | ✅ 50 preguntas | Complementario, no reemplazo |
| `JOURNAL_SUBMISSION_PACKET/RESPONSE_TO_REVIEWERS_TEMPLATE.md` | ✅ 7 objeciones | Aplicable como banco secundario |

> **Conclusión:** este paquete es **estructuralmente completo** y puede revisarse desde hoy. Solo se "activa" cuando Iván recibe el dictamen del comité.

---

## §7 — Inventario de archivos

```
Defensa/COMMITTEE_REVIEW_PACKET/
├── README.md                          ← este archivo
├── COMMITTEE_COMPOSITION.md           ← tipología del comité FADA + 3 plantillas
├── TOP_25_LIKELY_OBJECTIONS.md        ← banco principal: 25 objeciones pre-fabricadas
├── RESPONSE_FRAMEWORK.md              ← metodología de respuesta en 4 pasos
├── RESPONSE_LOG_TEMPLATE.md            ← plantilla para responder dictamen
├── MANUSCRIPT_TRIM_PLAN.md            ← poda por capítulo (si el comité lo pide)
├── BUDGET_REVISION_PLAN.md            ← qué hacer si piden re-experimentación cara
├── ARXIV_UPDATE_PLAN.md               ← cómo actualizar preprint sin retractar
├── COMMITTEE_ETHICS_CHECK.md          ← 8 chequeos éticos previos (FPIC, datos indígenas)
└── CHECKLIST_ANTES_DE_ENTREGAR.md     ← 35 ítems / 5 gates pre-entrega
```

**Total estimado:** 10 archivos, ~140 KB, ~2,200 líneas.

---

## §8 — Cómo NO usar este paquete

- ❌ NO usar como sustituto de la lectura crítica del manuscrito. Iván debe leer `Capitulos/Cap1_..Cap6_..md` completo antes de la defensa.
- ❌ NO usar las respuestas pre-fabricadas mecánicamente sin verificar que aplican al contexto exacto del comité. Cada universidad tiene matices.
- ❌ NO usar para responder observaciones de TIPO A (revisión mayor) sin consultar al director de tesis primero.
- ❌ NO enviar al comité antes de que el director de tesis (T118) lo apruebe — el director es el firmante primario de la respuesta institucional.
- ❌ NO incluir este paquete en `Capitulos/` ni en `paper/` — pertenece a `Defensa/` porque es logística de defensa, no contenido académico.
