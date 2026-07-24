# Google Cloud Competitive Brief — AWS Field Team — Week of 2026-07-22

**Data caveat (read first):** All four sources this week are baseline captures (first look, no prior diff). "Added" content is a snapshot mined for material signals, **not** literal week-over-week deltas. No price *deltas* are computable this week — prior captured values do not exist in `state/`. Prices below are stated as captured values with units. Next week's run will produce true diffs against this baseline.

Sources: `state/_candidates.json`, `sources/gcp.yaml`

## TL;DR

- **Google is retiring 16 open-model Vertex MaaS endpoints on Oct 21, 2026** (DeepSeek, Llama 3.3 70B, Qwen3, GLM, Kimi K2, MiniMax, GPT-OSS, E5 embeddings). Every Vertex customer running open models has a forced migration in ~15 months. Direct Bedrock model-choice wedge — usable *now* in bake-offs and renewals.
- **CSEK (customer-supplied encryption keys) is deprecated on Compute Engine and will be disabled July 20, 2027.** Regulated customers who chose GCP for hold-your-own-key control lose it. Renewal-stage opening.
- **Google SecOps legacy SIEM APIs (Backstory/Ingestion) turn down July 20, 2027**; new instances lose them Oct 26, 2026. Every custom SOC integration must be rewritten regardless of vendor — that rewrite window is a migration-evaluation window.
- **Gemini Enterprise seat pricing is now published: $21/seat/mo (Business) and $30/seat/mo (Standard/Plus)** — Google has committed to a per-seat agent-platform price point that will show up in Amazon Q / Bedrock AgentCore deals. Watch item this week; expect it in discovery calls immediately.
- **New Gemini Flash GAs come with a sampling-parameter lockdown** (temperature/top-K/top-P ignored) and Gemini 3.5 Flash is removed from the Global region Aug 4, 2026 — model churn plus reduced control is a portability talking point.

## Material changes (COMMITMENT)

Ranked by severity. All items T1 unless noted.

### 1. Vertex AI open-model MaaS endpoint retirement — Oct 21, 2026
- **What changed:** 16 model-as-a-service endpoints deprecated, retirement Oct 21, 2026: `deepseek-ocr`, `deepseek-r1-0528`, `deepseek-v3.2`, `deepseek-v3.1`, `glm-5`, `glm-4.7`, `gpt-oss-20b`, `kimi-k2-thinking`, `llama-3.3-70b-instruct`, `minimax-m2`, `multilingual-e5-large/small`, and four Qwen3 variants (incl. `qwen3-coder-480b`). (T1, gcp_release_notes_all)
- **Theme / AWS counterpart:** ai_inference_price → **Bedrock, Trainium, Inferentia**. Deal stage: bake-off and migration.
- **What it means:** Google is consolidating serving capacity behind Gemini. Any customer with production traffic on these endpoints — especially DeepSeek, Llama, and Qwen coder workloads — must re-platform within 15 months. Re-platforming to another Vertex endpoint is not free; re-platforming to Bedrock is the same work.
- **Talk track:** "Google just gave your open-model workloads an eviction date. If you have to migrate anyway, migrate to the platform whose business model depends on model choice — Bedrock serves DeepSeek, Llama, Qwen, and Kimi as first-class managed models, and open weights can run on Trainium/Inferentia for price control."
- **Honest concession:** Gemini Flash-class models are genuinely strong on price-performance, and Google will pitch the retirement as "we'll move you to something cheaper and better." Don't claim the customer's workload will regress — claim they've lost the *option*, and options have contract value.

### 2. Compute Engine CSEK deprecation — disabled July 20, 2027
- **What changed:** Encrypting disks, snapshots, images, and machine images with customer-supplied encryption keys is deprecated and will be **disabled July 20, 2027**. The matching `gcloud` flags are already deprecated. (T1, gcp_release_notes_all)
- **Theme / AWS counterpart:** compute_price / trust-and-control adjacency → **EC2** (EBS + KMS, incl. external key stores). Deal stage: renewal, especially regulated verticals (finserv, public sector, healthcare).
- **What it means:** Customers who architected on GCP specifically because they could supply their own key material at the resource level are being pushed to CMEK (Google-managed KMS with customer keys). For some compliance postures that is a material change requiring re-review — which reopens the platform decision.
- **Talk track:** "Your key-custody model on GCP has an end date. Before you re-architect around Google's KMS, this is the moment to re-evaluate — AWS KMS supports external key stores (XKS) where key material never leaves your HSM, and that capability has no deprecation notice."
- **Honest concession:** CMEK with Cloud EKM covers most of the same compliance ground, and AWS also steers customers toward KMS-managed patterns over raw supplied keys (SSE-C is narrow). The wedge is the *forced re-review*, not a capability GCP can't match.

### 3. Google SecOps legacy SIEM API turndown
- **What changed:** Backstory API (incl. Customer Management API) and Ingestion API deprecated in favor of Chronicle API. **Oct 26, 2026:** new SecOps instances won't support legacy calls. **July 20, 2027:** all legacy endpoints fail for everyone. Applies to custom scripts, integrations, SOAR connectors, ingestion feeds. (T1, gcp_release_notes_all)
- **Theme / AWS counterpart:** No direct battlecard_map theme — closest is data_gravity (security telemetry pipelines) → **S3 / Glue** via Amazon Security Lake (OCSF). Deal stage: renewal.
- **What it means:** Every SecOps customer with custom ingestion or SOAR integrations has a mandatory engineering project. Mandatory rewrites are when SOC teams run alternatives.
- **Talk track:** "You're going to rewrite your ingestion pipelines either way. Security Lake normalizes to OCSF — an open schema — so the next rewrite is the last one tied to a vendor's proprietary API."
- **Honest concession:** Chronicle API is a genuine modernization, migration is API-level not data-level, and Security Lake is a data layer, not a SIEM — the customer still needs analytics on top. Don't oversell it as a Chronicle replacement.

### 4. Batch resource-location breaking change
- **What changed:** Batch jobs can no longer create Compute Engine resources outside the job's region. Grandfathered projects (used `allowedLocations[]` cross-region before July 31, 2026) get until **June 30, 2027**; everyone else sooner. (T1, gcp_release_notes_all)
- **Theme / AWS counterpart:** accelerator_supply → **Capacity Blocks, P5/P6 capacity** (cross-region capacity chasing is how customers cope with GPU scarcity). Deal stage: migration/bake-off for HPC and training-adjacent batch.
- **What it means:** Customers who used cross-region `allowedLocations[]` to hunt GPU/CPU capacity wherever it existed lose that flexibility. On a supply-constrained platform, removing "run it wherever there's capacity" is a real operational regression.
- **Talk track:** "If your batch jobs chase capacity across regions today, GCP is taking that away. AWS Batch has no such restriction, and Capacity Blocks let you *reserve* accelerator capacity ahead of time instead of hunting for it."
- **Honest concession:** Most Batch users run in-region already; this bites a minority — but that minority is exactly the capacity-constrained, high-spend accelerator segment.

### 5. Pricing snapshots captured (baseline — structure, not deltas)
- **What changed:** First capture of GCP compute and Vertex pricing pages. Notables: Spot up to **91% off** on-demand; CUDs up to **70%** (memory-optimized) / **55%** (other); spend-based "Compute flexible CUDs" (Savings-Plans-analog). Vertex accelerators (us-central1, hourly, USD): H100 80GB **$9.797 + $1.469 management fee**, H100 Mega **$11.896**, H200 141GB **$10.709**, a3-highgpu-8g **$101.007**, a4-highgpu-8g **$148.212**, TPU v5e 1-chip **$1.38**, TPU v6e 1-chip **$3.105**, **tpu7x (Ironwood-class) 1-chip $13.80**. Gemini Enterprise Agent Platform pricing page is live. (T1, gcp_pricing_compute + gcp_pricing_vertex)
- **Theme / AWS counterpart:** compute_price → **EC2, Savings Plans, Graviton**; accelerator_supply → **Trainium2/3, P5/P6, Capacity Blocks**.
- **What it means:** Cannot state increases/decreases — no prior values in `state/`. What *is* material: Google publishes list pricing for its newest TPU generation (tpu7x at $13.80/chip-hr) and per-GPU management fees on Vertex. The Vertex **management fee on H100 (+$1.47/hr, ~15% on top of the GPU rate)** is a line item customers often miss in Google quotes.
- **Talk track:** "When you compare that Vertex quote, check for the per-hour management fee on managed prediction — it's a separate SKU on top of the accelerator rate. Ask for the fully-loaded per-hour number, then let's compare against SageMaker/Bedrock fully loaded."
- **Honest concession:** Google's TPU list-price transparency is better than ours for Trainium — sellers should expect customers to ask "what's the equivalent AWS list price per chip-hour" and should have the Trainium2/UltraServer answer ready rather than deflecting. Spot-discount headlines (91% vs our ~90%) are noise; steer to workload-level TCO.

**Migration-friction date table (for QBR slides):**

| GCP change | Customers affected | Hard date |
|---|---|---|
| Gemini 3.5 Flash removed (Global region, Gemini Enterprise) | Gemini Enterprise app users | Aug 4, 2026 |
| 16 open-model MaaS endpoints retired | Vertex open-model inference | Oct 21, 2026 |
| SecOps legacy APIs blocked on new instances | New SecOps provisioning | Oct 26, 2026 |
| Batch cross-region resources (grandfathered) | Cross-region batch/HPC | June 30, 2027 |
| CSEK disabled | Hold-your-own-key compute customers | July 20, 2027 |
| SecOps legacy APIs fully turned down | All SecOps custom integrations | July 20, 2027 |

## Watch (SIGNAL)

- **Gemini Enterprise seat pricing: $21/seat/mo (Business, 1–300 seats, 25 GiB pooled index/seat) and $30/seat/mo (Standard/Plus, unlimited seats, 75 GiB/seat, VPC-SC, CMEK, FedRAMP High/HIPAA support, Gemini Code Assist Standard, ADK/third-party agent bring-in).** (T2, gcp_agentspace) Theme: agent_platform → Bedrock AgentCore, Strands, MCP. This is a published committed price on a T2 marketing page — treat as near-COMMITMENT and expect it in Amazon Q Business / AgentCore discovery calls this quarter. Note the bundling: coding agent + enterprise search + agent runtime in one seat price is the pitch to counter. Track whether the $21/$30 numbers land on an official pricing page (T1) next capture.
- **Gemini 3.6 Flash + 3.5 Flash-Lite GA, with breaking sampling-parameter lockdown** — custom temperature/top-K/top-P are *ignored*. Paired with 3.5 Flash removal from Global region Aug 4, 2026, the pattern is fast model churn plus shrinking knob control. Talk track forming: "on Bedrock, model lifecycle and inference parameters stay under your control; ask Google for their model-deprecation SLA in writing." Watch whether the lockdown extends to Vertex API tiers broadly.
- **Cloud NGFW + WildFire** (Palo Alto malware analysis) — Google buying credibility in network security via partnership. Pressure point for AWS Network Firewall in security-led discovery. Watch for GA/pricing.
- **BYOIP IPv6 reservation for regional external passthrough NLB (Preview)** — IP-portability story that eases *inbound* migration to GCP. Watch for GA; counter is our own BYOIP support — don't let "you can keep your IPs" become a GCP-only claim.
- **Data lineage at org/folder/project level GA** (BigQuery, Managed Spark/Airflow) — data_gravity → Glue/DataZone-adjacent governance. Minor alone; watch as part of the BigQuery-gravity aggregate.
- **Gemini Enterprise BYOID mobile GA** — third-party IdP support removes an enterprise adoption blocker. Minor; feeds the agent_platform aggregate.

## Battlecard deltas

- **ai_inference_price (Bedrock/Trainium/Inferentia):** Add the Oct 21, 2026 MaaS retirement list verbatim to the battlecard — it's checkable by the customer and lands harder than any benchmark. Add the Vertex H100 management fee (+$1.469/hr on $9.797/hr, us-central1) as a quote-scrub item. Prior values: none (baseline) — no delta claimed. Sellers must pull current Bedrock/P5 list pricing before quoting comparisons.
- **compute_price (EC2/Savings Plans/Graviton):** Record baseline: Spot ≤91%, CUD ≤70%/55%, spend-based flexible CUDs ≈ Compute Savings Plans equivalence. No delta claimable this week. Concede discount-structure parity; win on Graviton price-performance and Spot capacity depth, not on discount headline percentages.
- **accelerator_supply (Trainium2/3, P5/P6, Capacity Blocks):** New baseline: tpu7x listed at $13.80/chip-hr; TPU v6e $3.105/chip-hr; regional availability lists captured. Add Batch cross-region restriction as a capacity-flexibility counterpoint. Sellers need a prepared Trainium2 $/chip-hr-equivalent answer — Google's public TPU list pricing will be quoted at us.
- **agent_platform (AgentCore/Strands/MCP):** New baseline: $21/$30 per-seat price points, no-code Agent Designer, ADK + third-party agent bring-in, Model Armor, connector library (M365, HubSpot, Jira). Counter-position: consumption-based AgentCore vs per-seat lock; MCP/Strands openness vs ADK. Concession: Google has a simpler procurement story ("a seat price and a 30-day trial") — don't dismiss it, match it with a scoped pilot offer.
- **data_gravity / egress_terms:** No material candidates this week. No changes.

## Strategic read

Google is concentrating: killing third-party open-model serving, locking Gemini inference parameters, and pushing a seat-priced, vertically integrated agent stack (Gemini Enterprise + ADK + Code Assist). Simultaneously it is shedding legacy control surfaces (CSEK, Backstory APIs, cross-region Batch) — accepting migration friction to simplify its platform. The concession to exploit: Google is trading customer optionality and integration stability for Gemini velocity, which makes "model choice + lifecycle stability + you keep the knobs" the coherent AWS counter-narrative this quarter.

## Gaps (no candidate data this week)

- **gcp_tpu_docs (T2):** No capture — we lack corroboration on Ironwood/tpu7x availability, regions, and reservation terms despite tpu7x *pricing* appearing on the Vertex page. The pricing signal is ahead of the supply signal; treat tpu7x GA/scale claims as unverified until this source lands.
- **gcp_blog_ai (T3):** No capture — no view of customer-win/migration/benchmark claims Google is amplifying. Low direct impact (T3 corroborates, never leads), but we can't pre-brief sellers on Google's marketing pushes.
- **alphabet_earnings (T1):** No capture — expected; source only triggers on a new 8-K filing and Q2 results were not in this window. Watch closely: next Alphabet 8-K will carry Cloud revenue/backlog/capex, which contextualizes the TPU pricing and capacity story above.

## Dropped (with one-line reason each)

- **gcloud routers named-set commands GA** — CLI plumbing; pressures no AWS service in any deal stage.
- **Regional MIG cross-zone repair GA** — incremental resilience parity; no bake-off shows up on this.
- **SecOps SOAR releases 6.3.93/6.3.94** — routine version rollouts, no seller consequence.
- **GKE Ubuntu vulkan-tools removal** — node-image hygiene, no deal relevance.
- **Secret Manager regional secret for DB passwords** — table-stakes feature parity, no wedge.
- **Looker reports deprecated (July 13, 2026)** — real friction but no battlecard theme covers BI; flag to battlecard owners if a QuickSight theme is added.
- **Vertex Featurestore / evaluation / AutoML line-item prices** — captured to baseline for future diffing, but no prior values and no AWS map entries make them non-actionable this week.

---

**Key things worth knowing beyond the brief itself:** this was a baseline week (first capture for all four sources), so next week's run is when true deltas start flowing — especially on the pricing pages. Three sources returned nothing (`gcp_tpu_docs`, `gcp_blog_ai`, `alphabet_earnings`); the tpu7x pricing-without-supply-corroboration gap is the one to close first. Want me to save this brief to a file (e.g., `briefs/2026-07-22.md`)?