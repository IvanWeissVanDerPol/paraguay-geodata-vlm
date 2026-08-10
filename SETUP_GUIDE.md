# 🚀 SETUP GUIDE — P1 GeoData v2

**Complete installation + credential-handoff guide.**

This is the single document you need to go from a fresh checkout to a fully working environment.

**Time estimate:** 30-60 minutes (mostly downloads).
**Difficulty:** medium (you'll need to create 3-4 free accounts).

---

## 📋 Table of contents

1. [What you're installing](#1-what-youre-installing)
2. [Quick start (5 min)](#2-quick-start-5-min)
3. [Full install (30-60 min)](#3-full-install-30-60-min)
4. [Credentials: what Iván needs to provide](#4-credentials-what-iván-needs-to-provide)
5. [How to pass credentials to Erebus](#5-how-to-pass-credentials-to-erebus)
6. [Daily workflow](#6-daily-workflow)
7. [Troubleshooting](#7-troubleshooting)

---

## 1. What you're installing

The thesis stack has **6 layers**:

| Layer | Components | Purpose |
|---|---|---|
| **System tools** | git, curl, wget, jq, sqlite3, gdal-bin | CLI utilities |
| **Python venv** | numpy, pandas, geopandas, shapely, rasterio | Geospatial data manipulation |
| **ML stack** | torch, transformers, ultralytics, open-clip-torch | Vision-language models |
| **LLM stack** | langchain, chromadb, sentence-transformers | RAG agent |
| **Web stack** | Next.js 16, Tailwind v4 (via `make init-web`) | Conversational interface |
| **Container stack** | docker, docker-compose | Reproducibility bundle |

**Total disk footprint:** ~3 GB (Python packages) + ~30 GB (data downloads).

---

## 2. Quick start (5 min)

```bash
# Clone the thesis repo (when ready)
git clone https://github.com/IvanWeissVanDerPol/paraguay-geodata-vlm.git
cd paraguay-geodata-vlm

# Run the full install
bash scripts/install.sh

# Verify everything works
make sanity

# Lock down secrets dir (do this once)
make lock-perms
```

That's it. You now have a working environment.

---

## 3. Full install (30-60 min)

### Step 3.1 — System requirements

| Component | Minimum | Recommended |
|---|---|---|
| OS | Linux (Ubuntu 22.04+ / Debian 12+) or macOS | Linux |
| RAM | 8 GB | 32 GB |
| Disk | 30 GB free | 100 GB |
| Python | 3.11+ | 3.13 |
| GPU | None (CPU works) | NVIDIA RTX 4090 or rented A100 |

### Step 3.2 — Create the free accounts you need

**Required (P0) — do these first:**

| Service | URL | What for | Time to register |
|---|---|---|---|
| **GitHub** | https://github.com/signup | Repo + code | 2 min |
| **HuggingFace** | https://huggingface.co/join | Dataset + model | 2 min |
| **Copernicus** | https://dataspace.copernicus.eu/ | Sentinel-2 satellite imagery | 5 min (instant approval) |

**Optional (P1) — do these when convenient:**

| Service | URL | What for |
|---|---|---|
| **AWS** | https://aws.amazon.com/free/ | Alt to Copernicus, free tier 12 months |
| **Google Cloud** | https://console.cloud.google.com/ | Open Buildings v3 download |
| **Cloudflare** | https://dash.cloudflare.com/sign-up | R2 storage for web hosting |

**Future (P2) — only when paper is ready (month 7+):**

| Service | URL | What for |
|---|---|---|
| **arXiv** | https://arxiv.org/register | Paper submission |
| **Zenodo** | https://zenodo.org/signup | Dataset DOI |
| **ORCID** | https://orcid.org/register | Author ID (free, do now actually) |

### Step 3.3 — Install

```bash
# Linux (Debian/Ubuntu) — root or sudo needed for system packages
bash scripts/install.sh

# macOS — install Homebrew first if you don't have it
brew install gdal jq wget
bash scripts/install.sh
```

The install script does:

1. Creates Python venv at `.venv/` using `uv`
2. Installs ~80 Python packages (geospatial + ML + LLM)
3. Installs system tools: `git-lfs`, `gdal-bin`, `wget`, `sqlite3`, `jq`
4. Pulls Ollama Docker image + small Llama model
5. Pulls Label Studio Docker image
6. Verifies all packages load

If `install.sh` fails on system tools (no `sudo`), you can skip them — the Python stack is enough for most work.

### Step 3.4 — Verify

```bash
make sanity
```

Expected output:

```
🎓 P1 GeoData v2 — sanity check

=== Python ===
  Python 3.13.x on Linux x86_64
  ✅ Version OK

=== Packages ===
  ✅ numpy              2.x
  ✅ pandas             3.x
  ✅ geopandas          1.x
  ✅ transformers       4.x
  ...

=== CLI tools ===
  ✅ git                  ...
  ✅ docker               ...
  ✅ curl                 ...
  ...

=== Data ===
  Latest snapshot: data/raw/2026-08-10
  OSM extracted: 20 shapefiles
  OSM total size: 544 MB
  ✅ OSM data present

=== Credentials ===
  Filled:      7
  Placeholders: 20
  ⚠️  ...

============================================================
  Overall: ✅ PASS
============================================================
```

### Step 3.5 — Download data

```bash
# OSM Paraguay only (default, ~300 MB)
make data-osm

# All datasets (requires Copernicus creds for Sentinel-2)
make data

# Just one dataset
make data DATASETS=osm,ign

# Status check
make data-status
```

---

## 4. Credentials: what Iván needs to provide

You have **20 credential slots** across **10 services**. Not all are required at once.

### Priority breakdown

| Priority | Service | Required now? | Where to get |
|---|---|---|---|
| **P0 — REQUIRED now** | `huggingface.token` | ✅ Yes | https://huggingface.co/settings/tokens (write scope) |
| | `huggingface.username` | ✅ Yes | https://huggingface.co/settings/profile |
| | `copernicus.user` / `copernicus.pass` | ✅ Yes (for Sentinel-2) | https://dataspace.copernicus.eu/ |
| | `github.token` | ✅ Yes (for code push) | https://github.com/settings/tokens (scope: repo) |
| **P1 — Optional** | `aws.access_key_id` / `aws.secret_access_key` | When convenient | https://aws.amazon.com/ (free tier) |
| | `google_cloud.service_account_json_path` | When convenient | https://console.cloud.google.com/ |
| | `cloudflare_r2.*` | When deploying web app | https://dash.cloudflare.com/ |
| **P2 — Later (month 7+)** | `arxiv.user` / `arxiv.pass` / `arxiv.orcid` | When submitting paper | https://arxiv.org/register |
| | `zenodo.token` | When minting DOI | https://zenodo.org/ |
| **P3 — Rarely needed** | `openai.api_key` | Only if using GPT for writing | https://platform.openai.com/ |
| | `anthropic.api_key` | Only if using Claude for writing | https://console.anthropic.com/ |
| | `una.student_id` | Only at enrollment (month 8+) | You already have this |

### Minimum viable creds (P0 only)

If you want to start working **today**, you only need:

1. **HuggingFace** token + username (for dataset/model upload later)
2. **GitHub** token (for code push)
3. **Copernicus** (only if you want Sentinel-2; OSM is already downloaded)

Without these, you can still:
- Run annotation on existing OSM data
- Train models locally (CPU mode)
- Develop the web app
- Write the paper

You only NEED the credentials at the moment they're used (month 3+ for HF, month 7+ for arxiv).

---

## 5. How to pass credentials to Erebus

### Step 5.1 — Fill in `secrets/creds.json`

Open `secrets/creds.json` in your editor:

```bash
nano secrets/creds.json
# or
code secrets/creds.json
```

Replace each `FILL_ME_*` with the real value:

```json
{
  "services": {
    "huggingface": {
      "token": "hf_abc123def456...",
      "username": "IvanWeissVanDerPol"
    },
    "github": {
      "token": "ghp_xyz789...",
      "user": "IvanWeissVanDerPol"
    }
  }
}
```

For ones you don't have yet, leave `FILL_ME_*` or set to `"skip"`.

### Step 5.2 — Validate

```bash
make validate-creds
```

Expected:

```
✅ Schema valid (patterns relaxed for placeholders)
   Filled:      5
   Placeholders: 15
   Skipped:      0
⚠️  Placeholders remaining. Fill them or set to 'skip' if not needed now.
   (OK to proceed in non-strict mode — Erebus will skip them.)
```

For **strict** mode (rejects any placeholders, used right before passing to Erebus):

```bash
make validate-creds-strict
```

Exit 0 = all creds filled, ready to pass.

### Step 5.3 — Lock file permissions

```bash
make lock-perms
```

This sets `chmod 700` on `secrets/` and `chmod 600` on `secrets/creds.json` so only your user can read them.

### Step 5.4 — Pass to Erebus

Two options:

#### Option A: Mensaje paste (simplest)

1. Open `secrets/creds.json`
2. Copy the entire file contents (Ctrl+A, Ctrl+C)
3. Open Mensaje chat with Erebus
4. Paste as one code block, prefixed with:

```
Erebus, load these credentials:
```json
[paste here]
```
```

5. Erebus will:
   - Save the file to `/opt/data/thesis-active/secrets/creds.json` on his end
   - Validate the schema
   - Tell you which services loaded successfully
   - Begin using them in the next operation

#### Option B: Encrypted paste (more secure)

```bash
# On Iván's machine, encrypt with Erebus's public age key
age -r erebus_public_key.txt secrets/creds.json > secrets/creds.json.age

# Send the .age file via Mensaje
```

Erebus decrypts with his private key. Same end result.

### Step 5.5 — Confirm

Erebus will reply with a summary like:

```
✅ Loaded credentials
  - huggingface (token + username)
  - github (token + user + repo)
  - copernicus (user + pass)
  ⏭️  Skipped 17 placeholders
  ⏭️  Not touched: aws, google_cloud, cloudflare_r2, arxiv, zenodo, openai, anthropic, una

🔒 Storage: /opt/data/thesis-active/secrets/creds.json (mode 600)
📤 Not committed to git.
🔄 Will use only for the thesis services above.

Ready. Next: what do you want me to do?
```

---

## 6. Daily workflow

Once everything is set up, your daily workflow is:

```bash
# Activate environment (every new terminal)
cd /opt/data/thesis-active
source .venv/bin/activate

# Common commands
make sanity               # health check
make annotate-sample      # run annotation on a small sample
make data-status          # see what data is downloaded
make web-dev              # start the web app dev server
make api                  # start the FastAPI backend
make label-studio         # start annotation UI
make benchmark            # run the 100-question benchmark
make train-smolvlm        # fine-tune SmolVLM
make eval                 # evaluate models

# Jupyter for exploration
make notebook             # http://localhost:8888

# Cleanup
make clean                # remove processed data + caches
```

---

## 7. Troubleshooting

### "uv: command not found"

Install uv:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### "ModuleNotFoundError: No module named 'geopandas'"

Activate the venv:

```bash
source .venv/bin/activate
which python3  # should point to .venv/bin/python3
```

If that's correct but geopandas still missing, reinstall:

```bash
uv pip install geopandas shapely fiona rasterio
```

### "docker: permission denied"

Add your user to the docker group:

```bash
sudo usermod -aG docker $USER
newgrp docker
```

### "Port 8080 already in use"

Edit `docker-compose.yml` and change the port mapping:

```yaml
ports:
  - "127.0.0.1:8081:8080"  # change 8081 to anything free
```

### "ogrinfo: command not found"

The install script needs `sudo` to install `gdal-bin`. Either:

- `sudo apt-get install -y gdal-bin` (Linux)
- `brew install gdal` (macOS)

Or use the Python alternative:

```python
import geopandas as gpd
gdf = gpd.read_file("file.shp")
```

### "Cannot open .env.example" or "permission denied on secrets/"

Run `make lock-perms` to set correct permissions.

### "huggingface-cli deprecated"

Use `hf` instead:

```bash
hf --version           # works
hf auth login --token hf_xxx
hf upload my-repo . .
```

### "Out of memory during training"

Reduce batch size in Makefile:

```makefile
BATCH_SIZE=4  # default 8
GRADIENT_ACCUMULATION=8  # default 4 (keeps effective batch at 32)
```

Or use CPU mode (slow but no GPU memory needed):

```bash
TORCH_DEVICE=cpu make train-smolvlm
```

### "Internet download failed"

```bash
# Retry just one dataset
make data DATASETS=osm

# Or manually
curl -L -o data/raw/osm/paraguay-latest-free.shp.zip \
    "https://download.geofabrik.de/south-america/paraguay-latest-free.shp.zip"
```

---

## 🎯 You're ready

After running through this guide, you have:

- ✅ Python environment with all packages
- ✅ Data downloaded (OSM Paraguay 302 MB / 2.46M features)
- ✅ Docker stack ready (label-studio, ollama, chroma, postgres)
- ✅ Annotation pipeline skeleton functional
- ✅ Credentials bundle ready to fill + pass to Erebus
- ✅ Makefile with 30+ commands for daily work
- ✅ SETUP_GUIDE (this file) for future reference

**Next step:** fill in `secrets/creds.json`, validate with `make validate-creds`, and paste to Erebus via Mensaje.

---

**Last updated:** 2026-08-10
**Maintained by:** Erebus (Hermes agent) for Iván Weiss Van der Pol