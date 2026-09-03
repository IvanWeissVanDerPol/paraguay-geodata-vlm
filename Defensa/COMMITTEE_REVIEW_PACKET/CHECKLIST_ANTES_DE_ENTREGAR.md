# CHECKLIST ANTES DE ENTREGAR — 35 ítems / 5 gates pre-entrega al comité FADA-FP-UNA

**Tesis:** Anotación semiautomática del corpus cartográfico abierto de Paraguay con modelos multimodales fundacionales y una interfaz conversacional para la reflexión territorial

**Autor:** Iván Weiss Van Der Pol

**Origen:** Split de **T124** `[P0][M10][NO-GPU][D] Thesis committee review + revisions`

**Fecha del paquete:** 2026-09-02

---

## §1 — Cómo usar este checklist

Este checklist cubre **35 ítems en 5 gates** que Iván debe verificar antes de entregar la versión revisada del manuscrito al comité FADA-FP-UNA. Los ítems se dividen en:

- 🔴 **BLOQUEANTE** (debe estar ✅ antes de imprimir): típicamente 18 ítems.
- 🟡 **RECOMENDABLE** (debe estar ✅ o tener nota explicativa): típicamente 12 ítems.
- 🟢 **OK** (puede estar pendiente, no afecta la entrega): típicamente 5 ítems.

**Tiempo total estimado:** 4–6 horas de revisión + ajustes finales. Se recomienda hacer esta revisión 2–3 días antes de la fecha límite interna, no el mismo día de la entrega.

---

## §2 — Gate A — Respuesta al dictamen (8 ítems)

### A.1 — Tabla de observaciones completa 🔴

> ¿La tabla de `RESPONSE_LOG_TEMPLATE.md` §3 tiene una fila por cada observación del comité?

- [ ] ✅ Sí, todas las observaciones están mapeadas
- [ ] 🔴 No, falta mapear observaciones → **ACCIÓN:** agregar filas faltantes antes de imprimir

### A.2 — Cada observación con respuesta A-C-J-O 🔴

> ¿Cada fila tiene la respuesta estructurada según el marco de `RESPONSE_FRAMEWORK.md` (Acknowledge → Cite → Justify → Offer)?

- [ ] ✅ Sí, todas con A-C-J-O completo
- [ ] 🔴 No, hay respuestas improvisadas → **ACCIÓN:** reescribir usando el marco

### A.3 — Observaciones tipo A consultadas con director 🔴

> ¿Las observaciones tipo A (revisión mayor) fueron consultadas con el director de tesis antes de comprometer la respuesta?

- [ ] ✅ Sí, todas con visto bueno del director
- [ ] 🔴 No → **ACCIÓN:** consultar al director antes de imprimir (reunión 1–2 horas)

### A.4 — Observaciones tipo C con anclaje a literatura 🔴

> ¿Cada observación tipo C (observación de fondo) tiene al menos 1 cita a literatura comparable?

- [ ] ✅ Sí, todas con cita comparable
- [ ] 🔴 No → **ACCIÓN:** agregar citas a `REFERENCES.bib` antes de imprimir

### A.5 — Plazo formal respetado 🔴

> ¿La fecha de respuesta está dentro del plazo formal FADA (típicamente 15–30 días desde la recepción del dictamen)?

- [ ] ✅ Sí, con al menos 5 días de margen
- [ ] 🔴 No, está al límite → **ACCIÓN:** solicitar prórroga tácita a Secretaría FADA
- [ ] 🔴 No, se pasó del plazo → **ACCIÓN:** consultar al director + secretaría, explicar motivo

### A.6 — Memo de cambios presente 🔴

> ¿La primera página del manuscrito revisado tiene el memo de cambios (ver `RESPONSE_LOG_TEMPLATE.md` §4)?

- [ ] ✅ Sí, memo completo con todas las observaciones
- [ ] 🔴 No → **ACCIÓN:** generar el memo usando la plantilla

### A.7 — Carta formal firmada 🔴

> ¿La carta formal (ver `RESPONSE_LOG_TEMPLATE.md` §2) está firmada por Iván + director (+ codirector + veedor si aplica)?

- [ ] ✅ Sí, firmas completas
- [ ] 🔴 No → **ACCIÓN:** coordinar firmas antes de imprimir

### A.8 — Versión con cambios resaltados 🟡

> ¿La versión entregada al comité tiene los cambios resaltados en amarillo (o similar) para facilitar la re-revisión?

- [ ] ✅ Sí, PDF con marcas de revisión
- [ ] 🟡 No, solo versión limpia → **NOTA:** incluir versión limpia + versión con marcas en USB

---

## §3 — Gate B — Formato del manuscrito (8 ítems)

### B.1 — Formato APA 7 consistente 🔴

> ¿Todas las citas en el texto siguen el formato APA 7 (Apellido et al., Año)?

- [ ] ✅ Sí, todas consistentes
- [ ] 🔴 No → **ACCIÓN:** correr `make format-manuscript` para normalizar

### B.2 — Bibliografía completa 🔴

> ¿Todas las obras citadas en el texto aparecen en `REFERENCES.bib`?

- [ ] ✅ Sí, todas en `REFERENCES.bib`
- [ ] 🔴 No → **ACCIÓN:** agregar entradas faltantes usando gestor BibTeX

### B.3 — Figuras a 300 DPI mínimo 🔴

> ¿Todas las figuras del manuscrito están a 300 DPI mínimo con metadatos (autor, fecha, fuente)?

- [ ] ✅ Sí, todas verificadas
- [ ] 🔴 No → **ACCIÓN:** regenerar figuras faltantes (ver OBJ-02 en `TOP_25_LIKELY_OBJECTIONS.md`)

### B.4 — Tablas con leyenda y unidades 🔴

> ¿Todas las tablas tienen leyenda explícita + unidades (cuando aplica) + fuente de datos?

- [ ] ✅ Sí, todas verificadas
- [ ] 🔴 No → **ACCIÓN:** agregar leyendas y unidades faltantes

### B.5 — Numeración de figuras/tablas consistente 🔴

> ¿La numeración de figuras y tablas es consistente en Cap. 1–6 (e.g., no hay "Figura 4.2" en Cap. 5)?

- [ ] ✅ Sí, verificada con `make format-manuscript-check`
- [ ] 🔴 No → **ACCIÓN:** corregir numeración, actualizar referencias cruzadas

### B.6 — Referencias cruzadas válidas 🔴

> ¿Todas las referencias internas del manuscrito ("ver Cap. X", "ver §Y", "ver Tabla Z") apuntan a secciones existentes?

- [ ] ✅ Sí, verificadas
- [ ] 🔴 No → **ACCIÓN:** corregir referencias rotas (probablemente por poda o reorganización)

### B.7 — Formato FADA-FP-UNA cumplido 🟡

> ¿El manuscrito cumple con el formato específico FADA-FP-UNA (portada, márgenes, fuente Times New Roman 12 pt, interlineado 1.5)?

- [ ] ✅ Sí, cumple con Manual de Normas FADA 2020
- [ ] 🟡 Parcialmente → **NOTA:** ajustar según feedback específico del comité

### B.8 — `make format-manuscript-check` retorna 0 errores 🔴

> ¿El comando `make format-manuscript-check` retorna 0 errores?

- [ ] ✅ Sí, 0 errores
- [ ] 🔴 No → **ACCIÓN:** corregir errores uno por uno (ver output del comando)

---

## §4 — Gate C — Contenido sustantivo (8 ítems)

### C.1 — Hipótesis H1, H2, H3 verificadas 🔴

> ¿El manuscrito verifica explícitamente las hipótesis H1, H2, H3 en Cap. 5 ó 6?

- [ ] ✅ Sí, las tres con datos cuantitativos
- [ ] 🔴 No → **ACCIÓN:** agregar verificación de la hipótesis faltante

### C.2 — Objetivos OE1–OE5 cerrados 🔴

> ¿Cada objetivo específico (OE1–OE5) tiene su cierre en Cap. 6 con resultados?

- [ ] ✅ Sí, los cinco con resultados
- [ ] 🔴 No → **ACCIÓN:** agregar cierre del objetivo faltante

### C.3 — Pregunta de investigación respondida 🔴

> ¿La pregunta de investigación de `FORMAL_PROPOSAL.md` está explícitamente respondida en Cap. 6?

- [ ] ✅ Sí, respondida con datos
- [ ] 🔴 No → **ACCIÓN:** agregar párrafo explícito en Cap. 6 §6.1

### C.4 — Limitaciones explícitas 🔴

> ¿La sección de Limitaciones (Cap. 5 §5.6) tiene al menos 5 limitaciones cuantificadas?

- [ ] ✅ Sí, 5+ limitaciones con datos
- [ ] 🔴 No → **ACCIÓN:** expandir la sección (ver OBJ-08 en `TOP_25_LIKELY_OBJECTIONS.md`)

### C.5 — Trabajo futuro concreto 🔴

> ¿La sección de Trabajo futuro (Cap. 6 §6.4) tiene al menos 5 líneas explícitas con cronograma?

- [ ] ✅ Sí, 5+ líneas con cronograma
- [ ] 🔴 No → **ACCIÓN:** expandir la sección (ver OBJ-04)

### C.6 — Reproducibilidad declarada 🟡

> ¿El manuscrito declara explícitamente cómo reproducir el experimento (commit hash, seeds, DOI)?

- [ ] ✅ Sí, sección de notas metodológicas completa
- [ ] 🟡 Parcialmente → **NOTA:** completar la tabla de stack tecnológico (OBJ-22)

### C.7 — Comparación con literatura comparable 🟡

> ¿El manuscrito compara resultados con al menos 5 trabajos similares (MapBiomas, GeoWiki, etc.)?

- [ ] ✅ Sí, tabla de comparación con 8+ trabajos
- [ ] 🟡 Parcialmente → **NOTA:** expandir tabla de trabajos relacionados (OBJ-16)

### C.8 — Discusión de sesgos algorítmicos 🟡

> ¿El manuscrito discute cuantitativamente el sesgo regional + racial + de género de los modelos foundation?

- [ ] ✅ Sí, con datos cuantitativos
- [ ] 🟡 Parcialmente → **NOTA:** expandir análisis si el comité lo requiere

---

## §5 — Gate D — Ética y atribución (6 ítems)

### D.1 — 8 chequeos éticos en verde 🔴

> ¿Los 8 checks de `COMMITTEE_ETHICS_CHECK.md` están ✅?

- [ ] ✅ Sí, los 8 ✅
- [ ] 🔴 No → **ACCIÓN:** resolver el check faltante antes de imprimir

### D.2 — FPIC documentado 🔴

> ¿El cuaderno de campo tiene el proceso FPIC documentado para las 4 comunidades?

- [ ] ✅ Sí, documentado
- [ ] 🔴 No → **ACCIÓN:** agregar al cuaderno de campo antes de imprimir

### D.3 — Anonimización verificada 🔴

> ¿El comando grep de `COMMITTEE_ETHICS_CHECK.md` §2 Check 2 retorna cero hits?

- [ ] ✅ Sí, cero hits
- [ ] 🔴 No → **ACCIÓN:** anonimizar datos personales antes de imprimir

### D.4 — Atribuciones completas 🔴

> ¿Cada dataset, modelo, código tiene atribución explícita (nombre, fuente, licencia, DOI)?

- [ ] ✅ Sí, todas verificadas
- [ ] 🔴 No → **ACCIÓN:** agregar atribuciones faltantes

### D.5 — Licencias compatibles 🟡

> ¿La tabla de compatibilidad de licencias en Cap. 3 §3.2 está completa?

- [ ] ✅ Sí, todas las combinaciones verificadas
- [ ] 🟡 Parcialmente → **NOTA:** completar si el comité pide detalles

### D.6 — Protocolo de retirada publicado 🟡

> ¿El README del dataset en Hugging Face Hub tiene la sección "Data withdrawal protocol"?

- [ ] ✅ Sí, protocolo publicado
- [ ] 🟡 Pendiente → **NOTA:** publicar antes de la defensa, no es bloqueante para el comité

---

## §6 — Gate E — Logística (5 ítems)

### E.1 — 3 copias físicas impresas 🔴

> ¿Se imprimieron 3 copias físicas del manuscrito revisado (una por cada evaluador con voto)?

- [ ] ✅ Sí, 3 copias en papel
- [ ] 🔴 No → **ACCIÓN:** imprimir 3 copias en copiadora FADA (USD 5–10 total)

### E.2 — Copia digital en USB 🔴

> ¿La versión digital (PDF/A) está en USB etiquetada con nombre + fecha + dictamen?

- [ ] ✅ Sí, USB lista
- [ ] 🔴 No → **ACCIÓN:** copiar PDF/A al USB, etiquetar, verificar legibilidad en otro computador

### E.3 — Membrete FADA + logos en carta formal 🔴

> ¿La carta formal tiene el membrete FADA-FP-UNA y los logos institucionales?

- [ ] ✅ Sí, membrete y logos presentes
- [ ] 🔴 No → **ACCIÓN:** descargar logos de la web institucional, agregar al header

### E.4 — Datos de cabecera completos 🔴

> ¿Los 11 campos de cabecera de `RESPONSE_LOG_TEMPLATE.md` §1 están llenos?

- [ ] ✅ Sí, los 11 campos llenos (incluyendo placeholders resueltos)
- [ ] 🔴 No → **ACCIÓN:** completar campos faltantes antes de imprimir

### E.5 — Carta de presentación a Secretaría FADA 🟢

> ¿Se entregó también una carta de presentación a Secretaría Académica FADA (no solo al comité)?

- [ ] ✅ Sí, entregada
- [ ] 🟢 Pendiente → **NOTA:** opcional pero recomendado para mantener buena relación con secretaría

---

## §7 — Resumen del checklist

| Gate | Items | Bloqueantes 🔴 | Recomendables 🟡 | OK 🟢 |
|------|-------|----------------|-------------------|-------|
| A — Respuesta al dictamen | 8 | 7 | 1 | 0 |
| B — Formato del manuscrito | 8 | 6 | 2 | 0 |
| C — Contenido sustantivo | 8 | 5 | 3 | 0 |
| D — Ética y atribución | 6 | 4 | 2 | 0 |
| E — Logística | 5 | 4 | 0 | 1 |
| **TOTAL** | **35** | **26** | **8** | **1** |

**Si todos los 🔴 están ✅:** el manuscrito está listo para entregar.

**Si algún 🔴 está pendiente:** **NO imprimir ni entregar** hasta resolver.

**Si algún 🟡 está pendiente:** evaluar caso por caso; documentar la decisión en el memo de cambios.

**Si 🟢 está pendiente:** no es bloqueante; resolver post-defensa si se desea.

---

## §8 — Verificación final (5 minutos antes de imprimir)

Antes de mandar a imprimir las 3 copias físicas, hacer esta verificación final:

1. ✅ Todos los archivos del paquete COMMITTEE_REVIEW_PACKET/ están presentes:
   - [ ] README.md
   - [ ] COMMITTEE_COMPOSITION.md
   - [ ] TOP_25_LIKELY_OBJECTIONS.md
   - [ ] RESPONSE_FRAMEWORK.md
   - [ ] RESPONSE_LOG_TEMPLATE.md
   - [ ] MANUSCRIPT_TRIM_PLAN.md
   - [ ] BUDGET_REVISION_PLAN.md
   - [ ] ARXIV_UPDATE_PLAN.md
   - [ ] COMMITTEE_ETHICS_CHECK.md
   - [ ] CHECKLIST_ANTES_DE_ENTREGAR.md (este archivo)

2. ✅ Carta formal con firmas completas.

3. ✅ Membrete FADA + logos presentes.

4. ✅ Datos de cabecera completos (11 campos).

5. ✅ Versión digital PDF/A en USB etiquetada.

**Si todo está ✅:** imprimir 3 copias físicas y entregar en Secretaría FADA (o directamente al comité, según reglamento interno).

---

## §9 — Anti-patrones

### Anti-patrón 1 — Entregar sin verificar el checklist

> ❌ "Tengo prisa, voy a entregar el manuscrito revisado sin revisar este checklist."

**Por qué es malo:** el checklist existe porque detecta errores que toman 5 minutos en corregir pero 5 días en descubrir post-entrega (e.g., referencia cruzada rota, figura a baja resolución, firma faltante). **Siempre revisar el checklist.**

### Anti-patrón 2 — Asumir que el comité no notará detalles de formato

> ❌ "El comité evalúa el contenido, no el formato. No me preocupo por los márgenes."

**Por qué es malo:** el comité FADA-FP-UNA tiene criterios formales explícitos (Manual de Normas FADA 2020). Un manuscrito que no cumple el formato genera una observación tipo B automática. **Siempre cumplir el formato.**

### Anti-patrón 3 — Firmar la carta sin que el director la haya revisado

> ❌ "Voy a firmar la carta ahora y luego el director la revisa."

**Por qué es malo:** si el director objeta algún párrafo de la carta, hay que reimprimir todo. **Siempre coordinar firmas antes de imprimir.**

### Anti-patrón 4 — Olvidar el memo de cambios

> ❌ "El manuscrito revisado habla por sí solo, no necesito memo de cambios."

**Por qué es malo:** el memo de cambios es la primera página que lee el comité. Sin memo, tienen que reconstruir la historia de cambios ellos mismos, lo cual toma tiempo y genera fricción. **Siempre incluir el memo.**

### Anti-patrón 5 — Imprimir solo 2 copias

> ❌ "El director de tesis ya tiene una copia, solo imprimo 2 para el comité."

**Por qué es malo:** el director no es uno de los 3 evaluadores con voto. La copia del director es **adicional** a las 3 copias para el comité. **Siempre imprimir 3 + 1 para Iván + 1 para director = 5 copias totales** (o mínimo 3 + 1 para Iván).
