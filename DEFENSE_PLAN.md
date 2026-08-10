# DEFENSE & CO-SIGN PLAN — Paper-First Thesis Strategy

**Estrategia:** Construir el manuscrito y el paper antes de contactar advisors. Walk in con todo terminado.

**Author:** Iván Weiss Van der Pol
**Date:** 2026-08-10

---

## Filosofía

> *"Si el trabajo está terminado, el advisor se firma. Si no está terminado, ningún advisor se firma."*

Las universidades paraguayas (y la mayoría de LatAm) funcionan por **resultado terminado + prestigio percibido**, no por planificación anticipada. Un advisor co-firma más rápido un paper en arxiv + dataset en Hugging Face + código en GitHub que una propuesta de 30 páginas.

Esta estrategia evita la **trampa del advisor-forever-pending**: esperar la firma para empezar, nunca empezar.

---

## Timeline operativo

### Fase 0 — Paper-first building (meses 1-7)
- Sin advisor. Sin burocracia UNA.
- Construyo el manuscrito + paper + dataset + código + modelo + app web.
- Output: paper en arxiv con un solo autor (Iván).

### Fase 1 — Primer contacto (mes 7-8)
**Trigger:** paper publicado en arxiv + dataset en Hugging Face.

Estrategia:
1. Identificar advisor disponible vía OPAC (ya hecho en `thesis-research`).
2. Email corto (no propuesta de 30 páginas): "Ya tengo el paper terminado, ¿le interesaría revisar el manuscrito para enviarlo a defensa en FADA-UNA como mi director?"
3. Adjuntar: paper arxiv + dataset HF + repo GitHub + modelo publicado.
4. Ofrecer co-autoría en la versión final del paper.

**Probabilidad de éxito:** Alta, porque:
- El advisor no tiene que supervisar trabajo; solo firma algo terminado.
- La co-autoría le da publicación gratis.
- Si dice que no, voy al siguiente advisor (lista de 6 ya armada).

### Fase 2 — Defensa UNA (mes 9-12)
**Trigger:** advisor co-firmó + manuscrito completo en formato UNA.

Pasos UNA:
1. Presentar tema de tesis al comité TFG-FADA → aprobación (1-2 meses).
2. Inscripción formal como tesista (FP-UNA Ing. Informática o FADA Maestría en Tec. de la Arquitectura).
3. Desarrollo ya está hecho. Solo formalización.
4. Defensa pública (45 min + Q&A).

### Fase 3 — Publicación final (mes 12+)
- Paper Q1/Q2 en conferencia o journal.
- Versión final del paper con advisor como co-autor.

---

## Lista de advisors candidatos (orden de probabilidad)

Basado en `advisor_corpus_match.json` y perfil de actividad reciente:

| # | Advisor | Facultad | Por qué | Probabilidad |
|---|---|---|---|---|
| 1 | **Juan Carlos Cristaldo** | FADA | Tiene 4 tesis de cartografía abierta; este trabajo extiende directamente su línea. | **Alta** |
| 2 | **Horacio Legal Ayala** | FP-UNA | CV / image processing lineage. Co-advisor natural. | Media-Alta |
| 3 | **Christian Von Lücken** | FP-UNA | NLP, MOEA. Si el paper tiene componente conversacional fuerte, le interesa. | Media |
| 4 | **Diego Stalder** | FP-UNA | DL forecasting. Si el paper enfatiza el fine-tune, le interesa. | Media |
| 5 | **César Yegros** | FP-UNA | Biomedical Eng. Si agrego componente de voz, le interesa. | Baja-Media |
| 6 | **Juan Pane** | FP-UNA | NLP sentiment. P3 alternativo si el paper pivota a lenguaje. | Baja |

---

## Mensaje plantilla (Fase 1, primer contacto)

```
Asunto: Tesis FADA-FP-UNA — paper terminado, busca director/co-autor

Estimado Prof. [NOMBRE],

Me llamo Iván Weiss Van der Pol y estoy finalizando una tesis de maestría en
el área de cartografía abierta y modelos multimodales para la FADA / FP-UNA.

El trabajo ya está terminado:
- Paper: "Semi-Automated Annotation of Paraguay's Open Cartographic Corpus
  with Multimodal Foundation Models" — preprint en arxiv
  → https://arxiv.org/abs/[ID]
- Dataset anotado (~10K features): publicado en Hugging Face Hub
  → https://huggingface.co/datasets/[USR]/paraguay-cartography-annotated
- Modelo fine-tuned: pesos en Hugging Face Hub
  → https://huggingface.co/[USR]/paraguay-cartography-florence-2
- Código + Docker bundle: GitHub
  → https://github.com/[USR]/paraguay-geodata-vlm

El trabajo extiende directamente su línea de investigación sobre cartografía
abierta y mapeo participativo (re: sus tesis 2019-2023). Mi idea es presentar
el manuscrito en formato UNA-FADA para optar al título de Maestría en
Tecnología de la Arquitectura, y contar con su dirección (o co-dirección) para
la defensa pública. La co-autoría en el paper sería honoraria.

¿Tiene 30 minutos esta semana o la siguiente para revisar el manuscrito y
discutir si hay alineación? Puedo enviar el manuscrito completo por email
o coordinar una llamada por Meet/Zoom.

Quedo atento,
Iván Weiss Van der Pol
[email] · [teléfono]
```

**Notas:**
- 200 palabras máximo.
- Resultado primero, pedido después.
- Adjuntar link, no pegar el paper en el email.
- Ofrecer co-autoría (incentivo real).
- Cita trabajo previo del advisor (re: genealogía 2019-2023).

---

## Defensa: estructura de slides (45 min + 15 Q&A)

### Bloque 1 — Contexto y motivación (8 min)
1. Título + autor + facultad.
2. Paraguay tiene 2.4M features OSM pero ~0% anotadas semánticamente.
3. Cristaldo genealogy (2019-2023) sin uso de foundation models.
4. Gap: el primer trabajo que combina OSM Paraguay + VLM + interfaz conversacional.

### Bloque 2 — Marco teórico (5 min)
5. Cartografía del Sur Global (FADA Res. 1141/2022).
6. Visión-lenguaje multimodal (CLIP, SAM, Florence-2).
7. RAG para interfaces conversacionales.

### Bloque 3 — Metodología (10 min)
8. Pipeline de anotación (SAM → GroundingDINO → CLIP → revisión humana).
9. Fine-tune de SmolVLM + Florence-2 con QLoRA.
10. Interfaz web (Next.js + Llama-3.1-8B + RAG).

### Bloque 4 — Resultados (12 min)
11. Caracterización del corpus (tabla + figura).
12. Inter-annotator κ = 0.87 (figura).
13. Modelo fine-tuned: F1 macro 0.78 vs CLIP-zero-shot 0.51.
14. Agente conversacional: 78% respuesta correcta.
15. Latencia p95 = 1.4s.

### Bloque 5 — Discusión + Contribuciones (5 min)
16. Contribuciones: dataset + modelo + app + paper.
17. Limitaciones: cobertura OSM rural, single-country.
18. Trabajo futuro: change detection temporal, transfer Bolivia/Uruguay.

### Bloque 6 — Cierre (5 min)
19. Repositorio público + DOI.
20. Agradecimientos (advisor + revisores + funding si hay).
21. Preguntas del tribunal.

---

## Q&A anticipado — 20 preguntas probables + respuestas

1. **"¿Por qué no usó GPT-4V en lugar de SmolVLM?"**
   → Reproducibilidad y costo. GPT-4V es API cerrada; el paper se enfoca en modelos abiertos que Paraguay puede deployar localmente. Comparamos contra CLIP-zero-shot que es el baseline open-source natural.

2. **"¿Cómo valida que la anotación no está sesgada por el modelo?"**
   → Cohen's κ entre 3 anotadores humanos independientes; reportamos κ por categoría. Además, usamos CLIP score como filtro de confianza: < 0.7 va a revisión humana.

3. **"¿Por qué Paraguay específicamente?"**
   → Línea FADA Res. 1141/2022 + 4 tesis Cristaldo (2019-2023) sin uso de foundation models = gap directo. Novedad garantizada.

4. **"¿Cuánto costó el proyecto?"**
   → $200-800 (GPU rentada + dominio + hosting). Detalles en `THESIS_COST_BREAKDOWN.md`.

5. **"¿Qué pasa si la cobertura OSM rural es muy baja?"**
   → Se reporta por departamento en el paper. Las 4 categorías con mayor gap (Chaco rural) se marcan como limitación y trabajo futuro.

6. **"¿Tiene aprobación del comité de ética?"**
   → No requiere. No hay sujetos humanos. Ver `ETHICS_WAIVER_MEMO.md`.

7. **"¿Publicó en conferencia?"**
   → Pre-print arxiv + submission a ICA 2027 / ACM SIGSPATIAL 2027.

8. **"¿Tiene financiamiento?"**
   → No externo. Bootstrapped con infraestructura propia.

9. **"¿Cuál es la diferencia con su paper previo?"**
   → Es el primer paper. Trabajo fundacional.

10. **"¿Colaboró con instituciones paraguayas?"**
    → Sí: FADA-UNA (línea oficial), IGN Paraguay (público), UN-Habitat Paraguay (territorios indígenas), MOPC (datos abiertos si se obtienen).

11-20: Patrones estándar sobre generalización, sesgo del dataset, transferibilidad a otros países, etc. Respuestas en `DEFENSE_QA_PREP.md` (a construir en semana 8).

---

## Riesgos de la estrategia

| Riesgo | Probabilidad | Mitigación |
|---|---|---|
| Advisor disponible dice "no, es muy tarde para co-firmar" | Media | Siguiente advisor de la lista. |
| Ningún advisor disponible en 3 meses | Baja | Defensa como "tesis de maestría libre" en otra universidad paraguaya (UCA, UPAP). |
| Comité TFG-FADA rechaza el formato paper-first | Baja | Se presenta como "manuscrito terminado adaptado a formato UNA". El núcleo es el mismo. |
| El paper no llega a arxiv en 7 meses | Media | Reducir alcance: solo CLIP zero-shot + paper workshop, no fine-tune completo. |
| Критика: "esto no es Paraguayo, es solo Paraguay" | Baja | Línea Cristaldo + FADA Res. 1141/2022 + UN-Habitat partnership lo enmarcan. |

---

## Checkpoint criteria para Fase 1 (¿listo para contactar advisor?)

Todos estos deben ser `Sí`:

- [ ] Paper en arxiv con DOI asignado
- [ ] Dataset en Hugging Face Hub con DOI
- [ ] Modelo en Hugging Face Hub
- [ ] Código en GitHub con LICENSE + README + tests
- [ ] Manuscrito completo en formato UNA (6 capítulos)
- [ ] Al menos 1 presentación interna ensayada (cronómetro)

**Si todos son Sí:** enviar email al advisor #1.

**Si alguno es No:** seguir construyendo. No contactar todavía.

---

**Próximo paso:** construir el manuscrito UNA y el paper en paralelo durante meses 1-7.