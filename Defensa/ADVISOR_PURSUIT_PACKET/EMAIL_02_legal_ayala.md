# EMAIL 02 — Horacio Legal Ayala (FP-UNA, computer vision)

**Para:** Prof. Horacio Legal Ayala
**Facultad:** Facultad Politécnica, Universidad Nacional de Asunción (FP-UNA), Departamento de Ingeniería Informática
**Email:** `[PLACEHOLDER_003_legal_ayala]` (buscar en directorio FP-UNA)
**Probabilidad de aceptación:** MEDIA-ALTA (componente CV fuerte)
**Cuándo enviar:** segundo, solo si Cristaldo declina o no responde en 21 días

---

## Asunto sugerido

```
Tesis FP-UNA — anotación semiautomática con visión por computadora, busca director/co-autor
```

Alternativa más corta:

```
Tesis CV + cartografía FP-UNA — busca director (paper terminado)
```

---

## Cuerpo del email

```
Estimado Prof. Legal Ayala,

Me llamo Iván Weiss Van der Pol y estoy finalizando una tesis de maestría
en el área de visión por computadora aplicada a cartografía, en el marco
de FP-UNA / FADA-UNA. Le escribo porque su trabajo en procesamiento de
imágenes y computer vision es directamente relevante al componente técnico
del trabajo.

El trabajo está terminado en un 100% — busco co-firma sobre trabajo cerrado,
no supervisión:

  - Paper: "[PLACEHOLDER_018 — título exacto]"
    → https://arxiv.org/abs/[PLACEHOLDER_006]

    Abstract: [PLACEHOLDER_019]

  - Dataset anotado: [PLACEHOLDER_020] (~10K features, anotación con
    Florence-2 + SAM + CLIP + revisión inter-anotador Cohen κ=0.87)
    → https://huggingface.co/datasets/[PLACEHOLDER_007]

  - Modelo fine-tuned: pesos en Hugging Face Hub
    → https://huggingface.co/[PLACEHOLDER_008]

  - Código + Docker: GitHub
    → https://github.com/[PLACEHOLDER_009]

Por qué su perfil encaja:

  El corazón técnico del trabajo es la pipeline de anotación semiautomática
  (Sección 4.2 del paper, Tabla 4.7): combinamos Florence-2 (modelo
  base, 2023 — vendor de la fundación con sede Redmond), Segment
  Anything Model (SAM, 2023 — vendor con sede Menlo Park) para
  segmentación de geometrías en teselas Sentinel-2, y CLIP (modelo
  fundación visión-lenguaje, 2021) para zero-shot classification de
  features OSM. Su línea de computer
  vision en FP-UNA tiene expertise directo en la integración de estos
  modelos para el caso paraguayo.

  Su trabajo en [PLACEHOLDER_004 — referencia específica a 1-2 papers
  recientes del Prof. Legal Ayala, ej. sobre detección de objetos en
  imágenes satelitales o clasificación de uso de suelo] es el tipo de
  base técnica que da credibility a la sección de métodos.

Lo que le pido:

  - Director o co-director de tesis en FP-UNA Ing. Informática.
  - Co-autor en el paper, con sección destacada de computer vision
    methods (Sección 4 del paper, ~6 páginas, 4 figuras, 4 tablas).
  - En el manuscrito UNA, podría ser co-director junto con un director
    FADA si se requiere la doble filiación.

Lo que le ofrezco:

  - Cero supervisión técnica: la pipeline ya está implementada,
    documentada y con tests passing (CI en GitHub Actions).
  - Co-firma sobre un paper con componente CV reproducible (código +
    Docker + dataset público).
  - Flexibilidad de calendario (defensa primer semestre 2027 o antes).
  - Si me acepta como tesista, llevo a FP-UNA el packet de inscripción
    ya armado para Ing. Informática.

¿Le interesaría revisar el paper arxiv + conversar 30 minutos por
videollamada para evaluar el encaje técnico?

Si me confirma interés esta semana, le envío el PDF del paper + el
manuscrito UNA + agendamos la llamada. Si no es el momento adecuado o
el tema no le interesa, le agradezco y le pido sugerencia de un colega
en FP-UNA con perfil similar.

Cordialmente,

Iván Weiss Van der Pol
ORCID: [PLACEHOLDER_010]
Tel: [PLACEHOLDER_011]
```

---

## Notas para Iván antes de enviar

1. **Llenar `[PLACEHOLDER_004]`** con 1-2 papers REALES del Prof. Legal Ayala. Buscar en Google Scholar con `author:"Horacio Legal Ayala" UNA Paraguay` o revisar publicaciones del Departamento de Informática FP-UNA. Citar paper + año + 1 frase sobre el método.

2. **Diferencia clave vs Cristaldo:** Legal Ayala NO es la línea directa del trabajo. El framing es "usted es el especialista técnico que da credibility al componente CV", no "este trabajo es la 5ta tesis de su línea". El tono debe ser más respetuoso de su tiempo y menos "le estoy dando una extensión de su línea".

3. **Opción co-director:** mencionar la posibilidad de co-dirección con un director FADA (ej. Cristaldo si acepta) o un director FP-UNA diferente. Esto abre más opciones para él.

4. **Timing:** enviar solo DESPUÉS de que Cristaldo decline o no responda en 21 días. NO enviar en paralelo (R-NEW-18: advisor #2 queda mal si recibe email antes que #1 responda).

5. **NO adjuntar manuscrito completo** en este primer email.

6. **Si el paper aún NO está en arxiv:** NO enviar. Mismo trigger que Cristaldo.

---

## Follow-up plan (resumen)

- Day 3: nada.
- Day 7: follow-up corto confirmando recepción.
- Day 14: segundo follow-up ofreciendo videollamada.
- Day 21: si no responde, pivotear a advisor #3 (Von Lücken).

---

## Cross-refs

- `ADVISOR_SHORTLIST_TABLE.md` — Legal Ayala es advisor #2, prioridad MEDIA-ALTA
- `EMAIL_01_cristaldo.md` — enviar ANTES de este (si Cristaldo responde afirmativamente, NO enviar este)
- `EMAIL_03_von_lucken.md` — backup si Legal Ayala declina
- `FOLLOWUP_CADENCE.md` — cadencia detallada
- `SUCCESS_HANDOFF_PACKET.md` — qué enviar si Legal Ayala acepta
