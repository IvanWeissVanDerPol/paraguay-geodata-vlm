# IMPRIMIR_TODO — Comando único para generar PDF consolidado

> **Propósito:** convertir los 3 documentos del paquete MOPC en un único PDF listo para imprimir.
> **Tiempo:** ~5-15 segundos (depende del motor LaTeX).

---

## Opción A — pandoc + xelatex (recomendado, mejor calidad tipográfica)

```bash
cd /opt/data/thesis-active/Defensa/MOPC_FILING_PACKET/
pandoc \
  --pdf-engine=xelatex \
  -V geometry:margin=2.5cm \
  -V geometry:top=3cm \
  -V fontsize=11pt \
  -V mainfont="DejaVu Sans" \
  -V monofont="DejaVu Sans Mono" \
  -V lang=es \
  -V titlepage=true \
  -V colorlinks=true \
  -V linkcolor=blue \
  -V urlcolor=blue \
  -V toccolor=black \
  -o MOPC_SOLICITUD_2026.pdf \
  MOPC_CARTA_DE_SALIDA.md \
  SFP_020_FORMULARIO.md \
  ANEXO_TECNICO.md
```

**Requisitos:**
- pandoc ≥ 3.1 (verificar con `pandoc --version`)
- TeX Live con xelatex (en macOS: `brew install --cask mactex`; en Ubuntu: `sudo apt install texlive-xetex texlive-fonts-recommended texlive-lang-spanish`)
- Fuente DejaVu Sans (incluida en Linux por defecto; en macOS: `brew install --cask font-dejavu-sans`)

---

## Opción B — pandoc + wkhtmltopdf (más rápido, menor calidad)

```bash
cd /opt/data/thesis-active/Defensa/MOPC_FILING_PACKET/
pandoc \
  --pdf-engine=wkhtmltopdf \
  -V margin-top=25mm \
  -V margin-bottom=25mm \
  -V margin-left=25mm \
  -V margin-right=25mm \
  -V fontsize=11pt \
  --metadata lang=es \
  -o MOPC_SOLICITUD_2026.pdf \
  MOPC_CARTA_DE_SALIDA.md \
  SFP_020_FORMULARIO.md \
  ANEXO_TECNICO.md
```

---

## Opción C — WeasyPrint + Python (sin LaTeX, ideal para servidores)

```bash
cd /opt/data/thesis-active/Defensa/MOPC_FILING_PACKET/
pip install weasyprint markdown
python3 scripts/render_mopc_pdf.py
```

Donde `scripts/render_mopc_pdf.py` es:

```python
#!/usr/bin/env python33
"""Render MOPC filing packet to a single PDF via WeasyPrint."""
from pathlib import Path
from weasyprint import HTML, CSS

base = Path("/opt/data/thesis-active/Defensa/MOPC_FILING_PACKET")
files = [
    base / "MOPC_CARTA_DE_SALIDA.md",
    base / "SFP_020_FORMULARIO.md",
    base / "ANEXO_TECNICO.md",
]
combined = "\n\n\\pagebreak\n\n".join(f.read_text(encoding="utf-8") for f in files)

css = CSS(string="""
@page { size: A4; margin: 2.5cm; }
body { font-family: 'DejaVu Sans', sans-serif; font-size: 11pt; line-height: 1.5; }
h1 { page-break-before: always; margin-top: 0; }
h2 { margin-top: 1.5em; }
table { border-collapse: collapse; width: 100%; margin: 1em 0; }
th, td { border: 1px solid #888; padding: 6pt; text-align: left; vertical-align: top; }
th { background: #eee; }
code { background: #f4f4f4; padding: 1pt 4pt; border-radius: 3pt; }
pre { background: #f4f4f4; padding: 8pt; border-radius: 4pt; }
blockquote { border-left: 4pt solid #888; padding-left: 12pt; color: #444; }
""")

HTML(string=combined, base_url=str(base)).write_pdf(
    str(base / "MOPC_SOLICITUD_2026.pdf"),
    stylesheets=[css],
)
print(f"PDF escrito: {base / 'MOPC_SOLICITUD_2026.pdf'}")
```

---

## Opción D — Solo imprimir los .md sueltos (sin consolidar)

Si preferís imprimir cada documento por separado (recomendable si querés firmar el SFP-020 sin firmar también la carta y el Anexo):

```bash
# Cada documento como PDF independiente
cd /opt/data/thesis-active/Defensa/MOPC_FILING_PACKET/

for f in MOPC_CARTA_DE_SALIDA.md SFP_020_FORMULARIO.md ANEXO_TECNICO.md; do
  base="${f%.md}"
  pandoc --pdf-engine=xelatex \
    -V geometry:margin=2.5cm \
    -V fontsize=11pt \
    -V mainfont="DejaVu Sans" \
    -V lang=es \
    -o "${base}.pdf" \
    "$f"
done

ls -la *.pdf
```

---

## Verificación post-impresión

Después de ejecutar el comando de tu preferencia, verificá:

```bash
ls -la MOPC_SOLICITUD_2026.pdf   # debe existir y pesar > 50 KB
file MOPC_SOLICITUD_2026.pdf     # debe decir "PDF document"
pdfinfo MOPC_SOLICITUD_2026.pdf  # debe mostrar ~14 páginas
```

Si todo está OK, el PDF está listo para imprimir en una impresora láser A4.

---

*Comando generado por Erebus (agente autónomo de Iván) bajo licencia MIT.*