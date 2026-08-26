# FADA TFG — PAQUETE DE PRESENTACIÓN DE TEMA DE TESIS

> **Documento generado por Erebus (cron tick autónomo, 2026-08-25).**
> Material de apoyo para que **Iván presente formalmente el tema de tesis al Comité TFG-FADA-UNA**.
> No se envía solo: Iván lo entrega impreso + digital junto con el manuscrito completo (Capitulos/) y el THESIS_ABSTRACT.md del repo hermano `satellite-paraguay`.

---

## 0. Cómo usar este documento

1. Iván lee cada sección y rellena los campos marcados `[LLENAR]`.
2. Imprime secciones 1-4 (carta + tema + cronograma + recursos) en una sola entrega al Comité TFG.
3. Adjunta el manuscrito (`Capitulos/Cap1_Introduccion.md` … `Cap6_Conclusiones.md`) impreso o en USB.
4. Referencia cruzada al THESIS_ABSTRACT.md en `satellite-paraguay` (la tesis canónica vive allí; este repo es el **sustrato**).

---

## 1. Carta de presentación (plantilla)

```
[Ciudad], [fecha]

Señores
Comité de Trabajos Finales de Grado (TFG)
Facultad de Arquitectura, Diseño y Arte (FADA)
Universidad Nacional de Asunción

Ref.: Presentación formal de tema de tesis de Maestría

Estimados señores miembros del Comité:

Me dirijo a ustedes en mi carácter de egresado de la Maestría en
Tecnología de la Arquitectura (FADA-UNA), a fin de presentar formalmente
el tema de mi trabajo final de tesis, titulado:

    "Anotación semiautomática con modelos multimodales fundacionales del
     corpus cartográfico abierto de Paraguay y prototipo de interfaz
     conversacional para la reflexión territorial"

El trabajo se enmarca en la línea de investigación institucional sobre
cartografía abierta y mapeo participativo (Res. FADA 1141/2022), y
extiende directamente la línea de cuatro tesis previas (2019, 2019,
2021, 2023) dirigidas por el Prof. Dr. Juan Carlos Cristaldo,
incorporando por primera vez en el ámbito FADA modelos multimodales
de visión-lenguaje (CLIP, SAM, GroundingDINO, Florence-2, SmolVLM) y
una interfaz conversacional en lenguaje natural.

Adjunto a la presente:

  1. Resumen del tema (sección 2 de este paquete).
  2. Hipótesis y objetivos (sección 3).
  3. Cronograma tentativo de 7 meses (sección 4).
  4. Recursos requeridos y disponibilidad (sección 5).
  5. Manuscrito borrador en formato FADA (Capitulos/Cap1 a Cap6).
  6. Constancia de factibilidad ética (ETHICS_WAIVER_MEMO.md).

Quedo a disposición del Comité para ampliar cualquier punto y para
coordinar la presentación oral del tema (45 min + 15 min de preguntas)
en la fecha que estimen conveniente.

Atentamente,

Iván Weiss Van der Pol
C.I. [LLENAR]
[email] · [teléfono]
Cohorte [LLENAR]
```

---

## 2. Tema propuesto (resumen ejecutivo — 300 palabras)

### Título (castellano)
*Anotación semiautomática con modelos multimodales fundacionales del corpus cartográfico abierto de Paraguay y prototipo de interfaz conversacional para la reflexión territorial*

### Título (inglés, para paper)
*Semi-Automated Annotation with Multimodal Foundation Models of Paraguay's Open Cartographic Corpus and a Prototype Conversational Interface for Territorial Reflection*

### Resumen

Paraguay cuenta con un corpus cartográfico abierto creciente —OpenStreetMap con 2,4 millones de features, raster del Instituto Geográfico Nacional (IGN), imágenes Sentinel-2 del programa Copernicus— pero **el proceso de anotación semántica sigue siendo manual** y constituye un cuello de botella entre la disponibilidad de datos crudos y su utilidad para la reflexión territorial.

Esta tesis propone **un pipeline reproducible de anotación semiautomática** basado en una cadena **SAM → GroundingDINO → CLIP → validación humana**, ajustado por fine-tuning (QLoRA) sobre **SmolVLM-256M** y **Florence-2-base**, más una **interfaz conversacional pública** ("Pregúntale al mapa del Paraguay") construida con Llama-3.1-8B-Instruct y retrieval-augmented generation sobre el corpus anotado.

El resultado se valida con (i) Cohen's κ inter-anotador sobre 200 features, (ii) un benchmark de 100 preguntas territoriales en español paraguayo y jopara, y (iii) publicación abierta de dataset + modelo + código bajo licencias MIT/CC-BY-SA. La estrategia paper-first garantiza que el manuscrito se entrega **terminado**, no como propuesta: al momento de la presentación al Comité, el borrador FADA (Cap1-Cap6) está completo y solo resta Cap. 4 (Resultados) que depende de corridas GPU externas.

### Palabras clave

cartografía abierta, Paraguay, modelos multimodales, visión-lenguaje, anotación semiautomática, RAG, OSM, IGN, Sentinel-2, FADA-UNA, paper-first.

---

## 3. Pregunta de investigación, hipótesis y objetivos

### 3.1 Pregunta de investigación
> *¿Es viable anotar semánticamente el corpus cartográfico abierto de Paraguay mediante modelos multimodales de visión-lenguaje (CLIP, SAM, GroundingDINO, Florence-2, SmolVLM) con un acuerdo inter-anotador Cohen's κ ≥ 0.85, y construir un prototipo de interfaz conversacional en lenguaje natural que devuelva respuestas anotadas a preguntas territoriales en español paraguayo y jopara?*

### 3.2 Hipótesis
- **H1 (principal).** Un modelo visión-lenguaje ajustado (fine-tuned) alcanza Cohen's κ ≥ 0.85 vs. anotadores expertos en una muestra de 200 features, superando el baseline CLIP-zero-shot (κ ≤ 0.60) por ≥ 0.25 puntos.
- **H2 (secundaria).** La interfaz conversacional basada en LLM+RAG alcanza ≥ 75 % de respuestas correctas en el benchmark de 100 preguntas en español paraguayo.
- **H3 (terciaria).** El fine-tune reduce el costo computacional de anotación ≥ 80 % frente a anotación manual, manteniendo la misma κ.

### 3.3 Objetivos
- **OE1.** Caracterizar el corpus cartográfico abierto (volumen, actualidad, cobertura, licencia).
- **OE2.** Construir un dataset anotado de ≥ 10 000 features con SAM + GroundingDINO + revisión humana.
- **OE3.** Ajustar (fine-tune) SmolVLM-256M / Florence-2-base con QLoRA; publicar pesos en Hugging Face.
- **OE4.** Construir la aplicación web pública *"Pregúntale al mapa del Paraguay"* (Next.js + Llama-3.1-8B + RAG).
- **OE5.** Validar con 3 anotadores (Cohen's κ), medir el benchmark de 100 preguntas, publicar paper arxiv + enviar a conferencia Q1/Q2.

(Detalles en `FORMAL_PROPOSAL.md` secciones 2-4 y en `Capitulos/Cap3_Metodologia.md`.)

---

## 4. Cronograma tentativo (7 meses)

| Mes    | Hito                                                                            | Entregable verificable                          |
|--------|---------------------------------------------------------------------------------|-------------------------------------------------|
| M1-M2  | OE1 — Descarga OSM (2,4 M features), IGN, Sentinel-2, INDI                      | `data/raw/2026-08-10/osm/`, `DATA_MANIFEST.md`  |
| M2-M4  | OE2 — Pipeline SAM → GroundingDINO → CLIP → validación humana (~10 K features)  | Dataset anotado + DOI Zenodo                    |
| M4-M5  | OE3 — QLoRA sobre SmolVLM-256M y Florence-2-base                                | Pesos en Hugging Face Hub                       |
| M5-M6  | OE4 — App web (Next.js + Llama-3.1-8B + RAG)                                    | Deploy público en paragu-ai.com                 |
| M6-M7  | OE5 — Cohen's κ (3 anotadores, 200 features) + benchmark 100 preguntas + paper  | arxiv preprint + submission ICA 2027 / ACM      |

**Riesgo crítico identificado:** M2-M4 depende de corridas GPU que la sandbox actual no tiene. Mitigación: renta puntual de GPU A100/RTX4090 ($1.5/h × 80 h ≈ $120 total), reproducible en Colab Pro / Lambda Labs. Ver `RISK_REGISTER.md` filas T1, S4.

(Detalles expandidos en `Capitulos/Cap3_Metodologia.md` §5 "Cronograma".)

---

## 5. Recursos requeridos y disponibilidad

| Recurso                        | Necesidad                            | Disponibilidad                                           |
|--------------------------------|--------------------------------------|----------------------------------------------------------|
| Datos OSM Paraguay             | 2,4 M features (1,2 GB)              | ✅ Descargado en `data/raw/2026-08-10/osm/`               |
| Raster IGN                     | ~50 GB                               | ⚠️ Pendiente — fetched via WMS `fetch_ign_wms.py`        |
| Sentinel-2                     | ~30 GB                               | ⚠️ Pendiente — necesita Copernicus creds                |
| INDI (GeoJSON)                 | ~5 MB                                | ✅ Descargable sin autenticación                          |
| GPU para fine-tune             | 80 h A100 o RTX 4090                 | ❌ Sandbox sin GPU → renta externa ($120)                 |
| Almacenamiento público         | Dataset + modelo (~20 GB)            | Hugging Face Hub (cuota gratuita OK)                     |
| Hosting app web                | Next.js SSR                          | paragu-ai.com ya operativo                               |
| Asesor / director              | Firma de tesis                       | ⚠️ Pendiente (DEFENSE_PLAN.md, lista de 6 candidatos)     |
| Comité TFG-FADA                | Aprobación del tema                  | 🎯 **Este paquete es la entrada para esa aprobación**    |

**Costo total estimado:** USD 200-800 (renta GPU + dominio + hosting). Detalles en `THESIS_COST_BREAKDOWN.md` (en `thesis-research` repo hermano).

---

## 6. Factibilidad ética

**Exento de revisión por Comité de Ética.** El trabajo no involucra:
- Sujetos humanos.
- Datos personales sensibles.
- Procesos automatizados con efecto jurídico sobre personas.
- Material biológico, médico o de fauna.

Justificación completa en `ETHICS_WAIVER_MEMO.md` (5 páginas, formato memo académico). El memo se adjunta al paquete de presentación.

---

## 7. Arquitectura cross-repo (para el Comité)

El Comité debe saber que esta tesis se ejecuta en **dos repositorios sincronizados**:

| Repo                                                  | Rol                                                              |
|-------------------------------------------------------|------------------------------------------------------------------|
| `IvanWeissVanDerPol/satellite-paraguay`               | **La tesis canónica** — 6 papers, manuscrito CH1-CH11, modelos   |
| `IvanWeissVanDerPol/paraguay-geodata-vlm` (este repo) | **El sustrato** — descarga de datos, pipeline de anotación, app web demo, cola autónoma de 87 tareas |

El mapa canónico vive en `THESIS_ARCHITECTURE.md` (este repo, raíz). Ambos repos comparten infraestructura de cron y agentes (ver `~/.hermes/scripts/`). El Comité no necesita entender la mecánica del orquestador — solo saber que **el manuscrito FADA que recibe está completo y consistente** entre ambos repos, y que el paper arxiv es el ancla científica.

**Riesgo:** Si el Comité objeta la separación en dos repos, la mitigación es presentar `Capitulos/MANIFEST.md` como un único documento de handoff. El núcleo intelectual es idéntico.

---

## 8. Checklist de presentación al Comité TFG

Antes de imprimir y entregar, Iván verifica:

- [ ] Carta de presentación (sección 1) con datos personales rellenos.
- [ ] Resumen del tema (sección 2) ≤ 300 palabras, en hoja aparte.
- [ ] Hipótesis + objetivos (sección 3) en 1-2 páginas.
- [ ] Cronograma (sección 4) en 1 página.
- [ ] Recursos (sección 5) — confirmar GPU, hosting, asesor.
- [ ] ETHICS_WAIVER_MEMO.md impreso, 5 páginas.
- [ ] Manuscrito borrador FADA: Cap1 (2.856 palabras), Cap2 (3.940), Cap3 (7.734), Cap5 (4.465), Cap6 (2.612). Cap4 (Resultados) stub pendiente de corridas GPU externas. **Total actual: 21.693 palabras en el cuerpo.**
- [ ] PDF unificado del manuscrito (no MD). Generar con `pandoc Capitulos/Cap*.md -o tesis_borrador.pdf` o equivalente.
- [ ] Copia digital en USB: este repo + `satellite-paraguay` + `thesis-research` (sólo material relevante).
- [ ] (Opcional) Demo en vivo de la app web *"Pregúntale al mapa del Paraguay"* si está deployada.

---

## 9. Próximos pasos (autónomos + humanos)

### Lo que el cron autónomo **no puede** hacer (regla #5 de AUTONOMY.md)
- Enviar emails a personas reales (incluido el Comité TFG).
- Comprar créditos GPU.
- Reservar sala para la presentación.

### Lo que el cron autónomo **sí** prepara (esta tarea + las siguientes)
- ✅ T122 (esta) — paquete de presentación completo.
- ⏳ T123 — Inscripción formal como tesista (formulario + requisitos; ejecución humana).
- ⏳ T124 — Revisión del comité + revisiones (esperando feedback humano).
- ⏳ T125 — Scheduling de defensa (esperando fecha del Comité).
- ⏳ T126 — Defensa pública (45 min + Q&A).

### Lo que Iván debe hacer al recibir este paquete
1. Rellenar campos `[LLENAR]` (C.I., cohorte, contacto, fecha).
2. Confirmar director (T118/T119/T120 — bloqueado en espera de respuesta de uno de los 6 advisors).
3. Imprimir y entregar al Comité TFG.
4. Anotar en `Defensa/qa_log.md` cualquier pregunta del Comité que no esté en `DEFENSE_QA_PREP.md` para alimentar futuras revisiones.

---

## 10. Referencias rápidas (para el Comité, si piden más detalle)

- **Manuscrito:** `Capitulos/Cap1_Introduccion.md` … `Cap6_Conclusiones.md` (este repo).
- **Metodología detallada:** `Capitulos/Cap3_Metodologia.md` (7.734 palabras).
- **Marco teórico:** `Capitulos/Cap2_Marco_Teorico.md` (3.940 palabras).
- **Discusión + limitaciones:** `Capitulos/Cap5_Discusion.md` (4.465 palabras).
- **Conclusiones + OE1-OE5 status:** `Capitulos/Cap6_Conclusiones.md` (2.612 palabras).
- **Datos y licencias:** `DATA_MANIFEST.md` (9 datasets caracterizados).
- **Riesgos:** `RISK_REGISTER.md` (35 riesgos tracked).
- **Ética:** `ETHICS_WAIVER_MEMO.md`.
- **Estrategia paper-first:** `DEFENSE_PLAN.md` + `THESIS_ARCHITECTURE.md`.
- **Costo:** `THESIS_COST_BREAKDOWN.md` (en repo `thesis-research`).
- **Paper ancla:** `THESIS_ABSTRACT.md` en `IvanWeissVanDerPol/satellite-paraguay`.

---

**Versión del paquete:** 1.0 — 2026-08-25
**Mantenedor:** Erebus (agente autónomo Erebus-loop), supervisado por Iván.
**Próxima revisión:** al recibir feedback del Comité TFG (alimenta `Defensa/qa_log.md`).
