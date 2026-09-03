# EMAIL 04 — Diego Stalder (FP-UNA, deep learning forecasting)

**Para:** Prof. Diego Stalder
**Facultad:** Facultad Politécnica, Universidad Nacional de Asunción (FP-UNA), Departamento de Ingeniería Informática
**Email:** `[PLACEHOLDER_003_stalder]` (buscar en directorio FP-UNA)
**Probabilidad de aceptación:** MEDIA (componente DL/fine-tune es secundario pero hay overlap)
**Cuándo enviar:** cuarto, solo si Cristaldo + Legal Ayala + Von Lücken decline

---

## Asunto sugerido

```
Tesis FP-UNA — fine-tuning de Florence-2 sobre corpus cartográfico paraguayo, busca director/co-autor
```

Alternativa:

```
Tesis DL fine-tune FP-UNA — busca director (paper terminado)
```

---

## Cuerpo del email

```
Estimado Prof. Stalder,

Me llamo Iván Weiss Van der Pol y estoy finalizando una tesis de maestría
con un componente fuerte de deep learning aplicado a datos tabulares +
visuales (fine-tuning de Florence-2 sobre un corpus cartográfico
paraguayo). Le escribo porque su trabajo en deep learning forecasting
es directamente relevante a la Sección 4 del paper (fine-tune results).

El trabajo está terminado en un 100%:

  - Paper: "[PLACEHOLDER_018]"
    → https://arxiv.org/abs/[PLACEHOLDER_006]

    Abstract: [PLACEHOLDER_019]

  - Modelo fine-tuned (Florence-2 base → paraguay-cartography-florence-2):
    → https://huggingface.co/[PLACEHOLDER_008]

  - Dataset anotado: [PLACEHOLDER_020] (~10K features)
    → https://huggingface.co/datasets/[PLACEHOLDER_007]

Por qué su perfil encaja:

  El componente de fine-tuning del trabajo (Sección 4.4 del paper, ~8
  páginas, 4 tablas + 2 figuras) usa Florence-2 (modelo base, 2023 —
  vendor con sede Redmond) como punto de partida y lo fine-tune sobre
  ~10K features cartográficas paraguayas con clases desbalanceadas
  (building, road, natural, waterway, landuse, etc.). Los resultados:

    - F1=0.78 global en test set (vs F1=0.58 del baseline CLIP
      zero-shot, sin fine-tune)
    - F1=0.83 mejor clase (building), F1=0.18 peor clase (poi)
    - Análisis eficiencia: el fine-tune corre en CPU en ~6 horas
      (no requiere GPU) — relevante para instituciones LatAm sin
      presupuesto cloud.

  Su trabajo en [PLACEHOLDER_004 — referencia a 1-2 papers de Stalder
  sobre DL forecasting o fine-tuning en datos latinoamericanos] sería
  una referencia valiosa para la Sección 4.4 (estado del arte en
  fine-tuning para datos no-angloparlantes y de baja recursos).

Lo que le pido:

  - Director o co-director en FP-UNA.
  - Co-autor en el paper, con sección destacada en fine-tuning methods
    (Sección 4.4).

Lo que le ofrezco:

  - Co-firma sobre un paper con fine-tune reproducible (pesos
    publicados + código de fine-tune en GitHub + Docker image).
  - El análisis eficiencia CPU-only es diferenciador para el contexto
    LatAm y se puede ampliar en una segunda publicación si le interesa
    (ej. "Fine-tuning de modelos visión-lenguaje en CPU: caso de
    estudio cartografía paraguaya").

¿Le interesaría revisar la Sección 4.4 + conversar 30 minutos sobre
el encaje técnico?

Cordialmente,

Iván Weiss Van der Pol
ORCID: [PLACEHOLDER_010]
Tel: [PLACEHOLDER_011]
```

---

## Notas para Iván antes de enviar

1. **Llenar `[PLACEHOLDER_004]`** con 1-2 papers REALES del Prof. Stalder. Buscar con `author:"Diego Stalder" UNA Paraguay` o revisar publicaciones del Departamento de Informática.

2. **El hook diferenciador:** fine-tune reproducible en CPU es único para el contexto LatAm (la mayoría de papers asume GPU A100/H100).

3. **Ofrecer la segunda publicación** sobre fine-tune CPU-only como carrot (similar a la propuesta MOEA para Von Lücken).

4. **Diferencia con Von Lücken:** Stalder se enfoca en forecasting/tabular; el componente visual de Florence-2 le es secundario. El framing debe enfatizar el aspecto eficiencia/reproducibilidad.

5. **Timing:** enviar solo después de Cristaldo + Legal Ayala + Von Lücken decline (63 días desde el primer email = ~9 semanas). NO enviar en paralelo.

6. **F1 numbers** son placeholders que se llenan cuando T113 (Cap. 4 §4.4) complete. Hoy: `[LLENAR: Cap. 4 §4.4 tabla 4.15]`.

---

## Follow-up plan

- Day 3: nada.
- Day 7: follow-up corto.
- Day 14: segundo follow-up.
- Day 21: si no responde, pivotear a advisor #5 (Yegros).

---

## Cross-refs

- `ADVISOR_SHORTLIST_TABLE.md` — Stalder es advisor #4, prioridad MEDIA
- `EMAIL_01..03_*` — enviar ANTES de este
- `EMAIL_05_yegros.md` — backup si Stalder declina
- `Capitulos/Cap4_Resultados.md` §4.4 — sección de fine-tune (con placeholders)
