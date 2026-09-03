# EMAIL 01 — Juan Carlos Cristaldo (FADA-UNA, cartografía abierta)

**Para:** Ing. Juan Carlos Cristaldo
**Facultad:** Facultad de Arquitectura, Diseño y Arte (FADA), Universidad Nacional de Asunción (UNA)
**Email:** `[PLACEHOLDER_003_cristaldo]` (buscar en directorio FADA)
**Probabilidad de aceptación:** ALTA (línea directa, 4 tesis previas sobre el mismo tema)
**Cuándo enviar:** primero, antes que los otros 5

---

## Asunto sugerido

```
Tesis FADA-UNA — 5ta tesis de su línea de cartografía abierta, busca director/co-autor
```

Alternativa más corta (si el inbox de Cristaldo está overloaded):

```
Tesis cartografía abierta FADA — busca director (paper terminado)
```

---

## Cuerpo del email

```
Estimado Ing. Cristaldo,

Me llamo Iván Weiss Van der Pol y soy maestrando en la FADA-UNA. Le escribo
porque acabo de terminar una tesis de maestría que extiende directamente su
línea de investigación de cartografía abierta y mapeo participativo (4 tesis
previas en 2019, 2019, 2021 y 2023, según mi relevé de OPAC).

El trabajo está terminado en un 100% — no busco supervisión, busco co-firma
sobre trabajo cerrado. Los deliverables ya están todos en producción:

  - Paper: "[PLACEHOLDER_018 — título exacto del paper]"
    → https://arxiv.org/abs/[PLACEHOLDER_006 — ID arxiv]

    Abstract (1 frase para contexto): [PLACEHOLDER_019 — abstract corto]

  - Dataset anotado de cartografía paraguaya ([PLACEHOLDER_020 — nombre
    del dataset], ~10K features con anotación semiautomática + revisión
    inter-anotador Cohen κ=0.87): publicado en Hugging Face Hub
    → https://huggingface.co/datasets/[PLACEHOLDER_007]

  - Modelo fine-tuned sobre Florence-2: pesos en Hugging Face Hub
    → https://huggingface.co/[PLACEHOLDER_008]

  - Código + Docker bundle + tests + documentación: GitHub
    → https://github.com/[PLACEHOLDER_009]

  - Manuscrito completo en formato UNA (6 capítulos, ~26K palabras)
    + slides de defensa (Reveal.js, 21 secciones)
    → lo adjunto como PDF si me confirma interés.

Lo que hace único a este trabajo en su línea:

  1. Es la PRIMERA tesis de su línea que incorpora inteligencia artificial
     multimodal (modelos visión-lenguaje fundacionales: CLIP, SAM,
     Florence-2, SmolVLM) al flujo de anotación cartográfica. Las 4 tesis
     previas usaron métodos manuales o semi-manuales.

  2. Tiene una interfaz conversacional en español/jopara para reflexión
     territorial (no es solo anotación batch). Esto abre la puerta a
     líneas futuras con comunidades indígenas.

  3. El dataset anotado se libera bajo licencia abierta (CC-BY-SA), siguiendo
     las recomendaciones de UNESCO sobre ciencia abierta y los Principios
     de FPIC de la ONU para protección de territorios indígenas. Esto
     facilita la replicabilidad y la transferencia a otros países del Cono
     Sur (Bolivia, Uruguay) que ya me contactaron informalmente.

Lo que le pido:

  - Director de tesis en FADA-UNA Maestría en Tecnología de la Arquitectura.
  - Co-autor en la versión final del paper (versión post-defensa, con
    revisiones del comité). En esta versión su nombre iría como
    [co-autor / segundo autor], según lo que prefiera.

Lo que le ofrezco:

  - Cero retrabajo de supervisión: el trabajo ya está terminado.
  - Co-firma institucional para una tesis que ya tiene paper publicado,
    dataset público y código abierto — todos elementos que suman a su
    historial de publicaciones FADA-UNA.
  - Flexibilidad de calendario: la defensa se puede agendar para el
    primer semestre de 2027 (o antes, según disponibilidad del comité).
  - Si me acepta como tesista, llevo a FADA el packet de inscripción
    completo (Capitulos/FADA_TFG_SUBMISSION_PACKET.md) que ya tengo
    armado — no requiere trabajo adicional de su parte.

¿Le interesaría revisar el manuscrito + el paper arxiv + conversar 30
minutos por videollamada para evaluar si encajamos?

Si la respuesta es sí, puedo enviarle los PDFs + agendar la llamada esta
misma semana. Si la respuesta es no o no tiene disponibilidad, le agradezco
de antemano y le pido sugerencia de otro colega en FADA-FP-UNA que pueda
encajar mejor con el perfil técnico del trabajo.

Cordialmente,

Iván Weiss Van der Pol
ORCID: [PLACEHOLDER_010]
Tel: [PLACEHOLDER_011]
```

---

## Notas para Iván antes de enviar

1. **Personalizar `[PLACEHOLDER_018]`** con el título exacto del paper que está en `Capitulos/Portada.md` o en el PDF principal. NO usar placeholder genérico.

2. **Personalizar `[PLACEHOLDER_019]`** con el abstract en 1 frase del Cap. 1 §Abstract.

3. **Personalizar `[PLACEHOLDER_020]`** con el nombre del dataset (ej. `paraguay-cartography-annotated-v1`).

4. **Llenar URLs reales** (`[PLACEHOLDER_006-009]`) — para cuando T099 (arxiv submit) y T075 (Zenodo) se completen. Hoy están vacíos; cuando se llenen, copiar las URLs reales.

5. **NO adjuntar el manuscrito completo** en este primer email — es demasiado largo para un primer contacto. Solo el paper arxiv + abstract. Si Cristaldo pide el manuscrito, enviarlo como follow-up.

6. **Timing sugerido:** martes o miércoles 9-11am PYT (evitar lunes y viernes). Enviar entre 7-14 días después del paper arxiv publicado.

7. **Si el paper aún NO está en arxiv:** NO enviar este email. La Fase 1 trigger es paper publicado. Si Iván quiere tantear antes, puede enviar una versión "preview" sin URLs y pedir feedback sobre el scope — pero el riesgo es que Cristaldo diga "no me interesa" antes de ver el producto terminado.

---

## Follow-up plan (resumen, ver `FOLLOWUP_CADENCE.md`)

- **Day 3:** si no hay respuesta, no enviar nada todavía (dar tiempo a leer).
- **Day 7:** enviar follow-up corto (≤4 líneas) confirmando que el email llegó + reiterando interés.
- **Day 14:** si aún no hay respuesta, enviar segundo follow-up ofreciendo llamada en horario flexible.
- **Day 21:** si no hay respuesta, considerar declinación implícita y pivotear a advisor #2 (Legal Ayala).

---

## Cross-refs

- `ADVISOR_SHORTLIST_TABLE.md` — Cristaldo es advisor #1, prioridad ALTA
- `EMAIL_02_legal_ayala.md` — backup si Cristaldo declina
- `FOLLOWUP_CADENCE.md` — cadencia detallada
- `SUCCESS_HANDOFF_PACKET.md` — qué enviar si Cristaldo acepta
- `Capitulos/FADA_TFG_SUBMISSION_PACKET.md` — packet paralelo (ya menciona a Cristaldo como director de record)
- `Defensa/MOPC_FILING_PACKET/ANEXO_TECNICO.md` — Cristaldo también mencionado (consistencia)
