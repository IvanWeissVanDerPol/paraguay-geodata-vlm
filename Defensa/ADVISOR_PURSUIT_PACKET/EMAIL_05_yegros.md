# EMAIL 05 — César Yegros (FP-UNA, biomedical engineering) — CONDITIONAL

**Para:** Prof. César Yegros
**Facultad:** Facultad Politécnica, Universidad Nacional de Asunción (FP-UNA), Departamento de Ingeniería Biomédica
**Email:** `[PLACEHOLDER_003_yegros]` (buscar en directorio FP-UNA)
**Probabilidad de aceptación:** BAJA-MEDIA (componente voz NO está en el paper actual; este email es conditional)
**Cuándo enviar:** quinto, SOLO si Iván decide extender el paper con componente de voz (STT/TTS en jopara). Si NO hay extensión de voz planeada, NO enviar.

---

## Asunto sugerido

```
Tesis FP-UNA — interfaz por voz en jopara sobre cartografía, busca director/co-autor (extensión opcional)
```

---

## Cuerpo del email

```
Estimado Prof. Yegros,

Me llamo Iván Weiss Van der Pol y estoy finalizando una tesis de maestría
que combina cartografía paraguaya con interfaz conversacional. Le escribo
porque su trabajo en biomedical engineering + procesamiento de señales
de voz podría ser relevante para una EXTENSIÓN OPTATIVA del trabajo
agregando componente de voz (speech-to-text + text-to-speech en jopara
para la interfaz conversacional).

Estado actual del trabajo (terminado en 100%):

  - Paper: "[PLACEHOLDER_018]" (versión base, sin voz)
    → https://arxiv.org/abs/[PLACEHOLDER_006]

  - Interfaz conversacional actual: solo texto (escrito en pantalla).
    Funciona en español paraguayo + jopara.

Extensión propuesta (NO implementada aún, scope abierto):

  - Componente STT: wav2vec 2.0 XLSR-53 fine-tune sobre audio jopara
    (~50 horas de audio etiquetado, pendiente de采集 con comunidades).
  - Componente TTS: VITS o Tacotron 2 fine-tune sobre voces jopara.
  - Validación: 50 hablantes nativos evalúan usabilidad + intelligibility
    en contexto territorial (preguntas tipo "¿dónde queda el
    arroyo Ka'i?" o "¿cuál es el territorio de la comunidad X?").

Por qué su perfil encaja (si la extensión procede):

  - Expertise en procesamiento de señales biomédicas (audio, voz).
  - Acceso potencial a infraestructura de采集 de audio en comunidades
    indígenas (si tiene convenio con INDI o con la FP-UNA Lab. Señales).
  - Su línea de biomedical engineering aplicada a lenguas de baja
    recursos en Paraguay sería una de las pocas referencias.

Lo que le pido:

  - Co-director (no director principal) en FP-UNA, focused en la
    extensión de voz.
  - Co-autor en una SEGUNDA publicación (paper derivado) sobre la
    interfaz de voz — NO en el paper base.

Lo que le ofrezco:

  - Co-firma sobre un paper derivado en biomedical engineering +
  NLP.
  - La posibilidad de aplicar su metodología de采集 de audio a
    comunidades que ya están en el corpus del paper base.

Importante: este email es CONDITIONAL a que Iván decida ejecutar la
extensión de voz. Si decide que NO va a extender (porque el scope ya
está cerrado), este email NO se envía. Ver `ADVISOR_SHORTLIST_TABLE.md`
§"Política de envío" — Yegros y Pane son los únicos advisors
opcionales en la lista corta.

¿Le interesaría explorar esta extensión? Si me confirma interés, podemos
agendar 30 minutos para discutir el scope, los recursos necesarios y
los posibles convenios institucionales.

Cordialmente,

Iván Weiss Van der Pol
ORCID: [PLACEHOLDER_010]
Tel: [PLACEHOLDER_011]
```

---

## Notas para Iván antes de enviar

1. **DECISIÓN REQUERIDA antes de enviar:** ¿vas a extender el paper con componente de voz? Si NO, este email queda en el paquete sin enviarse.

2. **Recursos necesarios para la extensión:** ~50h audio etiquetado, GPU para fine-tune, convenio con comunidad indígena para采集. Esto es ~3-6 meses de trabajo adicional.

3. **Si decides SÍ enviar:** llenar placeholders + personalizar el párrafo "Por qué su perfil encaja" con 1-2 papers REALES de Yegros.

4. **Si decides NO enviar:** dejar el archivo en el paquete como referencia futura. Si en 2 años decides extender con voz, ya tienes el draft listo.

5. **Timing:** enviar después de Cristaldo + Legal Ayala + Von Lücken + Stalder decline (84 días desde el primer email = ~12 semanas).

---

## Follow-up plan (si decides enviar)

- Day 3: nada.
- Day 7: follow-up corto.
- Day 14: segundo follow-up.
- Day 21: si no responde, pivotear a advisor #6 (Pane).

---

## Cross-refs

- `ADVISOR_SHORTLIST_TABLE.md` — Yegros es advisor #5, prioridad BAJA-MEDIA, **conditional**
- `EMAIL_01..04_*` — enviar ANTES de este (si decides enviar)
- `EMAIL_06_pane.md` — backup si Yegros no responde (también conditional)
- `Capitulos/PAPER_OUTLINE.md` — ver si hay sección预留 para voz
