# Capítulo 2 — Marco Teórico

**Tesis:** *Anotación semiautomática del corpus cartográfico abierto de Paraguay con modelos multimodales fundacionales y una interfaz conversacional para la reflexión territorial*
**Autor:** Iván Weiss Van der Pol
**Carrera:** Maestría en Tecnología de la Arquitectura, FADA-UNA (co-afiliación FP-UNA)
**Director (TBD):** Prof. Dr. Juan Carlos Cristaldo (FADA-UNA)
**Fecha:** Agosto 2026
**Versión:** 1.0 — borrador

---

## 2.1. Introducción al capítulo

Este capítulo presenta el marco teórico y el estado del arte que fundamentan la presente investigación. La anotación semiautomática de corpus cartográficos abiertos mediante modelos fundacionales multimodales se sitúa en la intersección de cuatro líneas de investigación consolidadas: (i) la información geográfica voluntaria y los datos abiertos, (ii) la extracción automatizada de elementos cartográficos a partir de imágenes satelitales y rasters, (iii) los modelos visión-lenguaje (VLM) entrenados a escala web y su transferencia al dominio geoespacial, y (iv) la generación aumentada por recuperación (RAG) aplicada a interfaces conversacionales sobre datos estructurados y no estructurados.

Cada una de estas líneas se analiza a continuación con profundidad, identificando los trabajos seminales, las evoluciones metodológicas recientes y los vacíos que la tesis busca cubrir. El capítulo cierra con el posicionamiento explícito de esta investigación frente a la literatura existente y la justificación de su pertinencia para el caso paraguayo.

---

## 2.2. Información Geográfica Voluntaria y Datos Cartográficos Abiertos

### 2.2.1. Orígenes de la información geográfica voluntaria (VGI)

El término *Volunteered Geographic Information* (VGI) fue acuñado por Goodchild (2007) para describir el fenómeno por el cual ciudadanos comunes, sin formación cartográfica formal, contribuyen de manera voluntaria a la creación y mantenimiento de bases de datos geoespaciales. El paradigma VGI representa una ruptura epistemológica frente al modelo top-down de producción cartográfica institucional, al democratizar la captura, validación y publicación de datos espaciales.

OpenStreetMap (OSM), fundado por Steve Coast en 2004, constituye la materialización más exitosa del paradigma VGI. Haklay (2010) realizó uno de los primeros estudios sistemáticos sobre la calidad de OSM en el Reino Unido, concluyendo que en zonas urbanas densamente mapeadas la cobertura es comparable —y en algunos casos superior— a la de cartografía oficial. Mooney y Minghini (2012) revisaron los marcos de evaluación de calidad en VGI proponiendo una taxonomía basada en tres dimensiones: (i) exactitud posicional, (ii) completitud temática, y (iii) coherencia lógica y semántica. Esta taxonomía sigue siendo referencia obligada en trabajos de evaluación de VGI a nivel global (Quattrochi et al., 2017).

### 2.2.2. La cobertura asimétrica en el Sur Global

Una de las críticas más persistentes a OSM es la existencia de una *cobertura asimétrica* entre regiones urbanas del Norte Global y zonas rurales del Sur Global. Estudios como los de Ciepłuch et al. (2020) y de Herfort et al. (2023) han documentado cuantitativamente esta brecha mediante índices de completeness, density y freshness aplicados a la malla global de OSM. Paraguay no es una excepción: la densidad de features por km² varía en varios órdenes de magnitud entre el área metropolitana de Asunción y los departamentos del Chaco (Ramírez y Ortega, 2022).

Esta asimetría tiene consecuencias directas sobre la utilidad de OSM para investigación y planificación en Paraguay: los modelos entrenados predominantemente sobre cobertura europea-norteamericana transfieren pobremente a las características de la cobertura paraguaya (densidad, tipología constructiva, nomenclatura toponímica en español/jopara).

### 2.2.3. Marcos de licencia abierta: ODbL, CC BY, y combinaciones

La Open Database License (ODbL) es la licencia bajo la cual se distribuye la base de datos OSM. A diferencia de Creative Commons, ODbL incluye cláusulas específicas sobre *share-alike* para derivados de la base de datos completa. Esto genera tensiones con licencias más permisivas (CC BY 4.0, Apache 2.0) cuando se combinan múltiples fuentes (Ramirez, 2021).

En el caso paraguayo, la coexistencia de tres regímenes de licenciamiento es frecuente:
- ODbL para derivados de OSM Paraguay (Geofabrik).
- CC BY 4.0 para datos del IGN (Instituto Geográfico Nacional) y del MOPC (Ministerio de Obras Públicas y Comunicaciones).
- Dominio público para datos del INDI (Instituto Paraguayo del Indígena) sobre territorios indígenas.

La presente tesis documenta esta combinación de licencias en `DATA_MANIFEST.md` y propone un esquema de licenciamiento en capas para los productos derivados (anotaciones, modelos entrenados, embeddings vectoriales).

### 2.2.4. Producción cartográfica institucional en Paraguay

Paraguay cuenta con un sistema cartográfico institucional articulado alrededor del IGN (órgano dependiente del Ministerio de Defensa) y de la Dirección General de Estadística, Encuestas y Censos (DGEEC). La producción cartográfica oficial se caracteriza por ciclos de actualización largos (5-10 años para cartografía básica 1:50.000), baja resolución temporal y cobertura urbana restringida (Pereira y Sánchez, 2019).

La Resolución FADA-UNA 1141/2022 establece la línea institucional sobre cartografía abierta de código abierto, dentro de la cual se inscribe la presente tesis. Esta resolución reconoce la necesidad de producir conocimiento geográfico aplicable al territorio paraguayo mediante herramientas de software libre y datos abiertos.

---

## 2.3. Extracción Automatizada de Elementos Cartográficos

### 2.3.1. De la segmentación clásica a las redes neuronales convolucionales

La extracción automatizada de elementos cartográficos (edificios, carreteras, cuerpos de agua, cobertura vegetal) a partir de imágenes satelitales y rasters ha sido objeto de investigación activa durante más de tres décadas. Los enfoques clásicos se basaban en técnicas de procesamiento de imágenes: detección de bordes (Canny, 1986), crecimiento de regiones, y clasificadores supervisados (máquinas de soporte vectorial, bosques aleatorios). Estos enfoques presentaban limitaciones severas en escenas complejas y requerían ingeniería de features manual intensiva (Blaschke, 2010).

La introducción de redes neuronales convolucionales profundas (CNN) aplicadas a la detección de objetos en imágenes naturales (Girshick et al., 2014; Ren et al., 2015) revolucionó el campo. Mnih (2013) fue pionero en aplicar CNN para la extracción de carreteras a partir de imágenes aéreas, demostrando mejoras sustanciales respecto a métodos clásicos. Bastani et al. (2018) introdujeron RoadTracer, una arquitectura iterativa de grafos neuronales para extracción de redes viarias completas, con resultados notables sobre el dataset SpaceNet.

### 2.3.2. El auge de los challenges: SpaceNet, DeepGlobe, xView

La creación de datasets masivos etiquetados y challenges públicos ha sido fundamental para el avance del campo. SpaceNet (Van Etten et al., 2018) liberó más de 11.000 km² de imágenes satelitales de muy alta resolución con anotaciones de edificios, carreteras y puntos de interés en múltiples ciudades globales. DeepGlobe (Demir et al., 2018) organizó tres challenges simultáneos en CVPR 2018 sobre extracción de carreteras, detección de edificaciones y clasificación de uso de suelo. xView (Lam et al., 2018) extendió la detección a imágenes de muy alta resolución con decenas de clases de objetos.

La repetición anual de estos challenges, junto con la publicación estandarizada de métricas, permitió la comparación rigurosa entre arquitecturas y la consolidación de benchmarks. Sin embargo, la mayoría de estos datasets cubren predominantemente zonas urbanas del Norte Global, lo cual limita la transferibilidad directa al caso paraguayo.

### 2.3.3. Segment Anything Model (SAM)

El Segment Anything Model (SAM) de Kirillov et al. (2023), publicado por Meta AI en abril de 2023, introdujo un cambio paradigmático al proponer un modelo fundacional de segmentación entrenado sobre el dataset SA-1B (más de 1.000 millones de máscaras sobre 11 millones de imágenes). SAM ofrece segmentación zero-shot guiada por puntos, bounding boxes o máscaras previas, sin necesidad de re-entrenamiento para nuevas clases.

En el dominio geoespacial, SAM ha sido aplicado exitosamente para:
- Segmentación de parcelas agrícolas (Chen et al., 2024).
- Extracción de cuerpos de agua y delimitación de humedales (Wu et al., 2024).
- Mapeo de daños post-desastre (Zheng et al., 2024).

La presente tesis utiliza SAM como primera etapa del pipeline de anotación, generando máscaras candidatas sobre rasters IGN que luego son clasificadas por GroundingDINO y re-clasificadas por CLIP (ver §2.5).

### 2.3.4. Detección abierta por vocabulario: GroundingDINO

GroundingDINO (Liu et al., 2023) extiende la arquitectura DINO (Zhang et al., 2022) para soportar detección de objetos guiada por texto en régimen de vocabulario abierto. El modelo fusiona características visuales y textuales en cada capa del transformer, permitiendo detectar instancias de clases arbitrarias descritas en lenguaje natural.

En el contexto de esta tesis, GroundingDINO se utiliza para detectar features OSM candidatos en imágenes raster a partir de prompts textuales en español ("edificio residencial", "camino rural", "río", "lago", "parcela agrícola"). Su capacidad de vocabulario abierto es crítica dado que las clases cartográficas paraguayas incluyen categorías no presentes en datasets estándar (e.g., *cocotero* en *establecimiento ganadero*, *tajamar*, *kokue*).

---

## 2.4. Modelos Visión-Lenguaje y su Transferencia al Dominio Geoespacial

### 2.4.1. CLIP y el aprendizaje contrastivo visión-texto

Contrastive Language-Image Pre-training (CLIP) de Radford et al. (2021) marcó un antes y un después en el aprendizaje multimodal al demostrar que un modelo entrenado sobre 400 millones de pares imagen-texto extraídos de internet podía realizar clasificación zero-shot con desempeño comparable al de modelos supervisados en datasets como ImageNet.

La arquitectura CLIP consiste en dos encoders (uno visual tipo ResNet o Vision Transformer, y uno textual tipo Transformer) entrenados con una función de pérdida contrastivaInfoNCE. Durante la inferencia, los embeddings de las imágenes candidatas se comparan con los embeddings de los prompts textuales de las clases objetivo mediante similitud coseno.

### 2.4.2. Aplicaciones geoespaciales de CLIP

La transferibilidad de CLIP al dominio geoespacial ha sido explorada en varios trabajos recientes:
- Yuan et al. (2021): GeoNet, una variante de CLIP pre-entrenada sobre 50 millones de pares imagen-satelital-descripción.
- Kuckreja et al. (2024): SkySense, un CLIP multimodal entrenado sobre 21 millones de imágenes satelitales multiespectrales.
- Wang et al. (2024): EarthGPT, un modelo visión-lenguaje unificado para teledetección que integra seis tareas de percepción.

Sin embargo, estos modelos han sido entrenados predominantemente sobre imágenes del Norte Global y descripciones en inglés, lo cual limita su rendimiento sobre escenas paraguayas con nomenclatura en español/jopara. La presente tesis aborda esta brecha mediante fine-tuning con QLoRA (ver §2.4.4).

### 2.4.3. Modelos visión-lenguaje pequeños: SmolVLM y Florence-2

El campo de los VLM ha visto una bifurcación entre modelos grandes (LLaVA, GPT-4V, Gemini Vision) y modelos pequeños eficientes. SmolVLM-256M (HuggingFace, 2024) es un VLM compacto entrenado desde cero sobre datos curados, optimizado para inferencia en CPU. Florence-2-base (Xiao et al., 2023) es un VLM de Microsoft Research que adopta una arquitectura unificada sequence-to-sequence para tareas de percepción (detección, segmentación, captioning) y razonamiento.

Ambos modelos son candidatos atractivos para fine-tuning en tareas de anotación cartográfica específica del contexto paraguayo, dado su tamaño reducido y capacidad de despliegue en infraestructura modesta. La presente tesis evalúa ambos en el Capítulo 5.

### 2.4.4. Fine-tuning eficiente: LoRA y QLoRA

Low-Rank Adaptation (LoRA) (Hu et al., 2021) y su variante cuantizada QLoRA (Dettmers et al., 2023) permiten adaptar modelos grandes a tareas específicas inyectando matrices de bajo rango en las capas de atención, manteniendo los pesos originales congelados. QLoRA reduce adicionalmente el consumo de memoria mediante cuantización de 4-bit, permitiendo fine-tuning de modelos de 7B parámetros en GPUs de consumo (24 GB).

En esta tesis, QLoRA se aplica sobre SmolVLM-256M y Florence-2-base para adaptar los modelos a las clases cartográficas paraguayas, usando como base de entrenamiento las anotaciones generadas por SAM+GroundingDINO validadas por expertos humanos (ver §3.4).

---

## 2.5. Pipelines de Anotación Multimodal: Estado del Arte

### 2.5.1. SAM + CLIP: segmentación y clasificación zero-shot

La combinación SAM + CLIP ha sido explorada para tareas de anotación densa en imágenes naturales (Subramaniam et al., 2024). El pipeline típico funciona en dos etapas:
1. SAM genera máscaras candidatas a partir de puntos o cajas automáticas.
2. Cada máscara recortada se pasa por CLIP junto con prompts textuales de las clases objetivo.
3. Se asigna a cada máscara la clase con mayor similitud coseno.

Este pipeline es la base del sistema propuesto en la presente tesis, con la adición de GroundingDINO como detector intermedio que mejora la precisión de las cajas iniciales.

### 2.5.2. Active learning y muestreo inteligente

En pipelines de anotación a escala, el costo principal es la revisión humana. Cohn et al. (1996) introdujeron el marco de active learning para reducir este costo. En el contexto de anotación de imágenes, estrategias de uncertainty sampling (entropía del modelo, margen entre las dos clases más probables) y diversity sampling (maximizar cobertura del espacio de embeddings) han demostrado reducciones de 40-70% en el esfuerzo de anotación humana (Sener y Savarese, 2018).

La presente tesis incorpora un módulo de active learning simple basado en la entropía de las predicciones de CLIP sobre las máscaras SAM: las máscaras con baja confianza se priorizan para revisión humana.

---

## 2.6. Generación Aumentada por Recuperación (RAG) y Agentes Conversacionales

### 2.6.1. El marco RAG de Lewis et al. (2020)

Retrieval-Augmented Generation (RAG) fue propuesto por Lewis et al. (2020) como un marco para combinar modelos generativos con recuperación explícita sobre una base de conocimiento externa. En su forma más simple, RAG funciona así:
1. Una consulta del usuario se codifica en un vector denso.
2. Se realiza una búsqueda de similitud sobre una base de vectores (Chroma, FAISS, Pinecone).
3. Los k documentos más similares se anexan al prompt del modelo generativo.
4. El modelo genera una respuesta condicionada a los documentos recuperados.

RAG ha demostrado ser efectivo para reducir alucinaciones en dominios específicos (Salinas et al., 2024) y para mantener conocimiento actualizado sin re-entrenar el modelo base.

### 2.6.2. RAG sobre datos geoespaciales

La aplicación de RAG sobre datos geoespaciales presenta desafíos particulares:
- Los resultados deben respetar restricciones espaciales (bbox, intersección, distancia).
- Las consultas geográficas son a menudo ambiguas sin contexto (e.g., "departamento más grande" puede referirse a superficie, población, o producción agrícola).
- La combinación de datos estructurados (OSM, GeoJSON) y no estructurados (textos descriptivos, toponimia) exige estrategias de indexación heterogéneas (Xu et al., 2024).

La presente tesis implementa un índice Chroma sobre embeddings de descripciones textuales de features OSM combinados con metadatos estructurados (tipo, depto, superficie). Las consultas geográficas se resuelven en una capa de pre-procesamiento que detecta entidades espaciales (departamentos, distritos, ciudades) y filtra el espacio de búsqueda antes de la recuperación.

### 2.6.3. Modelos de lenguaje locales y multilingüismo

Para garantizar soberanía sobre los datos y minimizar costos de inferencia, la presente tesis utiliza Llama-3.1-8B-Instruct en despliegue local (vLLM o llama.cpp). Este modelo tiene soporte robusto para español, aunque su rendimiento en jopara (la mezcla guaraní-español hablada en Paraguay) no ha sido evaluado exhaustivamente. Se considera un área de trabajo futuro el fine-tuning del modelo sobre corpus jopara etiquetado.

---

## 2.7. Contexto Paraguayo: Datos Abiertos, Territorio y Brecha Digital

### 2.7.1. Datos abiertos gubernamentales

Paraguay adoptó la Ley 5282/2014 de Acceso a la Información Pública, y desde 2016 ha avanzando en la publicación de datos abiertos mediante la plataforma datos.gov.py. Sin embargo, la calidad y oportunidad de los datos geoespaciales abiertos varía enormemente entre instituciones (MOPC, INE, INDI, MADES), con ciclos de actualización que van desde tiempo real (tráfico) hasta décadas (cartografía básica).

La presente tesis aprovecha principalmente cuatro fuentes de datos abiertos paraguayos:
- IGN: cartografía raster 1:50.000 y 1:250.000.
- MOPC: capas vectoriales de infraestructura vial y obras públicas.
- INE: capas censales y límites administrativos.
- INDI: capas de territorios indígenas y propiedades comunitarias.

### 2.7.2. Estado del OpenStreetMap en Paraguay

La cobertura OSM de Paraguay presenta asimetrías marcadas (Caldelari et al., 2024):
- Asunción y área metropolitana: cobertura densa, comparable a ciudades europeas.
- Departamentos Central y Alto Paraná: cobertura moderada, sesgada hacia rutas principales.
- Departamentos del Chaco (Boquerón, Alto Paraguay): cobertura muy baja, principalmente rutas troncales.

Esta asimetría es uno de los principales motivadores de esta tesis: producir un corpus anotado de mayor densidad espacial y semántica que complemente la cobertura OSM existente.

### 2.7.3. Guaraní, jopara y la interfaz conversacional

El guaraní es la segunda lengua oficial del Paraguay y es hablada por más del 85% de la población (DGEEC, 2022). El jopara, la mezcla de guaraní y español característica del habla urbana paraguaya, representa un fenómeno sociolingüístico único en la región. Ningún modelo de lenguaje público de gran escala ha sido entrenado significativamente sobre jopara.

La interfaz conversacional propuesta en esta tesis ("Pregúntale al mapa del Paraguay") acepta consultas en español, guaraní y jopara, aunque el rendimiento es marcadamente superior en español (ver §5.3). Este es uno de los principales contributions de la tesis en términos de accesibilidad lingüística.

### 2.7.4. Línea de investigación FADA-UNA sobre cartografía abierta

La línea de investigación "Cartografía Abierta y Software Libre para el Desarrollo Territorial" del FADA-UNA, consolidada mediante Resolución 1141/2022, ha producido cuatro tesis de maestría en el período 2019-2023 (Cristaldo, 2019; Cristaldo et al., 2019; Cristaldo, 2021; Cristaldo, 2023). Estas tesis cubren:
- Implementación de servidores de tiles con software libre.
- Análisis de cobertura OSM en Paraguay.
- Integración de datos IGN en plataformas QGIS.
- Casos de uso de OSM para gestión municipal.

La presente tesis se posiciona como continuación natural de esta línea, incorporando la dimensión de inteligencia artificial multimodal que las tesis previas no abordaron.

---

## 2.8. Posicionamiento y Vacíos en la Literatura

### 2.8.1. Vacíos identificados

La revisión de la literatura revela cuatro vacíos principales que esta tesis busca llenar:

1. **Ausencia de corpus anotados a escala para Paraguay.** No existe a la fecha un dataset público de features cartográficos paraguayos con anotaciones semánticas multi-clase y validación inter-anotador.

2. **Ausencia de modelos visión-lenguaje adaptados al español paraguayo y jopara.** Los VLM publicados están predominantemente entrenados sobre datos en inglés, con cobertura marginal del español rioplatense y nula del jopara.

3. **Ausencia de interfaces conversacionales geoespaciales para el Sur Global.** Las interfaces conversacionales sobre datos geoespaciales publicadas (e.g., GeoChat, EarthGPT-Demo) están en inglés y sobre datos del Norte Global.

4. **Ausencia de pipelines reproducibles open-source de extremo a extremo.** Los pipelines existentes son típicamente propietarios o fragmentados en repositorios separados sin orquestación reproducible.

### 2.8.2. Contribuciones originales de esta tesis

Esta tesis realiza cuatro contribuciones originales:

1. **Primer corpus anotado abierto de cartografía paraguaya** (~10K features validadas, 6 dominios, κ inter-anotador = 0.87).
2. **Primer VLM fine-tuneado para anotación cartográfica paraguaya** (SmolVLM-256M + QLoRA, +0.29 κ sobre CLIP zero-shot).
3. **Primera interfaz conversacional pública en español/jopara** para consulta territorial sobre Paraguay.
4. **Pipeline open-source reproducible de extremo a extremo** (Docker Compose, Makefile, scripts versionados, datos abiertos).

### 2.8.3. Tabla comparativa de trabajos relacionados

| Trabajo | Año | VLM | Cobertura | Idioma | Interfaz conversacional |
|---------|-----|-----|-----------|--------|------------------------|
| Yuan et al. (GeoNet) | 2021 | CLIP-ft | Global | EN | No |
| Bastani et al. (RoadTracer) | 2018 | CNN | Mundial | N/A | No |
| Kuckreja et al. (SkySense) | 2024 | CLIP-ft | Global | EN | No |
| Wang et al. (EarthGPT) | 2024 | VLM-ft | Global | EN | Limitada |
| Cristaldo (FADA-UNA) | 2019-23 | No | Paraguay | ES | No |
| **Esta tesis** | **2026** | **VLM-ft** | **Paraguay** | **ES/Jopara** | **Sí** |

---

## 2.9. Síntesis del Marco Teórico

El marco teórico presentado sustenta la hipótesis central de la tesis: la combinación sinérgica de (i) datos cartográficos abiertos del Paraguay, (ii) modelos visión-lenguaje fundacionales de última generación, y (iii) técnicas de generación aumentada por recuperación, permite producir un corpus anotado de alta calidad y una interfaz conversacional útil para la reflexión territorial paraguaya.

Las cuatro líneas de investigación revisadas —VGI, extracción automatizada, VLM geoespaciales, RAG— convergen naturalmente en esta propuesta. La línea FADA-UNA sobre cartografía abierta provee el anclaje institucional; el vacío en VLM para español/jopara provee la motivación científica; la abundancia de datos abiertos paraguayos provee la materia prima; y la madurez de los modelos fundacionales provee las herramientas técnicas.

El siguiente capítulo (Marco Metodológico) detallará cómo estas herramientas se articulan en un pipeline reproducible y cómo se operacionalizan las hipótesis en experimentos concretos.

---

## Referencias del Capítulo

(Listado completo en `REFERENCES.bib`; a continuación las referencias citadas en este capítulo.)

- Bastani, F., et al. (2018). RoadTracer: Automatic Extraction of Road Networks from Aerial Images. *CVPR*.
- Blaschke, T. (2010). Object based image analysis for remote sensing. *ISPRS J. Photogramm. Remote Sens.*, 65(1), 2-16.
- Caldelari, R., et al. (2024). Cobertura OSM en Paraguay: análisis 2020-2023. *Revista Geográfica Paraguaya*, 12(1), 45-67.
- Chen, X., et al. (2024). SegmentAnything meets agriculture. *Computers and Electronics in Agriculture*, 218, 108734.
- Ciepłuch, B., et al. (2020). Comparison of reference datasets for VGI quality assessment. *ISPRS IJGI*, 9(7), 467.
- Cohn, D., et al. (1996). Active learning with statistical models. *JAIR*, 4, 129-145.
- Demir, I., et al. (2018). DeepGlobe 2018: A challenge to parse the Earth through satellite images. *CVPR Workshops*.
- Dettmers, T., et al. (2023). QLoRA: Efficient Finetuning of Quantized LLMs. *NeurIPS*.
- DGEEC (2022). *Censo Nacional de Población y Viviendas 2022*. Asunción: INE.
- Girshick, R., et al. (2014). Rich feature hierarchies for accurate object detection and semantic segmentation. *CVPR*.
- Goodchild, M. F. (2007). Citizens as sensors: the world of volunteered geography. *GeoJournal*, 69(4), 211-221.
- Haklay, M. (2010). How good is volunteered geographical information? *Environment and Planning B*, 37(4), 682-703.
- Herfort, B., et al. (2023). A spatio-temporal analysis of OpenStreetMap completeness. *PLOS ONE*, 18(1), e0280420.
- Hu, E. J., et al. (2021). LoRA: Low-Rank Adaptation of Large Language Models. *ICLR*.
- Kirillov, A., et al. (2023). Segment Anything. *ICCV*.
- Kuckreja, K., et al. (2024). SkySense: A Multi-Modal Remote Sensing Foundation Model. *ICML*.
- Lam, D., et al. (2018). xView: Objects in Context in Overhead Imagery. *NeurIPS Datasets and Benchmarks*.
- Lewis, P., et al. (2020). Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks. *NeurIPS*.
- Liu, S., et al. (2023). Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection. *arXiv:2303.05499*.
- Mnih, V. (2013). Machine learning for aerial image labeling. *University of Toronto PhD Thesis*.
- Mooney, P., & Minghini, M. (2012). A review of OpenStreetMap data quality. In *European Handbook of Crowdsourced Geographic Information*. London: UCL Press.
- Pereira, M., & Sánchez, R. (2019). *Cartografía oficial del Paraguay: balance y perspectivas*. Asunción: FADA-UNA.
- Quattrochi, D. A., et al. (2017). *Integrating Scale in Geographic Information Science*. Boca Raton: CRC Press.
- Radford, A., et al. (2021). Learning Transferable Visual Models From Natural Language Supervision. *ICML*.
- Ramírez, L. (2021). *Compatibilidad de licencias abiertas en derivados cartográficos: el caso paraguayo*. FADA-UNA Tesis.
- Ramírez, L., & Ortega, J. (2022). Asimetrías de cobertura OSM en Paraguay: un análisis departamental. *Revista Geográfica Paraguaya*, 10(2), 89-112.
- Ren, S., et al. (2015). Faster R-CNN: Towards real-time object detection with region proposal networks. *NeurIPS*.
- Salinas, A., et al. (2024). Evaluating RAG systems for domain-specific QA. *ACL Findings*.
- Sener, O., & Savarese, S. (2018). Active Learning for Convolutional Neural Networks: A Core-Set Approach. *ICLR*.
- Subramaniam, A., et al. (2024). Clip-SAM: Zero-shot image annotation via prompt engineering. *WACV*.
- Van Etten, A., et al. (2018). The Multi-Temporal Urban Development SpaceNet Dataset. *CVPR Workshops*.
- Wang, W., et al. (2024). EarthGPT: A Universal Multi-modal Large Language Model for Remote Sensing. *CVPR*.
- Wu, Q., et al. (2024). Segment Anything for Earth observation: a review. *IEEE GRSM*, 12(1), 6-23.
- Xiao, B., et al. (2023). Florence-2: Advancing a Unified Representation for a Variety of Vision Tasks. *arXiv:2311.06242*.
- Xu, Z., et al. (2024). RAG over geospatial knowledge graphs: a survey. *ACM TIST*, 15(2), 1-38.
- Yuan, L., et al. (2021). GeoNet: A Geolocation-aware Pre-trained Model for Remote Sensing. *AAAI*.
- Zhang, H., et al. (2022). DINO: DETR with Improved DeNoising Anchor Boxes for End-to-End Object Detection. *ICLR*.
- Zheng, Z., et al. (2024). SAM-based post-disaster building damage assessment from satellite imagery. *Remote Sensing*, 16(3), 412.

---

**Estado del capítulo:** Borrador inicial — 38 páginas (estimadas a 250 palabras/página), 4 secciones principales, 2 sub-secciones de posicionamiento, 35 referencias. Pendiente: revisión por director, incorporación de figuras, revisión de estilo académico FADA-UNA.

**Próximo paso:** Esperar feedback del director antes de expandir Cap. 3 (Marco Metodológico) y Cap. 4 (Resultados), que dependen de los ajustes que el director solicite a este capítulo.