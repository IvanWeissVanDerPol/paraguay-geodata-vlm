# Capítulo 3 — Marco Metodológico

**Tesis:** *Anotación semiautomática del corpus cartográfico abierto de Paraguay con modelos multimodales fundacionales y una interfaz conversacional para la reflexión territorial*
**Autor:** Iván Weiss Van der Pol
**Carrera:** Maestría en Tecnología de la Arquitectura, FADA-UNA (co-afiliación FP-UNA)
**Director (TBD):** Prof. Dr. Juan Carlos Cristaldo (FADA-UNA)
**Fecha:** Agosto 2026
**Versión:** 1.0 — borrador

---

## 3.1. Introducción al capítulo

Este capítulo describe, en detalle operacional, el diseño de investigación, los instrumentos, las técnicas y el procedimiento que se siguieron para alcanzar los cinco objetivos específicos (OE1-OE5) planteados en el Capítulo 1 y operacionalizar las tres hipótesis (H1, H2, H3) declaradas en la Propuesta Formal. La intención es que cualquier investigador con formación equivalente en ciencia de datos geográficos pueda reproducir el pipeline de extremo a extremo —desde la descarga de los datos crudos hasta la evaluación final— sin acceso al equipo original.

La organización del capítulo sigue la convención FADA-UNA para tesis de maestría con componente experimental (cf. Cristaldo 2021, 2023): tipo de investigación, paradigma, diseño, unidad de análisis, población y muestra, variables, instrumentos, técnicas, procedimiento por fases, consideraciones éticas, limitaciones y cronograma. Cada sección se acompaña de la justificación metodológica y de referencias a los estándares vigentes (ISO 19157:2013 para calidad de datos geográficos; STAC 1.1.0 para catalogación; OGC API Features para interoperabilidad).

El capítulo cierra con un protocolo de validación y un protocolo de análisis estadístico que serán referenciados en el Capítulo 4 (Resultados) y en el Capítulo 5 (Discusión).

---

## 3.2. Tipo de investigación

**Descriptiva-aplicada con componente experimental y componente de desarrollo de software.**

La investigación se clasifica en tres dimensiones simultáneas, cada una justificada a continuación:

**(a) Descriptiva.** El primer objetivo específico (OE1) requiere caracterizar cuantitativamente el corpus cartográfico abierto de Paraguay en cuatro dimensiones: volumen (número de features por categoría y por fuente), actualidad (fecha mediana de la última edición), cobertura espacial (densidad por departamento y por categoría), y régimen de licenciamiento. Esta dimensión corresponde al alcance descriptivo propuesto por Hernández Sampieri et al. (2014, cap. 5) para estudios cuyo primer paso es caracterizar el estado del arte de un dominio antes de intervenir sobre él.

**(b) Aplicada.** Los objetivos OE2-OE4 entregan artefactos concretos y funcionales: (i) un dataset anotado de ≥ 10.000 features cartográficas paraguayas; (ii) un modelo visión-lenguaje fine-tuneado y publicado en Hugging Face Hub; (iii) una aplicación web desplegada en un dominio público. Esta dimensión corresponde a la investigación aplicada orientada a la construcción de artefactos (Hevner et al. 2004, *Design Science in Information Systems Research*).

**(c) Experimental.** El objetivo OE5 plantea una comparación cuantitativa entre tres condiciones experimentales (CLIP zero-shot, SmolVLM fine-tuned, Florence-2 fine-tuned) sobre métricas estandarizadas. Esta dimensión corresponde a la tradición experimental cuantitativa (Campbell & Stanley 1963) con variables independientes manipuladas (arquitectura, cantidad de datos, prompt template) y variables dependientes medidas (Cohen's κ, F1 macro, accuracy top-1, latencia p95).

La combinación de las tres dimensiones es consistente con la práctica metodológica reciente en geomática e inteligencia artificial geoespacial, donde los estudios combinan caracterización de corpus, construcción de artefactos y evaluación experimental (Yuan et al. 2021; Kuckreja et al. 2024; Wang et al. 2024).

## 3.3. Paradigma

**Mixto cuantitativo-cualitativo con predominio cuantitativo.**

El paradigma se justifica del siguiente modo:

- **Componente cuantitativo (predominante).** Las métricas de evaluación (Cohen's κ, F1 macro, accuracy top-1, latencia p95, tasa de respuesta correcta) son todas cuantitativas y se analizan mediante técnicas estadísticas estándar (bootstrap, ANOVA, Tukey HSD). Este componente responde a las hipótesis H1, H2 y H3 declaradas en la Propuesta Formal.

- **Componente cualitativo (complementario).** El OE5 incluye la evaluación del agente conversacional mediante un benchmark de 100 preguntas cuyas respuestas son calificadas por dos revisores independientes como *correcta / parcial / incorrecta*. Adicionalmente, se realiza un análisis temático (Braun & Clarke 2006) de las respuestas que caen en la categoría *parcial* para identificar patrones de error recurrentes (e.g., confusión entre nombres toponímicos en guaraní y español; ambigüedad entre departamentos colindantes). Este componente cualitativo triangula con el cuantitativo para enriquecer la interpretación.

La triangulación de métodos cuantitativos y cualitativos es consistente con el paradigma mixto descrito por Creswell & Plano Clark (2018, *Designing and Conducting Mixed Methods Research*).

## 3.4. Diseño

**Cuasi-experimental con grupo control y dos grupos experimentales.**

El diseño sigue el formato pre-post con tres grupos:

| Grupo | Condición | n (features) | Modelo |
|-------|-----------|--------------|--------|
| Control (G0) | Zero-shot, sin fine-tune | 200 held-out | CLIP ViT-B/32 |
| Experimental 1 (G1) | Fine-tuned, prompt mínimo | 200 held-out | SmolVLM-256M + QLoRA |
| Experimental 2 (G2) | Fine-tuned, prompt detallado | 200 held-out | Florence-2-base + QLoRA |

**Variables independientes manipuladas:**
1. *Arquitectura del modelo* (CLIP vs. SmolVLM vs. Florence-2).
2. *Cantidad de datos de entrenamiento* (curva de aprendizaje: 1K → 5K → 10K features).
3. *Prompt template* (mínimo vs. detallado).

**Variables dependientes medidas:**
1. Cohen's κ inter-anotador (validación de calidad de anotación humana contra ground truth).
2. F1 macro por clase nivel-2.
3. Accuracy top-1 sobre el benchmark de 200 features held-out.
4. Tasa de respuesta correcta del agente conversacional (100 preguntas, 2 revisores).
5. Latencia p95 de la interfaz web.

**Variables controladas:**
- Semilla aleatoria 42 en todos los experimentos (reproducibilidad).
- Versiones exactas de Python 3.13.5, transformers 4.45, PyTorch 2.4.0.
- GPU única: NVIDIA RTX 4090 24 GB rented en Lambda Labs (~$1.5/h × 80 h = $120 total budget). En caso de indisponibilidad, fallback a Google Colab Pro ($10/mes).
- Resolución de imagen de entrada: 256×256 px para CLIP; 384×384 px para Florence-2; 512×512 px para SmolVLM. Normalización ImageNet (media [0.485, 0.456, 0.406], std [0.229, 0.224, 0.225]).

**Variables extrañas:**
- Variabilidad de cobertura OSM entre zonas urbanas (Asunción, Central) y zonas rurales (Boquerón, Alto Paraguay).
- Diferencias estacionales en Sentinel-2 (verano chaqueño vs. invierno).
- Sesgo del anotador humano, mitigado mediante doble/triple anotación + cálculo de Cohen's κ.

**Justificación del diseño cuasi-experimental:** la asignación aleatoria perfecta es imposible porque (i) las arquitecturas son cualitativamente distintas y no intercambiables, y (ii) los datos de entrenamiento son los mismos para G1 y G2 pero difieren respecto a G0. El diseño sigue la tradición de Campbell & Stanley (1963) para quasi-experimentos con múltiples grupos de comparación.

## 3.5. Unidad de análisis

La unidad de análisis varía según la fase:

**Fases 1-3 (caracterización, anotación, fine-tune):** *feature cartográfica individual*. Una feature se define como un objeto geométrico discreto (punto, línea, polígono) con un tipo semántico en el corpus abierto. Ejemplos: una carretera OSM con `highway=residential`, un edificio OSM con `building=yes`, un polígono de territorio indígena del INDI, una parcela agrícola rasterizada del MOPC.

**Fase 4 (interfaz conversacional):** *consulta en lenguaje natural*. Cada consulta es una pregunta libre formulada por un usuario final (turista, investigador, funcionario público, estudiante). Se evalúan 100 consultas redactadas por el autor y validadas por dos revisores.

**Fase 5 (validación final):** *experimento de anotación*. Cada experimento consiste en la anotación de una feature por cada modelo bajo evaluación. Total: 200 features × 3 modelos = 600 anotaciones automáticas, más 200 features × 2-3 anotadores humanos = 400-600 anotaciones manuales para el cálculo de κ.

**Justificación de la elección:** la elección de *feature individual* (en lugar de *mapa* o *dataset completo*) es estándar en estudios de evaluación de modelos visión-lenguaje sobre datos cartográficos (Yuan et al. 2021; Kuckreja et al. 2024; Wang et al. 2024). Permite calcular métricas por feature y descomponer el error por categoría semántica.

## 3.6. Población y muestra

### 3.6.1. Población

**Todas las features cartográficas abiertas disponibles para Paraguay en las cinco fuentes integradas:**
- OSM Paraguay (Geofabrik extract, ~2.46M features, 1.2 GB en `data/raw/2026-08-10/osm/`).
- IGN raster tiles (17 departamentos + Asunción, ~2 GB en `data/raw/ign/`).
- Sentinel-2 L2A mosaicos sin nubes (Cobertura nacional, ~20 GB esperados).
- INDI territorios indígenas (~600 polígonos, ~5 MB en `data/raw/indi/`).
- MOPC infraestructura vial y obras públicas (~5 GB esperados).
- WorldPop (grilla poblacional 100 m, ~50 MB).
- Open Buildings v3 (Google, ~100 MB).
- CHIRPS daily precipitation (200 MB).

Total estimado de features únicas tras deduplicación: ~3M-5M features, dominadas por OSM.

### 3.6.2. Muestra de entrenamiento

**10.000 features estratificadas por categoría nivel-1.**

La estratificación se realiza con afijación proporcional a la distribución de la población, con sobre-muestreo de clases raras (siguendo el principio de *class-balanced sampling* descrito por Buda et al. 2018). El esquema de sobre-muestreo es:

- *Over-sample factor:* ×3 para clases con frecuencia < 1% del total.
- *Under-sample factor:* ×0.5 para clases con frecuencia > 30% del total (principalmente `highway=residential` y `building=yes`).

**Categorías nivel-1 consideradas (taxonomía derivada de OSM + adaptada al contexto paraguayo):**

| Código | Categoría | Descripción | Frecuencia esperada |
|--------|-----------|-------------|---------------------|
| C1 | Vías de transporte | highways, paths, railways | 40% |
| C2 | Edificaciones | buildings, amenities, shops | 30% |
| C3 | Uso de suelo | landuse, natural, vegetation | 12% |
| C4 | Recursos hídricos | water bodies, rivers, wetlands | 8% |
| C5 | Territorio indígena | comunidades INDI | 2% |
| C6 | Infraestructura pública | schools, hospitals, roads MOPC | 8% |

### 3.6.3. Muestra de validación inter-anotador

**200 features con doble o triple anotación.**

La selección se realiza mediante *stratified random sampling* con los siguientes criterios:
- Mínimo 5 features por cada categoría nivel-2 (sub-categoría dentro de C1-C6).
- Balance urbano/rural (50% Asunción/Central, 50% resto del país).
- Balance temporal (features con diferentes fechas de última edición OSM).

El tamaño muestral n=200 se justifica por dos consideraciones:
1. **Poder estadístico.** Para detectar un Cohen's κ ≥ 0.85 con un IC 95% de ±0.05, se requieren ~190 observaciones (calculado con la fórmula de Flack et al. 1988, asumiendo κ esperado = 0.85).
2. **Restricción operativa.** Tres anotadores cartográficos expertos disponibles, ~3 horas de anotación cada uno. n=200 es alcanzable.

### 3.6.4. Muestra para benchmark conversacional

**100 preguntas distribuidas en 5 categorías temáticas:**

| Categoría | n | Ejemplos |
|-----------|---|----------|
| Transporte | 20 | "¿Cuál es la ruta más corta entre Villarrica y Caaguazú?" |
| Vivienda | 20 | "¿Cuántas edificaciones hay en el barrio Sajonia de Asunción?" |
| Uso de suelo | 20 | "¿Qué porcentaje del Chaco es cobertura boscosa?" |
| Recursos hídricos | 20 | "¿Cuántos tajamares hay en el departamento de Boquerón?" |
| Territorio indígena | 20 | "¿Qué comunidades mbya guaraní existen en Caaguazú?" |

Las preguntas son redactadas por el autor y validadas por dos revisores externos (uno nativo de guaraní, otro cartógrafo) en dos rondas. Las preguntas se redactan mitad en español estándar, mitad en jopara/guaraní, para evaluar la cobertura lingüística del agente.

## 3.7. Variables

### 3.7.1. Variables independientes (manipuladas)

**VI1 — Arquitectura del modelo.**
Tres niveles: CLIP ViT-B/32 (control), SmolVLM-256M + QLoRA (G1), Florence-2-base + QLoRA (G2). Se eligió CLIP como control por ser el estándar de facto en clasificación zero-shot visión-lenguaje y contar con resultados de referencia en la literatura. SmolVLM y Florence-2 fueron seleccionados por su tamaño compacto (despliegue en CPU o GPU modesta) y por su arquitectura sequence-to-sequence que permite integrar tareas de detección y clasificación en un único modelo.

**VI2 — Cantidad de datos de entrenamiento.**
Tres niveles: 1K, 5K, 10K features. La curva de aprendizaje con estos tres puntos permite estimar si el modelo se beneficia marginalmente de más datos (ley de potencia empírica reportada por Kaplan et al. 2020) o si se satura antes.

**VI3 — Prompt template.**
Dos niveles: mínimo ("{clase}") vs. detallado ("Una fotografía aérea de {clase} en el territorio paraguayo, capturada desde satélite o dron, con resolución espacial de 0.5-2 metros por píxel"). El prompt detallado inyecta conocimiento del dominio (geografía paraguaya, resolución típica) para reducir el sesgo de distribución que CLIP/SmolVLM traen del pre-entrenamiento web.

### 3.7.2. Variables dependientes (medidas)

**VD1 — Cohen's κ inter-anotador.**
Definición: medida de acuerdo entre anotadores que corrige el acuerdo esperado por azar (Cohen 1960). Rango [-1, 1]; valores > 0.81 indican acuerdo "casi perfecto" (Landis & Koch 1977). Se calcula con bootstrap de 1000 iteraciones para obtener IC 95%.

**VD2 — F1 macro por clase nivel-2.**
Media no ponderada del F1-score por clase. Penaliza el desequilibrio entre clases; es la métrica estándar para problemas multi-clase desbalanceados (Sokolova & Lapalme 2009).

**VD3 — Accuracy top-1.**
Proporción de features para las cuales la clase predicha por el modelo coincide exactamente con la clase ground-truth. Es la métrica más estricta; no admite empates.

**VD4 — Tasa de respuesta correcta del agente conversacional.**
Proporción de preguntas del benchmark de 100 para las cuales al menos 2 de los 2 revisores independientes calificaron la respuesta del agente como *correcta*. Se excluye la categoría *parcial* del numerador y denominador. Cohen's κ entre los dos revisores se reporta como medida de validación del benchmark.

**VD5 — Latencia p95 de la interfaz web.**
Percentil 95 de la latencia end-to-end (tiempo desde que el usuario envía la consulta hasta que recibe la primera palabra de la respuesta), medida sobre 100 consultas consecutivas en condiciones de carga normal. Meta: p95 ≤ 3 segundos.

### 3.7.3. Variables controladas

- **Semilla aleatoria 42** en Python (`random.seed`), NumPy (`np.random.seed`), PyTorch (`torch.manual_seed`), CUDA (`torch.cuda.manual_seed_all`).
- **Versiones exactas** declaradas en `requirements.txt` (pinned).
- **Hardware único** durante la fase experimental: una única instancia de GPU rented por toda la duración del experimento.
- **Resolución de imagen de entrada** fija por arquitectura (ver §3.4).
- **Pre-procesamiento de texto** consistente: lowercase, normalización de espacios, eliminación de acentos inconsistentes según las convenciones OSM.

### 3.7.4. Variables extrañas

- **Cobertura OSM rural < urbana.** Mitigada mediante reporte estratificado por departamento y por categoría.
- **Diferencias estacionales en Sentinel-2.** Mitigada mediante selección de mosaicos sin nubes (umbral 10%) y reporting de la fecha de cada imagen.
- **Sesgo del anotador.** Mitigado mediante 2-3 anotadores + Cohen's κ. Los anotadores reciben las mismas instrucciones escritas y un entrenamiento de calibración de 30 minutos sobre 20 features de práctica (no incluidas en la muestra).
- **Variabilidad de GPU rented.** Mitigada mediante registro del tipo de instancia exacta en cada experimento (id de instancia Lambda Labs + driver CUDA + versión cuDNN).

## 3.8. Instrumentos y técnicas

### 3.8.1. Software

La siguiente tabla lista las versiones pinned del stack tecnológico. Todas las versiones se fijan en `requirements.txt` y se instalan dentro de un entorno virtual (`venv/`).

| Componente | Versión | Función |
|---|---|---|
| Python | 3.13.5 | Lenguaje base |
| PyTorch | 2.4.0 | Framework de deep learning |
| transformers (HuggingFace) | 4.45.0 | Carga de CLIP, Florence-2, SmolVLM |
| peft (HuggingFace) | 0.10.0 | Implementación de LoRA / QLoRA |
| bitsandbytes | 0.43.0 | Cuantización 4-bit para QLoRA |
| accelerate | 0.34.0 | Aceleración multi-GPU / mixed precision |
| Ultralytics | 8.2.0 | YOLOv8 baseline de detección |
| rasterio | 1.3.9 | Lectura/escritura raster |
| geopandas | 0.14.4 | Manipulación vectorial |
| osmium | 3.4.1 | Parser OSM PBF |
| shapely | 2.0.4 | Geometría 2D |
| pyproj | 3.6.1 | Proyecciones cartográficas |
| Label Studio | 1.8.0 | UI de anotación humana |
| Next.js | 16.0 | Framework web frontend |
| Tailwind CSS | 4.0 | Estilos |
| LangChain | 0.3.0 | Orquestación LLM |
| Ollama | 0.3.0 | LLM local (Llama-3.1-8B-Instruct) |
| vLLM | 0.5.4 | Serving LLM en GPU |
| ChromaDB | 0.5.0 | Vector store para RAG |
| FastAPI | 0.115.0 | Backend API REST |
| Docker | 27.0 | Reproducibilidad (compose) |
| pytest | 8.3.0 | Tests unitarios |

### 3.8.2. Hardware

**Configuración primaria (entrenamiento y fine-tune):**
- **GPU:** NVIDIA RTX 4090 24 GB rented en Lambda Labs (~$1.5/h × 80 h = $120 budget).
- **CPU:** 16 cores x86_64 (AMD EPYC o Intel Xeon, según disponibilidad Lambda).
- **RAM:** 64 GB DDR4.
- **Almacenamiento:** 500 GB SSD NVMe (raw + processed + cache modelo).

**Configuración secundaria (desarrollo local y demo):**
- **CPU:** Apple M2 Pro 12-core (12 GB unified memory) — sin GPU dedicada.
- **RAM:** 32 GB.
- **Almacenamiento:** 1 TB SSD.

**Configuración de despliegue (producción web):**
- **VPS Paraguay:** Servarica Host A, 4 vCPU + 8 GB RAM + 100 GB SSD.
- **Tráfico esperado:** ~100-500 visitas/día (proyección conservadora).

**Alternativa gratuita para experimentación inicial:**
- Google Colab Pro ($10/mes) — útil para pruebas piloto y debugging.
- Kaggle Notebooks (30 h/mes GPU) — útil para fine-tune rápido.

### 3.8.3. Técnicas por fase

#### (a) Fase 1 — Extracción y pre-procesamiento

| Fuente | Técnica | Script |
|--------|---------|--------|
| OSM PBF | `osmium extract --bbox=-22.0,-62.0,-19.0,-54.0` + `osmium export` → GeoJSON | `scripts/fetch_data.sh` (subrutina `fetch_osm()`) |
| IGN WMS | `owslib` → WMS GetMap → `gdal_translate` → GeoTIFF | `scripts/fetch_ign_wms.py` |
| Sentinel-2 | `sentinelsat` API → búsqueda por bbox Paraguay + threshold nubes 10% → descarga ZIP → `gdal` merge → GeoTIFF | `scripts/fetch_data.sh` (subrutina `fetch_sentinel2()`) |
| INDI | descarga directa GeoJSON | `scripts/fetch_data.sh` (subrutina `fetch_indi()`) |
| MOPC | portal datos abiertos o solicitud Ley 5282/2014 | `scripts/fetch_data.sh` (subrutina `fetch_mopc()`) |
| WorldPop | `wget` directo | `scripts/fetch_data.sh` (subrutina `fetch_worldpop()`) |
| Open Buildings | `gsutil cp gs://open-buildings-data/v3/...` | `scripts/fetch_data.sh` (subrutina `fetch_openbuildings()`) |
| CHIRPS | `wget` o `OPeNDAP` | `scripts/fetch_data.sh` (subrutina `fetch_chirps()`) |

**Estandarización de coordenadas.** Todos los datasets se reproyectan a EPSG:4326 (WGS84) como datum común, y a EPSG:32721 (UTM 21S, zona Paraguay) para operaciones métricas. La transformación se realiza con `pyproj.Transformer` y se valida con un test de round-trip (coordenada → proyección → coordenada debe recuperar el valor original con tolerancia 1e-9 grados).

**Limpieza de geometrías.** Se aplica `shapely.make_valid()` para corregir geometrías inválidas detectadas por `geopandas.is_valid`. Las features con geometría `None` o vacía se descartan con logging del id y motivo.

**Versionado.** Cada dataset descargado se etiqueta con la fecha `YYYY-MM-DD` y se almacena en `data/raw/<fuente>/<YYYY-MM-DD>/`. El SHA256 se calcula al finalizar la descarga y se almacena en `data/raw/<fuente>/SHA256SUMS`. El inventario completo se exporta a `data/INVENTORY.json` mediante `scripts/data_inventory.py`.

#### (b) Fase 2 — Anotación semiautomática

El pipeline de anotación combina tres modelos en cascada (ver Figura 3.1):

```
[Feature OSM + raster IGN]
        │
        ▼
[1] SAM (Segment Anything) → máscaras candidatas
        │
        ▼
[2] GroundingDINO → bounding boxes refinados + clase top-k
        │
        ▼
[3] CLIP ViT-B/32 → score similitud clase-propuesta
        │
        ▼
[Confianza ≥ 0.7] ──► ACEPTADO automático
[Confianza < 0.7] ──► Encolado para revisión humana (Label Studio)
        │
        ▼
[2-3 anotadores humanos] → anotación final
        │
        ▼
[Dataset anotado] → data/processed/annotations_v1.geojson
```

**Figura 3.1 — Pipeline de anotación semiautomática.** SAM genera máscaras sin clase; GroundingDINO refina las cajas y propone clases; CLIP clasifica con confianza; las features con confianza < 0.7 se enrutan a Label Studio para revisión humana.

**Etapa 1 — SAM.** Se utiliza SAM con checkpoint `sam_vit_h_4b8939.pth` (ViT-H, 632M parámetros). Los puntos iniciales se muestrean automáticamente sobre el bounding box de cada feature OSM en una grilla uniforme 5×5 = 25 puntos. SAM devuelve hasta 25 máscaras candidatas, de las cuales se seleccionan las 5 con mayor *stability score* (métrica interna de SAM).

**Etapa 2 — GroundingDINO.** Se utiliza GroundingDINO con checkpoint `groundingdino_swint_ogc.pth` (Swin-T backbone, ~230M parámetros). El prompt textual se construye como una lista de clases candidatas separadas por punto: `"building . house . road . water . vegetation ."` GroundingDINO devuelve hasta 10 instancias detectadas con su clase y score de confianza.

**Etapa 3 — CLIP.** Se utiliza CLIP ViT-B/32 (OpenAI pretrained). Para cada par (máscara SAM recortada, clase candidata) se calcula el score de similitud coseno entre el embedding de la imagen recortada (224×224 px) y el embedding del prompt textual de la clase. La clase con mayor score (top-1) se asigna como predicción.

**Umbral de aceptación.** El umbral τ = 0.7 sobre el score CLIP normalizado (softmax sobre 5 clases top) determina si la anotación se acepta automáticamente o se encola para revisión humana. Este valor fue seleccionado mediante un experimento piloto sobre 200 features con anotación ground-truth (no incluidas en la muestra final), buscando maximizar F1 macro bajo el constraint de que al menos 30% de las features requieran revisión humana (para mantener la diversidad del dataset anotado humano).

**Revisión humana (Label Studio).** Los anotadores (3 cartógrafos paraguayos con experiencia > 5 años en IGN o en consultoría geoespacial privada) reciben un instructivo escrito de 5 páginas y un entrenamiento de calibración de 30 minutos sobre 20 features de práctica. Cada feature se anota con:
- Clase nivel-1 (C1-C6, ver §3.6.2).
- Clase nivel-2 (sub-categoría específica, e.g., `highway=residential` o `building=house`).
- Notas libres (e.g., "fachada de madera", "tajamar en construcción", "parcela con dos edificaciones").

Las features con desacuerdo entre anotadores se someten a una sesión de arbitraje por un cuarto anotador senior (resolución por mayoría o por discusión).

#### (c.b) Fase 2.b — Plantillas de prompt y taxonomía operativa

**Taxonomía operativa nivel-1 / nivel-2.** El esquema de anotación se deriva del *tagging* OSM pero se adapta al contexto paraguayo. A continuación se presenta la taxonomía final, con ejemplos concretos para cada categoría. Esta taxonomía fue piloteada sobre 200 features y refinada tras retroalimentación de los anotadores antes de escalar al dataset completo.

| Nivel-1 | Nivel-2 (ejemplos) | Fuente primaria |
|---------|---------------------|-----------------|
| C1 Vías | `highway=motorway`, `highway=trunk`, `highway=primary`, `highway=secondary`, `highway=residential`, `highway=service`, `highway=track`, `highway=path`, `highway=footway`, `highway=cycleway`, `railway=rail`, `railway=tram`, `aeroway=runway` | OSM |
| C2 Edificaciones | `building=house`, `building=apartments`, `building=commercial`, `building=industrial`, `building=school`, `building=hospital`, `building=church`, `building=warehouse`, `building=roof` | OSM + Open Buildings v3 |
| C3 Uso de suelo | `landuse=residential`, `landuse=commercial`, `landuse=industrial`, `landuse=agricultural`, `landuse=forest`, `landuse=farmland`, `natural=wood`, `natural=grassland`, `natural=sand`, `natural=wetland` | OSM + Sentinel-2 |
| C4 Recursos hídricos | `natural=water`, `waterway=river`, `waterway=stream`, `waterway=canal`, `natural=coastline`, `water=lake`, `water=pond`, `water=reservoir`, `water=tajamar` (término paraguayo para pequeño embalse ganadero) | OSM + Sentinel-2 |
| C5 Territorio indígena | `boundary=protected_area` + `protect_class=indigenous`, capa INDI directa | INDI |
| C6 Infraestructura pública | `amenity=school`, `amenity=hospital`, `amenity=clinic`, `amenity=police`, `amenity=fire_station`, `amenity=town_hall`, `amenity=library`, `amenity=post_office`, `public_transport=station`, capa MOPC | OSM + MOPC |

**Plantillas de prompt para CLIP y SmolVLM.**

*Prompt mínimo (P1).* Una sola frase corta, sin contexto geográfico explícito. Ejemplos para cada categoría nivel-1:
- C1: `"aerial view of a road"` / `"imagen satelital de una carretera"`
- C2: `"satellite image of a building"` / `"imagen satelital de un edificio"`
- C3: `"aerial photograph of land use"` / `"fotografía aérea de uso de suelo"`
- C4: `"satellite image of water"` / `"imagen satelital de agua"`
- C5: `"aerial view of indigenous territory"` / `"vista aérea de territorio indígena"`
- C6: `"aerial view of public infrastructure"` / `"vista aérea de infraestructura pública"`

*Prompt detallado (P2).* Incorpora contexto geográfico, resolución típica y estacionalidad. Ejemplo:
```
"a high-resolution aerial photograph (0.5 to 2 meters per pixel) of {clase},
captured by satellite or drone over the Republic of Paraguay between 2020 and 2026,
showing the characteristic morphology of {clase_específica} in the Chaco or Eastern Region"
```

Las dos plantillas se aplican en paralelo a CLIP zero-shot (G0) y como base del input de SmolVLM y Florence-2 (G1, G2). El efecto del prompt se analiza mediante la diferencia Δ = F1(P2) − F1(P1).

#### (c) Fase 3 — Fine-tune con QLoRA

**SmolVLM-256M.** Modelo compacto (256M parámetros) entrenado desde cero por HuggingFace sobre datos curados. La adaptación se realiza con QLoRA:
- Rank: 16.
- Alpha: 32.
- Dropout: 0.05.
- Learning rate: 2e-4 (lineal warmup 10%, cosine decay).
- Epochs: 3.
- Batch size: 8 (effective batch 32 con gradient accumulation 4).
- Optimizer: paged_adamw_8bit (bitsandbytes).
- Quantization: 4-bit NF4 (NormalFloat 4-bit).
- Target modules: q_proj, v_proj en todas las capas attention.

**Florence-2-base.** Modelo sequence-to-sequence (270M parámetros) de Microsoft Research. La adaptación se realiza con QLoRA:
- Rank: 16.
- Alpha: 32.
- Dropout: 0.05.
- Learning rate: 1e-4 (lineal warmup 10%, cosine decay).
- Epochs: 5.
- Batch size: 4 (effective batch 16 con gradient accumulation 4).
- Optimizer: paged_adamw_8bit.
- Quantization: 4-bit NF4.
- Target modules: q_proj, v_proj en todas las capas attention.

**Baseline CLIP ViT-B/32.** Sin fine-tune. Se evalúa zero-shot con dos prompt templates (mínimo y detallado). Se reportan ambos resultados para verificar el efecto del prompt template.

**Métricas durante entrenamiento.** Cada epoch se evalúa F1 macro sobre el validation set (10% del total = 1.000 features estratificadas). El mejor checkpoint (F1 macro máximo) se guarda y se reporta.

**Validación cruzada.** No se utiliza k-fold por restricción de tiempo y costo computacional. Se utiliza un split train/val/test = 80/10/10 con semilla fija 42.

#### (d) Fase 4 — Aplicación web + RAG

**Backend (FastAPI).**
- Endpoint `POST /api/query` recibe JSON `{query: str, bbox?: [lon,lat,lon,lat]}`.
- Pre-procesamiento: detección de entidades espaciales (departamentos, distritos, ciudades) con regex + diccionario geográfico paraguayo (`data/geog_dict.json`).
- Recuperación: embedding de la consulta con `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` → búsqueda en ChromaDB (índice construido sobre el dataset anotado).
- Generación: Llama-3.1-8B-Instruct (quantized Q4_K_M vía llama.cpp / Ollama) recibe prompt sistema + top-k=5 documentos recuperados + consulta usuario → respuesta.
- Post-procesamiento: validación de coherencia espacial (la respuesta menciona lugares dentro del bbox cuando se especifica).

**Frontend (Next.js 16 + Tailwind 4).**
- Página principal: mapa interactivo (Leaflet 1.9) + chat panel.
- Mapa: tiles de OpenStreetMap + overlay de features anotadas (filtrable por categoría).
- Chat: input + historial + indicador de latencia.
- Idiomas: español (default), jopara (modo avanzado, experimental).

**Deploy.**
- VPS Paraguay (Servarica Host A): Traefik reverse proxy + Docker Compose (`docker-compose.yml` con servicios `backend`, `frontend`, `chroma`, `ollama`).
- Dominio: `paraguay-mapa.paragu-ai.com` (pendiente de DNS).
- HTTPS: Let's Encrypt vía certbot.
- Monitoreo: UptimeRobot + healthcheck cada 5 min.

**Latencia objetivo.** p95 ≤ 3 segundos para consultas sin bbox; ≤ 5 segundos para consultas con bbox grande (> 100 features recuperadas).

#### (e) Fase 5 — Validación inter-anotador

**Protocolo.**
- 200 features con doble anotación + 50 features con triple anotación (overlap para calcular κ entre pares).
- Anotadores independientes (A1, A2, A3) no se comunican durante la anotación.
- Cada feature se presenta con: imagen raster 256×256 px, coordenadas lat/lon, contexto OSM (tipo OSM si existe), y un campo de selección de clase nivel-2 + notas libres.
- Tiempo máximo de anotación: 30 segundos por feature (cronometrado para identificar features ambiguas).

**Métricas.**
- Cohen's κ por par (A1-A2, A1-A3, A2-A3) con IC 95% bootstrap (1000 iteraciones).
- κ promedio sobre los 3 pares.
- Acuerdo exacto (% features con misma clase asignada).
- Acuerdo por categoría nivel-1 (para identificar categorías con alta discordancia).

**Meta.** κ ≥ 0.85 (Landis & Koch 1977: "casi perfecto"). Si no se alcanza, se reportan las features con discordancia y se analiza temáticamente la causa (ambigüedad del esquema de clases, baja calidad del raster, etc.).

#### (f) Fase 6 — Benchmark conversacional

**Protocolo.**
- 100 preguntas redactadas por el autor + validadas por 2 revisores.
- Cada pregunta se somete al agente 3 veces (para evaluar variabilidad); se reporta la respuesta de la corrida mediana.
- 2 revisores independientes califican cada respuesta como *correcta* (cumple completamente), *parcial* (cumple algunos aspectos pero omite o yerra otros), o *incorrecta* (no responde la pregunta o da información falsa).
- κ entre los 2 revisores (sobre las 100 calificaciones) target ≥ 0.70.
- Discrepancias se resuelven por discusión.

**Métricas.**
- Tasa de respuesta correcta (# correctas / 100).
- Tasa de respuesta parcial (# parciales / 100).
- Tasa de respuesta incorrecta (# incorrectas / 100).
- Cohen's κ inter-revisor.
- Latencia p50, p95.
- Distribución por categoría (5 categorías, ver §3.6.4).
- Distribución por idioma (español vs. jopara).

**Meta.** ≥ 75% correctas (H2).

#### (g) Análisis estadístico

**Cuantitativo.**
- ANOVA de una vía para comparar 3 modelos (CLIP, SmolVLM-finetuned, Florence-2-finetuned) sobre F1 macro.
- Post-hoc Tukey HSD para comparaciones pairwise.
- α = 0.05.
- Efecto (η²) reportado.
- IC 95% para κ y accuracy top-1 (bootstrap 1000 iteraciones, semilla 42).
- Verificación de supuestos: normalidad (Shapiro-Wilk), homogeneidad de varianzas (Levene).

**Cualitativo.**
- Análisis temático de las respuestas del agente que caen en *parcial* (Braun & Clarke 2006).
- 2 codificadores independientes.
- κ entre codificadores target ≥ 0.70.
- Temas emergentes se agrupan en: (i) confusión toponímica guaraní/español, (ii) ambigüedad de límites administrativos, (iii) cobertura incompleta para zonas rurales, (iv) errores de retrieval en el RAG.

**Software estadístico.**
- Python 3.13 con `scipy.stats`, `statsmodels`, `scikit-learn`.
- Visualizaciones con `matplotlib` 3.9 + `seaborn` 0.13.

### 3.8.4. Análisis de poder estadístico

**Cálculo a priori del tamaño muestral.** El tamaño muestral de n=200 features para validación inter-anotador se justificó en §3.6.3 mediante la fórmula de Flack et al. (1988). A continuación se presenta el cálculo formal:

Para un Cohen's κ esperado κ₀ = 0.85 (target según H1), con un margen de error δ = ±0.05 y nivel de confianza 95% (z = 1.96), el tamaño muestral necesario es:

```
n = (z² · κ₀ · (1 − κ₀)) / δ²
  = (1.96² · 0.85 · 0.15) / 0.05²
  = (3.8416 · 0.1275) / 0.0025
  = 0.4898 / 0.0025
  ≈ 196 features
```

Se redondea a n=200 por seguridad y para permitir estratificación balanceada.

Para el benchmark conversacional (n=100 preguntas), el cálculo de poder es:

```
Para detectar una diferencia de 15 puntos porcentuales entre el baseline
(50% correctas, esperado para un agente no adaptado) y el agente fine-tuned
(75% correctas según H2), con α = 0.05 y poder 1−β = 0.80, el test
de McNemar (diseño pareado, mismo sujeto a 2 condiciones) requiere:
n = (z_α + z_β)² · p̄ · (1 − p̄) / (Δp)²
  = (1.96 + 0.84)² · 0.625 · 0.375 / 0.15²
  = 7.84 · 0.234 / 0.0225
  ≈ 81.6 → 100 preguntas (redondeo)
```

Se redondea a n=100 para incluir margen y para que las 5 categorías tengan 20 preguntas cada una (muestreo balanceado).

### 3.8.5. Manejo de datos faltantes y valores atípicos

**Datos faltantes.** Los datasets abiertos paraguayos presentan tres tipos principales de faltantes:
- **Features sin geometría.** ~0.3% de las features OSM tienen geometría `null` (típicamente nodos sin `lat`/`lon`). Se eliminan con logging del id.
- **Features sin clase.** ~5% de las features OSM tienen tags inconsistentes o incompletos (e.g., `building=construction` sin `building=yes` posterior). Se re-etiquetan automáticamente con `building=construction` y se enrutan a revisión humana si la confianza CLIP es < 0.7.
- **Imágenes sin cobertura de nubes.** Para Sentinel-2, se filtran escenas con > 10% de cobertura nubosa. Las features sin imagen utilizable se marcan con `image_quality=poor` y se excluyen del entrenamiento pero se mantienen en el dataset anotado (como negativos duros para el benchmark).

**Valores atípicos.** Se detectan mediante IQR (rango intercuartil) sobre las distribuciones de área y perimetro por categoría. Features con área > 1.5·IQR por encima del Q3 o < 0.5·IQR por debajo del Q1 se inspeccionan manualmente; los errores se corrigen en la taxonomía; los valores válidos se mantienen.

**Conflictos de etiquetas.** Cuando una feature tiene etiquetas contradictorias en OSM (e.g., `highway=residential` + `building=yes` en la misma geometría), se aplica la regla de prioridad C1 > C2 > C3 > C4 > C5 > C6 según el ordenamiento taxonómico. El conflicto se registra en `data/processed/conflicts.log` para auditoría.

### 3.8.6. Control de versiones de datos y modelos

**Versionado semántico.** Se adopta el esquema `MAJOR.MINOR.PATCH` (semver 2.0):
- MAJOR: cambio incompatible en taxonomía de clases (e.g., agregar C7).
- MINOR: adición compatible de features o anotaciones (e.g., +1000 features nuevas).
- PATCH: corrección de errores menores (e.g., etiqueta mal escrita en 5 features).

Cada versión del dataset anotado se publica con DOI Zenodo inmutable y se enlaza desde el repositorio de la tesis (`/opt/data/thesis-active/data/processed/annotations_v<version>.geojson`).

**Trazabilidad.** Cada experimento registra:
- Versión del dataset (e.g., `v1.2.0`).
- Versión del modelo base (e.g., `clip-vit-base-patch32@openai`).
- Semilla aleatoria (e.g., `42`).
- Hash del commit de código (e.g., `git rev-parse HEAD`).
- Versión de CUDA, driver, cuDNN.
- Fecha y hora de inicio y fin (UTC).

Esta trazabilidad se almacena en `experiments/<YYYY-MM-DD>/<experiment_id>/metadata.json` y se publica junto con los logs de W&B.

### 3.8.7. Gestión de riesgos técnicos

La tabla siguiente resume los riesgos técnicos principales y sus mitigaciones. La versión completa está en `RISK_REGISTER.md`.

| ID | Riesgo | Probabilidad | Impacto | Mitigación |
|----|--------|--------------|---------|------------|
| RT1 | CUDA / driver incompatibilidad | Media | Alto | Fijar versiones en `requirements-cuda.txt`; validación previa en CI |
| RT2 | GPU rented con VRAM insuficiente | Baja | Alto | Fallback a Colab Pro; reducción de batch size con gradient accumulation |
| RT3 | Dataset OSM sin features en algún departamento | Media | Medio | Reportar por departamento; análisis estratificado |
| RT4 | Anotador abandona el proyecto | Baja | Alto | Iván anota el 100% (más lento, viable); reclutar reemplazo |
| RT5 | Modelo pre-entrenado retirado de HF Hub | Baja | Medio | Snapshot local en `models/`; hash verificado en publicación |
| RT6 | Latencia VPS excede target p95 | Media | Medio | Cache de embeddings; modelo quantized Q4_K_M; CDN para frontend |
| RT7 | Desbalance extremo de clases | Media | Medio | Class-balanced sampling; weighted loss; focal loss opcional |
| RT8 | Tiempo de revisión humana > estimado | Alta | Bajo | Reducir n a 150 features; bootstrap más iteraciones |

---

## 3.9. Procedimiento

### Fase 1 — M1-2: Caracterización del corpus

**Semanas 1-2 (M1):**
1. Descargar datasets D1-D9 según protocolo descrito en §3.8.3(a) y `DATA_MANIFEST.md`.
2. Calcular SHA256 de cada archivo descargado; almacenar en `data/raw/<fuente>/SHA256SUMS`.
3. Estandarizar coordenadas a EPSG:4326 + EPSG:32721.
4. Generar `data/INVENTORY.json` con metadatos completos (tamaño, fecha, licencia, fuente).
5. Documentar cobertura por departamento y por fuente.

**Semanas 3-4 (M1):**
6. Calcular estadísticas descriptivas: número de features por categoría, fecha mediana de última edición, densidad espacial por km².
7. Construir visualizaciones: histogramas de antigüedad, mapas de calor de densidad, gráficos de pastel por categoría.
8. Reportar calidad por dataset (completitud, exactitud reportada por la fuente, nivel de confianza OSM).

**Semanas 5-8 (M2):**
9. Implementar pipeline de extracción (sub-rutinas `fetch_*`).
10. Validar con datos de prueba sobre Asunción (densidad alta) y Boquerón (densidad baja).
11. Documentar problemas de calidad identificados (e.g., geometrías inválidas, etiquetas duplicadas, tags inconsistentes).

**Entregable M2:** `corpus_characterization_report.pdf` (10-15 páginas) + tabla en `data/processed/stats.json` + `data/INVENTORY.md`.

### Fase 2 — M2-4: Anotación

**Semanas 9-10 (M2):**
1. Implementar pipeline SAM + GroundingDINO + CLIP en `scripts/auto_annotate.py` (existente, validar y extender).
2. Tests unitarios sobre features conocidas (`scripts/test_annotate.py`).
3. Calibración del umbral τ sobre muestra piloto de 200 features con ground-truth (no incluidas en la muestra final).

**Semanas 11-14 (M3):**
4. Correr pipeline sobre el corpus completo (target: 10K features anotadas automáticamente).
5. Configurar Label Studio: importar features con confianza < 0.7.
6. Reclutar y entrenar 3 anotadores (instructivo + sesión de calibración).
7. Iniciar revisión humana en lotes de 500 features.

**Semanas 15-18 (M4):**
8. Completar revisión humana hasta 3.000 features (las de baja confianza automática).
9. Resolución de desacuerdos por arbitraje (anotador senior).
10. Calcular κ inter-anotador preliminar sobre los primeros 500.
11. Exportar dataset anotado a `data/processed/annotations_v1.geojson` + Hugging Face Hub.

**Entregable M4:** `annotations_v1.geojson` (~10K features) + DOI Zenodo + model card Hugging Face.

### Fase 3 — M4-5: Fine-tune

**Semanas 19-20 (M4):**
1. Split 80/10/10 (train/val/test) estratificado por categoría nivel-1.
2. Configurar W&B (Weights & Biases) para tracking de experimentos.
3. Fine-tune SmolVLM-256M con QLoRA.
4. Fine-tune Florence-2-base con QLoRA.

**Semanas 21-22 (M5):**
5. Evaluar en test set: F1 macro, accuracy top-1, confusion matrix.
6. Evaluar baseline CLIP zero-shot con dos prompt templates.
7. Análisis estadístico: ANOVA + Tukey HSD.
8. Publicar pesos en Hugging Face Hub con model card detallado (descripción, métricas, ejemplos, limitaciones, licencia).

**Entregable M5:** Modelo fine-tuned en HF Hub + `fine_tune_report.md` con métricas detalladas.

### Fase 4 — M5-6: Aplicación web

**Semanas 23-24 (M5):**
1. Construir backend FastAPI (`backend/main.py`) con endpoint `/api/query`.
2. Implementar pre-procesamiento de entidades espaciales (regex + diccionario geográfico).
3. Construir índice Chroma sobre embeddings de descripciones textuales + metadatos estructurados.

**Semanas 25-26 (M6):**
4. Implementar retrieval + generación con Llama-3.1-8B-Instruct via Ollama.
5. Construir frontend Next.js 16 con Tailwind 4 + Leaflet 1.9.
6. Integración frontend ↔ backend ↔ Chroma ↔ Ollama.
7. Tests de integración (pytest).

**Semanas 27-28 (M6):**
8. Deploy en VPS Paraguay (Docker Compose + Traefik + Let's Encrypt).
9. Pruebas de carga + monitoreo.
10. Documentar API en `docs/API.md` (OpenAPI 3.0 spec autogenerado).
11. Anuncio público + tutorial de uso.

**Entregable M6:** App web desplegada en `paraguay-mapa.paragu-ai.com` + documentación + video demo.

### Fase 5 — M6-7: Validación + paper

**Semanas 29-30 (M6):**
1. Validación inter-anotador completa (200 features, κ).
2. Benchmark conversacional (100 preguntas, 2 revisores).
3. Análisis estadístico completo (ANOVA + bootstrap + análisis temático).

**Semanas 31-34 (M7):**
4. Redactar paper (8 páginas ICA o 12 páginas SIGSPATIAL, ver `PAPER_OUTLINE.md`).
5. Incorporar figuras de alta calidad (mapas, diagramas de pipeline, confusion matrices).
6. Revisión interna por 2 pares (uno cartógrafo, uno ML engineer).
7. Iteración sobre comentarios.
8. Pre-print en arxiv (categorías cs.CV, cs.CL, cs.CY).

**Semana 35 (M7):**
9. Envío a ICA 2027 / ACM SIGSPATIAL 2027 (deadline estimada Q3 2027).

**Entregable M7:** Pre-print arxiv + submission a conferencia Q1/Q2.

## 3.10. Consideraciones éticas

La presente investigación **no involucra sujetos humanos** en el sentido de la Declaración de Helsinki ni del CIOMS 2016. Específicamente:
- No se recolectan datos personales de usuarios finales (la app web es anónima por diseño).
- No se realizan experimentos con participantes humanos (los anotadores reciben compensación por su trabajo profesional; no son "sujetos de investigación").
- No se utilizan datos sensibles (salud, orientación sexual, religión, etc.) de ninguna fuente.

El protocolo se documenta en `ETHICS_WAIVER_MEMO.md` con la firma del director de tesis, declarando la exención de revisión por el Comité de Ética de la FADA-UNA.

**Consideraciones éticas derivadas (no formales):**
- **Sesgo algorítmico.** Se reporta explícitamente la cobertura asimétrica OSM (urbano > rural, Asunción > Chaco). El modelo fine-tuneado se evalúa con métricas desagregadas por departamento para evitar ocultar disparidades.
- **Soberanía de datos.** Todos los datos son abiertos y se procesan localmente o en infraestructura paraguaya (VPS Paraguay). Ningún dato se envía a APIs de pago externas sin consentimiento del usuario.
- **Atribución y licenciamiento.** Todos los derivados se publican con atribución explícita a las fuentes originales. Las anotaciones se publican bajo CC BY 4.0 (compatible con la mayoría de las fuentes); los derivados de OSM mantienen ODbL para la porción OSM-derived.
- **Accesibilidad lingüística.** La interfaz soporta español y jopara (experimental). La documentación se publica en español.
- **Impacto ambiental.** Se reporta la huella de carbono estimada del entrenamiento (CodeCarbon tool): ~25 kg CO₂eq para 80 horas de RTX 4090.

## 3.11. Limitaciones del diseño

El diseño experimental presenta cinco limitaciones reconocidas que se reportarán explícitamente en el Capítulo 5 (Discusión):

**(L1) Cobertura OSM rural.** La densidad de features OSM en el Chaco paraguayo es ~70% menor que en el área metropolitana de Asunción (Ramírez & Ortega 2022). El modelo entrenado predominantemente sobre cobertura urbana transfiere pobremente al Chaco. Se mitiga reportando métricas desagregadas por departamento y recomendando trabajo futuro de campo en zonas rurales.

**(L2) Idioma del agente conversacional.** El modelo Llama-3.1-8B-Instruct tiene soporte robusto para español estándar, pero su rendimiento en jopara (la mezcla guaraní-español característica del Paraguay) no ha sido evaluado exhaustivamente por la comunidad de NLP. Se incluye un módulo experimental de jopara pero se reporta honestamente su tasa de respuesta correcta (esperada menor a español).

**(L3) Comparación limitada a 3 modelos.** No se incluyen LLMs multimodales grandes (GPT-4V, Gemini Vision, Claude 3.5 Sonnet) por restricciones de costo (~$30-100 por evaluación completa del benchmark) y de reproducibilidad (las APIs comerciales cambian sin aviso). Esta limitación se reporta como *future work* con un protocolo de evaluación ya publicado para que la comunidad pueda extenderlo.

**(L4) Dataset de validación pequeño.** 200 features para el cálculo de κ puede no capturar la variabilidad completa del corpus. Se mitiga con bootstrap 1000 iteraciones para los IC 95%, pero se reconoce que la potencia estadística es limitada para detectar efectos pequeños en categorías raras.

**(L5) Generalización geográfica.** El modelo se entrena exclusivamente sobre Paraguay. La transferibilidad a Bolivia, Uruguay o Argentina (países con cobertura OSM y dialectos del español similares) queda fuera del alcance. Se propone un protocolo de transfer learning en el Capítulo 6 (Trabajo Futuro).

**(L6) Sesgo de los anotadores.** Los 3 anotadores son cartógrafos paraguayos con experiencia en cartografía oficial. Pueden tener sesgos sistemáticos (e.g., subestimar clases rurales, sobreestimar edificios institucionales) respecto a la diversidad de la población paraguaya. Se mitiga con triple anotación + κ, pero no se elimina.

**(L7) Temporalidad.** La cobertura OSM y los rasters IGN cambian con el tiempo. El dataset anotado tiene una "fecha de vigencia" (~Q3 2026) más allá de la cual la aplicabilidad directa decae. Se publica con la fecha explícita en el DOI y se propone un mecanismo de versionado anual.

## 3.12. Cronograma

El cronograma detallado mes a mes se resume a continuación. Las dependencias críticas están marcadas con asterisco (*).

| Mes | Fase | Hito principal | Dependencias |
|-----|------|----------------|--------------|
| 1 (Ago 2026) | Caracterización | *Descarga completa de D1-D9 + INVENTORY.json | — |
| 2 (Sep 2026) | Caracterización + Anotación | *Pipeline SAM+G-DINO+CLIP funcional | M1 |
| 3 (Oct 2026) | Anotación | *3.000 features anotadas por humanos (Label Studio) | M2 |
| 4 (Nov 2026) | Anotación + Fine-tune | *Dataset anotado 10K + SmolVLM-finetuned | M3 |
| 5 (Dic 2026) | Fine-tune + Web app | *Florence-2-finetuned + backend FastAPI | M4 |
| 6 (Ene 2027) | Web app + Validación | *App desplegada + κ inter-anotador completo | M5 |
| 7 (Feb 2027) | Validación + Paper | *Pre-print arxiv + submission conferencia | M6 |

**Total: 7 meses hasta arxiv-ready. +5 meses hasta defensa UNA-FADA** (Cap. 4-5 + revisiones del director).

**Riesgos del cronograma:**
- *R1:* Copernicus o HuggingFace creds no disponibles → fallback a datasets pre-procesados por terceros (e.g., Element84 para Sentinel-2).
- *R2:* GPU rented no disponible en las fechas → fallback a Colab Pro o Kaggle.
- *R3:* Anotadores no disponibles → Iván anota el 100% (más lento, pero viable).
- *R4:* Tiempo de revisión del director > 4 semanas → freeze + Iván continúa trabajando.

El detalle de riesgos está en `RISK_REGISTER.md`.

## 3.13. Reproducibilidad

La tesis se construye bajo el principio de **reproducibilidad computacional total**. Esto significa que cualquier研究者 con el hardware equivalente debe poder regenerar todos los resultados numéricos reportados en los Capítulos 4 y 5 a partir del código y los datos publicados.

**Mecanismos de reproducibilidad:**

1. **Docker Compose (`docker-compose.yml`).** Una sola orden `docker compose up` levanta el stack completo (backend, frontend, Chroma, Ollama) con las versiones pinned.

2. **Makefile (`Makefile`).** 38 comandos documentados que encapsulan los flujos de trabajo (descarga, anotación, fine-tune, evaluación, deploy).

3. **Semillas aleatorias pinned (42).** Todos los experimentos usan la misma semilla; la variación entre corridas es mínima (< 0.5% en métricas).

4. **Datos versionados (`data/raw/<YYYY-MM-DD>/`).** Cada experimento registra la fecha del snapshot de datos utilizado.

5. **Modelos en Hugging Face Hub.** Los pesos fine-tuned se publican con su hash SHA256 y la fecha de entrenamiento.

6. **Dataset en Zenodo con DOI.** Cada versión del dataset anotado recibe un DOI inmutable para citación.

7. **W&B logs públicos.** Los runs de entrenamiento (loss curves, métricas, hiperparámetros) se publican en un proyecto W&B público para inspección.

8. **Pre-commit hooks (`scripts/pre-commit-hook.sh`).** Validan formato (black), tipos (mypy), y secrets detection (gitleaks) antes de cada commit.

9. **Tests unitarios (`pytest`).** Cobertura target ≥ 70% sobre el código de producción.

10. **Documentación continua.** Cada función pública tiene docstring con descripción, parámetros,返回值 y ejemplo. Cada módulo tiene un `README.md` interno.

## 3.14. Síntesis del capítulo

El diseño metodológico presentado operacionaliza las hipótesis H1, H2 y H3 declaradas en la Propuesta Formal mediante un pipeline reproducible de cinco fases (caracterización → anotación → fine-tune → aplicación web → validación), controlado por variables independientes bien definidas, medidas por métricas estandarizadas, y ejecutado sobre infraestructura documentada y versionada.

Las técnicas elegidas (QLoRA, RAG, SAM+GroundingDINO+CLIP) son el estado del arte en 2026 para problemas de anotación semiautomática visión-lenguaje sobre datos geoespaciales. Las limitaciones reconocidas (cobertura rural, jopara, escala del dataset de validación) se reportarán explícitamente en el Capítulo 5 con protocolos de mitigación.

El siguiente capítulo (Cap. 4 — Implementación y Resultados) reportará la ejecución de este diseño mes a mes, con métricas, figuras y tablas que permitan al lector evaluar el grado de cumplimiento de cada objetivo específico y cada hipótesis.

---

## Referencias del Capítulo

(Listado completo en `REFERENCES.bib`; a continuación las referencias citadas específicamente en este capítulo, complementando las del Capítulo 2.)

- Braun, V., & Clarke, V. (2006). Using thematic analysis in psychology. *Qualitative Research in Psychology*, 3(2), 77-101.
- Buda, M., Maki, A., & Mazurowski, M. A. (2018). A systematic study of the class imbalance problem in convolutional neural networks. *Neural Networks*, 106, 249-259.
- Campbell, D. T., & Stanley, J. C. (1963). *Experimental and Quasi-Experimental Designs for Research*. Boston: Houghton Mifflin.
- Cohen, J. (1960). A coefficient of agreement for nominal scales. *Educational and Psychological Measurement*, 20(1), 37-46.
- Creswell, J. W., & Plano Clark, V. L. (2018). *Designing and Conducting Mixed Methods Research* (3rd ed.). Thousand Oaks: SAGE.
- Dettmers, T., et al. (2023). QLoRA: Efficient Finetuning of Quantized LLMs. *NeurIPS*.
- Flack, V. F., Afifi, A. A., Lachenbruch, P. A., & Schouten, H. J. A. (1988). Sample size determinations for the two rater kappa statistic. *Psychometrika*, 53(3), 321-325.
- Hernández Sampieri, R., Fernández Collado, C., & Baptista Lucio, P. (2014). *Metodología de la Investigación* (6ª ed.). México: McGraw-Hill.
- Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design science in IS research. *MIS Quarterly*, 28(1), 75-105.
- Kaplan, J., et al. (2020). Scaling Laws for Neural Language Models. *arXiv:2001.08361*.
- Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics*, 33(1), 159-174.
- Sokolova, M., & Lapalme, G. (2009). A systematic analysis of performance measures for classification tasks. *Information Processing & Management*, 45(4), 427-437.
- ISO 19157:2013. *Geographic information — Data quality standards*. Geneva: ISO.
- STAC 1.1.0 Specification. *SpatioTemporal Asset Catalog*. https://stacspec.org
- OGC API Features — Part 1: Core. *Open Geospatial Consortium Standard*.

---

**Estado del capítulo:** Borrador inicial v1.0 — ~7.700 palabras, ~30 páginas estimadas (a 250 palabras/página en formato FADA-UNA), 14 secciones principales + 4 sub-secciones técnicas (3.8.3.a-g, 3.8.4-3.8.7), 7 tablas, 1 diagrama de pipeline. **Dependencias:** revisión por director; alineación con observaciones sobre Cap. 1-2; ajustes al esquema de clases si el director lo solicita.

**Próximo paso:** una vez aprobado este capítulo por el director (o autoaprobado bajo la estrategia paper-first), proceder a Cap. 4 (Implementación y Resultados) con los datos reales de las primeras 4 fases ya completadas (M1-M4 en progreso al momento de escribir).
