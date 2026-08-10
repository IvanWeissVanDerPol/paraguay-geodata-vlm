#!/usr/bin/env python3
"""
sanity_check.py — End-to-end environment + data + pipeline test.
Run: make sanity
"""
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def check_python():
    print("=== Python ===")
    import platform
    print(f"  Python {platform.python_version()} on {platform.system()} {platform.machine()}")
    py_version = tuple(int(x) for x in platform.python_version_tuple())
    assert py_version >= (3, 11), f"Python >= 3.11 required, got {platform.python_version()}"
    print("  ✅ Version OK")


def check_packages():
    print("\n=== Packages ===")
    required = {
        "numpy": "numpy",
        "pandas": "pandas",
        "geopandas": "geopandas",
        "shapely": "shapely",
        "rasterio": "rasterio",
        "transformers": "transformers",
        "torch": "torch",
        "open_clip": "open_clip",
        "ultralytics": "ultralytics",
        "langchain": "langchain",
        "chromadb": "chromadb",
        "jsonschema": "jsonschema",
    }
    missing = []
    for name, mod in required.items():
        try:
            m = __import__(mod)
            v = getattr(m, "__version__", "?")
            if v == "?":
                # try importlib.metadata
                try:
                    import importlib.metadata as md
                    v = md.version(name)
                except Exception:
                    pass
            print(f"  ✅ {name:<18} {v}")
        except ImportError:
            print(f"  ❌ {name:<18} missing")
            missing.append(name)
    if missing:
        print(f"\n  Install missing: uv pip install {' '.join(missing)}")
        return False
    return True


def check_cli_tools():
    print("\n=== CLI tools ===")
    tools = {
        "git": ["git", "--version"],
        "docker": ["docker", "--version"],
        "curl": ["curl", "--version"],
        "jq": ["jq", "--version"],
        "ogrinfo": ["ogrinfo", "--version"],
        "hf": ["hf", "--version"],
    }
    for name, cmd in tools.items():
        try:
            r = subprocess.run(cmd, capture_output=True, text=True, timeout=5)
            if r.returncode == 0:
                first_line = (r.stdout or r.stderr).split("\n")[0][:50]
                # hf CLI shows a "Hint" line first; skip it
                if first_line.startswith("Hint:"):
                    lines = (r.stdout or r.stderr).split("\n")
                    first_line = next((l for l in lines if l and not l.startswith("Hint:")), first_line)[:50]
                print(f"  ✅ {name:<20} {first_line}")
            else:
                print(f"  ❌ {name:<20} not available")
        except FileNotFoundError:
            print(f"  ❌ {name:<20} not installed")


def check_data():
    print("\n=== Data ===")
    raw_dir = ROOT / "data" / "raw"
    if not raw_dir.exists():
        print(f"  ❌ data/raw/ not found")
        return False
    dates = sorted([d for d in raw_dir.iterdir() if d.is_dir()])
    if not dates:
        print(f"  ❌ no data snapshots yet")
        return False
    latest = dates[-1]
    print(f"  Latest snapshot: {latest.relative_to(ROOT)}")
    osm_dir = latest / "osm"
    if osm_dir.exists():
        shapefiles = list((osm_dir / "extracted").glob("*.shp")) if (osm_dir / "extracted").exists() else []
        print(f"  OSM extracted: {len(shapefiles)} shapefiles")
        if shapefiles:
            total_bytes = sum(s.stat().st_size for s in shapefiles)
            print(f"  OSM total size: {total_bytes / 1e6:.0f} MB")
            print("  ✅ OSM data present")
    sha_file = latest / "SHA256SUMS"
    if sha_file.exists():
        n_hashes = len(sha_file.read_text().strip().split("\n"))
        print(f"  SHA256SUMS: {n_hashes} entries")
    return True


def check_credentials():
    print("\n=== Credentials ===")
    creds_file = ROOT / "secrets" / "creds.json"
    if not creds_file.exists():
        print(f"  ⚠️  secrets/creds.json not found")
        return False
    try:
        creds = json.loads(creds_file.read_text())
        n_filled = 0
        n_placeholder = 0
        n_skip = 0
        for svc_name, svc_data in creds.get("services", {}).items():
            if not isinstance(svc_data, dict):
                continue
            for k, v in svc_data.items():
                if k.startswith("_"):
                    continue
                if not isinstance(v, str):
                    continue
                if v.startswith("FILL_ME_"):
                    n_placeholder += 1
                elif v.lower() == "skip":
                    n_skip += 1
                else:
                    n_filled += 1
        print(f"  Filled:      {n_filled}")
        print(f"  Placeholders: {n_placeholder}")
        print(f"  Skipped:      {n_skip}")
        if n_placeholder == 0 and n_skip == 0:
            print("  ✅ All credentials filled")
        elif n_placeholder == 0:
            print("  ✅ All filled (some marked skip)")
        else:
            print(f"  ⚠️  {n_placeholder} credentials still placeholder")
            print(f"  Run: make validate-creds")
        return n_placeholder == 0
    except Exception as e:
        print(f"  ❌ creds.json parse error: {e}")
        return False


def check_pipeline():
    print("\n=== Annotation pipeline (smoke test) ===")
    try:
        sys.path.insert(0, str(ROOT / "scripts"))
        from auto_annotate import PROMPTS  # noqa
        print(f"  ✅ PROMPTS loaded ({len(PROMPTS)} categories)")
        for cat in PROMPTS:
            n_es = len(PROMPTS[cat].get("es", []))
            n_en = len(PROMPTS[cat].get("en", []))
            print(f"     {cat:<12} {n_es} ES / {n_en} EN prompts")
    except Exception as e:
        print(f"  ❌ annotation pipeline: {e}")
        return False
    return True


def main():
    print("🎓 P1 GeoData v2 — sanity check\n")
    print(f"Project root: {ROOT}\n")

    check_python()
    pkg_ok = check_packages()
    check_cli_tools()
    data_ok = check_data()
    creds_ok = check_credentials()
    pipeline_ok = check_pipeline()

    print()
    print("=" * 60)
    overall = pkg_ok and data_ok and pipeline_ok
    print(f"  Overall: {'✅ PASS' if overall else '⚠️  PASS WITH WARNINGS'}")
    print(f"  Packages:    {'✅' if pkg_ok else '❌'}")
    print(f"  Data:        {'✅' if data_ok else '❌'}")
    print(f"  Credentials: {'✅' if creds_ok else '⚠️'}")
    print(f"  Pipeline:    {'✅' if pipeline_ok else '❌'}")
    print("=" * 60)

    return 0 if overall else 1


if __name__ == "__main__":
    sys.exit(main())