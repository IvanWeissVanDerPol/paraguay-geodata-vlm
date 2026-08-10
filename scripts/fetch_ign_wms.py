#!/usr/bin/env python3
"""
fetch_ign_wms.py — Pull IGN Paraguay raster tiles via WMS.

IGN Paraguay = Instituto Geográfico Nacional "Juan José Franco"
Public WMS service (no auth required for raster layers).

Usage:
    python3 scripts/fetch_ign_wms.py --deptos=all
    python3 scripts/fetch_ign_wms.py --deptos=central,asuncion,alto_parana
    python3 scripts/fetch_ign_wms.py --bbox="-57.6,-25.3,-57.5,-25.2" --zoom 14

Output:
    data/raw/<date>/ign/<depto>/<z>/<x>/<y>.tif

Note: The WMS endpoint and layer names need to be confirmed by hitting
the IGN capabilities document at runtime. The defaults below are the most
common endpoints; the script will probe and adapt.
"""
import argparse
import json
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Default WMS endpoints to try (in order)
WMS_CANDIDATES = [
    "https://www.ign.gob.py/wms",
    "https://www.ign.gob.py/geoserver/wms",
    "https://geoserver.ign.gob.py/wms",
    "https://ide.ign.gob.py/wms",
]

# Paraguay departamentos + bounding boxes (approximate centroids)
DEPARTAMENTOS = {
    "asuncion": {"name": "Asunción (Capital)", "bbox": [-57.65, -25.32, -57.55, -25.22], "zoom": 14},
    "concepcion": {"name": "Concepción", "bbox": [-57.45, -23.40, -56.40, -22.10], "zoom": 10},
    "san_pedro": {"name": "San Pedro", "bbox": [-57.50, -24.50, -55.50, -23.00], "zoom": 10},
    "cordillera": {"name": "Cordillera", "bbox": [-57.40, -25.50, -56.40, -24.50], "zoom": 11},
    "guaira": {"name": "Guairá", "bbox": [-56.80, -26.20, -55.50, -25.40], "zoom": 11},
    "caaguazu": {"name": "Caaguazú", "bbox": [-56.50, -25.70, -55.00, -24.50], "zoom": 10},
    "caazapa": {"name": "Caazapá", "bbox": [-56.60, -26.80, -55.40, -25.50], "zoom": 11},
    "itapua": {"name": "Itapúa", "bbox": [-56.30, -27.50, -54.80, -26.40], "zoom": 10},
    "misiones": {"name": "Misiones", "bbox": [-57.30, -27.50, -56.50, -26.50], "zoom": 11},
    "paraguari": {"name": "Paraguarí", "bbox": [-57.50, -26.50, -56.30, -25.30], "zoom": 11},
    "alto_parana": {"name": "Alto Paraná", "bbox": [-55.50, -26.20, -54.20, -24.80], "zoom": 10},
    "central": {"name": "Central", "bbox": [-57.80, -25.80, -57.20, -25.00], "zoom": 12},
    "neembucu": {"name": "Ñeembucú", "bbox": [-58.50, -27.50, -57.00, -25.50], "zoom": 11},
    "amambay": {"name": "Amambay", "bbox": [-56.30, -23.50, -55.00, -21.80], "zoom": 11},
    "canindeyu": {"name": "Canindeyú", "bbox": [-55.50, -24.80, -53.80, -23.50], "zoom": 10},
    "presidente_hayes": {"name": "Presidente Hayes", "bbox": [-60.00, -25.50, -57.00, -22.00], "zoom": 9},
    "alto_paraguay": {"name": "Alto Paraguay", "bbox": [-60.00, -21.50, -57.00, -19.50], "zoom": 9},
    "boqueron": {"name": "Boquerón", "bbox": [-62.50, -23.50, -58.50, -20.00], "zoom": 9},
}


def probe_wms(endpoints, timeout=15):
    """Try each endpoint, return (url, layers_list) of the first that works."""
    for url in endpoints:
        try:
            cap_url = f"{url}?service=WMS&request=GetCapabilities"
            req = urllib.request.Request(cap_url, headers={"User-Agent": "thesis-er/1.0"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                body = r.read().decode("utf-8", errors="ignore")
            if "<WMS_Capabilities" in body or "WMT_MS_Capabilities" in body:
                # Extract layer names
                layers = re.findall(r"<Name>([^<]+)</Name>", body)
                return url, layers
        except (urllib.error.URLError, urllib.error.HTTPError, OSError):
            continue
    return None, []


def fetch_tile(base_url, layer, bbox, width=1024, height=1024, crs="EPSG:4326", timeout=30):
    """Fetch a single WMS tile as TIFF."""
    params = {
        "service": "WMS",
        "version": "1.1.1",
        "request": "GetMap",
        "layers": layer,
        "bbox": ",".join(str(x) for x in bbox),
        "width": width,
        "height": height,
        "srs": crs,
        "format": "image/tiff",
    }
    url = f"{base_url}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"User-Agent": "thesis-er/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def fetch_depto(base_url, layer, depto_key, out_dir, max_retries=3):
    """Fetch all tiles for one departamento. Retries with backoff."""
    info = DEPARTAMENTOS[depto_key]
    bbox = info["bbox"]
    width = height = 1024
    out_path = out_dir / depto_key / "full.tif"
    out_path.parent.mkdir(parents=True, exist_ok=True)

    for attempt in range(max_retries):
        try:
            tiff_bytes = fetch_tile(base_url, layer, bbox, width, height)
            if len(tiff_bytes) < 100:
                raise ValueError(f"Response too small ({len(tiff_bytes)} bytes)")
            out_path.write_bytes(tiff_bytes)
            return {"ok": True, "bytes": len(tiff_bytes), "path": str(out_path)}
        except Exception as e:
            if attempt < max_retries - 1:
                wait = 2 ** attempt
                print(f"   Retry {attempt + 1}/{max_retries} in {wait}s: {e}")
                time.sleep(wait)
            else:
                return {"ok": False, "error": str(e), "path": str(out_path)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--deptos", default="all",
                    help="Comma-separated list (e.g. 'central,asuncion') or 'all'")
    ap.add_argument("--layer", default=None,
                    help="Layer name (auto-detected from capabilities if omitted)")
    ap.add_argument("--zoom", type=int, default=None,
                    help="Override default zoom level per depto")
    ap.add_argument("--out-dir", default=None,
                    help="Output directory (default: data/raw/<date>/ign)")
    ap.add_argument("--probe-only", action="store_true",
                    help="Just probe WMS endpoints, don't fetch")
    args = ap.parse_args()

    # Output dir
    if args.out_dir:
        out_dir = Path(args.out_dir)
    else:
        from datetime import datetime
        date = datetime.now().strftime("%Y-%m-%d")
        out_dir = ROOT / "data" / "raw" / date / "ign"
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"🗺️  IGN Paraguay WMS fetcher")
    print(f"   Output: {out_dir}")
    print()

    # Probe
    print("🔍 Probing WMS endpoints...")
    base_url, layers = probe_wms(WMS_CANDIDATES)
    if not base_url:
        print("❌ No working WMS endpoint found.")
        print("   Tried:")
        for url in WMS_CANDIDATES:
            print(f"     {url}")
        print()
        print("   Possible reasons:")
        print("   1. No internet (check: ping google.com)")
        print("   2. IGN has moved/restructured their WMS")
        print("   3. WMS is firewalled to Paraguayan IPs only")
        print()
        print("   Fallback: download from mirrors or use Sentinel-2 only")
        sys.exit(1)

    print(f"✅ Working endpoint: {base_url}")
    print(f"   Available layers: {len(layers)}")
    for layer in layers[:10]:
        print(f"     - {layer}")
    if len(layers) > 10:
        print(f"     ... and {len(layers) - 10} more")

    # Pick layer
    if args.layer:
        layer = args.layer
    else:
        # Pick first layer that looks like raster (not vector)
        candidates = [l for l in layers if any(kw in l.lower() for kw in
                    ["raster", "orto", "imagen", "satelite", "elevation", "dem"])]
        if candidates:
            layer = candidates[0]
        else:
            layer = layers[0]
    print(f"\n📐 Selected layer: {layer}")

    if args.probe_only:
        print("\n(probe-only mode — not fetching)")
        return 0

    # Determine deptos
    if args.deptos == "all":
        depto_list = list(DEPARTAMENTOS.keys())
    else:
        depto_list = [d.strip() for d in args.deptos.split(",") if d.strip() in DEPARTAMENTOS]
        if not depto_list:
            print(f"❌ No valid deptos in: {args.deptos}")
            print(f"   Valid: {list(DEPARTAMENTOS.keys())}")
            sys.exit(2)

    print(f"\n📥 Fetching {len(depto_list)} deptos...")
    print(f"   (resolution: 1024×1024 px each)")

    # Fetch loop
    results = []
    for i, depto in enumerate(depto_list, 1):
        info = DEPARTAMENTOS[depto]
        print(f"\n  [{i}/{len(depto_list)}] {info['name']}...")
        result = fetch_depto(base_url, layer, depto, out_dir)
        if result["ok"]:
            mb = result["bytes"] / 1024 / 1024
            print(f"     ✅ {mb:.2f} MB → {result['path']}")
        else:
            print(f"     ❌ {result['error']}")
        results.append({"depto": depto, **result})

    # Summary
    ok = sum(1 for r in results if r["ok"])
    total_mb = sum(r["bytes"] for r in results if r.get("bytes", 0)) / 1024 / 1024
    print(f"\n📊 Summary: {ok}/{len(results)} succeeded, {total_mb:.1f} MB total")
    print(f"   Output: {out_dir}")

    # Write manifest
    manifest = {
        "fetched_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "wms_endpoint": base_url,
        "layer": layer,
        "results": results,
    }
    manifest_path = out_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2))
    print(f"   Manifest: {manifest_path}")

    return 0 if ok == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())