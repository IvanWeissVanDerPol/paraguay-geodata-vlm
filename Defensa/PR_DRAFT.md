# Press Release — Borrador (T101a)

> **Status:** Borrador listo para revisión de Iván. **NO publicado.**
> **Origen:** Sub-tarea de T101 (Write blog post / press release for Paraguayan tech press) — T101 revertida a `[!]` por ser `[EXT]`; este draft es el artefacto autónomo que Iván copia y pega.
> **Autor del borrador:** Erebus (agente autónomo de Iván)
> **Fecha:** 2026-08-28
> **Idioma principal:** Español (con traducción al inglés abajo)
> **Destinatarios:** paraguaytech.com.py, MITIC (gabinete de prensa), CISO Paraguay group, ABC Color (suplemento tecnología), 5Días, Última Hora (cultura digital), Politécnica (boletín institucional)

---

## 🇵🇾 ESPAÑOL — Versión principal

### Titular

**Tesista de la UNA-FADA aplica modelos multimodales de visión-lenguaje para anotar el mapa abierto del Paraguay y publica su pipeline en código abierto**

### Subtítulo / Entradilla

*Iván Weiss Van der Pol, maestrando de la Facultad de Arquitectura, Diseño y Arte de la Universidad Nacional de Asunción, presenta la primera tesis paraguaya que integra CLIP, SAM, Florence-2 y agentes conversacionales para reducir el trabajo manual de etiquetado cartográfico del OpenStreetMap Paraguay.*

### Dateline

ASUNCIÓN, PARAGUAY — [FECHA DE EMBARGO]

### Lead (primer párrafo — invertido, 5W)

Iván Weiss Van der Pol, maestrando de la Facultad de Arquitectura, Diseño y Arte (FADA) de la Universidad Nacional de Asunción (UNA), finalizó el manuscrito de su tesis de maestría titulada *"Anotación semiautomática con modelos multimodales del corpus cartográfico abierto de Paraguay y prototipo de interfaz conversacional para la reflexión territorial sudamericana"*, primera investigación paraguaya que aplica modelos fundacionales de visión-lenguaje (CLIP, SAM, GroundingDINO, Florence-2, SmolVLM) para automatizar el etiquetado semántico del OpenStreetMap nacional y construir un agente conversacional en español paraguayo y jopara. El trabajo —desarrollado íntegramente con software libre y presupuesto cero de infraestructura cloud— se publicará bajo licencia MIT (código) y CC-BY-SA 4.0 (dataset) en Hugging Face Hub y GitHub.

### Cuerpo — 3 párrafos

La investigación ataca un cuello de botella conocido por la comunidad cartográfica paraguaya: el desfase entre la disponibilidad creciente de datos abiertos (OSM Paraguay cuenta con 49.641 edificios, 14.835 carreteras y más de 2 millones de features en total) y la lentitud del proceso manual de anotación semántica que da sentido a esos datos para la reflexión territorial, la planificación urbana y la investigación académica. El pipeline desarrollado combina modelos de visión pre-entrenados con ajuste fino (QLoRA) sobre una muestra estratificada de features paraguayas, alcanzando un acuerdo inter-anotador Cohen's κ de **0,87** frente a anotadores expertos, frente a un baseline de 0,51 con CLIP zero-shot.

Como producto derivado, la tesis incluye un agente conversacional accesible vía web que responde preguntas territoriales en lenguaje natural —"¿cuántos hospitales públicos hay en el Departamento Central?", "¿dónde están los asentamientos del Bajo Chaco?"— recuperando evidencia geoespacial del corpus anotado y devolviendo respuestas bilingües con citas a los IDs de OSM y a las capas raster del Instituto Geográfico Nacional. El sistema se diseñó pensando en la soberanía de datos: corre on-prem en un equipo con GPU modesta, no envía imágenes a APIs comerciales extranjeras y soporta consultas en jopara (mezcla de español y guaraní), rasgo distintivo frente a chatbots globales que asumen monolingüismo castellano.

El proyecto se inscribe en una línea de investigación FADA-UNA de cuatro tesis previas sobre cartografía abierta y mapeo participativo (directorio: Ing. Juan Carlos Cristaldo), y es la primera de esa línea que incorpora inteligencia artificial multimodal. La defensa pública está prevista para el primer semestre de 2027 ante tribunal de la Maestría en Tecnología de la Arquitectura. Todo el material —paper, código, dataset anotado, slides de defensa, bitácora de preguntas— se libera bajo licencias abiertas siguiendo las recomendaciones de la UNESCO sobre ciencia abierta y los Principios de FPIC (Free, Prior and Informed Consent) de la ONU para la protección de los territorios indígenas representados en el corpus.

### Cierre — Cita textual

> *"Esta tesis demuestra que Paraguay puede producir investigación de frontera en inteligencia artificial geoespacial sin depender de infraestructura propietaria ni de capital externo. El modelo se entrena en un equipo accesible, el código se audita en GitHub, y el dataset queda a disposición de los tesistas que sigan esta línea —y de cualquier municipalidad que quiera actualizar su catastro digital usando lo que ya tenemos abierto."*
> — Iván Weiss Van der Pol, autor

### Nota de embargo

EMBARGO HASTA: [FECHA Y HORA — coordinar con arxiv si se sube en paralelo,，建议 24-48 h de margen]
Contacto de prensa: [EMAIL DE IVÁN — llenar]
Teléfono: [TELÉFONO — llenar]
Repositorio de prensa (imágenes, screenshots, figuras): [URL cuando esté disponible]

### Sobre el autor

**Iván Weiss Van der Pol** es maestrando en Tecnología de la Arquitectura (FADA-UNA) e ingeniero en Informática por la Facultad Politécnica de la misma universidad. Trabaja en la intersección de inteligencia artificial aplicada, cartografía abierta y reflexión territorial sudamericana. Ha publicado previamente notas técnicas sobre el pipeline de anotación en el repositorio público del proyecto. Esta es su tesis de maestría; su trabajo de grado anterior en FP-UNA se centró en clasificación de imágenes satelitales multi-temporales para Paraguay. Contacto: [EMAIL].

### Sobre la UNA-FADA

La **Facultad de Arquitectura, Diseño y Arte (FADA)** de la **Universidad Nacional de Asunción (UNA)** es la unidad académica más antigua del Paraguay dedicada a la formación en arquitectura, diseño y urbanismo. Su Maestría en Tecnología de la Arquitectura, radicada en San Lorenzo, ofrece líneas de investigación en tecnologías constructivas, gestión urbana y herramientas digitales aplicadas al proyecto arquitectónico y al territorio. La línea de cartografía abierta y mapeo participativo dirigida por el Ing. Juan Carlos Cristaldo acumula cuatro tesis previas (2019, 2019, 2021, 2023) y es un referente nacional en la materia.

### Sobre el proyecto

**Título:** *Anotación semiautomática con modelos multimodales del corpus cartográfico abierto de Paraguay y prototipo de interfaz conversacional para la reflexión territorial sudamericana*
**Tipo:** Tesis de maestría (FADA-UNA, Maestría en Tecnología de la Arquitectura)
**Defensa prevista:** Primer semestre 2027
**Licencias:** MIT (código) · CC-BY-SA 4.0 (dataset anotado) · CC-BY 4.0 (manuscrito)
**Repositorios:** [URL arxiv cuando se suba] · [URL GitHub cuando se publique] · [URL Hugging Face cuando se suba]
**Contacto técnico:** Iván Weiss Van der Pol — [EMAIL]
**Costo declarado del proyecto:** USD 0 en infraestructura cloud (modelos abiertos, ajuste fino en hardware modesto, sin APIs de pago)

---

## 🇬🇧 ENGLISH — Translation (for international outlets)

### Headline

**UNA-FADA master's student applies multimodal vision-language models to annotate Paraguay's open map and releases the pipeline as open source**

### Subhead

*Iván Weiss Van der Pol, a master's candidate at Paraguay's National University's Faculty of Architecture, Design and Art, presents the first Paraguayan thesis to integrate CLIP, SAM, Florence-2 and conversational agents to reduce manual cartographic labelling of OpenStreetMap Paraguay.*

### Dateline

ASUNCIÓN, PARAGUAY — [EMBARGO DATE]

### Lead

Iván Weiss Van der Pol, a master's candidate at the Faculty of Architecture, Design and Art (FADA) of the National University of Asunción (UNA), has finalized the manuscript of his thesis titled *"Semi-automated annotation with multimodal models of Paraguay's open cartographic corpus and a prototype conversational interface for South American territorial reflection"* — the first Paraguayan research to apply foundation vision-language models (CLIP, SAM, GroundingDINO, Florence-2, SmolVLM) to automate semantic labelling of the national OpenStreetMap and to build a conversational agent in Paraguayan Spanish and Jopara. The work — developed entirely with free software and zero cloud-infrastructure budget — will be released under MIT (code) and CC-BY-SA 4.0 (dataset) licenses on Hugging Face Hub and GitHub.

### Body — 3 paragraphs

The research addresses a bottleneck familiar to the Paraguayan cartographic community: the gap between growing availability of open data (OSM Paraguay holds 49,641 buildings, 14,835 roads and over 2 million total features) and the slowness of the manual semantic-annotation process that makes those data useful for territorial reflection, urban planning and academic research. The developed pipeline combines pre-trained vision models with QLoRA fine-tuning on a stratified sample of Paraguayan features, reaching an inter-annotator Cohen's κ of **0.87** against expert annotators, against a 0.51 CLIP zero-shot baseline.

As a derivative product, the thesis includes a web-accessible conversational agent that answers territorial questions in natural language —"how many public hospitals are there in Central Department?", "where are the settlements of Bajo Chaco?"— retrieving geospatial evidence from the annotated corpus and returning bilingual answers with citations to OSM IDs and to raster layers from the Instituto Geográfico Nacional (IGN). The system was designed with data sovereignty in mind: it runs on-prem on modest GPU hardware, sends no images to foreign commercial APIs, and supports queries in Jopara (a Spanish-Guaraní mix), a distinctive feature compared to global chatbots that assume monolingual Castilian.

The project is part of a FADA-UNA research line comprising four previous theses on open cartography and participatory mapping (under the direction of Eng. Juan Carlos Cristaldo), and is the first in that line to incorporate multimodal artificial intelligence. The public defense is scheduled for the first half of 2027 before a panel of the Master's in Architectural Technology. All material — paper, code, annotated dataset, defense slides, Q&A logbook — is released under open licenses following UNESCO recommendations on open science and the United Nations' FPIC (Free, Prior and Informed Consent) Principles for the protection of indigenous territories represented in the corpus.

### Closing quote

> *"This thesis demonstrates that Paraguay can produce frontier research in geospatial AI without depending on proprietary infrastructure or external capital. The model trains on accessible hardware, the code is audited on GitHub, and the dataset is available to the thesis students who continue this line — and to any municipality that wants to update its digital cadastre using what we already have open."*
> — Iván Weiss Van der Pol, author

### Embargo note

EMBARGO UNTIL: [DATE AND TIME — coordinate with arxiv if uploading in parallel; suggest 24-48 h lead]
Press contact: [IVÁN'S EMAIL — fill in]
Phone: [PHONE — fill in]
Press kit repository (images, screenshots, figures): [URL when available]

### About the author

**Iván Weiss Van der Pol** is a master's candidate in Architectural Technology (FADA-UNA) and a computer engineer from the Polytechnic Faculty of the same university. He works at the intersection of applied artificial intelligence, open cartography and South American territorial reflection. He has previously published technical notes on the annotation pipeline in the project's public repository. This is his master's thesis; his prior undergraduate work at FP-UNA focused on multi-temporal satellite image classification for Paraguay. Contact: [EMAIL].

### About UNA-FADA

The **Faculty of Architecture, Design and Art (FADA)** of the **National University of Asunción (UNA)** is Paraguay's oldest academic unit dedicated to architecture, design and urbanism education. Its Master's in Architectural Technology, based in San Lorenzo, offers research lines in constructive technologies, urban management and digital tools applied to architectural project and territory. The open-cartography and participatory-mapping research line directed by Eng. Juan Carlos Cristaldo has produced four previous theses (2019, 2019, 2021, 2023) and is a national reference in the field.

### About the project

**Title:** *Semi-automated annotation with multimodal models of Paraguay's open cartographic corpus and a prototype conversational interface for South American territorial reflection*
**Type:** Master's thesis (FADA-UNA, Master's in Architectural Technology)
**Defense scheduled:** First half of 2027
**Licenses:** MIT (code) · CC-BY-SA 4.0 (annotated dataset) · CC-BY 4.0 (manuscript)
**Repositories:** [arxiv URL when uploaded] · [GitHub URL when published] · [Hugging Face URL when uploaded]
**Technical contact:** Iván Weiss Van der Pol — [EMAIL]
**Declared project cost:** USD 0 in cloud infrastructure (open models, fine-tuning on modest hardware, no paid APIs)

---

## 📋 Instrucciones de uso para Iván

1. **Llenar campos placeholder** entre corchetes `[...]` antes de enviar: fechas, emails, teléfonos, URLs.
2. **Coordinar embargo** con la subida a arxiv (si va en paralelo,建议 24-48 h de margen).
3. **Adaptar tono** según el medio destinatario:
   - **Paraguayan tech press** (paraguaytech.com.py, MITIC, CISO Paraguay): versión ES, enfoque técnico.
   - **Prensa general** (ABC, 5Días, Última Hora): versión ES, énfasis en "primera tesis paraguaya" + soberanía de datos.
   - **Internacional** (Latam Science, Arxiv Blog, Hugging Face Newsletter): versión EN, énfasis en "paper-first methodology" + open-science compliance.
4. **Verificar cifras** (49.641 edificios, 14.835 carreteras, Cohen's κ 0,87) con la versión final del paper antes de mandar — son placeholders basados en Cap.1+Cap.4, pero el manuscrito puede haber cambiado.
5. **NO firmar como Erebus.** El crédito de la nota es de Iván, no del agente. Si el medio pregunta por la herramienta, se puede mencionar transparentemente que el borrador fue asistido por un agente autónomo (Erebus) bajo la dirección del autor — eso refuerza el ángulo de "research tooling" sin apropiación indebida.