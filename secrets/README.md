# secrets/ — Credentials Bundle

**This directory holds Iván's credentials. NEVER commit its contents.**

## Files

| File | Purpose |
|---|---|
| `creds.json` | The actual credentials bundle. Edit before passing to Erebus. |
| `creds.schema.json` | JSON Schema for validating `creds.json`. Run `python3 scripts/validate_creds.py` before passing. |
| `README.md` | This file. |

## File permissions

```bash
chmod 700 secrets/
chmod 600 secrets/creds.json
```

These permissions ensure only the owner can read/write. Anything else in the dir gets the same group/world lockdown.

## Workflow

### 1. Iván fills creds.json

Open `secrets/creds.json` in your editor. Replace each `FILL_ME_*` placeholder with the real value, or leave the placeholder if you want to defer (set `"skip"` for ones you don't have).

### 2. Iván validates

```bash
make validate-creds
# or
python3 scripts/validate_creds.py
```

### 3. Iván passes to Erebus

Two options:

**Option A (recommended): paste into WhatsApp DM to Erebus.**

Open `secrets/creds.json` and paste the contents as one code block. Erebus will:
1. Save it to `/opt/data/thesis-active/secrets/creds.json` on his end (sandbox already isolated).
2. Validate against `creds.schema.json`.
3. Echo back which services got valid creds.
4. **Immediately** rewrite the file in-place with the actual values swapped in (your local copy stays as `FILL_ME_*`; only Erebus's sandbox has the real values).

**Option B (more secure): use age / gpg encryption.**

```bash
# Iván's machine
age -r erebus_public_key.txt secrets/creds.json > secrets/creds.json.age
# Send the .age file via WhatsApp / email
```

Erebus decrypts with his private key. Same end result, but the file is encrypted in transit.

### 4. After use

Erebus stores creds only in `/opt/data/thesis-active/secrets/creds.json` (sandbox file system). They are:
- **NOT** committed to git (`.gitignore` blocks `secrets/creds.json`).
- **NOT** sent to any external service except the ones Iván specified.
- **NOT** logged to console output.
- **NOT** echoed back to the chat after the initial load confirmation.

To rotate a credential: edit `creds.json`, re-run `make validate-creds`, re-paste to Erebus.

## What Erebus does with each service

| Service | Used for | When |
|---|---|---|
| `huggingface` | Upload dataset + model weights | Month 3-7 |
| `copernicus` | Download Sentinel-2 imagery | Week 1-2 |
| `aws` | Cloud-free Sentinel-2 mosaics (alt to Copernicus) | Week 1-2 |
| `github` | Push code to repo | Week 1 |
| `google_cloud` | Open Buildings v3 download | Week 2-3 |
| `cloudflare_r2` | Dataset + model backup, optional web hosting | Month 5+ |
| `arxiv` | Submit paper preprint | Month 7 |
| `zenodo` | Mint DOI for dataset + model | Month 6-7 |
| `openai` / `anthropic` | LLM-assisted paper writing | Optional |
| `una` | Final enrollment at FADA | Month 8+ (when advisor phase) |

## What Erebus will NEVER do

- ❌ Send credentials to any third party (no telemetry, no analytics).
- ❌ Echo them back in the chat after loading.
- ❌ Commit `secrets/creds.json` to git.
- ❌ Use them for anything outside this thesis project.

## What Erebus WILL do

- ✅ Load them into environment variables / config files inside the sandbox.
- ✅ Use them to call the services above for their stated purposes.
- ✅ Tell you which credentials were loaded successfully.
- ✅ Tell you which were skipped.
- ✅ Refuse to proceed if a P0 credential is missing for a step that needs it.

## Rollback / cleanup

To wipe Erebus's access at any point:

```bash
# Iván's command
echo "Erebus, wipe credentials" > /tmp/msg.txt
# send via WhatsApp
```

Erebus will:
1. Delete `secrets/creds.json` on his sandbox.
2. Invalidate any session tokens loaded in env.
3. Rotate any API keys used (where the service supports it).
4. Confirm: "creds wiped. Next operation requires re-paste."

---

**Status:** Empty template. Iván fills, validates, and passes.
**Last updated:** 2026-08-10