#!/usr/bin/env python3
"""
data_inventory.py — Build complete data inventory with SHA256 + sizes + licenses.

Walks data/raw/ and produces:
- data/raw/INVENTORY.json — structured manifest
- data/raw/INVENTORY.md — human-readable table

Run: make data-status (also runs this)
"""
import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_RAW = ROOT / "data" / "raw"

# License info per dataset (from DATA_MANIFEST.md)
LICENSE_MAP = {
    "osm": {
        "license": "ODbL-1.0",
        "attribution": "© OpenStreetMap contributors",
        "share_alike": True,
    },
    "ign": {
        "license": "Public Domain (Paraguayan government)",
        "attribution": "IGN Paraguay",
        "share_alike": False,
    },
    "sentinel2": {
        "license": "Copernicus Free & Open",
        "attribution": "European Space Agency (ESA)",
        "share_alike": False,
    },
    "worldpop": {
        "license": "CC-BY-4.0",
        "attribution": "WorldPop",
        "share_alike": False,
    },
    "openbuildings": {
        "license": "CC-BY-4.0",
        "attribution": "Google Open Buildings",
        "share_alike": False,
    },
    "indi": {
        "license": "Public Domain (Paraguayan government)",
        "attribution": "INDI Paraguay",
        "share_alike": False,
    },
    "mopc": {
        "license": "Public Domain (Ley 5282/2014)",
        "attribution": "MOPC Paraguay",
        "share_alike": False,
    },
    "chirps": {
        "license": "Public Domain",
        "attribution": "UCSB Climate Hazards Center",
        "share_alike": False,
    },
}


def sha256(path, chunk_size=65536):
    """Compute SHA256 of a file."""
    h = hashlib.sha256()
    try:
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(chunk_size), b""):
                h.update(chunk)
    except (PermissionError, OSError):
        return None
    return h.hexdigest()


def human_bytes(n):
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if n < 1024:
            return f"{n:.2f} {unit}"
        n /= 1024
    return f"{n:.2f} PB"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--snapshot", help="Specific snapshot date (default: latest)")
    args = ap.parse_args()

    if not DATA_RAW.exists():
        print(f"❌ {DATA_RAW} not found")
        return 1

    # Pick snapshot
    snapshots = sorted([d for d in DATA_RAW.iterdir() if d.is_dir()])
    if not snapshots:
        print(f"❌ No snapshots in {DATA_RAW}")
        return 1
    if args.snapshot:
        snap = DATA_RAW / args.snapshot
        if not snap.exists():
            print(f"❌ Snapshot {args.snapshot} not found")
            return 1
    else:
        snap = snapshots[-1]

    print(f"📦 Building inventory for: {snap.relative_to(ROOT)}")
    print()

    inventory = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "snapshot": snap.name,
        "datasets": {},
    }

    # Walk each dataset dir
    for ds_dir in sorted(snap.iterdir()):
        if not ds_dir.is_dir():
            continue
        ds_name = ds_dir.name
        license_info = LICENSE_MAP.get(ds_name, {
            "license": "Unknown",
            "attribution": "Unknown",
            "share_alike": False,
        })

        files = []
        total_size = 0
        for f in sorted(ds_dir.rglob("*")):
            if not f.is_file():
                continue
            size = f.stat().st_size
            total_size += size
            sha = sha256(f)
            files.append({
                "path": str(f.relative_to(ROOT)),
                "size_bytes": size,
                "size_human": human_bytes(size),
                "sha256": sha,
            })

        inventory["datasets"][ds_name] = {
            "path": str(ds_dir.relative_to(ROOT)),
            "file_count": len(files),
            "total_size_bytes": total_size,
            "total_size_human": human_bytes(total_size),
            **license_info,
            "files": files,
        }

    # Total
    total_size = sum(d["total_size_bytes"] for d in inventory["datasets"].values())
    inventory["total_size_bytes"] = total_size
    inventory["total_size_human"] = human_bytes(total_size)

    # Write JSON
    json_path = snap / "INVENTORY.json"
    json_path.write_text(json.dumps(inventory, indent=2))
    print(f"✅ Wrote {json_path.relative_to(ROOT)}")

    # Write Markdown
    md_path = snap / "INVENTORY.md"
    lines = [
        f"# Data Inventory — {snap.name}",
        "",
        f"**Generated:** {inventory['generated_at']}",
        f"**Total size:** {inventory['total_size_human']}",
        f"**Datasets:** {len(inventory['datasets'])}",
        "",
        "| Dataset | Files | Size | License | Attribution |",
        "|---------|------:|-----:|---------|-------------|",
    ]
    for ds_name, ds in inventory["datasets"].items():
        lines.append(
            f"| **{ds_name}** | {ds['file_count']:,} | {ds['total_size_human']} | {ds['license']} | {ds['attribution']} |"
        )
    lines.append(f"| **TOTAL** | | **{inventory['total_size_human']}** | | |")
    lines.append("")
    lines.append("## Per-dataset file list")
    lines.append("")
    for ds_name, ds in inventory["datasets"].items():
        lines.append(f"### {ds_name} ({ds['file_count']} files, {ds['total_size_human']})")
        lines.append("")
        if ds["files"]:
            lines.append("| File | Size | SHA256 (first 16) |")
            lines.append("|------|-----:|--------------------|")
            for f in ds["files"][:20]:  # cap at 20 to keep readable
                sha_short = (f["sha256"] or "n/a")[:16] if f["sha256"] else "n/a"
                lines.append(f"| `{Path(f['path']).name}` | {f['size_human']} | `{sha_short}...` |")
            if len(ds["files"]) > 20:
                lines.append(f"| ... and {len(ds['files']) - 20} more | | |")
        else:
            lines.append("_No files yet — fetch with `make data DATASETS={ds_name}` or `make data-{ds_name}`_")
        lines.append("")
    md_path.write_text("\n".join(lines))
    print(f"✅ Wrote {md_path.relative_to(ROOT)}")
    print()
    print(f"📊 Summary: {len(inventory['datasets'])} datasets, "
          f"{sum(d['file_count'] for d in inventory['datasets'].values())} files, "
          f"{inventory['total_size_human']} total")

    return 0


if __name__ == "__main__":
    sys.exit(main())