# DATA MANIFEST — P1 GeoData v2

**Thesis:** Anotación semiautomática con modelos multimodales del corpus cartográfico abierto de Paraguay
**Author:** Iván Weiss Van der Pol
**Date:** 2026-08-10

---

## 1. Datasets required

| # | Dataset | Type | Source | License | Size est. | Already in repo? |
|---|---|---|---|---|---|---|
| D1 | OpenStreetMap Paraguay extract | Vector (GeoJSON, PBF) | Geofabrik downloads.geofabrik.de | ODbL 1.0 | ~250 MB | Yes (paraguay-geodata) |
| D2 | OSM Paraguay changeset history | Vector + metadata | openstreetmap.org API | ODbL 1.0 | ~50 MB | No (to fetch) |
| D3 | IGN raster tiles (Asunción, deptos) | Raster (Web Mercator) | ign.gob.py WMS | Public domain (Paraguayan gov) | ~2 GB | Yes (paraguay-geodata) |
| D4 | Sentinel-2 L2A (cloud-free mosaics) | Raster multispectral | Copernicus Open Access Hub | Copernicus free & open | ~20 GB (Paraguay mosaic) | No (to fetch) |
| D5 | INDI indigenous territories polygons | Vector (GeoJSON) | indi.gov.py (or UN-Habitat mirror) | Public domain | ~5 MB | Yes (paraguay-geodata) |
| D6 | MOPC road drone imagery (public release) | Raster (JPEG/GeoTIFF) | mopc.gov.py open data portal | Public domain | ~5 GB | No (to fetch) |
| D7 | WorldPop Paraguay population grid | Raster (GeoTIFF) | worldpop.org | CC BY 4.0 | ~50 MB | No (to fetch) |
| D8 | Open Buildings (Google) Paraguay | Vector (GeoJSON) | sites.research.google/open-buildings | CC BY 4.0 | ~100 MB | No (to fetch) |
| D9 | Climate Hazards InfraRed (CHIRPS) Paraguay | Raster | data.chc.ucsb.edu | Public domain | ~200 MB | No (to fetch) |
| D10 | Paraguay parcel registry (catastro) | Vector | SET.gov.py partial open data | Mixed (some public) | TBD | To evaluate |

**Total estimated raw size:** ~28 GB
**Total estimated annotated dataset:** ~50K-100K features, ~500 MB

## 2. License compatibility matrix

| Combination | Compatible? | Notes |
|---|---|---|
| ODbL (OSM) + Public domain (IGN, Copernicus) + CC BY (WorldPop, Open Buildings) | ✅ YES | All open, attribution required for ODbL + CC BY |
| ODbL derivatives | ✅ YES with attribution + share-alike | If thesis publishes derived dataset, must inherit ODbL terms for the OSM-derived portion |
| MOPC drone imagery public release | ✅ YES | Public domain per Paraguayan access-to-info law 5282/2014 |

## 3. Data acquisition plan

### D1 — OSM Paraguay extract
- **URL:** `https://download.geofabrik.de/south-america/paraguay-latest-free.shp.zip` (or .osm.pbf)
- **Method:** `wget` or `curl` to local store
- **Storage:** `data/raw/osm/paraguay-latest-free.shp.zip`
- **SHA256:** computed on download, recorded in `data/raw/osm/SHA256SUMS`
- **Versioning:** `paraguay-latest-free` updates daily; pin to date `2026-08-10` for reproducibility

### D3 — IGN raster tiles
- **URL:** `https://www.ign.gob.py/servicios/wms` (WMS endpoint)
- **Method:** `owslib` Python client or `gdalwms`
- **Storage:** `data/raw/ign/<depto>/<z>/<x>/<y>.tif`
- **Coverage:** 17 departamentos + Asunción capital
- **Tile size:** 256×256 to 1024×1024 px depending on zoom

### D4 — Sentinel-2 L2A
- **URL:** `https://scihub.copernicus.eu/` (registration required, free) OR `https://element84.com/sentinel-2-cloud-free-mosaics/` (preprocessed)
- **Method:** `sentinelsat` Python client or direct download from Element84
- **Storage:** `data/raw/sentinel2/<tile_id>/<date>.tif`
- **Cloud cover threshold:** < 10%
- **Date range:** 2024-01-01 to 2026-08-10 (cloud-free mosaics)

### D5 — INDI indigenous territories
- **URL:** `https://www.indi.gov.py/datos-abiertos` or UN-Habitat mirror
- **Method:** manual download or API
- **Storage:** `data/raw/indi/territorios_indigenas.geojson`
- **Fields:** id_territorio, nombre_comunidad, pueblo, departamento, area_ha

### D6 — MOPC drone imagery
- **URL:** `https://www.mopc.gov.py/datos-abiertos` (to verify)
- **Fallback:** request via acceso a la información pública (Ley 5282/2014)
- **Storage:** `data/raw/mopc/drones/<campaign>/<flight>.tif`

### D7 — WorldPop
- **URL:** `https://www.worldpop.org/geodata/summary?id=47434` (Paraguay 2020 UN-adjusted)
- **Method:** direct download

### D8 — Open Buildings
- **URL:** `https://sites.research.google/open-buildings/` (3D buildings, v3, 2024)
- **Method:** `gsutil cp` from `gs://open-buildings-data/v3/`
- **Coverage:** Paraguay tiles `8S, 9S, 20S, 21S` for south, `17S, 18S` for north

### D9 — CHIRPS
- **URL:** `https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_daily/netcdf/p25/`
- **Method:** direct download or OPeNDAP
- **Storage:** `data/raw/chirps/<year>.nc`

## 4. Annotation schema

Each feature will be annotated with:

```json
{
  "feature_id": "uuid-v4",
  "source_dataset": "OSM|IGN|Sentinel-2|INDI|MOPC",
  "geometry_type": "Point|LineString|Polygon|Raster",
  "category": {
    "level_1": "highway|building|landuse|water|vegetation|indigenous|...",
    "level_2": "primary|residential|industrial|forest|territory|...",
    "level_3": "paved|dirt|mixed|..."
  },
  "attributes": {
    "surface": "asphalt|concrete|dirt|gravel|...",
    "condition": "good|fair|poor|unknown",
    "confidence": 0.0
  },
  "spatial_ref": "EPSG:4326",
  "bbox": [xmin, ymin, xmax, ymax],
  "area_m2": 1234.5,
  "source_id": "osm-way-123456789",
  "annotator_id": "anon-001",
  "annotation_date": "2026-09-15",
  "review_status": "single-reviewed|double-reviewed|disputed"
}
```

**Total categories:** ~15 level-1, ~60 level-2, ~120 level-3 (estimated)

## 5. Storage and version control

- **Local:** `/opt/data/thesis-active/data/` (gitignored; raw + processed)
- **Git LFS:** for derived datasets > 100 MB that need version tracking
- **Hugging Face Hub:** for the published annotated dataset (10K-100K features, ~500 MB)
- **Zenodo:** for DOI-anchored snapshot at publication time
- **R2 / S3:** not needed for thesis; only for production hosting of the web app

## 6. Data quality and validation

| Validation | Method | Frequency |
|---|---|---|
| OSM geometry validity | `osmium` check + `pyosmium` validation | On ingest |
| IGN raster completeness | Compare against OSM coverage polygons; flag gaps | On ingest |
| Sentinel-2 cloud-free | `s2cloudless` mask | Per tile |
| Annotation consistency | Cohen's κ between 2-3 annotators on 200-feature sample | At month 4 |
| Class imbalance | Distribution check; targeted augmentation for rare classes | At month 4 |

## 7. Ethical and legal re-confirmation

All datasets listed above are **public, freely licensed, and contain no personal data**. See `ETHICS_WAIVER_MEMO.md` for full justification.

## 8. Reproducibility

- All downloads scripted in `scripts/fetch_data.sh` and committed to repo
- All SHA256 hashes recorded in `data/raw/SHA256SUMS`
- All versioned by download date (`data/raw/2026-08-10/...`)
- Docker bundle `data/Dockerfile.data` captures exact OS + Python + GDAL versions

## 9. Open issues to resolve

- [ ] MOPC drone imagery public availability — verify portal exists or request via Ley 5282/2014
- [ ] Catastro (SET) parcel data — mixed openness; may be deferred
- [ ] UN-Habitat Paraguay indigenous territories — confirm licensing
- [ ] WorldPop 2025 release vs 2020 — use latest available

---

**Next action:** `scripts/fetch_data.sh` to be implemented in Week 1.