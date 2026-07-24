# AWS vs. Google Cloud
_Compete Deck — SA-to-SA / SA-to-Customer — July 2026_

---

## Executive Summary

- **BLUF: We win on capacity certainty, model choice, and control surfaces that don't have an expiration date.**
- Google's Q2 2026 results are real — Cloud revenue +82% YoY, backlog $514B — but their own CFO said on the earnings call that "revenue would have been higher if we were able to meet the demand." That is a public admission of a capacity ceiling.
- In the same quarter, Google set hard retirement dates on three things customers rely on: 16 open-model Vertex endpoints (Oct 2026), CSEK hold-your-own-key encryption (Jul 2027), and legacy SecOps SIEM APIs (Jul 2027).
- The honest frame for this deck: Google's AI infrastructure story converted from marketing claim to audited financial fact this quarter. We are not disputing their momentum — we are showing where that momentum is creating forced migrations, and why AWS is the calmer landing spot for each one.

---

## Market Context — Analyst Positioning

- **Gartner Magic Quadrant for Strategic Cloud Platform Services (2025):** AWS named a Leader for the 15th consecutive year, positioned highest on Ability to Execute.
- **Gartner Magic Quadrant for AI Infrastructure (inaugural, 2026):** Google Cloud named a Leader, positioned highest for Ability to Execute and furthest for Completeness of Vision on this specific quadrant — a newer, AI-infra-focused evaluation, distinct from the general cloud-platform quadrant above.
- **Read it straight, not defensively:** these are two different quadrants measuring different things. Google leads the AI-infrastructure-specific view; AWS leads the broader strategic cloud-platform view where execution track record and platform breadth are weighted higher. Don't contest the AI-infra placement — reframe the conversation to total platform risk, not just accelerator benchmarks.

---

## Market Context — Trends This Quarter

- Alphabet raised $49.6B via stock issuance plus $20.3B in senior unsecured notes in-quarter, earmarked for AI infrastructure buildout — external financing for capex, not pure free-cash-flow funding. Worth tracking as a sustainability signal across coming quarters.
- Google is consolidating model-serving behind Gemini (retiring 16 third-party open-model endpoints) while simultaneously locking down inference parameters on new Gemini Flash models — the pattern across the quarter is platform velocity traded for customer optionality.
- Google is shedding legacy control surfaces (CSEK, Backstory SIEM APIs, cross-region Batch flexibility) at the same time it's raising capex — simplifying the platform while scaling it, which is where migration friction concentrates.

---

## Architecture Comparison — Compute & Capacity

- **AWS:** EC2 fleet depth across instance families and regions; Capacity Blocks let customers *reserve* GPU/accelerator capacity ahead of need rather than compete for it.
- **Google Cloud:** Compute Engine + TPU fleet (v6e, tpu7x/Ironwood-class); admitted supply-constrained this quarter per CFO on the Q2 call.
- **Batch/HPC:** GCP Batch jobs can no longer create Compute Engine resources outside the job's region (grandfathered accounts get until Jun 2027, everyone else sooner) — removes the "hunt for capacity across regions" pattern GPU-scarce customers used. AWS Batch carries no equivalent restriction.
- **Wedge:** on a platform that just told the market it's supply-constrained, removing cross-region capacity-hunting is a real operational regression for the exact accelerator-scarce segment most likely to need it.

---

## Architecture Comparison — AI/ML Serving

- **AWS:** Bedrock (managed, multi-model) + Trainium/Inferentia (owned silicon) + SageMaker — model choice is the product thesis.
- **Google Cloud:** Vertex AI, historically multi-model via MaaS, now consolidating: 16 open-model endpoints (DeepSeek, Llama 3.3 70B, Qwen3 ×4, GLM, Kimi K2, MiniMax, GPT-OSS, embeddings) retire Oct 21, 2026.
- **Concession:** Gemini Flash-class models are genuinely strong on price-performance, and Google will pitch the retirement as "we're moving you to something cheaper and better." Don't claim workload regression — the customer loses the *option*, and contracts should price optionality.
- **tpu7x (Ironwood-class) pricing is public** ($13.80/chip-hr) ahead of firm availability/region/reservation-terms corroboration — pricing signal is ahead of the supply signal.

---

## Architecture Comparison — Security & Control Surfaces

- **Encryption:** GCP is deprecating CSEK (customer-supplied encryption keys) on Compute Engine, fully disabled Jul 20, 2027. Customers who chose GCP specifically for resource-level hold-your-own-key control lose that model. AWS KMS supports External Key Stores (XKS) — key material never leaves the customer's HSM — with no deprecation notice.
- **SecOps/SIEM:** Backstory and Ingestion APIs deprecated; new SecOps instances lose them Oct 26, 2026, full turndown Jul 20, 2027 for everyone. Every custom SOC integration needs a mandatory rewrite.
- **Concession:** CMEK with Cloud EKM covers most of the same compliance ground as CSEK for most postures, and Chronicle API is a genuine SIEM modernization, not a downgrade. The wedge is the *forced re-review window*, not a capability gap AWS uniquely fills — Security Lake (OCSF, open schema) is the pitch: the next mandatory rewrite is the last one tied to a vendor's proprietary API.

---

## Feature Deep-Dive — Model Choice & Lock-In

- **Evidence:** 16 Vertex MaaS endpoints retire Oct 21, 2026 (DeepSeek, Llama, Qwen3 ×4, GLM, Kimi K2, MiniMax, GPT-OSS, E5 embeddings). New Gemini Flash models ignore custom temperature/top-K/top-P.
- **AWS counter:** Bedrock serves DeepSeek, Llama, Qwen, and Kimi as first-class managed models today; open weights also run on Trainium/Inferentia for price control.
- **Talk track:** "If you have to migrate anyway, migrate to the platform whose business model depends on model choice, not away from it."
- **Deal stage:** bake-off, migration — usable now, not a future watch item.

---

## Feature Deep-Dive — Accelerator Supply

- **Evidence:** Google CFO, Q2 2026 earnings call: "our cloud revenue would have been higher if we were able to meet the demand." Cloud backlog $514B, >50% converting to revenue within 24 months.
- **AWS counter:** Capacity Blocks for ML — reserve accelerator capacity ahead of time instead of competing for it during a publicly admitted shortage.
- **Concession:** a customer already committed to GCP with backlog priority may get preferential allocation over a net-new AWS evaluation running the same capacity argument in reverse. Don't overplay this against an already-embedded GCP account.
- **Deal stage:** competitive bake-off, especially training-adjacent workloads.

---

## Feature Deep-Dive — Pricing Transparency & Structure

- **Evidence:** Vertex publishes per-chip-hour TPU list pricing (tpu7x $13.80, v6e $3.105) and a separate management fee on managed GPU prediction (+$1.469/hr on H100's $9.797/hr base, ~15% on top).
- **AWS counter:** ask for the fully-loaded per-hour Vertex number before comparing to SageMaker/Bedrock — the management fee is a line item customers often miss in Google quotes.
- **Concession:** Google's TPU list-price transparency is genuinely better than AWS's equivalent for Trainium today. Sellers should have a Trainium2/UltraServer $/chip-hr-equivalent answer ready rather than deflecting the comparison.
- **Deal stage:** quote scrub, TCO conversation.

---

## Feature Deep-Dive — Discount Structures

- **Evidence (GCP, baseline captured 2026-07-22):** Spot up to 91% off on-demand; CUDs up to 70% (memory-optimized) / 55% (other); spend-based flexible CUDs (Savings-Plans-analog).
- **AWS position:** Spot ≤~90%, Savings Plans structurally equivalent to flexible CUDs.
- **Concession:** discount-structure parity is real — don't contest the headline percentages. Win on Graviton price-performance and Spot capacity *depth* (availability at scale, not just discount ceiling), and steer the conversation to workload-level TCO instead of discount-header comparisons.
- **Deal stage:** renewal, cost-optimization review.

---

## Feature Deep-Dive — Agent Platform

- **Evidence:** Gemini Enterprise seat pricing published — $21/seat/mo (Business, 1–300 seats) and $30/seat/mo (Standard/Plus, unlimited, VPC-SC, CMEK, FedRAMP High/HIPAA, Code Assist Standard, ADK/third-party agent bring-in). ~90% of Fortune 100 cited as Gemini Enterprise adopters (adoption claim, not a revenue/depth metric).
- **AWS counter:** Amazon Q Business / Bedrock AgentCore — consumption-based rather than per-seat, Strands + MCP openness vs. Google's ADK-first model.
- **Concession:** Google has a simpler procurement story — a seat price and a 30-day trial. Match it with a scoped pilot offer rather than dismissing the simplicity.
- **Deal stage:** discovery — expect the $21/$30 figures to surface immediately in agent-platform conversations this quarter.

---

## Pricing & TCO — Apples-to-Apples Snapshot

| Item | Google Cloud (captured) | AWS equivalent |
|---|---|---|
| H100 80GB, on-demand | $9.797/hr + $1.469/hr mgmt fee = $11.266/hr fully loaded | Compare fully-loaded P5 rate — pull current list before quoting |
| TPU v6e (1-chip) | $3.105/hr | Compare current Trainium2 $/chip-hr |
| tpu7x / Ironwood-class (1-chip) | $13.80/hr (list; supply unconfirmed) | Compare current Trainium3 $/chip-hr |
| Spot discount ceiling | up to 91% | ~90%, deeper capacity depth |
| Committed-use ceiling | up to 70% (memory-optimized) | Savings Plans — structurally equivalent |
| Agent platform | $21–$30/seat/mo | Consumption-based (Bedrock AgentCore) |

*No week-over-week deltas yet on these figures — 2026-07-22 was this pipeline's first capture. Treat as a baseline snapshot, refresh before every quote.*

---

## Pricing & TCO — The Hidden Line Items

- **Vertex management fee:** +$1.469/hr on H100 managed prediction — ask for it explicitly, it's a separate SKU from the base accelerator rate.
- **Forced migrations are TCO, not just engineering cost:** the Oct 2026 MaaS retirement, the CSEK turndown, and the SecOps API turndown are each a mandatory re-platforming project with real engineering hours attached — quantify that cost in any GCP-retention TCO model a customer builds.
- **Recommendation:** when a customer presents a GCP TCO model, ask whether it accounts for the three forced-migration windows above. Most won't — that's the gap to point at.

---

## Pricing & TCO — Migration-Friction Date Table (for QBR use)

| GCP change | Customers affected | Hard date |
|---|---|---|
| Gemini 3.5 Flash removed (Global region) | Gemini Enterprise app users | Aug 4, 2026 |
| 16 open-model MaaS endpoints retired | Vertex open-model inference | Oct 21, 2026 |
| SecOps legacy APIs blocked on new instances | New SecOps provisioning | Oct 26, 2026 |
| Batch cross-region resources (grandfathered) | Cross-region batch/HPC | Jun 30, 2027 |
| CSEK disabled | Hold-your-own-key compute customers | Jul 20, 2027 |
| SecOps legacy APIs fully turned down | All SecOps custom integrations | Jul 20, 2027 |

---

## Customer Evidence — Data Gap (Read Before Presenting)

- **This pipeline has no CRM/Salesforce feed and no case-study database — it monitors public GCP surfaces only** (release notes, pricing pages, earnings filings, product docs).
- A live search this month for a named, public case study of a customer moving from Google Cloud to AWS did not surface one specific enough to cite honestly — general AWS migration case studies exist (AWS's official case-study library), but none confirmed as a GCP-to-AWS switch.
- **Do not present fabricated logos, quotes, or win counts on this slide.** Field/sales leadership: supply real named wins from CRM before this section goes in front of a customer — this deck should be updated with your actual pipeline data before an SA-to-customer conversation.

---

## Customer Evidence — What We Can Cite Today

- Gartner Magic Quadrant for Strategic Cloud Platform Services: AWS Leader, 15 consecutive years, highest Ability to Execute (analyst-level evidence, not a customer testimonial — usable as third-party validation while the case-study gap above gets filled).
- AWS's public case-study library (aws.amazon.com/solutions/case-studies) has volume and breadth across industries — direct SAs there for sourcing a same-industry reference while a GCP-specific switch story isn't yet available.
- **Action for next month's deck:** field teams should submit any GCP-to-AWS win (even anonymized/logo-blind) so this section has real content instead of a flagged gap.

---

## Objection Handling — "Google's AI momentum is real, why fight it?"

- **Objection:** "Cloud revenue is up 82%, backlog is $514B — Google is clearly winning on AI."
- **Response:** Agreed, and we won't pretend otherwise. But their own CFO said on the record that demand exceeded what they could supply. Momentum and capacity are two different questions — ask what your actual lead time and reserved-capacity terms look like before assuming the momentum translates to availability for your workload.

---

## Objection Handling — "Your TPU pricing isn't as transparent as Google's"

- **Objection:** "Google publishes clean per-chip-hour TPU pricing; AWS's Trainium pricing is harder to compare."
- **Response:** Fair — that's a real gap to close, and sellers should walk in with a current Trainium2/UltraServer $/chip-hr number ready rather than deflecting. Also worth surfacing: Google's headline TPU rate doesn't include the management fee that shows up on the Vertex GPU SKUs — ask whether the number they're citing is fully loaded.

---

## Objection Handling — "We're already committed to GCP's agent platform"

- **Objection:** "We've already scoped Gemini Enterprise at $21–$30/seat, it's simple to procure."
- **Response:** The simplicity is real — match it with a scoped AgentCore pilot rather than arguing against per-seat pricing on principle. Where consumption-based pricing wins is variable/spiky agent usage; ask what their expected utilization curve looks like before the per-seat model is assumed to be cheaper at scale.

---

## Objection Handling — "We already built on GCP's SIEM and encryption model"

- **Objection:** "We picked GCP specifically for hold-your-own-key control and Backstory integrations — switching is disruptive."
- **Response:** Both of those have hard turndown dates now (CSEK: Jul 2027, Backstory APIs: Jul 2027) — the disruption is happening regardless of whether AWS is in the conversation. The only question is whether the customer does one rewrite (to an open schema like OCSF via Security Lake) or two (to Chronicle now, and to whatever replaces it after the next GCP platform simplification).

---

## Objection Handling — "This all sounds like it cuts both ways"

- **Objection:** "You're citing Google's own admissions, but doesn't AWS have a comparable supply-constraint story on GPUs?"
- **Response:** Yes, and pretending otherwise would be a battlecard nobody trusts. Capacity Blocks exist specifically because reservable capacity is the honest answer to a supply-constrained accelerator market, on both platforms. The differentiator isn't "AWS has infinite supply" — it's giving customers a reservation mechanism rather than a first-come queue.

---

## Call to Action

- **Next steps:** pull current Bedrock/Trainium/P5 list pricing before any Vertex/TPU quote comparison — don't cite this deck's captured numbers as current without a refresh.
- **Resources:** `sources/gcp.yaml` battlecard map, weekly Intelligence Brief (`artifacts/weekly-intelligence-brief-*.md`), this deck's markdown source (`decks/compete-deck-gcp-vs-aws-*.md`) for editing before a specific customer conversation.
- **Deal support:** for the Migration-Friction Date table or Customer Evidence gap, loop in field leadership before presenting externally — this deck is a competitive-intel starting point, not a final customer-facing asset without a named-logo pass.
