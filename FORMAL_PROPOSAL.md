# PROPUESTA FORMAL — Sustrato de la tesis UNA-FADA

> **🌍 Contexto cross-repo (2026-08-15):** Este doc fue escrito originalmente como propuesta para la tesis "P1 GeoData v2" (standalone). Tras revisión, **este repo es el sustrato de la tesis** — la tesis en sí vive en [`IvanWeissVanDerPol/satellite-paraguay`](https://github.com/IvanWeissVanDerPol/satellite-paraguay), titulada *"Multi-Temporal Satellite Computer Vision for Paraguay"*. Ver [`THESIS_ARCHITECTURE.md`](THESIS_ARCHITECTURE.md) para el mapa cross-repo.

**Subtítulo de este doc:** Propuesta del lado sustrato — adquisición de datos + anotación + web app.

**Title (Spanish):** *Anotación semiautomática con modelos multimodales del corpus cartográfico abierto de Paraguay y prototipo de interfaz conversacional para la reflexión territorial sudamericana*

**Title (English):** *Semi-automated annotation with multimodal foundation models of Paraguay's open cartographic corpus and a prototype conversational interface for South American territorial reflection*

**Author:** Iván Weiss Van der Pol
**Faculty (proposed):** FADA (Maestría en Tecnología de la Arquitectura) — primary; FP-UNA (Ing. Informática) — co-affiliation
**Date:** 2026-08-10
**Status:** Draft, ready for advisor co-sign after manuscript completion

---

## 1. Planteamiento del problema

Paraguay cuenta con una cobertura cartográfica abierta creciente — OpenStreetMap (OSM) con 49.641 edificios y 14.835 carreteras catalogadas (Geofabrik 2026 extract), tiles raster del Instituto Geográfico Nacional (IGN), e imágenes Sentinel-2 del programa Copernicus (EU). Sin embargo, **el proceso de anotación semántica sigue siendo mayoritariamente manual** y existe un cuello de botella entre la disponibilidad de datos crudos y su utilidad para la reflexión territorial, la planificación urbana, y la investigación académica paraguaya.

La FADA-UNA ha desarrollado una línea de investigación de 4 tesis (2019, 2019, 2021, 2023) sobre cartografía abierta y mapeo participativo (director: Ing. Juan Carlos Cristaldo), pero **ninguna ha incorporado modelos multimodales de visión-lenguaje** para automatizar la anotación o construir interfaces conversacionales sobre el corpus cartográfico.

## 2. Pregunta de investigación

> *¿Es viable anotar semánticamente el corpus cartográfico abierto de Paraguay mediante modelos multimodales de visión-lenguaje (CLIP, SAM, GroundingDINO, Florence-2, Llama-3.2-Vision) con un acuerdo inter-anotador ≥ 0.85 (Cohen's κ), y construir un prototipo de interfaz conversacional en lenguaje natural que devuelva respuestas anotadas a preguntas territoriales en español paraguayo y jopara?*

## 3. Hipótesis

### H1 (principal)
> Un modelo visión-lenguaje ajustado (fine-tuned) sobre el corpus cartográfico abierto paraguayo alcanza un acuerdo inter-anotador **Cohen's κ ≥ 0.85** frente a anotadores expertos en una muestra de 200 features, superando el baseline CLIP-zero-shot (κ esperado ≤ 0.60) por al menos 0.25 puntos.

### H2 (secundaria)
> Una interfaz conversacional basada en un agente LLM (Llama-3.1-8B con retrieval-augmented generation sobre el corpus anotado) alcanza una **tasa de respuesta correcta ≥ 75%** en un benchmark de 100 preguntas territoriales en español paraguayo.

### H3 (terciaria)
> El fine-tune reduce el costo computacional de anotación **≥ 80%** comparado con anotación manual, manteniendo la calidad (misma κ).

## 4. Objetivos

### 4.1 Objetivo general
Construir un pipeline reproducible de anotación semiautomática y una interfaz conversacional para el corpus cartográfico abierto paraguayo, publicando el dataset, los pesos del modelo y la aplicación web como artefactos abiertos.

### 4.2 Objetivos específicos

1. **OE1.** Caracterizar el corpus cartográfico abierto de Paraguay (OSM + IGN + Sentinel-2 + INDI) en volumen, actualidad, cobertura y licencia. *Mes 1-2.*
2. **OE2.** Construir un dataset anotado de ≥ 10.000 features cartográficas con etiquetas semánticas (tipo de carretera, material constructivo, clase de uso de suelo) usando SAM + GroundingDINO + validación humana. *Mes 2-4.*
3. **OE3.** Ajustar (fine-tune) un modelo visión-lenguaje pequeño (SmolVLM-256M o Florence-2-base) sobre el dataset OE2, publicando los pesos en Hugging Face. *Mes 4-5.*
4. **OE4.** Construir una aplicación web pública *"Pregúntale al mapa del Paraguay"* (Next.js 16 + Tailwind v4) que consuma el modelo OE3 + un agente LLM (Llama-3.1-8B-Instruct con RAG) y permita preguntas en lenguaje natural. *Mes 5-6.*
5. **OE5.** Validar con 3 anotadores expertos en una muestra de 200 features (Cohen's κ), medir el rendimiento en el benchmark de 100 preguntas, y publicar un paper en arxiv + envío a conferencia Q1/Q2 (ICA 2027, ACM SIGSPATIAL 2027, ISPRS 2027). *Mes 6-7.*

## 5. Marco teórico (resumen)

- **Cartografía crítica del Sur Global.** Línea oficial FADA (Res. 1141/2022): *"producir capacidades en cartografía con software libre que permitan producir no solo datos, sino capacidades locales para la reflexión y la gestión territorial."*
- **Visión-lenguaje multimodal.** Fundamentos: CLIP (Radford 2021), SAM (Kirillov 2023), GroundingDINO (Liu 2023), Florence-2 (Xiao 2023), SmolVLM (Marafioti 2024).
- **Retrieval-Augmented Generation (RAG).** Lewis 2020, con adaptaciones para datos geoespaciales estructurados (Bommasani 2022 on foundation models).
- **Estado del arte en Paraguay.** Cristaldo 2019/2019/2021/2023 (4 tesis, sin uso de foundation models); INDEC Paraguay (no aplica); MOPC (sin publicación académica).

## 6. Metodología (resumen)

### 6.1 Tipo de investigación
- **Descriptiva-aplicada** con componente experimental (benchmark vs. baseline) y componente de desarrollo de software (pipeline + aplicación web).

### 6.2 Fases (cronograma 7 meses)
1. **M1-2 — Caracterización del corpus.** Extracción OSM (Geofabrik), descarga IGN (WMS), Sentinel-2 (Copernicus), INDI (GeoJSON público).
2. **M2-4 — Anotación.** Pipeline SAM → GroundingDINO → validación humana sobre ~10K features.
3. **M4-5 — Fine-tune.** QLoRA sobre SmolVLM-256M o Florence-2-base. Publicación en Hugging Face.
4. **M5-6 — Aplicación web.** Next.js + Llama-3.1-8B-Instruct + RAG sobre el corpus anotado.
5. **M6-7 — Validación + paper.** Cohen's κ, benchmark de 100 preguntas, draft arxiv + envío a conferencia.

### 6.3 Técnicas e instrumentos
- **Software:** Python 3.13, Ultralytics (YOLO), transformers (HuggingFace), rasterio, geopandas, Next.js 16, Tailwind v4, LangChain.
- **Hardware:** GPU única (RTX 4090 o A100 rented ~$1.5/h × 80h = $120 total). Reproducible en Colab Pro / Lambda Labs / SageMaker.
- **Evaluación:** Cohen's κ inter-anotador, F1 macro por clase, exactitud top-1 sobre benchmark de 100 preguntas, latencia p95 de la interfaz conversacional.

### 6.4 Análisis estadístico
- **Cuantitativo.** Cohen's κ con IC 95%, bootstrap 1000 iteraciones, ANOVA para comparar 3 modelos (CLIP-zero-shot, SmolVLM-finetuned, Florence-2-finetuned).
- **Cualitativo.** Análisis temático de las preguntas del benchmark y de las respuestas del agente (2 revisores independientes).

## 7. Contribuciones esperadas

1. **Dataset abierto.** ~10K features cartográficas paraguayas anotadas, publicado en Hugging Face + Zenodo con DOI.
2. **Modelo abierto.** Pesos fine-tuned de SmolVLM o Florence-2 sobre Paraguay, publicado en Hugging Face.
3. **Aplicación web pública.** *paraguay-mapa.paragu-ai.com* (o dominio equivalente), accesible sin autenticación.
4. **Paper Q1/Q2.** Pre-print arxiv + envío a ICA 2027 o ACM SIGSPATIAL 2027.
5. **Reproducibilidad.** Docker bundle + seeds + scripts en repo público.

## 8. Viabilidad

- **Datos:** 100% accesibles sin permisos. OSM (ODbL), IGN (público), Sentinel-2 (gratuito), INDI (público).
- **Ética:** exento (sin sujetos humanos). Ver `ETHICS_WAIVER_MEMO.md`.
- **Costo:** ~$200-800 total (GPU + dominio + hosting). Ver `THESIS_COST_BREAKDOWN.md` del repo `thesis-research`.
- **Tiempo:** 7 meses para arxiv-ready. 12 meses para defensa UNA-FADA.
- **Conocimientos previos:** Python, Docker, ML básico. Existe repo `paraguay-geodata` con datos y scripts base.

## 9. Limitaciones esperadas

- Cobertura OSM en zonas rurales del Chaco es ~30% menor que en zonas urbanas; se reportará esta asimetría.
- Fine-tune sobre un único país limita transferibilidad; se evaluará transfer a Bolivia/Uruguay como trabajo futuro.
- Benchmark de 100 preguntas es reducido; el paper公开ará el protocolo para ampliación comunitaria.

## 10. Referencias clave (a expandirse en Cap. 2)

- Radford et al. (2021). *Learning Transferable Visual Models From Natural Language Supervision* (CLIP). ICML.
- Kirillov et al. (2023). *Segment Anything*. ICCV.
- Liu et al. (2023). *GroundingDINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection*. arXiv:2303.05499.
- Xiao et al. (2023). *Florence-2: Advancing a Unified Representation for a Variety of Vision Tasks*. arXiv:2311.06242.
- Marafioti et al. (2024). *SmolVLM: Towards Smaller Multimodal Models*. arXiv.
- Lewis et al. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. NeurIPS.
- Cristaldo, J. C. (2019, 2019, 2021, 2023). Cuatro tesis de cartografía abierta, FADA-UNA.

---

**Próximo paso:** este documento se presenta al comité TFG UNA-FADA una vez que el manuscrito y el paper estén terminados (estrategia paper-first). No requiere firma de advisor antes del trabajo; la firma se solicita al finalizar.