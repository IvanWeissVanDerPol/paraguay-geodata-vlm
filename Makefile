# Makefile — P1 GeoData v2 thesis
# Run `make help` to see all targets.

.PHONY: help
help:  ## Show this help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

# ============================================================================
# Setup & installation
# ============================================================================

.PHONY: install
install:  ## Run full install (Python + Docker + tools)
	bash scripts/install.sh

.PHONY: install-py
install-py:  ## Install only Python deps
	uv venv .venv --python 3.13
	. .venv/bin/activate && uv pip install -r requirements.txt

.PHONY: validate-creds
validate-creds:  ## Validate secrets/creds.json
	. .venv/bin/activate && python3 scripts/validate_creds.py

.PHONY: validate-creds-strict
validate-creds-strict:  ## Validate creds (strict — reject placeholders)
	. .venv/bin/activate && python3 scripts/validate_creds.py --strict

.PHONY: lock-perms
lock-perms:  ## Lock down secrets/ directory perms
	chmod 700 secrets/
	chmod 600 secrets/creds.json secrets/creds.schema.json
	@echo "🔒 secrets/ locked (700 dir, 600 files)"

# ============================================================================
# Data pipeline
# ============================================================================

.PHONY: data
data:  ## Download all datasets via fetch_data.sh
	bash scripts/fetch_data.sh --datasets $(DATASETS)

.PHONY: data-osm
data-osm:  ## Download OSM Paraguay only (default)
	bash scripts/fetch_data.sh --datasets osm

.PHONY: data-ign
data-ign:  ## Pull IGN raster tiles via WMS
	. .venv/bin/activate && python3 scripts/fetch_ign_wms.py

.PHONY: data-sentinel
data-sentinel:  ## Download Sentinel-2 (requires Copernicus creds)
	. .venv/bin/activate && python3 scripts/fetch_sentinel.py --from $(SENTINEL_FROM) --to $(SENTINEL_TO)

.PHONY: data-status
data-status:  ## Show data inventory status
	. .venv/bin/activate && python3 scripts/data_status.py

# ============================================================================
# Annotation
# ============================================================================

.PHONY: annotate
annotate:  ## Run auto-annotation pipeline on a shapefile
	. .venv/bin/activate && python3 scripts/auto_annotate.py \
		--input $(INPUT) --output $(OUTPUT) --category $(CATEGORY) \
		--max-samples $(SAMPLES) --confidence-threshold $(CONF)

.PHONY: annotate-sample
annotate-sample:  ## Run on a 1K sample for testing
	. .venv/bin/activate && python3 scripts/auto_annotate.py \
		--input data/raw/2026-08-10/osm/extracted/gis_osm_buildings_a_free_1.shp \
		--output data/processed/buildings_annotated_sample.geojson \
		--category building --max-samples 1000 --confidence-threshold 0.7

.PHONY: annotate-all
annotate-all:  ## Run full pipeline on all categories
	. .venv/bin/activate && python3 scripts/annotate_all.sh

.PHONY: label-studio
label-studio:  ## Start Label Studio (Docker or local)
	@if command -v docker >/dev/null 2>&1; then \
		docker compose up -d label-studio; \
		echo "Label Studio at http://localhost:8080"; \
	else \
		. .venv/bin/activate && label-studio start; \
	fi

# ============================================================================
# ML training
# ============================================================================

.PHONY: train-smolvlm
train-smolvlm:  ## Fine-tune SmolVLM-256M with QLoRA
	. .venv/bin/activate && python3 scripts/train.py --model smolvlm --epochs 3 --batch 8

.PHONY: train-florence2
train-florence2:  ## Fine-tune Florence-2-base with QLoRA
	. .venv/bin/activate && python3 scripts/train.py --model florence2 --epochs 5 --batch 4

.PHONY: eval
eval:  ## Evaluate trained models on test set
	. .venv/bin/activate && python3 scripts/eval.py --split test

.PHONY: kappa
kappa:  ## Compute Cohen's κ inter-annotator agreement
	. .venv/bin/activate && python3 scripts/inter_annotator_agreement.py

# ============================================================================
# Conversational agent
# ============================================================================

.PHONY: ollama
ollama:  ## Start Ollama + pull models
	ollama serve &
	ollama pull llama3.1:8b-instruct-q4_K_M

.PHONY: agent-test
agent-test:  ## Test the RAG agent on a sample query
	. .venv/bin/activate && python3 scripts/agent_query.py --query "¿Cuántas carreteras pavimentadas hay en Central?"

.PHONY: benchmark
benchmark:  ## Run the 100-question benchmark
	. .venv/bin/activate && python3 scripts/benchmark.py --questions BENCHMARK_QUESTIONS.md --output data/processed/benchmark_results.json

# ============================================================================
# Web app
# ============================================================================

.PHONY: init-web
init-web:  ## Create Next.js 16 + Tailwind v4 project
	cd web && npx create-next-app@latest . --typescript --tailwind --app --src-dir --use-npm

.PHONY: web-dev
web-dev:  ## Run web app dev server
	cd web && npm run dev

.PHONY: init-backend
init-backend:  ## Create FastAPI backend project
	mkdir -p backend && cd backend && uv init --python 3.13

.PHONY: api
api:  ## Run FastAPI backend
	. .venv/bin/activate && cd backend && uvicorn main:app --reload --host 0.0.0.0 --port 8001

.PHONY: compose-up
compose-up:  ## Start all services via docker-compose
	docker compose up -d

.PHONY: compose-down
compose-down:  ## Stop all services
	docker compose down

.PHONY: compose-logs
compose-logs:  ## Tail docker-compose logs
	docker compose logs -f

# ============================================================================
# Publication
# ============================================================================

.PHONY: hf-upload-dataset
hf-upload-dataset:  ## Upload annotated dataset to HuggingFace
	. .venv/bin/activate && python3 scripts/hf_upload.py --what dataset --path data/processed/annotations_v1.geojson

.PHONY: hf-upload-model
hf-upload-model:  ## Upload fine-tuned model to HuggingFace
	. .venv/bin/activate && python3 scripts/hf_upload.py --what model --path models/florence2-paraguay/

.PHONY: hf-login
hf-login:  ## Authenticate with HuggingFace
	. .venv/bin/activate && hf auth login --token $(HF_TOKEN)

.PHONY: zenodo-publish
zenodo-publish:  ## Mint DOI on Zenodo
	. .venv/bin/activate && python3 scripts/zenodo_publish.py

.PHONY: arxiv-submit
arxiv-submit:  ## Submit paper to arxiv
	. .venv/bin/activate && python3 scripts/arxiv_submit.py

# ============================================================================
# Quality / sanity
# ============================================================================

.PHONY: sanity
sanity:  ## End-to-end sanity check
	. .venv/bin/activate && python3 scripts/sanity_check.py

# ============================================================================
# Autonomous work loop
# ============================================================================

.PHONY: tick
tick:  ## Run one autonomous work tick (pick + execute + log)
	. .venv/bin/activate && python3 scripts/autonomous_tick.py

.PHONY: tick-dry
tick-dry:  ## Show what the next tick would do (no state change)
	. .venv/bin/activate && python3 scripts/autonomous_tick.py --dry-run

.PHONY: tick-list
tick-list:  ## List all pending tasks in priority order
	. .venv/bin/activate && python3 scripts/autonomous_tick.py --list

.PHONY: tick-claim
tick-claim:  ## Claim a specific task (use T### id)
	. .venv/bin/activate && python3 scripts/autonomous_tick.py --claim $(TASK_ID)

.PHONY: tick-complete
tick-complete:  ## Mark a task complete
	. .venv/bin/activate && python3 scripts/autonomous_tick.py --complete $(TASK_ID) --output "$(OUTPUT)" --notes "$(NOTES)"

.PHONY: tick-blocked
tick-blocked:  ## Mark a task blocked
	. .venv/bin/activate && python3 scripts/autonomous_tick.py --blocked $(TASK_ID) --output "$(OUTPUT)" --notes "$(NOTES)"

.PHONY: weekly
weekly:  ## Run weekly review (stats + recommendations)
	. .venv/bin/activate && python3 scripts/weekly_review.py

.PHONY: rehearse
rehearse:  ## Interactive defense rehearsal (timer + per-slide prompts)
	. .venv/bin/activate && python3 scripts/rehearse_defense.py rehearse

.PHONY: rehearse-dry
rehearse-dry:  ## Print defense rehearsal structure + time budgets (no run)
	. .venv/bin/activate && python3 scripts/rehearse_defense.py dry

.PHONY: rehearse-report
rehearse-report:  ## Summarize past defense rehearsals
	. .venv/bin/activate && python3 scripts/rehearse_defense.py report

.PHONY: status
status:  ## Show current project status (progress + blockers + tasks)
	@echo "=== TASK QUEUE ==="
	@grep -c "^- \[x\]" TASK_QUEUE.md 2>/dev/null | xargs -I{} echo "  Done:    {}"
	@grep -c "^- \[\~\]" TASK_QUEUE.md 2>/dev/null | xargs -I{} echo "  Active:  {}"
	@grep -c "^- \[\!\]" TASK_QUEUE.md 2>/dev/null | xargs -I{} echo "  Blocked: {}"
	@grep -c "^- \[ \]" TASK_QUEUE.md 2>/dev/null | xargs -I{} echo "  Pending: {}"
	@echo ""
	@echo "=== LAST 10 TICKS ==="
	@tail -50 PROGRESS.md | grep -E "## 20" | tail -10
	@echo ""
	@echo "=== BLOCKERS ==="
	@grep "^- \[\!\]" TASK_QUEUE.md 2>/dev/null | head -5 || echo "  (none)"

# ============================================================================
# Git workflow (Erebus auto-commits; Ivan triggers sync)
# ============================================================================

.PHONY: git-init
git-init:  ## Initialize git repo (one-time)
	git init --initial-branch=main
	git config user.name "Iván Weiss Van der Pol"
	git config user.email "thesis@ivanweissvanderpol.dev"
	git config core.autocrlf input
	git config pull.rebase true
	git remote add origin https://github.com/IvanWeissVanDerPol/paraguay-geodata-vlm.git
	@echo "✅ git repo initialized"
	@echo "   Next: make commit (creates initial commit)"
	@echo "   Then: bash scripts/git_sync.sh --push (pushes to remote)"

.PHONY: commit
commit:  ## Create atomic commit (auto-detects type/scope from changed files)
	. .venv/bin/activate && python3 scripts/git_commit.py

.PHONY: commit-dry
commit-dry:  ## Show what would be committed (no actual commit)
	. .venv/bin/activate && python3 scripts/git_commit.py --dry-run

.PHONY: commit-feat
commit-feat:  ## Commit as feat type
	. .venv/bin/activate && python3 scripts/git_commit.py --type feat --subject "$(SUBJECT)"

.PHONY: commit-fix
commit-fix:  ## Commit as fix type
	. .venv/bin/activate && python3 scripts/git_commit.py --type fix --subject "$(SUBJECT)"

.PHONY: commit-docs
commit-docs:  ## Commit as docs type
	. .venv/bin/activate && python3 scripts/git_commit.py --type docs --subject "$(SUBJECT)"

.PHONY: git-sync
git-sync:  ## Sync local with remote (fetch + rebase + status). Safe.
	bash scripts/git_sync.sh

.PHONY: git-fetch
git-fetch:  ## Only fetch from remote, no push
	bash scripts/git_sync.sh --fetch

.PHONY: git-first-push
git-first-push:  ## First-time push to empty GitHub repo (uses GH_TOKEN env or prompts)
	bash scripts/first_push.sh

.PHONY: git-push
git-push:  ## Push local commits to remote
	bash scripts/git_sync.sh --push

.PHONY: git-resolve
git-resolve:  ## Auto-resolve merge conflicts (PROGRESS, TASK_QUEUE, RISK)
	. .venv/bin/activate && python3 scripts/git_conflict_resolver.py

.PHONY: git-resolve-dry
git-resolve-dry:  ## Show what conflict resolver would do
	. .venv/bin/activate && python3 scripts/git_conflict_resolver.py --dry-run

.PHONY: git-log
git-log:  ## Show last 20 commits
	git log --oneline -20

.PHONY: git-status
git-status:  ## Show git working tree status
	git status --short --branch

.PHONY: git-branches
git-branches:  ## List all branches
	git branch -av

.PHONY: git-branch-feat
git-branch-feat:  ## Create new feature branch (use NAME=my-feature)
	git checkout -b "feat/$(NAME)"
	@echo "✅ Branched: feat/$(NAME)"
	@echo "   Work here, then merge to main with: git checkout main && git merge feat/$(NAME)"


.PHONY: heartbeat
heartbeat:  ## Touch the heartbeat file (call after any work)
	bash scripts/thesis-heartbeat.sh "manual heartbeat"

.PHONY: watchdog
watchdog:  ## Check if thesis work is recent; trigger resume if stale
	. .venv/bin/activate && python3 scripts/thesis_watchdog.py

.PHONY: watchdog-check
watchdog-check:  ## Just report watchdog status, no action
	. .venv/bin/activate && python3 scripts/thesis_watchdog.py --check-only

.PHONY: heartbeat-install
heartbeat-install:  ## Touch heartbeat once to initialize
	bash scripts/thesis-heartbeat.sh "first heartbeat"


.PHONY: git-install-hooks
git-install-hooks:  ## Install pre-commit hook
	cp scripts/pre-commit-hook.sh .git/hooks/pre-commit
	chmod +x .git/hooks/pre-commit
	@echo "✅ pre-commit hook installed"

.PHONY: lint
lint:  ## Run ruff + black check
	. .venv/bin/activate && ruff check . && black --check .

.PHONY: test
test:  ## Run pytest
	. .venv/bin/activate && pytest tests/ -v

.PHONY: notebook
notebook:  ## Start Jupyter Lab
	. .venv/bin/activate && jupyter lab --ip 0.0.0.0 --port 8888

.PHONY: clean
clean:  ## Remove generated files (keeps data/raw and secrets)
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .pytest_cache -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .ruff_cache -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	rm -rf data/processed/* 2>/dev/null || true
	@echo "🧹 Cleaned (raw data + secrets preserved)"

.PHONY: clean-all
clean-all: clean  ## Nuke everything (including data — DESTRUCTIVE)
	rm -rf .venv data/raw data/processed data/models
	@echo "💣 Full clean done. Re-run 'make install' to rebuild."

# ============================================================================
# Convenience variables
# ============================================================================

DATASETS ?= osm
INPUT ?= data/raw/2026-08-10/osm/extracted/gis_osm_buildings_a_free_1.shp
OUTPUT ?= data/processed/buildings_annotated.geojson
CATEGORY ?= building
SAMPLES ?= 5000
CONF ?= 0.7
SENTINEL_FROM ?= 2024-01-01
SENTINEL_TO ?= 2026-08-10