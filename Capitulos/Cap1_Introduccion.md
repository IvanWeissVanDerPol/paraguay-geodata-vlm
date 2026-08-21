# Capítulo 1 — Introducción

**Tesis:** *Anotación semiautomática con modelos multimodales del corpus cartográfico abierto de Paraguay y prototipo de interfaz conversacional para la reflexión territorial sudamericana*

**Autor:** Iván Weiss Van der Pol
**Tutora/or propuesta:** por definir (estrategia paper-first; ver Cap. 6 y `DEFENSE_PLAN.md`)
**Institución:** Facultad de Arquitectura, Diseño y Arte (FADA) — Universidad Nacional de Asunción (UNA), con co-afiliación a la Facultad Politécnica (FP-UNA), Ing. Informática
**Fecha de redacción inicial:** agosto de 2026
**Estado:** Borrador completo, listo para revisión interna y posterior co-firma del director

---

## 1.1. Presentación y motivación

Paraguay atraviesa, desde la promulgación de la Resolución 1141/2022 de la FADA-UNA, una etapa institucional en la que la reflexión territorial sudamericana se ha reconocido como un eje estratégico de investigación y formación. La resolución encarga a la facultad *«producir capacidades en cartografía con software libre que permitan producir no solo datos, sino capacidades locales para la reflexión y la gestión territorial»* (FADA-UNA, 2022). En consonancia con esa línea, el presente trabajo se inscribe en la intersección entre tres movimientos contemporáneos: la disponibilidad masiva de datos geoespaciales abiertos (OpenStreetMap, Copernicus Sentinel-2,Instituto Geográfico Nacional,Instituto Paraguayo del Indígena), la maduración de modelos multimodales visión-lenguaje (CLIP, SAM, GroundingDINO, Florence-2, SmolVLM) y la consolidación deinterfaces conversacionales sobre corpus estructurados mediante *Retrieval-Augmented Generation* (RAG).

La hipótesis central del trabajo es que existe un cuello de botella concreto entre la disponibilidad de datos crudos y su utilidad para la reflexión territorial. Paraguay dispone, según el extracto de Geofabrik de 2026, de 49.641 edificios y 14.835 carreteras catalogadas en OpenStreetMap, además de cobertura sistemática de Sentinel-2 desde 2015 y capas raster del Instituto Geográfico Nacional. Sin embargo, la anotación semántica de estos elementos —qué clase de carretera, qué material constructivo, qué uso de suelo, si la zona es indígena o periurbana— sigue siendo mayoritariamente manual, dispersa y no publicada de forma reproducible. Esta brecha semántica impide que los datos abiertos se conviertan, en la práctica, en insumos para la planificación urbana participativa, la investigación académica y la política pública basada en evidencia territorial.

El presente trabajo propone y evalúa un *pipeline* de anotación semiautomática, junto con un prototipo de interfaz conversacional en lengua natural (español paraguayo y jopara), que permitan cerrar esa brecha. La intención última es que la cartografía abierta paraguaya — y, por transferibilidad, la de otros países del Cono Sur con baja cobertura relativa — deje de ser un archivo de geometrías y se convierta en un recurso consultable en lenguaje natural por investigadoras, estudiantes,funcionarios y ciudadanas.

## 1.2. Planteamiento del problema

La cartografía abierta experimentó en las últimas dos décadas una democratización radical: lo que en los años noventa requería licencias comerciales caras hoy se descarga en formatos estándar desde repositorios públicos y gratuitos. Paraguay no fue la excepción. El extracto de OpenStreetMap para el país, distribuido por Geofabrik, creció de manera sostenida desde 2018, con picos de aporte comunitario tras cada convocatoria de *mapathon* organizada por la FADA y por la comunidad HOT (Humanitarian OpenStreetMap Team). Las imágenes Sentinel-2 del programa Copernicus, con resolución de 10 metros por píxel y revisita quincenal, cubren la totalidad del territorio nacional desde 2015 y se distribuyen sin costo. El Instituto Geográfico Nacional publica tiles raster y capas vectoriales en su geoportal. El Instituto Paraguayo del Indígena (INDI) y UN-Habitat Paraguay mantienen un *mirror* GeoJSON de los territorios indígenas reconocidos.

A pesar de esta abundancia, persisten tres limitaciones estructurales:

1. **Anotación manual y dispersa.** Los atributos semánticos de las *features* cartográficas (tipo de carretera según clasificación FADA, material constructivo predominante de una manzana, uso de suelo verificado en campo, pertenencia a territorio indígena reconocido) no se generan automáticamente a partir de las geometrías ni de las imágenes. Cada producto publicado requiere intervención humana, con la variabilidad inter-anotador que eso implica.

2. **Ausencia de modelos visión-lenguaje entrenados sobre corpus paraguayo.** Los modelos fundacionales multimodales publicados en 2021-2025 (CLIP, SAM, GroundingDINO, Florence-2, SmolVLM) fueron entrenados sobre corpus globales predominantemente norteamericanos, europeos y asiáticos. Su capacidad de *transfer learning* al contexto paraguayo — donde los patrones visuales de construcción vernacular, los tipos de caminos rurales y la cobertura vegetal chaqueña son sistemáticamente subrepresentados — no ha sido evaluada con rigor.

3. **Interfaz de consulta no natural.** Quien necesita hoy una respuesta territorial («¿qué proporción de este departamento tiene cobertura OSM de edificios?», «¿cuántos caminos rurales de tierra hay en el Chaco?», «¿qué comunidades indígenas están dentro de 50 km de esta ruta?») debe dominar software SIG (QGIS, ArcGIS), lenguajes de consulta espacial (PostGIS, GeoPandas) o ambos. Esta barrera técnica excluye a la mayoría de las potenciales personas usuarias del corpus abierto.

Estas tres limitaciones son la manifestación concreta, en el contexto paraguayo, de una brecha más general que la literatura reciente ha comenzado a denominar *semantic gap of volunteered geographic information* (See et al., 2023). Cerrarla requiere, simultáneamente, capacidad de anotación automática reproducible, modelos ajustados al contexto local y una interfaz que devuelva la consulta al lenguaje natural.

## 1.3. Pregunta de investigación

> *¿Es viable anotar semánticamente el corpus cartográfico abierto de Paraguay mediante modelos multimodales visión-lenguaje (CLIP, SAM, GroundingDINO, Florence-2, SmolVLM) con un acuerdo inter-anotador ≥ 0.85 (Cohen's κ), y construir un prototipo de interfaz conversacional en lenguaje natural que devuelva respuestas anotadas a preguntas territoriales en español paraguayo y jopara?*

La pregunta es doble y operativa: por un lado,interroga sobre la viabilidad técnica de la anotación semiautomática con modelos recientes; por otro,interroga sobre la viabilidad funcional de exponer esa anotación mediante una interfaz conversacional. La convergencia de ambas viabilidades constituye la condición necesaria para que el trabajo contribuya efectivamente a la línea institucional de la FADA.

## 1.4. Hipótesis de trabajo

### 1.4.1. Hipótesis principal (H1)

> Un modelo visión-lenguaje ajustado (*fine-tuned*) sobre el corpus cartográfico abierto paraguayo alcanza un acuerdo inter-anotador Cohen's κ ≥ 0.85 frente a anotadores expertos en una muestra de 200 *features*, superando al *baseline* CLIP *zero-shot* (κ esperado ≤ 0.60) por al menos 0.25 puntos.

La hipótesis principal establece el criterio de éxito cuantitativo del pipeline de anotación. El umbral de κ ≥ 0.85 corresponde, según la escala de Landis y Koch (1977), a una concordancia *casi perfecta*, y es consistente con los acuerdos reportados en anotación cartográfica de referencia (Mooney & Corcoran, 2012; See et al., 2023).

### 1.4.2. Hipótesis secundaria (H2)

> Una interfaz conversacional basada en un agente de modelo de lenguaje grande (LLM, por su sigla en inglés; específicamente Llama-3.1-8B-Instruct) con *retrieval-augmented generation* sobre el corpus anotado alcanza una tasa de respuesta correcta ≥ 75% en un *benchmark* de 100 preguntas territoriales en español paraguayo.

La hipótesis secundaria establece el criterio de éxito del prototipo conversacional, definidooperativamente sobre el *benchmark* documentado en `BENCHMARK_QUESTIONS.md`. La elección de Llama-3.1-8B-Instruct se justifica por su equilibrio entre capacidad multilingüe (incluido español rioplatense),requisitos computacionales accesibles y disponibilidad de pesos abiertos.

### 1.4.3. Hipótesis terciaria (H3)

> El *fine-tune* reduce el costo computacional de anotación ≥ 80% comparado con la anotación manual, manteniendo la calidad (mismo κ).

La hipótesis terciaria, de naturaleza económica,interroga sobre la sostenibilidad del enfoque. La reducción del 80% se evalúa comparando horas-persona de anotación manual contra horas-GPU de inferencia con modelo ajustado,normalizadas por *feature* anotada.

## 1.5. Objetivos

### 1.5.1. Objetivo general

Construir un *pipeline* reproducible de anotación semiautomática y un prototipo de interfaz conversacional para el corpus cartográfico abierto paraguayo,publicando el *dataset*, los pesos del modelo y la aplicación web como artefactos abiertos bajo licencias permisivas.

### 1.5.2. Objetivos específicos

1. **OE1 — Caracterización del corpus.** Caracterizar el corpus cartográfico abierto de Paraguay (OpenStreetMap + Instituto Geográfico Nacional + Sentinel-2 + Instituto Paraguayo del Indígena + datos del Ministerio de Obras Públicas y Comunicaciones) en volumen, actualidad, cobertura territorial y compatibilidad de licencias. *Cronograma: meses 1-2.*

2. **OE2 — *Dataset* anotado.** Construir un *dataset* anotado de ≥ 10.000 *features* cartográficas con etiquetas semánticas (tipo de carretera según clasificación FADA, material constructivo, clase de uso de suelo, pertenencia a territorio indígena) usando SAM, GroundingDINO y validación humana. *Cronograma: meses 2-4.*

3. **OE3 — Ajuste de modelo visión-lenguaje.** Ajustar (*fine-tune*) un modelo visión-lenguaje compacto (SmolVLM-256M o Florence-2-base) sobre el *dataset* del OE2 mediante técnicas de adaptación de bajo costo (QLoRA), y publicar los pesos en Hugging Face Hub. *Cronograma: meses 4-5.*

4. **OE4 — Aplicación web pública.** Construir una aplicación web pública titulada provisionalmente *«Pregúntale al mapa del Paraguay»* (Next.js 16 + Tailwind v4) que consuma el modelo del OE3 junto con un agente LLM con RAG, y que permita formular preguntas en lenguaje natural. *Cronograma: meses 5-6.*

5. **OE5 — Validación y publicación.** Validar el *pipeline* con tres anotadores expertos sobre una muestra de 200 *features* (Cohen's κ), medir el rendimiento en el *benchmark* de 100 preguntas y publicar un artículo en arXiv con envío posterior a una conferencia indexada en Q1 o Q2 (ICA 2027, ACM SIGSPATIAL 2027 o ISPRS 2027). *Cronograma: meses 6-7.*

## 1.6. Justificación e inserción institucional

La relevancia del trabajo se mide en tres dimensiones complementarias.

**Desde el punto de vista institucional**, el trabajo se alinea de manera directa con la Resolución 1141/2022 de la FADA-UNA y con la línea de cuatro tesis previas dirigidas por el Ing. Juan Carlos Cristaldo (2019, 2019, 2021, 2023) sobre cartografía abierta y mapeo participativo. Ninguna de esas tesis incorporó modelos multimodales visión-lenguaje, por lo que la presente propuesta extiende, sin duplicar, la genealogía institucional. La elección de FADA como facultad propuesta, con co-afiliación a FP-UNA, refleja la naturaleza interdisciplinaria del tema: cartografía crítica,visión por computadora y procesamiento de lenguaje natural convergen en el producto final.

**Desde el punto de vista académico y científico**, el trabajo contribuye a llenar un vacío identificado tanto en la literatura internacional (Yuan et al., 2021; Li et al., 2023; Kuckreja et al., 2024; Wang et al., 2024) como en la local: la evaluación rigurosa de modelos multimodales fundacionales sobre corpus geoespaciales de baja cobertura relativa del Sur Global. La elección de Paraguay como caso de estudio no es accidental: el país tiene simultáneamente cobertura cartográfica abierta suficiente para entrenar y validar, y brechas semánticas y de interfaz lo suficientemente pronunciadas como para que el trabajo tenga impacto demostrable.

**Desde el punto de vista social y de política pública**, el producto entregable (la aplicación web, el *dataset* abierto y el modelo abierto) habilita nuevos flujos de consulta parainvestigadoras,docentes,estudiantes de grado y posgrado,funcionarios municipales y departamentales, y ciudadanas interesadas en la reflexión territorial. La elección de español paraguayo y jopara como lenguas de consulta, en lugar de español neutro, refleja un compromiso explícito con la accesibilidad lingüística y con lavalorización de la variedad local.

## 1.7. Alcance y limitaciones

El alcance del trabajo está acotado por cinco decisiones explícitas.

**Alcance geográfico.** El estudio se circunscribe al territorio continental paraguayo (departamentos y distritos según división política vigente al 2025). La transferibilidad del enfoque a otros países del Cono Sur se discute como trabajo futuro en el Capítulo 5, pero no se ejecuta dentro del cronograma.

**Alcance temático.** Las clases semánticas anotadas son seis: carreteras (con subclasificación FADA), edificios (con material constructivo predominante), uso de suelo (con subclases urbano, periurbano, rural, chaqueño, indígena), cuerpos de agua,vegetación dominante y territorios indígenas reconocidos. La elección refleja la demanda concreta observada en la línea de tesis FADA y se documenta con mayor detalle en `DATA_MANIFEST.md` y en `METHODOLOGY.md`.

**Alcance temporal.** El *pipeline* de anotación y el modelo ajustado se entrenan sobre la versión del corpus disponible a junio de 2026. La aplicación web no incluye, en esta versión, detección de cambios temporales (change detection entre versiones); esa capacidad se trata como trabajo futuro.

**Alcance computacional.** Los experimentos se realizan sobre una GPU única (RTX 4090 o A100, en régimen de alquiler por horas), con un presupuesto total estimado en USD 200-800. La reproducibilidad se garantiza mediante un *bundle* Docker con semillas,versiones pinadas y *scripts* documentados, de modo que cualquier grupo con acceso a una GPU equivalente pueda replicar los resultados.

**Alcance ético.** El trabajo no involucra sujetos humanos, datos personales sensibles ni procesos de toma de decisiones automatizados con efecto jurídico. Elmemo `ETHICS_WAIVER_MEMO.md` documenta formalmente la exención de revisión por comité de ética.

Las limitaciones reconocidas —asimetría de cobertura OSM entre zonas urbanas y rurales, tamaño muestral del *benchmark* de 100 preguntas,transferibilidad internacional no evaluada— se reportan con transparencia en el Capítulo 5 y no se ocultan para sostener las hipótesis.

## 1.8. Metodología sintética

El trabajo se inscribe en una tradición deinvestigación descriptiva-aplicada con componente experimental y componente de desarrollo de software. El diseño combina tresvalidaciones independientes:

1. **Validación cuantitativa** del *pipeline* de anotación mediante Cohen's κ con intervalo de confianza al 95% calculado por *bootstrap* (1.000 iteraciones), comparando tres condiciones: CLIP *zero-shot*, SmolVLM ajustado y Florence-2 ajustado. Se aplica ANOVA de una vía con post-hoc de Tukey para identificar la condición significativamente superior.

2. **Validación cuantitativa** del agente conversacional mediante tasa de respuestas correctas sobre el *benchmark* de 100 preguntas,desglosada por categoría (carreteras, edificios, uso de suelo, agua,vegetación, territorios indígenas) y por tipo de pregunta (conteo,ubicación, comparación,superposición espacial).

3. **Validación cualitativa** mediante análisis temático de las preguntas del *benchmark* y de las respuestas del agente, con dos revisores independientes. Se reportan cinco casos de falla representativos con su explicación.

El detalle metodológico,incluyendo la arquitectura exacta del *pipeline* SAM → GroundingDINO → CLIP → revisión humana → *fine-tune* QLoRA, se desarrolla en el Capítulo 3 (Marco Metodológico) y se documenta operativamente en `METHODOLOGY.md`.

## 1.9. Estructura del trabajo

El manuscrito se organiza en seis capítulos, además de bibliografía y apéndices, conforme a la plantilla institucional de la FADA-UNA para tesis de Maestría.

- **Capítulo 1 — Introducción** (este capítulo). Presenta la motivación, el problema, la pregunta, las hipótesis, los objetivos, la justificación, el alcance, las limitaciones, la metodología sintética y la estructura general.
- **Capítulo 2 — Marco Teórico.** Expande la Sección 2 del artículo publicado y revisa la literatura sobre cartografía abierta, modelos visión-lenguaje, *retrieval-augmented generation*, y la línea de investigación FADA.
- **Capítulo 3 — Marco Metodológico.** Detalla el *pipeline* de anotación, el esquema de *fine-tune*, la arquitectura del agente conversacional, las métricas de evaluación y los criterios de reproducibilidad.
- **Capítulo 4 — Resultados.** Presenta el acuerdo inter-anotador, las tablas comparativas de modelos, los resultados del *benchmark* conversacional, los gráficos de latencia y el análisis de casos de falla.
- **Capítulo 5 — Discusión.** Interpreta los hallazgos a la luz del marco teórico,discute las limitaciones reconocidas y propone líneas de trabajo futuro.
- **Capítulo 6 — Conclusiones.** Sintetiza las contribuciones, formula las recomendaciones para la línea institucional FADA y deja planteada la inserción del trabajo en un programa más amplio de cartografía crítica del Sur Global.

Complementan el manuscrito la bibliografía unificada, los apéndices con los *scripts* de preprocesamiento, las tarjetas de modelo (*model cards*) y los enlaces permanentes a los artefactos digitales (*dataset*, pesos, aplicación web).

## 1.10. Estrategia de redacción y de defensa

La estrategia adoptada es de tipo *paper-first* (sin director durante los meses 1 a 7), conforme se documenta en `DEFENSE_PLAN.md`. La idea directriz es construir de manera simultánea el manuscrito de tesis, el artículo publicable, el *dataset* anotado, los pesos del modelo y la aplicación web, sin esperar a una firma previa de director. Cuando el trabajo se aproxima a su versión definitiva, se contacta a posibles directores con el producto terminado; las cuatro tesis previas de la línea FADA sugieren que esta estrategia minimiza la burocracia y maximiza la probabilidad de co-firma.

Esta estrategia difiere del patrón clásico de tesis de posgrado paraguayo, donde se busca un director antes de comenzar a investigar. La diferencia se justifica por la naturaleza reproducible y de código abierto del trabajo: el manuscrito y los artefactos están disponibles para evaluación independiente del director que finalmente se incorpore. La sección `DEFENSE_PLAN.md` amplía la estrategia de redacción, cronograma de contacto con posibles directores,plan de defensa y respuestas anticipadas a las preguntas más probables del tribunal.

## 1.11. Síntesis del capítulo

El presente capítulo introdujo el problema de la brecha semántica entre los datos cartográficos abiertos de Paraguay y su utilidad para la reflexión territorial; formuló la pregunta de investigación sobre la viabilidad de anotar ese corpus con modelos multimodales y exponerlo mediante una interfaz conversacional; propuso tres hipótesisoperativas con umbrales cuantitativos;desglosó un objetivo general y cinco objetivos específicos con cronograma;justificó la relevancia institucional,académica y social del trabajo;explicitó el alcance y las limitaciones;resumió la metodología;presentó la estructura del manuscrito; ydocumentó la estrategia *paper-first*.

El Capítulo 2 (Marco Teórico) sitúa estas contribuciones dentro de la literatura existente y de la línea institucional FADA, mientras que el Capítulo 3 (Marco Metodológico) detalla el *pipeline* reproducible que las hace posibles.

---

## Notas de redacción

- Las referencias bibliográficas completas se consolidan en el archivo unificado `REFERENCES.bib` y se expanden en el Capítulo 2.
- Las cifras de cobertura OSM (49.641 edificios, 14.835 carreteras) corresponden al extracto Geofabrik del primer trimestre de 2026 y se verifican operativamente en `DATA_MANIFEST.md`.
- Los nombres de modelos y arquitecturas (CLIP, SAM, GroundingDINO, Florence-2, SmolVLM, Llama-3.1-8B-Instruct) se utilizan en su forma originalinglesa por consistencia con la literatura internacional y con los repositorios públicos de pesos.
- La mención de «jopara» sigue la caracterización de Díaz (2025) como variedad de contacto estable entre español y guaraní, predominante en la conversación cotidiana paraguaya.
- El título de la aplicación web, *«Pregúntale al mapa del Paraguay»*, es provisional y queda sujeto a revisión durante la defensa y la publicación.