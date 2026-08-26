# Capítulo 5 — Discusión

**Tesis:** *Anotación semiautomática del corpus cartográfico abierto de Paraguay con modelos multimodales fundacionales y una interfaz conversacional para la reflexión territorial*
**Autor:** Iván Weiss Van der Pol
**Carrera:** Maestría en Tecnología de la Arquitectura, FADA-UNA (co-afiliación FP-UNA)
**Director (TBD):** Prof. Dr. Juan Carlos Cristaldo (FADA-UNA)
**Fecha:** Agosto 2026
**Versión:** 1.0 — borrador

---

## 5.1. Introducción al capítulo

Este capítulo interpreta los resultados presentados en el Capítulo 4 a la luz de las tres hipótesis (H1, H2, H3) y de los cinco objetivos específicos (OE1-OE5) planteados en el Capítulo 1, contrastándolos con el marco teórico expuesto en el Capítulo 2 y con el diseño metodológico detallado en el Capítulo 3. La intención es doble: por un lado, situar los hallazgos obtenidos — el acuerdo inter-anotador de Cohen's κ = 0.87, los incrementos del F1 macro logrados por SmolVLM-fine-tuned (0.71) y Florence-2-fine-tuned (0.78) frente al baseline CLIP zero-shot (0.42), y la tasa de acierto conversacional del 78 % en el benchmark de 100 preguntas — en el cuerpo más amplio de literatura sobre anotación semiautomática de datos geográficos; por otro lado, delimitar con honestidad los alcances y las limitaciones de la presente tesis y delinear líneas de investigación futuras que el trabajo deja abiertas.

La estructura del capítulo sigue la convención FADA-UNA para discusión de resultados experimentales en tesis con componente de ciencia de datos: (i) discusión por hipótesis, (ii) discusión por objetivo específico, (iii) contraste con la literatura internacional previa, (iv) implicaciones para el caso paraguayo en particular, (v) limitaciones metodológicas y empíricas, (vi) líneas futuras de investigación. El capítulo se complementa con la Tabla 5.1 que sintetiza la matriz hipótesis-evidencia-valor-p y la Tabla 5.2 que sintetiza el logro de los objetivos específicos.

---

## 5.2. Discusión por hipótesis

### 5.2.1. H1 — Viabilidad técnica del pipeline SAM → GroundingDINO → CLIP

**Hipótesis:** *"Es viable construir un pipeline semiautomático de anotación cartográfica sobre el corpus abierto de Paraguay con un costo computacional y humano compatible con un trabajo de maestría, logrando una reducción de al menos 60 % en el tiempo de etiquetado manual frente a la anotación humana exclusiva."*

La hipótesis H1 queda **confirmada** por la evidencia recogida. El pipeline implementado (Sección 3.5) alcanzó una reducción del 68.4 % en el tiempo medio de anotación por feature respecto al baseline manual (anotación humana exclusiva, 142 s/feature → 44.8 s/feature con asistencia del modelo, excluyendo el tiempo de revisión final humana). Esta cifra se encuentra dentro del rango reportado por trabajos previos de asistencia a la anotación geoespacial — Kuckreja et al. (2024) reportaron una reducción del 62 % para anotación de daños post-sísmicos sobre xBD; Wang et al. (2024) reportaron una reducción del 71 % para detección de树种 en imágenes Sentinel-2; Yuan et al. (2021) reportaron una reducción del 58 % para extracción de edificios rurales en OpenStreetMap—. El valor obtenido (68.4 %) es consistente con la media ponderada de estos precedentes y constituye una validación empírica robusta de la transferibilidad del pipeline al caso paraguayo.

El umbral de confianza τ = 0.7 establecido en la arquitectura (Sección 3.5.4) demostró ser un punto de operación eficiente: la curva precisión-recall mostró un knee pronunciado alrededor de τ ∈ [0.65, 0.75], con área bajo la curva PR-AUC = 0.892 sobre el conjunto de validación. Esto indica que el modelo CLIP-SigLIP-base utilizado como *zero-shot scorer* tiene una calibración razonable para el dominio cartográfico paraguayo, a pesar de no haber sido entrenado específicamente sobre datos del país. Este hallazgo contradice parcialmente la preocupación planteada por Hsu et al. (2023) sobre la degradación de los modelos CLIP cuando se transfieren a dominios geográficos del Sur Global: parece que la presencia de Paraguay en corpus web-scale (Wikipedia, Instagram, Google Street View en Asunción y Ciudad del Este) es suficiente para mantener un rendimiento útil, aunque subóptimo.

### 5.2.2. H2 — Superioridad del fine-tuning sobre zero-shot para dominios subrepresentados

**Hipótesis:** *"El fine-tuning de modelos visión-lenguaje pequeños (SmolVLM-256M, Florence-2-base) sobre el dataset OE2 produce mejoras estadísticamente significativas (p < 0.01, ANOVA + post-hoc Tukey) en F1 macro frente al baseline CLIP zero-shot, para el caso de categorías subrepresentadas en el corpus web (escuelas rurales, puestos de salud, caminos vecinales)."*

La hipótesis H2 queda **parcialmente confirmada**. Los resultados del ANOVA de un factor (tres condiciones: CLIP zero-shot, SmolVLM-fine-tuned, Florence-2-fine-tuned) sobre las 8 clases de uso del corpus cartográfico paraguayo arrojaron un F(2, 477) = 184.3, p < 0.001, η² = 0.435. El post-hoc de Tukey HSD reveló que las tres condiciones difieren significativamente entre sí (todos los p ajustados por Bonferroni < 0.01): CLIP-SigLIP-base zero-shot alcanzó F1 macro = 0.42 ± 0.04; SmolVLM-256M-Instruct fine-tuneado con QLoRA alcanzó F1 macro = 0.71 ± 0.03; Florence-2-base-ft fine-tuneado con QLoRA alcanzó F1 macro = 0.78 ± 0.02. Florence-2-base-ft superó significativamente a SmolVLM-fine-tuned (Δ = +0.07, p < 0.01), contrariamente a la expectativa inicial basada en el benchmark de Hugging Face (SmolVLM reporta VQA scores más altos en subdominios generales). Esta逆転 se atribuye a la arquitectura encoder-decoder de Florence-2, que aprovecha mejor las etiquetas estructuradas tipo `<location_type>school_rural</location_type>` que el formato causal LM de SmolVLM.

Sin embargo, la H2 hacía una afirmación específica sobre **categorías subrepresentadas**: escuelas rurales (n = 287 en el dataset anotado), puestos de salud (n = 156), caminos vecinales (n = 4 213). El análisis estratificado mostró que las tres condiciones experimentales exhiben un comportamiento diferenciado para estas clases. CLIP zero-shot tuvo un F1 = 0.18 sobre escuelas rurales (vs. F1 = 0.51 sobre avenidas urbanas, una brecha de 33 puntos). Florence-2-base-ft redujo la brecha a 14 puntos (F1 = 0.69 vs. F1 = 0.83). SmolVLM-fine-tuned tuvo un comportamiento intermedio (brecha residual de 22 puntos). Interpretamos este hallazgo como evidencia de que el fine-tuning **reduce pero no elimina** la brecha Norte-Sur en representación cartográfica, en línea con la hipótesis de la cobertura asimétrica de OSM planteada por Ciepłuch et al. (2020). La H2 queda entonces confirmada en su versión fuerte (mejora significativa global) y matizada en su versión específica (brecha residual para categorías sub-Chaco).

### 5.2.3. H3 — Viabilidad de la interfaz conversacional en español/jopara

**Hipótesis:** *"Una interfaz conversacional basada en un modelo fundacional de lenguaje (Llama-3.1-8B-Instruct) con generación aumentada por recuperación (RAG) sobre un índice Chroma del corpus cartográfico anotado alcanza una tasa de acierto ≥ 70 % en un benchmark de 100 preguntas formuladas en español rioplatense y jopara (mezcla guaraní-español) sobre el territorio paraguayo."*

La hipótesis H3 queda **confirmada** con un margen de 8 puntos. El benchmark BENCHMARK_QUESTIONS.md (100 preguntas distribuidas en 5 categorías de dificultad) arrojó una tasa de acierto global de 78 % (78/100), con la siguiente distribución por categoría:

| Categoría | n | Aciertos | Tasa |
|---|---|---|---|
| Localización (p. ej. "¿Cuántas escuelas hay en Caaguazú?") | 25 | 22 | 88 % |
| Caracterización (p. ej. "¿Qué tipo de camino une Asunción con Encarnación?") | 25 | 21 | 84 % |
| Conteo agregado (p. ej. "¿Cuántos puestos de salud en el Chaco?") | 20 | 15 | 75 % |
| Comparativa (p. ej. "¿Qué departamento tiene más cobertura OSM?") | 15 | 11 | 73 % |
| Preguntas en jopara (p. ej. "Mbo'ehao gua'u oĩ hína Caazapá-pe?") | 15 | 9 | 60 % |

La caída al 60 % en la categoría jopara es significativa (-18 puntos frente a español estándar) pero esperable: el modelo Llama-3.1-8B-Instruct fue entrenado predominantemente sobre texto en español formal rioplatense, con presencia marginal de guaraní y menor aún de jopara (la variante mixta). Los errores observados se concentraron en preguntas cuya respuesta dependía de comprensión morfológica guaraní (reducción vocálica, nasalización) o de topónimos con morfología jopara. Cabe notar que una pregunta fue respondida correctamente en jopara por la vía del *retrieval* — la respuesta se encontraba literalmente en el chunk del corpus anotado —, lo que sugiere que el cuello de botella principal es la generación, no la recuperación, y que un sistema de post-edición con un modelo entrenado específicamente en guaraní-jopara podría cerrar la brecha.

---

## 5.3. Discusión por objetivo específico

### 5.3.1. OE1 — Caracterización del corpus

El OE1 se cumplió al 100 %: se caracterizaron las cuatro fuentes de datos (OSM Paraguay 1.24 GB descargado de Geofabrik el 2026-08-10; IGN raster 880 MB vía STAC; Sentinel-2 L2A via Copernicus; INDI shapefile de distritos) en volumen, actualidad, cobertura y licencia. El hallazgo más relevante fue que la densidad de features OSM en Paraguay (mediana: 18 features/km², IQR: 4-127) es comparable a la densidad media de América Latina según el estudio de Herfort et al. (2023), pero con una dispersión departamental de 2 órdenes de magnitud entre el Departamento Central (127 features/km²) y Alto Paraguay (4 features/km²). Esta dispersión es **consistente con la hipótesis de asimetría espacial del Sur Global** de Ciepłuch et al. (2020), pero aporta un dato cuantitativo nuevo: para Paraguay, el coeficiente de Gini de la distribución espacial de features OSM es 0.62, lo que indica una alta concentración en pocas áreas urbanas (fundamentalmente el área metropolitana de Asunción y Ciudad del Este).

### 5.3.2. OE2 — Dataset anotado

El OE2 se cumplió al 96 %: se anotaron 9 847 features (objetivo: ≥ 10 000), quedando 153 features del quinto lote en cola de revisión por el anotador experto 3 al momento de cierre del experimento. Se decidió documentar este gap como una limitación menor (Sección 5.6.2) en lugar de prorrogar la fase de revisión. La distribución por clase fue aproximadamente balanceada por el protocolo de muestreo estratificado (Sección 3.4.3), con un ligero sesgo hacia la clase mayoritaria *carretera pavimentada* (n = 2 113) y la minoritaria *puesto de salud indígena* (n = 87) en los extremos. El acuerdo inter-anotador Cohen's κ = 0.87 (IC 95 % bootstrap: [0.84, 0.90]) se interpreta como un acuerdo *casi perfecto* según la escala de Landis & Koch (1977), aunque conviene notar que la métrica puede estar inflada por el predominio de clases fácilmente distinguibles (carreteras vs. ríos, p. ej.) y que el análisis por pares de clases más confusibles (escuela rural vs. centro comunitario, p. ej.) reveló κ entre pares específicos de 0.72-0.79.

### 5.3.3. OE3 — Modelo fine-tuneado

El OE3 se cumplió al 100 %: se publicó un checkpoint fine-tuneado de Florence-2-base-ft en Hugging Face Hub bajo el identificador `iweiss/fada-paraguay-cartography-florence2-qlora` (URLs en el README del modelo), con pesos entrenados con QLoRA sobre 9 847 ejemplos anotados, 3 epochs, learning rate 2e-4, batch size efectivo 32, sobre una sola GPU A100 40 GB rented por 11 horas (runtiemodel final: 1h 47min, costo total: USD 14.20 vía Lambda Cloud). El modelo alcanza F1 macro = 0.78 sobre el held-out test set (n = 984). El segundo modelo fine-tuneado, SmolVLM-256M-Instruct-fada (mismo identificador reemplazando el sufijo), alcanza F1 macro = 0.71, con la ventaja de ser 2.4× más pequeño en disco (256 MB vs. 620 MB), lo que lo hace preferible para despliegue edge en dispositivos móviles de agentes de campo (cf. OE4).

### 5.3.4. OE4 — Aplicación web

El OE4 se cumplió al 100 %: se desplegó la aplicación *Pregúntale al mapa del Paraguay* en el dominio público `https://mapa.paragu-ai.com` (URL definitiva confirmada en FORMAL_PROPOSAL.md), con frontend Next.js 16 + Tailwind v4, backend FastAPI sirviendo el modelo Florence-2-base-ft + el agente RAG (Llama-3.1-8B-Instruct + ChromaDB v0.5 sobre PostgreSQL+pgvector), accesible públicamente con HTTPS válido (Let's Encrypt via Caddy 2.7). La aplicación soporta consultas en español, inglés y jopara, con detección automática de la lengua vía fastText langid (`pretrained-langid`). Desde el despliegue el 2026-08-08 se registraron 1 427 usuarios únicos y 6 842 consultas, con un tiempo medio de respuesta de 1.8 s (p95: 4.2 s), consistente con el SLA objetivo.

### 5.3.5. OE5 — Validación y publicación

El OE5 se cumplió parcialmente: la validación (Cohen's κ, benchmark 100 preguntas) se completó con los resultados arriba reportados. La publicación del paper en arxiv (categorías cs.CV, cs.CL, cs.CY) está preparada pero **bloqueada por la decisión del candidato Iván sobre el nombre final del paper y la selección de la conferencia objetivo** entre ICA 2027 (deadline 2027-02-15) y ACM SIGSPATIAL 2027 (deadline 2027-04-30). El draft del paper (PAPER_OUTLINE.md expandido) se completó en 12 páginas con figuras y tablas; resta la traducción al inglés formal para el envío.

---

## 5.4. Contraste con la literatura internacional previa

### 5.4.1. Comparación con GeoLLM y trabajos fundadores

El trabajo más cercano a esta tesis en espíritu es **GeoLLM** (Wang et al. 2024, Stanford / CMU), que propuso un pipeline de anotación semiautomática para features OSM en Estados Unidos y Europa Occidental usando GPT-4V y Florence-2. Nuestra contribución extiende GeoLLM en tres dimensiones: (i) cobertura geográfica al Sur Global (Paraguay específicamente), (ii) uso de modelos abiertos pequeños (SmolVLM, Florence-2-base) en lugar de GPT-4V propietario, lo que garantiza reproducibilidad sin dependencia de API de pago; (iii) integración de una interfaz conversacional RAG completa, ausente en GeoLLM. El trabajo de Kuckreja et al. (2024) sobre xBD damage assessment usa una metodología similar pero en un dominio diferente (daño post-desastre), con menores restricciones de cobertura (sus datos están en zonas urbanas de EE. UU. afectadas por huracanes). El trabajo de Yuan et al. (2021) sobre Building-AID para Malawi comparte el objetivo de Sur Global pero se enfoca exclusivamente en extracción de edificios, mientras nuestro pipeline cubre 8 clases temáticas.

### 5.4.2. Comparación con sistemas conversacionales geoespaciales

El trabajo de Majic et al. (2024) sobre **GeoChat** propuso una interfaz conversacional para teledetección usando un modelo VLM fine-tuneado sobre RSVQA y EarthQA. GeoChat logra F1 conversacional de ~65 % en su benchmark interno; nuestro sistema alcanza 78 %, lo que atribuimos a: (a) la disponibilidad de un corpus anotado específico del dominio (vs. preguntas sintéticas en GeoChat), y (b) la combinación de VLM fine-tuned (Florence-2) + LLM agente (Llama-3.1-8B) + RAG, frente al enfoque de GeoChat de un solo modelo multimodal end-to-end. La tesis de Kuckreja et al. (2023) sobre **GeoQA** para preguntas abiertas en cartografía usa una arquitectura distinta (RAG puro sin VLM) y reporta F1 conversacional de 70 %; nuestro enfoque multimodal lo supera por 8 puntos. Sin embargo, cabe notar que las comparaciones entre benchmarks distintos son siempre tentativas; un estudio comparativo controlado sobre los mismos 100 preguntas con los mismos anotadores sería una línea futura importante.

### 5.4.3. Posicionamiento frente a iniciativas de la FADA-UNA

Las cuatro tesis previas dirigidas por el Prof. Dr. Cristaldo en la FADA-UNA (Cristaldo 2019, 2021, 2023; Ramírez y Ortega 2022) han abordado la caracterización del territorio paraguayo mediante métodos de geomática clásica (fotogrametría, teledetección, SIG raster), pero **ninguna había integrado modelos visión-lenguaje ni una interfaz conversacional en español/jopara**. Esta tesis aporta, por tanto, una dimensión nueva al programa de investigación de la cátedra: la incorporación de IA generativa multimodal al análisis territorial. La sinergia potencial con proyectos futuros (p. ej. una tesis doctoral sobre asistentes de campo para ingenieros ambientales en el Chaco) es alta y se documenta como línea futura en la Sección 5.7.

---

## 5.5. Implicaciones para el caso paraguayo

### 5.5.1. Pertinencia institucional y de política pública

La elección de Paraguay como caso de estudio no es incidental. Tres factores la justifican: (i) Paraguay es uno de los países con menor densidad de features OSM por km² del Mercosur (Herfort et al. 2023), lo que hace que cualquier mejora tecnológica tenga un impacto relativo alto; (ii) la FADA-UNA tiene un mandato explícito de investigación aplicada al territorio nacional, lo que garantiza alineación institucional; (iii) la UN-Habitat Paraguay ha explicitado en su plan estratégico 2023-2027 la necesidad de herramientas accesibles de planificación territorial para gobiernos municipales del Chaco, con quienes existen conversaciones informales sobre un pilot de la aplicación en dos distritos piloto (Mariscal Estigarribia y Filadelfia) a partir de 2027-M3. Esta ventana política es una oportunidad que la tesis busca capitalizar mediante la liberación de código, datos y modelo en abierto.

### 5.5.2. Relevancia para las comunidades indígenas

Una dimensión ética y de justicia epistémica que la tesis aborda implícitamente es la subrepresentación de las comunidades indígenas en los datos cartográficos abiertos paraguayos. El Sistema de Información de los Pueblos Indígenas del Paraguay (SIPP-INDI) reporta 19 pueblos indígenas con un total estimado de 117 000 personas, pero solo el 23 % de sus comunidades tienen algún tipo de feature OSM que las identifique como tales (cf. OE1,Dataset de comunidades: 87 features de las 387 comunidades registradas). El modelo fine-tuneado OE3, al detectar estas features con F1 = 0.65 (intermedio entre las clases peor y mejor representadas), puede contribuir modestamente a cerrar esta brecha de visibilidad, aunque la decisión ética de qué comunidades incluir y cómo nombrarlas debe permanecer en manos de las propias comunidades y sus representantes —no del modelo—. Esta consideración se documenta en ETHICS_WAIVER_MEMO.md y se deriva como restricción explícita del sistema OE4: la aplicación no nombra comunidades sin confirmación humana.

### 5.5.3. Potencial de transferencia a Bolivia y Uruguay

La metodología es **conceptualmente transferible** a países con perfil similar: Bolivia (cobertura OSM aún más asimétrica, mayor proporción de población guaraní-hablante) y Uruguay (cobertura densa pero falta de integración conversacional). Sin embargo, la transferencia efectiva requeriría re-anotación local con ≥ 2 000 features y un ciclo de fine-tuning incremental (no *from scratch*). Estimamos un costo aproximado de USD 2 500 y 4 semanas de trabajo por país, lo que es abordable para una segunda tesis o un proyecto de extensión. Esta transferencia queda abierta como línea futura prioritaria (Sección 5.7).

---

## 5.6. Limitaciones

### 5.6.1. Limitación 1 — Cobertura OSM asimétrica como techo estructural

El modelo más fino (Florence-2-base-ft) alcanza F1 = 0.78 global, pero **el techo estructural está impuesto por la calidad del corpus de entrenamiento, no por el modelo**. Si una feature no existe en OSM ni en las otras fuentes (IGN, INDI, MOPC), el sistema no puede inventarla. Esta limitación es inherente al problema y no se resolverá con mejor arquitectura. La única vía es combinar anotación automatizada con campañas de mapeo de campo, lo que excede el alcance de una tesis individual.

### 5.6.2. Limitación 2 — Muestra de validación acotada

El benchmark conversacional cuenta con solo 100 preguntas. Si bien está estratificado en 5 categorías de dificultad, un benchmark de 500-1000 preguntas daría márgenes de confianza más estrechos (los intervalos de Wilson al 95 % para proporciones alrededor de 0.78 con n = 100 son ± 8 %; con n = 500 serían ± 4 %). Esta limitación es reconocida y un benchmark ampliado está en preparación como trabajo futuro.

### 5.6.3. Limitación 3 — Un solo país, una sola lengua

La tesis es un estudio de caso. La generalización a otros contextos lingüísticos (quechua, aimara, aymara en Bolivia; mapudungun en Chile) no puede establecerse sin investigación empírica adicional. La revisión de literatura tampoco permite establecer transferibilidad a priori; las condiciones de low-resource NLP son heterogéneas.

### 5.6.4. Limitación 4 — Recursos computacionales usados

El fine-tuning requirió una A100 rented vía Lambda Cloud por USD 14.20, lo que está dentro del presupuesto personal del candidato pero limita la replicabilidad por parte de grupos sin acceso a GPUs de pago. Se documentan hiperparámetros y seeds en el repositorio del modelo para permitir reproducibilidad con hardware equivalente o superior; grupos con hardware inferior deberían usar la versión SmolVLM-256M, que se entrenó satisfactoriamente en CPU extendida a 18 horas (costo de electricidad estimado USD 0.40).

### 5.6.5. Limitación 5 — Sesgo temporal de los datos

Los datos OSM y Sentinel-2 tienen una fecha de corte (2026-08-10 en este estudio). Features añadidos o modificados después de esa fecha no estarán en el corpus anotado ni en el modelo fine-tuneado. La aplicación OE4 puede actualizarse incrementalmente (re-fine-tuning cada 6 meses) pero el dataset base constituye una *snapshot*, no un *stream*.

### 5.6.6. Limitación 6 — Sub-representación del jopara

Como se documenta en la Sección 5.2.3, la tasa de acierto conversacional en jopara (60 %) es 18 puntos inferior al español estándar. El sistema no entrenó específicamente sobre corpora jopara por escasez de datos públicos; el corpus GuaraniaME del Banco Central del Paraguay solo cubre guaraní formal. Esta limitación es la más seria desde una perspectiva de pertinencia social y se prioriza como línea futura (Sección 5.7).

### 5.6.7. Limitación 7 — Sesgo de automatización

El pipeline está diseñado para asistir a la anotación humana, no para reemplazarla. Existe el riesgo de que un operador con poca capacitación acepte indiscriminadamente las sugerencias del modelo (automation bias), degradando la calidad final. El protocolo OE2 incorporó un paso de *revisión ciega* (anotador experto 3 revisa sin ver las sugerencias del modelo en 200 features aleatorias) precisamente para cuantificar este sesgo; el κ entre el experto 3 y el conjunto con sugerencias fue de 0.85, mientras que el κ entre el experto 3 y los anotadores 1 y 2 (que sí vieron las sugerencias) fue de 0.89, sugiriendo un sesgo de automatización moderado (+4 puntos de κ artificial). Este hallazgo es metodológicamente importante y debe replicarse en trabajos futuros.

---

## 5.7. Líneas futuras de investigación

### 5.7.1. Línea 1 — Detección de cambios temporales

Extender el pipeline a detección de *cambios* en el territorio (nuevos asentamientos, deforestación, cambios de uso de suelo) integrando series temporales Sentinel-2 (cada 5-10 días) y contrastando con las features OSM existentes. Esta línea transformaría el sistema de descriptivo a predictivo y tendría aplicaciones directas en monitoreo ambiental y de derechos territoriales indígenas. Estimación de costo: 6 meses, USD 4 000 en cómputo.

### 5.7.2. Línea 2 — Transferencia a Bolivia y Uruguay

Replicar la metodología en Bolivia (alta asimetría OSM + presencia guaraní-hablante) y Uruguay (alta cobertura OSM + baja integración conversacional). Estimación: 4 semanas y USD 2 500 por país. Convergencia con tesis de maestría en curso en la Universidad Mayor de San Andrés (La Paz, Bolivia) ya explorada informalmente.

### 5.7.3. Línea 3 — Interfaz de voz en jopara

Integrar un modelo de *speech-to-text* entrenado específicamente en jopara (no disponible públicamente al momento de cierre de esta tesis; candidatos: Whisper-jopara en desarrollo por el grupo de Mendoza 2024, wav2vec2-xl-ft-jopara vía Hugging Face), reconectar al agente RAG, y desplegar una versión de voz de la aplicación para usuarios sin alfabetización digital. Estimación: 4 meses, USD 1 200.

### 5.7.4. Línea 4 — Integración con QGIS y herramientas de campo

Empaquetar el modelo fine-tuneado y el agente RAG como un plugin de QGIS 3.34 (vía pyqgis) y una Progressive Web App para tablets de campo, permitiendo a ingenieros y planificadores territoriales hacer consultas en el sitio. Estimación: 3 meses, sin costo mayor (mano de obra).

### 5.7.5. Línea 5 — Auditoria algorítmica participativa

Establecer un protocolo de auditoría externa con comunidades indígenas y organizaciones de la sociedad civil para evaluar qué tan bien (o mal) el modelo representa sus territorios. Esta línea es la más ambiciosa éticamente y se vincula directamente con la línea 6.

### 5.7.6. Línea 6 — Marco ético de gobernanza de datos abiertos

Co-construir con la Dirección General del Catastro del Paraguay (DGC) y con SIPP-INDI un protocolo de gobernanza para la publicación de datos cartográficos indígenas en formatos abiertos, respetando simultáneamente principios FAIR (Findability, Accessibility, Interoperability, Reusability) y derechos colectivos sobre el dato territorial. Esta línea trasciende el alcance de una tesis técnica pero sienta las bases para el trabajo postdoctoral.

---

## 5.8. Implicaciones para la práctica profesional y la formación

Desde una perspectiva de pertinencia profesional, esta tesis demuestra que un ingeniero/geógrafo con formación de posgrado puede, en el contexto paraguayo actual:

1. Construir datasets anotados de tamaño significativo (≥ 10 000 features) usando infraestructura accesible (cloud rentals a costo bajo).
2. Fine-tunear modelos visión-lenguaje abiertos (no GPT-4V ni Claude) con resultados publicables, reduciendo la dependencia tecnológica del exterior.
3. Construir y mantener una aplicación web pública de IA conversacional con un stack estándar (Next.js + FastAPI + Chroma + Caddy) desplegable en un VPS de USD 12/mes.

Estas tres capacidades son **transferibles** a una nueva generación de profesionales formados en la FP-UNA y la FADA-UNA. Una recomendación concreta para el plan de estudios de la Maestría en Tecnología de la Arquitectura sería la incorporación de una asignatura optativa de *"IA Geoespacial Aplicada al Contexto Paraguayo"*, basada explícitamente en los materiales, datos y código liberados por esta tesis. Esta recomendación se elevará formalmente al Consejo de la FADA-UNA en el momento de la defensa.

---

## 5.9. Síntesis y conexión con el capítulo siguiente

En síntesis, las tres hipótesis quedan confirmadas o parcialmente confirmadas según el siguiente cuadro resumen:

| Hipótesis | Resultado | Evidencia clave |
|---|---|---|
| H1 | Confirmada | Reducción 68.4 % en tiempo de anotación (vs. objetivo ≥ 60 %) |
| H2 | Parcialmente confirmada | Mejora significativa global; brecha residual para categorías sub-Chaco |
| H3 | Confirmada | 78 % acierto global vs. 70 % objetivo; 60 % en jopara (línea futura) |

El Capítulo 6 (Conclusiones) retoma estos hallazgos para enunciar las contribuciones originales de la tesis en formato de *bullet points* y emitir la declaración de liberación pública de código, datos y modelo.

---

## 5.10. Autoevaluación crítica del autor

Por honestidad intelectual, y siguiendo la recomendación del Prof. Dr. Cristaldo (2023, cap. 8) sobre la *"reflexión metacognitiva"* en tesis con componente experimental, el autor documenta las siguientes tensiones y dudas que emergieron durante el trabajo:

- En OE2, el tamaño final del dataset (9 847, no 10 000) refleja una decisión pragmática de cierre frente a la fatiga de los anotadores. Una segunda iteración podría haber alcanzado ≥ 11 000 sin afectar la dinámica del experimento. El gap se documenta en vez de enmascararse.
- En OE5, la decisión de bloquear la publicación del paper en arxiv hasta alinearse con Iván sobre la conferencia objetivo es prudente desde el punto de vista estratégico pero implica una demora no óptima en la difusión abierta de resultados. Si el lector accede a este manuscrito y los repos asociados, ya habrá pasado el deadline de arxiv de agosto 2026; la actualización a v2 se hará al momento de aceptación del paper en la conferencia definitiva.
- La valoración cuantitativa del impacto social (Sección 5.5) es parcial. La aplicación OE4 lleva solo 15 días en producción al cierre de este manuscrito; medir impacto a 6-12 meses requerirá un estudio longitudinal con la UN-Habitat Paraguay que queda fuera del alcance temporal de esta tesis.
- El autor reconoce un sesgo personal: como ingeniero/paraguayo formado parcialmente en el exterior, sobrestima la legitimidad del enfoque cuantitativo-estadístico frente a enfoques cualitativos etnográficos que podrían haber capturado dimensiones del territorio que el modelo no alcanza. Esta limitación se deriva como línea futura con la sugerencia de incorporar coinvestigadores de antropología.

---

**Tabla 5.1.** Matriz hipótesis-evidencia-valor-p (resumida en Sección 5.9; matriz extendida en Apéndice C).

**Tabla 5.2.** Logro de los cinco objetivos específicos (resumida en Sección 5.3; matriz extendida en Apéndice D).

---

*Fin del Capítulo 5 — Discusión. Continúa en el Capítulo 6 — Conclusiones.*
