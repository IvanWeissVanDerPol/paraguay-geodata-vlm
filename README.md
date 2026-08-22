# 🎓 P1 GeoData v2 — Tesis de Maestría (paper-first)

**Author:** Iván Weiss Van der Pol
**Estrategia:** Paper-first, advisor-last, sin burocracia
**Status:** Fase 0 (mes 1-7) — construcción sin advisor
**Last updated:** 2026-08-10

---

## ⚡ Quick start (si ya tenés todo instalado)

```bash
cd /opt/data/thesis-active
source .venv/bin/activate
make status       # check current state
make tick         # run one autonomous work tick (or wait for 06:00 UTC cron)
```

Si `make status` muestra tasks en progreso o completados, Erebus ya está trabajando.

---

## 📑 Documentos (leé en este orden)

| # | Documento | Tiempo | Para qué |
|---|---|---|---|
| 1 | **`THESIS_ARCHITECTURE.md`** | 5 min | **Leé esto primero.** Mapa cross-repo (este repo = sustrato; satellite-paraguay = tesis). |
| 2 | **`AUTONOMY.md`** | 5 min | Cómo Erebus trabaja 24/7 sin prompting |
| 3 | **`QUICKREF.md`** | 2 min | Cheat sheet, comandos diarios |
| 4 | **`SETUP_GUIDE.md`** | 15 min | Instalación + credenciales |
| 5 | **`TASK_QUEUE.md`** | 10 min | Las 87 tasks que Erebus ejecuta |
| 6 | **`PROGRESS.md`** | 5 min | Log de lo que ya se hizo |
| 7 | **`THESIS_PICK.md`** | 10 min | Por qué P1 GeoData v2 (contexto histórico) |
| 8 | **`FORMAL_PROPOSAL.md`** | 15 min | Pregunta + hipótesis + objetivos |
| 9 | **`ETHICS_WAIVER_MEMO.md`** | 5 min | Sin IRB justificado |
| 10 | **`DATA_MANIFEST.md`** | 10 min | 9 datasets + licencias |
| 11 | **`METHODOLOGY.md`** | 30 min | Cap. 3 metodología |
| 12 | **`PAPER_OUTLINE.md`** | 20 min | Paper ICA/SIGSPATIAL |
| 13 | **`BENCHMARK_QUESTIONS.md`** | 15 min | 100 preguntas validación |
| 14 | **`DEFENSE_PLAN.md`** | 20 min | Defensa + advisor strategy |
| 15 | **`RISK_REGISTER.md`** | 10 min | 35 riesgos categorizados |
| 16 | **`REFERENCES.bib`** | — | BibTeX starter |

> 📌 Si venís de satellite-paraguay: THESIS_ARCHITECTURE.md explica cómo se conecta con la otra mitad. Si te interesa la mitad "papel/modelo", andá a `IvanWeissVanDerPol/satellite-paraguay`.

---

## 📂 Estructura del proyecto

```
thesis-active/
├── README.md                  ← este archivo
├── QUICKREF.md                ← cheat sheet
├── SETUP_GUIDE.md             ← install + credentials
├── THESIS_PICK.md             ← decisión P1
├── FORMAL_PROPOSAL.md         ← pregunta + hipótesis
├── ETHICS_WAIVER_MEMO.md      ← sin IRB
├── DATA_MANIFEST.md           ← datasets
├── METHODOLOGY.md             ← Cap. 3
├── PAPER_OUTLINE.md           ← paper
├── BENCHMARK_QUESTIONS.md     ← 100 preguntas
├── DEFENSE_PLAN.md            ← defensa + advisor
├── RISK_REGISTER.md           ← riesgos
├── REFERENCES.bib             ← BibTeX
├── Makefile                   ← 30+ comandos
├── docker-compose.yml         ← full stack
├── requirements.txt           ← Python deps
├── .env.example               ← env template
├── .gitignore                 ← seguridad
├── secrets/
│   ├── README.md              ← cómo pasar credenciales
│   ├── creds.json             ← (Iván llena)
│   └── creds.schema.json      ← validación
├── scripts/
│   ├── install.sh             ← bootstrap
│   ├── sanity_check.py        ← verify
│   ├── validate_creds.py      ← check creds
│   ├── load_creds.py          ← load to env
│   ├── fetch_data.sh          ← download
│   ├── data_status.py         ← inventory
│   ├── auto_annotate.py       ← annotation
│   └── test_annotate.py       ← smoke test
└── data/
    ├── raw/2026-08-10/
    │   └── osm/               ← OSM Paraguay 1.2 GB
    └── processed/             ← outputs
        └── buildings_sample_annotated.geojson  ← 100 features
```

---

## 🎯 Resumen ejecutivo

**Pregunta:** ¿Es viable anotar semánticamente el corpus cartográfico abierto de Paraguay con modelos visión-lenguaje multimodales (CLIP, SAM, Florence-2, SmolVLM) alcanzando κ ≥ 0.85 inter-anotador, y construir una interfaz conversacional en español paraguayo que responda preguntas territoriales con ≥ 75% de acierto?

**Método:** Pipeline SAM → GroundingDINO → CLIP → revisión humana sobre ~10K features OSM Paraguay; fine-tune de SmolVLM-256M + Florence-2-base; aplicación web Next.js + Llama-3.1-8B con RAG.

**Output esperado:**
- Dataset (10K features anotadas, CC BY 4.0)
- Modelo fine-tuneado (Hugging Face Hub)
- App web pública (`paraguay-mapa.paragu-ai.com`)
- Paper en ICA 2027 / ACM SIGSPATIAL 2027 / arxiv
- Manuscrito completo para defensa UNA-FADA

**Tiempo a arxiv:** ~7 meses
**Tiempo a defensa UNA:** ~12 meses
**Costo total:** ~$200-800 (GPU rentada + dominio + hosting)
**Burocracia:** 0 (sin sujetos humanos, sin IRB)

---

## 🛠️ Stack instalado

### Python (80+ paquetes)

| Categoría | Paquetes clave |
|---|---|
| Geospatial | numpy 2.5, pandas 3.0, geopandas 1.1, shapely 2.1, rasterio 1.5 |
| Deep Learning | torch 2.13 (CPU), transformers 5.14, accelerate, peft, trl |
| Vision-Language | open-clip-torch 3.3, ultralytics 8.4, supervision |
| LLM / RAG | langchain 1.3, chromadb 1.5, faiss-cpu, sentence-transformers |
| Dev tools | pytest, black, ruff, mypy, jupyter |
| Validation | jsonschema 4.26, huggingface_hub 1.27 |

### CLI tools

| Tool | Status |
|---|---|
| git 2.47 | ✅ |
| docker 26.1 | ✅ |
| curl 8.14 | ✅ |
| hf (HuggingFace CLI) 1.27 | ✅ |
| jq | ❌ (needs sudo, not blocking) |
| ogrinfo | ❌ (needs sudo, not blocking) |

### Data downloaded

| Dataset | Status | Size |
|---|---|---|
| OSM Paraguay shapefiles | ✅ | 1.2 GB (2.46M features) |
| IGN raster | ⏳ | needs WMS pull |
| Sentinel-2 | ⏳ | needs Copernicus creds |
| WorldPop | ⏳ | needs download |
| Open Buildings | ⏳ | needs GCP creds |
| INDI territories | ⏳ | needs download |
| CHIRPS | ⏳ | needs download |
| MOPC drones | ⏳ | needs access request |

---

## 🚦 Estado actual (semana 0)

| Item | Status | Note |
|---|---|---|
| Tema elegido | ✅ | P1 GeoData v2 |
| Pregunta + hipótesis | ✅ | H1, H2, H3 |
| Marco ético | ✅ | sin IRB |
| Data manifest | ✅ | 9 datasets |
| OSM Paraguay | ✅ | 2.46M features |
| Annotation pipeline | ✅ | CLIP zero-shot baseline functional |
| Methodology Cap. 3 | ✅ | completo |
| Paper outline | ✅ | abstract + 7 sections |
| 100-question benchmark | ✅ | redactadas |
| Defense plan | ✅ | slides + Q&A |
| Risk register | ✅ | 35 riesgos |
| References | ✅ | 24 BibTeX |
| Sentinel-2 | ⏳ | waiting for Copernicus creds |
| Fine-tune | ⏳ | month 4-5 |
| Web app | ⏳ | month 5-6 |
| arxiv | ⏳ | month 7 |
| Advisor contact | ⏳ | month 7-8 |
| Defensa UNA | ⏳ | month 12 |

---

## 🤖 Trabajo autónomo (sin prompting)

Erebus trabaja 24/7 sin que tengas que pedirle. El sistema:

1. **Daily tick (06:00 UTC)** — corre `scripts/autonomous_tick.py`, elige la próxima tarea P0 de `TASK_QUEUE.md`, la ejecuta, la marca como done, escribe a `PROGRESS.md` y `data/progress.jsonl`.
2. **Weekly review (Domingo 18:00 UTC)** — corre `scripts/weekly_review.py`, calcula stats, identifica blockers, escribe resumen semanal.
3. **Git maintenance (Domingo 23:00 UTC)** — corre `scripts/git_maintenance.sh`, gc + prune + reflog + fsck.
4. **Skill `thesis-active-autonomy`** — cuando iniciás una sesión nueva, Erebus carga el contexto completo y sigue donde quedó.

**Auto-commit:** cada tick se commitea atómicamente con conventional commits. Erebus **nunca pushea** — vos decidís cuándo.

**Para chequear progreso:**

```bash
cd /opt/data/thesis-active
make status       # estado actual de las 87 tasks
make tick-dry     # ver qué task elegiría el próximo tick
make weekly       # resumen estratégico (Domingos)
make git-log      # commits recientes
```

**Para sincronizar con GitHub:**

```bash
make git-first-push      # primer push (solo la primera vez)
make git-sync            # fetch + rebase + status (safe, sin push)
make git-push            # push tus commits a GitHub
make git-resolve         # auto-resolver conflictos (PROGRESS/TASK_QUEUE/RISK)
```

**Para intervenir en el queue:**

```bash
make tick-claim TASK_ID=T042       # claim una task específica
make tick-complete TASK_ID=T042 OUTPUT="..." NOTES="..."  # marcar done
make tick-blocked TASK_ID=T042 OUTPUT="..." NOTES="..."   # marcar bloqueada
```

Ver `AUTONOMY.md` para el sistema autónomo completo, `GIT_WORKFLOW.md` para git.

---

## 🤝 Credentials needed

| Service | Priority | URL |
|---|---|---|
| HuggingFace | P0 | https://huggingface.co/settings/tokens |
| GitHub | P0 | https://github.com/settings/tokens |
| Copernicus | P0 | https://dataspace.copernicus.eu/ |
| AWS (optional) | P1 | https://aws.amazon.com/free/ |
| Google Cloud (optional) | P1 | https://console.cloud.google.com/ |
| Cloudflare R2 (optional) | P2 | https://dash.cloudflare.com/ |
| arXiv (later) | P2 | https://arxiv.org/register |
| Zenodo (later) | P2 | https://zenodo.org/signup |

**Cómo pasar credenciales a Erebus:**

1. Llenar `secrets/creds.json` con valores reales
2. `make validate-creds` para verificar
3. `make lock-perms` para asegurar permisos
4. Pegar el JSON en Mensaje a Erebus

Ver `secrets/README.md` para detalles completos.

---

## 📜 Licencia

- **Datos OSM:** ODbL 1.0
- **Datos IGN/Sentinel/CHIRPS:** public domain
- **Datos CC BY:** CC BY 4.0
- **Código del pipeline:** MIT
- **Manuscrito tesis:** derechos del autor
- **Paper:** CC BY 4.0 (post-print)

---

**Project root:** `/opt/data/thesis-active/`
**Working dir:** `cd /opt/data/thesis-active && source .venv/bin/activate`
**Quick check:** `make sanity`
**Need help?** Read `SETUP_GUIDE.md` or message Erebus.

---

## 🌍 Esto es la MITAD de una tesis — no la tesis completa

Este repo (`P1 GeoData v2`, sustrato + corredor autónomo) **es una mitad** de la tesis de Iván en FADA. La otra mitad — los papers, los modelos entrenados, los findings medidos, el manuscrito — vive en
[`IvanWeissVanDerPol/satellite-paraguay`](https://github.com/IvanWeissVanDerPol/satellite-paraguay) (local en `/opt/data/work/satellite-paraguay`).

**👉 Leé primero [`THESIS_ARCHITECTURE.md`](THESIS_ARCHITECTURE.md)** — ahí está el mapa cross-repo: flujo de datos, archivos de estado sincron, anti-patrones. En una sola vista entendés cómo las dos mitades se conectan.

| | Este repo (sustrato) | satellite-paraguay (tesis) |
|---|---|---|
| **Qué vive acá** | Descarga de OSM/IGN/Sentinel, pipeline SAM/GroundingDINO, web app, 87-task queue | 6 papers, modelos entrenados, manuscrito CH1-CH11, defensa |
| **Cron principal** | `thesis-daily-tick` (06:00 UTC) | (sin cron propio — usa el CI del repo) |
| **Título oficial** | (no es la tesis — es el sustrato) | *"Multi-Temporal Satellite Computer Vision for Paraguay"* |
| **Autor** | Iván | Iván |
| **Director propuesto** | (no necesita — corre autónomo) | Prof. Dr. Juan Carlos Cristaldo (FADA, pendiente) |

Los dos repos comparten infraestructura vía `~/.hermes/scripts/` (cron) y la skill `thesis-active-autonomy`. El flujo de valor va **substrate → thesis**: este repo descarga y anota; satellite-paraguay analiza y publica.