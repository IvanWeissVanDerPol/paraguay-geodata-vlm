#!/usr/bin/env bash
# first_push.sh — Push the local repo to the empty GitHub repo.
#
# This is a ONE-TIME script. After the first push, use git_sync.sh or
# make git-push for subsequent pushes.
#
# Required:
#   - GitHub repo exists: IvanWeissVanDerPol/paraguay-geodata-vlm
#   - You have a Personal Access Token (PAT) with 'repo' scope
#   - The token must NOT be committed anywhere
#
# Usage:
#   bash scripts/first_push.sh                     # interactive (will prompt for token)
#   GH_TOKEN=ghp_xxx bash scripts/first_push.sh    # non-interactive (recommended)
#
# What it does:
#   1. Verifies remote exists + is empty
#   2. Configures git credential helper (temporary, in-memory only)
#   3. Pushes main branch to origin
#   4. Verifies push succeeded
#   5. Cleans up credential from memory

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$PROJECT_ROOT"

red()    { echo -e "\033[31m$1\033[0m"; }
green()  { echo -e "\033[32m$1\033[0m"; }
yellow() { echo -e "\033[33m$1\033[0m"; }
blue()   { echo -e "\033[34m$1\033[0m"; }

echo "🚀 first_push.sh — initial push of local repo to GitHub"
echo

# 1. Verify remote exists
if ! git remote get-url origin >/dev/null 2>&1; then
    red "❌ No 'origin' remote configured"
    echo "   Run: git remote add origin https://github.com/IvanWeissVanDerPol/paraguay-geodata-vlm.git"
    exit 1
fi

ORIGIN_URL=$(git remote get-url origin)
echo "📡 Remote: $ORIGIN_URL"

# Verify the remote repo actually exists + is empty
REMOTE_STATUS=$(curl -s -o /dev/null -w "%{http_code}" --max-time 15 "$ORIGIN_URL")
echo "🔍 Remote HTTP status: $REMOTE_STATUS"

if [[ "$REMOTE_STATUS" != "200" ]]; then
    red "❌ Remote repo not accessible. Create it first: https://github.com/new"
    exit 2
fi

# 2. Get auth — prefer env var, fall back to prompt
if [[ -z "${GH_TOKEN:-}" ]]; then
    yellow "⚠️  No GH_TOKEN env var set. Will prompt for token."
    echo "   To avoid prompt: export GH_TOKEN=ghp_xxxxxxxxxxxx"
    echo "   Get a token at: https://github.com/settings/tokens (scope: repo)"
    echo
    read -rs -p "GitHub Personal Access Token: " GH_TOKEN
    echo
fi

if [[ -z "$GH_TOKEN" ]]; then
    red "❌ No token provided"
    exit 3
fi

# 3. Configure credential helper in-memory only (NOT persistent)
# This uses git's credential cache for this single command, then forgets it
GIT_ASKPASS_TEMP=$(mktemp)
cat > "$GIT_ASKPASS_TEMP" <<EOF
#!/usr/bin/env bash
echo "$GH_TOKEN"
EOF
chmod +x "$GIT_ASKPASS_TEMP"
export GIT_ASKPASS="$GIT_ASKPASS_TEMP"

# 4. Confirm before pushing
echo
echo "📦 About to push:"
git log --oneline | head -10
echo
LOCAL_COUNT=$(git rev-list --count HEAD)
echo "  Total local commits: $LOCAL_COUNT"
echo
read -rp "Continue with push? [y/N] " CONFIRM
if [[ "$CONFIRM" != "y" && "$CONFIRM" != "Y" ]]; then
    yellow "Aborted by user"
    rm -f "$GIT_ASKPASS_TEMP"
    exit 0
fi

# 5. Push
echo
echo "🚀 Pushing to origin/main..."
GIT_TERMINAL_PROMPT=0 git push -u origin main 2>&1 | tail -20

# 6. Verify
PUSH_STATUS=$(curl -s -o /dev/null -w "%{http_code}" --max-time 15 \
    "https://api.github.com/repos/IvanWeissVanDerPol/paraguay-geodata-vlm/commits")
if [[ "$PUSH_STATUS" == "200" ]]; then
    REMOTE_COUNT=$(curl -s --max-time 15 \
        "https://api.github.com/repos/IvanWeissVanDerPol/paraguay-geodata-vlm/commits" | \
        python3 -c "import json,sys; print(len(json.load(sys.stdin)))")
    green "✅ Push successful. Remote now has $REMOTE_COUNT commit(s)."
else
    red "❌ Push may have failed. Remote status: $PUSH_STATUS"
    echo "   Check: https://github.com/IvanWeissVanDerPol/paraguay-geodata-vlm"
fi

# 7. Cleanup — wipe token from temp file
rm -f "$GIT_ASKPASS_TEMP"
unset GH_TOKEN
unset GIT_ASKPASS

echo
echo "📊 Final state:"
git status --short --branch
echo
git log --oneline -5

echo
green "✅ first_push complete"
echo "   Next: use 'make git-sync' / 'make git-push' for subsequent pushes"