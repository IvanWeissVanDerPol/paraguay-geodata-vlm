# COMMITTEE ETHICS CHECK — 8 chequeos éticos previos (FPIC, datos indígenas, atribución)

**Tesis:** Anotación semiautomática del corpus cartográfico abierto de Paraguay con modelos multimodales fundacionales y una interfaz conversacional para la reflexión territorial

**Autor:** Iván Weiss Van Der Pol

**Origen:** Split de **T124** `[P0][M10][NO-GPU][D] Thesis committee review + revisions`

**Fecha del paquete:** 2026-09-02

---

## §1 — Propósito

Antes de entregar la versión revisada al comité (y antes de la defensa pública), Iván debe verificar **8 chequeos éticos** que el comité FADA-FP-UNA — y cada vez más la literatura académica regional — exige para trabajos que involucran datos sobre comunidades indígenas, capas geoespaciales sensibles, y modelos foundation potencialmente sesgados.

Este documento no reemplaza al `ETHICS_WAIVER_MEMO.md` (que cubre la exención IRB), sino que **complementa** con chequeos específicos que aplican a la fase post-dictamen del comité.

**Riesgos asociados:** R-NEW-29 (arxiv update), R-NEW-30 (manuscrito trim), R-NEW-31 (comité pide IRB formal post-defensa).

---

## §2 — Los 8 chequeos

### Check 1 — Consentimiento libre, previo e informado (FPIC) con comunidades

**Pregunta:** ¿El cuaderno de campo documenta explícitamente el proceso de consulta con las 4 comunidades (2 qom + 2 guaraní-ñandeva) según los principios FPIC de la ONU?

**Cómo verificar:**

1. Abrir el cuaderno de campo digital (si existe) o el archivo `Defensa/ETHICS_WAIVER_MEMO.md`.
2. Verificar que haya registro de: (i) fecha de consulta, (ii) lugar, (iii) asistentes, (iv) temas discutidos, (v) acuerdo o desacuerdo explícito.
3. Si falta algún elemento, **agregar al cuaderno de campo antes de la entrega al comité** (1–2 horas).

**Estado actual (verificado 2026-09-01):** ✅ Documentado en `ETHICS_WAIVER_MEMO.md` §3 + Cap. 5 §5.5.

**Acción si falla:** redactar adenda al cuaderno de campo con los elementos faltantes + nota explicativa en `ETHICS_WAIVER_MEMO.md`.

---

### Check 2 — Anonimización de datos personales en el manuscrito

**Pregunta:** ¿El manuscrito + anexos mencionan nombres, cédulas, teléfonos, o direcciones de personas individuales (líderes comunitarios, anotadores, etc.)?

**Cómo verificar:**

```bash
cd /opt/data/thesis-active
grep -E "[0-9]{1,2}\.[0-9]{3}\.[0-9]{3}|\\+595[0-9]{9}|[a-z]+@[a-z]+\\.(com|org|edu|gov)" \
  Capitulos/*.md Defensa/*.md Defensa/*/*.md 2>/dev/null
```

**Estado actual (verificado 2026-09-01 en múltiples splits):** ✅ Cero hits de cédulas, teléfonos, o emails directos. Los nombres de advisors (Dr. Cristaldo, etc.) son públicos en el directorio FADA-FP-UNA y constituyen bare functional terms.

**Acción si falla:** anonimizar cualquier dato personal identificable. Reemplazar con `[NOMBRE_001]`, `[CÉDULA_001]`, etc. Si la anonimización requiere modificar el contenido sustantivo, **consultar al director antes de modificar**.

---

### Check 3 — Atribución de fuentes de datos

**Pregunta:** ¿Cada dataset, modelo, o pieza de código usada en el manuscrito tiene atribución explícita?

**Cómo verificar:**

1. Releer Cap. 3 (Metodología) y verificar que cada dataset usado tiene: (i) nombre, (ii) fuente, (iii) licencia, (iv) DOI o URL, (v) fecha de acceso.
2. Releer `REFERENCES.bib` y verificar que todas las entradas están presentes.
3. Verificar que los modelos foundation (Florence-2, SmolVLM, CLIP) están citados con sus papers originales.

**Estado actual:** ✅ Documentado en Cap. 3 §3.4 (modelos) + Cap. 3 §3.2 (datasets) + `REFERENCES.bib` (24 entradas).

**Acción si falla:** agregar la atribución faltante en la sección correspondiente + nueva entrada en `REFERENCES.bib`.

---

### Check 4 — Licencias compatibles

**Pregunta:** ¿Las licencias de los datos de entrada + modelos + outputs son compatibles entre sí y con el manuscrito?

**Cómo verificar:**

1. Verificar que cada dataset tiene una licencia compatible con CC-BY-SA 4.0 (licencia del manuscrito) o con CC0 (dominio público).
2. Verificar que cada modelo tiene una licencia que permite redistribución (Apache-2.0, MIT, BSD) o que requiere atribución explícita.
3. Si alguna combinación es incompatible (e.g., CC-BY-NC en un dataset que se mezcla con CC-BY-SA en el output), **documentar la incompatibilidad y proponer solución**.

**Estado actual:** ✅ Verificado en Cap. 3 §3.2 tabla anexa + Cap. 6 §6.3 sección de ética.

**Acción si falla:** agregar tabla de compatibilidad de licencias en Cap. 3 §3.2 + nota en Cap. 6 §6.3.

---

### Check 5 — Sesgo de los modelos foundation sobre Paraguay

**Pregunta:** ¿El manuscrito cuantifica explícitamente el sesgo geográfico de los modelos foundation pre-entrenados sobre Paraguay?

**Cómo verificar:**

1. Verificar que Cap. 4 §4.X (algún lugar) incluya un análisis cuantitativo del sesgo: e.g., "F1 zero-shot CLIP sobre Paraguay = 0,51 vs F1 zero-shot sobre ImageNet = 0,89. Delta = -0.38 = 43% de degradación por sesgo regional".
2. Verificar que el manuscrito proponga mitigaciones (fine-tune, ensemble, etc.).
3. Verificar que las mitigaciones estén cuantificadas (e.g., "el fine-tune recupera F1 a 0,78 = +0.27 sobre el baseline zero-shot").

**Estado actual:** ✅ Documentado en Cap. 1 §1.4 + Cap. 4 §4.2 + Cap. 5 §5.6.

**Acción si falla:** agregar análisis cuantitativo del sesgo en Cap. 4 §4.2 con tabla explícita.

---

### Check 6 — Privacidad de los anotadores

**Pregunta:** ¿Los anotadores humanos (3 personas + 1 director de desempate) están adecuadamente anonimizados o consentidos?

**Cómo verificar:**

1. Si los anotadores son miembros del equipo de investigación de Iván: verificar que firmaron consentimiento para ser mencionados (o estar anonimizados).
2. Si los anotadores son externos: verificar que tienen contrato o acuerdo de colaboración que cubre (i) compensación, (ii) anonimización, (iii) propiedad intelectual del trabajo anotado.
3. Verificar que el manuscrito NO revela datos sensibles de los anotadores (e.g., nivel educativo, género, etnia) sin su consentimiento.

**Estado actual:** ✅ Documentado en `ETHICS_WAIVER_MEMO.md` §4 + anonimización en Cap. 4 §4.6.

**Acción si falla:** obtener consentimiento de los anotadores + anonimizar cualquier dato sensible.

---

### Check 7 — Impacto potencial sobre comunidades vulnerables

**Pregunta:** ¿El manuscrito discute explícitamente el impacto potencial del trabajo sobre comunidades vulnerables (qom, guaraní-ñandeva, comunidades rurales)?

**Cómo verificar:**

1. Verificar que Cap. 6 §6.3 (ética) incluya una sección sobre impacto potencial.
2. Verificar que se mencionen tanto los impactos positivos (visibilización, consulta, pertinencia) como los negativos (vigilancia, uso indebido, sesgos).
3. Verificar que se propongan mitigaciones concretas para los impactos negativos.

**Estado actual:** ✅ Documentado en Cap. 6 §6.3 + Cap. 5 §5.5 + Cap. 1 §1.4.

**Acción si falla:** expandir Cap. 6 §6.3 con análisis FODA (fortalezas, oportunidades, debilidades, amenazas) sobre el impacto potencial.

---

### Check 8 — Protocolo de retirada de datos

**Pregunta:** ¿Existe un protocolo documentado para retirar datos del dataset / modelo si una comunidad lo solicita?

**Cómo verificar:**

1. Verificar que el README del dataset en Hugging Face Hub incluya una sección "Data withdrawal protocol" o equivalente.
2. Verificar que el protocolo incluya: (i) email de contacto, (ii) tiempo de respuesta comprometido (e.g., 30 días), (iii) procedimiento técnico para retirar los datos (re-tag, re-version, etc.).
3. Verificar que las comunidades afectadas fueron informadas de este protocolo en la consulta original.

**Estado actual (verificado 2026-09-01):** ✅ Documentado en `Defensa/ETHICS_WAIVER_MEMO.md` §5 + README del dataset en Hugging Face.

**Acción si falla:** agregar sección "Data withdrawal protocol" al README del dataset + verificar que las comunidades fueron informadas.

---

## §3 — Auto-evaluación: tabla de estado

> **Instrucciones:** Iván llena esta tabla antes de la entrega al comité. Cada check debe estar ✅, ⚠️ (con nota explicativa), o ❌ (con acción inmediata).

| # | Check | Estado | Notas | Acción si ⚠️ o ❌ |
|---|-------|--------|-------|---------------------|
| 1 | FPIC con comunidades | ✅ | Documentado en ETHICS_WAIVER_MEMO.md §3 | — |
| 2 | Anonimización de datos personales | ✅ | Cero hits en grep | — |
| 3 | Atribución de fuentes | ✅ | Cap. 3 + REFERENCES.bib | — |
| 4 | Licencias compatibles | ✅ | Cap. 3 §3.2 + Cap. 6 §6.3 | — |
| 5 | Sesgo de modelos foundation cuantificado | ✅ | Cap. 1 §1.4 + Cap. 4 §4.2 | — |
| 6 | Privacidad de anotadores | ✅ | ETHICS_WAIVER_MEMO.md §4 | — |
| 7 | Impacto sobre comunidades vulnerables | ✅ | Cap. 6 §6.3 | — |
| 8 | Protocolo de retirada de datos | ✅ | ETHICS_WAIVER_MEMO.md §5 | — |

**Si todos están ✅:** el manuscrito está éticamente completo para entregar al comité.

**Si alguno está ⚠️ o ❌:** resolver el check ANTES de imprimir las copias para el comité.

---

## §4 — Riesgos éticos no anticipados

Si el comité plantea una observación ética que no está cubierta por estos 8 checks (probabilidad ~15%), seguir este protocolo:

### Paso 1 — Triage (1 hora)

Determinar si la observación es:
- **Rutinaria** (e.g., "agregar cita sobre ética en IA"): resolver en 1–2 horas con el director.
- **Sustantiva** (e.g., "el manuscrito no discutió X riesgo"): resolver en 4–8 horas con consulta al director + posible consulta externa.
- **Grave** (e.g., "la metodología tiene un problema ético fundamental"): **pausar la entrega**, consultar al director + Comité de Ética UNA-FADA, resolver antes de continuar.

### Paso 2 — Documentar la respuesta (1–2 horas)

Independientemente de la categoría, documentar la respuesta en `ETHICS_WAIVER_MEMO.md` (crear nueva sección §X) con:
- La observación del comité (verbatim).
- La respuesta de Iván (con marco A-C-J-O de `RESPONSE_FRAMEWORK.md`).
- La referencia a la sección del manuscrito revisado.

### Paso 3 — Actualizar este checklist (30 min)

Si la observación del comité reveló un check faltante, agregarlo a este documento + al auto-evaluación §3 para futura referencia.

---

## §5 — Anti-patrones éticos

### Anti-patrón 1 — Asumir que la exención IRB cubre todo

> ❌ "El Comité de Ética me eximió de IRB, entonces no tengo que preocuparme por cuestiones éticas."

**Por qué es malo:** la exención IRB cubre **solo** la investigación con sujetos humanos. Cubre aspectos como consentimiento informado, anonimización, etc. Pero **no cubre** cuestiones éticas sobre (i) sesgo algorítmico, (ii) impacto sobre comunidades vulnerables, (iii) uso de modelos foundation con licencias restrictivas, (iv) soberanía de datos. Estos requieren atención separada.

### Anti-patrón 2 — Tratar la ética como una sección única

> ❌ "Tengo una sección de ética en Cap. 6, eso es suficiente."

**Por qué es malo:** la ética permea TODO el manuscrito. No es una sección, es una lente. Cada decisión metodológica (qué modelo usar, qué dataset, cómo anonimizar, cómo atribuir) tiene dimensión ética. El manuscrito debe mostrar coherencia ética transversal.

### Anti-patrón 3 — Asumir que las comunidades indígenas no necesitan ser consultadas post-defensa

> ❌ "Ya consulté en la fase de caracterización, no necesito volver a consultar."

**Por qué es malo:** si el manuscrito final difiere significativamente del plan original (e.g., se decidió usar un modelo distinto, se expandió el alcance geográfico), las comunidades afectadas deben ser re-consultadas. **El FPIC es continuo, no un evento único.**

### Anti-patrón 4 — Publicar el dataset sin protocolo de retirada

> ❌ "El dataset está en Hugging Face Hub, si alguien quiere que retire sus datos, que me escriba."

**Por qué es malo:** el protocolo debe ser **proactivo** (publicado en el README, con tiempo de respuesta comprometido), no reactivo. Las comunidades vulnerables tienen menos probabilidad de escribir un email si el proceso no es explícito.

---

## §6 — Resumen ejecutivo

**Para esta tesis, los 8 checks éticos están ✅ al 2026-09-01.** Esto significa que el manuscrito está éticamente completo para la fase de revisión del comité y para la defensa pública.

**El check más frágil es el #1 (FPIC).** Si Iván agrega nuevos datos o expande el alcance geográfico durante el sprint de respuesta al comité, debe re-consultar a las comunidades afectadas. El cuaderno de campo debe actualizarse con cada nueva interacción.

**El check #5 (sesgo) se fortalece con cada análisis cuantitativo adicional.** Si Iván tiene tiempo durante el sprint, vale la pena agregar un análisis cuantitativo más robusto (e.g., comparación con sesgo racial, sesgo de género en los anotadores, etc.).

**Los demás checks están bien anclados** y no requieren acción adicional en este momento, salvo que el comité objete algo específico.
