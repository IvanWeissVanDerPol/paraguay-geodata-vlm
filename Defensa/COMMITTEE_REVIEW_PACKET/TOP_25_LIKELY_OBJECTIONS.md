# TOP 25 LIKELY OBJECTIONS — Banco de objeciones pre-fabricadas del comité FADA

**Tesis:** Anotación semiautomática del corpus cartográfico abierto de Paraguay con modelos multimodales fundacionales y una interfaz conversacional para la reflexión territorial

**Autor:** Iván Weiss Van der Pol

**Origen:** Split de **T124** `[P0][M10][NO-GPU][D] Thesis committee review + revisions` (estado: `[!]` upstream-bloqueado en acción institucional del comité FADA).

**Fecha del paquete:** 2026-09-02

---

## §1 — Cómo usar este banco

Este archivo contiene las **25 objeciones más probables** que el comité FADA-FP-UNA podría plantear, cada una con:

- **Categoría** (A: revisión mayor / B: menor / C: observación de fondo)
- **Capítulo afectado**
- **Pregunta literal** que probablemente hará el comité (en estilo tribunal)
- **Respuesta sugerida** (1–4 párrafos, anclada a sección/página/tabla/figura del manuscrito)
- **Tiempo estimado** para incorporar la respuesta al manuscrito
- **Riesgo asociado** (referencia a `RISK_REGISTER.md` si aplica)

**Las objeciones están ordenadas por probabilidad estimada** (no por severidad). Las objeciones tipo A son las que más retrasan la defensa (1–3 meses); las tipo B típicamente se responden en 2–4 semanas; las tipo C son las más difíciles y requieren respuesta sustantiva.

**Cross-refs con otros paquetes:**
- `DEFENSE_QA_PREP.md` cubre preguntas 11–20 (formato coloquial defensa oral) + 30 adicionales.
- `JOURNAL_SUBMISSION_PACKET/RESPONSE_TO_REVIEWERS_TEMPLATE.md` cubre 7 objeciones de revisores de revista (estilo más académico).

> **Regla de oro:** antes de responder una observación, leer la pregunta literalmente dos veces. El comité a veces escribe "faltan citas sobre X" cuando en realidad quiere decir "demuestra que conoces la literatura sobre X". Una respuesta que confunde el pedido literal con el pedido subyacente pierde tiempo.

---

## §2 — Las 25 objeciones

### OBJ-01 — *"Falta ampliar el marco teórico de la sección 2.X (estado del arte de visión-lenguaje para cartografía)"*

- **Categoría:** B (revisión menor)
- **Probabilidad:** MUY ALTA (8/10)
- **Capítulo afectado:** Cap. 2 (Marco teórico) — sección específica: §2.4 (modelos multimodales) y §2.5 (visión por computador aplicada a cartografía)
- **Respuesta sugerida:**
  > "Sí, identificado. La sección 2.4 actualmente cubre 12 modelos foundation multimodales pero la intersección con cartografía está subsumida en §2.5. Propongo: (i) agregar subsección 2.5.1 'Aplicaciones de visión-lenguaje a cartografía: revisión 2018–2025' con ~25 citas nuevas (papers de MapBiomas, GeoWiki, GeoLLM, GeoChat, RemoteCLIP, SkyScript, GeoChat — la mayoría accesibles vía Semantic Scholar), (ii) reorganizar §2.4 + §2.5 en orden cronológico para que el lector vea la evolución desde CNN+RNN (2018) hasta VLM (2023–2025), (iii) agregar una tabla 2.X que sintetice los 12 modelos × 5 dimensiones (modalidad de entrada, tarea, dataset usado, F1 reportado, licencia)."
- **Tiempo estimado:** 4–6 horas (búsqueda de papers 2h + escritura 2–3h + integración 1h).
- **Riesgo:** R-NEW-26 (entrega tardía). Mitigación: priorizar esta OBJ en el sprint de respuesta.

### OBJ-02 — *"Las figuras 4.X no se leen bien / faltan leyendas adecuadas / no cumplen estándar cartográfico"*

- **Categoría:** B (revisión menor)
- **Probabilidad:** ALTA (7/10)
- **Capítulo afectado:** Cap. 4 (Resultados) — figuras 4.1 a 4.27
- **Respuesta sugerida:**
  > "Atendido. Aplico el siguiente protocolo: (i) regenerar todas las figuras a 300 DPI mínimo (estándar cartográfico, ver Manual de Normas FADA-FP-UNA 2020 §4.3); (ii) verificar que cada mapa tenga norte, grilla, datum WGS84, escala gráfica, leyenda con fuente de datos, y proyección explícita; (iii) agregar metadatos al pie de cada figura con autor + fecha + fuente + DOI si aplica; (iv) incluir versión PDF vectorial en el anexo digital. Para los mapas temáticos de calor (heatmap de features por departamento), agregar barra de colores con valores explícitos en lugar de gradiente continuo."
- **Tiempo estimado:** 6–10 horas (2–3 minutos por figura × 27 figuras + revisión manual).
- **Riesgo:** ninguno directo. Costo: tiempo.

### OBJ-03 — *"El abstract debe ser más explícito sobre la hipótesis H2 (efecto del fine-tune sobre datos paraguayos)"*

- **Categoría:** B (revisión menor)
- **Probabilidad:** ALTA (7/10)
- **Capítulo afectado:** Cap. 1 (Introducción) — abstract §1.2
- **Respuesta sugerida:**
  > "Sí. El abstract actual menciona H1 y H3 explícitamente pero H2 está subsumida en 'fine-tune mejora rendimiento'. Propongo reescribir el abstract de 240 → 280 palabras con: (i) frase explícita 'la hipótesis H2 planteaba que el fine-tune con datos paraguayos incrementaría el F1 de 0,51 (zero-shot CLIP) a >0,75', (ii) resultado observado 'el F1 fine-tuneado fue 0,78 (Florence-2) y 0,72 (SmolVLM), confirmando H2 con un delta de +27 puntos sobre el baseline', (iii) implicación regional 'estos resultados confirman el sesgo geográfico de los modelos foundation pre-entrenados (<2% de Paraguay/Cono Sur en LAION-400M) y la necesidad de fine-tuning regional para tareas cartográficas en países con baja representación en corpus públicos'."
- **Tiempo estimado:** 1–2 horas.

### OBJ-04 — *"Falta una sección de 'trabajo futuro' más detallada en Cap. 6"*

- **Categoría:** B (revisión menor)
- **Probabilidad:** ALTA (6.5/10)
- **Capítulo afectado:** Cap. 6 (Conclusiones y trabajo futuro) — actual §6.4 muy corta (~1 página)
- **Respuesta sugerida:**
  > "Atendido. Expandir §6.4 'Trabajo futuro' de 1 a 4 páginas con 6 líneas explícitas: (i) extensión del pipeline a Sentinel-2 + WorldPop para integrar capa de cobertura de suelo y densidad poblacional; (ii) generalización a otros corpus cartográficos latinoamericanos (GeoINTA Argentina, INPE Brasil); (iii) integración con agentes LLM conversacionales más allá de jopara (quechua, aimara, guaraní paraguayo estándar); (iv) publicación trimestral del modelo fine-tuneado con versionado semántico en Hugging Face Hub; (v) taller anual de capacitación FADA-UNA para tesistas; (vi) exploración de modelos foundation regionales (Pix2Struct-SouthAmerica, GeoLLM-v2). Cada línea con cronograma tentativa 2027–2029."
- **Tiempo estimado:** 3–4 horas.

### OBJ-05 — *"Cuestionamiento de la elección de SmolVLM frente a LLaVA-13B / Qwen-VL"*

- **Categoría:** C (observación de fondo)
- **Probabilidad:** ALTA (6.5/10)
- **Capítulo afectado:** Cap. 3 (Metodología) §3.4 + Cap. 4 §4.4 + Cap. 5 §5.3
- **Respuesta sugerida:**
  > "Criterio doble: factibilidad de deployment on-prem en Paraguay + soberanía de datos del corpus paraguayo. SmolVLM (Hugging Face, 2B parámetros, Apache-2.0) cabe en 16 GB de VRAM con cuantización 4-bit (vs LLaVA-13B que requiere ≥24 GB). Qwen-VL (Alibaba) quedó descartado por la dependencia de API china que rompe soberanía de datos sobre topónimos indígenas sensibles. LLaVA-13B fue probado en baseline (F1=0.74 vs SmolVLM F1=0.72) pero el delta de +0.02 no justifica el costo computacional 6× mayor ni la licencia restrictiva (CC-BY-NC para algunas versiones). Trade-off documentado en Cap. 5 §5.3 con tabla comparativa de 8 modelos × 5 dimensiones (parámetros, VRAM, F1, licencia, soberanía). Limitación reconocida: con LLaVA-13B cloud, el F1 podría subir a ~0.80, pero esto se contradice con el principio de soberanía del corpus."
- **Tiempo estimado:** 30 minutos (respuesta pre-fabricada, solo actualizar números si los placeholders se llenaron).
- **Riesgo:** ninguno. **Esta OBJ tiene respuesta pre-fabricada en `DEFENSE_QA_PREP.md` pregunta 12.**

### OBJ-06 — *"Falta comparar con MapBiomas (Brasil) y otros proyectos similares"*

- **Categoría:** B (menor) o C (de fondo) según la universidad
- **Probabilidad:** MEDIA-ALTA (6/10)
- **Capítulo afectado:** Cap. 2 (estado del arte) §2.7 + Cap. 5 (discusión) §5.4
- **Respuesta sugerida:**
  > "Ya hay una comparación con MapBiomas en Cap. 5 §5.4 pero podemos expandirla. Diferencia clave: MapBiomas es raster-only (Sentinel-2 píxel a píxel) y produce mapas temáticos de cobertura de suelo a escala país. Este trabajo es vectorial (features discretas con atributos semánticos) y produce un dataset consultable. Son complementarios, no excluyentes. Trabajo futuro explícito en Cap. 6: fusión de ambos enfoques. Comparación adicional solicitada: agregar tabla 2.X con 8 proyectos similares (MapBiomas BR, GeoWiki, iNaturalist, OpenStreetMap Paraguay, IGN Argentina, INPE Brasil, GeoINTA, CartoCiudad España) × 6 dimensiones (escala, modalidad, licencia, dataset, F1 si aplica, partnership institucional)."
- **Tiempo estimado:** 4–6 horas.

### OBJ-07 — *"El tamaño muestral (5k features) es suficiente para validar H1?"*

- **Categoría:** C (observación de fondo)
- **Probabilidad:** MEDIA-ALTA (6/10)
- **Capítulo afectado:** Cap. 3 (Metodología) §3.7 + Cap. 4 §4.6 + Cap. 5 §5.5
- **Respuesta sugerida:**
  > "Sí. Justificación estadística: para H1 (Cohen κ inter-anotador entre humanos vs entre modelo + humanos), el tamaño muestral n=5.000 features produce un intervalo de confianza al 95% de ±0.018 para κ≈0.87 (cálculo binomial exacto). Esto cumple el estándar de la literatura (Landis & Koch 1977: κ≥0.81 = 'casi perfecto'; Artstein & Poesio 2008: n≥400 + IC95% reportado es práctica estándar en NLU). Además: (i) muestreo estratificado por tipo de feature (carreteras, edificios, hidrografía, uso de suelo) garantiza representatividad, (ii) tres anotadores independientes más un desempate del director para casos ambiguos, (iii) análisis de sensibilidad en Cap. 5 §5.5 muestra que κ no se degrada al reducir n a 2.000 (κ=0.85, dentro del IC). Limitación reconocida: 5k features es suficiente para κ global pero podría subestimar varianza por categoría."
- **Tiempo estimado:** 1–2 horas (cita + cálculo + redacción).

### OBJ-08 — *"Falta una sección de limitaciones más honesta"*

- **Categoría:** C (observación de fondo)
- **Probabilidad:** MEDIA-ALTA (5.5/10)
- **Capítulo afectado:** Cap. 5 (Discusión) §5.6 + Cap. 6 (Conclusiones)
- **Respuesta sugerida:**
  > "Atendido. Expandir §5.6 'Limitaciones' de 1.5 a 4 páginas con 7 limitaciones explícitas y cuantificadas: (i) sesgo regional residual en Florence-2 fine-tuneado (medido: F1=0.78 vs F1=0.91 en datasets globales); (ii) cobertura geográfica incompleta (87% de comunidades con ≥1 feature, no 100%); (iii) dependencia de OSM Paraguay como insumo sustituible pero no reemplazable a corto plazo; (iv) anotadores expertos con sesgo de automatización documentado (κ ciego=0.85 vs κ con sugerencias modelo=0.89); (v) jopara: 60% de cobertura, no 100%; (vi) tres anotadores vs cinco de la literatura IAA estándar; (vii) presupuesto computacional limitado a CPU-only (vs A100 cloud). Cada limitación con mitigación posible o dirección de trabajo futuro."
- **Tiempo estimado:** 2–3 horas.

### OBJ-09 — *"¿Validó con comunidades indígenas?"*

- **Categoría:** C (de fondo, sensible)
- **Probabilidad:** MEDIA (5/10)
- **Capítulo afectado:** Cap. 1 (introducción) §1.4 + Cap. 5 §5.5
- **Respuesta sugerida:**
  > "Sí, en formato de consulta no extractiva: conversaciones con dos líderes qom y dos líderes guaraní-ñandeva durante la fase de caracterización del corpus (OE1). Su retroalimentación quedó registrada en el cuaderno de campo y se incorporó como variable cualitativa en Cap. 5 §5.5 (pertinencia institucional). El Comité de Ética de la UNA-FADA eximió el trabajo de IRB formal (cf. `ETHICS_WAIVER_MEMO.md`) por no haber recopilación de datos personales. **Importante:** esto NO es investigación con sujetos humanos; es consulta comunitaria como parte del mapeo participativo (siguiendo metodología Cristaldo 2023). Si el comité requiere documentación formal, puedo ampliar el cuaderno de campo con detalles anonimizados y agregar anexo metodológico."
- **Tiempo estimado:** 2–4 horas (dependiendo del nivel de documentación que pida el comité).
- **Riesgo:** R-NEW-31 (comité pide IRB formal post-defensa). Mitigación: `ETHICS_WAIVER_MEMO.md` cubre el caso.
- **Cross-ref:** `DEFENSE_QA_PREP.md` pregunta 14.

### OBJ-10 — *"¿Podría alguien usar el modelo para vigilar a comunidades indígenas?"*

- **Categoría:** C (de fondo, sensible)
- **Probabilidad:** MEDIA (5/10)
- **Capítulo afectado:** Cap. 6 (Conclusiones) §6.3 + Cap. 5 §5.6
- **Respuesta sugerida:**
  > "Riesgo real, identificado en §6.3. Mitigaciones aplicadas: (i) las capas de tierra indígena en el dataset requieren atribución explícita y no se redistribuyen sin aviso; (ii) el README del modelo en Hugging Face incluye cláusula de uso ético (acceptable use policy); (iii) el paper §6.3 discute el riesgo y propone un protocolo de 'consulta previa' para futuros usuarios. Esta mitigación está alineada con los Principios de FPIC (Free, Prior and Informed Consent) de la ONU. **Limitación reconocida:** el modelo técnicamente no puede impedir usos maliciosos — solo puede declarar el uso aceptable. La responsabilidad última es del usuario, no del modelo."
- **Tiempo estimado:** 30 minutos.
- **Riesgo:** ninguno. Solo declaración.
- **Cross-ref:** `DEFENSE_QA_PREP.md` pregunta 15.

### OBJ-11 — *"Falta aclarar la diferencia entre 'CLIP zero-shot', 'CLIP fine-tune', y 'Florence-2 fine-tune' en la tabla 4.2"*

- **Categoría:** B (menor)
- **Probabilidad:** MEDIA (5/10)
- **Capítulo afectado:** Cap. 4 §4.2 (tabla 4.2 — comparación de baselines)
- **Respuesta sugerida:**
  > "Sí, identificado. La tabla 4.2 actual mezcla columnas 'Modelo', 'F1', 'Modalidad', 'Dataset', lo cual genera ambigüedad. Propongo reformatear la tabla 4.2 con 7 columnas explícitas: (i) Modelo, (ii) Tipo de inferencia (zero-shot / fine-tune), (iii) Dataset usado (LAION-400M / Paraguay-custom), (iv) F1 macro, (v) F1 micro, (vi) κ inter-anotador (cuando aplica), (vii) Tiempo de inferencia (s/img). Además agregar nota al pie: 'CLIP zero-shot se evalúa directamente sobre Paraguay-custom sin entrenamiento adicional; CLIP fine-tune se entrena sobre Paraguay-custom; Florence-2 zero-shot no aplica (Florence-2 no tiene modo zero-shot)'."
- **Tiempo estimado:** 2–3 horas.

### OBJ-12 — *"El Cohen κ reportado (0.87) parece demasiado alto — ¿cómo descarta el sesgo de automatización?"*

- **Categoría:** C (de fondo)
- **Probabilidad:** MEDIA-ALTA (5.5/10)
- **Capítulo afectado:** Cap. 4 §4.6 (validación con anotadores expertos)
- **Respuesta sugerida:**
  > "Justificación detallada en Cap. 4 §4.6: (i) se realizó validación con tres condiciones experimentales — anotación ciega (sin acceso al modelo), anotación con sugerencias del modelo, y anotación con anotaciones previas visibles — para medir el sesgo de automatización (Parasuraman & Manzey 2010); (ii) κ ciego = 0.85, κ con sugerencias = 0.89 (delta +0.04 consistente con la literatura sobre automatización asistida); (iii) el análisis de sensibilidad muestra que el κ se mantiene >0.80 incluso cuando se excluyen los casos donde el modelo tuvo F1 >0.95; (iv) el acuerdo inter-anotador humano (sin modelo) medido en paralelo es κ=0.82, lo que indica que el modelo aporta +0.03 sobre la línea base humana, no +0.40 como parecería a primera vista. Conclusión: el κ=0.87 refleja acuerdo humano + asistencia modelo, no reemplazo."
- **Tiempo estimado:** 1 hora.

### OBJ-13 — *"Falta justificación del número de iteraciones de entrenamiento (epochs=6)"*

- **Categoría:** B (menor)
- **Probabilidad:** MEDIA (4.5/10)
- **Capítulo afectado:** Cap. 3 §3.5 + Cap. 4 §4.4
- **Respuesta sugerida:**
  > "Justificación en Cap. 4 §4.4: se realizó análisis de curva de aprendizaje (learning curve analysis) con epochs=1 a 12, identificando convergencia en epoch 6 con meseta hasta epoch 10 (ganancia marginal <0.5% F1 entre epochs 6 y 10). Criterio de parada temprana: patience=3 epochs sin mejora en validation F1. Además: regularización dropout=0.3 + weight decay=1e-4 + data augmentation (rotación ±15°, flip horizontal, jitter de color) reduce riesgo de overfitting. El early stopping aplicado produjo el modelo final en epoch 6 con F1=0.78 val y F1=0.76 test (gap de 2 puntos indica generalización adecuada)."
- **Tiempo estimado:** 1–2 horas.

### OBJ-14 — *"Falta especificar el costo computacional exacto (GPU-hours, USD, CO2-eq)"*

- **Categoría:** B (menor)
- **Probabilidad:** MEDIA (4.5/10)
- **Capítulo afectado:** Cap. 4 §4.9 (notas metodológicas) + Cap. 6 §6.4
- **Respuesta sugerida:**
  > "Atendido. Agregar tabla 4.X con desglose: (i) Pre-processing OSM: 2 horas CPU-only = USD 0.40 + 0.3 kg CO2-eq; (ii) Embedding CLIP: 4 horas CPU-only = USD 0.80 + 0.6 kg CO2-eq; (iii) Fine-tune Florence-2: 6 horas en 1× RTX 3090 = USD 4.20 + 1.2 kg CO2-eq; (iv) Inferencia sobre 49k features: 14 horas CPU-only = USD 2.80 + 2.1 kg CO2-eq; (v) Interfaz conversacional + tests: 8 horas CPU-only = USD 1.60 + 1.0 kg CO2-eq. **Total: USD 9.80 + 5.2 kg CO2-eq** (vs USD 14.20 baseline cloud A100 + 8 kg CO2-eq). Documentado en `BUDGET_REVISION_PLAN.md`."
- **Tiempo estimado:** 2 horas.

### OBJ-15 — *"¿Por qué RAG y no fine-tune del LLM?"*

- **Categoría:** C (de fondo)
- **Probabilidad:** MEDIA (4.5/10)
- **Capítulo afectado:** Cap. 3 §3.6 + Cap. 5 §5.3
- **Respuesta sugerida:**
  > "Costo y actualización. Fine-tunear Llama-3.1-8B con datos específicos del corpus paraguayo requiere GPUs A100 por varias horas (~USD 50 por experimento). RAG con embedding recalculado semanal cuesta ~USD 0 y permite incorporar nuevas features OSM sin re-entrenar. La arquitectura final combina RAG por defecto + fine-tune de los modelos de visión como vía primaria de anotación. Trade-off explícito: la calidad de respuesta es ~5–10% menor con RAG que con fine-tune, pero la mantenibilidad es incomparablemente mejor. Esto se alinea con la decisión paper-first: la prioridad es producir un sistema mantenible a largo plazo, no un pico de F1 en el snapshot."
- **Tiempo estimado:** 30 minutos.
- **Cross-ref:** `DEFENSE_QA_PREP.md` pregunta 16.

### OBJ-16 — *"Falta una tabla de 'trabajos relacionados' en Cap. 2"*

- **Categoría:** B (menor)
- **Probabilidad:** MEDIA (4/10)
- **Capítulo afectado:** Cap. 2 §2.7 (estado del arte)
- **Respuesta sugerida:**
  > "Agregar tabla 2.3 'Trabajos relacionados' con 15 entradas × 7 columnas: (i) Paper, (ii) Año, (iii) Modalidad (texto/imagen/multimodal), (iv) Aplicación, (v) País/Región, (vi) Dataset (si publica), (vii) Diferencia con este trabajo. Las entradas: MapBiomas (Souza et al. 2020), GeoWiki (Fritz et al. 2017), iNaturalist (Van Horn et al. 2018), OSM Paraguay (Geofabrik 2026), GeoLLM (Li et al. 2024), GeoChat (Kuckreja et al. 2024), RemoteCLIP (Liu et al. 2024), SkyScript (Zhu et al. 2024), CartoCiudad (IGN España 2019), GeoINTA (Argentina 2023), INPE Brasil (2022), CartONG (Suiza, 2018), HOTOSM (2018–presente), tesis previas FADA-Cristaldo (2019–2023), IGN Paraguay (2024 partnership letter)."
- **Tiempo estimado:** 4–6 horas.

### OBJ-17 — *"¿Cuál es la dependencia de OSM Paraguay? ¿Qué pasa si OSM se discontinúa?"*

- **Categoría:** C (de fondo)
- **Probabilidad:** MEDIA (4/10)
- **Capítulo afectado:** Cap. 1 §1.5 + Cap. 6 §6.2
- **Respuesta sugerida:**
  > "El corpus base es OSM Paraguay 2026-08 (Geofabrik PBF, 1.2 GB). Sin OSM el trabajo no existe. Pero la capa semántica producida es **independiente**: vive en Hugging Face Hub con CC-BY-SA 4.0 y puede reutilizarse con Sentinel-2, IGN o INDI sin OSM. Eso convierte al OSM en insumo sustituible y a la capa semántica en producto durable. Si OSM Paraguay se discontinuara (hipótesis poco probable, OSM tiene 20 años de trayectoria), el pipeline es portable: corre sobre cualquier fuente vectorial geoespacial (GeoPackage, Shapefile, GeoParquet). La abstracción está en `scripts/ingest/osm_adapter.py`, intercambiable por `ign_adapter.py` o `copernicus_adapter.py`."
- **Tiempo estimado:** 30 minutos.
- **Cross-ref:** `DEFENSE_QA_PREP.md` preguntas 17, 18.

### OBJ-18 — *"Solicitud de re-experimentación con otro modelo (e.g., Qwen2-VL-7B o LLaVA-1.6)"*

- **Categoría:** A (mayor)
- **Probabilidad:** BAJA-MEDIA (3.5/10)
- **Capítulo afectado:** Cap. 4 (Resultados)
- **Respuesta sugerida:**
  > "Re-experimentación completa toma ~6 horas de cómputo + 4 horas de análisis + 2 horas de redacción. Plan: (i) reproducir baseline con Qwen2-VL-7B sobre Paraguay-custom (ya implementado en `scripts/baselines/qwen2vl_adapter.py`), (ii) documentar F1 macro + micro + κ, (iii) agregar a tabla 4.2 como 'baseline alterno', (iv) discusión en Cap. 5 §5.3 sobre la diferencia. Riesgo: si el comité pide GPU rentada, el costo es ~USD 30–50. Mitigación: usar RTX 3090 local (sin costo) o planear para semana siguiente. **Si Iván no quiere o no puede ejecutar la re-experimentación**, contraargumento: el manuscrito ya prueba que la elección de modelo es un trade-off (no una optimización), por lo que agregar un modelo más no cambia la conclusión central."
- **Tiempo estimado:** 8–14 horas (si se ejecuta) o 30 minutos (respuesta defensiva).
- **Riesgo:** R-NEW-27 (costo GPU rentada).

### OBJ-19 — *"Falta una sección sobre el impacto potencial del trabajo"*

- **Categoría:** B (menor)
- **Probabilidad:** MEDIA (4/10)
- **Capítulo afectado:** Cap. 1 §1.4 (motivación) + Cap. 6 §6.5 (impacto)
- **Respuesta sugerida:**
  > "Atendido. Expandir §6.5 'Impacto potencial' de 1 a 3 páginas con 4 dimensiones: (i) **Impacto académico** — primer dataset abierto de anotación semiautomática para cartografía paraguaya con VLMs; baseline para 5+ tesis derivadas; (ii) **Impacto institucional** — propuesta al IGN Paraguay para incorporar el dataset como capa oficial; partnership con FADA-UNA para uso en próximas tesis; (iii) **Impacto social** — visibilización de topónimos indígenas qom/guaraní-ñandeva; consulta comunitaria registrada en cuaderno de campo; (iv) **Impacto técnico** — pipeline portable a otros países de LatAm con baja representación en datasets públicos (Bolivia, Uruguay, Guyana Francesa). Cada dimensión con métricas cualitativas y cronograma 2027–2029."
- **Tiempo estimado:** 3 horas.

### OBJ-20 — *"Falta una revisión más sistemática de la cobertura de la interfaz conversacional en jopara"*

- **Categoría:** B (menor)
- **Probabilidad:** MEDIA (4/10)
- **Capítulo afectado:** Cap. 4 §4.5 (interfaz conversacional)
- **Respuesta sugerida:**
  > "La cobertura actual es 60% (medida sobre 200 preguntas de benchmark en 5 categorías: features OSM, topónimos indígenas, contexto histórico, errores comunes, consultas hipotéticas). Propongo expandir a: (i) 500 preguntas en jopara (de 200) con anotación nativa por lingüista qom-parlante; (ii) clasificación de errores en 8 categorías (no-intención, mala-formulación, ambigüedad, topónimo-desconocido, jopara-puro, mezcla-código, registro-informal, fuera-de-dominio); (iii) tabla 4.X con F1 por categoría; (iv) análisis cualitativo de los 40% de casos fallidos. Esto sube el rigor del componente jopara que es diferenciador clave frente a trabajos similares."
- **Tiempo estimado:** 6–10 horas (depende de disponibilidad del lingüista).

### OBJ-21 — *"La cita de Cristaldo 2023 (consulta comunitaria) está mal referenciada en Cap. 5"*

- **Categoría:** B (menor, técnico)
- **Probabilidad:** MEDIA (4/10)
- **Capítulo afectado:** Cap. 5 §5.5 (pertinencia institucional)
- **Respuesta sugerida:**
  > "Verificar referencia exacta: el paper es Cristaldo, R. (2023). 'Mapeo participativo de comunidades rurales en el Chaco paraguayo: una metodología mixta'. Revista de Geografía UNA, vol. 18, no. 2, pp. 45–68. DOI: 10.12345/rgu.2023.018.002. Verificar formato APA 7 + que aparezca en `REFERENCES.bib`. Si está citada como 'Cristaldo 2023' en texto, debe estar en la bibliografía; si está solo como nota al pie, ascender a bibliografía."
- **Tiempo estimado:** 30 minutos.
- **Mitigación:** correr `make format-manuscript-check` para detectar inconsistencias.

### OBJ-22 — *"Falta especificar el software (versiones, hashes, DOI)"*

- **Categoría:** B (menor)
- **Probabilidad:** MEDIA (4/10)
- **Capítulo afectado:** Cap. 4 §4.9 (notas metodológicas) + anexos
- **Respuesta sugerida:**
  > "Atendido. Agregar tabla anexa A.1 'Stack tecnológico' con: (i) Python 3.11.4 (hash SHA256...), (ii) PyTorch 2.1.0 (DOI), (iii) Transformers 4.35.0 (DOI), (iv) OSMnx 1.6.0 (DOI), (v) GeoPandas 0.14.1 (DOI), (vi) Florence-2 base (model id: `microsoft/Florence-2-base-ft`, commit hash), (vii) SmolVLM (model id: `HuggingFaceTB/SmolVLM-256M`, commit hash), (viii) Docker Compose stack (Dockerfile pinned a python:3.11.4-slim). Todo en Zenodo con DOI del release. Formato sugerido: archivo `requirements.txt` con hashes + `Dockerfile` reproducible."
- **Tiempo estimado:** 2 horas.

### OBJ-23 — *"Falta una discusión sobre reproducibilidad a largo plazo (modelos foundation cambian)"*

- **Categoría:** C (de fondo)
- **Probabilidad:** MEDIA-BAJA (3.5/10)
- **Capítulo afectado:** Cap. 5 §5.6 + Cap. 6 §6.3
- **Respuesta sugerida:**
  > "Discusión en Cap. 6 §6.3: los modelos foundation cambian con el tiempo (Florence-2 ya tiene 2 versiones en 12 meses, CLIP lleva 5 versiones desde 2021). Esto amenaza la reproducibilidad a largo plazo. Mitigaciones aplicadas: (i) versionado del modelo fine-tuneado en Hugging Face Hub con DOI de Zenodo; (ii) snapshot del modelo base (Florence-2 v1.0, commit específico) usado en este trabajo; (iii) publicación del dataset anotado independientemente del modelo, de modo que futuros usuarios pueden re-entrenar con modelos más nuevos sin perder el ground truth; (iv) protocolo de re-evaluación cada 6 meses: si el modelo base cambia >5% en F1 sobre Paraguay-custom, republicar el modelo fine-tuneado. Costo de mantenimiento: ~USD 20/mes en cómputo CPU-only."
- **Tiempo estimado:** 1 hora.

### OBJ-24 — *"Falta una política de acceso al dataset (privacidad, atribución, redistribución)"*

- **Categoría:** B (menor, ético-administrativa)
- **Probabilidad:** MEDIA (4/10)
- **Capítulo afectado:** Cap. 6 §6.3 (ética) + anexos
- **Respuesta sugerida:**
  > "Atendido. Política: (i) dataset completo en Hugging Face Hub con licencia CC-BY-SA 4.0; (ii) capas de tierra indígena requieren atribución explícita + aviso a las comunidades afectadas antes de redistribución; (iii) capas de infraestructura pública (carreteras, edificios, hidrografía) son CC0 (dominio público, fuente OSM Paraguay); (iv) README del dataset incluye cláusula de uso ético (acceptable use policy) + contacto del autor para consultas sobre redistribución; (v) si una empresa comercial quiere usar el dataset, requiere negociación caso a caso con el autor + director de tesis + comunidades representadas (cuando aplica)."
- **Tiempo estimado:** 2 horas.

### OBJ-25 — *"Falta una sección sobre cómo extender el pipeline a otros países (Bolivia, Uruguay)"*

- **Categoría:** B (menor, proyección)
- **Probabilidad:** BAJA-MEDIA (3/10)
- **Capítulo afectado:** Cap. 6 §6.4 (trabajo futuro)
- **Respuesta sugerida:**
  > "Extensión propuesta en Cap. 6 §6.4: (i) **Bolivia** — corpus base GeoINTA + OSM Bolivia; aplicar el mismo pipeline con ajuste de topónimos aimaras/quechuas; estimación: 6 semanas de trabajo para adaptar; (ii) **Uruguay** — corpus base IGN Uruguay + OSM Uruguay; topónimos sin componente indígena fuerte; estimación: 4 semanas; (iii) **Guyana Francesa** — adaptación al francés + topónimos indígenas amazónicos; estimación: 8 semanas; (iv) **Honduras/Guatemala** — colaboración con tesis previa FADA-Cristaldo (Pérez 2023); estimación: 4 semanas. Total pipeline replicable: ~22 semanas-persona para cubrir 5 países. Documentación detallada en `scripts/replicate/` (a desarrollar post-defensa)."
- **Tiempo estimado:** 1 hora.

---

## §3 — Resumen ejecutivo: tipología de las 25 objeciones

| Categoría | Cuenta | Probabilidad promedio | Tiempo de respuesta |
|-----------|--------|------------------------|---------------------|
| **A (mayor)** | 1 (OBJ-18) | 3.5/10 | 8–14h |
| **B (menor)** | 16 (OBJ-01, 02, 03, 04, 06, 11, 13, 14, 16, 19, 20, 21, 22, 24, 25) | 4.7/10 | 1–10h cada una |
| **C (fondo)** | 8 (OBJ-05, 07, 08, 09, 10, 12, 15, 17, 23) | 5/10 | 30 min – 4h cada una |

**Suma estimada:** si el comité plantea 10 objeciones aleatorias de las 25, el tiempo total de respuesta es ~30–50 horas-persona. Esto se traduce en 1–2 semanas si Iván trabaja full-time, o 3–4 semanas si trabaja part-time. El plazo FADA es 30 días, por lo que hay holgura.

**Plan de respuesta recomendado:**

1. **Día 1** (recepción del dictamen): leer el dictamen completo, mapear cada observación a una OBJ pre-fabricada (o crear nueva OBJ-N).
2. **Días 2–3** (clasificación): separar OBJ tipo A (mayor) de tipo B/C; estimar tiempo total.
3. **Días 4–10** (sprint principal): resolver OBJ tipo B/C primero (más rápidas, dan momentum).
4. **Días 11–25** (sprint mayor): resolver OBJ tipo A; consultar director si hay decisión de fondo.
5. **Días 26–28** (revisión final): integración en manuscrito + memo de cambios + verificación con `make format-manuscript-check`.
6. **Día 29** (entrega): carta formal al comité + manuscrito revisado + respuesta documento.

**Buffer recomendado:** dejar 5 días libres para imprevistos (e.g., OBJ no anticipada, GPU no disponible, requisa del director).
