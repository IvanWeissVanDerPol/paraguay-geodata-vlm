#!/usr/bin/env bash
# .git/hooks/pre-commit — Run sanity checks before each commit.
#
# Auto-installed by scripts/install.sh. Runs:
# 1. Secret leak check (delegated to git_commit.py --dry-run)
# 2. Python syntax check on staged .py files
# 3. JSON validity on staged .json files
# 4. Markdown sanity (file size limits)
#
# To bypass: git commit --no-verify
# To disable: rm .git/hooks/pre-commit

set -e

cd "$(git rev-parse --show-toplevel)"

red()    { echo -e "\033[31m$1\033[0m"; }
yellow() { echo -e "\033[33m$1\033[0m"; }
green()  { echo -e "\033[32m$1\033[0m"; }

echo "🔍 pre-commit hook running..."

# 1. Secret leak check
STAGED_FILES=$(git diff --cached --name-only --diff-filter=ACM | grep -v "^$" || true)
if [[ -n "$STAGED_FILES" ]]; then
    # Quick pattern check
    LEAKS=$(echo "$STAGED_FILES" | grep -E "secrets/creds\.json|\.env$|secrets/.*\.(key|pem|age)$" || true)
    if [[ -n "$LEAKS" ]]; then
        red "❌ Secret-like file in commit:"
        echo "$LEAKS"
        exit 1
    fi

    # Check staged file contents for known token patterns
    # Skip example/template files (intentionally contain fake tokens)
    for f in $STAGED_FILES; do
        if [[ -f "$f" ]]; then
            if [[ "$f" == *.example ]] || [[ "$f" == *template* ]] || [[ "$f" == *EXAMPLE* ]]; then
                continue
            fi
            if grep -lE "hf_[A-Za-z0-9_]{20,}|ghp_[A-Za-z0-9_]{20,}|AKIA[A-Z0-9]{16}|sk-[A-Za-z0-9]{20,}" "$f" 2>/dev/null; then
                red "❌ Token-like pattern in $f"
                exit 1
            fi
        fi
    done
fi

# 2. Python syntax check
PY_FILES=$(echo "$STAGED_FILES" | grep -E "\.py$" || true)
if [[ -n "$PY_FILES" ]]; then
    source .venv/bin/activate 2>/dev/null || true
    for f in $PY_FILES; do
        if [[ -f "$f" ]]; then
            if ! python3 -c "import ast; ast.parse(open('$f').read())" 2>/dev/null; then
                red "❌ Python syntax error in $f"
                python3 -c "import ast; ast.parse(open('$f').read())"
                exit 1
            fi
        fi
    done
fi

# 3. JSON validity
JSON_FILES=$(echo "$STAGED_FILES" | grep -E "\.json$" || true)
if [[ -n "$JSON_FILES" ]]; then
    for f in $JSON_FILES; do
        if [[ -f "$f" ]]; then
            if ! python3 -c "import json; json.load(open('$f'))" 2>/dev/null; then
                red "❌ Invalid JSON in $f"
                exit 1
            fi
        fi
    done
fi

# 4. Markdown size check (warn if > 200 KB)
MD_FILES=$(echo "$STAGED_FILES" | grep -E "\.md$" || true)
if [[ -n "$MD_FILES" ]]; then
    for f in $MD_FILES; do
        if [[ -f "$f" ]]; then
            SIZE=$(wc -c < "$f")
            if [[ $SIZE -gt 200000 ]]; then
                yellow "⚠️  $f is large ($(($SIZE / 1024)) KB) — consider splitting"
            fi
        fi
    done
fi

green "✅ pre-commit checks passed"
exit 0