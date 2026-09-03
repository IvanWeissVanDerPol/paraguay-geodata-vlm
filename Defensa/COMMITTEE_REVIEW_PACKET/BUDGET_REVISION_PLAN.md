# BUDGET REVISION PLAN — Qué hacer si el comité pide re-experimentación con costo elevado

**Tesis:** Anotación semiautomática del corpus cartográfico abierto de Paraguay con modelos multimodales fundacionales y una interfaz conversacional para la reflexión territorial

**Autor:** Iván Weiss Van Der Pol

**Origen:** Split de **T124** `[P0][M10][NO-GPU][D] Thesis committee review + revisions`

**Fecha del paquete:** 2026-09-02

---

## §1 — Contexto y principio rector

El manuscrito actual declara un costo total de **USD 14.20** en cómputo (todo CPU-only + 1× RTX 3090 local para fine-tune). Si el comité pide **re-experimentación con un modelo más caro** (e.g., LLaVA-13B, Qwen2-VL-72B, GPT-4V, Gemini-1.5-Pro) o con **un dataset más grande** (e.g., full Sentinel-2 Paraguay), el costo puede escalar a USD 50–300. Este plan documenta cómo responder a esa situación sin违背 el principio rector de la tesis: **soberanía computacional y de datos del corpus paraguayo**.

**Riesgo asociado:** R-NEW-27 (costo GPU rentada).

**Principio rector:** cualquier costo >USD 50 requiere visto bueno explícito de Iván antes de ejecutar.

---

## §2 — Catálogo de posibles solicitudes de re-experimentación

| Solicitud probable | Modelo / dataset | Costo estimado (USD) | Tiempo de ejecución | ¿Vale la pena? |
|--------------------|------------------|----------------------|----------------------|-----------------|
| Re-correr LLaVA-13B como baseline alterno | LLaVA-13B en RTX 3090 local | 0–5 | 6 h | **Sí** — baja costo, alta señal |
| Re-correr Qwen2-VL-7B como baseline alterno | Qwen2-VL-7B en RTX 3090 local | 0–5 | 5 h | **Sí** — baja costo, alta señal |
| Fine-tune completo de LLaVA-13B sobre Paraguay-custom | LLaVA-13B + RTX 3090 o A100 cloud | 30–80 (cloud) | 12–24 h | **Depende** — ver §3 |
| Re-correr con dataset completo de Sentinel-2 (~5 TB) | Sentinel-2 + cómputo cloud | 200–500 | 2–4 semanas | **No** — usar muestra estratificada |
| Re-correr con GPT-4V como oráculo | GPT-4V API | 50–200 | 4–8 h | **No** — viola soberanía de datos |
| Re-correr con Gemini-1.5-Pro como oráculo | Gemini-1.5-Pro API | 30–150 | 4–8 h | **No** — viola soberanía de datos |
| Validación cruzada con 10-fold en lugar de 5-fold | Re-correr todas las baselines | 10–20 | 4–6 h | **Sí** — baja costo, fortalece rigor |
| Bootstrap de intervalos de confianza (1000 muestras) | Re-procesar outputs | 0 (CPU) | 2 h | **Sí** — costo cero, mejora presentación |

---

## §3 — Árbol de decisión: ¿ejecutar o contraargumentar?

```
                    ┌─ El comité pide re-experimentación
                    │
                    ▼
        ¿El costo es > USD 50?
        ├── NO  ───────► Ejecutar (sin consultar a Iván)
        │                  Tiempo total ≤ 2 semanas
        │                  Documentar como "análisis de robustez" en Cap. 5
        │
        └── SÍ  ───────► ¿El modelo es soberano (no-API)?
                         ├── NO (API externa) ──► Contraargumentar §4.1
                         │                          "La comparación con API externa
                         │                           no aporta a la contribución
                         │                           metodológica porque rompe
                         │                           soberanía de datos"
                         │
                         └── SÍ (modelo open-weight)
                              │
                              ▼
                       ¿La hipótesis H1/H2/H3 depende del resultado?
                       ├── NO ──► Contraargumentar §4.2
                       │          "El resultado de esta re-experimentación
                       │           no cambia las conclusiones del manuscrito"
                       │
                       └── SÍ ──► Consultar a Iván
                                   Presentar 3 opciones:
                                   (a) Ejecutar con presupuesto
                                   (b) Diferir a trabajo futuro (Cap. 6)
                                   (c) Reducir el alcance (muestra estratificada)
```

---

## §4 — Contraargumentos pre-fabricados

### §4.1 — Contra-modelos API externa (GPT-4V, Gemini, Claude)

> "Agradezco la sugerencia del comité de comparar con un modelo frontier. Sin embargo, esta comparación **rompe la soberanía de datos** que es un principio metodológico explícito del manuscrito (Cap. 1 §1.5, Cap. 5 §5.6, Cap. 6 §6.3). El corpus paraguayo incluye topónimos indígenas qom y guaraní-ñandeva clasificados como sensibles por las comunidades (cuaderno de campo, ver `ETHICS_WAIVER_MEMO.md`). Enviar este corpus a una API externa de un proveedor fuera del Paraguay constituye:
>
> 1. **Violación del protocolo FPIC** (Free, Prior and Informed Consent) acordado con las comunidades en la fase de caracterización.
> 2. **Riesgo de data leakage** — los proveedores de API pueden usar los prompts para entrenar versiones futuras del modelo, lo cual haría que el corpus paraguayo aparezca en versiones posteriores sin consentimiento de las comunidades.
> 3. **Inconsistencia metodológica** — el manuscrito declara explícitamente (Cap. 3 §3.4) que todos los modelos son open-weight y ejecutables on-prem para garantizar soberanía.
>
> **Alternativa propuesta:** en lugar de comparar con GPT-4V directamente, podemos citar la literatura existente que ya hizo esa comparación (e.g., Liu et al. 2024 sobre GPT-4V en tareas de cartografía) y discutir las implicaciones para Paraguay en Cap. 5 §5.3 sin exponer el corpus."

**Tiempo de redacción:** 30 minutos. **Tasa de éxito estimada:** 70% (los comités que objetan API externas suelen ceder ante el argumento FPIC).

### §4.2 — Contra-re-experimentación costosa que no cambia conclusiones

> "La re-experimentación solicitada toma [X horas, $Y] y produciría un delta esperado de [±0.02 F1] según el análisis de la literatura comparable (ver Tabla 2.3). Dado que las hipótesis H1, H2, H3 son robustas a este delta (ver Cap. 5 §5.5 análisis de sensibilidad), el resultado **no cambia ninguna conclusión central del manuscrito**. Propongo en su lugar:
>
> 1. Agregar al Cap. 6 (Trabajo futuro) una mención explícita de la re-experimentación como línea futura.
> 2. Documentar el análisis de sensibilidad actual (Cap. 5 §5.5) como evidencia suficiente de robustez.
> 3. Si el comité insiste, ejecutar la re-experimentación con muestra estratificada (10% del dataset, costo USD 5–10, tiempo 1–2 h) como compromiso intermedio."

**Tiempo de redacción:** 30 minutos. **Tasa de éxito estimada:** 50% (depende de si el comité valora más el principio de robustez o el principio de completitud).

### §4.3 — Contra-dataset completo (cuando piden re-correr con Sentinel-2)

> "El dataset completo Sentinel-2 Paraguay 2024–2026 (~5 TB sin comprimir) requiere infraestructura cloud que el presupuesto actual no contempla. Propongo en su lugar:
>
> 1. Documentar la limitación en Cap. 5 §5.6 (ya está: 'cobertura limitada a 87% de las comunidades por muestreo estratificado, no por cobertura completa').
> 2. Si el comité lo solicita, ejecutar con **muestra estratificada por departamento** (1 imagen Sentinel-2 por departamento × 17 departamentos = 17 imágenes × ~500 MB = 8.5 GB, costo USD 5 en cloud, 4 h de procesamiento).
> 3. Documentar los resultados de la muestra estratificada como evidencia de escalabilidad."

**Tiempo de redacción:** 20 minutos. **Tasa de éxito estimada:** 80% (los comités suelen aceptar muestras estratificadas cuando el dataset completo es inviable).

---

## §5 — Plan B — Aceptar la re-experimentación con presupuesto limitado

Si Iván acepta la re-experimentación (visto bueno explícito), seguir este protocolo:

### Paso 1 — Negociar alcance (1 hora)

Negociar con el director de tesis + Iván el alcance mínimo aceptable:
- ¿Es aceptable una muestra estratificada en lugar del dataset completo?
- ¿Es aceptable un modelo de menor tamaño (e.g., LLaVA-7B en lugar de LLaVA-13B)?
- ¿Es aceptable una sola corrida en lugar de validación cruzada?

### Paso 2 — Calcular costo exacto (30 minutos)

Con el alcance negociado, calcular:
- Tiempo de cómputo (horas × potencia)
- Costo en USD (horas × tarifa cloud o amortización local)
- Tiempo de análisis post-procesamiento
- Tiempo de redacción para incorporar al manuscrito

### Paso 3 — Ejecutar (variable)

Ejecutar la re-experimentación. Documentar todo:
- Commit hash del código usado
- Semillas aleatorias
- Versión del dataset
- Outputs en formato reproducible (JSON + log)

### Paso 4 — Análisis y redacción (4–8 horas)

- Análisis estadístico (F1 macro, F1 micro, κ, intervalos de confianza)
- Comparación con resultados originales (tabla + figura)
- Discusión en Cap. 5 §5.X (nueva subsección "Análisis de robustez")
- Actualización del abstract si el resultado cambia alguna conclusión

### Paso 5 — Validación (1 hora)

- `make format-manuscript-check` — 0 errors
- Verificar que la nueva subsección no rompe referencias cruzadas
- Verificar que el abstract sigue siendo coherente

---

## §6 — Plan C — Diferir a trabajo futuro

Si la re-experimentación no es viable (costo o tiempo), diferir a Cap. 6 (Trabajo futuro):

### Redacción sugerida para Cap. 6 §6.4

> "Una línea futura de investigación es la re-experimentación del pipeline con [modelo X / dataset Y] para evaluar la robustez de las hipótesis H1, H2, H3. Esta re-experimentación no fue incluida en el manuscrito actual por restricciones de [costo / tiempo / infraestructura], pero el análisis de sensibilidad reportado en §5.5 indica que las conclusiones son robustas a esta variación. Estimación de recursos para la re-experimentación futura: [X horas-cómputo, $Y, Z semanas de análisis]. Esta línea se工作计划 para 2027-Q2 como continuación post-defensa."

**Tiempo de redacción:** 30 minutos.

---

## §7 — Plantilla de comunicación con Iván si se requiere autorización

Si el plan B requiere visto bueno de Iván, enviar este mensaje al bridge interno:

```
🚨 SOLICITUD AUTORIZACIÓN RE-EXPERIMENTACIÓN

El comité FADA-FP-UNA solicita en el dictamen N° [N] una re-experimentación:
- Modelo/dataset: [nombre]
- Costo estimado: USD [X]
- Tiempo de ejecución: [Y horas]
- Tiempo de redacción post: [Z horas]
- Probabilidad de cambiar conclusiones: [alta / media / baja]

Opciones:
(a) Ejecutar — requiere tu OK explícito (gasto USD [X])
(b) Contraargumentar con §4.X (sin gasto, 30 min de redacción)
(c) Diferir a Cap. 6 trabajo futuro (sin gasto, 30 min de redacción)

Tu decisión: ___
```

---

## §8 — Lección aprendida (memoria del proyecto)

**Regla para futuras tesis:** incluir en el manuscrito (ya está en Cap. 3 §3.4) una **declaración explícita de los modelos open-weight** usados y una **justificación de por qué no se usan modelos API**. Esto previene la mayoría de las objeciones de "comparar con GPT-4V".

**Regla para Iván:** antes de aceptar cualquier re-experimentación costosa, verificar:
1. ¿El modelo es soberano (no API externa)?
2. ¿La hipótesis depende del resultado?
3. ¿Hay alternativa con muestra estratificada?

Si la respuesta a (1) es NO, contraargumentar con §4.1. Si la respuesta a (2) es NO, contraargumentar con §4.2. Si la respuesta a (3) es SÍ, ofrecer la muestra como compromiso.

---

## §9 — Costos de referencia (para calcular presupuestos rápido)

| Recurso | Costo unitario | Fuente |
|---------|----------------|--------|
| RTX 3090 (24 GB) local | USD 0.40/hora (amortización 24 meses sobre USD 1500) | Iván owns |
| A100 (80 GB) cloud | USD 1.50–3.00/hora | Lambda Labs, Vast.ai |
| H100 (80 GB) cloud | USD 2.50–5.00/hora | Lambda Labs, RunPod |
| CPU-only 16 cores | USD 0.10–0.20/hora | Hetzner, OVH |
| Storage 1 TB | USD 0.02–0.10/mes | Backblaze, Wasabi |
| GPT-4V API | USD 0.01–0.03/imagen | OpenAI pricing 2024 |
| Gemini-1.5-Pro API | USD 0.005–0.015/imagen | Google pricing 2024 |
| Fine-tune Florence-2 (base) en RTX 3090 | USD 0.70 (6 h × 0.4/hora amortizado + energía USD 0.50) | Estimación Iván 2026-08 |

**Total declarado del manuscrito actual: USD 14.20** (ver Cap. 4 §4.9).

---

## §10 — Anti-patrones

### Anti-patrón 1 — Aceptar re-experimentación sin consultar a Iván

> ❌ "El comité pide LLaVA-13B, lo voy a ejecutar porque tengo RTX 3090 disponible."

**Por qué es malo:** aunque el costo sea bajo, el principio rector dice "cualquier costo >USD 50 requiere visto bueno". Si Iván tiene compromisos presupuestarios para otras tesis o proyectos, el costo puede ser relevante. **Siempre consultar.**

### Anti-patrón 2 — Aceptar comparación con GPT-4V o Gemini

> ❌ "OK, voy a probar GPT-4V para tener el oráculo."

**Por qué es malo:** viola soberanía de datos y el protocolo FPIC con comunidades indígenas. **Siempre contraargumentar con §4.1.**

### Anti-patrón 3 — Diferir a Cap. 6 sin consultar al director

> ❌ "Esta observación la voy a diferir a trabajo futuro."

**Por qué es malo:** diferir es una decisión que afecta la integridad del manuscrito. El director debe aprobar. **Siempre consultar al director antes de comprometer una respuesta de diferimiento.**

### Anti-patrón 4 — Re-experimentar sin documentar seeds y hashes

> ❌ "Re-corrí LLaVA-13B y me dio F1=0.74. Lo agrego al manuscrito."

**Por qué es malo:** sin reproducibilidad, el resultado no es publicable. **Siempre documentar:** commit hash del código, semillas aleatorias, versión del dataset, paths de los outputs.
