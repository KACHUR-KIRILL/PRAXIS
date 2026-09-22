# U6 — model and channel cost per practitioner per month

**Status:** provisional calculation, 2026-09-22. Author self-checked (hand-computed test case); **not independently reviewed** — required under contract §4 before this supports a pricing or margin decision. Not validated by any measurement.
**Task:** [Issue #1](https://github.com/KACHUR-KIRILL/PRAXIS/issues/1) (P2 checkpoint, active step U6).
**Brief links:** U6 and H5 in [brief §10 and §13](../../product/PRAXIS-BRIEF-v0.1.md).

## 1. Framing — read before the numbers

**Question.** For the recommended MVP scope (one channel, conversation up to booking, client card, reminders), how much do model API tokens and per-message channel fees cost for one practitioner per month, and what share of a reference price is that?

**Decision it informs.** The price floor and margin behind H5, and which levers (model tier, prompt design, channel) matter. It does **not** decide H5: the Owner has not set the H5 threshold, so the output is cost and cost share, not "converges / does not converge".

**What is measured.** API token cost for three candidate Claude tiers (Haiku 4.5, Sonnet 5, Opus 5.5) at first-party list prices, and channel fees for Telegram (base case, per the Owner's instruction for this calculation on 2026-09-22) with WhatsApp as a comparison.

**What is not measured.** Hosting, database, monitoring; payment processing, taxes, FX; support or integrator labour; human onboarding time; content, avatar and supplier-ordering functions (outside MVP); non-Anthropic models (their pricing pages were unreachable from the session); model quality — a cheaper tier is only a valid option if it passes the U5/H2 acceptance threshold.

**Nature of every volume input.** All conversation volumes and token sizes are **Co-Pilot assumptions** with no measurement behind them. The three scenarios are synthetic: `low` and `high` move all parameters jointly in one direction, so `high` is a compounded stress case, not a forecast.

## 2. Assumed processing design (model boundary)

1. Each client message triggers one model call carrying a static prefix (system prompt with practitioner voice and rules + the full knowledge base + tool definitions), the client card and the dialog history so far.
2. Calendar lookups and booking writes are extra model round trips (`tool_calls_per_dialog`).
3. One card-update call per dialog; one summary call per escalated dialog. Both use a short instruction without the knowledge base.
4. Reminders are deterministic templates with no model call.
5. One model for all calls. Prompt caching, when on, applies only to the static prefix with a 1-hour TTL: hits at the cache-read price, misses at the 1-hour write price (2x input). The growing dialog tail is not cached (conservative).
6. An overhead multiplier covers retries, guardrail calls and malformed turns.

A retrieval design (only relevant knowledge-base fragments per call) or a cheaper model for tool and card calls would lower cost; neither is modelled.

## 3. Inputs

All inputs, units, labels and rationale are in [`inputs.json`](inputs.json). Labels: `SOURCE` (dated primary source read in this session), `SECONDARY` (from `research/`, search summaries), `ASSUMPTION`, `OWNER`.

| Input | Label | Value(s) |
| --- | --- | --- |
| Claude prices, cache multipliers | SOURCE — platform.claude.com pricing page, retrieved 2026-09-22, sha256 `c1faa23e…eb54f7` | Haiku 4.5 $1/$5; Sonnet 5 $2/$10; Opus 5.5 $4/$20 per M input/output; 1h cache write 2x input; cache read 0.1x (0.05x on Opus 5.5) |
| Tokenizer factor | SOURCE, same page — "approximately 30% more tokens" on 4.7+ models | 1.3 for Sonnet 5 and Opus 5.5; token sizes are stated in the Haiku 4.5 tokenizer. Ratio for Russian text not measured |
| Telegram Bot API | SECONDARY — primary page blocked again | $0 |
| Telegram Business (bot replies as the practitioner's account) | ASSUMPTION — Premium gating unverified | $5/month |
| WhatsApp utility template | SECONDARY illustrative ~$0.01; bounds assumed | $0.005 / 0.01 / 0.03 per reminder |
| WhatsApp service reply | ASSUMPTION — reported free now, reported billable from 2026-10-01, rate unknown | $0; hypothetical $0.002 and $0.005 as sensitivity only |
| Visits per month | ASSUMPTION | 60 / 100 / 160 |
| Dialogs per visit | ASSUMPTION | 1.0 / 1.5 / 2.5 |
| Client messages per dialog | ASSUMPTION | 4 / 6 / 10 |
| Static prefix (system + KB + tools), tokens | ASSUMPTION | 5,000 / 9,500 / 19,500 |
| Output per reply incl. reasoning, tokens | ASSUMPTION | 150 / 250 / 600 |
| Cache hit rate on static prefix | ASSUMPTION | 0.6 / 0.8 / 0.9 |

Values are listed as low / base / high; the remaining token and overhead parameters are in `inputs.json`.

## 4. Method

Per dialog with `n` client messages, `t` tool calls and escalation share `e`, with static prefix `P`, card `C`, exchange size `E`, tool result `TR`, aux instruction `A`:

- reply call `i = 1..n` input: `P + C + (i-1)·E + E/2`, summed: `n·P + n·C + E·n²/2`;
- tool call input: `P + C + n·E/2 + TR` (`t` calls);
- card update and escalation input: `A + C + n·E` (`1 + e` calls);
- output: `n·out_reply + t·out_tool + out_card + e·out_escalation`.

Monthly tokens = dialogs × per-dialog tokens, where dialogs = visits × dialogs per visit. Cost = tokens × tokenizer factor × overhead × price; with caching, static-prefix tokens are priced at `h·cache_read + (1-h)·cache_write_1h`. WhatsApp = reminders × template rate + agent replies × reply rate. Code: [`u6_model.py`](u6_model.py); tests: [`test_u6_model.py`](test_u6_model.py) (hand-computed case, input completeness).

## 5. Results

Full generated tables: [`results.md`](results.md). Key rows, USD per practitioner per month, Telegram Bot API channel ($0):

| Scenario | Dialogs / replies | Haiku 4.5, cached | Sonnet 5, cached | Opus 5.5, cached | Sonnet 5, no cache |
| --- | --- | ---: | ---: | ---: | ---: |
| low | 60 / 240 | 1.92 | 4.98 | 9.72 | 5.56 |
| base | 150 / 900 | 10.05 | 26.14 | 49.55 | 43.86 |
| high (stress) | 400 / 4,000 | 85.82 | 223.14 | 413.06 | 485.20 |

Channel, base scenario: Telegram $0 (or $5 with the assumed Business subscription); WhatsApp $2.00 for templates only, up to $10.50 with high template and hypothetical reply rates.

Share of reference price, base scenario, cached: Sonnet 5 — 33% of $79, 12% of $219, 6.5% of $400, 5.2% of $500. Opus 5.5 — 63% of $79, 12% of $400. The price points are AI Beauty Bot tiers (secondary-sourced) and the Owner's $400–500 assumption A2; none is a chosen price.

One-off onboarding (assumed 300k input / 40k output tokens): $0.50–2.60 depending on the model.

## 6. Co-Pilot reading (not an Owner decision)

1. **At the assumed base volume, model plus channel cost is small against the Owner's $400–500 price (2–12% across tiers) but material against competitor anchors ($79–219: about 5–63%).** Cost does not appear to block a $400–500 price; it would constrain a price near the competitors.
2. **The channel is not the cost driver.** Telegram costs $0–5; WhatsApp at secondary-sourced rates adds $2–10 at base. Model tier and conversation volume dominate.
3. **Cost scales with dialogs and messages per dialog and is dominated by the static prefix** (about 86% of input tokens at base). Prompt caching cuts base cost by about 40% (Sonnet 5: $43.86 → $26.14); knowledge-base size is the next lever (sensitivity table, `results.md` §5).
4. **The compounded high case exceeds the $79 anchor on every tier, exceeds $219 on Sonnet 5 and Opus 5.5, and reaches the $400–500 range on Opus 5.5.** If heavy-volume practitioners exist, a flat price needs a usage cap or tiering. Whether they exist is exactly what is unknown.
5. **What would change these conclusions:** real dialogs per visit and messages per dialog (largest swings), the cheapest tier that passes the U5/H2 threshold, the achieved cache hit rate, and a verified WhatsApp rate if WhatsApp becomes the channel. The first two are measurable in the pilot at no extra cost if logged from day one.

**H5 cannot be evaluated yet.** The Owner's threshold is missing. A usable form: "model + channel cost ≤ X% of price in the base scenario and ≤ Y% in the high scenario, on the cheapest tier that passes U5". Setting X and Y is the Owner's decision.

## 7. Limitations

- Every volume and token size is an assumption; no practitioner data was used.
- The 1.3 tokenizer factor is the vendor's general figure; the Russian-text ratio was not measured (`count_tokens` on a sample dialog would settle it).
- Telegram and WhatsApp pricing and gating were not read from primary pages (proxy blocked); Telegram Business gating is unverified.
- The static prefix assumes the full knowledge base in every call; a retrieval design changes the cost structure.
- The cache hit rate depends on traffic gaps per practitioner; with the 1-hour TTL it is plausible during working hours but not measured. Caches are per workspace and a practitioner's prefix is unique, so there is no cross-practitioner cache sharing.
- Reasoning-token spend per reply is folded into `output_tokens_per_reply` and is uncertain.
- Prices are mutable; re-check the pricing page before relying on these figures after 2026-09-22.

## 8. Run record

- **Code revision:** the commit that adds this directory (`git log -- models/U6-UNIT-COST`).
- **Environment:** Python 3.11.15, standard library only; no randomness, no network.
- **Commands (from repository root):**
  - `python -B -m unittest discover -s models/U6-UNIT-COST -p "test_*.py" -v` → 7 tests passed, 2026-09-22.
  - `python -B models/U6-UNIT-COST/u6_model.py > models/U6-UNIT-COST/results.md`.
- **Outputs:** [`results.md`](results.md).

## 9. Review

Not independently reviewed. Suggested review: a separate executor (for example, the Codex entry point `AGENTS.md`, or a spreadsheet built without reading this code) recomputes the base and high rows from `inputs.json` and challenges the model boundary in section 2. Record the reviewer, the reviewed commit, findings and disagreements here.
