# MANUSCRIPT MANIFEST — UNA-FADA Tesis de Maestría

> Snapshot generado por `scripts/format_manuscript.py`. Útil para entregar a un director o comité TFG sin abrir cada capítulo.

## Identidad del manuscrito

| Campo | Valor |
|---|---|
| Título canónico | *Anotación semiautomática del corpus cartográfico abierto de Paraguay con modelos multimodales fundacionales y una interfaz conversacional para la reflexión territorial* |
| Autor | Iván Weiss Van der Pol |
| Carrera | Maestría en Tecnología de la Arquitectura, FADA-UNA (co-afiliación FP-UNA) |
| Director (TBD) | Prof. Dr. Juan Carlos Cristaldo (FADA-UNA) |
| Fecha de redacción | Agosto 2026 |
| Versión global | 1.0 — borrador |

## Estructura

El manuscrito sigue la convención estándar de tesis FADA-UNA: Introducción → Marco Teórico → Marco Metodológico → Resultados → Discusión → Conclusiones. Cap4 (Resultados) está pendiente hasta que los experimentos M2-M4 (GPU-bound) y los datos Copernicus/Sentinel-2 estén disponibles.

**Total palabras (cuerpo):** 20,794.

## Cómo regenerar

```bash
cd /opt/data/thesis-active
source .venv/bin/activate
make format-manuscript
```

