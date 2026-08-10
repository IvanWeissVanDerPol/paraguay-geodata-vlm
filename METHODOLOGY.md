# METHODOLOGY — P1 GeoData v2

**Thesis:** Anotación semiautomática con modelos multimodales del corpus cartográfico abierto de Paraguay
**Author:** Iván Weiss Van der Pol
**Date:** 2026-08-10
**Status:** Chapter 3 skeleton (Cap. III — Marco Metodológico)

---

## 3.1 Tipo de investigación

**Descriptiva-aplicada con componente experimental.**

- **Descriptiva:** caracterización del corpus cartográfico abierto de Paraguay (OE1).
- **Aplicada:** construcción de un pipeline reproducible + aplicación web pública (OE2-OE4).
- **Experimental:** comparación cuantitativa entre modelos (CLIP-zero-shot vs. SmolVLM-finetuned vs. Florence-2-finetuned) sobre métricas estandarizadas (Cohen's κ, F1 macro, accuracy top-1) (OE5).

## 3.2 Paradigma

**Mixto cuantitativo-cualitativo con predominio cuantitativo.** El componente cuantitativo evalúa el rendimiento de los modelos; el cualitativo analiza temáticamente las respuestas del agente conversacional.

## 3.3 Diseño

**Cuasi-experimental con grupo control (CLIP-zero-shot como baseline) y dos grupos experimentales (SmolVLM-fine-tuned, Florence-2-fine-tuned).** Variables independientes controladas: arquitectura del modelo, cantidad de datos de entrenamiento, prompt template.

## 3.4 Unidad de análisis

**Features cartográficas individuales** (highways, buildings, land-use polygons, indigenous territories). Total esperado: 10.000 features anotadas para entrenamiento + 200 features para validación inter-anotador + 100 preguntas para benchmark conversacional.

## 3.5 Población y muestra

- **Población:** todas las features cartográficas abiertas disponibles para Paraguay en OSM + IGN + Sentinel-2 + INDI + MOPC.
- **Muestra de entrenamiento:** 10.000 features estratificadas por categoría nivel-1 (proporcional a la distribución del corpus; sobre-muestreo de clases raras si necesario).
- **Muestra de validación inter-anotador:** 200 features, submuestreo estratificado.
- **Muestra para benchmark conversacional:** 100 preguntas distribuidas en 5 categorías temáticas (transporte, vivienda, uso de suelo, recursos hídricos, territorio indígena).

## 3.6 Variables

### Independientes (manipuladas)
- **Arquitectura del modelo:** CLIP-zero-shot, SmolVLM-256M-finetuned, Florence-2-base-finetuned.
- **Cantidad de datos de entrenamiento:** 1K, 5K, 10K features (curva de aprendizaje).
- **Prompt template:** mínimo vs. detallado.

### Dependientes (medidas)
- **Cohen's κ inter-anotador** (validación de calidad de anotación).
- **F1 macro** por clase nivel-2.
- **Accuracy top-1** sobre benchmark de 200 features held-out.
- **Tasa de respuesta correcta** del agente conversacional (100 preguntas).
- **Latencia p95** de la interfaz web (segundos).

### Controladas
- Semilla aleatoria (42 para todos los experimentos).
- Versiones exactas de Python 3.13, transformers 4.45, PyTorch 2.4.
- GPU única (RTX 4090 24 GB rented, Lambda Labs $1.5/h).
- Resolución de imagen de entrada (256×256 para CLIP, 384×384 para Florence-2).

### Extrañas
- Variabilidad de cobertura OSM (zonas rurales < urbanas).
- Diferencias estacionales en Sentinel-2 (verano vs. invierno chaqueño).
- Sesgo del anotador (mitigado con 2-3 anotadores + κ).

## 3.7 Instrumentos y técnicas

### 3.7.1 Software
| Componente | Versión | Función |
|---|---|---|
| Python | 3.13 | Lenguaje base |
| PyTorch | 2.4 | Framework de deep learning |
| transformers (HuggingFace) | 4.45 | Carga de CLIP, Florence-2, SmolVLM |
| Ultralytics | 8.2 | YOLOv8 para detección baseline |
| rasterio | 1.3 | Lectura/escritura raster |
| geopandas | 0.14 | Manipulación vectorial |
| osmium | 3.4 | Parser OSM |
| Label Studio | 1.8 | UI de anotación humana |
| Next.js | 16 | Framework web |
| Tailwind CSS | 4 | Estilos |
| LangChain | 0.3 | Orquestación LLM |
| Ollama | 0.3 | LLM local (Llama-3.1-8B) |
| Docker | 27 | Reproducibilidad |

### 3.7.2 Hardware
- **GPU:** NVIDIA RTX 4090 24 GB (alquilada en Lambda Labs ~$1.5/h) — 80 horas = $120 total
- **CPU:** 16 cores x86_64
- **RAM:** 64 GB
- **Almacenamiento:** 500 GB SSD (raw + processed)
- **Alternativa gratuita:** Google Colab Pro ($10/mes) para experimentación inicial

### 3.7.3 Técnicas

#### a) Extracción y preprocesamiento
- OSM: `osmium extract` y `osmium export` para GeoJSON.
- IGN: `owslib` para WMS → GeoTIFF vía `gdal_translate`.
- Sentinel-2: `sentinelsat` para búsqueda + descarga; `s2cloudless` para máscara de nubes.
- INDI: descarga directa GeoJSON.

#### b) Anotación
- **Fase automática (10K features).** Pipeline:
  1. SAM → máscaras de objetos en raster
  2. GroundingDINO → propuestas de clase ("highway", "building", "forest")
  3. CLIP → score de similitud clase-propuesta
  4. Threshold 0.7 → aceptado; < 0.7 → marcado para revisión humana
- **Fase humana (Label Studio).** 2-3 anotadores validan las propuestas automáticas sobre el 30% del dataset (3K features) y corrigen las < 0.7. Tiempo estimado: ~50 horas-anotador total.

#### c) Fine-tuning
- **SmolVLM-256M.** QLoRA con rank=16, alpha=32, lr=2e-4, 3 epochs, batch=8.
- **Florence-2-base.** QLoRA con rank=16, alpha=32, lr=1e-4, 5 epochs, batch=4.
- **Baseline:** CLIP ViT-B/32 zero-shot (sin fine-tune).
- **Métrica durante entrenamiento:** F1 macro sobre validation set (10% del total).

#### d) Validación inter-anotador
- 200 features con doble-anotación.
- **Cohen's κ** con IC 95%, bootstrap 1000 iteraciones.
- **Target:** κ ≥ 0.85 (sustancialmente de acuerdo).

#### e) Benchmark conversacional
- 100 preguntas redactadas por el autor, validadas por 2 revisores.
- Categorías: 20 transporte, 20 vivienda, 20 uso de suelo, 20 hídrico, 20 indígena.
- Evaluación: 2 revisores independientes califican respuesta como correcta/parcial/incorrecta (κ target ≥ 0.70).

#### f) Análisis estadístico
- **Cuantitativo.** ANOVA de una vía para comparar 3 modelos en F1 macro. Post-hoc Tukey HSD. α = 0.05.
- **Bootstrap.** IC 95% para κ y accuracy top-1.
- **Cualitativo.** Análisis temático de respuestas del agente (Braun & Clarke 2006). 2 codificadores independientes.

## 3.8 Procedimiento

### Fase 1 — M1-2: Caracterización del corpus
1. Descargar datasets D1-D9 según `DATA_MANIFEST.md`.
2. Calcular estadísticas descriptivas: número de features por categoría, cobertura espacial, actualidad.
3. Documentar calidad por dataset (completitud, exactitud reportada por la fuente).
4. **Entregable:** `corpus_characterization_report.pdf` + tabla en `data/processed/stats.json`.

### Fase 2 — M2-4: Anotación
1. Implementar pipeline SAM + GroundingDINO + CLIP (`scripts/auto_annotate.py`).
2. Correr sobre el corpus. Generar 10K propuestas automáticas.
3. Configurar Label Studio para revisión humana.
4. Anotadores revisan 3K features (las de baja confianza automática).
5. Exportar dataset anotado a `data/processed/annotations_v1.geojson` + Hugging Face Hub.

### Fase 3 — M4-5: Fine-tune
1. Split 80/10/10 (train/val/test).
2. Fine-tune SmolVLM-256M con QLoRA.
3. Fine-tune Florence-2-base con QLoRA.
4. Evaluar en test set: F1 macro, accuracy top-1, confusion matrix.
5. Publicar pesos en Hugging Face Hub con model card.

### Fase 4 — M5-6: Aplicación web
1. Construir backend FastAPI que carga el modelo fine-tuned + Llama-3.1-8B-Instruct vía Ollama.
2. Implementar RAG: índice vectorial (Chroma) sobre el dataset anotado.
3. Construir frontend Next.js 16 con Tailwind v4.
4. Deploy en VPS Paraguay (`paraguay-mapa.paragu-ai.com`).
5. Documentar API en `docs/API.md`.

### Fase 5 — M6-7: Validación + paper
1. Validación inter-anotador (200 features, κ).
2. Benchmark conversacional (100 preguntas, 2 revisores).
3. Análisis estadístico completo.
4. Draft paper (8 páginas, formato ICA 2027 o ACM SIGSPATIAL 2027).
5. Pre-print arxiv.
6. Envío a conferencia.

## 3.9 Consideraciones éticas

Sin sujetos humanos. Exento de revisión ética. Ver `ETHICS_WAIVER_MEMO.md`.

## 3.10 Limitaciones del diseño

- **Cobertura OSM rural.** Menor en Chaco; se reportará por departamento.
- **Idioma del agente conversacional.** Optimizado para español paraguayo estándar; jopara será stretch goal.
- **Comparación limitada a 3 modelos.** No se incluyen LLMs multimodales grandes (GPT-4V, Gemini) por costo y reproducibilidad.
- **Dataset de validación pequeño.** 200 features para κ puede no capturar variabilidad completa; bootstrap mitiga.

## 3.11 Cronograma

| Mes | Fase | Entregable principal |
|---|---|---|
| 1 | Extracción + caracterización | corpus_characterization_report.pdf |
| 2 | Pipeline anotación auto | auto_annotated_v1.geojson |
| 3 | Anotación humana | human_reviewed_v1.geojson |
| 4 | Fine-tune SmolVLM + Florence-2 | modelo_v1 en HF Hub |
| 5 | App web + RAG | paraguay-mapa deployado |
| 6 | Validación completa | validation_report.pdf |
| 7 | Paper draft + arxiv | arxiv preprint + submission |

**Total: 7 meses hasta arxiv-ready. +5 meses hasta defensa UNA.**

---

**Próximo paso:** implementar `scripts/fetch_data.sh` y `scripts/auto_annotate.py` durante las semanas 1-2.