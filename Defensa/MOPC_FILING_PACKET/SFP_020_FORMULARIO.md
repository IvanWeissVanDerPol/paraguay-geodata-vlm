# Formulario SFP-020 — Solicitud Formal de Datos Públicos

> **Marco legal:** Ley 5282/2014, Decreto 1134/2014
> **Organismo ante quien se presenta:** Ministerio de Obras Públicas y Comunicaciones (MOPC) — Dirección General del Servicio Geográfico Militar
> **Tipo de solicitud:** [X] Persona física  [ ] Persona jurídica  [ ] Institución académica
> **Materia:** Datos geoespaciales producidos o custodiados por el MOPC (mosaicado aéreo institucional)

---

## Sección 1 — Datos del solicitante

| Campo | Valor |
|-------|-------|
| **Apellidos** | Weiss Van der Pol |
| **Nombres** | Iván |
| **Tipo y N° de documento** | Cédula de Identidad Paraguaya N° [CEDULA_NRO] |
| **Nacionalidad** | Paraguaya |
| **Fecha de nacimiento** | [FECHA_NACIMIENTO] |
| **Estado civil** | [ESTADO_CIVIL] |
| **Profesión u oficio** | Arquitecto / Maestrando en Tecnología de la Arquitectura |
| **Domicilio real** | [DOMICILIO_REAL] |
| **Departamento** | [DEPARTAMENTO] |
| **Localidad** | [LOCALIDAD] |
| **Teléfono fijo** | [TELEFONO_FIJO] |
| **Teléfono móvil** | [TELEFONO_CONTACTO] |
| **Correo electrónico** | [EMAIL_CONTACTO] |
| **Institución académica** | Universidad Nacional de Asunción — Facultad de Arquitectura, Diseño y Arte (FADA) — Maestría en Tecnología de la Arquitectura |
| **Matrícula / estudiante** | [MATRICULA_UNA] |

---

## Sección 2 — Datos del representante (si aplica)

> No aplica — el solicitante es persona física.

---

## Sección 3 — Identificación clara de la información solicitada

| Campo | Valor |
|-------|-------|
| **Descripción específica** | Mosaicado aéreo institucional del MOPC, campañas 2018-2025, para los Departamentos Central y zonas periurbanas del Gran Asunción + Asunción Capital, resolución ≥ 30 cm/píxel, sistema WGS84 / UTM 21S. Adicionalmente: Modelo Digital de Elevación (DEM, ≥ 1 m/píxel) y ortofotos del Área Metropolitana del Gran Asunción. |
| **Formato requerido** | GeoTIFF (.tif) con metadatos embebidos, idealmente con archivo auxiliar .tfw y .prj. Aceptable ECW o MrSID si comprimido con metadatos. |
| **Sistema de referencia** | WGS84 / UTM zona 21S (EPSG:32721). Aceptable WGS84 geográfico (EPSG:4326) si la versión UTM no está disponible. |
| **Periodo temporal** | Campañas 2018-2025 (preferentemente 2023-2025). |
| **Cobertura geográfica** | Asunción (Capital) + Departamento Central + áreas periurbanas del Gran Asunción (San Lorenzo, Fernando de la Mora, Lambaré, Luque, Mariano Roque Alonso, Limpio, Capiatá, Ñemby, San Antonio, Itauguá, Villa Elisa). |
| **Cantidad / Volumen aproximado** | ~50 GB (mosaicado aéreo Central) + ~5 GB (DEM) + ~20 GB (orto Gran Asunción). Estimación conservadora basada en resolución 30 cm y cobertura ~2.500 km². |

> Ver descripción completa en **Anexo Técnico** adjunto (`ANEXO_TECNICO.md`), secciones 1, 2 y 3.

---

## Sección 4 — Finalidad de la información solicitada

| Campo | Valor |
|-------|-------|
| **Finalidad específica** | Investigación de tesis de maestría titulada *"Anotación semiautomática con modelos multimodales del corpus cartográfico abierto de Paraguay y prototipo de interfaz conversacional para la reflexión territorial sudamericana"*. |
| **Tipo de investigación** | Académica (sin fines comerciales) |
| **Director de tesis** | Ing. Juan Carlos Cristaldo — FADA-UNA |
| **Producto académico esperado** | Manuscrito de tesis (Universidad Nacional de Asunción, 2027) + dataset anotado publicado en Hugging Face Hub + código de software en GitHub + 1 paper en conferencia Q1/Q2 (ICA 2027 / ACM SIGSPATIAL 2027 / ISPRS 2027) |
| **Plazo de retención de datos** | 24 meses posteriores a la defensa de tesis. Pasado ese plazo, los archivos serán eliminados del equipo local y se conservará únicamente el derivado procesado (etiquetas de features OSM proyectadas sobre el mosaicado). |
| **Licencia de la publicación derivada** | MIT (código) y CC-BY-SA 4.0 (dataset anotado). |

> Ver **Anexo Técnico** adjunto, secciones 4, 5, 6 y 7.

---

## Sección 5 — Modalidad de entrega preferida

| Campo | Opción marcada |
|-------|----------------|
| [X] | Entrega digital (descarga desde servidor FTP/SFTP del MOPC, o transferencia mediante HDD externo facilitado por el solicitante) |
| [ ] | Entrega presencial (CD/DVD / HDD en ventanilla del MOPC) |
| [ ] | Consulta en sala (revisión in situ sin extracción de copias) |

**Justificación:** el volumen estimado (~75 GB) hace preferible la entrega digital mediante transferencia SFTP. Si el MOPC solo dispone de entrega presencial, el solicitante se compromete a acercar un HDD externo nuevo (sin uso previo, marca a convenir) al MOPC para la grabación.

---

## Sección 6 — Compromisos del solicitante

[X] Me comprometo a no redistribuir los datos crudos a terceros sin autorización expresa del MOPC.
[X] Me comprometo a citar la fuente institucional en toda publicación derivada.
[X] Me comprometo a entregar al MOPC una copia del trabajo final.
[X] Me comprometo a no aplicar técnicas de identificación de personas sobre el mosaicado aéreo.
[X] Me comprometo a respetar las restricciones de uso que el MOPC especifique en la autorización.
[X] Declaro bajo juramento que los datos solicitados se utilizarán exclusivamente para la finalidad declarada en la Sección 4.

---

## Sección 7 — Exención de tasa administrativa

| Campo | Valor |
|-------|-------|
| **Solicita exención** | [X] Sí  [ ] No |
| **Motivo de exención** | Decreto 1134/2014, Art. 14 — solicitud con fines de investigación académica de grado/posgrado en universidad pública paraguaya (UNA-FADA) |
| **Documentación de respaldo** | Constancia de inscripción a la Maestría FADA-UNA (período 2026) + Aval del director de tesis Ing. Juan Carlos Cristaldo |

---

## Sección 8 — Firma y lugar

**Lugar y fecha:** [LUGAR_FECHA]

**Firma del solicitante:**

[FIRMA_OLOGRAFA — imprimir en hoja aparte con Cédula a la vista]

---

**Para uso exclusivo del MOPC — Sección de recepción (no completar)**

| Campo | (completado por MOPC) |
|-------|----------------------|
| **Fecha de recepción** | ____/____/______ |
| **N° de Expediente** | __________________ |
| **Funcionario receptor** | __________________ |
| **Firma del funcionario** | __________________ |
| **Sello de Mesa de Entrada** | [Sello MOPC] |

---

> **Próximo paso administrativo:** una vez presentada la solicitud en Mesa de Entrada Única del MOPC, el funcionario receptor asignará un N° de Expediente que aparecerá en la Constancia de Recepción. Guardar esa constancia — es la prueba del plazo legal de 15 días hábiles para respuesta (Ley 5282/2014, Art. 17).

---

*Documento generado por Erebus (agente autónomo de Iván) bajo licencia MIT. Los placeholders `[CORCHETES]` deben ser completados por Iván antes de imprimir. Ver `INSTRUCCIONES_DE_APRESENTACION.md` para el paso a paso completo.*