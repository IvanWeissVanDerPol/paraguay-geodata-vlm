# Anexo Técnico — Solicitud de Acceso a Datos Aéreos del MOPC

> **Adjunto a:** SFP-020 Formulario y Carta de Salida del solicitante Iván Weiss Van der Pol
> **Maestría:** Maestría en Tecnología de la Arquitectura — FADA-UNA
> **Director de tesis:** Ing. Juan Carlos Cristaldo
> **Fecha:** [LUGAR_FECHA]

---

## 1. Contexto del proyecto de tesis

La tesis de maestría *"Anotación semiautomática con modelos multimodales del corpus cartográfico abierto de Paraguay y prototipo de interfaz conversacional para la reflexión territorial sudamericana"* se desarrolla en el marco de la línea de investigación FADA-UNA de **cartografía abierta y mapeo participativo** (4 tesis previas: 2019, 2019, 2021, 2023 — director Ing. Juan Carlos Cristaldo). Es la primera tesis de esta línea que incorpora **inteligencia artificial multimodal** (modelos visión-lenguaje) al flujo de anotación cartográfica.

### 1.1 Problema identificado

Paraguay cuenta con un corpus cartográfico abierto creciente:
- **OpenStreetMap Paraguay:** ~49.641 edificios, ~14.835 carreteras, ~2 millones de features totales (extracto Geofabrik 2026).
- **Instituto Geográfico Nacional (IGN):** tiles raster de los 17 departamentos + Asunción Capital (~2 GB).
- **Copernicus Sentinel-2:** mosaicos L2A libres de nubes (~20 GB para Paraguay completo).

Sin embargo, **el proceso de anotación semántica sigue siendo mayoritariamente manual**, lo que genera un cuello de botella entre la disponibilidad de datos crudos y su utilidad para:
- planificación urbana municipal,
- investigación académica en reflexión territorial sudamericana,
- catastros digitales abiertos.

### 1.2 Pregunta de investigación

> *¿Es viable anotar semánticamente el corpus cartográfico abierto de Paraguay mediante modelos multimodales de visión-lenguaje (CLIP, SAM, GroundingDINO, Florence-2, SmolVLM) con un acuerdo inter-anotador ≥ 0.85 (Cohen's κ), y construir un prototipo de interfaz conversacional en lenguaje natural que devuelva respuestas anotadas a preguntas territoriales en español paraguayo y jopara?*

### 1.3 Hipótesis

- **H1:** un modelo visión-lenguaje ajustado sobre el corpus cartográfico abierto paraguayo alcanza un Cohen's κ ≥ 0.85 frente a anotadores expertos.
- **H2:** una interfaz conversacional basada en LLM + RAG alcanza una tasa de respuesta correcta ≥ 75% sobre un benchmark de 100 preguntas territoriales en español paraguayo.
- **H3:** el fine-tune reduce el costo computacional de anotación ≥ 80% comparado con anotación manual, manteniendo la calidad.

---

## 2. Datos solicitados — especificación técnica detallada

### 2.1 Mosaicado aéreo institucional

| Parámetro | Especificación |
|-----------|----------------|
| **Producto** | Mosaico de ortofotos institucionales del MOPC |
| **Cobertura** | Asunción Capital + Departamento Central + municipios del Gran Asunción (San Lorenzo, Fernando de la Mora, Lambaré, Luque, Mariano Roque Alonso, Limpio, Capiatá, Ñemby, San Antonio, Itauguá, Villa Elisa) |
| **Periodo** | Campañas 2018-2025 (preferentemente 2023-2025) |
| **Resolución espacial** | ≥ 30 cm/píxel (preferentemente 15-20 cm/píxel si disponible) |
| **Sistema de referencia** | WGS84 / UTM zona 21S (EPSG:32721). Aceptable WGS84 geográfico (EPSG:4326). |
| **Resolución radiométrica** | 8 bits por canal (RGB) o 16 bits (RGB+NIR) si disponible |
| **Bandas** | RGB (mínimo) / RGB+NIR (preferente) |
| **Formato** | GeoTIFF (.tif) con metadatos embebidos + archivo .tfw + archivo .prj |
| **Compresión** | LZW o DEFLATE (sin pérdida); aceptable ECW/MrSID si con metadatos |
| **Volumen estimado** | ~50 GB (cobertura ~2.500 km² × 4 bytes/píxel × 3 bandas) |
| **Tiles** | Preferentemente en hojas 1:5.000 (formato cartográfico estándar MOPC) |

### 2.2 Modelo Digital de Elevación (MDE / DEM)

| Parámetro | Especificación |
|-----------|----------------|
| **Producto** | MDE derivado del levantamiento aerofotogramétrico |
| **Cobertura** | Misma cobertura que el mosaicado aéreo (Sección 2.1) |
| **Resolución espacial** | ≥ 1 m/píxel (preferentemente 50 cm/píxel si disponible) |
| **Sistema de referencia** | WGS84 / UTM zona 21S (EPSG:32721) |
| **Tipo** | DSM (Digital Surface Model, incluye edificaciones) o DTM (Digital Terrain Model, solo terreno). Aceptable cualquiera; preferir DTM para análisis de cuencas |
| **Formato** | GeoTIFF 32-bit float + metadatos |
| **Volumen estimado** | ~5 GB |

### 2.3 Ortofotos del Gran Asunción

| Parámetro | Especificación |
|-----------|----------------|
| **Producto** | Ortofotos del Gran Asunción |
| **Cobertura** | Misma cobertura que el mosaicado aéreo (Sección 2.1) |
| **Periodo** | Última campaña disponible (preferentemente 2023-2025) |
| **Resolución espacial** | ≥ 30 cm/píxel |
| **Formato** | GeoTIFF + .tfw + .prj |
| **Volumen estimado** | ~20 GB |

---

## 3. Para qué se utilizarán los datos

### 3.1 Pipeline de anotación semiautomática (OE2-OE3)

El mosaicado aéreo institucional provee el **contexto geoespacial de referencia** sobre el cual se proyectan los features de OpenStreetMap Paraguay. El flujo de uso es:

1. **Adquisición y descarga** del mosaicado aéreo del MOPC y tiles raster del IGN.
2. **Proyección de features OSM** sobre el mosaicado aéreo (mediante geopandas + rasterio).
3. **Cropping automático** de parches de 256×256 píxeles centrados en cada feature OSM.
4. **Auto-anotación** mediante SAM (Segment Anything Model) + GroundingDINO (detector con prompts de texto).
5. **Validación humana** en Label Studio sobre muestra de 10.000 features.
6. **Fine-tune** de SmolVLM-256M o Florence-2 base con QLoRA sobre el dataset anotado.
7. **Evaluación** con Cohen's κ vs. anotadores expertos.

### 3.2 Validación cruzada con OSM (OE1)

El mosaicado aéreo sirve para **validar la exactitud posicional** de los features OSM proyectados:
- Calcular distancia euclidiana entre centroide OSM y centroide del edificio detectado por SAM sobre el mosaicado aéreo.
- Detectar **features OSM desactualizados** (edificios demolidos, carreteras nuevas no catalogadas, cambios de uso de suelo).
- Generar un **mapa de cambios** entre la versión OSM actual y el estado real del territorio según el mosaicado aéreo.

### 3.3 Prototipo de interfaz conversacional (OE4)

El mosaicado aéreo y el DEM se indexan como capas raster en un backend PostGIS + pgSTAC. La interfaz conversacional *"Pregúntale al mapa del Paraguay"* (Next.js 16 + Llama-3.1-8B-Instruct con RAG) devuelve a las consultas ciudadanas:
- recortes del mosaicado aéreo institucional como evidencia visual,
- coordenadas exactas de los features consultados,
- metadatos del MOPC cuando estén disponibles.

### 3.4 Línea base territorial para la defensa pública (OE5)

El mosaicado aéreo provee la **línea base territorial** sobre la cual se comparan los resultados cuantitativos del modelo ajustado (Cohen's κ, F1 macro por clase, latencia p95).

---

## 4. Cómo se procesarán los datos

### 4.1 Pipeline reproducible (escrito en Python)

Todos los scripts son **software libre** y se publican bajo licencia MIT en el repositorio de la tesis. Stack tecnológico:

- **Python 3.13** (lenguaje principal)
- **geopandas 1.1+** (manipulación de features vectoriales)
- **rasterio 1.5+** (I/O de raster)
- **shapely 2.1+** (geometría)
- **transformers 5.14+** (HuggingFace, modelos visión-lenguaje)
- **ultralytics 8.4+** (YOLO, opcional para detección adicional)
- **Label Studio** (validación humana, Docker)
- **QLoRA + PEFT** (fine-tune eficiente en GPU modesta)
- **LangChain + ChromaDB** (RAG para la interfaz conversacional)

### 4.2 Infraestructura disponible

| Recurso | Detalle |
|---------|---------|
| **GPU** | 1× A100 rented ($1.5/h × ~80h = $120 total one-time). Alternativa reproducible: Google Colab Pro / Lambda Labs. |
| **Almacenamiento local** | 500 GB SSD en equipo del maestrando |
| **Almacenamiento institucional** | Repositorio GitHub + Hugging Face Hub (gratuito, código + dataset) |
| **Red** | Conexión a internet para descarga del mosaicado (estimado 75 GB total) |
| **Backup** | Réplica en disco externo + Hugging Face Hub (cifrado en tránsito) |

### 4.3 Trazabilidad computacional

Cada script registra en `data/progress.jsonl`:
- SHA256 de cada archivo del mosaicado aéreo descargado,
- timestamp UTC de cada operación,
- parámetros de cada modelo ajustado (semilla aleatoria, hiperparámetros, versión de librería),
- métricas intermedias (F1 macro, Cohen's κ).

---

## 5. Licencia de publicación y distribución

### 5.1 Datos crudos del MOPC

Los datos crudos del mosaicado aéreo institucional **NO se redistribuirán**. Se utilizarán exclusivamente para la investigación declarada y se almacenarán en infraestructura local. Si en el futuro la UNA-FADA quisiera publicar una versión derivada (por ejemplo, etiquetas de features proyectadas sobre el mosaicado), se solicitará autorización previa al MOPC.

### 5.2 Productos derivados de la tesis

- **Código de software:** Licencia MIT — disponible en GitHub desde el inicio del proyecto.
- **Dataset anotado:** Licencia CC-BY-SA 4.0 — disponible en Hugging Face Hub desde la defensa de tesis.
- **Manuscrito de tesis:** Licencia CC-BY-NC-SA 4.0 — disponible en repositorio institucional UNA desde la defensa.
- **Paper académico:** Licencia estándar de la conferencia objetivo (probable arXiv + proceedings ICA/SIGSPATIAL/ISPRS).

### 5.3 Citación obligatoria de la fuente

Toda publicación derivada citará al MOPC con la fórmula:

> *"Fuente: Ministerio de Obras Públicas y Comunicaciones — Servicio Geográfico Militar (campaña [AÑO]). Datos obtenidos mediante solicitud formal SFP-020 [N° EXPEDIENTE] en el marco de la tesis de maestría UNA-FADA (director: Ing. Juan Carlos Cristaldo)."*

---

## 6. Cronograma de uso (M1-M7)

| Mes | Actividad | Uso del mosaicado aéreo |
|-----|-----------|--------------------------|
| M1 (Ago 2026) | Setup + descarga | Descarga del mosaicado y verificación de integridad |
| M2 (Sep 2026) | Pipeline SAM + GroundingDINO | Proyección de features OSM sobre mosaicado |
| M3 (Oct 2026) | Validación humana (Label Studio) | Anotación visual sobre recortes del mosaicado |
| M4 (Nov 2026) | Dataset anotado | Detección de cambios OSM vs mosaicado (validación cruzada) |
| M5 (Dic 2026) | Fine-tune SmolVLM | Entrenamiento sobre recortes (sin incluir mosaicado crudo en dataset publicado) |
| M6 (Ene 2027) | Interfaz conversacional | Indexación del mosaicado como capa de evidencia visual en el RAG |
| M7 (Feb 2027) | Validación + defensa | Generación de figuras comparativas para el manuscrito y la defensa pública |

**Plazo de retención local:** 24 meses posteriores a la defensa de tesis (M7 + 24 meses = M31 ≈ Feb 2029). Pasado ese plazo, los archivos del mosaicado aéreo se eliminan del equipo local y del respaldo en disco externo. Se conserva únicamente el dataset anotado (etiquetas sin mosaicado subyacente).

---

## 7. Cumplimiento normativo

### 7.1 Ley 5282/2014 de Libre Acceso a la Información Pública

La presente solicitud cumple con todos los requisitos del Art. 6:
- Identificación clara del solicitante (Sección 1 del SFP-020).
- Identificación clara de la información solicitada (Sección 3 del SFP-020 + Sección 2 de este Anexo).
- Finalidad específica declarada (Sección 4 del SFP-020 + Sección 3 de este Anexo).
- Modalidad de entrega preferida (Sección 5 del SFP-020).

### 7.2 Decreto 1134/2014

Solicita exención de tasa administrativa conforme al Art. 14 (fines de investigación académica de posgrado en universidad pública paraguaya).

### 7.3 Ley 6538/2020 de Datos Abiertos

Los datos solicitados son **datos abiertos gubernamentales** según la definición del Art. 3 (datos producidos o custodiados por organismos del Estado en formato digital, con licencia de reutilización). El solicitante se compromete a cumplir las restricciones del Art. 11 sobre no aplicar técnicas de identificación de personas y respetar los términos de uso que el MOPC especifique.

### 7.4 Protección de datos personales

El mosaicado aéreo tiene resolución ≥ 30 cm/píxel, suficiente para que **rostros individuales no sean identificables** (umbral de identificación de personas ≈ 15 cm/píxel según recomendaciones del Consejo de Europa). El solicitante se compromete explícitamente a:
- No aplicar técnicas de reconocimiento facial ni de identificación de personas.
- No publicar recortes del mosaicado aéreo en redes sociales ni en medios de comunicación.
- Eliminar el mosaicado aéreo del equipo local en el plazo declarado (Sección 6).

### 7.5 Soberanía de datos

Todos los datos descargados se almacenan en infraestructura **local** (equipo del maestrando + disco externo). No se suben a servicios cloud extranjeros durante el procesamiento. Únicamente el **dataset anotado derivado** se publica en Hugging Face Hub (alojado en Estados Unidos pero con datos derivados, no crudos).

---

## 8. Presupuesto y financiamiento

La tesis se ejecuta con **presupuesto cero de infraestructura cloud** (ver `THESIS_COST_BREAKDOWN.md`):

| Ítem | Costo |
|------|-------|
| GPU rented (A100, ~80h) | $120 USD one-time |
| Hosting (Vercel hobby tier) | $0 USD |
| Dominio (.com.ar opcional) | $15 USD/year |
| Disco externo (1 TB backup) | $50 USD one-time |
| **Total estimado M1-M7** | **~$200 USD** |

No se solicita financiamiento al MOPC ni se requiere desembolso institucional. La tasa administrativa del SFP-020 se solicita exenta conforme al Decreto 1134/2014 Art. 14.

---

## 9. Contacto para coordinación técnica

Si el MOPC requiere aclaraciones técnicas adicionales sobre el procesamiento de los datos solicitados, puede contactar a:

- **Director de tesis:** Ing. Juan Carlos Cristaldo — FADA-UNA — [EMAIL DIRECTOR — completar]
- **Maestrando:** Iván Weiss Van der Pol — [EMAIL_CONTACTO] — [TELEFONO_CONTACTO]
- **Secretaría Académica FADA:** secretaria.fada@una.py — (+595 21) 422-553

---

## 10. Avales institucionales

### 10.1 Aval del director de tesis

> *Certifico que la presente solicitud se enmarca en el plan de trabajo aprobado por la línea de investigación de cartografía abierta de la FADA-UNA, y que los datos solicitados son necesarios para la ejecución de la tesis de maestría del maestrando Iván Weiss Van der Pol.*
>
> **Ing. Juan Carlos Cristaldo**
> Director de Tesis
> FADA — Universidad Nacional de Asunción
> Fecha: [LUGAR_FECHA]
> Firma: [FIRMA Y SELLO]

### 10.2 Aval de Secretaría Académica FADA

> *Certifico que el maestrando Iván Weiss Van der Pol se encuentra inscripto y activo en la Maestría en Tecnología de la Arquitectura de la FADA-UNA, período lectivo 2026.*
>
> **Secretaría Académica**
> FADA — Universidad Nacional de Asunción
> Fecha: [LUGAR_FECHA]
> Firma: [FIRMA Y SELLO]

---

*Documento generado por Erebus (agente autónomo de Iván) bajo licencia MIT. Los placeholders `[CORCHETES]` deben ser completados por Iván antes de imprimir. Ver `INSTRUCCIONES_DE_APRESENTACION.md` para el paso a paso completo.*