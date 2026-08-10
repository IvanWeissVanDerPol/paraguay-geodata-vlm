# ETHICS WAIVER MEMO — P1 GeoData v2

**Thesis:** Anotación semiautomática con modelos multimodales del corpus cartográfico abierto de Paraguay y prototipo de interfaz conversacional para la reflexión territorial sudamericana

**Author:** Iván Weiss Van der Pol
**Date:** 2026-08-10
**Status:** Self-assessment, to be presented with manuscript

---

## TL;DR

**No ethics committee review is required for this thesis.** This memo justifies the conclusion with reference to the four recognized international criteria (Belmont Report, CIOMS, Paraguayan Law 1614/2000 on research ethics, UNA-FADA internal regulations).

---

## 1. Source of all data

| Data | Source | Type | Human subjects? |
|---|---|---|---|
| OpenStreetMap Paraguay extract | Geofabrik / openstreetmap.org (ODbL license) | Public geospatial vector data | **No** — crowdsourced, anonymized contributions |
| IGN raster tiles (Instituto Geográfico Nacional Paraguay) | ign.gob.py public WMS | Public raster cartography | **No** |
| Sentinel-2 satellite imagery | Copernicus Open Access Hub (EU) | Public satellite | **No** |
| OSM changeset history | openstreetmap.org API | Public, anonymized user IDs only | **No** |
| Paraguay indigenous territories | INDI / publicly available GeoJSON (UN-Habitat partnership) | Public polygon data | **No** — territory polygons, not persons |
| MOPC drone imagery (if used) | Ministerio de Obras Públicas y Comunicaciones (public dataset) | Public infrastructure imagery | **No** |
| Fine-tune eval (200 features, 3 annotators) | Annotators are **thesis author + 2 public cartographers** | Internal annotation | Annotators consent in writing as research collaborators (not subjects) |

## 2. Criteria for requiring ethics review (Belmont / CIOMS)

A research project requires IRB/ethics review when **at least one** is true:

- [ ] Collects data from **living human subjects** through intervention or interaction
- [ ] Collects **identifiable private information** about living persons
- [ ] Involves **biological samples**, medical procedures, or clinical interventions
- [ ] Studies **vulnerable populations** (children, prisoners, mentally disabled, etc.)
- [ ] Could cause **harm to participants' dignity, privacy, or well-being**

## 3. Applicability to this thesis

| Criterion | Applies? | Justification |
|---|---|---|
| Living human subjects | **NO** | All data is geospatial, raster, or satellite. No persons are studied. |
| Identifiable private information | **NO** | No names, IDs, biometrics, or personal data. OSM user IDs are pseudonymous and not re-identifiable without admin access to openstreetmap.org. |
| Biological samples | **NO** | N/A |
| Vulnerable populations | **NO** | N/A |
| Dignity/privacy harm | **NO** | Annotation work is on cartographic features (highways, buildings, land-use classes), not on persons. |

## 4. Paraguayan legal framework

- **Ley 1614/2000** (Ley de Investigación Científica con Seres Humanos): regulates research *with human beings*. **Out of scope** — no human subjects.
- **Ley 1682/2001** (Ley de Información de Interés Público): the datasets used (IGN, INDI, MOPC, OSM) are public interest information. In scope, not regulated as sensitive.
- **Ley 6534/2020** (Protección de Datos Personales): **out of scope** — no personal data processed.

## 5. UNA-FADA institutional framework

- FADA research line *Mapeo de software libre* (Resolución 1141/2022) explicitly contemplates work on OSM Paraguay as a normal research activity, with no ethics review triggered when no human subjects are involved.

## 6. Indirect ethics considerations (voluntary)

Although no ethics review is required, this thesis adopts three voluntary safeguards:

1. **OSM contributor anonymization.** OSM user IDs will be hashed (SHA-256) before any analysis. No re-identification attempted.
2. **Indigenous territory data sovereignty.** When working with indigenous territories, attribution follows UN-Habitat CARE principles and INDI protocols. No ground-truth data from communities is used without consent.
3. **Drone imagery (MOPC).** If used, only the public MOPC-released dataset is consumed. No drone flights over private property are conducted for this thesis.

## 7. Annotation protocol (3 annotators)

- Annotators are **public cartographers** (Cristaldo lab collaborators, IGN professionals, or community mappers).
- Annotators sign a **collaboration agreement** stating they annotate as research collaborators, not as human subjects.
- Compensation: standard academic credit (co-authorship on dataset paper, attribution in thesis acknowledgements).
- Annotator disagreement is measured with **Cohen's κ inter-annotator agreement**; target κ ≥ 0.85.

## 8. Conclusion

This thesis is **exempt from ethics committee review** under:
- Belmont Report criteria (no human subjects)
- CIOMS International Ethical Guidelines (no intervention on persons)
- Paraguayan Ley 1614/2000 (no research with human beings)
- UNA-FADA Resolución 1141/2022 (mapping with open data is institutional normal practice)

The thesis author keeps this memo on file. It will be attached to the manuscript when submitted to UNA TFG committee and to the target publication venue (ICA / ACM SIGSPATIAL / Remote Sensing of Environment).

---

**Signature:** _________________________
**Date:** 2026-08-10
**Witness (optional):** _________________________