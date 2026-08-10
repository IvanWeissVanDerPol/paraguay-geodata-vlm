# P1 GeoData v2 — Quick Reference Card

**Print this. Tape it to your monitor.**

---

## Daily 5-minute warmup

```bash
cd /opt/data/thesis-active
source .venv/bin/activate
make sanity
```

If `make sanity` shows all green, you're good.

---

## The 10 commands you'll use 90% of the time

| Command | What it does |
|---|---|
| `make status` | Health check (packages, data, creds, pipeline) |
| `make data-osm` | Download OSM Paraguay |
| `make annotate-sample` | Run annotation on 1K buildings sample |
| `make data-status` | Show what's downloaded |
| `make validate-creds` | Check credentials file |
| `make notebook` | Start Jupyter Lab |
| `make label-studio` | Start annotation UI |
| `make api` | Start FastAPI backend |
| `make web-dev` | Start Next.js dev server |
| `make compose-up` | Start all services via Docker |
| `make commit` | Atomic commit (Erebus runs this) |
| `make git-first-push` | First push to empty GitHub repo (Ivan runs once) |
| `make git-sync` | Sync local with GitHub (Ivan runs this) |

---

## Critical files (don't lose these)

```
README.md                       ← start here
SETUP_GUIDE.md                  ← installation walkthrough
FORMAL_PROPOSAL.md              ← pregunta + hipótesis + objetivos
ETHICS_WAIVER_MEMO.md           ← no IRB
DATA_MANIFEST.md                ← datasets list
METHODOLOGY.md                  ← Cap. 3
PAPER_OUTLINE.md                ← paper outline
BENCHMARK_QUESTIONS.md          ← 100 validation questions
DEFENSE_PLAN.md                 ← defensa + advisor strategy
RISK_REGISTER.md                ← 35 riesgos
secrets/creds.json              ← credentials (PERMISSIONS 600!)
.env.example                    ← env var template
Makefile                        ← all commands
scripts/install.sh              ← bootstrap
scripts/sanity_check.py         ← verify environment
scripts/validate_creds.py       ← validate credentials
scripts/load_creds.py           ← load credentials to env
scripts/auto_annotate.py        ← annotation pipeline
data/raw/2026-08-10/osm/        ← OSM Paraguay 1.2 GB
docker-compose.yml              ← full stack
```

---

## When you get stuck

1. `make sanity` — runs diagnostics
2. Read `SETUP_GUIDE.md` troubleshooting section
3. Ask Erebus via WhatsApp (paste the error)

---

## Quick stats (as of 2026-08-10)

- **OSM Paraguay:** 2.46M features, 1.2 GB extracted
- **Buildings:** 1.7M (all with generic `fclass='building'` — gap confirmed!)
- **Python packages:** 80+ installed (numpy 2.x, transformers 5.x, torch 2.x)
- **CLI tools:** git, docker, curl, hf (all working)
- **System tools missing:** jq, ogrinfo (apt-get needs sudo; not blocking)
- **Credentials:** 0/20 filled (template ready, awaiting Iván)
- **Makefile targets:** 30+ commands
- **Documentation:** 13 markdown files (~80 KB)
- **Code:** 5 Python scripts (~30 KB)
- **Total project size:** ~1.5 GB on disk

---

## The 5 minute conversation with Erebus

When you want to do something:

```
Erebus, [action you want]

E.g.:
  Erebus, run annotation on 5K buildings
  Erebus, download Copernicus Sentinel-2 for August 2026
  Erebus, draft the related work section of the paper
  Erebus, push this commit to GitHub
```

If credentials are needed, Erebus will say:
"I need the [service] credentials. Fill secrets/creds.json and paste here."

---

**Last updated:** 2026-08-10
**Project root:** `/opt/data/thesis-active/`