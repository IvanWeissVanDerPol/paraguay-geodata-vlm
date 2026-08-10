#!/usr/bin/env python3
"""
data_status.py — Show inventory of downloaded datasets.

Usage:
    python3 scripts/data_status.py
    make data-status
"""
import os
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_RAW = ROOT / "data" / "raw"


def human_bytes(n):
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if n < 1024:
            return f"{n:.1f} {unit}"
        n /= 1024
    return f"{n:.1f} PB"


def main():
    if not DATA_RAW.exists():
        print(f"❌ {DATA_RAW} not found. Run 'make data-osm' first.")
        return 1

    print("📦 Data inventory\n")
    snapshots = sorted([d for d in DATA_RAW.iterdir() if d.is_dir()])
    if not snapshots:
        print("No data snapshots yet.")
        return 1

    for snap in snapshots:
        print(f"📅 Snapshot: {snap.name}")
        print(f"   Path: {snap.relative_to(ROOT)}")
        for dataset in sorted(snap.iterdir()):
            if not dataset.is_dir():
                continue
            files = list(dataset.rglob("*"))
            file_count = sum(1 for f in files if f.is_file())
            total_size = sum(f.stat().st_size for f in files if f.is_file())
            print(f"   📂 {dataset.name:<14} {file_count:>4} files  {human_bytes(total_size):>10}")

            if dataset.name == "osm":
                extracted = dataset / "extracted"
                if extracted.exists():
                    shps = sorted(extracted.glob("*.shp"))
                    print(f"      Shapefiles: {len(shps)}")
                    for shp in shps[:3]:
                        size = shp.stat().st_size
                        print(f"        - {shp.stem:<50} {human_bytes(size)}")
                    if len(shps) > 3:
                        print(f"        ... and {len(shps) - 3} more")

        # SHA256SUMS
        sha = snap / "SHA256SUMS"
        if sha.exists():
            n = len(sha.read_text().strip().split("\n"))
            print(f"   🔐 SHA256SUMS: {n} entries")
        print()

    # Disk usage
    result = subprocess.run(["du", "-sh", str(DATA_RAW)], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"💾 Total disk usage: {result.stdout.strip().split()[0]}")

    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())