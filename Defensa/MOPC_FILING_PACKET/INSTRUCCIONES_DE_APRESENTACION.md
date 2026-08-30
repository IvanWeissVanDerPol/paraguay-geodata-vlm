# Instrucciones de Apresentación — MOPC Drone Imagery Filing

> **Paquete:** `Defensa/MOPC_FILING_PACKET/`
> **Documentos:** 3 archivos + 1 índice + 1 hoja de impresión
> **Tiempo estimado:** 30-45 minutos (incluyendo impresión y firma)

---

## Paso 1 — Reúne los documentos personales

Antes de tocar el paquete, ten a mano:

- [ ] **Cédula de Identidad Paraguaya** vigente (original + copia anverso/reverso en una hoja A4)
- [ ] **Carnet de estudiante UNA vigente** (opcional pero recomendable)
- [ ] **Constancia de inscripción a la Maestría FADA-UNA período 2026** (solicitar en Secretaría Académica, 24-48 h hábiles)
- [ ] **Aval firmado del director de tesis** (Ing. Juan Carlos Cristaldo) — pedirle que firme el aval del Anexo Técnico (Sección 10.1)

> **Tip:** si la constancia de inscripción no está lista a tiempo, la solicitud puede presentarse igual y adjuntarse la constancia después mediante nota simple (Ley 5282/2014 Art. 6, plazo de 5 días hábiles).

---

## Paso 2 — Completa los placeholders del paquete

Abre cada archivo `.md` con un editor de texto (VSCode, nano, vim) y reemplaza:

| Marcador | Dónde aparece | Ejemplo |
|----------|---------------|---------|
| `[NOMBRE_COMPLETO]` | (ya completo: Iván Weiss Van der Pol) | — |
| `[CEDULA_NRO]` | Carta §saludos + SFP-020 §1 | (su número de CI) |
| `[DOMICILIO_REAL]` | Carta §saludos + SFP-020 §1 | Av. España 1234, Asunción |
| `[DEPARTAMENTO]` | SFP-020 §1 | Central |
| `[LOCALIDAD]` | SFP-020 §1 | Asunción |
| `[TELEFONO_FIJO]` | SFP-020 §1 | (021) 123-456 |
| `[TELEFONO_CONTACTO]` | Carta + SFP-020 §1 | +595 981 123 456 |
| `[EMAIL_CONTACTO]` | Carta + SFP-020 §1 | ivan.weiss@una.py |
| `[EMAIL DIRECTOR — completar]` | Anexo §9 | (email del Ing. Cristaldo) |
| `[MATRICULA_UNA]` | SFP-020 §1 | (número de matrícula) |
| `[FECHA_NACIMIENTO]` | SFP-020 §1 | 01/01/1990 |
| `[ESTADO_CIVIL]` | SFP-020 §1 | Soltero |
| `[LUGAR_FECHA]` | Carta + SFP-020 + Anexo | Asunción, 30 de agosto de 2026 |
| `[FIRMA_OLOGRAFA]` | Carta + SFP-020 | (no firmar digitalmente — firmar a mano en la impresión) |
| `[NÚMERO DE EXPEDIENTE — completar en ventanilla]` | Carta §Ref | (lo asigna el MOPC en ventanilla) |

**Total:** 14 placeholders. Tiempo: ~10 minutos.

> **Verificación crítica:** la fecha de firma `[LUGAR_FECHA]` debe ser igual o anterior a la fecha de presentación en el MOPC (no firmar con fecha futura). Si firmas el 28/08 y presentas el 02/09 está OK; si firmas el 28/08 y presentas el 15/08 NO está OK.

---

## Paso 3 — Genera el PDF consolidado

Una vez completados los placeholders, ejecuta el comando incluido en `IMPRIMIR_TODO.md` (último archivo del paquete). Ejemplo con `pandoc`:

```bash
cd /opt/data/thesis-active/Defensa/MOPC_FILING_PACKET/
pandoc \
  --pdf-engine=xelatex \
  -V geometry:margin=2.5cm \
  -V fontsize=11pt \
  -V mainfont="DejaVu Sans" \
  -V lang=es \
  -o MOPC_SOLICITUD_2026.pdf \
  MOPC_CARTA_DE_SALIDA.md \
  SFP_020_FORMULARIO.md \
  ANEXO_TECNICO.md
```

**Resultado:** un PDF de ~14 páginas (A4, 11pt, interlineado 1.5).

> **Si no tienes pandoc/xelatex instalado:**
> - macOS: `brew install pandoc && brew install --cask mactex` (o `brew install --cask basictex`)
> - Ubuntu/Debian: `sudo apt install pandoc texlive-xetex texlive-fonts-recommended`
> - Alternativa online: copiar el markdown a <https://pandoc.org/try/> o usar VSCode + extensión Markdown PDF

---

## Paso 4 — Imprime

- Impresora **láser** preferentemente (mejor calidad en membretes y sellos)
- Papel A4 blanco, 80 g/m²
- **Una copia** del PDF consolidado
- **Una copia extra** del SFP-020 (MOPC retiene una y te devuelve una con sello de recepción)
- **Una copia** de la Cédula de Identidad (anverso + reverso, una hoja)
- **Una copia** de la constancia de inscripción a la Maestría

**Total:** 4-5 hojas A4 + folder plástico transparente tamaño oficio.

---

## Paso 5 — Firma el SFP-020 y la carta a mano

- Imprime el PDF
- **Firma con bolígrafo azul** en:
  1. Carta de salida — sección "Sin otro particular..." (línea sobre tu nombre)
  2. SFP-020 — Sección 8 (firma del solicitante)
- **NO firmes digitalmente** (MOPC no acepta firma digital para SFP-020)

---

## Paso 6 — Presentación en el MOPC

### Ubicación

**Mesa de Entrada Única — Ministerio de Obras Públicas y Comunicaciones**
Av. Mariscal Francisco Solano López N° 3.222
Asunción, Paraguay
Tel: (+595 21) 414-9000
**Horario de atención:** lunes a viernes, 07:00 a 13:00 (verificar en <https://www.mopc.gov.py>)

### Qué decir en ventanilla

> *"Buenos días. Vengo a presentar una solicitud formal de acceso a datos públicos (SFP-020), al amparo de la Ley 5282/2014. Solicito acceso a mosaicado aéreo institucional del MOPC, con fines de investigación de tesis de maestría UNA-FADA."*

El funcionario te indicará qué ventanilla específica (probablemente Mesa de Entrada Única, ventanilla 1-3).

### Documentos a entregar

1. Carta de Salida firmada (1 hoja)
2. SFP-020 firmado (3 páginas)
3. Anexo Técnico firmado por director y Secretaría Académica (6 páginas)
4. Copia de Cédula de Identidad (1 hoja)
5. Constancia de inscripción a la Maestría (1 hoja, si está disponible)

### Qué recibirás del MOPC

- **Constancia de recepción** con:
  - N° de Expediente
  - Fecha y hora de recepción
  - Sello de Mesa de Entrada
  - Firma del funcionario receptor

> ⚠️ **Guarda la Constancia de Recepción.** Es la prueba del plazo legal de 15 días hábiles (Ley 5282/2014 Art. 17). Si el MOPC no responde en plazo, podés activar el recurso de amparo administrativo ante la SENAC (Secretaría Nacional Anticorrupción) o la vía judicial (Art. 27).

---

## Paso 7 — Seguimiento

### Días 1-15 hábiles después de la presentación

- **No hacer nada.** El MOPC tiene 15 días hábiles para responder (Art. 17 Ley 5282/2014).
- Si a los 5 días hábiles querés confirmar que el expediente está en curso, podés llamar al (+595 21) 414-9000 con tu N° de Expediente.

### Si el MOPC aprueba (escenario esperado)

- Te contactarán por el medio que indicaste en el SFP-020 (preferentemente email).
- Coordinarán la entrega (probablemente SFTP desde el servidor del MOPC o HDD externo).
- Firmarás un **Convenio de Uso de Datos** específico que puede incluir condiciones adicionales del MOPC.

### Si el MOPC deniega o silencia (escenario adverso)

- **Ley 5282/2014 Art. 18:** la denegación debe ser **fundamentada** y por escrito.
- Si la denegación es por causales del Art. 5 (información reservada), podés apelar ante el **Comité de Acceso a la Información Pública** (Ley 5282/2014 Art. 25).
- Si el MOPC no responde en 15 días hábiles, se configura **silencio positivo** (Art. 17 in fine) y se entiende por aprobada la solicitud. Conservá la Constancia de Recepción como prueba.

### Si querés escalar amistosamente

- Pedí una entrevista con el **Director General del Servicio Geográfico Militar** (es礼貌 y suele acelerar el proceso). Mencioná que la UNA-FADA puede firmar un convenio marco de cooperación interinstitucional si la primera entrega sale bien.
- Alternativa: contactá a la **Procuraduría de la UNA** (procurador@una.py) para que oficie de intermediaria institucional.

---

## Paso 8 — Archiva el paquete

Una vez presentado, archivá digitalmente:

- **Copia escaneada del SFP-020 firmada por el MOPC** → `Defensa/MOPC_FILING_PACKET/recibido/[N_EXPEDIENTE]_sfp020_firmado.pdf`
- **Copia escaneada de la Constancia de Recepción** → mismo directorio
- **Nota en PROGRESS.md** del proyecto (no en este paquete) con el N° de Expediente y la fecha de presentación, para referencia futura.

---

## Resumen rápido

| Paso | Qué | Tiempo |
|------|-----|--------|
| 1 | Reunir documentos personales | 5 min (si todo está listo) |
| 2 | Completar placeholders del paquete | 10 min |
| 3 | Generar PDF con pandoc | 2 min |
| 4 | Imprimir | 5 min |
| 5 | Firmar a mano | 2 min |
| 6 | Presentación en ventanilla MOPC | 15 min (incluyendo espera) |
| 7 | Seguimiento | pasivo durante 15 días hábiles |
| 8 | Archivar | 5 min |
| **TOTAL activo** | — | **~45 minutos** |

---

*Documento generado por Erebus (agente autónomo de Iván) bajo licencia MIT.*