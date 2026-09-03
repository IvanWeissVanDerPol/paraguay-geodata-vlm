# CHECKLIST ANTES DE ENVIAR — 50 ítems / 6 gates

**Aplicar a:** cada advisor antes de enviar el email inicial (EMAIL_0X_*.md).

**Bloqueante vs NO bloqueante:**
- **🔴 BLOQUEANTE** = si está rojo, NO enviar el email. Resolver primero.
- **🟡 RECOMENDABLE** = si está amarillo,理想 resolver antes, pero se puede enviar si no hay tiempo.
- **🟢 OK** = confirmado, listo para enviar.

---

## Gate A — Autoría y datos personales (6 ítems)

- [ ] 🔴 **A1.** Nombre legal completo de Iván confirmado: "Iván Weiss Van der Pol"
- [ ] 🔴 **A2.** Cédula paraguaya de Iván disponible (si Cristaldo la pide para MOPC packet): `[PLACEHOLDER_012]`
- [ ] 🔴 **A3.** ORCID de Iván registrado y público: `[PLACEHOLDER_010]`
- [ ] 🔴 **A4.** Teléfono de Iván disponible para el pie del email: `[PLACEHOLDER_011]`
- [ ] 🟡 **A5.** Email "profesional" usado para enviar (NO email personal con apodos): ej. `iweiss@una.py` o `iweissv@fpuna.edu.py`
- [ ] 🟢 **A6.** Firma de email con todos los datos correcta (nombre, ORCID, tel)

---

## Gate B — Materiales del trabajo (12 ítems)

- [ ] 🔴 **B1.** Paper en arxiv con DOI asignado y URL pública
- [ ] 🔴 **B2.** URL arxiv en el email coincide con la URL real (verificar 2 veces — copy-paste errors son comunes)
- [ ] 🔴 **B3.** Dataset en Hugging Face Hub con DOI y URL pública
- [ ] 🔴 **B4.** URL HF dataset en el email coincide con la URL real
- [ ] 🔴 **B5.** Modelo fine-tuned en Hugging Face Hub con URL pública
- [ ] 🔴 **B6.** URL HF modelo en el email coincide con la URL real
- [ ] 🔴 **B7.** Código en GitHub con LICENSE + README + tests + URL pública
- [ ] 🔴 **B8.** URL GH repo en el email coincide con la URL real
- [ ] 🟡 **B9.** Manuscrito UNA en PDF (~3 MB) listo para adjuntar si el advisor pide
- [ ] 🟡 **B10.** Slides de defensa (Defensa/slides.html) exportados a PDF por si el advisor pide
- [ ] 🟡 **B11.** Packet FADA TFG (Capitulos/FADA_TFG_SUBMISSION_PACKET.md) listo para enviar al comité cuando se requiera
- [ ] 🟢 **B12.** LICENSE del código es OSI-approved (MIT o Apache 2.0)

---

## Gate C — Email en sí (7 ítems)

- [ ] 🔴 **C1.** Nombre del advisor escrito correctamente (doble verificación): `[PLACEHOLDER_001]`
- [ ] 🔴 **C2.** Título académico correcto: `[PLACEHOLDER_002]` (Dr./Mg./Ing./Prof.)
- [ ] 🔴 **C3.** Email del advisor verificado en directorio oficial (FP-UNA / FADA / Google Scholar)
- [ ] 🔴 **C4.** Asunto del email no es spam-trigger (evitar: "URGENTE", "OPORTUNIDAD ÚNICA", "$", todo mayúsculas)
- [ ] 🔴 **C5.** Saludo es formal ("Estimado Prof. [Apellido]") y NO informal ("Hola", "Hey", "Buenas")
- [ ] 🟡 **C6.** Hook específico al advisor es relevante (verificar que el paper del advisor citado en `[PLACEHOLDER_004]` es REAL y reciente)
- [ ] 🟢 **C7.** Email NO contiene datos personales hardcoded del advisor (cédula, teléfono personal) — solo `[PLACEHOLDER_NNN]` + email institucional

---

## Gate D — Co-autoría y alcance (5 ítems)

- [ ] 🔴 **D1.** Tipo de co-firma明确 (director / co-director / co-autor) y consistente con el email
- [ ] 🔴 **D2.** Sección del paper donde el advisor es co-autor está claramente identificada
- [ ] 🟡 **D3.** Orden de autores (Iván primero / advisor primero / joint) es coherente con la facultad del advisor (FADA permite cualquier orden; FP-UNA Ing. Informática tiene normativa específica)
- [ ] 🟡 **D4.** Co-autoría en versión final del paper (post-defensa) implica que el manuscrito actual sigue siendo single-author — esto está claro en el email
- [ ] 🟢 **D5.** Si el advisor es externo (no FADA-FP-UNA), verificar convenio vigente (Gate F5 abajo)

---

## Gate E — Ético y compliance (5 ítems)

- [ ] 🔴 **E1.** Email NO ofrece pago al advisor (ilegal en UNA-FADA + rompe la relación)
- [ ] 🔴 **E2.** Email NO pide al advisor que firme algo sin leerlo (fraude académico)
- [ ] 🔴 **E3.** Co-autoría es por contribución real (no honorary authorship)
- [ ] 🟡 **E4.** Si el corpus incluye territorios indígenas, verificar que el paper respeta FPIC (Free, Prior and Informed Consent) de la ONU — esto YA está hecho en ETHICS_WAIVER_MEMO.md
- [ ] 🟢 **E5.** Email NO contiene lenguaje discriminatorio, sexista, o excluyente

---

## Gate F — Logística (15 ítems)

### F.1 — Timing
- [ ] 🔴 **F1.** Día de la semana apropiado (martes a jueves, NO lunes ni viernes)
- [ ] 🔴 **F2.** Hora del día apropiada (9-11 AM PYT — advisor lee email con café)
- [ ] 🟡 **F3.** NO enviar en semana de exámenes o recesos en FADA-FP-UNA
- [ ] 🟡 **F4.** NO enviar justo después de un holiday largo (el advisor vuelve overloaded)

### F.2 — Concurrencia
- [ ] 🔴 **F5.** NO se envió email al advisor #2 antes de que #1 decline (R-NEW-18: advisor #2 queda mal)
- [ ] 🟡 **F6.** NO se está enviando el mismo email a varios advisors en paralelo (CC oculto o BCC accidental)

### F.3 — Advisor externo (solo si aplica)
- [ ] 🔴 **F7.** Si el advisor NO está en FADA-FP-UNA: verificar convenio vigente entre su universidad y FADA-UNA / FP-UNA (consultar con Secretaría Académica FADA antes de enviar)
- [ ] 🟡 **F8.** Si es advisor externo: agregar al email el contexto del convenio (ej. "adjunto carta de aval de Secretaría Académica FADA confirmando el convenio inter-institucional")

### F.4 — Documentación
- [ ] 🔴 **F9.** Anotar fecha/hora de envío en `Defensa/qa_log.md` inmediatamente después de enviar
- [ ] 🔴 **F10.** NO enviar emails con datos personales hardcoded (cédula, teléfono) sin encriptar (usar `[PLACEHOLDER_NNN]` o enviar como attachment con password)
- [ ] 🟡 **F11.** Backup de los emails enviados (el cliente de correo tiene "Sent" folder, pero Iván debería tener backup local también)
- [ ] 🟢 **F12.** NO enviar emails con archivos adjuntos >10 MB (usar link de servicio de compartición de archivos en su lugar)

### F.5 — Post-envío
- [ ] 🟡 **F13.** Iván tiene 2-3 horarios disponibles para videollamada predefinidos (anotar en `[PLACEHOLDER_015]`)
- [ ] 🟡 **F14.** Iván tiene PDF del manuscrito listo para enviar como follow-up si el advisor lo pide
- [ ] 🟢 **F15.** Iván tiene copia de `Capitulos/FADA_TFG_SUBMISSION_PACKET.md` lista para enviar al comité cuando se forme

---

## Resumen de bloqueantes

**🔴 TOTAL BLOQUEANTES:** 22 ítems
- Gate A: 4 (A1, A2, A3, A4)
- Gate B: 8 (B1-B8)
- Gate C: 5 (C1-C5)
- Gate D: 2 (D1, D2)
- Gate E: 3 (E1, E2, E3)
- Gate F: 4 (F1, F2, F5, F7, F9, F10) — *notar que algunos están en sub-gates*

**🟡 TOTAL RECOMENDABLES:** 17 ítems
**🟢 TOTAL OK:** 11 ítems

**Si los 22 bloqueantes están ✅:** el email está listo para enviar.
**Si algún bloqueante está ❌:** resolver antes de enviar (10-30 min dependiendo del ítem).

---

## Tiempo estimado para pasar el checklist completo

| Gate | Tiempo |
|---|---|
| A — Autoría | 5 min (verificar datos) |
| B — Materiales | 0 min (todo debería estar listo) |
| C — Email | 10 min (verificar placeholders + email del advisor) |
| D — Co-autoría | 5 min (confirmar alcance) |
| E — Ético | 2 min (re-lectura rápida) |
| F — Logística | 10 min (timing + anotación) |
| **TOTAL** | **~30 min por advisor** |

**Para los 6 advisors:** ~3 horas totales. Una sola sesión de trabajo.

---

## Cross-refs

- `EMAIL_01..06_*.md` — los emails a verificar
- `ADVISOR_SHORTLIST_TABLE.md` — orden de envío
- `FOLLOWUP_CADENCE.md` — qué hacer después de enviar
- `SUCCESS_HANDOFF_PACKET.md` — si el advisor acepta
- `DECLINE_PIVOT_PLAN.md` — si el advisor decline
- `Defensa/qa_log.md` — bitácora (anotar fecha/hora post-envío)
- `Capitulos/FADA_TFG_SUBMISSION_PACKET.md` — packet paralelo
- `Capitulos/FADA_TFG_SUBMISSION_PACKET.md` §8 — checklist de 9 puntos (similar pero para FADA)
