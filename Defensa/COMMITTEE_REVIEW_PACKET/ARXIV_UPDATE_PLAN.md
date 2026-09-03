# ARXIV UPDATE PLAN — Cómo actualizar el preprint sin retractar

**Tesis:** Anotación semiautomática del corpus cartográfico abierto de Paraguay con modelos multimodales fundacionales y una interfaz conversacional para la reflexión territorial

**Autor:** Iván Weiss Van Der Pol

**Origen:** Split de **T124** `[P0][M10][NO-GPU][D] Thesis committee review + revisions`

**Fecha del paquete:** 2026-09-02

---

## §1 — Contexto y principio rector

Una vez que el manuscrito esté en arxiv (T099, post-defensa), cualquier corrección posterior al manuscrito se enfrenta al problema de **cómo actualizar el preprint sin retractarlo**. Retractar y reenviar un paper a arxiv genera confusión en los lectores (especialmente si ya fue citado) y rompe los enlaces DOI.

Este plan documenta el protocolo oficial de arxiv para actualizar un preprint, y los criterios para decidir entre "actualización menor" (v2, v3...) versus "retractar y reenviar" (v1 con nuevo ID).

**Riesgo asociado:** R-NEW-29 (observación del comité contradice un dato publicado en preprint arxiv).

---

## §2 — Política oficial de arxiv (resumida)

Según las [Directrices de arxiv para reemplazo de preprints](https://arxiv.org/help/replace) (consultadas 2026-09-02):

- **Reemplazo (v2, v3, ...):** mantener el mismo arxiv ID. La versión anterior queda visible pero marcada como "superseded by v[N]". Los lectores ven la versión más reciente por defecto.
- **Retractación:** agregar un banner de "withdrawn" al paper. Mantiene el arxiv ID pero el paper se marca como retirado. El autor puede opcionalmente enviar un nuevo paper.
- **Nuevo envío:** si los cambios son tan grandes que el paper es esencialmente nuevo, el autor puede retractar el viejo y enviar uno nuevo con un arxiv ID distinto.

**Reglas arxiv:**
- El reemplazo (v2+) NO requiere aprobación de arxiv; el autor puede hacerlo en cualquier momento.
- La retractación SÍ requiere que el autor envíe un motivo.
- NO se permite cambiar el título principal del paper en un reemplazo menor (sí se puede agregar subtítulo).

---

## §3 — Criterios de decisión: ¿reemplazar o retractar?

### Reemplazar (v2) — cuando:

1. **Corrección de errores tipográficos o fatties menores** (e.g., numeración de figuras, citas faltantes en bibliografía).
2. **Actualización de un dato cuantitativo** (e.g., F1 recalculado, κ actualizado, tabla con nuevas filas).
3. **Adición de análisis de robustez** (e.g., nueva subsección "Análisis de sensibilidad" en Cap. 5).
4. **Respuesta a observaciones menores del comité** (3–15 ítems tipo B).
5. **Inclusión de un anexo adicional** sin modificar el cuerpo del paper.
6. **Actualización de la lista de agradecimientos** (e.g., agregar advisor formal post-defensa).

### Retractar y reenviar — cuando:

1. **Cambio de hipótesis central** (e.g., se refuta H1 con datos nuevos).
2. **Cambio de metodología principal** (e.g., se reemplaza Florence-2 por otro modelo como contribución central).
3. **Cambio de alcance** (e.g., el paper se expande de Paraguay a Paraguay + Bolivia).
4. **Cambio de contribución principal** (e.g., el paper se reposiciona de "método" a "estudio de caso").
5. **Más del 30% del contenido cambia** sustantivamente.

### Decisión por defecto

**Para el 90% de las situaciones que el comité puede generar, la respuesta es REEMPLAZAR (v2, v3, ...).** La retractación es un último recurso y debe estar consensuada con el director de tesis + Iván.

---

## §4 — Protocolo de reemplazo (paso a paso)

### Paso 1 — Preparar la versión revisada (4–8 h)

1. Aplicar los cambios del comité al manuscrito.
2. Actualizar `paper/paper.pdf` con la nueva versión.
3. Mantener un changelog interno (no se publica en arxiv, sirve para referencia del autor):

```
v2 — 2026-XX-XX
  Cambios respecto a v1:
  - Cap. 4 §4.X: actualizado F1 de LLaVA-13B baseline (N observaciones del comité respondidas)
  - Cap. 5 §5.X: nueva subsección "Análisis de robustez"
  - Bibliografía: +5 citas (solicitadas por el comité)
  - Figura 4.X: regenerada a 300 DPI (solicitada por el comité)
  Cambios no sustantivos: 7 correcciones tipográficas, 2 referencias actualizadas
```

### Paso 2 — Generar PDF compatible con arxiv (1 h)

1. Verificar que el PDF cumple con los requisitos de arxiv:
   - Tamaño máximo: 50 MB
   - Formato: PDF/A o PDF estándar (no PDF/X)
   - Fuentes embebidas (no usar fuentes externas en figuras)
   - Resolución de figuras: 150–300 DPI
2. Herramienta: `latexmk` (si compilando LaTeX) o `pandoc` + `wkhtmltopdf` (si desde markdown).
3. Verificar con `arxiv-checker` (herramienta web gratuita en https://arxiv.org/help/format_validation).

### Paso 3 — Actualizar metadata en arxiv (30 min)

Ir a https://arxiv.org/abs/[ID_v1] → "Replace" → cargar PDF nuevo + opcionalmente actualizar:

- **Abstract:** puede actualizarse (registro histórico preservado).
- **Comments field:** agregar "v2: [resumen de cambios principales, máx 200 caracteres]".
- **Journal reference:** agregar si ya hay DOI de revista.
- **DOI:** agregar si hay DOI de Zenodo o revista.
- **Subjects:** NO cambiar.

**Comments field sugerido:**

> "v2: Aclaraciones menores según observaciones del comité FADA-FP-UNA; +5 citas; nueva subsección 5.X (análisis de robustez); F1 LLaVA-13B baseline actualizado."

### Paso 4 — Confirmar y propagar (1 h)

1. Confirmar reemplazo en arxiv (suele ser inmediato, pero a veces hay cola de moderación).
2. Actualizar el README del repositorio GitHub con la referencia a v2.
3. Si hay DOI de Zenodo, republicar nueva versión del DOI con referencia a arxiv v2.
4. Actualizar cualquier cita externa (e.g., blog personal, redes sociales) para que apunte a v2.

### Paso 5 — Notificar (opcional, 30 min)

Si el paper ya fue citado por otros (en otros preprints, en redes sociales, etc.), notificar al editor del journal donde se envió (si aplica) y opcionalmente a los citadores conocidos:

> "Hola, el paper [arxiv ID] fue actualizado a v2 el [fecha]. Los cambios principales son: [resumen]. La conclusión central no cambia. Nuevo enlace: https://arxiv.org/abs/[ID]v2"

---

## §5 — Protocolo de retractación (caso extremo)

Si la situación amerita retractación (ver §3), seguir este protocolo:

### Paso 1 — Confirmar con director + Iván (1 día)

La retractación es una decisión seria. Confirmar con:
- Director de tesis
- Iván (decisor final)
- Co-autores (si aplica)

### Paso 2 — Generar PDF de retractación (2 h)

Crear un PDF breve (1–2 páginas) con:

> # Retraction of [título original]
>
> **Autor(es):** [nombres]
> **Arxiv ID:** [ID original]
> **Fecha:** [fecha]
>
> Por la presente retractamos el paper "[título]" ([arxiv ID]) publicado el [fecha original]. La retractación se debe a [motivo: cambio de hipótesis / cambio de metodología / re-análisis de datos]. El paper ha sido reemplazado por una nueva versión disponible en [nuevo ID o URL].
>
> Agradecemos al comité FADA-FP-UNA por las observaciones que motivaron esta retractación.
>
> Firmas:
> - Iván Weiss Van Der Pol
> - Director de tesis
> - Co-autores (si aplica)

### Paso 3 — Solicitar retractación en arxiv (15 min)

Ir a https://arxiv.org/abs/[ID] → "Withdraw" → cargar PDF de retractación + motivo.

### Paso 4 — Reenviar como nuevo paper (opcional, 4–8 h)

Si el comité / Iván decide reenviar, seguir el flujo normal de envío a arxiv como nuevo paper (con nuevo ID), asegurándose de:

- Citar el paper retractado en la bibliografía.
- Explicar en la introducción las diferencias con la versión retractada.
- Marcar la versión retractada como "predecesora" en metadatos.

---

## §6 — Caso especial: el comité objeta algo que contradice el preprint

Si el comité objeta un dato o conclusión del paper que **ya está en arxiv**, la situación es delicada porque el preprint ya es público. Opciones:

### Opción A — Reemplazar con corrección explícita

1. Generar v2 con el dato corregido.
2. En el campo "Comments" de arxiv, agregar: "v2 corrige el dato de [X] reportado en v1, que era [valor incorrecto]. El valor correcto es [valor correcto] según [análisis posterior]".
3. En el cuerpo del paper, agregar nota al pie en la sección correspondiente: "v1 de este preprint reportó [valor incorrecto]. El valor correcto es [valor correcto] (v2 actualizado el [fecha])".
4. Si el dato afecta una conclusión central, agregar una subsección "Corrección post-revisión" en Cap. 5 ó 6.

**Cuándo usar:** cuando el dato es corregible y la corrección no invalida la contribución central.

### Opción B — Reemplazar con reinterpretación

1. Generar v2 reinterpretando el dato sin necesariamente cambiarlo.
2. Si el comité dice "el F1=0.78 es bajo para Q1/Q2", pero el manuscrito defiende que es "aceptable para corpus regional", reforzar la defensa con literatura comparable.
3. En Cap. 5 §5.5 (discusión), agregar párrafo explícito que contextualice el F1=0.78 frente a literatura comparable (MapBiomas, GeoWiki).

**Cuándo usar:** cuando el dato es defendible pero la defensa actual es débil.

### Opción C — Retractar y reenviar

1. Si el comité objeta algo que es **esencialmente incorrecto** (e.g., error metodológico grave, sesgo no declarado), retractar.
2. Documentar la retractación como ejemplo de rigor metodológico.

**Cuándo usar:** solo en caso extremo (probabilidad <5% para esta tesis).

---

## §7 — Lección aprendida (memoria del proyecto)

**Regla para futuras tesis:** antes de enviar el manuscrito a arxiv, hacer una revisión completa con el director + al menos un revisor externo. Esto reduce la probabilidad de tener que reemplazar el preprint dentro de los 6 meses posteriores al envío.

**Regla para esta tesis:** dado que el preprint se enviará POST-defensa (T099 está bloqueado en T126 defensa), la mayoría de las observaciones del comité se incorporarán ANTES del envío a arxiv. El riesgo R-NEW-29 aplica solo si T099 se ejecuta antes de T124 (lo cual no debería pasar según el cronograma).

**Cronograma esperado:**

1. T124 (revisión del comité) — resuelve observaciones → manuscrito v2.0.
2. T126 (defensa pública) — aprueba manuscrito v2.0.
3. T099 (envío a arxiv) — primera versión del preprint en arxiv.
4. T100 (envío a conferencia) — referenciar arxiv v1.
5. T127 (envío a revista) — referenciar arxiv v1.
6. (Opcional) Si hay revisiones de la revista, generar arxiv v2.

**Implicación:** el caso "comité objeta algo que contradice el preprint" (R-NEW-29) es **cronológicamente imposible** en esta tesis, porque el comité revisa antes de que el preprint exista. Este plan se mantiene como **precaución** por si el flujo se altera (e.g., el director decide enviar a arxiv antes de la defensa).

---

## §8 — Anti-patrones

### Anti-patrón 1 — Retractar por una observación menor

> ❌ "El comité pidió una aclaración sobre F1=0.78, voy a retractar y reenviar."

**Por qué es malo:** retractar es una decisión seria. Para observaciones menores, **siempre reemplazar (v2)**, nunca retractar.

### Anti-patrón 2 — Reemplazar sin actualizar el campo "Comments"

> ❌ "Subí el PDF nuevo a arxiv sin avisar en Comments qué cambió."

**Por qué es malo:** los lectores y citadores no saben que la versión cambió. El campo "Comments" es la única señal pública de qué versión es la "actual".

### Anti-patrón 3 — Cambiar el título en un reemplazo

> ❌ "El comité sugiere cambiar 'Anotación semiautomática' por 'Anotación asistida por IA'. Lo cambio en v2."

**Por qué es malo:** arxiv NO permite cambiar el título principal en un reemplazo menor. Si el cambio de título es importante, **retractar y reenviar** con nuevo título.

### Anti-patrón 4 — Reemplazar más de 3 veces en 12 meses

> ❌ "El comité pide cambios, los aplico, el comité pide más cambios, los aplico, etc. (5 versiones en 6 meses)."

**Por qué es malo:** versiones excesivas generan desconfianza en los lectores. Si después de v3 todavía hay cambios significativos, **retractar y reenviar** como nuevo paper.

---

## §9 — Recursos

- **arxiv replacement policy:** https://arxiv.org/help/replace
- **arxiv format checker:** https://arxiv.org/help/format_validation
- **Ejemplo de retraction notice bien redactada:** https://arxiv.org/abs/2106.09685 (paper retractado por error en datos, notice clara y útil)
- **Alternativa a arxiv:** Zenodo (permite versionado más flexible, DOI por versión)
