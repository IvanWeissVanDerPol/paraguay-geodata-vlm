#!/usr/bin/env python3
"""
validate_creds.py — Validate secrets/creds.json against the schema.

Usage:
    python3 scripts/validate_creds.py [--strict]

In --strict mode, the script also rejects any FILL_ME_* placeholders that
should have been replaced (default: warns).

Exit codes:
    0 = valid
    1 = schema invalid
    2 = placeholders remaining (only --strict)
"""
import argparse
import json
import re
import sys
from pathlib import Path

try:
    import jsonschema
except ImportError:
    print("ERROR: jsonschema not installed. Run: uv pip install jsonschema")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
CREDS = ROOT / "secrets" / "creds.json"
SCHEMA = ROOT / "secrets" / "creds.schema.json"

FILL_ME_RE = re.compile(r"^FILL_ME_|^FILL_ME\s|\bskip\b$", re.IGNORECASE)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true",
                    help="Reject if any FILL_ME_ placeholders remain")
    args = ap.parse_args()

    if not CREDS.exists():
        print(f"❌ {CREDS} not found")
        sys.exit(1)
    if not SCHEMA.exists():
        print(f"❌ {SCHEMA} not found")
        sys.exit(1)

    creds = json.loads(CREDS.read_text())
    schema = json.loads(SCHEMA.read_text())

    print(f"🔍 Validating {CREDS.relative_to(ROOT)}")
    print(f"   Schema: {SCHEMA.relative_to(ROOT)}")
    print()

    # Validate schema (skip pattern checks when value is a placeholder)
    def is_placeholder(v):
        return isinstance(v, str) and (FILL_ME_RE.match(v.strip()) or v.strip().lower() == "skip")

    def deep_strip_patterns(obj, schema_node):
        """Recursively remove 'pattern' constraints from schema when value is placeholder."""
        if not isinstance(schema_node, dict):
            return schema_node
        new_node = dict(schema_node)
        # If obj is a placeholder string, drop pattern + minLength + maxLength constraints
        if is_placeholder(obj):
            for key in ("pattern", "minLength", "maxLength", "minimum", "maximum", "enum"):
                new_node.pop(key, None)
            return new_node
        # Recurse into nested object schemas
        for k, v in list(new_node.items()):
            if k == "properties" and isinstance(v, dict) and isinstance(obj, dict):
                new_props = {}
                for prop_name, prop_schema in v.items():
                    new_props[prop_name] = deep_strip_patterns(obj.get(prop_name), prop_schema)
                new_node[k] = new_props
            elif k == "items" and isinstance(obj, list):
                new_node[k] = deep_strip_patterns(obj[0] if obj else None, v)
        return new_node

    permissive_schema = deep_strip_patterns(creds, schema)

    try:
        jsonschema.validate(creds, permissive_schema)
        print("✅ Schema valid (patterns relaxed for placeholders)")
    except jsonschema.ValidationError as e:
        print(f"❌ Schema invalid: {e.message}")
        print(f"   Path: {'.'.join(str(p) for p in e.absolute_path)}")
        sys.exit(1)

    # Count placeholders
    placeholder_count = 0
    filled_count = 0
    skipped_count = 0

    def walk(obj, path=""):
        nonlocal placeholder_count, filled_count, skipped_count
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k.startswith("_"):
                    continue
                walk(v, f"{path}.{k}" if path else k)
        elif isinstance(obj, str):
            if FILL_ME_RE.match(obj.strip()):
                placeholder_count += 1
                # Walk up to find _priority hint
                priority = ""
                parts = path.split(".")
                if parts:
                    # Look for the service-level _priority
                    service_name = parts[0]
                    services_root = creds.get("services", {})
                    if service_name in services_root and isinstance(services_root[service_name], dict):
                        priority = services_root[service_name].get("_priority", "")
                print(f"  ⏳ {path}: placeholder ({priority or 'no priority info'})")
            elif obj.strip().lower() == "skip":
                skipped_count += 1
            else:
                filled_count += 1
        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                walk(item, f"{path}[{i}]")

    walk(creds)

    print()
    print(f"   Filled:      {filled_count}")
    print(f"   Placeholders: {placeholder_count}")
    print(f"   Skipped:      {skipped_count}")

    if placeholder_count > 0 and args.strict:
        print()
        print("❌ --strict: placeholders remaining. Replace or remove before proceeding.")
        sys.exit(2)

    if placeholder_count > 0:
        print()
        print("⚠️  Placeholders remaining. Fill them or set to 'skip' if not needed now.")
        print("   (OK to proceed in non-strict mode — Erebus will skip them.)")
    else:
        print()
        print("✅ All credentials filled. Ready to pass to Erebus.")

    sys.exit(0)


if __name__ == "__main__":
    main()