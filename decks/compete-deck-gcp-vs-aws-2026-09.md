# AWS vs. Google Cloud
_Compete Deck — SA-to-SA / SA-to-Customer — September 2026_

---

## Executive Summary

- **BLUF: The July thesis holds — and this month Google made it structural, not just financial.** In July we said Google's capacity ceiling was creating forced migrations. This month Google finished collapsing "Vertex AI" into a single "Agent Platform" brand and turned on consumption metering across it — the same platform, now billed by more meters.
- **Genuinely new since July:** Memory Bank metered billing goes live **today, September 1, 2026** (previously a future date, now in effect); a new Agent Runtime consumption meter ($0.085/vCPU-hr per 15,000 agent evaluations) shipped in August; Gemini Enterprise added a **$0-seat-fee pay-as-you-go edition**; and a new Storage-Optimized Vector Search pricing tier appeared this week.
- **Unchanged and worth saying plainly:** H100/TPU list pricing, discount ceilings, and the Oct 21 MaaS retirement list have not moved since July — three independent captures now confirm the same numbers. Don't manufacture urgency where there isn't any.
- **Honesty flag for this deck:** this pipeline's Tier-1 release-notes and earnings sources have returned `403 Forbidden` for six consecutive weeks. Every hard deprecation date carried forward from July (CSEK, SecOps, Batch cross-region) is **unconfirmed this month**, not re-verified. Say so out loud in any QBR that leans on those dates.
- **New this month:** a real, named, citable GCP-to-AWS migration (Quikr, India's largest classifieds platform) — see Customer Evidence. The CRM-feed gap that produced last month's "no case study" flag is still open; this is one field-sourced example, not a fix to the underlying gap.

---

## Market Context — Analyst Positioning

- **Gartner Magic Quadrant for Strategic Cloud Platform Services:** still the 2025 edition (no 2026 refresh has published) — AWS remains a Leader for the 15th consecutive year, highest Ability to Execute. Unchanged since July.
- **Gartner Magic Quadrant for AI Infrastructure (inaugural, published July 2026):** Google Cloud, AWS, and Azure all named Leaders. Google is positioned highest for Ability to Execute and furthest for Completeness of Vision. New detail this month: Gartner characterizes **AWS as the industry's "most extensive and mature cloud infrastructure"** for AI workloads, with a specific, narrower caution — networking and cluster design can introduce latency constraints for the largest distributed-training jobs.
- **New this month — Forrester Wave: AI Platforms, Q3 2026** (15 vendors evaluated): Google took the highest overall placement, the maximum Strategy score, and Forrester's "Customer Favorite" designation. AWS is also named a Leader, credited for scalable infrastructure plus Bedrock and AgentCore for agent orchestration.
- **Read it straight:** Google now leads one general quadrant's vision axis and one platform-specific Wave's strategy axis. Don't contest either. The reframe is the same one from July — total platform risk and execution track record over any single benchmark axis — now with a second analyst firm on the board, not just one.

---

## Market Context — Trends This Quarter

- **The rebrand finished:** the page formerly titled "Vertex AI Pricing" is now "Gemini Enterprise Agent Platform Pricing." This isn't cosmetic — the same rebrand that folded Agentspace into Gemini Enterprise in prior quarters has now folded Vertex AI's ML/AutoML pricing under the same "Agent Platform" umbrella. Expect customers to use "Agent Platform" and "Vertex AI" interchangeably for a while; sellers should too, but confirm which SKUs a customer means before quoting.
- **Metering keeps expanding on the same front door:** Agent Gateway (billing since Jul 13), Agent Runtime/Agent Compute ($0.085/vCPU-hr per 15,000 evaluations, new in August), and now Memory Bank (billing starts today, Sep 1) — three metered layers added to the platform within eight weeks, while the headline seat price ($21/$30, plus a new $0 PAYG tier) stays simple. Same strategic read as July, now with a third data point: monetize the plumbing, keep the marquee number simple.
- **Pipeline blindness is now a six-week-old, unresolved problem, not a one-off:** `gcp_release_notes_all` (T1), `gcp_tpu_docs` (T2), and the SEC EDGAR 8-K index (T1) have returned 403 since 2026-07-27. `PERPLEXITY_API_KEY` is still unset, so the documented fallback still can't engage. Two of three blocked sources are Tier 1. Any GA notice, deprecation, or 8-K filed since late July may have gone undetected — treat every "unchanged" claim about release notes or earnings in this deck as "last confirmed 2026-07-22," not "confirmed today."

---

## Architecture Comparison — Compute & Capacity

- **AWS:** EC2 fleet depth across instance families and regions; Capacity Blocks let customers *reserve* GPU/accelerator capacity ahead of need rather than compete for it.
- **Google Cloud:** Compute Engine pricing is byte-identical to the last three captures (Jul 22, Aug 24, and this run) — a genuinely stable baseline, not a gap in our monitoring. TPU fleet (v6e, tpu7x) pricing is likewise unchanged.
- **Batch/HPC restriction (carried forward, unverified this month):** GCP Batch jobs can no longer create Compute Engine resources outside the job's region (grandfathered accounts until Jun 2027). This was last independently confirmed 2026-07-22 via release notes — that source has been unreachable for six weeks, so treat the date as "still believed true," not "reconfirmed."
- **Wedge:** the underlying regression (no cross-region capacity-hunting on a platform whose CFO already flagged a capacity ceiling) still stands as reported in July. We simply can't re-verify it moved or didn't this month — say that to the customer rather than presenting it as freshly checked.

---

## Architecture Comparison — AI/ML Serving

- **AWS:** Bedrock (managed, multi-model) + Trainium/Inferentia (owned silicon) + SageMaker — model choice is the product thesis, unchanged.
- **Google Cloud:** what was "Vertex AI" is now branded "Agent Platform" under Gemini Enterprise. The Oct 21, 2026 retirement of 16 open-model MaaS endpoints (DeepSeek, Llama 3.3 70B, Qwen3 ×4, GLM, Kimi K2, MiniMax, GPT-OSS, embeddings) is unchanged and now **50 days out** from today.
- **Concession:** the rebrand doesn't change the underlying product decision customers face — Gemini Flash-class models remain genuinely strong on price-performance, and the retirement is still a real, dated, customer-checkable commitment, not FUD.
- **Deal stage:** bake-off, migration — the closer the date gets, the more this becomes a "what's your cutover plan" conversation rather than a "here's a risk" one.

---

## Architecture Comparison — Security & Control Surfaces

- **Encryption/SIEM dates (carried forward, unverified this month):** CSEK disabled Jul 20, 2027; SecOps legacy APIs blocked on new instances Oct 26, 2026, full turndown Jul 20, 2027. These were last confirmed 2026-07-22 against `gcp_release_notes_all`, which has 403'd for six straight weeks. We have no basis to say these dates moved — we also have no basis to say they didn't.
- **AWS position, unchanged:** KMS External Key Stores (XKS) — key material never leaves the customer's HSM — carries no deprecation notice. Security Lake (OCSF, open schema) remains the pitch for the SecOps rewrite.
- **Concession, unchanged from July:** CMEK with Cloud EKM and Chronicle API are genuine modernizations, not downgrades. The wedge is the forced re-review window, not a unique AWS capability.
- **What's actually new:** nothing on this slide is new — the honest move this month is flagging that "new" and "verified" are different claims while our T1 source stays dark.

---

## Feature Deep-Dive — Model Choice & Lock-In

- **Evidence:** 16 Vertex/Agent Platform MaaS endpoints retire Oct 21, 2026 — unchanged since first reported, now 50 days away. New Gemini Flash models still ignore custom temperature/top-K/top-P (unchanged).
- **AWS counter:** Bedrock serves DeepSeek, Llama, Qwen, and Kimi as first-class managed models today; open weights also run on Trainium/Inferentia for price control.
- **Talk track, sharpened for the shorter runway:** "50 days to migrate off endpoints Google is retiring — if the work is happening anyway, do it once, onto the platform whose business model depends on model choice."
- **Deal stage:** bake-off, migration — this is no longer a future-quarter conversation.

---

## Feature Deep-Dive — Accelerator Supply

- **Evidence (unverified this month):** Google CFO's Q2 2026 admission ("revenue would have been higher if we were able to meet the demand") and the $514B backlog figure are unchanged since July — but the SEC EDGAR source that would surface a Q3 update has 403'd for six weeks. We cannot say whether Q3 commentary has shifted this narrative.
- **AWS counter, unchanged:** Capacity Blocks for ML — reserve accelerator capacity ahead of time instead of competing for it during a publicly admitted shortage.
- **Concession, unchanged:** a customer already committed to GCP with backlog priority may get preferential allocation over a net-new AWS evaluation running the same capacity argument in reverse.
- **Deal stage:** competitive bake-off, especially training-adjacent workloads. Don't cite the Q2 figures as "current quarter" — they are the last confirmed figures, from a source that's currently unreachable.

---

## Feature Deep-Dive — Pricing Transparency & Structure

- **Evidence, now confirmed stable across three captures (Jul 22, Aug 24/31, this run):** H100 80GB at $9.79655/hr + $1.4695/hr management fee = $11.266/hr fully loaded; TPU v6e (1-chip) $3.105/hr; tpu7x (1-chip) $13.80/hr. This is a stronger claim than July's single-snapshot baseline — these numbers have held for six weeks.
- **AWS counter, unchanged:** ask for the fully-loaded per-hour Vertex/Agent Platform number before comparing to SageMaker/Bedrock — the management fee is still a line item customers miss in Google quotes.
- **Concession, unchanged:** Google's TPU list-price transparency remains genuinely better than AWS's Trainium equivalent. Sellers should walk in with a current Trainium2/UltraServer $/chip-hr number.
- **Deal stage:** quote scrub, TCO conversation.

---

## Feature Deep-Dive — Discount Structures

- **Evidence (baseline unchanged since 2026-07-22, Compute Engine pricing byte-identical across three captures):** Spot up to 91% off on-demand; CUDs up to 70% (memory-optimized) / 55% (other); spend-based flexible CUDs (Savings-Plans-analog).
- **AWS position, unchanged:** Spot ≤~90%, Savings Plans structurally equivalent to flexible CUDs.
- **Concession, unchanged:** discount-structure parity is real. Win on Graviton price-performance and Spot capacity depth, not discount-header comparisons.
- **Deal stage:** renewal, cost-optimization review. No delta to report this month — say so rather than restating July's numbers as if freshly negotiated.

---

## Feature Deep-Dive — Agent Platform & Consumption Metering

- **Evidence, new since July:** Agent Platform now runs three billed resource types — Agent Compute ($0.085/vCPU-hr after a 50-hr/month free tier), Agent Memory ($0.009/GiB-hr after 100 GiB-hr free), Agent Storage (~$0.30/GiB-month after 1 GiB-month free). Memory Bank read/write operations bill through the same Agent Compute meter (1 vCPU-hr per 3M reads, per 1M writes) — **effective today, Sep 1, 2026**, no longer a future date.
- **Evidence, seat ladder update:** Gemini Enterprise added a **$0-seat-fee, usage-based PAYG edition** (20+ seats, limited rollout) alongside the existing Business ($21/seat/mo, ≤300 seats) and Standard/Plus ($30/seat/mo, unlimited seats) tiers.
- **AWS counter:** Amazon Q Business / Bedrock AgentCore remain consumption-based with no per-seat floor and no separate multi-meter stack to reconcile — Strands + MCP openness vs. Google's ADK-first model.
- **Concession:** the PAYG tier is a genuine simplification of Google's *procurement* motion — match it with a scoped AgentCore pilot, don't dismiss it. But procurement simplicity and billing simplicity are different claims: a workload touching Runtime + Memory Bank + Gateway now reconciles four separate meters against three separate free-tier thresholds.
- **Deal stage:** discovery, bake-off — ask any active Agent Platform prospect to show a fully-loaded worked example across all four meters before comparing to a Bedrock/AgentCore consumption quote.

---

## Feature Deep-Dive — Vector Search / RAG Storage Economics

- **Evidence, new this week:** Agent Platform (Vertex) Vector Search added a "Storage-Optimized" tier — a single bundled SKU replacing per-VM node pricing: Capacity Units at $2.30/hr per replica (compute + up to 1 TiB active SSD storage, auto-scaling) plus Write Units at $0.45/GiB for index writes (batch or streaming).
- **AWS counter:** OpenSearch Serverless and Bedrock Knowledge Bases price on OCU-hours and ingested/stored data respectively — ask for a same-corpus-size, same-QPS comparison rather than comparing sticker rates; the node-based Vector Search pricing this replaces was notoriously hard to size in advance, which was itself a competitive opening.
- **Concession:** collapsing per-VM node math into two SKUs (Capacity Units + Write Units) is a real simplification for customers who found the old Vector Search pricing opaque — don't pretend the old model was better just because it's the one we'd been battlecarding against.
- **Deal stage:** discovery — this is brand new pricing structure, not yet seen in a live quote; flag it as a watch item for RAG/agent-memory conversations.

---

## Pricing & TCO — Apples-to-Apples Snapshot

| Item | Google Cloud (captured) | AWS equivalent |
|---|---|---|
| H100 80GB, on-demand | $9.797/hr + $1.469/hr mgmt fee = $11.266/hr fully loaded (stable 3 captures) | Compare fully-loaded P5 rate — pull current list before quoting |
| TPU v6e (1-chip) | $3.105/hr (stable 3 captures) | Compare current Trainium2 $/chip-hr |
| tpu7x / Ironwood-class (1-chip) | $13.80/hr (list; supply unconfirmed 6 weeks) | Compare current Trainium3 $/chip-hr |
| Agent Compute (Agent Runtime/Gateway/Memory Bank) | $0.085/vCPU-hr after 50 free hrs/mo | Bedrock AgentCore — consumption-based, single meter |
| Vector Search (Storage-Optimized, new) | $2.30/hr per Capacity Unit + $0.45/GiB write | OpenSearch Serverless / Bedrock Knowledge Bases — request matched-corpus quote |
| Spot discount ceiling | up to 91% | ~90%, deeper capacity depth |
| Committed-use ceiling | up to 70% (memory-optimized) | Savings Plans — structurally equivalent |
| Agent platform seats | $0 (PAYG, new) / $21 / $30 per seat/mo | Consumption-based (Bedrock AgentCore), no seat floor |

*Compute/TPU rows verified stable across three captures (07-22, 08-24/31, 09-01). Agent Runtime, Memory Bank, and Vector Search rows are new since the July deck. TPU supply/availability and the earnings-derived rows remain unconfirmed due to the ongoing six-week source outage — refresh before every quote regardless.*

---

## Pricing & TCO — The Hidden Line Items

- **Vertex/Agent Platform management fee:** +$1.469/hr on H100 managed prediction — unchanged, still a separate SKU from the base accelerator rate, still worth asking for explicitly.
- **New hidden-stack risk: the agent-runtime meter cluster.** A single agent workload can now touch Agent Compute, Agent Memory, Agent Storage, and Memory Bank read/write operations simultaneously — four meters, four free-tier thresholds, one bill. Ask any Agent Platform TCO model whether it accounts for all four, not just the headline seat price.
- **Unresolved billing-date conflict, do not repeat to a customer either way:** Google's own pages have carried a live contradiction for three straight weeks — "Semantic Governance Policy billing will commence later in 2026" vs. prior captures stating it has billed since Aug 1, 2026. We flag this as a pattern (billing dates on this platform have been genuinely hard to pin down this quarter), not as a specific number to cite.
- **Forced migrations are still TCO, not just engineering cost:** the Oct 2026 MaaS retirement, CSEK turndown, and SecOps API turndown are each a mandatory re-platforming project — quantify that cost in any GCP-retention TCO model, and note this month that we can't independently re-verify the two 2027 dates while the release-notes source is down.

---

## Pricing & TCO — Migration-Friction Date Table (for QBR use)

| GCP change | Customers affected | Hard date | Verification status |
|---|---|---|---|
| Memory Bank / Agent Runtime metering | Agent Platform builders | **Live now — Sep 1, 2026** | Confirmed this run (pricing page) |
| Agent Gateway metering | Agent-to-Anywhere users | Live since Jul 13, 2026 | Confirmed this run |
| 16 open-model MaaS endpoints retired | Agent Platform (Vertex) open-model inference | Oct 21, 2026 — 50 days out | Confirmed this run |
| SecOps legacy APIs blocked on new instances | New SecOps provisioning | Oct 26, 2026 | **Unconfirmed 6 weeks** — release notes source 403 |
| Batch cross-region resources (grandfathered) | Cross-region batch/HPC | Jun 30, 2027 | **Unconfirmed 6 weeks** — release notes source 403 |
| CSEK disabled | Hold-your-own-key compute customers | Jul 20, 2027 | **Unconfirmed 6 weeks** — release notes source 403 |
| SecOps legacy APIs fully turned down | All SecOps custom integrations | Jul 20, 2027 | **Unconfirmed 6 weeks** — release notes source 403 |

---

## Customer Evidence — What We Can Cite Today

- **New this month: a real, named, citable GCP-to-AWS migration.** Quikr — India's largest classifieds marketplace platform, 30M+ monthly users — migrated 47,965 BigQuery tables and 82 GCS buckets (~200 TB) from Google Cloud to AWS, executed with AWS partner CloudThat. Data moved via GCP Dataproc into Amazon S3 (converted to Parquet for cost and query efficiency), 8,000+ AWS Glue Crawlers built the Athena catalog. Source: CloudThat's public case study, "Quikr migrates from Google Cloud to AWS Cloud Platform" (cloudthat.com) and its companion case-study PDF.
- **Honest caveats before this goes in front of a customer:** this pipeline's outbound fetcher couldn't render cloudthat.com directly this run (network egress policy), so this is sourced via search-indexed content, not a page we opened and read ourselves — the title, company name, and figures above are corroborated across multiple independent search results, but confirm the live page yourself before quoting numbers externally. The case study's file metadata suggests it may not be a same-quarter win — treat it as a credible reference architecture story, not a "just happened" proof point.
- **Also citable, unchanged from July:** Gartner Magic Quadrant for Strategic Cloud Platform Services — AWS Leader, 15 consecutive years, highest Ability to Execute (analyst-level evidence, not a customer testimonial, but usable as third-party validation).
- **Deal stage:** reference-selling, migration discovery — same-industry (classifieds/marketplace, high-volume analytics) accounts are the best fit for the Quikr story.

---

## Customer Evidence — The CRM Gap Is Still Open

- **This pipeline still has no CRM/Salesforce feed and no case-study database** — it monitors public GCP surfaces only. Finding Quikr this month was a live web search against public case-study indexes, not a pipeline capability upgrade; the structural gap flagged every month since July is unchanged.
- **Do not present fabricated logos, quotes, or win counts.** Field/sales leadership: supply real, named, recent wins from CRM before this section goes in front of a customer — one third-party-sourced case study is not a substitute for your own pipeline data.
- **AWS's public case-study library** (aws.amazon.com/solutions/case-studies) remains the fallback resource for sourcing a same-industry reference while this gap stays open.
- **Action for next month's deck:** field teams should submit any GCP-to-AWS win (even anonymized/logo-blind) so this section keeps growing instead of relying on the same search-sourced example twice.

---

## Objection Handling — "Google's AI momentum is real, why fight it?"

- **Objection:** "Forrester just gave Google the highest overall score and called them a 'Customer Favorite' in AI Platforms — why are we still fighting this?"
- **Response:** Agreed, and we're not disputing it — Google topped Strategy in that Wave, and their CFO's own capacity admission from Q2 is still on the record too. AWS was also named a Leader in the same Wave, credited for Bedrock and AgentCore. Momentum on a vision axis and operational capacity are different questions — ask what the customer's actual reserved-capacity terms look like, not just which vendor scored highest on an analyst's strategy rubric.

---

## Objection Handling — "Your TPU pricing isn't as transparent as Google's"

- **Objection:** "Google publishes clean per-chip-hour TPU pricing; AWS's Trainium pricing is harder to compare."
- **Response:** Still fair, unchanged from July — sellers should walk in with a current Trainium2/UltraServer $/chip-hr number rather than deflecting. Also worth surfacing: Google's headline TPU rate still doesn't include the management fee on the Vertex/Agent Platform GPU SKUs (+$1.469/hr on H100, confirmed stable for six weeks) — ask whether the number they're citing is fully loaded.

---

## Objection Handling — "We're already committed to GCP's agent platform"

- **Objection:** "We've already scoped Gemini Enterprise — it's simple to procure, and now there's even a $0-seat PAYG option."
- **Response:** The PAYG tier is real and worth matching with a scoped AgentCore pilot, not arguing against on principle. But ask them to price one real agent workload across all four of Agent Platform's meters — Agent Compute, Agent Memory, Agent Storage, and Memory Bank operations — which went live today. "Simple to procure" and "simple to forecast" turned out to be different claims once Google added its third metering layer since July.

---

## Objection Handling — "We already built on GCP's SIEM and encryption model"

- **Objection:** "We picked GCP specifically for hold-your-own-key control and Backstory integrations — switching is disruptive."
- **Response:** Both turndown dates (CSEK: Jul 2027, Backstory APIs: Jul 2027) are unchanged from what we've told you before — though we want to be straight that our own monitoring of Google's release notes has been blocked for six weeks, so we're repeating, not re-confirming, those dates this month. The strategic point still stands regardless: the disruption is coming either way; the only choice is one rewrite (to an open schema via Security Lake) or two.

---

## Objection Handling — "This all sounds like it cuts both ways"

- **Objection:** "You're citing Google's own admissions and analyst reports, but doesn't AWS have comparable gaps — including the fact your own pipeline has been half-blind for six weeks?"
- **Response:** Yes to both, and we'd rather tell you that than paper over it. Capacity Blocks exist because reservable capacity is the honest answer to a supply-constrained accelerator market on both platforms. And this deck says plainly, slide by slide, which figures are freshly confirmed this month versus carried forward unverified — that's a deliberate choice, not an oversight, and it's the same discipline we'd want turned on us if the roles were reversed.

---

## Call to Action

- **Next steps:** pull current Bedrock/Trainium/P5 list pricing and a live Agent Platform four-meter worked example before any Vertex/Agent Platform quote comparison — don't cite this deck's captured numbers as current without a refresh, especially anything marked unverified above.
- **Pipeline ask:** this deck's own confidence depends on `gcp_release_notes_all`, `gcp_tpu_docs`, and the SEC EDGAR feed coming back online (six weeks down as of this run) — escalate provisioning a `PERPLEXITY_API_KEY` or unblocking those domains so next month's deck can re-verify the 2027 dates instead of repeating them.
- **Resources:** `sources/gcp.yaml` battlecard map, weekly Intelligence Brief (`artifacts/weekly-intelligence-brief-*.md`), this deck's markdown source (`decks/compete-deck-gcp-vs-aws-*.md`) for editing before a specific customer conversation.
- **Deal support:** for the Migration-Friction Date table, the Customer Evidence section, or the Quikr reference, loop in field leadership before presenting externally — this deck is a competitive-intel starting point, not a final customer-facing asset without a named-logo pass and independent source verification.
