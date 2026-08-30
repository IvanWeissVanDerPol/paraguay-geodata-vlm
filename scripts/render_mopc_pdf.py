#!/usr/bin/env python3
"""Render MOPC filing packet to a single PDF via WeasyPrint.

Usage:
    python3 scripts/render_mopc_pdf.py

Reads:
    Defensa/MOPC_FILING_PACKET/MOPC_CARTA_DE_SALIDA.md
    Defensa/MOPC_FILING_PACKET/SFP_020_FORMULARIO.md
    Defensa/MOPC_FILING_PACKET/ANEXO_TECNICO.md

Writes:
    Defensa/MOPC_FILING_PACKET/MOPC_SOLICITUD_2026.pdf

This script is part of the T046a autonomous deliverable (MOPC filing packet).
License: MIT.
"""
from pathlib import Path

try:
    from weasyprint import HTML, CSS
    import markdown
except ImportError as e:
    raise SystemExit(
        "Missing dependency. Install with:\n"
        "  pip install weasyprint markdown\n"
        f"Original error: {e}"
    )

BASE = Path("/opt/data/thesis-active/Defensa/MOPC_FILING_PACKET")
SRC_FILES = [
    BASE / "MOPC_CARTA_DE_SALIDA.md",
    BASE / "SFP_020_FORMULARIO.md",
    BASE / "ANEXO_TECNICO.md",
]
OUT_PDF = BASE / "MOPC_SOLICITUD_2026.pdf"


def md_to_html(md_text: str) -> str:
    """Convert one markdown doc to standalone HTML."""
    return markdown.markdown(
        md_text,
        extensions=["tables", "fenced_code", "toc", "attr_list"],
        output_format="html",
    )


def main() -> None:
    html_parts = []
    for f in SRC_FILES:
        if not f.exists():
            raise SystemExit(f"Missing source file: {f}")
        html_parts.append(md_to_html(f.read_text(encoding="utf-8")))

    combined_html = (
        "<!doctype html><html lang='es'><head><meta charset='utf-8'>"
        "<title>Solicitud MOPC — Iván Weiss Van der Pol — UNA-FADA</title>"
        "</head><body>"
        + "\n<hr style='page-break-after: always'>\n".join(html_parts)
        + "</body></html>"
    )

    css = CSS(
        string="""
        @page { size: A4; margin: 2.5cm; }
        body { font-family: 'DejaVu Sans', sans-serif; font-size: 11pt; line-height: 1.5; color: #222; }
        h1 { page-break-before: always; margin-top: 0; font-size: 18pt; border-bottom: 2px solid #333; padding-bottom: 4pt; }
        h1:first-of-type { page-break-before: avoid; }
        h2 { margin-top: 1.5em; font-size: 14pt; }
        h3 { margin-top: 1.2em; font-size: 12pt; }
        table { border-collapse: collapse; width: 100%; margin: 1em 0; font-size: 10pt; }
        th, td { border: 1px solid #888; padding: 6pt; text-align: left; vertical-align: top; }
        th { background: #eee; font-weight: bold; }
        code { background: #f4f4f4; padding: 1pt 4pt; border-radius: 3pt; font-size: 10pt; }
        pre { background: #f4f4f4; padding: 8pt; border-radius: 4pt; font-size: 9pt; overflow: auto; }
        blockquote { border-left: 4pt solid #888; padding-left: 12pt; color: #444; margin: 1em 0; }
        hr { border: none; border-top: 1px dashed #aaa; margin: 2em 0; }
        """
    )

    HTML(string=combined_html, base_url=str(BASE)).write_pdf(
        str(OUT_PDF),
        stylesheets=[css],
    )
    print(f"PDF written: {OUT_PDF}")
    print(f"Size: {OUT_PDF.stat().st_size:,} bytes")


if __name__ == "__main__":
    main()