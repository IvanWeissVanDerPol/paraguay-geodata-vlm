# RESPONSE FRAMEWORK — Metodología de respuesta en 4 pasos

**Tesis:** Anotación semiautomática del corpus cartográfico abierto de Paraguay con modelos multimodales fundacionales y una interfaz conversacional para la reflexión territorial

**Autor:** Iván Weiss Van der Pol

**Origen:** Split de **T124** `[P0][M10][NO-GPU][D] Thesis committee review + revisions` (estado: `[!]` upstream-bloqueado en acción institucional del comité FADA).

**Fecha del paquete:** 2026-09-02

---

## §1 — Propósito de este marco

Cuando una observación del comité **no está pre-fabricada** en `TOP_25_LIKELY_OBJECTIONS.md`, Iván necesita una metodología reproducible para estructurar la respuesta en minutos (no horas). Este documento presenta el marco **A-C-J-O** (Acknowledge → Cite → Justify → Offer), una variación del método CLEAR adaptado a comités académicos de tesis.

El marco es deliberadamente simple: cada paso tiene una pregunta guía y un formato de salida. Aplicar los 4 pasos en orden garantiza que la respuesta:

- Reconoce explícitamente la observación (no la evade).
- Ancla la respuesta en el manuscrito (no improvisa).
- Justifica la decisión metodológica con datos o literatura (no con opinión).
- Ofrece una acción concreta (no deja la pelota en el tejado del comité).

---

## §2 — Los 4 pasos del marco A-C-J-O

### Paso 1 — **A**cknowledge (Reconocer)

**Pregunta guía:** ¿Qué está pidiendo el comité, exactamente?

**Formato de salida:** 1 frase que parafrasea la observación del comité. Esta frase es la "etiqueta" que el comité leerá primero y recordará.

**Reglas:**

- **Sí, identificado / Atendido / Reconozco** — abrir con afirmación positiva, no con justificación.
- **NO usar:** "Entiendo que...", "Considero que...", "Es posible que..." — todo esto suena evasivo.
- **NO negar la observación** salvo que sea claramente incorrecta (en cuyo caso, también abrir con "Reconozco el punto, pero...").

**Ejemplo bueno:**

> "Sí, identificado: la sección 2.4 no incluye una subsección dedicada a la intersección visión-lenguaje y cartografía."

**Ejemplo malo:**

> "Es una observación interesante que merece consideración..."

---

### Paso 2 — **C**ite (Citar manuscrito o literatura)

**Pregunta guía:** ¿Qué sección/página/tabla/figura del manuscrito o de la literatura es la referencia directa?

**Formato de salida:** 1–3 referencias explícitas con localizador (sección, tabla, figura, página, DOI).

**Reglas:**

- **Anclar TODO a una referencia concreta** — el comité no aceptará respuestas abstractas.
- **Para datos internos del manuscrito:** formato `Cap. X, §Y, Tabla Z` o `Cap. X, Figura Z, p. Y`.
- **Para literatura externa:** formato `(Apellido et al. Año, DOI:10.XXXX/XXXX)`.
- **Si la observación es nueva (no hay referencia en el manuscrito):** citar literatura comparable como analogía (e.g., "Parasuraman & Manzey 2010 sobre sesgo de automatización").

**Ejemplo bueno:**

> "La observación aplica a Cap. 2 §2.4–§2.5, que actualmente cubre los 12 modelos foundation pero subsume la intersección con cartografía. Literatura comparable para la sección nueva: MapBiomas (Souza et al. 2020, DOI:10.XXXX), GeoWiki (Fritz et al. 2017, DOI:10.XXXX), RemoteCLIP (Liu et al. 2024, arXiv:2406.XXXX)."

**Ejemplo malo:**

> "Hay varias referencias relevantes en el área..."

---

### Paso 3 — **J**ustify (Justificar decisión o proponer cambio)

**Pregunta guía:** ¿Por qué el manuscrito tomó esa decisión, o por qué el cambio propuesto es la mejor ruta?

**Formato de salida:** 2–4 párrafos con la justificación técnica/metodológica. Si la observación pide un **cambio**, explicar por qué se acepta + cómo se implementa. Si la observación es **defendible** (la decisión actual es correcta), explicar por qué con datos.

**Reglas:**

- **Para cambios aceptados:** "Propongo [cambio X] porque [razón Y] con [método Z]".
- **Para decisiones defendidas:** "La decisión de [X] se justificó en [lugar] por [razón]. El comité podría cuestionar [alternativa], pero [contraargumento con dato]".
- **Usar datos o literatura, no opinión personal.** "Mi opinión es que..." es señal de respuesta débil.
- **Reconocer trade-offs honestamente.** "El cambio propuesto tiene el costo de X, pero el beneficio de Y justifica la implementación."

**Ejemplo bueno:**

> "La decisión de usar SmolVLM (2B parámetros, Apache-2.0) sobre LLaVA-13B se justificó en Cap. 3 §3.4 por dos criterios: (i) factibilidad on-prem en Paraguay (SmolVLM cabe en 16 GB VRAM con cuantización 4-bit, vs LLaVA-13B que requiere ≥24 GB); (ii) soberanía de datos (LLaVA tiene licencia CC-BY-NC en algunas versiones, SmolVLM es Apache-2.0). El delta de F1 entre ambos modelos es +0.02 a favor de LLaVA-13B (medido en baseline), pero este delta no justifica el costo computacional 6× mayor. Trade-off explícito en Cap. 5 §5.3."

**Ejemplo malo:**

> "Yo creo que la elección fue correcta porque..."

---

### Paso 4 — **O**ffer (Ofrecer acción concreta)

**Pregunta guía:** ¿Qué se compromete Iván a hacer, en qué plazo, y dónde queda documentado?

**Formato de salida:** 1 frase con (i) acción concreta, (ii) plazo estimado, (iii) lugar en el manuscrito o anexo.

**Reglas:**

- **SIEMPRE cerrar con acción concreta.** "Lo voy a considerar" no es una oferta; es una evasión.
- **Plazo en horas-persona**, no en semanas ("4–6 horas" en lugar de "la próxima semana").
- **Localizador específico:** "Cap. X, nueva §Y.Z", no "en el manuscrito".
- **Si no se puede implementar:** "No se puede implementar en este plazo porque [razón]. Alternativa: [propuesta]".

**Ejemplo bueno:**

> "Propongo agregar la subsección 2.5.1 en 4–6 horas (búsqueda de papers 2h, escritura 2–3h, integración 1h) con la tabla 2.X de 12 modelos × 5 dimensiones, anclada a las ~25 citas nuevas de MapBiomas, GeoWiki, GeoLLM, etc."

**Ejemplo malo:**

> "Voy a revisar el tema y mejorar la sección."

---

## §3 — Plantilla completa A-C-J-O

Para aplicar el marco en una observación del comité, copiar y llenar esta plantilla:

```
OBSERVACIÓN #___  |  TIPO: A / B / C  |  CAP: ___  |  FECHA: ___

TEXTO LITERAL DEL COMITÉ:
[pegar aquí la observación textual]

──────────────────────────────────────────────────────────

A — ACKNOWLEDGE:
[1 frase que parafrasea la observación]

C — CITE:
[1-3 referencias con localizador]

J — JUSTIFY:
[2-4 párrafos de justificación con datos/literatura]

O — OFFER:
[acción concreta + plazo + localizador]

──────────────────────────────────────────────────────────

TIEMPO TOTAL ESTIMADO: __ horas
CATEGORÍA RESULTANTE: TIPO A / B / C
PASA A SPRINT: DIA ___
DEPENDENCIAS: [director / GPU / consultor / etc.]
```

---

## §4 — Ejemplo completo: aplicación del marco a una observación no pre-fabricada

**Observación del comité:** *"El manuscrito no discute el impacto ambiental del cómputo utilizado (energía, CO2-eq). En la era del green computing, esto debería ser estándar."*

**Aplicación A-C-J-O:**

**A — ACKNOWLEDGE:**
> "Sí, identificado: el manuscrito actual (Cap. 4 §4.9 notas metodológicas) lista el costo computacional en USD pero no en CO2-eq ni en kWh."

**C — CITE:**
> "La observación aplica a Cap. 4 §4.9. Literatura comparable sobre green computing en ML: Strubell et al. 2019 (DOI:10.1145/306XXXX), Patterson et al. 2021 (arXiv:2104.XXXX), Lacoste et al. 2019 (DOI:10.1145/334XXXX). Estos papers establecen que reportar FLOPs y CO2-eq es práctica estándar en ML reproducible."

**J — JUSTIFY:**
> "El manuscrito ya reporta el costo en USD (USD 14.20 total, ver Cap. 4 §4.9 tabla anexa). La omisión del CO2-eq es una brecha de reproducibilidad, no una decisión metodológica. Calculé el consumo retroactivamente con la herramienta `codecarbon` (versión 0.16.1, https://github.com/mlco2/codecarbon): (i) CPU-only pre-processing: 2h × 60W = 0.12 kWh = 0.05 kg CO2-eq en Paraguay (factor de emisión 0.41 kg CO2/kWh, fuente ANDE 2024); (ii) Embedding CLIP CPU: 4h × 60W = 0.24 kWh = 0.10 kg CO2-eq; (iii) Fine-tune Florence-2 en RTX 3090: 6h × 350W = 2.1 kWh = 0.86 kg CO2-eq (factor Paraguay); (iv) Inferencia: 14h × 60W = 0.84 kWh = 0.34 kg CO2-eq. **Total: 5.2 kg CO2-eq.** Esto es 2–3 órdenes de magnitud menor que el baseline cloud A100 (~250 kg CO2-eq), lo cual valida la decisión de CPU-only para Paraguay. Trade-off: el cómputo CPU tomó ~3× más tiempo que GPU cloud, pero el costo ambiental se redujo ~50×."

**O — OFFER:**
> "Propongo agregar tabla 4.X 'Costos ambientales' (5 filas × 5 columnas: etapa, kWh, CO2-eq, fuente energía, ahorro vs cloud) en 1–2 horas. Localización: Cap. 4 §4.9, después de la tabla de costos USD. Incluir también una mención en el abstract de la sección: 'el cómputo total fue 5.2 kg CO2-eq, 50× menor que el baseline cloud A100'."

**Tiempo total:** 1.5 horas. **Categoría:** B (menor, addition de tabla). **Sprint:** día 5 (después de resolver las OBJ tipo A si las hay).

---

## §5 — Anti-patrones (qué NO hacer)

### Anti-patrón 1 — "Respuesta paja" (strawman response)

> ❌ "Entiendo que el comité podría considerar que..."
> ❌ "Si el comité cree que falta X..."
> ❌ "Quizás sería bueno revisar Y..."

**Por qué es malo:** no afirma nada, evade la observación, hace perder tiempo al comité. Los miembros del tribunal son expertos: detectan inmediatamente una respuesta que no se compromete.

### Anti-patrón 2 — "Defensa numantina" (defend everything)

> ❌ "El manuscrito está correcto. No veo la necesidad de modificar..."
> ❌ "Esa observación es incorrecta porque..."

**Por qué es malo:** incluso si la observación es defendible, una respuesta 100% defensiva aliena al comité. Es mejor aceptar la observación como oportunidad de mejora y matizar dentro de la aceptación.

### Anti-patrón 3 — "Promesa vaga" (vague promise)

> ❌ "Voy a mejorar la sección en el futuro."
> ❌ "Consideraré la observación para una versión futura del manuscrito."

**Por qué es malo:** el comité espera cambios en esta versión, no en una futura. La promesa vaga es funcional a evitar el trabajo.

### Anti-patrón 4 — "Sobrecarga de citas" (citation overload)

> ❌ [20 citas en un párrafo sin contexto]

**Por qué es malo:** el comité no tiene tiempo para verificar 20 citas. Mejor 3–5 citas bien ancladas y explicadas que 20 sin contexto.

### Anti-patrón 5 — "Olvido del director" (director bypass)

> ❌ Responder observaciones de tipo A sin consultar al director primero.

**Por qué es malo:** el director de tesis es el firmante institucional de la respuesta. Si Iván responde por su cuenta decisiones de fondo, está pasando por encima del director, lo cual es una falta grave en el reglamento FADA Art. 27.

**Regla:** observaciones tipo A (revisión mayor) SIEMPRE consultar al director antes de comprometer una respuesta.

---

## §6 — Reglas de oro

1. **No improvisar.** Si la observación no está pre-fabricada, aplicar A-C-J-O sistemáticamente. La improvisación se nota.
2. **Anclar todo.** El comité no aceptará respuestas abstractas. Cada afirmación debe tener un localizador.
3. **Reconocer trade-offs.** Las decisiones metodológicas son trade-offs, no verdades absolutas. Reconocer el trade-off honestamente genera credibilidad.
4. **Plazo en horas, no en semanas.** "4–6 horas" es concreto; "la próxima semana" es evasivo.
5. **Consultar al director para tipo A.** Las decisiones de fondo (re-experimentación, re-análisis, re-escritura de sección) requieren visto bueno del director.
6. **Verificar con `make format-manuscript-check` antes de entregar.** Inconsistencias técnicas (formato APA, figuras, citas) son la forma más rápida de perder credibilidad.
7. **Memo de cambios como primera página.** Lista cada observación + dónde se atendió. Facilita la re-revisión y muestra rigor.
