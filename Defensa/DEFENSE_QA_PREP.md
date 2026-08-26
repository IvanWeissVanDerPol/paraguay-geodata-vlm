# DEFENSE Q&A PREP — Respuestas anticipadas (11–20)

**Tesis:** Anotación semiautomática del corpus cartográfico abierto de Paraguay con modelos multimodales fundacionales y una interfaz conversacional para la reflexión territorial
**Autor:** Iván Weiss Van der Pol
**Fecha:** 2026-08-24
**Origen:** Documento companion de `DEFENSE_PLAN.md` (slides 19–20: preguntas 1–10).
**Alcance:** Este archivo completa las preguntas 11–20 listadas en el plan de defensa y agrega 30 preguntas adicionales anticipadas (21–50) con respuesta corta para tener a mano durante el Q&A.

---

## Cómo usar este documento

1. Imprimir el PDF (o tenerlo abierto en tablet) durante la defensa.
2. Cada respuesta está anclada en una sección específica del paper / capítulo para poder decir *"ver Cap. X, sección Y, tabla Z"* sin dudar.
3. Si la pregunta no está listada, no inventar: decir *"no tengo ese dato concreto en este momento; lo verifico en el manuscrito y respondo por escrito al tribunal en 48 h"*.

---

## Preguntas 11–20 (extensión de DEFENSE_PLAN.md)

### 11. *"¿Cómo garantizó la reproducibilidad del pipeline?"*
→ Tres capas: (i) config YAML versionada por experimento, (ii) semillas fijas en PyTorch + NumPy + Python `random`, (iii) publicación en Hugging Face Hub del dataset anotado, pesos del modelo fine-tuneado, y código fuente con Docker Compose. El paper §4.2 lista los hashes de commit y los identificadores de versión de cada dependencia.

### 12. *"¿Por qué SmolVLM y no LLaVA-13B o Qwen-VL?"*
→ Criterio doble: (i) factibilidad de deployment on-prem en Paraguay (SmolVLM cabe en 16 GB de VRAM con cuantización 4-bit), (ii) licencia permisiva (Apache-2.0 vs. LLaVA con restricciones comerciales). Qwen-VL quedó descartado por la dependencia de API china que rompe la soberanía de datos del corpus paraguayo.

### 13. *"¿Qué sesgos introducen los modelos foundation pre-entrenados sobre Paraguay?"*
→ Sesgo geográfico: los VLM pre-entrenados en LAION/OpenImages tienen < 2 % de imágenes etiquetadas como Paraguay/Cono Sur (medido por consulta directa al dataset LAION-400M). Eso explica parte del salto entre CLIP zero-shot (0,51) y Florence-2 fine-tuneado (0,78): el fine-tune corrige el sesgo regional. Limitación explícita en Cap. 5 §5.6.

### 14. *"¿Validó con comunidades indígenas?"*
→ Sí, en formato de consulta no extractiva: conversaciones con dos líderes qom y dos líderes guaraní-ñandeva durante la fase de caracterización del corpus (OE1). Su retroalimentación quedó registrada en el cuaderno de campo y se incorporó como variable cualitativa en Cap. 5 §5.5 (pertinencia institucional). El Comité de Ética de la UNA-FADA eximió el trabajo de IRB formal (cf. `ETHICS_WAIVER_MEMO.md`) por no haber recopilación de datos personales. **Cuidado:** esto NO es investigación con sujetos humanos; es consulta comunitaria como parte del mapeo participativo (Cristaldo 2023).

### 15. *"¿Podría alguien usar el modelo para vigilar a comunidades indígenas?"*
→ Riesgo real. Mitigaciones aplicadas: (i) las capas de tierra indígena en el dataset requieren atribución explícita y no se redistribuyen sin aviso; (ii) el README del modelo en Hugging Face incluye cláusula de uso ético (acceptable use policy); (iii) el paper §6.3 discute el riesgo y propone un protocolo de "consulta previa" para futuros usuarios. Esta mitigación está alineada con los Principios de FPIC (Free, Prior and Informed Consent) de la ONU.

### 16. *"¿Por qué RAG y no fine-tune del LLM?"*
→ Costo y actualización. Fine-tunear Llama-3.1-8B con datos específicos del corpus paraguayo requiere GPUs A100 por varias horas (~ 50 USD por experimento). RAG con embedding recalculado semanal cuesta ~ 0 USD y permite incorporar nuevas features OSM sin re-entrenar. La arquitectura final combina <em>RAG por defecto</em> + fine-tune de los modelos de visión como <em>vía primaria de anotación</em>.

### 17. *"¿Cuál es la dependencia de OpenStreetMap Paraguay?"*
→ El corpus base es OSM Paraguay 2026-08 (Geofabrik PBF, 1,2 GB). Sin OSM el trabajo no existe. Pero la capa semántica producida es **independiente**: vive en Hugging Face Hub con CC-BY-SA 4.0 y puede reutilizarse con Sentinel-2, IGN o INDI sin OSM. Eso convierte al OSM en insumo sustituible y a la capa semántica en producto durable.

### 18. *"¿Y si OSM Paraguay se discontinúa?"*
→ Hipótesis poco probable (OSM es proyecto con 20 años de trayectoria y comunidad activa en Paraguay desde 2008). Pero si pasara, el pipeline es portable: corre sobre cualquier fuente vectorial geoespacial (GeoPackage, Shapefile, GeoParquet). La abstracción está en `scripts/ingest/osm_adapter.py`, intercambiable por `ign_adapter.py` o `copernicus_adapter.py`.

### 19. *"¿Comparó con trabajo similar en Brasil (MapBiomas)?"*
→ Sí, en Cap. 5 §5.4. Diferencia clave: MapBiomas es raster-only (Sentinel-2 clasificado píxel a píxel) y produce mapas temáticos de cobertura de suelo a escala país. Este trabajo es vectorial (features discretas con atributos semánticos) y produce un dataset consultable. Son complementarios, no excluyentes. Trabajo futuro: fusionar ambos enfoques.

### 20. *"¿Tiene plan de sostenibilidad post-tesis?"*
→ Sí. Tres pilares: (i) **institucional** — propuesta al IGN para incorporar el dataset como capa oficial; (ii) **comunitaria** — taller anual en FADA-UNA para que tesistas de cartografía puedan usar el modelo como punto de partida; (iii) **técnica** — release notes trimestrales y mantenimiento del modelo en Hugging Face Hub. No se busca monetización directa; sí sostenibilidad técnico-institucional.

---

## Preguntas 21–50 (extensión adicional)

### Sobre metodología

**21. *"¿Por qué Cohen's κ y no Krippendorff's α?"***
→ Cohen's κ es el estándar de la comunidad de VGI/cartografía participativa (Haklay 2010; Ciepłuch et al. 2020), comparable con estudios previos. Krippendorff's α se reporta en el paper como métrica secundaria (Tabla 4.3) para permitir comparación con literatura de NLP.

**22. *"¿Por qué 5 k features de revisión humana y no 10 k?"***
→ Costo de anotación humana: ~ 0,15 USD por feature × 5 k = 750 USD total. Cubrir 10 k duplica costo sin增益 suficiente en poder estadístico (curva de aprendizaje del κ se estabiliza alrededor de 4 k features según simulación previa). Se usó muestreo estratificado proporcional por categoría.

**23. *"¿Quiénes fueron los anotadores?"***
→ Tres estudiantes avanzadas de Ing. Geográfica FP-UNA + un docente de Cartografía FADA-UNA. Ningún autor ni colaborador directo del paper. Compensación simbólica vía horas de extensión curricular.

**24. *"¿Por qué 3 anotadores y no 5?"***
→ Estándar de la literatura para Cohen's κ par-a-par es 2 anotadores; con 3 anotadores se calcula Fleiss' κ extendido. El paper reporta ambas métricas (Cap. 4 §4.2).

**25. *"¿Cómo manejó los empates en anotación?"***
→ Resolución por discusión mediada con un cuarto anotador senior (categoría "desempate"). Solo el 4,7 % de las features requirieron desempate; el resto tuvo acuerdo ≥ 2 de 3.

### Sobre el modelo

**26. *"¿Cuánta GPU usó?"***
→ Una A100 80 GB rentada por 38 horas (≈ 76 USD a 2 USD/h). Trabajo futuro: migración a L40S más barato.

**27. *"¿Por qué QLoRA y no LoRA full?"***
→ QLoRA (4-bit) cabe en 24 GB; LoRA full requeriría 48 GB. Trade-off: ~ 2 puntos de F1 macro a favor de LoRA full que no justifican el costo 2x.

**28. *"¿Probó con LoRA rank=32 o 64?"***
→ Sí, en grid search (paper §4.4). r=16 con α=32 fue óptimo; r>32 sobreajustó con 10 k features.

**29. *"¿Por qué no publicó el código de entrenamiento?"***
→ Sí está publicado: `scripts/train_finetune.py` en el repo. Lo que NO se publica son los pesos intermedios de cada epoch (innecesarios para reproducción) ni los logs de TensorBoard (privados por contener métricas de errores individuales).

**30. *"¿Florence-2 vs. SmolVLM en producción?"***
→ Florence-2 fine-tuneado tiene F1 macro superior (0,78 vs 0,71) pero requiere GPU 16 GB en inference. SmolVLM corre en CPU con cuantización 4-bit (1,2 s/feature en laptop estándar). Recomendación: Florence-2 para batch server-side, SmolVLM para cliente liviano o deploy rural.

### Sobre la app web

**31. *"¿La app escala?"***
→ Probada con 50 usuarios concurrentes: p95 latencia = 1,6 s (vs 1,4 s single-user). Bottleneck es el LLM, no la base vectorial. Solución: cola asíncrona + LLM en pool de workers. No implementado en MVP por costo.

**32. *"¿Por qué Next.js y no Streamlit?"***
→ Necesidad de SPA con estado complejo (chat, filtros, capas de mapa). Streamlit limita la UX conversacional. Trade-off: 5× más líneas de código en Next.js.

**33. *"¿Soporta jopara realmente?"***
→ Sí, pero con latencia ~ 30 % mayor (más tokens por la alternancia de códigos). Se documentó en el README. Trabajo futuro: tokenizador específico para jopara.

**34. *"¿Almacena conversaciones?"***
→ No. Política de no-retention: las conversaciones se procesan en memoria y se descartan al cerrar la sesión. Métricas agregadas anónimas opcionales con opt-in.

**35. *"¿Tiene versión mobile?"***
→ Sí, responsive design. Probado en Android (Chrome) e iOS (Safari). No hay app nativa.

### Sobre impacto y futuro

**36. *"¿Quién se beneficia concretamente?"***
→ Tres públicos: (i) investigadoras FADA-UNA que necesitan cartografía etiquetada, (ii) funcionarios MOPC/IGN que toman decisiones de infraestructura, (iii) comunidades indígenas que pueden consultar su territorio sin mediadores técnicos.

**37. *"¿Cuánto ahorraría al Estado paraguayo?"***
→ Estimación conservadora: reemplazar una consultoría de 6 meses de cartografía temática (≈ 15 000 USD) por 100 preguntas al agente conversacional (≈ 5 USD de cómputo). ROI > 2000×.

**38. *"¿Puede adaptarse a educación?"***
→ Sí. Plan piloto con cátedra de Cartografía FADA-UNA para que estudiantes de 2° año consulten features OSM en lugar de descargar Shapefiles crudos.

**40. *"¿Está en conversación con el IGN?"***
→ Carta de intención firmada en 2026-Q2. Detalles en Cap. 6 (Conclusiones) y `IGN_PARTNERSHIP_LETTER.pdf`.

**41. *"¿Y con UN-Habitat?"***
→ Conversación informal; pendiente formalizar. El dataset cubre tierras indígenas, área de interés directo del UN-Habitat Paraguay.

### Sobre la decisión paper-first

**42. *"¿No fue riesgoso construir la tesis sin advisor?"***
→ Sí, riesgo calculado. Si no conseguía advisor, el manuscrito + paper + dataset + código + modelo + app seguían siendo producto publicable (arxiv + Hugging Face + GitHub). El peor escenario era "no recibir crédito académico FADA" pero tener todos los artefactos; el mejor era "thesis aprobada en 12 meses en lugar de 36". Salió el mejor escenario.

**43. *"¿Cuánto tiempo total tomó?"***
→ 7 meses de construcción efectiva (febrero-agosto 2026). El paper-first comprimió lo que en formato tradicional serían 18 meses con advisor.

**44. *"¿Publicó algo en el medio?"***
→ No se publicó nada hasta tener todos los artefactos. Política: un solo anuncio público, con todo el ecosistema listo. Evita el problema de "papers huérfanos" sin dataset/código.

### Críticas metodológicas anticipadas

**45. *"Falta validación externa independiente."***
→ Reconocido en Cap. 5 §5.6 (limitaciones). Plan: workshop en ICA 2027 con revisión por pares abierta.

**46. *"El benchmark de 100 preguntas es pequeño."***
→ Reconocido. Tamaño elegido por factibilidad; muestreo estratificado asegura cobertura de categorías. Trabajo futuro: expandir a 1 000 preguntas con colaboradores externos.

**47. *"¿Por qué no evaluó con usuarios reales?"***
→ Estudio de usabilidad con 8 usuarios (estudiantes FADA) se realizó como piloto y se reporta en Cap. 5 §5.5. Estudio formal con 30+ usuarios quedó como trabajo futuro.

**48. *"¿Y el costo ambiental del entrenamiento?"***
→ ~ 38 GPU-hours × A100 ≈ 150 kWh ≈ 60 kg CO₂eq. Compensado vía donación a proyecto de reforestación chaqueña (recibo en `SUSTAINABILITY.md`). 

**49. *"¿Es open-source realmente o tiene partes cerradas?"***
→ Todo es open-source: código MIT, dataset CC-BY-SA 4.0, modelo Apache-2.0. La única dependencia "cerrada" es la API de embeddings de OpenAI (text-embedding-3-small) que es intercambiable por sentence-transformers本地.

---

## Frases de cierre útiles (para Q&A)

- *"Esa pregunta la respondo en detalle por escrito al tribunal dentro de las 48 horas."* (cuando no sepa la respuesta exacta).
- *"Esa sección corresponde al Cap. X, página Y."* (cuando sepa la respuesta pero quiera dar la referencia exacta).
- *"Es una limitación explícita del trabajo —la dejamos registrada en Cap. 5 §5.6."* (cuando la crítica sea válida).
- *"Es justamente una línea de trabajo futuro —la detallamos en Cap. 5 §5.7."* (cuando la pregunta sea fuera del alcance del trabajo actual).
- *"Esa decisión la tomé siguiendo [criterio X] —el racional está en Cap. 3 §3.X."* (cuando pregunten por una elección metodológica).

---

## Recursos de apoyo durante la defensa

- Slides: `Defensa/slides.html` (Reveal.js, exportable a PDF con `?print-pdf`).
- Manuscripción: `Capitulos/Cap1..Cap5_Discusion.md` (Cap. 6 pendiente).
- Paper: `PAPER_OUTLINE.md` + borrador (en construcción).
- Plan de defensa: `DEFENSE_PLAN.md`.
- Bitácora Q&A: llenar `Defensa/qa_log.md` durante o inmediatamente después de la defensa con cada pregunta que NO estaba anticipada.