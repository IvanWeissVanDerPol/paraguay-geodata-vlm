"""Test real annotation via venv python."""
import sys
sys.path.insert(0, '/opt/data/thesis-active/scripts')
from auto_annotate import PROMPTS, annotate_with_clip, build_geojson_feature
import geopandas as gpd
import json
from pathlib import Path
from collections import Counter

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            import numpy as np
            if isinstance(obj, np.integer):
                return int(obj)
            if isinstance(obj, np.floating):
                return float(obj)
            if isinstance(obj, np.ndarray):
                return obj.tolist()
        except ImportError:
            pass
        if hasattr(obj, '__geo_interface__'):
            return obj.__geo_interface__
        if hasattr(obj, 'isoformat'):
            return obj.isoformat()
        return str(obj)

print("Reading OSM buildings shapefile...")
shp = '/opt/data/thesis-active/data/raw/2026-08-10/osm/extracted/gis_osm_buildings_a_free_1.shp'
gdf = gpd.read_file(shp)
print(f"Loaded {len(gdf):,} buildings")
print(f"Columns: {list(gdf.columns)}")
print(f"CRS: {gdf.crs}")
print(f"\nfclass distribution (top 10):")
print(gdf['fclass'].value_counts().head(10))

sample = gdf.sample(n=100, random_state=42)
print(f"\nAnnotating {len(sample)} buildings with CLIP zero-shot baseline...")

annotated = []
for i, (_, row) in enumerate(sample.iterrows()):
    feat = {"properties": dict(row), "geometry": row.geometry.__geo_interface__}
    label, conf, scores = annotate_with_clip(feat, "building", "cpu")
    new_feat = build_geojson_feature(feat, "building", label, conf, {"masks": [], "boxes": []})
    annotated.append(new_feat)

out_path = Path('/opt/data/thesis-active/data/processed/buildings_sample_annotated.geojson')
out_path.parent.mkdir(parents=True, exist_ok=True)
with open(out_path, 'w') as f:
    json.dump({"type": "FeatureCollection", "features": annotated}, f, cls=NumpyEncoder)

needs_review = sum(1 for f in annotated if f['properties']['annot_needs_review'])
print(f"\nWrote {len(annotated)} features to {out_path}")
print(f"  {needs_review} need human review (confidence < 0.7)")
print(f"  {len(annotated) - needs_review} auto-accepted")

ann_labels = Counter(f['properties']['annot_label_l2'] for f in annotated)
print(f"\nAnnotation distribution:")
for label, n in ann_labels.most_common():
    print(f"  {label:<25} {n:>3}")

print(f"\nSample feature (first one):")
print(json.dumps(annotated[0], indent=2, default=str)[:600])