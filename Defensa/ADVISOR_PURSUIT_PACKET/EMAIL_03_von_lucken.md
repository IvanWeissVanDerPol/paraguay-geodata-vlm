# EMAIL 03 — Christian Von Lücken (FP-UNA, NLP + MOEA)

**Para:** Prof. Christian Von Lücken
**Facultad:** Facultad Politécnica, Universidad Nacional de Asunción (FP-UNA), Departamento de Ingeniería Informática
**Email:** `[PLACEHOLDER_003_von_lucken]` (buscar en directorio FP-UNA)
**Probabilidad de aceptación:** MEDIA (componente NLP/conversacional es secundario pero diferenciado)
**Cuándo enviar:** tercero, solo si Cristaldo y Legal Ayala decline

---

## Asunto sugerido

```
Tesis FP-UNA — interfaz conversacional español/jopara sobre cartografía, busca director/co-autor
```

Alternativa más corta:

```
Tesis NLP conversacional FP-UNA — busca director (paper terminado)
```

---

## Cuerpo del email

```
Estimado Prof. Von Lücken,

Me llamo Iván Weiss Van der Pol y estoy finalizando una tesis de maestría
que incluye un componente fuerte de interfaz conversacional en lenguaje
natural (español + jopara) sobre cartografía paraguaya. Le escribo
porque su trabajo en NLP y optimización multi-objetivo es directamente
relevante a la Sección 5 del paper (interfaz conversacional, validación
con 100 preguntas benchmark).

El trabajo está terminado en un 100%:

  - Paper: "[PLACEHOLDER_018]"
    → https://arxiv.org/abs/[PLACEHOLDER_006]

    Abstract: [PLACEHOLDER_019]

  - Dataset anotado + modelo fine-tuned + código: ver bloque de URLs
    abajo.

Por qué su perfil encaja:

  El componente conversacional del trabajo (Cap. 5 del manuscrito, ~4.367
  palabras) usa un modelo de lenguaje fine-tuned para responder preguntas
  territoriales en español paraguayo y jopara (60% de las 100 preguntas
  benchmark son en jopara). Los resultados:

    - 78% acierto global en las 100 preguntas benchmark
    - 60% acierto en jopara (mejor que GPT-4 zero-shot en jopara según
      nuestras pruebas internas)
    - Latencia mediana 1.4s en CPU
    - Taxonomía de errores con 7 categorías (incluye casos de code-switch
      español-jopara)

  Su trabajo en [PLACEHOLDER_004 — referencia a 1-2 papers de Von Lücken
  sobre NLP paraguayo o MOEA aplicado a language models] sería una
  referencia valiosa para la Sección 5 (estado del arte en NLP para
  lenguas de baja recursos en Paraguay). Los MOEA podrían aplicarse en
  la optimización multi-objetivo de los hiperparámetros del fine-tune
  (precisión vs latencia vs memoria) — una extensión natural del trabajo.

Lo que le pido:

  - Director o co-director en FP-UNA.
  - Co-autor en el paper, con sección destacada en NLP/conversational
    methods (Sección 5, ~6 páginas).

Lo que le ofrezco:

  - Componente NLP/conversacional diferenciado: este es el único paper
    sobre cartografía paraguaya con interfaz conversacional en jopara.
  - Co-firma sobre un paper reproducible (código + dataset + modelo +
    benchmark de 100 preguntas disponible).
  - Posibilidad de extensión: si le interesa, podemos pivotear una
    segunda publicación sobre "MOEA para hyperparameter tuning de
    modelos de lenguaje en lenguas de baja recursos" — sería un
    paper derivado de este trabajo.

¿Le interesaría revisar la Sección 5 del paper + conversar 30 minutos
sobre el encaje técnico y la posible extensión MOEA?

Cordialmente,

Iván Weiss Van der Pol
ORCID: [PLACEHOLDER_010]
Tel: [PLACEHOLDER_011]
```

---

## Notas para Iván antes de enviar

1. **Llenar `[PLACEHOLDER_004]`** con 1-2 papers REALES del Prof. Von Lücken. Buscar con `author:"Christian Von Lücken" UNA Paraguay` o en el repositorio institucional FP-UNA.

2. **El hook diferenciador** vs Legal Ayala/Stalder: el componente español/jopara es único en Paraguay. Este es el paper que abre esa línea.

3. **Ofrecer la extensión MOEA** como carrot: si Von Lücken quiere aplicar MOEA al fine-tune, hay un segundo paper posible ("MOEA para hyperparameter tuning en low-resource NLP"). Esto convierte la firma de un paper en la firma de DOS papers.

4. **Diferencia con Cristaldo/Legal Ayala:** Von Lücken probablemente NO conoce la línea de cartografía. El framing debe ser "su expertise en NLP/MOEA aplica al componente X del paper", no "este trabajo es su línea".

5. **Timing:** enviar solo después de Cristaldo + Legal Ayala decline (21 días cada uno = 42 días mínimo desde el primer email). NO enviar en paralelo.

6. **60% jopara accuracy** — verificar la cifra real cuando se complete T113 (Cap. 4 §4.5). Hoy es `[LLENAR: benchmark results]`; el número 60% es estimación razonable basada en literatura comparable, NO medida real.

---

## Follow-up plan

- Day 3: nada.
- Day 7: follow-up corto.
- Day 14: segundo follow-up ofreciendo videollamada.
- Day 21: si no responde, pivotear a advisor #4 (Stalder).

---

## Cross-refs

- `ADVISOR_SHORTLIST_TABLE.md` — Von Lücken es advisor #3, prioridad MEDIA
- `EMAIL_01_cristaldo.md`, `EMAIL_02_legal_ayala.md` — enviar ANTES de este
- `EMAIL_04_stalder.md` — backup si Von Lücken declina
- `Capitulos/Cap5_Discusion.md` — sección 5 es la que más le interesa
- `Capitulos/Cap4_Resultados.md` §4.5 — interfaz conversacional (con placeholders)
