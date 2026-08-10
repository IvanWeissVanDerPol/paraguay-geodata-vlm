#!/usr/bin/env bash
# git_sync.sh — Safe pull + rebase + push wrapper.
#
# Ivan-only script. Not invoked by autonomous ticks.
#
# Flow:
# 1. Verify remote configured
# 2. Check for local uncommitted changes (abort if any)
# 3. git fetch origin
# 4. Check if local is behind remote
# 5. If behind: try rebase; if conflict, abort cleanly
# 6. Push to remote (if ahead)
# 7. Report final state
#
# Usage:
#   bash scripts/git_sync.sh           # full sync (fetch + rebase + push)
#   bash scripts/git_sync.sh --fetch   # only fetch + status, no push
#   bash scripts/git_sync.sh --push    # force push attempt (refuses by default)
#   bash scripts/git_sync.sh --dry-run # show what would happen

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$PROJECT_ROOT"

FETCH_ONLY=false
PUSH=false
DRY_RUN=false
BRANCH="main"

for arg in "$@"; do
    case "$arg" in
        --fetch) FETCH_ONLY=true ;;
        --push) PUSH=true ;;
        --dry-run) DRY_RUN=true ;;
        --branch=*) BRANCH="${arg#--branch=}" ;;
        *) echo "Unknown arg: $arg"; exit 1 ;;
    esac
done

red()    { echo -e "\033[31m$1\033[0m"; }
green()  { echo -e "\033[32m$1\033[0m"; }
yellow() { echo -e "\033[33m$1\033[0m"; }
blue()   { echo -e "\033[34m$1\033[0m"; }

echo "🔄 git_sync.sh — sync local with remote"
echo "   Branch:  $BRANCH"
echo "   Fetch:   $([[ $FETCH_ONLY == true ]] && echo "only" || echo "yes")"
echo "   Push:    $([[ $PUSH == true ]] && echo "yes" || echo "no (default safe)")"
echo "   Dry-run: $([[ $DRY_RUN == true ]] && echo "yes" || echo "no")"
echo

# Verify it's a git repo
if ! git rev-parse --git-dir >/dev/null 2>&1; then
    red "❌ Not a git repository: $PROJECT_ROOT"
    exit 1
fi

# Verify remote exists
if ! git remote get-url origin >/dev/null 2>&1; then
    red "❌ No 'origin' remote configured."
    echo "   Run: git remote add origin https://github.com/IvanWeissVanDerPol/paraguay-geodata-vlm.git"
    exit 1
fi

ORIGIN_URL=$(git remote get-url origin)
echo "📡 Remote: $ORIGIN_URL"
echo

# Check for uncommitted local changes
if ! git diff-index --quiet HEAD -- 2>/dev/null; then
    red "❌ Uncommitted local changes. Commit or stash first:"
    git status --short
    echo
    echo "   To commit: make commit"
    echo "   To stash:  git stash push -u -m 'auto-stash'"
    exit 2
fi

# Fetch
echo "📥 Fetching from origin/$BRANCH..."
if [[ $DRY_RUN == false ]]; then
    git fetch origin "$BRANCH" 2>&1 | tail -5
fi
echo

# Check relationship
LOCAL=$(git rev-parse HEAD 2>/dev/null || echo "")
REMOTE=$(git rev-parse "origin/$BRANCH" 2>/dev/null || echo "")
BASE=$(git merge-base HEAD "origin/$BRANCH" 2>/dev/null || echo "")

if [[ -z "$REMOTE" ]]; then
    yellow "⚠️  Remote branch origin/$BRANCH doesn't exist yet."
    echo "   Will need to push first time: bash scripts/git_sync.sh --push"
    REMOTE=""
    BASE=""
fi

if [[ -n "$LOCAL" && -n "$REMOTE" ]]; then
    if [[ "$LOCAL" == "$REMOTE" ]]; then
        green "✅ Local is in sync with origin/$BRANCH"
    elif [[ "$LOCAL" == "$BASE" ]]; then
        yellow "⬇️  Local is behind origin/$BRANCH by $(git rev-list --count HEAD..origin/$BRANCH) commits"
        echo "   Need to pull + rebase (or merge)."

        if [[ $FETCH_ONLY == true || $DRY_RUN == true ]]; then
            yellow "   Skipping due to --fetch or --dry-run"
        else
            echo "   Running: git rebase origin/$BRANCH"
            if git rebase "origin/$BRANCH" 2>&1 | tail -10; then
                green "✅ Rebased successfully"
            else
                red "❌ Rebase conflict. Aborting."
                git rebase --abort 2>&1 || true
                echo "   Resolve manually with: git pull --rebase"
                exit 3
            fi
        fi
    elif [[ "$REMOTE" == "$BASE" ]]; then
        green "⬆️  Local is ahead of origin/$BRANCH by $(git rev-list --count origin/$BRANCH..HEAD) commits"
        if [[ $PUSH == true ]]; then
            echo "🚀 Pushing to origin/$BRANCH..."
            if [[ $DRY_RUN == false ]]; then
                git push origin "$BRANCH" 2>&1 | tail -5
            fi
            green "✅ Pushed"
        else
            yellow "   Not pushing by default. Use --push to push."
            echo "   (Erebus auto-commits but never pushes — Ivan triggers push.)"
        fi
    else
        yellow "🔀 Local and remote have diverged."
        echo "   Ahead:  $(git rev-list --count origin/$BRANCH..HEAD) commits"
        echo "   Behind: $(git rev-list --count HEAD..origin/$BRANCH) commits"
        echo
        echo "   This is unusual. Likely Erebus committed while you also pushed."
        echo "   Resolution:"
        echo "     1. bash scripts/git_sync.sh --fetch  (see what's there)"
        echo "     2. git rebase origin/$BRANCH        (replay your commits on top)"
        echo "     3. Resolve any conflicts"
        echo "     4. bash scripts/git_sync.sh --push  (push result)"
    fi
fi

echo
echo "📊 Final state:"
git log --oneline -5 2>/dev/null || true
echo
git status --short --branch
echo
green "✅ git_sync complete"