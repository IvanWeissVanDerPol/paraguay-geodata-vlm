#!/usr/bin/env bash
# fetch_data.sh — Download all datasets for P1 GeoData v2
# Usage: ./scripts/fetch_data.sh [--date YYYY-MM-DD] [--datasets osm,ign,sentinel,indi,mopc,worldpop,openbuildings,chirps]
# All downloads are versioned by date for reproducibility.
# Author: Iván Weiss Van der Pol · Date: 2026-08-10

set -euo pipefail

DATE=$(date +%Y-%m-%d)
SELECTED="osm,ign,sentinel,indi,worldpop,openbuildings,chirps"  # mopc needs manual request
DATA_ROOT="${DATA_ROOT:-/opt/data/thesis-active/data}"
RAW_DIR="$DATA_ROOT/raw/$DATE"

mkdir -p "$RAW_DIR"/{osm,ign,sentinel2,indi,mopc,worldpop,openbuildings,chirps}

# Parse args
while [[ $# -gt 0 ]]; do
  case "$1" in
    --date) DATE="$2"; shift 2 ;;
    --datasets) SELECTED="$2"; shift 2 ;;
    *) echo "Unknown arg: $1"; exit 1 ;;
  esac
done

log() { echo "[$(date +%H:%M:%S)] $1"; }

download() {
  local name="$1" url="$2" outfile="$3"
  log "Downloading $name → $outfile"
  curl -L --fail --retry 3 --retry-delay 5 -o "$outfile" "$url"
  if command -v sha256sum >/dev/null 2>&1; then
    sha256sum "$outfile" >> "$RAW_DIR/SHA256SUMS"
  fi
}

# D1 — OSM Paraguay extract (Geofabrik, free)
if [[ "$SELECTED" == *"osm"* ]]; then
  download "OSM Paraguay (shp)" \
    "https://download.geofabrik.de/south-america/paraguay-latest-free.shp.zip" \
    "$RAW_DIR/osm/paraguay-latest-free.shp.zip"
fi

# D3 — IGN raster (manual — see DATA_MANIFEST.md; WMS endpoints to query)
if [[ "$SELECTED" == *"ign"* ]]; then
  log "IGN raster: requires WMS pull. Run: python scripts/fetch_ign_wms.py --deptos=all"
  log "WMS endpoint: https://www.ign.gob.py/servicios/wms"
  log "Skipping automated download — manual step."
fi

# D4 — Sentinel-2 (requires Copernicus Hub account; alternative: Element84 cloud-free mosaics)
if [[ "$SELECTED" == *"sentinel"* ]]; then
  log "Sentinel-2: requires Copernicus Hub account (free registration at https://scihub.copernicus.eu/)"
  log "Alternative: download cloud-free mosaics from https://registry.opendata.aws/sentinel-2/"
  log "Example: aws s3 cp s3://sentinel-cogs/sentinel-s2-l2a-cogs/2024/S2A_21J_VH_... $RAW_DIR/sentinel2/ --recursive --exclude '*'"
  log "Skipping automated download — requires AWS account."
fi

# D5 — INDI indigenous territories (Paraguayan gov open data)
if [[ "$SELECTED" == *"indi"* ]]; then
  log "INDI: download from indi.gov.py or UN-Habitat mirror"
  log "Attempting direct download..."
  # Try a UN-Habitat mirror first
  download "INDI territories (UN-Habitat mirror)" \
    "https://data.humdata.org/dataset/paraguay-indigenous-territories" \
    "$RAW_DIR/indi/territories.html" || log "Manual download needed"
fi

# D7 — WorldPop Paraguay (CC BY 4.0)
if [[ "$SELECTED" == *"worldpop"* ]]; then
  download "WorldPop Paraguay 2020 UN-adjusted" \
    "https://www.worldpop.org/geodata/summary?id=47434" \
    "$RAW_DIR/worldpop/worldpop_py_2020.zip" || log "Manual download needed"
fi

# D8 — Open Buildings v3 (Google, CC BY 4.0)
if [[ "$SELECTED" == *"openbuildings"* ]]; then
  log "Open Buildings: requires gsutil + Google Cloud auth (free)"
  log "Paraguay tiles: 8S, 9S, 17S, 18S, 20S, 21S"
  log "Example: gsutil -m cp -r gs://open-buildings-data/v3/regions/S8S_buildings.csv.gz $RAW_DIR/openbuildings/"
  log "Skipping automated download — requires gsutil."
fi

# D9 — CHIRPS daily precipitation (public domain)
if [[ "$SELECTED" == *"chirps"* ]]; then
  log "CHIRPS daily NetCDF (2024-2026): https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_daily/netcdf/p25/"
  log "Manual download — file size ~200 MB per year."
fi

# D6 — MOPC drone imagery (manual — request via acceso a la información pública)
if [[ "$SELECTED" == *"mopc"* ]]; then
  log "MOPC drone: file Solicitud de Acceso a la Información Pública (Ley 5282/2014)"
  log "Form: https://www.mopc.gov.py/transparencia/solicitud-informacion"
  log "Estimated response time: 15 business days. Skipping."
fi

log "Done. Raw data at: $RAW_DIR"
log "SHA256SUMS at: $RAW_DIR/SHA256SUMS"
log ""
log "Next steps:"
log "  1. Verify each dataset: ls -lh $RAW_DIR/<dataset>/"
log "  2. Run scripts/fetch_ign_wms.py for IGN"
log "  3. Set up Copernicus Hub account for Sentinel-2"
log "  4. Once data is in place, run scripts/auto_annotate.py"