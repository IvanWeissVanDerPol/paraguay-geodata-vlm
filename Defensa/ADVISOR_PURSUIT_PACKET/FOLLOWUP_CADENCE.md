# FOLLOW-UP CADENCE — Day 3 / Day 7 / Day 14 / Day 30 + pivot timing

**Aplicar a:** cada advisor después de enviar el email inicial.
**Trigger:** el día se cuenta desde la fecha de envío del email inicial (anotar en `Defensa/qa_log.md`).

---

## Filosofía

El advisor recibe un email de un maestrando que le pide co-firma sobre trabajo terminado. La respuesta típica es una de:

1. **Respuesta positiva en ≤7 días:** quiere revisar el paper + agendar llamada. → Ir a `SUCCESS_HANDOFF_PACKET.md`.
2. **Respuesta neutral en 7-14 días:** "interesante, déjame ver, te respondo en X semanas". → No hacer follow-up todavía. Esperar.
3. **Sin respuesta en 14 días:** el email probablemente no fue leído o fue priorizado abajo. → Follow-up Day 14 (recordatorio corto).
4. **Declinación en cualquier momento:** "no es mi línea" / "estoy overloaded" / "no acepto nuevos tesistas". → Ir a `DECLINE_PIVOT_PLAN.md` (siguiente advisor).
5. **Sin respuesta después de Day 30:** declinación implícita. → Pivotear al siguiente advisor.

**NO ser pesado.** Un follow-up es recordatorio; dos follow-ups son insistencia; tres follow-ups son spam. La cadencia abajo es UN recordatorio (Day 14) + UN segundo recordatorio (Day 30 si es necesario) = máximo 2 follow-ups por advisor.

---

## Day 3 — Espera silenciosa

**Acción:** NINGUNA.

**Por qué:** dar tiempo a que el advisor lea el email + piense + responda. La mayoría de advisors académicos leen email 1-2 veces por semana, no diariamente. Si Iván envía un follow-up en Day 3, parece ansioso.

**Si Iván quiere hacer algo útil en Day 3:** verificar que el paper sigue en arxiv (URL funciona), preparar el PDF del manuscrito UNA por si el advisor lo pide, identificar 2-3 horarios disponibles para videollamada.

---

## Day 7 — Micro-follow-up (opcional)

**Acción SOLO si NO hubo respuesta en Day 3-6.**

**Plantilla (≤4 líneas):**

```
Estimado Prof. [PLACEHOLDER_002] [PLACEHOLDER_001],

Le escribo brevemente para confirmar que mi email anterior (enviado
el [FECHA]) llegó bien y reiterar mi interés en explorar la
posibilidad de co-firma sobre el trabajo terminado.

Si tiene 30 minutos esta semana o la próxima, puedo enviarle los
PDFs (paper + manuscrito) y agendar una videollamada en el horario
que mejor le quede.

Cordialmente,
Iván Weiss Van der Pol
```

**Notas:**
- NO adjuntar archivos otra vez — el email original ya tiene todas las URLs.
- NO reiterar todo el contenido del email original — es ruidoso.
- Ofrecer flexibilidad de horario.

**Si el advisor responde "ahora no, pero escríbeme en X semanas":** agendar el próximo follow-up para Day X+1. Anotar en qa_log.md.

---

## Day 14 — Follow-up formal (si NO hubo respuesta)

**Acción SOLO si NO hubo respuesta en Day 3-13.**

**Plantilla (≤6 líneas):**

```
Estimado Prof. [PLACEHOLDER_002] [PLACEHOLDER_001],

Le escribo para hacer un seguimiento de mi email del [FECHA EMAIL
INICIAL]. Entiendo que su inbox es exigente y que mi propuesta
puede no haber encajado en su radar.

Le comparto un resumen ejecutivo de 30 segundos:

  - Paper terminado y publicado en arxiv (DOI: [PLACEHOLDER_006])
  - Dataset abierto + modelo fine-tuned + código reproducible
  - 4-6 páginas de sección específica donde su expertise es
    directamente relevante: [SECCIÓN DEL PAPER]
  - Co-autoría ofrecida en versión final del paper

Si en este momento NO es buen momento para revisar el manuscrito,
le agradezco de antemano una respuesta breve (incluso un "ahora
no" me ayuda a reorganizar mi cronograma).

Si la dirección de email ya no es la correcta, le agradezco me
sugiera la dirección actualizada o el nombre de un colega que
pueda estar interesado.

Cordialmente,
Iván Weiss Van der Pol
```

**Notas:**
- Este es el último follow-up "amable" antes del pivot.
- Ofrecer la opción "ahora no" como salida digna — muchos advisors agradecen esta opción.
- Si el email bounced (dirección incorrecta), usar este follow-up para pedir dirección actualizada.

**Si el advisor responde en Day 14-20:** tratar como respuesta normal (ir a SUCCESS_HANDOFF_PACKET.md o DECLINE_PIVOT_PLAN.md según el contenido).

---

## Day 21 — Decisión de pivote

**Acción:** evaluar respuesta. Si NO hubo respuesta en Day 3-20, decidir.

**Opciones:**

A. **Pivotar al siguiente advisor** (ver `DECLINE_PIVOT_PLAN.md`).
   - Para advisors #1-4: pivotar.
   - Para advisor #5 (Yegros) y #6 (Pane): solo si la extensión/pivote fue aprobada.

B. **Un segundo follow-up "de cierre"** (opcional, solo si Iván tiene razón fuerte para creer que el advisor está overloaded pero interesado). Plantilla:

   ```
   Estimado Prof. [PLACEHOLDER_002],

   Entiendo que el timing no es el adecuado. Le escribo una última vez
   para preguntar: ¿le gustaría que le envíe un recordatorio en
   [FECHA FUTURA, ej. 3 meses] cuando [EVENTO, ej. inicio del semestre
   2027]? Si no recibo respuesta, asumiré que mi propuesta no encaja
   y no enviaré más emails.

   Cordialmente,
   Iván
   ```

   - SOLO si Iván tiene razón fuerte (ej. el advisor le dijo en persona "escríbeme en marzo").
   - Para el 90% de los casos, NO enviar este segundo follow-up; pivotar directamente.

C. **Mover el advisor a lista de "re-contactar en X meses"** (anotar en `Defensa/qa_log.md`).
   - Útil si el advisor está en sabático, de licencia, o tiene un deadline conocido.

---

## Day 30 — Cierre definitivo

**Acción:** marcar al advisor como `declined_implicit` en `qa_log.md` y mover al siguiente.

**Plantilla (opcional, NO obligatoria — Iván puede simplemente dejar de escribir):**

```
Estimado Prof. [PLACEHOLDER_002],

Cierro esta conversación sin haber recibido respuesta. Le agradezco
su tiempo y le deseo lo mejor en sus proyectos.

Si en el futuro el tema le interesa (o conoce a un colega que
pudiera interesarse), mi correo está abierto.

Cordialmente,
Iván Weiss Van der Pol
```

**Por qué es opcional:** muchos advisors prefieren NO recibir un email de cierre (asumen que el silencio fue entendido). Pero para advisors con los que Iván tiene relación previa, enviar este cierre es cortés.

---

## Cadencia visual

```
Day 0   → Email inicial (EMAIL_0X_*.md)
Day 3   → (silencio)
Day 7   → Micro-follow-up opcional
Day 14  → Follow-up formal (si no hubo respuesta antes)
Day 21  → Decisión: pivotar / re-contactar / cerrar
Day 30  → Cierre definitivo (opcional)
```

**Total por advisor:** 21-30 días (3-4 semanas) antes de mover al siguiente.
**Total por los 6 advisors:** 126-180 días (18-26 semanas) si todos decline.
**Si 1 advisor acepta:** la fase termina (4-21 días desde el primer email).

---

## Anotación en qa_log.md

Por cada advisor contactado, crear una entrada en `Defensa/qa_log.md`:

```markdown
## Advisor #N — [NOMBRE] — [FECHA EMAIL INICIAL]

- Email enviado: [YYYY-MM-DD HH:MM PYT]
- Day 7 follow-up enviado: [YYYY-MM-DD] (o "no enviado porque respondió antes")
- Day 14 follow-up enviado: [YYYY-MM-DD]
- Day 30 cierre enviado: [YYYY-MM-DD] (o "no enviado")
- Respuesta recibida: [YYYY-MM-DD] (o "ninguna")
- Verdict: [accepted / declined / declined_implicit / pending]
- Próximo paso: [iniciar SUCCESS_HANDOFF / pivotear a advisor #N+1 / re-contactar en X meses]
- Notas: [cualquier detalle relevante, ej. "el advisor pidió ver el paper primero antes de comprometerse"]
```

Esta bitácora permite a Erebus (en futuras sesiones) ver el estado de la fase sin tener que revisar el correo de Iván.

---

## Cross-refs

- `EMAIL_01..06_*.md` — emails iniciales
- `SUCCESS_HANDOFF_PACKET.md` — si el advisor acepta
- `DECLINE_PIVOT_PLAN.md` — si el advisor decline
- `Defensa/qa_log.md` — bitácora de la fase
