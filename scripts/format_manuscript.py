#!/usr/bin/env python3
"""
format_manuscript.py — Normalize all Cap*.md headers per the UNA-FADA template.

What it does
------------
1. Reads every `Capitulos/CapN_*.md` (N = 1..6).
2. Rewrites the header block (lines 1 through `---`) so all chapters share
   the same canonical UNA-FADA template:

       # Capítulo N — <Title>

       **Tesis:** *<canonical title>*
       **Autor:** Iván Weiss Van der Pol
       **Carrera:** Maestría en Tecnología de la Arquitectura, FADA-UNA (co-afiliación FP-UNA)
       **Director (TBD):** Prof. Dr. Juan Carlos Cristaldo (FADA-UNA)
       **Fecha:** Agosto 2026
       **Versión:** 1.0 — borrador

       ---

3. Validates section numbering: every `## N.M.` must start with the chapter
   number N. Reports any mismatch.
4. Emits `Capitulos/INDEX.md` with the chapter list, word counts, and section
   counts so Iván can see the manuscript shape at a glance.
5. Emits `Capitulos/MANIFEST.md` summarizing the canonical title, the
   director, the institution, and the version policy — useful when handing
   the manuscript to a third party.

Run
---
    make format-manuscript          # writes files in-place (idempotent)
    make format-manuscript-check    # dry-run, only validates

Why this exists
---------------
The original chapters were drafted independently and drifted:
- Cap1 had the early paper-first long title; Cap2-6 use the shorter canonical title.
- Cap1 had "Tutora/or propuesta" wording; the others use "Director (TBD)".
- Cap2 lacks a `Versión:` line; the others have one.
- Cap3's title is on the same line as `**Tesis:**`; the others have a blank
  line between `# Capítulo` and `**Tesis:**`.

Per AUTONOMY.md "Format manuscript per UNA-FADA template" (T112), the
manuscript must be internally consistent before Iván walks it into FADA.
This script enforces that consistency without altering body content.
"""
from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CAP_DIR = ROOT / "Capitulos"

CANONICAL_TITLE = (
    "Anotación semiautomática del corpus cartográfico abierto de Paraguay "
    "con modelos multimodales fundacionales y una interfaz conversacional "
    "para la reflexión territorial"
)
CANONICAL_AUTHOR = "Iván Weiss Van der Pol"
CANONICAL_CARRERA = (
    "Maestría en Tecnología de la Arquitectura, FADA-UNA (co-afiliación FP-UNA)"
)
CANONICAL_DIRECTOR = "Prof. Dr. Juan Carlos Cristaldo (FADA-UNA)"
CANONICAL_FECHA = "Agosto 2026"
CANONICAL_VERSION = "1.0 — borrador"

# Chapters we know about, in canonical order. Cap4 is blocked upstream; the
# formatter still produces a slot for it.
CHAPTERS = [
    (1, "Introducción", "Cap1_Introduccion.md"),
    (2, "Marco Teórico", "Cap2_Marco_Teorico.md"),
    (3, "Marco Metodológico", "Cap3_Metodologia.md"),
    # Cap4 (Resultados) is intentionally absent: blocked on real experiment
    # numbers until M2-M4 GPU-bound tasks complete.
    (4, "Resultados", "Cap4_Resultados.md"),
    (5, "Discusión", "Cap5_Discusion.md"),
    (6, "Conclusiones", "Cap6_Conclusiones.md"),
]


def build_header_block(chapter_num: int, chapter_title: str) -> str:
    """Return the canonical UNA-FADA header block for one chapter."""
    return (
        f"# Capítulo {chapter_num} — {chapter_title}\n"
        "\n"
        f"**Tesis:** *{CANONICAL_TITLE}*\n"
        f"**Autor:** {CANONICAL_AUTHOR}\n"
        f"**Carrera:** {CANONICAL_CARRERA}\n"
        f"**Director (TBD):** {CANONICAL_DIRECTOR}\n"
        f"**Fecha:** {CANONICAL_FECHA}\n"
        f"**Versión:** {CANONICAL_VERSION}\n"
        "\n"
        "---\n"
    )


SECTION_RE = re.compile(r"^##\s+(\d+)\.(\d+)\.?\s+(.+?)\s*$")


def split_header_and_body(text: str) -> tuple[str, str]:
    """Split a chapter file into (header_block, body).

    The header is everything from the start of the file through the first
    `---` separator. Body is everything after.
    """
    lines = text.splitlines(keepends=True)
    for i, line in enumerate(lines):
        if line.strip() == "---":
            header = "".join(lines[:i + 1])
            body = "".join(lines[i + 1 :])
            return header, body
    # No separator found — treat the whole file as header (anomaly).
    return text, ""


def validate_sections(body: str, chapter_num: int) -> list[str]:
    """Return a list of warnings for any section number that does not start
    with `chapter_num.M`."""
    warnings: list[str] = []
    for line in body.splitlines():
        m = SECTION_RE.match(line)
        if not m:
            continue
        sec_num = int(m.group(1))
        if sec_num != chapter_num:
            warnings.append(
                f"section starts with {sec_num}. but chapter is {chapter_num}: {line!r}"
            )
    return warnings


def word_count(text: str) -> int:
    # Strip code fences, inline code, and markdown link URLs before counting.
    cleaned = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    cleaned = re.sub(r"`[^`]*`", "", cleaned)
    cleaned = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", cleaned)
    cleaned = re.sub(r"^#+\s+", "", cleaned, flags=re.MULTILINE)
    return len(cleaned.split())


def format_one(chapter_num: int, chapter_title: str, filename: str, dry_run: bool) -> dict:
    path = CAP_DIR / filename
    report: dict = {
        "chapter": chapter_num,
        "title": chapter_title,
        "file": filename,
        "path": str(path.relative_to(ROOT)),
        "existed": path.exists(),
        "changes": [],
        "warnings": [],
        "words": 0,
    }

    if not path.exists():
        report["changes"].append("missing — would create stub")
        if not dry_run:
            path.write_text(
                build_header_block(chapter_num, chapter_title)
                + "\n## "
                + f"{chapter_num}.1. Pendiente\n\n"
                + f"_Este capítulo está bloqueado aguas arriba (ver TASK_QUEUE.md "
                + f"y PROGRESS.md). Se genera un stub para mantener la coherencia "
                + f"del manuscrito mientras se desbloquean los experimentos._\n",
                encoding="utf-8",
            )
        return report

    text = path.read_text(encoding="utf-8")
    header, body = split_header_and_body(text)
    new_header = build_header_block(chapter_num, chapter_title)

    if header != new_header:
        report["changes"].append("normalized header to canonical UNA-FADA block")
        if not dry_run:
            path.write_text(new_header + body, encoding="utf-8")

    report["warnings"].extend(validate_sections(body, chapter_num))
    report["words"] = word_count(body)
    return report


def write_index(reports: list[dict], dry_run: bool) -> Path:
    out = CAP_DIR / "INDEX.md"
    lines: list[str] = []
    lines.append("# Índice del Manuscrito — UNA-FADA")
    lines.append("")
    lines.append(
        "> **Generado automáticamente por `scripts/format_manuscript.py` "
        f"el {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}**"
    )
    lines.append("")
    lines.append(
        "Tabla de capítulos del manuscrito con conteo de palabras y secciones. "
        "Re-correr con `make format-manuscript` para regenerar."
    )
    lines.append("")
    lines.append("| # | Capítulo | Archivo | Palabras (cuerpo) | Estado |")
    lines.append("|---|---|---|---|---|")
    for r in reports:
        status = "✅ presente" if r["existed"] else "⚠️ stub"
        if r["warnings"]:
            status += " — ver warnings"
        lines.append(
            f"| {r['chapter']} | {r['title']} | `{r['file']}` | "
            f"{r['words']:,} | {status} |"
        )
    lines.append("")
    lines.append("## Versión canónica")
    lines.append("")
    lines.append(f"- **Título:** *{CANONICAL_TITLE}*")
    lines.append(f"- **Autor:** {CANONICAL_AUTHOR}")
    lines.append(f"- **Carrera:** {CANONICAL_CARRERA}")
    lines.append(f"- **Director (TBD):** {CANONICAL_DIRECTOR}")
    lines.append(f"- **Fecha:** {CANONICAL_FECHA}")
    lines.append(f"- **Versión:** {CANONICAL_VERSION}")
    lines.append("")
    if not dry_run:
        out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out


def write_manifest(reports: list[dict], dry_run: bool) -> Path:
    out = CAP_DIR / "MANIFEST.md"
    lines: list[str] = []
    lines.append("# MANUSCRIPT MANIFEST — UNA-FADA Tesis de Maestría")
    lines.append("")
    lines.append(
        "> Snapshot generado por `scripts/format_manuscript.py`. Útil para "
        "entregar a un director o comité TFG sin abrir cada capítulo."
    )
    lines.append("")
    lines.append("## Identidad del manuscrito")
    lines.append("")
    lines.append("| Campo | Valor |")
    lines.append("|---|---|")
    lines.append(f"| Título canónico | *{CANONICAL_TITLE}* |")
    lines.append(f"| Autor | {CANONICAL_AUTHOR} |")
    lines.append(f"| Carrera | {CANONICAL_CARRERA} |")
    lines.append(f"| Director (TBD) | {CANONICAL_DIRECTOR} |")
    lines.append(f"| Fecha de redacción | {CANONICAL_FECHA} |")
    lines.append(f"| Versión global | {CANONICAL_VERSION} |")
    lines.append("")
    lines.append("## Estructura")
    lines.append("")
    lines.append(
        "El manuscrito sigue la convención estándar de tesis FADA-UNA: "
        "Introducción → Marco Teórico → Marco Metodológico → Resultados → "
        "Discusión → Conclusiones. Cap4 (Resultados) está pendiente hasta que "
        "los experimentos M2-M4 (GPU-bound) y los datos Copernicus/Sentinel-2 "
        "estén disponibles."
    )
    lines.append("")
    total_words = sum(r["words"] for r in reports)
    lines.append(f"**Total palabras (cuerpo):** {total_words:,}.")
    lines.append("")
    lines.append("## Cómo regenerar")
    lines.append("")
    lines.append("```bash")
    lines.append("cd /opt/data/thesis-active")
    lines.append("source .venv/bin/activate")
    lines.append("make format-manuscript")
    lines.append("```")
    lines.append("")
    if not dry_run:
        out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out


def main() -> int:
    docstring = __doc__ or "Manuscript formatter"
    parser = argparse.ArgumentParser(description=docstring.split("\n", 1)[0])
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="only validate; do not write any files",
    )
    args = parser.parse_args()

    print("=" * 60)
    print("📐 Manuscript formatter — UNA-FADA template")
    print("=" * 60)
    print(f"Cap dir: {CAP_DIR}")
    print(f"Mode:    {'DRY-RUN (no writes)' if args.dry_run else 'WRITE'}")
    print()

    reports: list[dict] = []
    for chapter_num, chapter_title, filename in CHAPTERS:
        print(f"-- Capítulo {chapter_num} — {chapter_title} ({filename})")
        r = format_one(chapter_num, chapter_title, filename, args.dry_run)
        for change in r["changes"]:
            print(f"   change: {change}")
        for warn in r["warnings"]:
            print(f"   WARN:   {warn}")
        print(f"   words:  {r['words']:,}")
        reports.append(r)

    index_path = write_index(reports, args.dry_run)
    manifest_path = write_manifest(reports, args.dry_run)
    print()
    print(f"-- Wrote {index_path.relative_to(ROOT)} ({'would write' if args.dry_run else 'wrote'})")
    print(f"-- Wrote {manifest_path.relative_to(ROOT)} ({'would write' if args.dry_run else 'wrote'})")

    total_warnings = sum(len(r["warnings"]) for r in reports)
    total_changes = sum(len(r["changes"]) for r in reports)
    print()
    print(f"Summary: {total_changes} change(s), {total_warnings} warning(s).")
    if total_warnings and not args.dry_run:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())