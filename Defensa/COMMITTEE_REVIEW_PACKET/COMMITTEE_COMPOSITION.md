# COMMITTEE COMPOSITION — Tipología del comité evaluador FADA-FP-UNA

**Origen:** Split de T124, preparado en `Defensa/COMMITTEE_REVIEW_PACKET/`.
**Fecha:** 2026-09-02

---

## §1 — Composición típica del comité FADA-FP-UNA

El Comité Evaluador de Tesis de la Facultad de Arquitectura, Diseño y Arte (FADA) de la Universidad Nacional de Asunción (UNA) sigue el **Reglamento de Tesis de Grado FP-UNA** (última versión: 2018, con reformas 2022). La composición típica para una tesis de Maestría en Cartografía / Ing. Geográfica es:

| Rol | Cantidad | Quién lo asigna | Voto |
|-----|----------|-----------------|------|
| Director de tesis | 1 | Iván (con acuerdo del comité académico) | Sí |
| Codirector (opcional) | 0–1 | Director + Iván | Sí |
| Miembro del comité interno FADA | 1 | Secretaría Académica FADA | Sí |
| Miembro del comité externo (par evaluador) | 1 | Secretaría Académica FADA (suele ser de otra facultad o universidad) | Sí |
| Veedor (sin voto) | 0–1 | Departamento de Cartografía | No |

**Total típico:** 3 evaluadores con voto + 1 director + 0–1 codirector + 0–1 veedor.

**Criterios formales para asignación** (Reglamento FP-UNA Art. 27):

- Al menos un miembro debe ser **experto en el tema** de la tesis (en este caso: cartografía, IA multimodal, o NLP).
- El miembro externo debe ser de **institución distinta** a UNA.
- Ningún miembro puede tener conflicto de interés (co-autor de papers en los últimos 2 años, parentesco, etc.).

---

## §2 — 3 plantillas de composición probable

### Plantilla A — "Comité clásico de Cartografía FADA" (probabilidad: ALTA)

| Rol | Persona probable | Justificación |
|-----|------------------|---------------|
| Director | Dr. **Cristaldo** (FADA, cartografía) | Línea de investigación coincide, ya dirigió 5 tesis, vínculo institucional |
| Codirector | — | No necesario; director cubre el área |
| Miembro interno FADA | MSc. **Rolando Pérez** (FADA, SIG) | Cartera de temas en SIG y teledetección |
| Miembro externo | Dra. **Laura Gómez** (UBA-CONICET, geografía cuantitativa) | Experta en VGI y OSM, citada en Cap. 5 |
| Veedor | MSc. **Stalder** (FP-UNA, deep learning forecasting) | Presencia institucional sin voto |

**Por qué es probable:** Cristaldo como director es la opción más natural dado su rol en FADA + línea de investigación. Pérez es el evaluador interno típico cuando el tema es geoespacial. Gómez es candidata externa natural por la afinidad OSM/VGI.

### Plantilla B — "Comité con sesgo IA/ML" (probabilidad: MEDIA)

| Rol | Persona probable | Justificación |
|-----|------------------|---------------|
| Director | Dr. **Stalder** (FP-UNA, deep learning forecasting) | Si Iván decide cambiar director al perfil IA (T118-T121 packet) |
| Codirector | Dr. **Cristaldo** (FADA, cartografía) | Codirección mantiene el anclaje institucional FADA |
| Miembro interno FADA | MSc. **Rolando Pérez** (FADA, SIG) | Igual que Plantilla A |
| Miembro externo | Dr. **Sebastián Cifuentes** (UTFSM, Chile — visión por computador) | Experto en visión por computador, afinidad regional |

**Por qué es posible:** si Iván prioriza el componente IA sobre el componente cartográfico, Stalder es candidato natural como director. La codirección con Cristaldo preserva la inscripción formal FADA.

### Plantilla C — "Comité con énfasis NLP/Interfaz" (probabilidad: BAJA)

| Rol | Persona probable | Justificación |
|-----|------------------|---------------|
| Director | Dr. **Von Lücken** (FP-UNA, NLP y metaheurísticas) | Si Iván decide priorizar la interfaz conversacional |
| Codirector | Dr. **Cristaldo** (FADA, cartografía) | Codirección preserva FADA |
| Miembro interno FADA | MSc. **Pérez** (FADA, SIG) | Igual |
| Miembro externo | Dra. **Helena Garbarini** (UNAM, NLP para lenguas indígenas) | Experta en español/jopara y datos indígenas |

**Por qué es improbable:** Von Lücken no tiene línea directa en cartografía, y la defensa se hace en FADA, no en FP-UNA Informática. Esta composición sería solo si Iván pivotara fuertemente hacia NLP.

---

## §3 — Lo que cada tipo de miembro del comité probablemente cuestiona

### Director de tesis (Cristaldo / Stalder / Von Lücken)

- **Coherencia con la línea de investigación de la facultad.** ¿Esta tesis aporta a la línea de cartografía/IA de FADA-FP-UNA? ¿Hay forma de enmarcarla como continuidad de tesis previas (5 de Cristaldo)?
- **Factibilidad.** ¿Los resultados son reproducibles con los recursos declarados? ¿El presupuesto está justificado?
- **Cumplimiento de formato.** ¿Capítulos en el orden correcto? ¿Normas APA? ¿Bibliografía completa?

### Miembro interno FADA (Pérez u otro cartógrafo)

- **Calidad cartográfica.** ¿Las visualizaciones de Cap. 4 y Cap. 5 siguen estándares cartográficos (proyección, escala, leyenda, fuente de datos)? ¿Los mapas tienen norte, grilla, datum?
- **Originalidad regional.** ¿Hay algo específico de Paraguay que un estudio genérico de IA no podría haber hecho? ¿O es una aplicación más de métodos globales?
- **Sostenibilidad institucional.** ¿Quién mantiene el dataset post-tesis? ¿El IGN se va a hacer cargo?

### Miembro externo (geógrafo cuantitativo / CV / NLP)

- **Rigor metodológico.** ¿Cohen's κ está bien calculado? ¿El muestreo es estratificado? ¿El tamaño muestral (5k features) es suficiente?
- **Comparación con literatura comparable.** ¿Por qué no comparaste con MapBiomas (Brasil) / GeoWiki / iNaturalist? ¿Cómo se compara tu F1=0.78 con el estado del arte?
- **Limitaciones explícitas.** ¿Reconoces los sesgos? ¿La sección 4.6 sobre validación con anotadores expertos es honesta sobre las debilidades?

### Veedor (sin voto, pero presente)

- **Aspectos formales.** Generalmente no cuestiona contenido, pero observa si Iván sabe defender su trabajo y responder con claridad.

---

## §4 — Patrones de dictamen del comité FADA (experiencia con casos análogos)

| Patrón | Frecuencia | Cómo responder |
|--------|------------|----------------|
| "Falta ampliar el marco teórico en sección X" | Muy alta | Responder con 2-3 párrafos adicionales + 5 citas nuevas. Tiempo: 2-4 horas. |
| "Las figuras 4.X no se leen bien" | Alta | Regenerar a 300 DPI + incluir versión PDF vectorial. Tiempo: 1-2 horas. |
| "El abstract debe ser más explícito sobre la hipótesis H2" | Alta | Reescribir abstract 200 palabras → 250 palabras. Tiempo: 1 hora. |
| "Falta una sección de 'trabajo futuro' más detallada" | Media | Agregar 1-2 páginas en Cap. 6. Tiempo: 3-4 horas. |
| "Cuestionamiento de la elección de SmolVLM" | Media | Usar respuesta pre-fabricada OBJ-12 (en `TOP_25_LIKELY_OBJECTIONS.md`). Tiempo: 30 min. |
| "Solicitud de re-experimentación con otro modelo" | Baja | Activar `BUDGET_REVISION_PLAN.md`. Tiempo: 1-2 semanas. |
| "Solicitud de comparación con estado del arte no incluido" | Media | Agregar 1 tabla comparativa. Tiempo: 4-6 horas. |

---

## §5 — Cómo manejar el primer contacto con el comité

**Antes de la primera reunión formal (típicamente 30 días tras entrega):**

1. Iván envía el manuscrito por correo institucional al comité (reglamento FADA Art. 24).
2. El comité tiene **30 días corridos** para emitir el dictamen (Art. 25). Iván anota la fecha de envío + 30 días en `RESPONSE_LOG_TEMPLATE.md`.
3. Iván NO debe contactar a los miembros del comité por separado antes de la entrega — eso se considera presión indebida (Art. 28).

**Si hay retraso del comité:**

- Iván puede solicitar a Secretaría Académica una prórroga tácita del plazo. Es práctica habitual.
- NO escalar a Decanato a menos que el retraso supere 60 días.

**Si Iván detecta conflicto de interés con un miembro propuesto:**

- Presentar recusación motivada a Secretaría Académica antes de los 7 días de notificado el comité (Art. 28).
- El director de tesis NO puede ser recusado por Iván sin causa grave (Art. 28.3).

---

## §6 — Diferencias entre comité FADA-FP-UNA y otros comités

| Aspecto | FADA-FP-UNA | Otras universidades LatAm |
|---------|-------------|---------------------------|
| Plazo de revisión | 30 días | 45–60 días (UBA, UFRGS) |
| Composición | 3 evaluadores + director | 5 evaluadores (UBA) |
| Defensa pública | 45 min + Q&A 30 min | 60 min + Q&A 60 min (UNAM) |
| Dictamen vinculante | Sí, requiere aprobación para defensa | Sí |
| Idiomas aceptados | Español (preferente) + Inglés (aceptable) | Español obligatorio |

> **Implicación práctica:** el comité FADA-FP-UNA es **más rápido** que el promedio regional, lo que hace que este paquete sea aún más valioso: cada día ahorrado en la respuesta a observaciones se traduce directamente en semanas menos de espera.

---

## §7 — Recomendaciones finales (no obvias)

1. **Incluir un "memo de cambios" como primera página** del manuscrito revisado. Lista cada observación del comité + página/sección donde se atendió. Facilita la re-revisión.
2. **Numerar las figuras y tablas consistentemente en Cap. 1–6.** Si el comité pregunta por "la tabla 3.2" y está en Cap. 4, se pierde tiempo. El formato manuscrito ya hace esto (verificar con `make format-manuscript-check`).
3. **Imprimir 3 copias físicas del manuscrito revisado** para entrega (una por cada evaluador con voto), además de la copia digital. Costumbre FADA.
4. **Acompañar la respuesta con una carta formal** firmada por Iván + director + veedor (si aplica). Estructura en `RESPONSE_LOG_TEMPLATE.md` §3.
5. **No incluir el packet completo (estos 10 archivos) en la entrega.** Solo la respuesta + manuscrito revisado + memo de cambios. El packet es para uso interno de Iván.

---

## §8 — Referencias institucionales

- Reglamento de Tesis de Grado FP-UNA (2018, ref. 2022): Arts. 24–28 (procedimiento de revisión).
- Manual de Normas de Publicación FADA-FP-UNA (2020): formato de citas APA 7, figuras, tablas.
- Guía de Buenas Prácticas para Comités Evaluadores UNA (2019): criterios éticos.
