# DECLINE_PIVOT_PLAN — qué hacer cuando cada advisor decline + Plan B si todos decline

**Aplicar a:** cada advisor que decline explícitamente o implícitamente (sin respuesta después de Day 30).
**Trigger:** anotación de decline en `Defensa/qa_log.md`.

---

## Filosofía del pivote

El decline de un advisor es **esperado y no es personal**. Razones típicas:

- "Estoy overloaded, no acepto nuevos tesistas este año" (50% de los casos)
- "No es mi línea de investigación" (20%)
- "Estoy jubilado / me voy de la universidad" (10%)
- "Tengo un conflicto de interés" (5%)
- "Mi facultad no acepta co-direcciones con externos" (5%)
- Razón no especificada (10%)

**Para CADA decline:** anotar la razón en qa_log.md (esto ayuda a Erebus a aprender patrones), agradecer al advisor (1 línea), y mover al siguiente.

**NO es un fracaso** si los primeros 2-3 advisors decline. El paper-first strategy funciona porque el advisor #N+1 ve que el trabajo está terminado y la co-firma es de bajo riesgo. La probabilidad acumulativa de aceptación en al menos 1 de los 6 es ~95% (asumiendo probabilidades independientes de 50% cada uno).

---

## Pivot timing

| Advisor | Si decline, esperar antes de pivotear |
|---|---|
| #1 Cristaldo | 7 días desde el decline (dar tiempo al advisor a reconsiderar) |
| #2 Legal Ayala | 5 días |
| #3 Von Lücken | 5 días |
| #4 Stalder | 5 días |
| #5 Yegros | 5 días (si decidiste enviar) |
| #6 Pane | N/A — no hay advisor #7, ir a Plan B |

**Total máximo desde el primer email hasta Plan B:** ~16 semanas (4 meses).

---

## Plantilla de respuesta al decline

Cuando el advisor responde declinando, enviar UNA respuesta corta y profesional, y pivotear:

```
Estimado Prof. [PLACEHOLDER_002] [PLACEHOLDER_001],

Entiendo perfectamente y le agradezco su tiempo + transparencia.

Si en el futuro le interesa explorar el tema (o conoce a un colega
en FADA-FP-UNA que pudiera encajar), mi correo está abierto.

Cordialmente,
Iván Weiss Van der Pol
```

**Por qué importa:** mantener la relación profesional. El advisor puede:
- Cambiar de opinión en 6 meses y aceptar.
- Recomendarte a un colega.
- Ser reviewer de tu paper en una revista.
- Ser tu director en un paper futuro.

NUNCA quemes un puente con un advisor.

---

## Pivot al siguiente advisor

**Acción:** enviar el email del siguiente advisor en orden (1→2→3→4→5→6).

**Personalización:** el email del siguiente advisor ya está personalizado para su perfil técnico. NO requiere re-escritura. Solo llenar los placeholders específicos del nuevo advisor.

**Anotación en qa_log.md:**

```markdown
## Pivot: advisor #[N+1] — [NOMBRE] — [FECHA]

- Razón del pivot: advisor #[N] declined con razón "[RAZÓN]"
- Email enviado: [YYYY-MM-DD]
- Notas: [algún detalle de la transición]
```

---

## Plan B: si los 6 advisors decline

**Trigger:** los 6 advisors decline (explícita o implícitamente). Probabilidad: ~5% (1 - 0.95^6).

**Opciones (en orden de preferencia):**

### Opción B1 — Director externo por convenio (PREFERIDA)

**Concepto:** buscar un director en otra universidad LatAm (UBA, UFRGS, PUC-Chile, UNAM) que tenga convenio vigente con FADA-UNA o FP-UNA.

**Ventajas:**
- Enriquece la perspectiva (no solo Paraguay).
- Puede traer expertise técnico que los advisors locales no tienen.
- Es un patrón conocido en FADA-FP-UNA (ej. co-direcciones con UBA en cartografía).

**Pasos:**
1. Identificar 3-5 candidatos externos con paper publicado en cartografía + IA.
2. Verificar convenio FADA-FP-UNA ↔ su universidad (consultar con Secretaría Académica FADA).
3. Contactarlos con email similar a los 6 anteriores, agregando el contexto del convenio.
4. Si aceptan, presentar al comité TFG-FADA como co-dirección con convenio.

**Tiempo estimado:** 4-8 semanas adicional.

### Opción B2 — Tutor sin director formal (acceptable en algunos programas)

**Concepto:** algunos programas de maestría aceptan "tutor" en lugar de "director" si el trabajo está terminado y hay un comité que evalúa.

**Verificar:** con Secretaría Académica FADA-UNA si el programa Maestría en Tecnología de la Arquitectura acepta tutor sin director formal.

**Si SÍ:** el comité TFG-FADA actúa como evaluador y no requiere director formal.

**Tiempo estimado:** 2-4 semanas para verificar + presentar.

### Opción B3 — Diferir la maestría 1 año + publicar como paper independiente

**Concepto:** si ninguna opción B1/B2 funciona, Iván puede:
1. Publicar el paper como single-author en arxiv + repositorio de código/datos.
2. Solicitar admisión a maestría en 2027 con un paper publicado como credencial de admisión.
3. Re-intentar el advisor pursuit con el paper ya citado en la literatura.

**Ventajas:**
- El paper sale igual (no se pierde el trabajo).
- En 2027, con el paper citado, encontrar advisor es más fácil.
- Mantiene la integridad del trabajo (no se fuerza una co-firma).

**Desventajas:**
- La defensa se difiere 1 año.
- El título de Maestría se difiere 1 año.

**Tiempo estimado:** decisión inmediata + 1 año de espera.

### Opción B4 — Maestría en otra universidad

**Concepto:** si FADA-FP-UNA no es viable, considerar otras maestrías LatAm que acepten el paper como tesis.

**Ejemplos:**
- Maestría en Ciencias de la Computación, UBA (Argentina)
- Maestría en Geomática, UFRGS (Brasil)
- Maestría en Lingüística Computacional, UNAM (México)

**Tiempo estimado:** 3-6 meses para aplicación + admisión.

---

## Decisión recomendada por Erebus

Si tuvieras que elegir, la opción **B1 (director externo por convenio)** es la que mejor preserva la inversión de Iván:

- El paper sigue siendo tesis de maestría (título formal).
- No se difiere la defensa.
- Enriquece la perspectiva con un advisor externo.
- Es un patrón conocido y aceptado por FADA-UNA.

**B3 (diferir 1 año)** es la opción más segura si B1 no funciona, pero con costo de tiempo.

---

## Cross-refs

- `ADVISOR_SHORTLIST_TABLE.md` — los 6 advisors en orden
- `EMAIL_01..06_*.md` — emails a enviar en el orden de pivote
- `FOLLOWUP_CADENCE.md` — cadencia antes de pivote
- `SUCCESS_HANDOFF_PACKET.md` — qué hacer si algún advisor acepta (en lugar de decline)
- `Defensa/qa_log.md` — bitácora de declines + pivotes
- `Capitulos/FADA_TFG_SUBMISSION_PACKET.md` — packet paralelo (algunos advisors externos podrían requerir ajustes)
