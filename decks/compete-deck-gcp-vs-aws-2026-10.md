# AWS vs. Google Cloud
_Compete Deck — SA-to-SA / SA-to-Customer — October 2026_

---

## Executive Summary

- **BLUF: The thesis from July and September both hold, and this month the market-positioning picture got more precise, not more favorable to either side's talking points.** Gartner finally published the 2026 refresh of its general cloud-platform quadrant (Sept 1, 2026) — AWS stays a Leader for a 16th consecutive year, still highest on Ability to Execute. New and worth saying plainly: Google is now furthest for Completeness of Vision on *this* general quadrant too, not just the AI-infrastructure-specific one. Don't contest it — it's a real analyst finding.
- **Genuinely new since September:** Synergy Research's Q2 2026 hyperscaler numbers are out — AWS still the largest single hyperscaler at 28% share (down ~2pts YoY) growing revenue 37%; Google posted its strongest quarter on record, share up from 13% to 15% on 82% YoY growth. Separately, Gartner now forecasts worldwide AI-optimized IaaS spend crossing a structural line in 2026: inference spend ($23.3B) overtakes training spend ($19B) for the first time.
- **Unchanged and worth saying plainly:** H100/TPU list pricing, discount ceilings, and Agent Platform consumption-metering rates have now held byte-identical across four consecutive monthly captures (Jul, Aug, Sep, Oct). The Oct 21, 2026 MaaS retirement is unchanged in substance and now **20 days out** from today.
- **Honesty flag for this deck:** this pipeline's Tier-1 release-notes and earnings sources (`gcp_release_notes_all`, `gcp_tpu_docs`, `alphabet_earnings`) again returned `403 Forbidden` on today's capture. The outage that began in late July is now in its third month and third consecutive monthly deck. Every hard 2027 deprecation date (CSEK, SecOps, Batch cross-region) carried forward below remains **unconfirmed**, not re-verified — say so out loud in any QBR that leans on those dates.
- **Customer Evidence:** no new named GCP-to-AWS logo surfaced this month. The Quikr/CloudThat migration first reported in September is still the pipeline's only citable case — this month's search corroborated it with additional technical detail from a second independent source rather than replacing it. The CRM-feed gap is unchanged and still open.

---

## Market Context — Analyst Positioning

- **Gartner Magic Quadrant for Strategic Cloud Platform Services, 2026 edition (published Sept 1, 2026 — new this month):** AWS named a Leader for the 16th consecutive year, again positioned highest on Ability to Execute. Google Cloud also named a Leader, now its 9th consecutive year — and, new in this edition, positioned **furthest for Completeness of Vision on this general quadrant**, not only on the AI-infrastructure-specific one. Gartner names AI capabilities, industry solutions, digital sovereignty, operational efficiency, and hybrid/multicloud as the selection criteria driving this year's placements.
- **Gartner Magic Quadrant for AI Infrastructure (inaugural, published July 2026, unchanged):** AWS, Google Cloud, and Azure all named Leaders. Google remains positioned highest for Ability to Execute and furthest for Completeness of Vision on this narrower, AI-infra-specific quadrant. Gartner's qualitative language still characterizes AWS as the industry's "most extensive and mature cloud infrastructure" for AI workloads, with a specific caution that networking and cluster design can introduce latency constraints for the largest distributed-training jobs.
- **Forrester Wave: AI Platforms, Q3 2026 (unchanged):** Google took the highest overall placement, the maximum Strategy score, and Forrester's "Customer Favorite" designation. AWS is also a Leader, credited for scalable infrastructure plus Bedrock and AgentCore for agent orchestration.
- **Read it straight, not defensively:** Google's vision-axis strength has now shown up in two different Gartner quadrants and one Forrester Wave — this is a pattern, not a one-off. Don't contest any of it. AWS's differentiator across all three reports is the same one every month: the longest, most consistent execution track record (16 straight years on the general quadrant) and platform breadth. Reframe to total platform risk and production-readiness, not which vendor's roadmap narrative scores best on a strategy axis.

---

## Market Context — Trends This Quarter

- **New this month — Synergy Research Group, Q2 2026 hyperscaler results:** enterprise cloud infrastructure spend passed $143B in the quarter, up over $43B YoY (43% growth, the fastest in eight years), driven by GenAI services growing 165% YoY. Share: AWS 28% (down ~2pts from ~30% a year earlier, revenue +37% YoY), Azure 20% (flat YoY, +43% YoY revenue), Google Cloud 15% (up from 13%, its strongest quarter on record, +82% YoY revenue). The three hyperscalers now account for 67% of all cloud revenue.
- **Concession:** Google's growth rate is the fastest of the three and its share gain is real — don't contest the trendline. The honest counter is scale and durability, not rate: AWS's absolute revenue base is still the largest in the market, and a 2-point share decline against the fastest-growing competitor in the category is a very different story than share collapse.
- **New this month — Gartner, AI-optimized IaaS spending forecast (Aug 10, 2026 press release):** worldwide AI-optimized IaaS spend forecast at $42B in 2026 (+96%), reaching $66B in 2027. For the first time, global inference spend ($23.3B) is forecast to overtake training spend ($19B) within 2026 — a structural shift in what customers are actually buying capacity for.
- **Strategic read:** both vendors are already positioned for the inference-over-training crossover — AWS with its Trainium/Inferentia split and Capacity Blocks reservability, Google with Ironwood (tpu7x) explicitly marketed as its first inference-first TPU generation. Don't claim AWS invented the inference-specialized-silicon idea; the honest differentiator remains reservable access to capacity during an admitted shortage, not who specialized silicon first.
- **Pipeline blindness continues, third consecutive month:** `gcp_release_notes_all` (T1), `gcp_tpu_docs` (T2), and the SEC EDGAR 8-K index (T1) again returned `403 Forbidden` on today's capture. `PERPLEXITY_API_KEY` remains unset. Two of three blocked sources are Tier 1. Any GA notice, deprecation, or 8-K filed since late July may still have gone undetected.

---

## Architecture Comparison — Compute & Capacity

- **AWS:** EC2 fleet depth across instance families and regions; Capacity Blocks let customers *reserve* GPU/accelerator capacity ahead of need rather than compete for it.
- **Google Cloud:** Compute Engine pricing is byte-identical across four consecutive captures now (Jul 22, Aug 24/31, Sep 28, and today) — a stable baseline, not a monitoring gap. TPU fleet (v6e, tpu7x) pricing is likewise unchanged.
- **Batch/HPC restriction (carried forward, unverified for a third straight month):** GCP Batch jobs can no longer create Compute Engine resources outside the job's region (grandfathered accounts until Jun 2027). Last independently confirmed 2026-07-22 via release notes — that source has now been unreachable for over ten weeks.
- **Wedge:** the underlying regression (no cross-region capacity-hunting on a platform whose CFO already flagged a capacity ceiling, and whose own Q2-era demand numbers are corroborated independently by Synergy's 82% YoY Google Cloud revenue growth this quarter) still stands as reported in July. We still cannot re-verify whether the restriction itself moved — say that plainly rather than presenting it as freshly checked.

---

## Architecture Comparison — AI/ML Serving

- **AWS:** Bedrock (managed, multi-model) + Trainium/Inferentia (owned silicon) + SageMaker — model choice is the product thesis, unchanged.
- **Google Cloud:** "Agent Platform" (formerly Vertex AI) branding is now fully settled. The Oct 21, 2026 retirement of 16 open-model MaaS endpoints (DeepSeek, Llama 3.3 70B, Qwen3 ×4, GLM, Kimi K2, MiniMax, GPT-OSS, embeddings) is unchanged in substance and now **20 days out** from today.
- **Concession:** Gemini Flash-class models remain genuinely strong on price-performance, and the retirement is still a real, dated, customer-checkable commitment, not FUD. Nothing about the shrinking runway changes that.
- **Deal stage:** bake-off, migration — at 20 days out, this is squarely a "what's your cutover plan, and is it tested yet" conversation, not a future-quarter risk flag.

---

## Architecture Comparison — Security & Control Surfaces

- **Encryption/SIEM dates (carried forward, unverified for a third straight month):** CSEK disabled Jul 20, 2027; SecOps legacy APIs blocked on new instances Oct 26, 2026, full turndown Jul 20, 2027. Last confirmed 2026-07-22 against `gcp_release_notes_all`, which has now 403'd on three consecutive monthly runs of this pipeline.
- **AWS position, unchanged:** KMS External Key Stores (XKS) — key material never leaves the customer's HSM — carries no deprecation notice. Security Lake (OCSF, open schema) remains the pitch for the SecOps rewrite.
- **Concession, unchanged:** CMEK with Cloud EKM and Chronicle API are genuine modernizations, not downgrades. The wedge is the forced re-review window, not a unique AWS capability.
- **What's actually new:** nothing on the Google side of this slide has moved in three months of attempted re-verification. The honest move is still flagging that "unchanged" and "re-confirmed" are different claims while the T1 source stays dark — and noting that a three-month-old outage on the exact source that would confirm or retire these dates is itself a data point about how much weight to put on any single-source deprecation notice, from either vendor.

---

## Feature Deep-Dive — Model Choice & Lock-In

- **Evidence:** 16 Agent Platform MaaS endpoints retire Oct 21, 2026 — unchanged since first reported in July, now 20 days away. Gemini Flash models still ignore custom temperature/top-K/top-P (unchanged).
- **AWS counter:** Bedrock serves DeepSeek, Llama, Qwen, and Kimi as first-class managed models today; open weights also run on Trainium/Inferentia for price control.
- **Talk track, sharpened for the final stretch:** "20 days to migrate off endpoints Google itself is retiring — if the cutover work is happening anyway, do it once, onto the platform whose business model depends on model choice, not away from it."
- **Deal stage:** bake-off, migration — this is no longer a conversation about a future date, it's a conversation about a cutover plan due this month.

---

## Feature Deep-Dive — Accelerator Supply

- **Evidence (still unverified at the source, now corroborated independently):** Google CFO's Q2 2026 admission ("revenue would have been higher if we were able to meet the demand") and the $514B backlog figure are unchanged since July — the SEC EDGAR source that would surface a Q3 update is still 403'ing. Independent corroboration this month: Synergy Research's Q2 2026 figures show Google Cloud revenue growing 82% YoY, the fastest of the three hyperscalers — consistent with a demand-outstripping-supply story, though Synergy's numbers are a market-share report, not a capacity-constraint disclosure, and shouldn't be cited as if it were.
- **AWS counter, unchanged:** Capacity Blocks for ML — reserve accelerator capacity ahead of time instead of competing for it during a publicly admitted shortage.
- **Concession, unchanged:** a customer already committed to GCP with backlog priority may get preferential allocation over a net-new AWS evaluation running the same capacity argument in reverse.
- **Deal stage:** competitive bake-off, especially training-adjacent workloads. Keep citing the Q2 figures as "last confirmed," not "current quarter" — the earnings-specific source remains unreachable.

---

## Feature Deep-Dive — Pricing Transparency & Structure

- **Evidence, now confirmed stable across four consecutive captures (Jul 22, Aug 24/31, Sep 28, today):** H100 80GB at $9.79655/hr + $1.4694826/hr management fee = $11.266/hr fully loaded; TPU v6e (1-chip) $3.105/hr; tpu7x (1-chip) $13.80/hr. Four months of byte-identical pricing is a materially stronger claim than July's single-snapshot baseline.
- **AWS counter, unchanged:** ask for the fully-loaded per-hour Agent Platform number before comparing to SageMaker/Bedrock — the management fee is still a separate line item customers miss in Google quotes.
- **Concession, unchanged:** Google's TPU list-price transparency remains genuinely better than AWS's Trainium equivalent. Sellers should walk in with a current Trainium2/UltraServer $/chip-hr number.
- **Deal stage:** quote scrub, TCO conversation.

---

## Feature Deep-Dive — Discount Structures

- **Evidence (unchanged, Compute Engine pricing byte-identical across four captures):** Spot up to 91% off on-demand; CUDs up to 70% (memory-optimized) / 55% (other); spend-based flexible CUDs (Savings-Plans-analog).
- **AWS position, unchanged:** Spot ≤~90%, Savings Plans structurally equivalent to flexible CUDs.
- **Concession, unchanged:** discount-structure parity is real. Win on Graviton price-performance and Spot capacity depth, not discount-header comparisons.
- **Deal stage:** renewal, cost-optimization review. No delta to report for a second straight month — say so rather than restating old numbers as if freshly negotiated.

---

## Feature Deep-Dive — Agent Platform & Consumption Metering

- **Evidence, unchanged since September, confirmed stable on today's capture:** Agent Platform runs three billed resource types — Agent Compute ($0.085/vCPU-hr after a 50-hr/month free tier), Agent Memory ($0.009/GiB-hr after 100 GiB-hr free), Agent Storage (~$0.30/GiB-month after 1 GiB-month free). Memory Bank read/write operations bill through the same Agent Compute meter (1 vCPU-hr per 3M reads, per 1M writes) — now fully live since Sep 1, with no change to the rate.
- **Seat ladder, unchanged:** Gemini Enterprise's $0-seat-fee PAYG edition (20+ seats) sits alongside Business ($21/seat/mo, ≤300 seats) and Standard/Plus ($30/seat/mo, unlimited).
- **AWS counter, unchanged:** Amazon Q Business / Bedrock AgentCore remain consumption-based with no per-seat floor and no separate multi-meter stack to reconcile.
- **Concession, unchanged:** the PAYG tier is a genuine procurement simplification — match it with a scoped AgentCore pilot. Procurement simplicity and billing simplicity are still different claims: a workload touching Runtime + Memory Bank + Gateway reconciles four separate meters against four separate free-tier thresholds.
- **Deal stage:** discovery, bake-off — ask any active Agent Platform prospect to show a fully-loaded worked example across all four meters before comparing to a Bedrock/AgentCore consumption quote.

---

## Feature Deep-Dive — Vector Search / RAG Storage Economics

- **Evidence, confirmed stable, with one additional detail surfaced this month on closer read of the same capture:** Agent Platform Vector Search's "Storage-Optimized" tier bills Capacity Units at $2.30/hr per replica (includes up to 1 TiB active SSD storage, auto-scaling) plus Write Units at $0.45/GiB for index writes. Alongside it sits a **"Performance-Optimized" CU at $0.065/hr (1yr: $0.0585, 3yr: $0.052), bundling 2GB RAM** — a separate, cheaper tier for latency-sensitive smaller indexes rather than large-dataset storage. Both tiers are unchanged in rate since first captured; the Performance-Optimized tier simply wasn't called out in last month's deck.
- **AWS counter:** OpenSearch Serverless and Bedrock Knowledge Bases price on OCU-hours and ingested/stored data respectively — ask for a same-corpus-size, same-QPS comparison across whichever Agent Platform tier the customer is actually quoted, Storage- or Performance-Optimized, since the two serve different workload shapes and sticker rates aren't directly comparable to each other, let alone across vendors.
- **Concession:** having two clearly-scoped CU tiers (cost-per-TB for large corpora vs. cost-per-replica for latency-sensitive smaller ones) is a reasonable simplification over the old per-VM node pricing it replaced — don't dismiss it as a shell game.
- **Deal stage:** discovery — confirm which CU tier a customer's quote actually uses before building a comparison; this is still a watch item for RAG/agent-memory conversations, not yet seen contested in a live deal.

---

## Pricing & TCO — Apples-to-Apples Snapshot

| Item | Google Cloud (captured) | AWS equivalent |
|---|---|---|
| H100 80GB, on-demand | $9.797/hr + $1.469/hr mgmt fee = $11.266/hr fully loaded (stable 4 captures) | Compare fully-loaded P5 rate — pull current list before quoting |
| TPU v6e (1-chip) | $3.105/hr (stable 4 captures) | Compare current Trainium2 $/chip-hr |
| tpu7x / Ironwood-class (1-chip) | $13.80/hr (list; supply unconfirmed 10+ weeks) | Compare current Trainium3 $/chip-hr |
| Agent Compute (Agent Runtime/Gateway/Memory Bank) | $0.085/vCPU-hr after 50 free hrs/mo | Bedrock AgentCore — consumption-based, single meter |
| Vector Search, Storage-Optimized CU | $2.30/hr per CU (incl. 1 TiB SSD) + $0.45/GiB write | OpenSearch Serverless / Bedrock Knowledge Bases — request matched-corpus quote |
| Vector Search, Performance-Optimized CU | $0.065/hr per CU (incl. 2 GiB RAM) + $0.45/GiB write | Same — confirm which CU tier before comparing |
| Spot discount ceiling | up to 91% | ~90%, deeper capacity depth |
| Committed-use ceiling | up to 70% (memory-optimized) | Savings Plans — structurally equivalent |
| Agent platform seats | $0 (PAYG) / $21 / $30 per seat/mo | Consumption-based (Bedrock AgentCore), no seat floor |

*Compute, TPU, Agent Compute, and Vector Search rows now verified stable across four captures (07-22, 08-24/31, 09-28/09-01, and today). TPU supply/availability and the earnings-derived rows remain unconfirmed due to the ongoing 10+-week source outage — refresh before every quote regardless.*

---

## Pricing & TCO — The Hidden Line Items

- **Agent Platform management fee:** +$1.469/hr on H100 managed prediction — unchanged, still a separate SKU from the base accelerator rate, still worth asking for explicitly.
- **The agent-runtime meter cluster, unchanged since September:** a single agent workload can touch Agent Compute, Agent Memory, Agent Storage, and Memory Bank read/write operations simultaneously — four meters, four free-tier thresholds, one bill. Ask any Agent Platform TCO model whether it accounts for all four.
- **Vector Search tier selection is now itself a hidden line item:** with two differently-priced CU tiers (Storage- vs. Performance-Optimized) on the same product, a customer's quoted rate depends on which tier their workload lands in — ask which one is in the quote before comparing to an AWS number.
- **Forced migrations are still TCO, not just engineering cost:** the Oct 2026 MaaS retirement (now inside its final month), the CSEK turndown, and the SecOps API turndown are each a mandatory re-platforming project — quantify that cost in any GCP-retention TCO model, and note we still cannot independently re-verify the two 2027 dates while the release-notes source stays down.

---

## Pricing & TCO — Migration-Friction Date Table (for QBR use)

| GCP change | Customers affected | Hard date | Verification status |
|---|---|---|---|
| 16 open-model MaaS endpoints retired | Agent Platform open-model inference | Oct 21, 2026 — **20 days out** | Confirmed this run |
| Memory Bank / Agent Runtime metering | Agent Platform builders | Live since Sep 1, 2026 | Confirmed this run (pricing page, stable) |
| Agent Gateway metering | Agent-to-Anywhere users | Live since Jul 13, 2026 | Confirmed this run |
| SecOps legacy APIs blocked on new instances | New SecOps provisioning | Oct 26, 2026 | **Unconfirmed, 10+ weeks** — release notes source 403 |
| Batch cross-region resources (grandfathered) | Cross-region batch/HPC | Jun 30, 2027 | **Unconfirmed, 10+ weeks** — release notes source 403 |
| CSEK disabled | Hold-your-own-key compute customers | Jul 20, 2027 | **Unconfirmed, 10+ weeks** — release notes source 403 |
| SecOps legacy APIs fully turned down | All SecOps custom integrations | Jul 20, 2027 | **Unconfirmed, 10+ weeks** — release notes source 403 |

---

## Customer Evidence — What We Can Cite Today

- **No new named GCP-to-AWS logo surfaced this month.** The pipeline's live search re-confirmed and added detail to the same case first reported in September: **Quikr**, India's largest classifieds marketplace (30M+ monthly users), migrated 47,965 BigQuery tables and 82 GCS Coldline buckets (~150–200 TB) from Google Cloud to AWS with partner CloudThat. This month's search surfaced a second independently-indexed CloudThat case-study page describing the same migration with additional technical detail not in last month's deck: Amazon EMR clusters (on a VPC, using Spot EC2 instances for up to ~90% cost savings vs. on-demand) performed the BigQuery-to-S3 data movement, and all 47,965 tables were verified within 5 days; Amazon Athena serves the resulting analytics layer. Source: CloudThat's public case-study pages (cloudthat.com), titled "Quikr migrates from Google Cloud to AWS Cloud Platform" and (likely the same engagement, differently titled) "An E-Commerce Platform Achieves Seamless AWS Data Migration."
- **Honest caveats, unchanged from last month:** this pipeline's outbound fetcher still cannot render cloudthat.com directly (network egress policy) — every detail above is sourced via search-indexed snippets of the vendor's own published case study, not a page we opened and read ourselves. Confirm the live pages yourself before quoting any figure externally, and note that the two differently-titled CloudThat pages may describe the same deal under two different headlines rather than two separate wins — treat it as one corroborated case, not two.
- **Also citable:** the Gartner Magic Quadrant for Strategic Cloud Platform Services — AWS Leader for 16 consecutive years (2026 edition), highest Ability to Execute (analyst-level evidence, not a customer testimonial, but usable as third-party validation alongside the Quikr reference).
- **A lead we checked and are deliberately not using:** search this month surfaced older coverage (dating to AWS re:Invent 2017) of The Walt Disney Company naming AWS its "preferred" public cloud provider. Disney is a long-standing, genuinely multi-cloud customer of both AWS and Google Cloud — this is not a 2026 event, not a GCP-to-AWS migration, and should not be presented as a fresh win. Flagging it here so it doesn't resurface as a misremembered "recent" story in a field conversation.
- **Deal stage:** reference-selling, migration discovery — same-industry (classifieds/marketplace, high-volume BigQuery-scale analytics) accounts remain the best fit for the Quikr story.

---

## Customer Evidence — The CRM Gap Is Still Open

- **This pipeline still has no CRM/Salesforce feed and no case-study database** — it monitors public GCP surfaces only. Finding and corroborating Quikr was a live web search against public case-study indexes, not a pipeline capability upgrade; the structural gap flagged every month since July is unchanged.
- **Do not present fabricated logos, quotes, or win counts.** Field/sales leadership: supply real, named, recent wins from CRM before this section goes in front of a customer — one search-sourced case study, however well corroborated, is not a substitute for your own pipeline data.
- **AWS's public case-study library** (aws.amazon.com/solutions/case-studies) remains the fallback resource for sourcing a same-industry reference while this gap stays open.
- **Action for next month's deck, unchanged:** field teams should submit any GCP-to-AWS win (even anonymized/logo-blind) so this section grows instead of leaning on the same single case a third month running.

---

## Customer Evidence — Reference-Selling Guidance

- **Best-fit use of the Quikr story:** classifieds/marketplace platforms and any account with a large BigQuery analytics estate considering a replatform — the 47,965-table, ~150–200TB scale and the Dataproc/EMR → S3 → Athena pattern map directly onto a "how do we actually move the data" objection, which is usually the real blocker in these conversations, not a pricing one.
- **Weaker fit, use with care:** don't stretch the Quikr story into a generic "everyone is leaving GCP" narrative — it is one corroborated migration, not a trend line. Pair it with the Gartner SCPS 16-years-Leader fact (a durability argument) rather than implying momentum this single data point can't support.
- **If a customer or their GCP rep raises Disney, or any similar "AWS already won [big name]" claim:** verify the date and the actual arrangement before repeating it. The Disney/AWS "preferred cloud" story check this month (see prior slide) is a reminder that older, real announcements can resurface looking like fresh wins — a battlecard that gets a date wrong in front of a sophisticated customer costs more credibility than the anecdote was worth.
- **Standing ask to field:** anonymized/logo-blind wins are still welcome and still the fastest way to close this section's gap — they don't need to be customer-presentable to be useful internally for the next deck.

---

## Objection Handling — "Gartner just gave Google vision leadership on your own general cloud quadrant, not just the AI one — why fight it?"

- **Objection:** "The 2026 Gartner Magic Quadrant for Strategic Cloud Platform Services has Google positioned furthest for Completeness of Vision — not just on the AI-infrastructure quadrant, on the general one you're citing AWS's execution record from."
- **Response:** Accurate, and we're not disputing it — that's a genuine, new-this-month analyst finding. What it doesn't change is the other axis on the same quadrant: AWS is highest on Ability to Execute, for the 16th consecutive year. Vision and execution are different questions — ask what the customer's deployment actually needs more of: a compelling roadmap narrative, or a 16-year track record of shipping against one. Both are real; they're not the same thing.

---

## Objection Handling — "Your TPU pricing isn't as transparent as Google's"

- **Objection:** "Google publishes clean per-chip-hour TPU pricing; AWS's Trainium pricing is harder to compare."
- **Response:** Still fair, unchanged since July — sellers should walk in with a current Trainium2/UltraServer $/chip-hr number rather than deflecting. Also worth surfacing: Google's headline TPU rate still doesn't include the management fee on the Agent Platform GPU SKUs (+$1.469/hr on H100, now confirmed stable across four consecutive months) — ask whether the number they're citing is fully loaded.

---

## Objection Handling — "We're already committed to GCP's agent platform"

- **Objection:** "We've already scoped Gemini Enterprise — it's simple to procure, and there's a $0-seat PAYG option."
- **Response:** The PAYG tier is real and worth matching with a scoped AgentCore pilot, not arguing against on principle. But ask them to price one real agent workload across all four of Agent Platform's meters — Agent Compute, Agent Memory, Agent Storage, and Memory Bank operations, plus confirm which Vector Search CU tier (Storage- or Performance-Optimized) their RAG layer actually lands in. "Simple to procure" and "simple to forecast" are still different claims three months after Google added its third metering layer.

---

## Call to Action

- **Next steps:** pull current Bedrock/Trainium/P5 list pricing and a live Agent Platform four-meter worked example before any Vertex/Agent Platform quote comparison — don't cite this deck's captured numbers as current without a refresh, especially anything marked unverified above.
- **Pipeline ask, now a third consecutive month:** this deck's confidence depends on `gcp_release_notes_all`, `gcp_tpu_docs`, and the SEC EDGAR feed coming back online (10+ weeks down as of this run) — escalate provisioning a `PERPLEXITY_API_KEY` or unblocking those domains so next month's deck can re-verify the 2027 dates instead of repeating them a fourth time.
- **Resources:** `sources/gcp.yaml` battlecard map, weekly Intelligence Brief (`artifacts/weekly-intelligence-brief-*.md`), this deck's markdown source (`decks/compete-deck-gcp-vs-aws-*.md`) for editing before a specific customer conversation.
- **Deal support:** for the Migration-Friction Date table, the Customer Evidence section, or the Quikr reference, loop in field leadership before presenting externally — this deck is a competitive-intel starting point, not a final customer-facing asset without a named-logo pass and independent source verification.
