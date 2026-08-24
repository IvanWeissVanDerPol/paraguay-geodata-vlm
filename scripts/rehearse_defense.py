#!/usr/bin/env python3
"""
rehearse_defense.py — Cron-driven defense rehearsal tool.

Walks Iván through the 21-slide defense structure from Defensa/slides.html
using a per-slide timer, prompts, and a self-grading rubric. Logs each
rehearsal to data/rehearsal_log.jsonl for trend analysis over time.

Two modes:
  - `rehearse`  (default): interactive rehearsal with timer + prompts
  - `dry`: just print the 21-slide structure with per-block time budget
  - `report`: summarize past rehearsals (count, avg duration, weak slides)

Rehearsal structure follows Defensa/slides.html (21 sections, 6 bloques,
45 min + 15 min Q&A as per DEFENSE_PLAN.md).
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SLIDES = ROOT / "Defensa" / "slides.html"
REHEARSAL_LOG = ROOT / "data" / "rehearsal_log.jsonl"

# Bloque = block; each block has a target time budget (minutes).
# Total presentation target = 45 min. Q&A = 15 min. Defense = 60 min total.
BLOQUES = [
    {
        "n": 1,
        "name": "Contexto y motivación",
        "target_min": 8,
        "slides": [1, 2, 3, 4],
        "must_hit": [
            "Paraguay tiene 2.4M features OSM pero ~0% anotadas semánticamente",
            "Cristaldo genealogy (2019-2023) sin uso de foundation models",
            "Gap: primer trabajo que combina OSM Paraguay + VLM + interfaz conversacional",
        ],
    },
    {
        "n": 2,
        "name": "Marco teórico",
        "target_min": 5,
        "slides": [5, 6, 7],
        "must_hit": [
            "Cartografía del Sur Global (FADA Res. 1141/2022)",
            "Visión-lenguaje multimodal (CLIP, SAM, Florence-2)",
            "RAG para interfaces conversacionales",
        ],
    },
    {
        "n": 3,
        "name": "Metodología",
        "target_min": 10,
        "slides": [8, 9, 10],
        "must_hit": [
            "Pipeline de anotación (SAM → GroundingDINO → CLIP → revisión humana)",
            "Fine-tune de SmolVLM + Florence-2 con QLoRA",
            "Interfaz web (Next.js + Llama-3.1-8B + RAG)",
        ],
    },
    {
        "n": 4,
        "name": "Resultados",
        "target_min": 12,
        "slides": [11, 12, 13, 14, 15],
        "must_hit": [
            "Caracterización del corpus (tabla + figura)",
            "Inter-annotator κ = 0.87",
            "Modelo fine-tuned: F1 macro 0.78 vs CLIP-zero-shot 0.51",
            "Agente conversacional: 78% respuesta correcta",
            "Latencia p95 = 1.4s",
        ],
    },
    {
        "n": 5,
        "name": "Discusión + Contribuciones",
        "target_min": 5,
        "slides": [16, 17, 18],
        "must_hit": [
            "Contribuciones: dataset + modelo + app + paper",
            "Limitaciones: cobertura OSM rural, single-country",
            "Trabajo futuro: change detection temporal, transfer Bolivia/Uruguay",
        ],
    },
    {
        "n": 6,
        "name": "Cierre",
        "target_min": 5,
        "slides": [19, 20, 21],
        "must_hit": [
            "Repositorio público + DOI",
            "Agradecimientos (advisor + revisores + funding)",
            "Preguntas del tribunal",
        ],
    },
]

TOTAL_PRESENTATION_MIN = sum(b["target_min"] for b in BLOQUES)  # 45
QA_MIN = 15
TOTAL_DEFENSE_MIN = TOTAL_PRESENTATION_MIN + QA_MIN  # 60


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def cmd_dry() -> int:
    """Print the rehearsal structure with per-block time budgets."""
    print("=" * 72)
    print(f"DEFENSE REHEARSAL — {TOTAL_PRESENTATION_MIN} min presentation + {QA_MIN} min Q&A")
    print(f"Slides source: {SLIDES.relative_to(ROOT)}")
    print("=" * 72)
    for b in BLOQUES:
        print(
            f"\nBloque {b['n']} — {b['name']}  [{b['target_min']} min]"
        )
        print(f"  Slides: {b['slides']}")
        for must in b["must_hit"]:
            print(f"    ✓ {must}")
    print(
        f"\nTotal target: {TOTAL_PRESENTATION_MIN} min presentation + "
        f"{QA_MIN} min Q&A = {TOTAL_DEFENSE_MIN} min"
    )
    print(
        "\nRun `python3 scripts/rehearse_defense.py rehearse` for an interactive"
        " timed walkthrough."
    )
    return 0


def cmd_rehearse(non_interactive: bool = False) -> int:
    """Walk the speaker through the 21 slides with per-block timers."""
    print("=" * 72)
    print("DEFENSE REHEARSAL — INTERACTIVE")
    print(f"Target: {TOTAL_PRESENTATION_MIN} min presentation + {QA_MIN} min Q&A")
    print("=" * 72)
    print("\nPress ENTER to start each slide; Ctrl-C to abort.")
    print("(Timer measures wall-clock between ENTER presses.)\n")

    results = []
    start = time.time()
    try:
        for b in BLOQUES:
            print(f"\n--- Bloque {b['n']} — {b['name']} ({b['target_min']} min) ---")
            block_start = time.time()
            for slide in b["slides"]:
                input(f"\n[Slide {slide}] Press ENTER when you start presenting… ")
                slide_start = time.time()
                input(f"[Slide {slide}] Press ENTER when you finish… ")
                slide_dur = (time.time() - slide_start) / 60.0
                print(f"  → Slide {slide}: {slide_dur:.2f} min")
                results.append(
                    {
                        "slide": slide,
                        "bloque": b["n"],
                        "duration_min": round(slide_dur, 2),
                    }
                )
            block_dur = (time.time() - block_start) / 60.0
            over = block_dur - b["target_min"]
            status = "OK" if over <= 0 else f"OVER by {over:.2f} min"
            print(f"  Bloque {b['n']} total: {block_dur:.2f} min — {status}")
    except KeyboardInterrupt:
        print("\n\nRehearsal aborted by user.")
        return 130

    total_dur = (time.time() - start) / 60.0
    print("\n" + "=" * 72)
    print(f"PRESENTATION TOTAL: {total_dur:.2f} min (target {TOTAL_PRESENTATION_MIN})")
    print("=" * 72)

    over_min = total_dur - TOTAL_PRESENTATION_MIN
    if over_min > 2:
        print(f"⚠️  OVER TARGET by {over_min:.2f} min — trim weak slides.")
    elif over_min < -2:
        print(f"⚠️  UNDER TARGET by {-over_min:.2f} min — add depth to weak slides.")
    else:
        print("✓ Within ±2 min of target.")

    _log_rehearsal(
        {
            "timestamp": _now(),
            "type": "interactive",
            "total_min": round(total_dur, 2),
            "target_min": TOTAL_PRESENTATION_MIN,
            "delta_min": round(over_min, 2),
            "slides": results,
        }
    )
    return 0


def _log_rehearsal(entry: dict) -> None:
    REHEARSAL_LOG.parent.mkdir(parents=True, exist_ok=True)
    with REHEARSAL_LOG.open("a") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    print(f"\nLogged → {REHEARSAL_LOG.relative_to(ROOT)}")


def cmd_report() -> int:
    """Summarize past rehearsals from data/rehearsal_log.jsonl."""
    if not REHEARSAL_LOG.exists():
        print("No rehearsals logged yet. Run `rehearse_defense.py rehearse` first.")
        return 0
    rows = [json.loads(line) for line in REHEARSAL_LOG.read_text().splitlines() if line.strip()]
    if not rows:
        print("Log file empty.")
        return 0
    print("=" * 72)
    print(f"REHEARSAL REPORT — {len(rows)} sessions")
    print("=" * 72)
    durations = [r.get("total_min", 0.0) for r in rows]
    print(f"Avg duration: {sum(durations) / len(durations):.2f} min")
    print(f"Min duration: {min(durations):.2f} min")
    print(f"Max duration: {max(durations):.2f} min")
    print(f"Target:       {TOTAL_PRESENTATION_MIN} min")

    # Per-slide trend if we have slide-level data
    slide_totals: dict[int, list[float]] = {}
    for r in rows:
        for s in r.get("slides", []):
            slide_totals.setdefault(s["slide"], []).append(s["duration_min"])
    if slide_totals:
        print("\nPer-slide avg duration:")
        for slide in sorted(slide_totals):
            vals = slide_totals[slide]
            avg = sum(vals) / len(vals)
            print(f"  Slide {slide:2d}: {avg:.2f} min (n={len(vals)})")
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        prog="rehearse_defense.py",
        description="Defense rehearsal tool for FADA-UNA thesis defense.",
    )
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("dry", help="print structure + time budgets only")
    sub.add_parser("rehearse", help="interactive timed walkthrough")
    sub.add_parser("report", help="summarize past rehearsals")
    args = p.parse_args(argv)

    if args.cmd == "dry":
        return cmd_dry()
    if args.cmd == "rehearse":
        return cmd_rehearse()
    if args.cmd == "report":
        return cmd_report()
    p.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
