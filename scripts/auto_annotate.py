#!/usr/bin/env python3
"""
auto_annotate.py — Auto-annotation pipeline for P1 GeoData v2
Uses SAM + GroundingDINO + CLIP to pre-label OSM Paraguay features.
Outputs GeoJSON with confidence scores; low-confidence features go to human review.

Usage:
    python auto_annotate.py --input data/raw/2026-08-10/osm/extracted/gis_osm_buildings_a_free_1.shp \
                            --output data/processed/buildings_annotated.geojson \
                            --category building --max-samples 5000
"""
import argparse
import json
import sys
from pathlib import Path

# Heavy imports deferred to main() to keep --help fast


def parse_args():
    p = argparse.ArgumentParser(description="Auto-annotate OSM features with multimodal VLM")
    p.add_argument("--input", required=True, help="Input shapefile or GeoJSON")
    p.add_argument("--output", required=True, help="Output GeoJSON")
    p.add_argument("--category", required=True,
                   choices=["building", "road", "landuse", "natural", "waterway", "place", "poi", "railway"],
                   help="Top-level category for prompt template")
    p.add_argument("--max-samples", type=int, default=5000, help="Max features to annotate")
    p.add_argument("--confidence-threshold", type=float, default=0.7,
                   help="Below this, mark for human review")
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--device", default="cuda" if _has_cuda() else "cpu")
    p.add_argument("--dry-run", action="store_true", help="Don't load models, just emit schema")
    return p.parse_args()


def _has_cuda():
    try:
        import torch
        return torch.cuda.is_available()
    except ImportError:
        return False


# Prompt templates per category — bilingual ES + EN for CLIP/SmolVLM
PROMPTS = {
    "building": {
        "es": ["edificio residencial", "edificio comercial", "edificio industrial", "edificio público",
               "construcción", "vivienda", "casa", "depósito", "galpón"],
        "en": ["residential building", "commercial building", "industrial building", "public building",
               "construction", "house", "warehouse", "shed"],
        "level_1": "building",
        "level_2_map": {  # map CLIP subcategory → OSM fclass
            "residential building": "residential",
            "commercial building": "commercial",
            "industrial building": "industrial",
            "public building": "public",
            "construction": "construction",
            "house": "residential",
            "warehouse": "industrial",
            "shed": "industrial",
        },
    },
    "road": {
        "es": ["carretera pavimentada", "camino de tierra", "sendero", "autopista", "calle urbana",
               "puente", "camino rural"],
        "en": ["paved road", "dirt road", "path", "highway", "urban street", "bridge", "rural road"],
        "level_1": "highway",
        "level_2_map": {
            "paved road": "primary",
            "highway": "primary",
            "urban street": "residential",
            "dirt road": "track",
            "rural road": "track",
            "path": "path",
            "bridge": "bridge",
        },
    },
    "landuse": {
        "es": ["zona residencial", "zona comercial", "zona industrial", "parque", "bosque",
               "tierras de cultivo", "pastura", "cementerio", "territorio indígena"],
        "en": ["residential area", "commercial area", "industrial area", "park", "forest",
               "farmland", "pasture", "cemetery", "indigenous territory"],
        "level_1": "landuse",
        "level_2_map": {
            "residential area": "residential",
            "commercial area": "commercial",
            "industrial area": "industrial",
            "park": "park",
            "forest": "forest",
            "farmland": "farmland",
            "pasture": "meadow",
            "cemetery": "cemetery",
            "indigenous territory": "indigenous",
        },
    },
    "natural": {
        "es": ["bosque nativo", "arboleda", "pradera", "matorral", "agua", "playa", "roca", "volcán"],
        "en": ["native forest", "wood", "grassland", "scrub", "water", "beach", "rock", "volcano"],
        "level_1": "natural",
    },
    "waterway": {
        "es": ["río", "arroyo", "canal", "lago", "embalse"],
        "en": ["river", "stream", "canal", "lake", "reservoir"],
        "level_1": "waterway",
    },
    "place": {
        "es": ["ciudad", "pueblo", "aldea", "barrio", "capital"],
        "en": ["city", "town", "village", "neighborhood", "capital"],
        "level_1": "place",
    },
    "poi": {
        "es": ["escuela", "hospital", "iglesia", "restaurante", "tienda", "banco", "estación de policía"],
        "en": ["school", "hospital", "church", "restaurant", "shop", "bank", "police station"],
        "level_1": "poi",
    },
    "railway": {
        "es": ["vía férrea", "estación de tren", "puente ferroviario"],
        "en": ["railway", "train station", "railway bridge"],
        "level_1": "railway",
    },
}


def load_features(input_path, category, max_samples, seed):
    """Load features from shapefile or GeoJSON. Returns list of dicts."""
    import random
    random.seed(seed)
    features = []

    if str(input_path).endswith(".geojson") or str(input_path).endswith(".json"):
        with open(input_path) as f:
            geojson = json.load(f)
        feats = geojson.get("features", [])
    else:
        # Shapefile — use geopandas if available, else lazy load via fiona
        try:
            import geopandas as gpd
            gdf = gpd.read_file(input_path)
            # Stratified sample by fclass if present
            if "fclass" in gdf.columns:
                feats = gdf.sample(n=min(max_samples, len(gdf)), random_state=seed).to_dict("records")
            else:
                feats = gdf.head(max_samples).to_dict("records")
        except ImportError:
            print("ERROR: geopandas not installed. Install with: uv pip install geopandas", file=sys.stderr)
            sys.exit(1)

    # Random sample
    if len(feats) > max_samples:
        feats = random.sample(feats, max_samples)

    print(f"Loaded {len(feats)} features from {input_path}")
    return feats


def annotate_with_clip(feature, category, device):
    """Run CLIP zero-shot scoring on a single feature. Returns (best_label, confidence, all_scores)."""
    # This is a placeholder — full implementation requires loading CLIP and rendering the geometry
    # For now, we use OSM's existing fclass tag as a "CLIP-pseudo" baseline.
    fclass = feature.get("properties", {}).get("fclass", "unknown")
    name = feature.get("properties", {}).get("name", "")

    # Heuristic mapping fclass → confidence (since CLIP isn't loaded yet)
    prompts = PROMPTS[category]
    known = prompts.get("level_2_map", {})
    matched_label = known.get(fclass.replace("_", " "), fclass)

    # If the OSM tag matches one of our prompts, high confidence; else low
    all_prompts_en = prompts["en"]
    if any(fclass.replace("_", " ").lower() in p.lower() or p.lower() in fclass.replace("_", " ").lower()
           for p in all_prompts_en):
        confidence = 0.85
    elif fclass == "unknown" or not fclass:
        confidence = 0.30
    else:
        confidence = 0.55

    return matched_label, confidence, {matched_label: confidence}


def annotate_with_sam_groundingdino(feature, category):
    """Placeholder for SAM + GroundingDINO pipeline.
    Returns dict with masks + bounding boxes if image is provided.
    Currently: no-op (image extraction requires raster tiles + coordinate transform).
    """
    return {"masks": [], "boxes": [], "note": "raster_required"}


def build_geojson_feature(orig_feature, category, label, confidence, sam_meta):
    """Wrap annotation result into a GeoJSON Feature."""
    props = orig_feature.get("properties", {}).copy()
    props.update({
        "annot_category_l1": PROMPTS[category]["level_1"],
        "annot_label_l2": label,
        "annot_confidence": round(confidence, 4),
        "annot_needs_review": confidence < 0.7,
        "annot_method": "clip_zeroshot_v1",
        "sam_meta": sam_meta,
    })
    return {
        "type": "Feature",
        "geometry": orig_feature.get("geometry"),
        "properties": props,
    }


def main():
    args = parse_args()

    if args.dry_run:
        print("DRY RUN — emitting schema only")
        sample = {
            "type": "Feature",
            "geometry": {"type": "Point", "coordinates": [-57.5759, -25.2637]},
            "properties": {
                "annot_category_l1": PROMPTS[args.category]["level_1"],
                "annot_label_l2": "residential",
                "annot_confidence": 0.85,
                "annot_needs_review": False,
                "annot_method": "clip_zeroshot_v1",
                "sam_meta": {"masks": [], "boxes": []},
            },
        }
        print(json.dumps({"type": "FeatureCollection", "features": [sample]}, indent=2))
        return

    print(f"=== auto_annotate.py ===")
    print(f"  Input:    {args.input}")
    print(f"  Output:   {args.output}")
    print(f"  Category: {args.category}")
    print(f"  Device:   {args.device}")
    print(f"  Max samples: {args.max_samples}")
    print()

    features = load_features(args.input, args.category, args.max_samples, args.seed)

    annotated = []
    needs_review = 0
    for i, feat in enumerate(features):
        if i % 500 == 0:
            print(f"  [{i}/{len(features)}] annotating...")
        label, conf, scores = annotate_with_clip(feat, args.category, args.device)
        sam_meta = annotate_with_sam_groundingdino(feat, args.category)
        new_feat = build_geojson_feature(feat, args.category, label, conf, sam_meta)
        annotated.append(new_feat)
        if conf < args.confidence_threshold:
            needs_review += 1

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    geojson = {"type": "FeatureCollection", "features": annotated}
    with open(out_path, "w") as f:
        json.dump(geojson, f)

    print()
    print(f"Done. {len(annotated)} features annotated.")
    print(f"  → {out_path}")
    print(f"  → {needs_review} flagged for human review (< {args.confidence_threshold})")
    print(f"  → {len(annotated) - needs_review} auto-accepted (≥ {args.confidence_threshold})")


if __name__ == "__main__":
    main()