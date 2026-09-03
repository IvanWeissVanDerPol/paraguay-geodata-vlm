# SUCCESS HANDOFF PACKET — qué enviar al advisor cuando ACEPTA

**Trigger:** cuando un advisor responde "sí, me interesa" / "acepto co-firma" / "agendemos llamada".

**Timing:** enviar dentro de las 48 horas posteriores a la respuesta positiva del advisor. La velocidad aquí importa — el advisor está caliente, y cada día que pasa sin handoff formal baja la probabilidad de que mantenga el compromiso.

---

## Filosofía del handoff

Cuando un advisor acepta, Iván debe:

1. **Confirmar el alcance** de la co-firma (director / co-director, paper section, etc.).
2. **Enviar los materiales completos** (paper + manuscrito + slides + packet FADA).
3. **Proponer un cronograma** de los próximos pasos (inscripción, defensa, etc.).
4. **Resolver logística** (acceso a email del comité, calendario de reuniones).
5. **Documentar el acuerdo** (aunque sea por email, no formal legal — FADA se encarga del formal).

**NO es un contrato legal.** Es un email de "manos a la obra" con todos los detalles para que el advisor tenga el contexto completo sin tener que pedirlo.

---

## Plantilla del email de handoff

```
Estimado Prof. [PLACEHOLDER_002] [PLACEHOLDER_001],

¡Excelentes noticias! Le agradezco profundamente la confianza y el
compromiso con el trabajo.

Adjunto en este email (o enlazo en el cuerpo) todo el material
relevante para que tenga el contexto completo:

  1. PAPER ARXIV:
     - Título: "[PLACEHOLDER_018]"
     - URL: https://arxiv.org/abs/[PLACEHOLDER_006]
     - DOI: [PLACEHOLDER_doi_paper]

  2. MANUSCRITO UNA:
     - 6 capítulos en formato UNA-FADA, ~26K palabras
     - Adjunto: manuscrito_completo_UNA.pdf (~3 MB)

  3. SLIDES DE DEFENSA:
     - Defensa/slides.html (Reveal.js, 21 secciones, exportable a PDF)
     - URL: file:///Defensa/slides.html (en el repo)

  4. DATASET + MODELO + CÓDIGO:
     - Dataset: https://huggingface.co/datasets/[PLACEHOLDER_007]
     - Modelo: https://huggingface.co/[PLACEHOLDER_008]
     - Código: https://github.com/[PLACEHOLDER_009]

  5. PACKET FADA TFG:
     - Capitulos/FADA_TFG_SUBMISSION_PACKET.md (~14.5 KB)
     - Cubre: cover letter, abstract, hipótesis, cronograma,
       factibilidad ética, arquitectura, checklist pre-imprimir.

Sobre el alcance de la co-firma, confirmemos por escrito:

  □ Director de tesis (formal) en [FADA / FP-UNA] Maestría en
    [Tecnología de la Arquitectura / Ing. Informática].
  □ Co-director de tesis (formal).
  □ Co-autor en versión final del paper (post-defensa) como
    [primer co-autor / segundo co-autor / acknowledgments].
  □ Co-autor en secciones específicas: [Sección X / Sección Y].

Si alguno de estos puntos requiere ajuste (ej. su facultad tiene
normativa específica sobre co-autoría), le agradezco me lo
comunique y adaptamos el plan.

Próximos pasos propuestos (cronograma tentativo):

  Semana 1-2 (post-aceptación):
    - Revisión del manuscrito por su parte
    - Identificación de secciones que requieren modificación
      según normativa FADA / FP-UNA

  Semana 3-4:
    - Incorporación de comentarios del manuscrito
    - Reunión 1: 60 minutos, presencial o videollamada
    - Decisión sobre [PLACEHOLDER_013 — fecha tentativa defensa,
      ej. "primer semestre 2027" o "agosto 2027"]

  Semana 5-8:
    - Inscripción formal en FADA / FP-UNA (yo llevo el packet
      + su firma donde se requiera)
    - Reunión 2: ajuste fino del manuscrito

  Semana 9-12:
    - Defense scheduling con el comité TFG-FADA (yo coordino con
      Secretaría Académica)
    - Slides de defensa ajustados con sus comentarios

  Semana 13-16:
    - Defensa pública (45 min + 15 min Q&A)
    - Decisión sobre publicaciones post-defensa

Si necesita coordinar conmigo en algún paso, mi disponibilidad
es [PLACEHOLDER_015 — horarios disponibles para reunión, ej.
"lunes a viernes 14-18 PYT" o "sábados 9-13 PYT"]. Prefiero
videollamada para las reuniones técnicas (plataforma de
videoconferencia estándar — Iván confirma con el advisor cuál prefiere,
ej. Meet / Zoom / Jitsi según la preferência del advisor)
y presencial para las instancias formales en FADA-FP-UNA.

Si su facultad requiere algún documento específico para la
co-firma (ej. carta de aval, formulario de aceptación de
dirección), le agradezco me lo comunique para incluirlo en el
packet que llevaré a FADA-FP-UNA.

Quedo a la espera de sus comentarios sobre el manuscrito y el
cronograma. Si todo está en orden,我们可以 empezar la revisión
esta misma semana.

Cordialmente,

Iván Weiss Van der Pol
ORCID: [PLACEHOLDER_010]
Tel: [PLACEHOLDER_011]
```

---

## Condiciones negociables vs deal-breakers

**Antes de enviar el handoff, Iván debe definir internamente qué condiciones acepta y cuáles no:**

### Negociables (puede aceptar si el advisor pide)

- Modificar el título del paper (ej. agregar el nombre del advisor).
- Agregar al advisor como primer autor en la versión post-defensa (si FADA lo permite).
- Adelantar o atrasar la fecha de defensa según disponibilidad del comité.
- Cambiar el formato de la defensa (presencial vs videollamada).
- Agregar un capítulo o sección al manuscrito si el advisor lo requiere.
- Cambiar la facultad de inscripción (FADA vs FP-UNA) si el advisor está solo en una.

### Deal-breakers (NO debe aceptar)

- Reescribir Cap. 4 (Resultados) desde cero — el trabajo experimental está terminado.
- Eliminar la sección de la interfaz conversacional (Cap. 5) — es la contribución diferenciadora.
- Cambiar el alcance del paper a algo no relacionado con cartografía paraguaya.
- Retrasar la defensa más de 6 meses del cronograma tentativo.
- Aceptar co-firma de alguien que NO va a leer el manuscrito (es una forma de fraude académico).
- Pagar al advisor por la co-firma (esto es ilegal en UNA-FADA y rompería la relación).

Si el advisor pide algo en la lista de deal-breakers, NEGOCIAR amablemente pero NO aceptar. Si no hay acuerdo, pivotear al siguiente advisor (ir a `DECLINE_PIVOT_PLAN.md`).

---

## Documentación del acuerdo

**Inmediatamente después de enviar el email de handoff, crear una entrada en `Defensa/qa_log.md`:**

```markdown
## ACCEPTANCE — Advisor #[N] [NOMBRE] — [FECHA]

- Aceptación recibida: [YYYY-MM-DD HH:MM PYT]
- Tipo: [director / co-director / ambos]
- Facultad: [FADA / FP-UNA]
- Programa: [Maestría en Tecnología de la Arquitectura / Ing. Informática / otro]
- Co-autoría: [primer co-autor / segundo co-autor / acknowledgments]
- Sección destacada del paper: [Sección X]
- Email de handoff enviado: [YYYY-MM-DD]
- Material enviado: [paper + manuscrito + slides + packet FADA]
- Próxima reunión agendada: [YYYY-MM-DD HH:MM]
- Notas: [cualquier condición especial]
```

**Esta entrada es la evidencia de la co-firma.** Si el advisor se retracta después, Iván tiene documentation para presentar al comité TFG-FADA.

---

## Riesgos del handoff

| ID | Riesgo | Mitigación |
|---|---|---|
| R-NEW-21 | Advisor acepta pero después no responde emails → co-firma fantasma | Establecer cadencia semanal (no daily) de emails durante 4 semanas post-aceptación; si pasan 4 semanas sin respuesta, segunda conversación para confirmar compromiso |
| R-NEW-22 | Advisor pide modificaciones grandes al manuscrito que retrasan la defensa | Definir deal-breakers ANTES de aceptar; tener plan B (siguiente advisor) listo |
| R-NEW-23 | Advisor quiere co-autoría pero su facultad no permite co-firma con externos | Verificar antes de aceptar que el advisor tiene plaza vigente en FADA-FP-UNA (consultar directorio + Secretaría Académica) |
| R-NEW-24 | Advisor pide pago por la co-firma | RECHAZAR inmediatamente — ilegal en UNA-FADA. Si insiste,撤退 y pivotear |
| R-NEW-25 | Advisor co-firma pero el comité TFG-FADA no lo acepta (razones políticas / personales) | Investigar antes de aceptar si el comité tiene objeciones connues sobre el advisor; tener Plan B1 listo |

---

## Cross-refs

- `EMAIL_01..06_*.md` — emails originales que llevaron a la aceptación
- `FOLLOWUP_CADENCE.md` — cadencia usada
- `ADVISOR_SHORTLIST_TABLE.md` — el advisor aceptado (#N)
- `Capitulos/FADA_TFG_SUBMISSION_PACKET.md` — packet FADA que se entrega al comité
- `Defensa/JOURNAL_SUBMISSION_PACKET/` — packet paralelo para publicación post-defensa
- `Defensa/qa_log.md` — bitácora de la aceptación
