# MANUSCRIPT TRIM PLAN — Poda del manuscrito si el comité pide reducir extensión

**Tesis:** Anotación semiautomática del corpus cartográfico abierto de Paraguay con modelos multimodales fundacionales y una interfaz conversacional para la reflexión territorial

**Autor:** Iván Weiss Van Der Pol

**Origen:** Split de **T124** `[P0][M10][NO-GPU][D] Thesis committee review + revisions`

**Fecha del paquete:** 2026-09-02

---

## §1 — Contexto y estado actual

El manuscrito actual (Cap. 1–6 + anexos) tiene **26,301 palabras** (verificado `make format-manuscript-check` el 2026-09-01, ver PROGRESS.md). El estándar FADA-FP-UNA para tesis de Maestría en Cartografía es **18,000–22,000 palabras** (rango según el reglamento interno, no publicado formalmente). Si el comité objeta que el manuscrito es "excesivamente extenso para una maestría" (probabilidad media-baja: 2.5/10), este plan propone rutas de poda por capítulo con el objetivo de llegar a **~20,000 palabras** (punto medio del rango).

**Riesgo asociado:** R-NEW-30.

---

## §2 — Distribución actual de palabras por capítulo

| Capítulo | Palabras actuales | % del total | Densidad |
|----------|-------------------|-------------|----------|
| Cap. 1 — Introducción | 2,777 | 10.6% | Normal para intro |
| Cap. 2 — Marco teórico | 3,846 | 14.6% | Normal para marco teórico |
| Cap. 3 — Metodología | 7,262 | 27.6% | **Alto** — oportunidad de poda |
| Cap. 4 — Resultados | 5,507 | 20.9% | **Alto** — pero Cap. 4 es crítico |
| Cap. 5 — Discusión | 4,367 | 16.6% | Normal |
| Cap. 6 — Conclusiones | 2,542 | 9.7% | Normal para cierre |
| **TOTAL** | **26,301** | **100%** | — |

**Lectura:** los capítulos con mayor potencial de poda son Cap. 3 (Metodología) y Cap. 4 (Resultados), pero Cap. 4 es **crítico** (es donde están los placeholders que se llenan post-experimentos). Podar Cap. 4 es de alto riesgo. Cap. 3 es la mejor oportunidad de poda segura.

---

## §3 — Rutas de poda (3 opciones)

### Opción A — **Poda conservadora** (objetivo: 22,000 palabras, poda de 4,300)

**Filosofía:** podar solo lo redundante, sin alterar la estructura ni la coherencia interna.

**Cambios específicos:**

1. **Cap. 3 §3.4 (Selección de modelos)** — poda de 800 palabras. Eliminar descripción detallada de los 12 modelos candidatos (mantener solo 6 en tabla comparativa + texto resumido). Ahorro: 800 palabras.
2. **Cap. 3 §3.7 (Validación)** — poda de 600 palabras. Eliminar subsección de "validación cruzada con 5-fold" (mantener referencia pero mover a anexo). Ahorro: 600 palabras.
3. **Cap. 4 §4.1 (Caracterización del corpus)** — poda de 400 palabras. Eliminar descripción detallada de las 387 comunidades (mantener tabla resumen). Ahorro: 400 palabras.
4. **Cap. 5 §5.2 (Comparación con literatura)** — poda de 700 palabras. Eliminar subsección "extensión a otros dominios" (mover a Cap. 6 trabajo futuro). Ahorro: 700 palabras.
5. **Cap. 5 §5.6 (Limitaciones)** — poda de 500 palabras. Consolidar las 7 limitaciones en 5, eliminando las 2 más especulativas. Ahorro: 500 palabras.
6. **Cap. 2 §2.5 (Visión por computador)** — poda de 500 palabras. Eliminar subsección de "redes convolucionales clásicas" (considerar conocimiento previo). Ahorro: 500 palabras.
7. **Anexos** — consolidar 3 anexos en 1, eliminando redundancias. Ahorro: 800 palabras (cuenta en anexo, no en total Cap. 1-6).

**Total Opción A:** ~4,300 palabras podadas, manuscrito queda en 22,000 palabras. **Tiempo:** 6–8 horas.

**Riesgo:** bajo. No altera la coherencia ni la cobertura.

---

### Opción B — **Poda moderada** (objetivo: 20,000 palabras, poda de 6,300)

**Filosofía:** todo lo de Opción A + reorganización de Cap. 3 + eliminación de una sección completa.

**Cambios específicos (adicionales a Opción A):**

1. **Cap. 3 §3.5 (Fine-tune)** — poda de 1,000 palabras. Mover detalles de implementación (hiperparámetros, regularización, early stopping) a anexo, dejar solo la descripción metodológica. Ahorro: 1,000 palabras.
2. **Cap. 2 §2.7 (Trabajos relacionados)** — poda de 500 palabras. Reducir de 15 a 8 entradas en la tabla 2.3. Ahorro: 500 palabras.
3. **Cap. 4 §4.5 (Interfaz conversacional)** — poda de 500 palabras. Reducir ejemplos de diálogo (mantener solo 2 en lugar de 4). Ahorro: 500 palabras.

**Total Opción B:** ~6,300 palabras podadas (4,300 + 2,000), manuscrito queda en 20,000 palabras. **Tiempo:** 10–14 horas.

**Riesgo:** medio. Requiere reorganización + mover contenido a anexos.

---

### Opción C — **Poda agresiva** (objetivo: 18,000 palabras, poda de 8,300)

**Filosofía:** todo lo de Opción B + eliminación de una sección completa + fusión de dos capítulos.

**Cambios específicos (adicionales a Opción B):**

1. **Fusión Cap. 5 + Cap. 6** — reducción de 1,500 palabras. Eliminar la separación rígida entre Discusión y Conclusiones; crear un Cap. 5 unificado "Discusión y Conclusiones". Ahorro: 1,500 palabras.
2. **Cap. 4 §4.6 (Validación con expertos)** — poda de 500 palabras. Eliminar subsección de "sesgo de automatización" (cubrir en Cap. 5 con 1 párrafo). Ahorro: 500 palabras.

**Total Opción C:** ~8,300 palabras podadas (6,300 + 2,000), manuscrito queda en 18,000 palabras. **Tiempo:** 16–22 horas.

**Riesgo:** alto. La fusión Cap. 5 + Cap. 6 rompe la estructura tradicional del manuscrito FADA. Algunos miembros del comité podrían objetar el cambio de estructura tanto como objetaban la extensión original.

---

## §4 — Recomendación por defecto

**Recomiendo Opción A (poda conservadora)** como primera línea de respuesta. Justificación:

1. Cubre el 80% de la posible objeción ("manuscrito extenso") con el 50% del esfuerzo.
2. No altera la estructura ni la coherencia.
3. Deja margen para 1 ronda adicional de revisión menor sin tener que volver a podar.
4. Iván puede ejecutar la poda en una sesión de trabajo (sábado o domingo) y entregar la versión revisada el lunes.

**Si el comité insiste en poda adicional después de Opción A:** pasar a Opción B, evaluando caso por caso.

**Opción C solo si el comité lo pide explícitamente** — no se justifica por iniciativa propia porque el riesgo de romper la estructura es alto.

---

## §5 — Proceso de ejecución (Opción A)

### Paso 1 — Inventariar las secciones a podar (1 hora)

1. Releer Cap. 3 §3.4, §3.5, §3.7 con highlighting de párrafos candidatos a poda.
2. Releer Cap. 4 §4.1, §4.5, §4.6 con highlighting.
3. Releer Cap. 5 §5.2, §5.6 con highlighting.
4. Releer Cap. 2 §2.5 con highlighting.
5. Crear lista de párrafos específicos a podar (con número de palabra aproximado).

### Paso 2 — Podar y verificar coherencia (4–5 horas)

1. Para cada sección, aplicar la poda según el plan de §3 Opción A.
2. Después de cada sección podada, releer el contexto inmediato (2 párrafos antes y 2 después) para verificar coherencia.
3. Si una poda rompe coherencia, revertirla y elegir un párrafo alternativo.

### Paso 3 — Verificar referencias cruzadas (30 minutos)

1. Verificar que ninguna cita, tabla o figura del manuscrito apunte a una sección eliminada.
2. Actualizar las referencias cruzadas (e.g., "ver §3.4 para detalles de implementación" → "ver §3.4 para resumen, anexo B para detalles").

### Paso 4 — Validación con make (30 minutos)

1. `make format-manuscript` — verificar que no se rompió el formato.
2. `make format-manuscript-check` — debe retornar 0 errors.
3. `wc -w Capitulos/Cap*.md` — confirmar que el total está en ~22,000.

### Paso 5 — Memo de cambios en manuscrito revisado (30 minutos)

1. Agregar al memo de cambios (ver `RESPONSE_LOG_TEMPLATE.md` §4) la mención explícita: "Se realizó poda conservadora del manuscrito de 26,301 a 22,000 palabras, eliminando redundancias en §3.4, §3.5, §3.7, §4.1, §4.5, §5.2, §5.6 sin afectar coherencia ni cobertura. Detalles en `MANUSCRIPT_TRIM_PLAN.md`."

---

## §6 — Riesgos de la poda

| Riesgo | Descripción | Mitigación |
|--------|-------------|------------|
| **R-NEW-32** | La poda elimina accidentalmente una cita o referencia cruzada | Paso 3 del proceso de ejecución + verificación con `make format-manuscript-check` |
| **R-NEW-33** | El comité objeta la poda (e.g., "ahora falta información sobre X") | Responder con la referencia al anexo donde se movió el contenido (no se eliminó, se reubicó) |
| **R-NEW-34** | Iván pierde tiempo podando y luego el comité acepta el manuscrito original (26,301 palabras) | El costo de la poda es ~6–8 horas, que es bajo comparado con el costo de una revisión mayor |

---

## §7 — Anti-patrones (qué NO hacer al podar)

### Anti-patrón 1 — Podar la sección de Limitaciones

> ❌ "El manuscrito es muy largo, voy a reducir la §5.6 Limitaciones de 4 a 1.5 páginas."

**Por qué es malo:** la sección de Limitaciones es **crítica** para mostrar honestidad metodológica. Un comité que objeta extensión no va a aceptar que las Limitaciones se reduzcan — es contraproducente.

### Anti-patrón 2 — Podar las figuras o tablas

> ❌ "Voy a eliminar las figuras 4.15 a 4.20 porque el manuscrito es muy largo."

**Por qué es malo:** las figuras y tablas son **evidencia** de los experimentos. Eliminarlas reduce el rigor. Si una figura es redundante, marcarla como "[incluida en anexo]" en lugar de eliminarla.

### Anti-patrón 3 — Cambiar la numeración de secciones sin actualizar referencias cruzadas

> ❌ Podar §3.4 y renumerar como §3.4a, sin actualizar las 12 referencias a §3.4 en otros capítulos.

**Por qué es malo:** genera referencias rotas. Siempre correr `make format-manuscript-check` después de podar.

### Anti-patrón 4 — Podar el abstract

> ❌ "El abstract es muy largo, voy a reducirlo de 280 a 200 palabras."

**Por qué es malo:** el abstract es la primera (y a veces única) sección que lee un miembro del comité. Recortarlo reduce la claridad del manuscrito. Si el comité objeta el abstract, casi siempre es por falta de explicitud (OBJ-03), no por extensión.

---

## §8 — Después de la poda: cómo verificar el éxito

1. **Recuento de palabras:** `wc -w Capitulos/Cap*.md` debe retornar ~22,000 (Opción A) o ~20,000 (Opción B).
2. **Coherencia interna:** releer Cap. 1–6 secuencialmente, verificar que la narrativa fluya sin saltos.
3. **Verificación de referencias:** `grep -n "Cap\.\|§\|Tabla\|Figura" Capitulos/*.md | wc -l` debe retornar un número similar al original (no debe haber caído más de 10%).
4. **Validación de formato:** `make format-manuscript-check` debe retornar 0 errors.
5. **Verificación de placeholders:** `grep -c "LLENAR\|PLACEHOLDER" Capitulos/Cap*.md` debe retornar el mismo número que antes de la poda (no eliminar placeholders accidentalmente).
