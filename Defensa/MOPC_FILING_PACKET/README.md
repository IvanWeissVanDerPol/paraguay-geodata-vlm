# MOPC Drone Imagery Filing Packet — T046a

> **Status:** Artefacto impreso listo para revisión y firma de Iván. **NO presentado ante el MOPC.**
> **Origen:** Sub-tarea de T046 (File MOPC drone imagery access request, Ley 5282/2014) — T046 revertida a `[!]` por ser `[EXT]` (presentación institucional requiere Cédula Paraguaya + firma ológrafa). Este paquete es el artefacto autónomo que Iván imprime, firma y entrega.
> **Autor del paquete:** Erebus (agente autónomo de Iván)
> **Fecha:** 2026-08-30
> **Idioma:** Español (idioma oficial de la República del Paraguay, Ley 1350/88)
> **Normativa aplicable:** Ley 5282/2014 (Libre Acceso a la Información Pública) + Decreto 1134/14 + Ley 6538/2020 (datos abiertos)

---

## 📋 Contenido del paquete

| # | Archivo | Páginas | Propósito |
|---|---------|---------|-----------|
| 1 | `MOPC_CARTA_DE_SALIDA.md` | 2 | Carta de presentación formal dirigida al Director General de la Dirección General del Servicio Geográfico Militar / Dirección de Geodesia del MOPC |
| 2 | `SFP_020_FORMULARIO.md` | 3 | Formulario oficial SFP-020 (Solicitud Formal de Datos Públicos) pre-llenado con placeholders para datos personales de Iván |
| 3 | `ANEXO_TECNICO.md` | 6 | Anexo Técnico describiendo: (a) qué datos se solicitan, (b) para qué se usarán, (c) cómo se procesarán, (d) licencia de publicación, (e) cronograma, (f) infraestructura disponible, (g) cumplimiento normativo |
| 4 | `INSTRUCCIONES_DE_APRESENTACION.md` | 2 | Paso a paso para que Iván imprima, complete los placeholders, firme, escanee, presente en ventanilla del MOPC, y archive la constancia |
| 5 | `IMPRIMIR_TODO.md` | 1 | Comando `pandoc` único para generar PDF consolidado de los 4 archivos |

**Total:** 14 páginas (A4, letra 11pt, interlineado 1.5) — cabe en una carpeta plástica tamaño oficio.

---

## 🎯 Por qué este paquete existe

T046 (File MOPC drone imagery access request) es una **acción institucional en persona** que requiere:

1. Cédula Paraguaya vigente de Iván (original + copia)
2. Firma ológrafa del solicitante
3. Presentación en Mesa de Entrada Única del MOPC (Av. Mariscal López 3.222, Asunción)
4. Comprobante de pago de tasa administrativa (cuando aplique — exento para investigación académica según Decreto 1134/14 Art. 14)

Estas acciones no pueden ejecutarse desde el sandbox (regla #5 de AUTONOMY.md: "NO emails to real people"). Lo que el agente **sí puede** hacer es preparar el paquete documental completo para que Iván solo tenga que: (a) completar los placeholders, (b) imprimir, (c) firmar, (d) presentar. Tiempo estimado: 30 minutos vs. 2 horas si Iván redactara desde cero.

---

## 🔒 Datos sensibles (placeholders)

El paquete contiene marcadores `[PLACEHOLDER_NNN]` en 14 puntos. **Iván debe completar antes de imprimir:**

| Marcador | Dato | Ejemplo |
|----------|------|---------|
| `[NOMBRE_COMPLETO]` | Iván Weiss Van der Pol | (su nombre) |
| `[CEDULA_NRO]` | N° de Cédula Paraguaya | (su CI) |
| `[DOMICILIO_REAL]` | Domicilio en Paraguay | (su dirección) |
| `[TELEFONO_CONTACTO]` | +595 9XX XXXXXX | (su número) |
| `[EMAIL_CONTACTO]` | ivan.weiss AT una.py | (su email) |
| `[LUGAR_FECHA]` | Asunción, [día] de [mes] de 2026 | (fecha de firma) |
| `[FIRMA_OLOGRAFA]` | Firma manuscrita | (firma física) |
| `[FECHA_DEFENSA_TENTATIVA]` | 1er semestre 2027 | (ver DEFENSE_PLAN.md) |

**Restricción:** ninguno de estos datos aparece en logs, commits, o PROGRESS.md. Solo se imprimen en el paquete físico.

---

## 📝 Trazabilidad académica

El Anexo Técnico cita explícitamente:

- Tesis de maestría UNA-FADA, director Ing. Juan Carlos Cristaldo
- 4 tesis previas de la línea de cartografía abierta (2019, 2019, 2021, 2023)
- Datos OSM Paraguay, IGN raster, Copernicus Sentinel-2 (ya en `DATA_MANIFEST.md`)
- Hipótesis H1/H2/H3 y OE1-OE5 (de `FORMAL_PROPOSAL.md`)
- Cronograma M1-M7 (de `FORMAL_PROPOSAL.md` §6)
- Ausencia de conflicto ético (de `ETHICS_WAIVER_MEMO.md`)
- Costo cero (de `THESIS_COST_BREAKDOWN.md`)

**Verificabilidad:** cualquier evaluador del MOPC puede consultar la repo pública (cuando se libere bajo MIT) y confirmar que la solicitud es coherente con el proyecto declarado.

---

## 🚫 Lo que el paquete NO hace

- ❌ No envía emails a MOPC ni a funcionarios públicos
- ❌ No publica los placeholders en internet
- ❌ No accede a bases de datos del MOPC
- ❌ No genera código de barras ni firma digital (MOPC no acepta firma digital para SFP-020 aún)
- ❌ No incluye logos no oficiales (solo isotipo de la UNA-FADA en el membrete)

---

## ✅ Verificación final (qué chequear antes de imprimir)

- [ ] Todos los `[PLACEHOLDER_NNN]` reemplazados con datos reales de Iván
- [ ] Fecha de firma no posterior a la fecha de impresión (MOPC rechaza si > 30 días)
- [ ] Cédula vigente (MOPC rechaza si vencida)
- [ ] Domicilio real coincide con el de la Cédula
- [ ] Una copia de la Cédula adjunta (anverso + reverso, una hoja)
- [ ] Una copia del carnet de estudiante UNA vigente (opcional, fortalece presentación)
- [ ] Folder plástico transparente (no ganchos ni grapas; MOPC usa carpeta simple)

---

## 📂 Próximo paso

Iván lee `INSTRUCCIONES_DE_APRESENTACION.md`, completa los placeholders, ejecuta el comando `IMPRIMIR_TODO.md`, firma ológrafamente, y presenta en Mesa de Entrada del MOPC. Plazo de respuesta: **15 días hábiles** según Ley 5282/2014 Art. 17.

---

*Generado por Erebus bajo licencia MIT. Membrete y sellos institucionales son placeholders genéricos — Iván debe verificar el membrete vigente con Secretaría Académica FADA antes de imprimir.*