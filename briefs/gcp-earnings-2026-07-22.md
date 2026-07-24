# Google Cloud — Q2 2026 Earnings Brief (AWS field team)

Source: Alphabet Q2 2026 results, reported 2026-07-22. Produced as a one-off
analysis (earnings content isn't in the diffable page set at the time of
writing — see note at bottom); not run through the `gcp-analyst` subagent.

## Material changes (COMMITMENT)

- **Cloud revenue $24.8B, +82% YoY** (vs $13.6B Q2'25), beating consensus
  (~$22.3B). Growth accelerated sharply from 48% YoY as recently as Q4 2025.
  This is a published, audited financial result — not a claim.
- **Cloud operating income $8.8B**, vs $2.8B a year ago — margin expanded
  from ~21% to ~36% of segment revenue. Cloud is now profitable at scale, not
  subsidized growth.
- **Cloud backlog (RPO) $514B**, with >50% contracted to convert to revenue
  within 24 months (methodology per CFO Anat Ashkenazi). A number this size
  is a forward revenue commitment, not a pipeline estimate.
- **2026 capex guidance raised to up to $205B**, up from $180–190B guided
  last quarter — a $15–25B upward revision in a single quarter.
- **Capacity is the binding constraint, on the record**: CFO Ashkenazi told
  analysts "our cloud revenue would have been higher if we were able to meet
  the demand." That is a company admitting under-supply, not a
  marketing claim of demand strength.

## Watch (SIGNAL)

- Gemini Enterprise adoption cited at "nearly 90% of Fortune 100" — a
  penetration claim, not a revenue or seat-count figure; treat as directional
  until a hard number is published.
- TPU generation: newer TPU 8t/8i described as superseding Ironwood (3x
  training throughput, 2x performance per the Q1 call), and reported as the
  generation AI labs are demanding now. This is relevant to any deal where a
  prospect cites Ironwood-era GCP TPU benchmarks — the comparison point has
  already moved.
- Alphabet raised $49.6B via stock issuance (June) plus $20.3B in senior
  unsecured notes in-quarter, specifically to fund AI infrastructure buildout.
  External financing for capex (rather than pure free-cash-flow funding) is
  worth tracking across future quarters as a signal of how sustainable the
  capex pace is.
- Stock sold off on the print despite the beat, reportedly on the capex
  raise — market is pricing capex risk, not cloud-demand risk.

## Battlecard deltas

- **accelerator_supply** (→ Trainium2/3, P5/P6 capacity, Capacity Blocks):
  This is the single most usable line in the deck. Google is now on-record
  turning away Cloud revenue for lack of capacity. If AWS has shorter lead
  times or committed capacity (Capacity Blocks) in a contested region, that
  is a directly quotable counter to a prospect citing GCP AI momentum — the
  momentum is real, but so is the admitted supply gap. Concession: this cuts
  both ways — a customer already committed to GCP with backlog priority may
  get preferential allocation over a net-new AWS evaluation running the same
  capacity argument in reverse.
- **ai_inference_price** (→ Bedrock, Trainium, Inferentia): TPU generational
  claims (8t/8i vs Ironwood) will show up in bake-off deck slides. No public
  per-token GCP pricing moved this quarter (that's still tracked on
  `gcp_pricing_vertex`, unchanged this run) — so this is a performance claim
  to probe, not a price commitment to match.
- **agent_platform** (→ Bedrock AgentCore, Strands, MCP support): the 90%
  Fortune 100 Gemini Enterprise adoption stat will get quoted by GCP reps as
  proof of enterprise agent traction. Concession: that adoption figure is
  real reach even if it's not yet a revenue or deployment-depth metric — AWS
  reps should be ready to ask "adoption of what, at what depth" rather than
  dismiss it outright.
- **compute_price, data_gravity, egress_terms**: no earnings-call content
  this quarter maps to these — dropped, not because nothing happened, but
  because the call didn't speak to them.

## Strategic read

Google is choosing to compete on scale and is telling the market it is
supply-constrained, not demand-constrained — a materially stronger position
than a quarter ago, and the capex raise says they believe it. The honest
read for AWS sellers: GCP's AI infrastructure story converted from marketing
claim to audited financial fact this quarter (backlog, margin, and revenue
all moved together), which raises the bar on infra credibility arguments
generally — including AWS's own. Where Google is still exposed is execution
risk on that $205B capex converting to actually-available capacity fast
enough to clear a $514B backlog; that gap is the honest opening, not a
denial that the demand is real.

## Dropped (with one-line reason each)

- YouTube ad sales (+13% YoY) — not a Cloud or enterprise infra signal.
- Consolidated company revenue ($119.8B, +24%) and operating margin (34%,
  +2pt) — reported for context above but not itself a Cloud-specific,
  seller-actionable item.
- Gemini App 950M MAU, 22B tokens/min — consumer-scale usage stats, no
  stated line to an AWS enterprise deal.

---

**Note on process**: `sources/gcp.yaml`'s `alphabet_earnings` entry previously
pointed at `abc.xyz/investor/`, a JS-rendered page that never actually
surfaces quarter-specific content in a static fetch (confirmed: identical
~1.6KB nav shell regardless of quarter). It has been repointed to SEC
EDGAR's 8-K filing index for Alphabet (CIK 0001652044), which is static
server-rendered HTML and gains a new row — new accession number, new filing
date — the day of every earnings release. That page only signals "a release
just dropped," not the figures themselves, so it will trigger a real
COMMITMENT-tier diff next quarter (unlike the old URL, which never would
have), at which point the pipeline's own triage/analyze stages take over.
This brief was produced by manually researching this quarter's already-public
results rather than waiting for that mechanism, since today's release predates
the fix.

Sources:
- [Alphabet Q2 2026 earnings: revenue up 24%, Cloud surges 82%](https://finance.yahoo.com/markets/stocks/articles/alphabet-q2-2026-earnings-revenue-203058727.html)
- [Alphabet reports Q2 2026 revenue of $119.8 billion](https://9to5google.com/2026/07/22/alphabet-q2-2026-earnings/)
- [Google Q2 Cloud Revenue Surges 82%](https://www.tradingkey.com/analysis/stocks/us-stocks/262048041-google-earnings-report-q2-2026-goog-googl-services-cloud-search-capital-expenditures-tradingkey)
- [Alphabet earnings updates: Stock sinks during analyst call as company hikes 2026 capex](https://www.cnbc.com/2026/07/22/google-earnings-q2-goog-live-updates.html)
- [Alphabet Announces Second Quarter 2026 Results (SEC IR page)](https://abc.xyz/investor/news/news-details/2026/Alphabet-Announces-Second-Quarter-2026-Results-2026-Y3uQ6H4ZJa/default.aspx)
