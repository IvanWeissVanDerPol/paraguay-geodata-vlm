# 🔑 Credentials Howto — P1 GeoData v2

**This is the one-stop document for getting credentials into Erebus.**

---

## TL;DR

You need 3 P0 services to start:
1. **GitHub** — for pushing code (you already have the repo)
2. **HuggingFace** — for uploading dataset + model (mes 3+)
3. **Copernicus** — for downloading Sentinel-2 (mes 1-2, optional)

Get them in ~10 min total. Then paste them to Erebus via Mensaje or edit `secrets/creds.json`.

---

## P0 — Required now

### 1. HuggingFace (~3 min)

**Why:** Upload the annotated cartographic dataset (~10K features) and the fine-tuned model (Florence-2 / SmolVLM). When: month 3+.

**Steps:**
1. https://huggingface.co/join — register with email (NOT OAuth, OAuth doesn't work for HF API)
2. Confirm email (instant)
3. https://huggingface.co/settings/tokens
4. "New token"
5. Name: `thesis-ivan` (whatever)
6. Type: **Write** (must be write, not read-only, for uploads)
7. "Generate token"
8. **Copy immediately** — starts with `hf_`, ~40 chars

**Pass to Erebus:**
```
hf_token: <your HuggingFace token, starts with hf_, ~40 chars>
hf_username: IvanWeissVanDerPol
hf_dataset_name: paraguay-cartography-annotated
hf_model_name: paraguay-cartography-florence-2
```

---

### 2. GitHub (~1 min, you may already have it)

**Why:** Push code to your repo. You already created https://github.com/IvanWeissVanDerPol/paraguay-geodata-vlm.

**You already passed:** a Personal Access Token (PAT) via Mensaje to Erebus.

**If you want to rotate:**
1. https://github.com/settings/tokens
2. "Generate new token" → "Generate new token (classic)"
3. Note: `thesis-push`
4. Expiration: 90 days
5. Scopes: **`repo`** (Full control of private repositories)
6. "Generate token"
7. Copy immediately — starts with `ghp_`

**Pass to Erebus:**
```
github_token: <your GitHub PAT, starts with ghp_, 40 chars>
github_user: IvanWeissVanDerPol
github_repo: paraguay-geodata-vlm
```

⚠️ **Do NOT rotate while Erebus is actively pushing.** Rotation = downtime until you pass the new token.

---

### 3. Copernicus Dataspace (~5 min)

**Why:** Download Sentinel-2 satellite imagery for Paraguay (~20 GB). When: month 1-2.

**Steps:**
1. https://dataspace.copernicus.eu/
2. "Register" (top-right)
3. Fill: name, email, password
4. Confirm email (instant)
5. Login
6. **No separate API token** — your email + password ARE the credentials

**Pass to Erebus:**
```
copernicus_user: your@email.com
copernicus_pass: your_password_here
```

**Alternative to Copernicus** (free, no signup): cloud-free Sentinel-2 mosaics from https://registry.opendata.aws/sentinel-2/ (uses AWS free tier — see P1 below).

---

## P1 — Optional but useful

### AWS (free tier) — alternative to Copernicus

**Why:** Cloud-free Sentinel-2 mosaics (already processed). Faster than Copernicus for Paraguay.

**Steps:**
1. https://aws.amazon.com/free/ — "Create a free account"
2. Fill in credit card (NOT charged during free tier)
3. Wait for activation (~5 min)
4. https://console.aws.amazon.com/iam/home#/security_credentials
5. "Create access key" → "Command Line Interface (CLI)"
6. Copy both:
   - `Access key ID` (starts with `AKIA`)
   - `Secret access key` (40 chars)

**Pass to Erebus:**
```
aws_access_key_id: <your AWS access key, starts with AKIA, 20 chars>
aws_secret_access_key: <your AWS secret access key, 40 chars>
aws_region: us-east-1
```

---

### Google Cloud — for Open Buildings v3

**Why:** Download Google Open Buildings v3 dataset for Paraguay (~100 MB). When: month 2-3.

**Steps:**
1. https://console.cloud.google.com/ — register, activate free tier ($300 credit)
2. Create a project (any name, e.g. `thesis-paraguay`)
3. Enable Cloud Storage API: https://console.cloud.google.com/apis/library/storage-api.googleapis.com
4. Create service account:
   - https://console.cloud.google.com/iam-admin/serviceaccounts
   - "Create service account"
   - Name: `thesis-thesis`
   - Role: **Storage Object Viewer** (read-only, safe)
5. Click the service account → "Keys" → "Add key" → "Create new" → JSON
6. Save the downloaded JSON file as `gcp-service-account.json`

**Pass to Erebus:**
- Either paste the JSON content via Mensaje (small file)
- Or save it to `/opt/data/thesis-active/secrets/gcp-service-account.json` yourself
- And pass: `gcp_billing_project_id: your-project-id`

---

### Cloudflare R2 — for hosting the web app

**Why:** Host the "Pregúntale al mapa del Paraguay" web app + dataset backups. When: month 5+.

**Steps:**
1. https://dash.cloudflare.com/sign-up
2. Add a payment method (R2 has free tier: 10 GB storage + 10M requests/month)
3. R2 → "Create bucket" (e.g. `paraguay-geodata-vlm`)
4. R2 → "Manage R2 API tokens" → "Create API token"
5. Permissions: **Object Read & Write**
6. Copy:
   - `Account ID` (32 hex chars)
   - `Access Key ID`
   - `Secret Access Key`

**Pass to Erebus:**
```
cf_account_id: <your Cloudflare account ID, 32 hex chars>
cf_r2_access_key: <your R2 access key>
cf_r2_secret_key: <your R2 secret key>
cf_r2_bucket: paraguay-geodata-vlm
```

---

## P2 — For paper submission (month 6-7)

### arXiv (~5 min)

**Why:** Submit paper preprint. When: month 7.

**Steps:**
1. https://arxiv.org/register
2. Fill: name, email, password, institution (UNA)
3. Confirm email
4. Your username + password ARE the credentials

**Pass to Erebus:**
```
arxiv_user: your_username
arxiv_pass: your_password
arxiv_orcid: 0000-0000-0000-0000
```

Also get an **ORCID** (free, do it now): https://orcid.org/register — gives you `0000-0000-0000-0000` format ID for paper authorship.

---

### Zenodo (~3 min)

**Why:** Mint DOI for dataset + model so others can cite them. When: month 6-7.

**Steps:**
1. https://zenodo.org/signup (you can sign in with GitHub!)
2. https://zenodo.org/account/settings/applications/tokens/new/
3. Scopes: **`deposit:write`** and **`deposit:actions`**
4. "Create"
5. Copy the token

**Pass to Erebus:**
```
zenodo_token: <your Zenodo API token, ~50 chars>
```

---

## P3 — Optional, for LLM-assisted writing

### OpenAI / Anthropic

**Why:** Use GPT-4 / Claude to help draft paper sections. Optional.

**OpenAI:**
- https://platform.openai.com/signup
- https://platform.openai.com/api-keys
- "Create new secret key"

**Anthropic:**
- https://console.anthropic.com/
- https://console.anthropic.com/settings/keys
- "Create key"

**Pass to Erebus:**
```
openai_api_key: <your OpenAI API key, starts with sk-, ~50 chars>
anthropic_api_key: <your Anthropic API key, starts with sk-ant-, ~100 chars>
```

---

## 📋 Credential templates

### Minimal (start today)

```json
{
  "services": {
    "huggingface": {
      "token": "hf_xxx",
      "username": "IvanWeissVanDerPol"
    },
    "github": {
      "token": "ghp_xxx",
      "user": "IvanWeissVanDerPol",
      "repo": "paraguay-geodata-vlm"
    },
    "copernicus": {
      "user": "your@email.com",
      "pass": "your_password"
    }
  }
}
```

### Full (for paper submission)

```json
{
  "services": {
    "huggingface": {"token": "hf_xxx", "username": "IvanWeissVanDerPol"},
    "github": {"token": "ghp_xxx", "user": "IvanWeissVanDerPol", "repo": "paraguay-geodata-vlm"},
    "copernicus": {"user": "...", "pass": "..."},
    "aws": {"access_key_id": "AKIA...", "secret_access_key": "...", "region": "us-east-1"},
    "google_cloud": {"service_account_json_path": "/opt/data/thesis-active/secrets/gcp.json", "billing_project_id": "..."},
    "cloudflare_r2": {"account_id": "...", "access_key": "...", "secret_key": "...", "bucket": "..."},
    "arxiv": {"user": "...", "pass": "...", "orcid": "0000-0000-0000-0000"},
    "zenodo": {"token": "..."}
  }
}
```

---

## 🛡️ Security

- **Never** paste tokens in public channels
- **Mensaje DM to Erebus** is acceptable (the conversation is private)
- **Don't commit** `secrets/creds.json` to git (auto-blocked by `.gitignore` + pre-commit hook)
- **Rotate** tokens every 90 days (set a calendar reminder)
- **Use scope:** always use the minimum scope needed (write for HF, repo for GH)

---

## ✅ Verification

After passing creds:
```bash
cd /opt/data/thesis-active
make validate-creds
# Should show: ✅ Schema valid
#              Filled: N
#              Placeholders: 0  ← goal
```

Then Erebus will verify by:
- HuggingFace: list your repos at https://huggingface.co/{username}
- GitHub: list repo collaborators
- Copernicus: try to fetch the catalog (with low quota)
- AWS: list S3 buckets
- Zenodo: list your deposits

---

**Last updated:** 2026-08-10
**Maintained by:** Erebus for Iván Weiss Van der Pol