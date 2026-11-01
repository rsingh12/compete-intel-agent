# AWS vs. Google Cloud
_Compete Deck — SA-to-SA / SA-to-Customer — November 2026_

---

## Executive Summary

- **BLUF: Google just quietly unified its two biggest 2026 commercial moves — agent-runtime metering and GPU/accelerator pricing — under one "Gemini Enterprise" commit-discount layer, and this pipeline's prior deck (October) missed it entirely. We're fixing that this month, not papering over it.**
- **Genuinely new this run:** the Vertex/Gemini pricing page now carries flat **10% (1-year) / 20% (3-year) "Flexible Savings Plans"** across both the agent-runtime meters (Agent Compute/Memory/Storage) *and* GPU/accelerator infrastructure (A3 instances, A100, T4, V100, P100) — with published billing go-live dates. This mechanism actually went live in September; it surfaced in four consecutive weekly briefs and was never carried into a monthly deck until now. That's on us, and the fix is this deck's main addition.
- **Also new:** Google is rolling out agent-identity plumbing (IAM Helper + MCP Tools) and FinOps guardrails (per-project spend caps, now GA) around that same commit layer — and is onboarding Claude and OpenAI models onto Vertex Model Garden, which directly erodes the "Claude is a Bedrock-exclusive" talking track. Retire that line now.
- **Two hard dates referenced in this pipeline's prior decks have now passed:** the Oct 21, 2026 open-model MaaS retirement and the Oct 26, 2026 SecOps-legacy-API-on-new-instances block. This pipeline still cannot confirm enforcement on either — the one source that would show it (`gcp_release_notes_all`) has been 403'd for 15 consecutive weeks. Treat both as "past the deadline, unverified," not "upcoming."
- **Market positioning:** nothing reverses the July/September/October thesis. Analyst coverage this month adds detail rather than a new verdict — AWS independently confirmed to rank **second** (not just "also a Leader") on both axes of Gartner's AI Infrastructure quadrant, and a second, broader Forrester Wave (Public Cloud Platforms, not just AI Platforms) also names Google a Leader. A claimed Q3 2026 Synergy market-share update was checked and could not be verified as published — we are not citing it, and flag that discipline explicitly below.
- **Customer Evidence:** no new named GCP-to-AWS logo (third month running — Quikr, first reported in September, remains the only named case). New this month: two additional vendor-published, customer-anonymized GCP-to-AWS migration case studies surfaced in search — real and citable, but weaker evidence than a named logo. Use them for pattern corroboration only.

---

## Market Context — Analyst Positioning

- **Gartner Magic Quadrant for Cloud AI Infrastructure (report dated July 6, 2026; re-confirmed, with new detail, this cycle):** 17 vendors evaluated. Leaders: **AWS, Google Cloud, Microsoft, Oracle.** Visionaries: CoreWeave, Nebius, Crusoe. Challengers: Vultr, OVHcloud, Tencent Cloud. Niche Players: Lambda, Cloudflare, Nscale. Google is positioned highest for Ability to Execute and furthest for Completeness of Vision on this AI-infra-specific quadrant — unchanged since July. **New and worth saying plainly: independent coverage (not vendor-sourced) puts AWS second — not merely "also a Leader" — on both axes of this specific quadrant.** Say the rank-order honestly; don't round AWS's position up to parity with Google's on a report where it isn't.
- **Gartner Magic Quadrant for Strategic Cloud Platform Services, 2026 edition (published Sept 1, 2026; unchanged since October):** AWS named a Leader for the 16th consecutive year, highest Ability to Execute. Google Cloud also a Leader (9th consecutive year), furthest for Completeness of Vision on this general quadrant too, not only the AI-infra one.
- **New this month — Forrester Wave: Public Cloud Platforms, Q3 2026 (published mid-September 2026):** a *different*, broader Wave than the "AI Platforms" one cited since July — this one evaluates the 10 most significant public cloud platforms on 30 criteria. Google named a Leader with the highest score in the "current offering" category, including 23 of 30 criteria at the maximum score. **Honest gap:** Google's own write-up of this report does not state AWS's specific score, and this pipeline could not independently confirm AWS's category placement from accessible sources this cycle. Don't claim AWS placement here one way or the other until the report itself is pulled.
- **Forrester Wave: AI Platforms, Q3 2026 (unchanged since September):** Google took the highest overall placement, the maximum Strategy score, and Forrester's "Customer Favorite" designation. AWS is also a Leader, credited for scalable infrastructure plus Bedrock and AgentCore for agent orchestration.
- **Read it straight, not defensively:** across four analyst reports now (two Gartner MQs, two Forrester Waves), the pattern is consistent and not new: Google wins on vision/innovation/current-offering axes, AWS wins on execution track record and, on the AI-infra quadrant specifically, is confirmed second rather than co-leading. Reframe to total platform risk and production-readiness — the same move this deck has made since July — not which vendor's strategy narrative scores highest this quarter.

---

## Market Context — Trends This Quarter

- **Verification discipline, stated plainly:** a search this cycle surfaced what looked like a Synergy Research Q3 2026 hyperscaler market-share release with specific AWS/Azure/Google percentages. A follow-up check could not confirm that release actually exists — Synergy's own site shows no Q3 2026 press release as of today, and a second independent search explicitly stated the Q3 2026 figures aren't published yet. **We are not citing those numbers.** This is the same discipline this pipeline applies to its own blocked sources: if it can't be verified, say so, don't infer. The latest *confirmed* Synergy data remains Q2 2026 (enterprise cloud infrastructure spend $143B, +43% YoY, the fastest growth in eight years; shares AWS 28%, Azure 20%, Google Cloud 15%) — unchanged from the October deck, now simply the most recent verified snapshot rather than "this quarter's" number.
- **Carried forward, unchanged:** Gartner's Aug 10, 2026 AI-optimized IaaS forecast still stands — worldwide AI-optimized IaaS spend at $42B in 2026 (+96%), $66B in 2027, with global inference spend ($23.3B) forecast to overtake training spend ($19B) within 2026 for the first time.
- **New this run — platform branding has churned again.** The pricing page covering Agent Compute/Memory/Storage and GPU rates is now titled "**Gemini platform** pricing," not "Agent Platform" (October's term) or "Vertex AI" (July's term). The page itself states legacy AI Platform/AutoML scale-to-zero support and several lower-cost, lower-performance machine types are not carried into "Inference in Gemini platform." That's the third name for this surface in four months (Vertex AI → Agent Platform → Gemini platform), on top of "Agentspace" becoming "Gemini for Business"/"Gemini agent" at the product layer and "Gemini Enterprise" at the commercial layer.
- **Strategic read:** Google is simultaneously (a) consolidating its AI commercial surface into one legible, discount-bearing "Gemini Enterprise" rate card, (b) building the identity/governance plumbing (IAM Helper, MCP Tools, spend caps) to make that consumption model sellable to risk-averse buyers, and (c) neutralizing AWS's model-choice pitch by onboarding Claude and OpenAI onto its own platform — while still renaming the platform itself every few months. Commercial maturity and naming stability are different claims; don't let a clean new rate card imply the latter.

---

## Architecture Comparison — Compute & Capacity

- **AWS:** EC2 fleet depth across instance families and regions; Capacity Blocks let customers *reserve* GPU/accelerator capacity ahead of need rather than compete for it.
- **Google Cloud:** Compute Engine pricing is byte-identical again on the one line item we could re-fetch this run (no change in this capture). TPU fleet (v6e, tpu7x) pricing is likewise unchanged, now unconfirmed for 15 straight weeks due to the ongoing `gcp_tpu_docs` 403.
- **Open item, carried forward:** last month's capture spotted a new, unpriced Storage-optimized local-SSD family name, "Z4M" (alongside existing Z3/Z4D) — still no rate attached this run. Not battlecard material yet; worth a manual pricing-page check before it surfaces in a customer conversation.
- **Batch/HPC restriction (carried forward, unverified for a fourth straight month):** GCP Batch jobs can no longer create Compute Engine resources outside the job's region (grandfathered accounts until Jun 30, 2027). Last independently confirmed 2026-07-22 — the confirming source has now been unreachable for over fifteen weeks.
- **Wedge, unchanged:** the underlying regression (no cross-region capacity-hunting, on a platform whose CFO has already flagged a capacity ceiling) stands as reported in July. We still cannot re-verify whether the restriction itself moved.

---

## Architecture Comparison — AI/ML Serving

- **AWS:** Bedrock (managed, multi-model) + Trainium/Inferentia (owned silicon) + SageMaker — model choice is the product thesis, unchanged.
- **Google Cloud:** the serving surface is now branded "Gemini platform" (see Market Context). The Oct 21, 2026 retirement of 16 open-model MaaS endpoints (DeepSeek, Llama 3.3 70B, Qwen3 ×4, GLM, Kimi K2, MiniMax, GPT-OSS, embeddings) **has now passed its deadline — 11 days ago as of this deck.** This pipeline cannot confirm enforcement; the confirming source is still 403'ing.
- **New this run:** Claude Opus/Sonnet 5.5 and OpenAI models are now expanding on Google Cloud (Vertex Model Garden / Antigravity), per Google's own blog. This is a direct attack on Bedrock's model-choice differentiator.
- **Concession:** Gemini Flash-class models remain genuinely strong on price-performance, and the MaaS retirement was always a real, dated commitment, not FUD. On the model-choice point: "only AWS has Claude" is no longer an accurate line to use in a bake-off — retire it. Bedrock's differentiator going forward is breadth, Converse API consistency, and guardrails, not exclusivity.
- **Deal stage:** bake-off, migration. Any account that hadn't completed its DeepSeek/Llama/Qwen/GLM/Kimi K2/MiniMax/GPT-OSS/E5 migration off Vertex MaaS by Oct 21 should be treated as past the cliff now — push directly, lead with Bedrock/Trainium/Inferentia as the no-extra-step landing spot, and don't wait on this pipeline to confirm the vendor-side cutover.

---

## Architecture Comparison — Security, Identity & Control Surfaces

- **Encryption/SIEM dates (carried forward, unverified for a fourth straight month, and two now past due):** CSEK disabled Jul 20, 2027 (future, unverified). SecOps legacy APIs blocked on new instances **Oct 26, 2026 — this deadline has also now passed**, 6 days ago; full turndown Jul 20, 2027 (future, unverified). The confirming source (`gcp_release_notes_all`) has 403'd on five consecutive monthly deck cycles.
- **New this run — agent identity, not data-plane security:** Google shipped "IAM Helper" for Agent Skills and MCP Tools — identity/authorization plumbing scoped to the agent runtime, not the encryption/SIEM surfaces above. This is the plumbing that makes the new Gemini Enterprise consumption model (see Feature Deep-Dive) governable at an enterprise security-review stage.
- **AWS position, unchanged:** KMS External Key Stores (XKS) carries no deprecation notice. Security Lake (OCSF, open schema) remains the pitch for the SecOps rewrite. AgentCore's identity and MCP tool-governance model is the direct counter to Google's IAM Helper.
- **Concession, unchanged:** CMEK with Cloud EKM and Chronicle API are genuine modernizations, not downgrades. The wedge is the forced re-review window and the now-passed-but-unconfirmed deadlines, not a unique AWS capability.
- **What's actually new:** two of the three hard 2026/2027 dates this deck has tracked since July have now passed the calendar without this pipeline able to confirm what happened on Google's side. That is itself worth saying in any QBR: a competitive deck that has had to carry "deadline passed, enforcement unconfirmed" for two consecutive items is a data point about source reliability, independent of which vendor it's describing.

---

## Feature Deep-Dive — Model Choice & Lock-In

- **Evidence:** 16 Gemini-platform MaaS endpoints' retirement deadline (Oct 21, 2026) has passed; enforcement unconfirmed. Gemini Flash models still ignore custom temperature/top-K/top-P (unchanged since July).
- **AWS counter:** Bedrock serves DeepSeek, Llama, Qwen, and Kimi as first-class managed models today; open weights also run on Trainium/Inferentia for price control.
- **New wrinkle this month:** Claude and OpenAI models are now expanding on Vertex Model Garden. This cuts both ways — concede it plainly. It removes "exclusivity" as a Bedrock argument, but it also means a customer evaluating "where do I run Claude" now has a real Google-side option to weigh, not just an AWS one.
- **Talk track, updated:** "The migration deadline already passed — if the cutover work already happened, or is happening now under pressure, the question isn't 'can I get Claude elsewhere,' it's 'whose platform is my business model better protected by.' Bedrock's thesis is model choice as a permanent feature, not a transitional one."
- **Deal stage:** bake-off, migration — this is a live cutover conversation, not a future-date flag.

---

## Feature Deep-Dive — Accelerator Supply

- **Evidence (still unverified at the source):** Google CFO's Q2 2026 admission ("revenue would have been higher if we were able to meet the demand") and the $514B backlog figure are unchanged since July — the SEC EDGAR source that would surface a Q3 update is still 403'ing, now for 15 weeks. Synergy's Q2 2026 figures (Google Cloud revenue +82% YoY, fastest of the three hyperscalers) remain the latest independently corroborating data point; no Q3 2026 Synergy release could be confirmed this cycle (see Market Context).
- **AWS counter, unchanged:** Capacity Blocks for ML — reserve accelerator capacity ahead of time instead of competing for it during a publicly admitted shortage.
- **Concession, unchanged:** a customer already committed to GCP with backlog priority may get preferential allocation over a net-new AWS evaluation running the same capacity argument in reverse.
- **Deal stage:** competitive bake-off, especially training-adjacent workloads. Keep citing the Q2 figures as "last confirmed," not "current quarter."

---

## Feature Deep-Dive — Pricing Transparency & Structure

- **Evidence, now confirmed stable across five consecutive monthly captures (Jul 22, Aug 24/31, Sep 28, Oct, and this run):** H100 80GB at $9.79655/hr base + $1.4695/hr management fee = $11.266/hr fully loaded; TPU v6e (1-chip) $3.105/hr; tpu7x (1-chip) $13.80/hr. Five months of byte-identical pricing is a materially stronger claim than July's single-snapshot baseline.
- **AWS counter, unchanged:** ask for the fully-loaded per-hour Gemini-platform number before comparing to SageMaker/Bedrock — the management fee is still a separate line item customers miss in Google quotes.
- **Concession, unchanged:** Google's TPU list-price transparency remains genuinely better than AWS's Trainium equivalent. Sellers should walk in with a current Trainium2/UltraServer $/chip-hr number.
- **Deal stage:** quote scrub, TCO conversation.

---

## Feature Deep-Dive — Gemini Enterprise Flexible Savings Plans Now Span Agent Runtime and GPU Infrastructure

- **What changed, and why this is the headline of this month's deck:** this pipeline's own weekly briefs first flagged a "Gemini Enterprise Flexible Savings Plan" in September 2026 — a flat **10% (1-year) / 20% (3-year)** term-commit discount. It has been live and stable since, but neither the September nor the October monthly compete deck carried it. This run confirms it now spans two distinct commercial surfaces under one discount mechanism:
  - **Agent runtime:** Agent Compute $0.085/vCPU-hr → $0.0765 (1yr) → $0.068 (3yr); Agent Memory $0.009/GiB-hr → $0.0081 → $0.0072; Agent Storage ≈$0.30/GiB-month → proportionally discounted at the same 10%/20%.
  - **GPU/accelerator infrastructure:** a3-ultragpu-8g $96.02/hr → $86.41 (1yr) → $76.81 (3yr); a3-megagpu-8g $106.65/hr → $95.99 → $85.32; A100 80GB $4.517/hr → $4.066 → $3.614; and flat 10%/20% on older T4/V100/P100 parts as well.
  - **Billing go-live dates are now published, not just rates:** Agent Gateway since Jul 13, 2026; Memory Bank, Sessions, and Skill Registry since Sep 1, 2026; Semantic Governance Policy billing "later in 2026" — language that has been internally inconsistent across this pipeline's own weekly captures and should not be quoted as a firm date.
- **Honest caveat #1 — it is not a blanket 20% off anything:** this pipeline's own September capture found a real discount asymmetry: H100 80GB's *base* accelerator rate carries no 1yr/3yr discount column at all, but its ~15%-of-base management-fee overlay *does* discount 10%/20%. H200 141GB is the mirror case — the base rate discounts, the management fee is listed "Unavailable" for both terms. Quote this per-SKU; "20% off everything" is a claim the data won't support if challenged.
- **Honest caveat #2:** the management fee is a separate SKU from the base GPU rate on every multi-year quote, same as on-demand — ask for it explicitly.
- **AWS counter:** AgentCore bills consumption per component and AWS Savings Plans/EDP discounting applies across the whole account — compute, storage, and inference together — not a single product-scoped savings plan. The honest comparison is total-account commit economics, not a single SKU's rate card.
- **Concession:** a single, flat, easy-to-model 10%/20% commit discount spanning both agent runtime and GPU infra is genuinely more legible to a FinOps buyer than AWS's multi-mechanism discount story (Savings Plans + EDP + Capacity Blocks). Don't dismiss the simplicity — counter it with a worked AgentCore TCO sheet, not a shrug.
- **Deal stage:** renewal, migration, multi-year TCO conversation — this is usable today. Any account being pitched a multi-year Gemini Enterprise commitment needs an AWS TCO counter now, not next quarter; the metering it's committing against (Memory Bank/Sessions/Skill Registry) has had barely two months of live billing history.

---

## Feature Deep-Dive — Agent Platform Consumption Metering & Seat Pricing

- **Evidence, unchanged since September, re-confirmed stable this run:** Gemini Enterprise runs three billed resource types for agent runtime — Agent Compute, Agent Memory, Agent Storage (see prior slide for rates) — plus Memory Bank read/write operations billed through the same Agent Compute meter (1 vCPU-hr per 3M reads, per 1M writes).
- **Seat ladder, unchanged:** Gemini Enterprise's $0-seat-fee PAYG edition (20+ seats) sits alongside Business ($21/seat/mo, ≤300 seats) and Standard/Plus ($30/seat/mo, unlimited).
- **AWS counter, unchanged:** Amazon Q Business / Bedrock AgentCore remain consumption-based with no per-seat floor and no separate multi-meter stack to reconcile.
- **Concession, unchanged:** the PAYG tier is a genuine procurement simplification. Procurement simplicity and billing simplicity are still different claims — a workload touching Runtime + Memory Bank + Gateway now reconciles four meters against four free-tier thresholds, *and* against the new Flexible Savings Plan discount tiers layered on top.
- **Deal stage:** discovery, bake-off — ask any active Gemini Enterprise prospect for a fully-loaded worked example across all meters, at whatever commit term they're being quoted, before comparing to a Bedrock/AgentCore consumption quote.

---

## Feature Deep-Dive — Agent Identity, MCP Governance & FinOps Guardrails

- **Evidence, new this run (tier-3 blog signal, escalated because it corroborates the tier-1 pricing commitment above):** Google shipped "IAM Helper" scoped to Agent Skills and MCP Tools — per-agent identity and authorization plumbing — alongside per-project spend caps that are now **generally available** (a workload "pauses instead of overspending" once it hits a budget ceiling).
- **Why this is SIGNAL, not noise:** identity/governance and FinOps guardrails are exactly the two things a security and procurement review asks for before approving a consumption-based, multi-meter commitment like the one on the prior two slides. This is Google building the enterprise trust layer underneath its own new pricing model, not a standalone feature announcement.
- **AWS counter:** Bedrock AgentCore's identity and MCP tool-governance model, plus AWS Budgets/Budget Actions/Cost Anomaly Detection for the FinOps side — AWS's version of both pieces already exists and is more battle-tested, but Google's "hard pause" framing on spend caps is a clean, concrete talking point. Don't contest it; match it.
- **Deal stage:** discovery, security review — expect "how does AWS handle per-agent identity and MCP tool governance, and can a workload hard-stop at a budget cap" to surface in any Gemini Enterprise bake-off from here on.

---

## Feature Deep-Dive — Vector Search / RAG Storage Economics

- **Evidence, confirmed stable, unchanged since October:** Gemini-platform Vector Search's "Storage-Optimized" tier bills Capacity Units at $2.30/hr per replica (includes up to 1 TiB active SSD, auto-scaling) plus Write Units at $0.45/GiB for index writes. The "Performance-Optimized" tier runs $0.065/hr per CU (1yr: $0.0585, 3yr: $0.052), bundling 2GiB RAM, for latency-sensitive smaller indexes.
- **AWS counter:** OpenSearch Serverless and Bedrock Knowledge Bases price on OCU-hours and ingested/stored data respectively — ask for a same-corpus-size, same-QPS comparison against whichever tier the customer is actually quoted.
- **Concession:** two clearly-scoped CU tiers (cost-per-TB for large corpora vs. cost-per-replica for latency-sensitive smaller ones) is a reasonable simplification over the old per-VM node pricing it replaced.
- **Deal stage:** discovery — confirm which CU tier a customer's quote actually uses, and note the Performance-Optimized tier also now carries a 1yr/3yr Flexible Savings Plan discount, consistent with this month's broader pattern.

---

## Pricing & TCO — Apples-to-Apples Snapshot

| Item | Google Cloud (captured) | AWS equivalent |
|---|---|---|
| H100 80GB, on-demand | $9.797/hr + $1.469/hr mgmt fee = $11.266/hr fully loaded (stable 5 captures) | Compare fully-loaded P5 rate — pull current list before quoting |
| H100 80GB, 3yr Flexible Savings Plan | Base rate: **no discount.** Mgmt fee only: $1.469 → $1.175/hr (20% off) | Compare current P5 Savings Plan / Capacity Blocks combination |
| H200 141GB, 3yr Flexible Savings Plan | Base rate: $10.709 → $8.567/hr (20% off). Mgmt fee: "Unavailable" for discount | Compare current P5e/P6 equivalent |
| TPU v6e (1-chip) | $3.105/hr (stable 5 captures) | Compare current Trainium2 $/chip-hr |
| tpu7x / Ironwood-class (1-chip) | $13.80/hr (list; supply unconfirmed 15+ weeks) | Compare current Trainium3 $/chip-hr |
| a3-ultragpu-8g, 3yr Flexible Savings Plan | $96.02/hr → $76.81/hr (20% off) | Compare current P5/P5e instance + Savings Plan |
| A100 80GB, 3yr Flexible Savings Plan | $4.517/hr → $3.614/hr (20% off) | Compare current P4d + Savings Plan |
| Agent Compute, 3yr Flexible Savings Plan | $0.085/vCPU-hr → $0.068/vCPU-hr (20% off) | Bedrock AgentCore — consumption-based, no term-commit SKU |
| Vector Search, Storage-Optimized CU | $2.30/hr per CU (incl. 1 TiB SSD) + $0.45/GiB write | OpenSearch Serverless / Bedrock Knowledge Bases — request matched-corpus quote |
| Vector Search, Performance-Optimized CU | $0.065/hr per CU, 3yr $0.052/hr (incl. 2 GiB RAM) + $0.45/GiB write | Same — confirm which CU tier before comparing |
| Agent platform seats | $0 (PAYG) / $21 / $30 per seat/mo | Consumption-based (Bedrock AgentCore), no seat floor |

*Compute, TPU, Agent Compute, and Vector Search base rows verified stable across five captures (07-22, 08-24/31, 09-28, 10-26, and this run, 11-01). The Flexible Savings Plan columns are new to this deck, not new to the market — they've been live since September. TPU supply/availability and the earnings-derived rows remain unconfirmed due to the ongoing 15-week source outage — refresh before every quote regardless.*

---

## Pricing & TCO — The Hidden Line Items

- **The management-fee asymmetry is now a multi-year problem, not just an on-demand one:** H100's management fee discounts under the Flexible Savings Plan but its base rate doesn't; H200 is the reverse. A 3-year commitment quote that doesn't itemize both lines separately will misstate the real multi-year total either way — ask for both lines, discounted and undiscounted, before signing off on any TCO comparison.
- **The agent-runtime meter cluster, unchanged since September:** a single agent workload can touch Agent Compute, Agent Memory, Agent Storage, and Memory Bank read/write operations simultaneously — four meters, four free-tier thresholds, now each with its own Flexible Savings Plan discount column. Ask any Gemini Enterprise TCO model whether it accounts for all four, at whatever term they're quoting.
- **Vector Search tier selection remains a hidden line item:** a customer's quoted rate depends on which CU tier (Storage- vs. Performance-Optimized) their workload lands in, and now also on whether a commit term is applied — confirm both before comparing to an AWS number.
- **Forced migrations are still TCO, not just engineering cost, and two are now overdue:** the Oct 2026 MaaS retirement and the Oct 26 SecOps new-instance block have both passed their deadlines with enforcement unconfirmed — quantify the re-platforming cost in any GCP-retention TCO model regardless of whether Google has flipped the switch yet.

---

## Pricing & TCO — Migration-Friction Date Table (for QBR use)

| GCP change | Customers affected | Hard date | Verification status |
|---|---|---|---|
| 16 open-model MaaS endpoints retired | Gemini-platform open-model inference | Oct 21, 2026 — **passed, 11 days ago** | Deadline confirmed; enforcement **unconfirmed**, 15+ weeks |
| SecOps legacy APIs blocked on new instances | New SecOps provisioning | Oct 26, 2026 — **passed, 6 days ago** | Deadline confirmed; enforcement **unconfirmed**, 15+ weeks |
| Gemini Enterprise Flexible Savings Plans (agent runtime + GPU) | Any multi-year Gemini Enterprise commitment | Live since Sep 2026 | Confirmed this run, stable |
| Memory Bank / Agent Runtime / Gateway metering | Gemini-platform agent builders | Live since Jul 13 / Sep 1, 2026 | Confirmed this run, stable |
| Batch cross-region resources (grandfathered) | Cross-region batch/HPC | Jun 30, 2027 | **Unconfirmed, 15+ weeks** — release notes source 403 |
| CSEK disabled | Hold-your-own-key compute customers | Jul 20, 2027 | **Unconfirmed, 15+ weeks** — release notes source 403 |
| SecOps legacy APIs fully turned down | All SecOps custom integrations | Jul 20, 2027 | **Unconfirmed, 15+ weeks** — release notes source 403 |

---

## Customer Evidence — What We Can Cite Today

- **No new named GCP-to-AWS logo surfaced this month — third consecutive month.** The best citable case remains **Quikr**, India's largest classifieds marketplace (30M+ monthly users), which migrated 47,965 BigQuery tables and ~150–200 TB from Google Cloud to AWS with partner CloudThat (Amazon EMR on Spot EC2 for the data move, Amazon Athena serving the analytics layer). First reported in September, re-confirmed with added technical detail in October, unchanged this month.
- **New this month — two additional vendor-published, customer-anonymized GCP-to-AWS case studies, lower evidentiary tier than Quikr:**
  - **Datamatics** (AWS partner) published case-study pages describing a migration of a "leading communications provider for schools in Australia" from Google Cloud to AWS — moving off GCP-hosted Redis-on-VMs and Kubernetes onto AWS Elastic services, isolating the auth module, and phasing in Cloudflare. **Caveat worth stating out loud:** different published versions of this same-sounding engagement report inconsistent outcome metrics (one cites 42% lower traffic congestion and 25% efficiency gain; another, framed as a multi-cloud consolidation, cites 19% lower TCO, 32% efficiency, and 10% more schools registered). Treat as one vendor's real but internally inconsistent self-reported case, not two corroborating wins — verify the live page before quoting any specific number externally.
  - **Kunai** published a case study describing a "Top 5 U.S. bank" integrating an acquisition's Google Cloud environment onto the parent company's AWS infrastructure (AWS DMS for the data move, application refactoring for AWS-specific services). No metrics given, customer unnamed.
- **Also citable:** the Gartner Magic Quadrant for Strategic Cloud Platform Services — AWS Leader for 16 consecutive years, highest Ability to Execute (analyst-level evidence, not a customer testimonial, usable alongside the Quikr reference).
- **Deal stage:** reference-selling, migration discovery. Quikr remains the best-fit reference for classifieds/marketplace and large-BigQuery-estate accounts; the Datamatics and Kunai cases are directionally useful ("this keeps happening across industries, vendors, and deal sizes") but not individually strong enough to lead a pitch.

---

## Customer Evidence — The CRM Gap Is Still Open

- **This pipeline still has no CRM/Salesforce feed and no case-study database** — it monitors public GCP and AWS-partner surfaces only. Finding Quikr, Datamatics, and Kunai was live web search against public case-study indexes, not a pipeline capability upgrade; the structural gap flagged every month since July is unchanged.
- **Do not present fabricated logos, quotes, or win counts.** Field/sales leadership: supply real, named, recent wins from CRM before this section goes in front of a customer — three search-sourced cases, however corroborating as a pattern, are not a substitute for your own pipeline data.
- **AWS's public case-study library** (aws.amazon.com/solutions/case-studies) remains the fallback resource for sourcing a same-industry reference while this gap stays open.
- **Action for next month's deck, unchanged:** field teams should submit any GCP-to-AWS win (even anonymized/logo-blind) so this section grows with verified internal data instead of leaning on search-sourced vendor pages a fourth month running.

---

## Customer Evidence — Reference-Selling Guidance

- **Best-fit use of the Quikr story, unchanged:** classifieds/marketplace platforms and any account with a large BigQuery analytics estate considering a replatform.
- **Use the Datamatics and Kunai cases only as pattern evidence, not as standalone proof points:** "independent vendors, across schools-communications and banking, are separately publishing GCP-to-AWS migration work this year" is a defensible, honest claim. "Here are three customer wins" is not — Datamatics' and Kunai's customers are both anonymized, and Datamatics' own metrics disagree with themselves across two published versions.
- **If a customer or their GCP rep cites a headline market-share or analyst number you haven't independently verified this month, check it before repeating it** — this deck itself caught and discarded an unverifiable Q3 2026 Synergy figure this cycle. The discipline that applies to Google's claims applies to ours too.
- **Standing ask to field, unchanged:** anonymized/logo-blind wins are still the fastest way to close this section's gap — they don't need to be customer-presentable to be useful internally for the next deck.

---

## Objection Handling — "Google's new Flexible Savings Plan beats anything AWS offers on a multi-year commit"

- **Objection:** "Google gives me one rate card with a flat 20% off for a 3-year commit, across both my agent spend and my GPUs. What's AWS's equivalent number?"
- **Response:** The simplicity is real, and sellers should bring a worked AgentCore + Savings Plans + EDP number to the meeting rather than arguing the mechanism. But ask them to itemize the quote: on H100, the 20% applies to the management fee, not the base accelerator rate; on H200, it's the reverse. A "flat 20% off everything" headline doesn't survive a SKU-by-SKU read of their own pricing page — ask for that read before comparing totals.

---

## Objection Handling — "Claude and OpenAI models are on Google Cloud now too — your model-choice pitch is gone"

- **Objection:** "You used to say Bedrock was the place to run Claude. Google just put Claude and OpenAI models on Vertex Model Garden."
- **Response:** Accurate, and we're not disputing it — retire the exclusivity line. What doesn't change: Bedrock's model-choice thesis was never "exclusive access," it was breadth, a consistent Converse API across providers, and guardrails that work the same way regardless of which model is behind them. Ask whether the Google quote includes the same cross-model consistency, or a different integration per model.

---

## Objection Handling — "Two of your deprecation dates already passed — doesn't that prove nothing happened?"

- **Objection:** "You've been warning about the Oct 21 MaaS retirement and the Oct 26 SecOps API block for months. Both dates are past. If it mattered, wouldn't we have heard?"
- **Response:** Fair question, and the honest answer is this pipeline genuinely cannot confirm enforcement either way — the one source that would show it has been blocked for 15 weeks. That's not evidence nothing happened; it's an evidence gap, and we're saying so rather than guessing. The actionable move is the same regardless: confirm directly with the account whether their migration off the retired endpoints or legacy SecOps APIs is actually done, and lead with the AWS landing point either way.

---

## Objection Handling — "This all sounds like it cuts both ways"

- **Objection:** "You're citing Google's own admissions and a pipeline outage you can't fix — doesn't AWS have comparable gaps?"
- **Response:** Yes, and pretending otherwise would be a battlecard nobody trusts. AWS has its own supply-constrained GPU story, its own multi-mechanism (not single-rate-card) discount structure that's genuinely less legible than Google's new one, and this deck just discarded an unverifiable market-share figure rather than use it. The differentiator isn't "AWS has no gaps" — it's a 16-year execution track record and a willingness to say "unconfirmed" instead of filling gaps with marketing.

---

## Call to Action

- **Next steps:** pull current Bedrock/Trainium/P5 list pricing and AWS Savings Plans/EDP terms before any Gemini Enterprise Flexible Savings Plan comparison — this deck's captured numbers are real but will date quickly, especially the new multi-year discount columns.
- **Field correction from this cycle:** the Gemini Enterprise Flexible Savings Plan (agent runtime + GPU, flat 10%/20%) has been live since September and is usable in active deals today — don't wait for next month's deck to start using it; it should already be in any multi-year Gemini Enterprise competitive conversation.
- **Pipeline ask, now a fifth consecutive month:** this deck's confidence depends on `gcp_release_notes_all`, `gcp_tpu_docs`, and the SEC EDGAR feed coming back online (15+ weeks down). Two hard deadlines have now passed without this pipeline able to confirm enforcement — escalate provisioning a `PERPLEXITY_API_KEY` or unblocking those domains before a third deadline passes unverified.
- **Resources:** `sources/gcp.yaml` battlecard map, weekly Intelligence Brief (`artifacts/weekly-intelligence-brief-*.md`), this deck's markdown source (`decks/compete-deck-gcp-vs-aws-*.md`) for editing before a specific customer conversation.
- **Deal support:** for the Migration-Friction Date table, the Customer Evidence section, or the Flexible Savings Plan TCO comparison, loop in field leadership before presenting externally — this deck is a competitive-intel starting point, not a final customer-facing asset without a named-logo pass and independent source verification.
