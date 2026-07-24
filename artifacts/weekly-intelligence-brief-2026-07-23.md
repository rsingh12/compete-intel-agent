## Weekly Brief: AI/ML Competitive Landscape
**Period:** 2026-07-16 to 2026-07-22 | **Author:** Competitive Intel Pipeline (gcp-analyst) | **Classification:** Internal

> Purpose: the recurring artifact that keeps leadership informed and field teams armed.

### Flash (Action Required)
- **Vertex AI is retiring 16 open-model MaaS endpoints on Oct 21, 2026** (DeepSeek, Llama 3.3 70B, Qwen3 ×4, GLM, Kimi K2, MiniMax, GPT-OSS, E5 embeddings). Every customer running these on GCP has a forced migration inside 15 months — usable in live bake-offs and renewals *today*, not just as a watch item. Reps should be pulling current Bedrock/Trainium pricing now.

### Priority Updates (This Week)
- **Alphabet Q2 2026 earnings:** Cloud revenue $24.8B (+82% YoY, beat consensus ~$22.3B); Cloud operating margin expanded 21%→36%; backlog (RPO) $514B; 2026 capex guidance raised to up to $205B (from $180–190B). CFO stated on the record that revenue "would have been higher if we were able to meet the demand" — a public admission of capacity constraint.
- **Gemini Enterprise seat pricing published:** $21/seat/mo (Business) and $30/seat/mo (Standard/Plus) — first committed per-seat price point on the agent platform; expect it in Amazon Q/AgentCore discovery immediately.
- **Compute Engine CSEK deprecation:** customer-supplied encryption keys disabled July 20, 2027 — opens a renewal-stage conversation with regulated (finserv/public sector/healthcare) accounts.
- **SecOps legacy SIEM APIs (Backstory/Ingestion) turning down:** new instances lose them Oct 26, 2026; full turndown July 20, 2027 — every custom SOC integration has a mandatory rewrite window.

### Strategic Signals (This Quarter)
- **Capex funded externally, not just from free cash flow:** $49.6B raised via stock issuance (June) + $20.3B in senior unsecured notes, specifically earmarked for AI infrastructure — worth tracking quarter over quarter as a signal of how sustainable the capex pace actually is.
- **Model-serving consolidation:** killing third-party open-model MaaS endpoints while locking down Gemini Flash sampling parameters (temperature/top-K/top-P now ignored) — Google is trading customer optionality for platform velocity.
- **New TPU generation (tpu7x/8t/8i) positioned as superseding Ironwood** (3x training throughput per prior call) — pricing is public ($13.80/chip-hr) but supply/availability corroboration is still missing from our sources; treat GA/scale claims as unverified.
- **Security partnership signal:** Cloud NGFW + Palo Alto WildFire — Google buying credibility in network security rather than building it natively.

### Win/Loss Snapshot
- **Wins this week:** *no data source* | **Losses this week:** *no data source*
- **Top competitor in losses:** *no data source* | **Common theme:** *no data source*
- *Gap: this pipeline monitors public GCP surfaces only (pricing pages, release notes, earnings filings). It has no CRM/Salesforce feed, so it cannot populate deal counts. Wiring in a CRM export would close this gap.*

### Recommended Actions
1. **Field:** Lead with the Oct 21, 2026 MaaS retirement list (verbatim, it's customer-checkable) in any active DeepSeek/Llama/Qwen bake-off; pair with the capacity-constraint admission from the earnings call as the honest counter to "GCP has AI momentum."
2. **Product/Pricing:** Get a Trainium2/UltraServer $/chip-hr answer ready and public — Google's TPU list-price transparency (tpu7x $13.80/chip-hr, v6e $3.105) is ahead of ours and will get quoted at reps directly.
