#!/usr/bin/env bash
# install.sh — One-shot setup for P1 GeoData v2 thesis
# Run: bash install.sh
# All installs are idempotent — safe to re-run.

set -euo pipefail

cd "$(dirname "$0")/.."
ROOT="$(pwd)"
echo "🎓 Installing P1 GeoData v2 thesis stack in: $ROOT"
echo

# ============================================================
# 1. Python venv + core data stack
# ============================================================
echo "=== [1/8] Python venv + geospatial stack ==="

if [[ ! -d ".venv" ]]; then
    uv venv .venv --python 3.13
fi
source .venv/bin/activate

uv pip install --quiet --upgrade pip setuptools wheel

# Core geospatial + ML
uv pip install --quiet \
    numpy pandas geopandas shapely fiona pyproj rasterio \
    geoalchemy2 contextily folium mapclassify \
    matplotlib seaborn plotly \
    scikit-learn scipy statsmodels \
    torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

echo "  ✅ venv + geopandas + rasterio + pytorch(cpu) installed"
echo

# ============================================================
# 2. ML/NLP stack
# ============================================================
echo "=== [2/8] ML/NLP stack (transformers, sentence-transformers) ==="

uv pip install --quiet \
    transformers datasets accelerate peft trl bitsandbytes \
    sentence-transformers langchain langchain-community langchain-huggingface \
    chromadb faiss-cpu \
    open-clip-torch Pillow opencv-python ultralytics \
    supervision fiftyone \
    jupyter ipykernel ipywidgets \
    pytest pytest-cov black ruff mypy

echo "  ✅ transformers + langchain + open-clip-torch + ultralytics"
echo

# ============================================================
# 3. Geospatial CLI tools (GDAL/OGR for ogrinfo)
# ============================================================
echo "=== [3/8] GDAL/OGR CLI tools ==="

# Try apt first (Debian/Ubuntu)
if command -v apt-get >/dev/null 2>&1; then
    sudo apt-get update -qq && sudo apt-get install -y -qq gdal-bin libgdal-dev wget sqlite3 jq
elif command -v apk >/dev/null 2>&1; then
    sudo apk add --no-cache gdal wget sqlite jq
elif command -v yum >/dev/null 2>&1; then
    sudo yum install -y epel-release
    sudo yum install -y gdal wget sqlite jq
else
    echo "  ⚠️  Unknown package manager. Install gdal-bin manually."
fi

echo "  ✅ gdal-bin (ogrinfo), wget, sqlite3, jq"
echo

# ============================================================
# 4. Git LFS + HuggingFace CLI + AWS CLI + gsutil
# ============================================================
echo "=== [4/8] Git LFS + HF CLI + AWS CLI + gsutil ==="

# git-lfs via apt (preferred) or direct binary
if command -v apt-get >/dev/null 2>&1; then
    sudo apt-get install -y -qq git-lfs
    sudo git lfs install
elif command -v apk >/dev/null 2>&1; then
    sudo apk add --no-cache git-lfs
    sudo git lfs install
fi

# HuggingFace CLI (lightweight pip)
uv pip install --quiet "huggingface_hub[cli]"

# AWS CLI v2 (lightweight installer)
if ! command -v aws >/dev/null 2>&1; then
    curl -fsSL "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o /tmp/awscliv2.zip
    cd /tmp && unzip -q -o awscliv2.zip && sudo ./aws/install || true
    cd "$ROOT"
fi

# gsutil via pip (works without full Google Cloud SDK)
uv pip install --quiet gsutil

echo "  ✅ git-lfs, huggingface-cli, aws-cli, gsutil"
echo

# ============================================================
# 5. Node.js packages (Next.js 16 + Tailwind v4 + LangChain JS)
# ============================================================
echo "=== [5/8] Node.js stack ==="

# We don't install the full Next.js project here — that's `make init-web`
# but we pre-install global tooling
npm install -g --silent pnpm yarn >/dev/null 2>&1 || true

echo "  ✅ pnpm + yarn (globals) — Next.js project created by 'make init-web'"
echo

# ============================================================
# 6. Docker bundle preparation (not actually running services)
# ============================================================
echo "=== [6/8] Docker setup ==="

# Verify docker present
if command -v docker >/dev/null 2>&1; then
    docker --version
    # Compose v2 is bundled in modern Docker; if not, install plugin
    if ! docker compose version >/dev/null 2>&1; then
        sudo apt-get install -y -qq docker-compose-plugin || true
    fi
else
    echo "  ⚠️  Docker not available. Install Docker Desktop or docker.io."
fi
echo

# ============================================================
# 7. Ollama (local LLM runtime)
# ============================================================
echo "=== [7/8] Ollama (local LLM) ==="

if ! command -v ollama >/dev/null 2>&1; then
    curl -fsSL https://ollama.com/install.sh | sh
fi

# Pre-pull small model (cheap; ~600 MB) so first run works
ollama pull llama3.2:3b-instruct-q4_K_M || true

echo "  ✅ Ollama + llama3.2:3b-instruct-q4_K_M (650 MB)"
echo

# ============================================================
# 8. Label Studio (annotation UI)
# ============================================================
echo "=== [8/8] Label Studio ==="

# Label Studio runs in Docker for clean isolation
if command -v docker >/dev/null 2>&1; then
    docker pull heartexlabs/label-studio:latest
    echo "  ✅ label-studio Docker image pulled"
else
    uv pip install --quiet label-studio
    echo "  ✅ label-studio installed via pip"
fi
echo

# ============================================================
# Verify
# ============================================================
echo "=== Verification ==="
source .venv/bin/activate
python3 -c "
import sys
print(f'Python: {sys.version.split()[0]}')
mods = ['numpy', 'pandas', 'geopandas', 'shapely', 'rasterio', 'transformers', 'torch', 'open_clip', 'ultralytics', 'langchain', 'chromadb', 'fiona']
for m in mods:
    try:
        mod = __import__(m)
        v = getattr(mod, '__version__', '?')
        print(f'  ✅ {m:<20} {v}')
    except ImportError as e:
        print(f'  ❌ {m:<20} {e}')
"

echo
echo "============================================="
echo "✅ Install complete. Next: 'make sanity'"
echo "============================================="