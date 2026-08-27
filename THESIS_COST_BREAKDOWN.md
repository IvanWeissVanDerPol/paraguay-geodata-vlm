# 💰 THESIS_COST_BREAKDOWN — Iván Weiss Van der Pol · UNA-FADA · P1 GeoData v2

**Purpose:** Single source of truth for money actually spent on the thesis (vs money budgeted / projected). Lives at the repo root so the cost conversation is auditable and not buried in chapters.

**Status (2026-08-27):** 🟢 **Actual spend to date: USD 0.00** — project is fully CPU + open-data + free-tier, no cloud spend incurred, no paid APIs touched. Numbers below are **budgeted / projected** per `Capitulos/Cap1_Introduccion.md` §alcance computacional + `Capitulos/Cap5_Discusion.md` §discusión de resultados + `Capitulos/Cap6_Conclusiones.md` §limitaciones.

**Convention:** all figures in USD unless noted; PYG conversion at 7 300 Gs./USD (Aug 2026 mid-rate) for sanity checks. Conversion is informational only — no PYG has moved.

---

## 1. Budgeted spend (per Cap. 1 §alcance computacional)

| Line item                                | Budgeted USD | When        | Source of truth                                |
| ---------------------------------------- | -----------: | ----------- | ---------------------------------------------- |
| GPU time — single A100 40 GB rental       |       200-500| M2, M4      | `Cap1_Introduccion.md` §98; `Cap5_Discusion.md` §implementación OE3 |
| Domain name (paraguay-cartography.ai)    |         12-15| M7          | FADA submission packet §5                       |
| VPS hosting (Hostinger KVM 2 equiv.)      |        12/mo | M7-M12      | `Cap6_Conclusiones.md` §4 (post-defense hosting) |
| OpenAI / Anthropic evaluation API calls  |       50-150 | M6 (optional) | `Cap3_Metodologia.md` §665 (excluded por costo + reproducibilidad) |
| Storage (R2 / HF Hub datasets free tier) |          0  | M5          | free tier suffices for ~50K features             |
| **Total budgeted (one-time + 6 mo)**      | **300-800**  |             |                                                |

---

## 2. Projected actuals (per Cap. 5 §implementación OE3 + Cap. 6 §6)

| Line item                                | Projected USD | Status                                  |
| ---------------------------------------- | ------------: | --------------------------------------- |
| Florence-2-base QLoRA fine-tune (11h A100)|          47  | `Cap6_Conclusiones.md` §80 + §106       |
| SmolVLM-256M-Instruct QLoRA (extended)   |     ~0.40 elec| `Cap5_Discusion.md` §128 (CPU run)      |
| VPS hosting (post-defense)               |          12/mo| `Cap6_Conclusiones.md` §4               |
| Model + dataset HF Hub uploads           |           0  | free tier                                 |
| **Projected one-time total**             |       ~60    |                                         |
| **Projected recurring (per month)**      |       ~12    | only after defense/public release        |

---

## 3. Actual spend ledger (the only section that matters for "track actual spend")

### 3.1 External services

| Service                         | Date       | Amount USD | Reason / receipt       | Authorized by |
| ------------------------------- | ---------- | ---------: | ---------------------- | ------------- |
| _none yet_                      | —          |          0 | project is sandbox-only|               |

### 3.2 Compute

| Resource                        | Date       | Amount USD | Reason                 | Authorized by |
| ------------------------------- | ---------- | ---------: | ---------------------- | ------------- |
| Local sandbox CPU               | ongoing    |          0 | always-free tier       | n/a           |
| Local sandbox disk              | ongoing    |          0 | 1.2 GB OSM extract on local disk | n/a |

### 3.3 Datasets

| Dataset                         | Source                      | License         | Cost USD |
| ------------------------------- | --------------------------- | --------------- | -------: |
| OSM Paraguay extract (Geofabrik)| https://download.geofabrik.de/osm/south-america/paraguay-latest-free.shp.zip | ODbL  | 0 |
| Sentinel-2 (planned)           | Copernicus / Element84      | free + open     | 0 |
| WorldPop Paraguay (planned)     | worldpop.org                | CC-BY 4.0       | 0 |
| CHIRPS (planned)                | chg.geog.ucsb.edu           | CC-BY 4.0       | 0 |
| Google Open Buildings v3 (planned) | sites.research.google/open-buildings | CC-BY 4.0 | 0 |
| INDI indigenous territories (planned) | UN-Habitat mirror     | open             | 0 |

All planned datasets are free + open-licensed per DATA_MANIFEST.md. **Zero dataset spend incurred or planned.**

### 3.4 Personnel / labor

| Contributor                      | Role               | Hours | Cost USD |
| -------------------------------- | ------------------ | ----: | -------: |
| Iván Weiss Van der Pol           | tesista + author   | ~600h projected (M1-M7) | 0 (own time) |
| Erebus (AI agent, this repo)     | substrate generator| ~40h actual | 0 (sandboxed compute) |
| Future advisor (TBD)             | revisión metodológica | 0h actual | 0 (not yet engaged) |

### 3.5 Other

| Item                             | Date       | Amount USD | Reason                 | Authorized by |
| ------------------------------- | ---------- | ---------: | ---------------------- | ------------- |
| _none yet_                      | —          |          0 |                        |               |

---

## 4. Total actual spend (lifetime)

```
   One-time:    USD     0.00
   Recurring:   USD     0.00 / month
   Grand total: USD     0.00
```

**Status:** 🟢 Zero spend. Project remains entirely within the "free + open + sandbox" envelope authorized by Iván per AUTONOMY.md rule #4 ("NO spending money — no cloud GPU rentals, no paid APIs, no AWS billing — unless Iván explicitly OK'd"). All cost numbers in Cap. 1 / Cap. 5 / Cap. 6 are *projected / modeled* in the manuscript for the reviewer to assess budget realism — not actual spend.

---

## 5. Spend authorization gate

Before **any** spend happens, this is the protocol:

1. Erebus flags a hard blocker (e.g. "GPU compute for fine-tune", "paid API for evaluation", "domain registration").
2. Erebus writes a one-page proposal here: line item + USD estimate + cheapest alternative considered + why free tier won't work.
3. Iván reviews, edits the proposal, and replies in chat with `authorized: <line item> up to <USD ceiling>`.
4. Erebus executes only the authorized line item; logs the receipt + date + USD in §3.1-3.5 above; updates §4 total.
5. Any spend **without** an authorization entry above is unauthorized and a violation of AUTONOMY.md rule #4.

No authorization entries to date → zero spend is correct.

---

## 6. Projected burndown to defense (M12)

Even if all projected items in §1-§2 are eventually incurred (which is the manuscript's modeled scenario, NOT a commitment):

```
  Today (M7)        →   USD     0
  M8  (defense prep) →   USD    60  (one A100 rental for rebuttal figures)
  M9  (publication) →   USD    15  (domain registration if arxiv rejected)
  M10 (post-print)  →   USD    12  (1st month hosting for web app)
  M11 (hosting)     →   USD    12
  M12 (hosting)     →   USD    12
  ────────────────────────────────
  Cumulative M12    →   USD   111  (well below Cap. 1 §98 ceiling of USD 200-800)
```

This is **not a budget commitment** — it's a worst-case model. Iván can stay at USD 0 indefinitely by (a) skipping the rebuttal-figure GPU rental, (b) using arxiv.org free hosting, (c) hosting on a personal machine.

---

## 7. Notes for the monthly review (T137 cadence)

When this file is reviewed each month, the agent should:

1. Read §3 (actual ledger) → confirm zero or note new entries.
2. Read §6 (projected burndown) → adjust if calendar slipped.
3. Read RISK_REGISTER.md §F "Financial risks" → flag any new spending vectors.
4. Append a one-line entry to PROGRESS.md `## <YYYY-MM-DD> — Monthly cost review` with: actual spend / projected / delta / any new authorizations.
5. If a new authorization is needed (e.g. "GPU rental approved for rebuttal figures"), add it to §3.1 with date + Iván's chat-quoted authorization.

---

## 8. Related files

- `Capitulos/Cap1_Introduccion.md` §98 — budget ceiling mentioned in introduction.
- `Capitulos/Cap3_Metodologia.md` §665 — excluded paid APIs + reproducibility rationale.
- `Capitulos/Cap5_Discusion.md` §68 + §128 — actual compute cost model (A100 USD 14.20 for Florence-2, USD 0.40 elec for SmolVLM CPU).
- `Capitulos/Cap6_Conclusiones.md` §4 + §30 + §80 + §106 — post-defense hosting + feasibility of low-cost AI stack.
- `RISK_REGISTER.md` §11-13 — severity rubric includes $ impact thresholds.
- `Capitulos/FADA_TFG_SUBMISSION_PACKET.md` §5 — recursos + disponibilidad table for the FADA committee.
- `AUTONOMY.md` rule #4 — the hard rule: NO spending money unless Iván explicitly OK'd.

---

*Maintained by Erebus per T137 cadence. Review monthly. All entries dated. Zero-actual-spend status as of 2026-08-27.*