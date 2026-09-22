---
name: response-self-check
description: Check task fit before substantive work and review a draft before sending when the user or project instructions request a standing self-check. Prevent scope drift, then check evidence, completion claims, reasoning and proportionality without adding a routine review report.
---

# Response self-check

Use this skill at two points in a conversation or project that requests this practice: before substantive work and before each user-facing answer. Follow the project's authoritative instructions; this skill is a reusable method, not a second project contract or additional authority.

## Before substantive work: drift check

Before a new calculation, model, implementation branch or material document edit, identify internally in one short pass:

1. **Active question:** What exact current Issue/checkpoint or user decision is being advanced?
2. **Decision impact:** What result could change the next decision? If none, do not start the work.
3. **Authority:** Which inputs are Owner decisions, which are provisional assumptions, and which are merely examples or suggestions?
4. **Professional challenge gate:** If the Owner suggests adding a feature, metric, test, mechanism, or action, first decide whether it serves the same decision and primary outcome. Identify the strongest reason not to do it. If it introduces a second decision, outcome category, intervention policy, or evidence standard, challenge the proposal before editing and keep it separate unless the Owner explicitly redirects scope. Agreement or enthusiasm is not analysis and must not substitute for a recommendation.
5. **Stop condition:** What smallest result is sufficient, and what work is outside the current step?
6. **Thesis fit, for product tests and models:** Trace `product function -> decision question -> primary outcome -> allowed conclusion`. Name adjacent categories the outcome does not measure, such as aggregate monetary value, individual holder value, behavior, liquidity or safety. Use a plausible analogous system or counterexample to expose category errors; the analogy itself is not evidence.
7. **Propagation state, for cross-cutting product summaries:** Is the artifact a draft, independently reviewed, or Owner-approved? Keep a draft or reviewed-only summary standalone; do not add it to mandatory/canonical entry points or propagate its claims as project truth before explicit Owner approval.

For an operating or economic simulation, also trace the real process before choosing parameters: actors/accounts, acquisition and exit, growth and heterogeneity, event timing, concurrency/ordering, external cash and settlement, returns/reversals, accepted obligations, and scale. A normalized population needs an explicit invariance argument or a narrow scope statement. A per-user or per-transaction limit is not evidence of system-level protection against aggregate demand. If these flows are missing, do not compensate with more metrics or thresholds; correct the model boundary first.

Treat a follow-up question or proposed parameter as clarification or a hypothesis by default. Do not turn it into a new workstream, selected requirement or parameter sweep unless the Owner explicitly redirects the active step or the result can materially change its decision. When an existing checkpoint says to stop arbitrary sweeps, that instruction controls. Answer a narrow question qualitatively when calculation would not alter the active decision.

For a decision-bearing test, multiple reported metrics are allowed only under a declared hierarchy: one primary outcome for the decision, secondary diagnostics that explain it, and guardrails that can disqualify a candidate. Do not combine distinct decisions into one test merely because they share a ledger, implementation, or scenario. Shared infrastructure is not shared epistemic scope.

If the check fails, return to the active checkpoint, explain the mismatch briefly, and perform only the smallest useful correction. Do not add another tracker, registry, approval gate or ceremonial checklist.

## Before a user-facing answer

For a progress update, check only the claims being communicated; for a final answer, check the complete requested outcome.

Check the draft against the task and available evidence:

- Does it answer the actual request, including later corrections? If an important part is unfinished, complete authorized work or state the concrete blocker.
- Are consequential factual claims supported by inspected sources or observed results? Separate observations, assumptions, recommendations and user decisions. Recheck mutable state when the conclusion depends on it; do not repeat settled checks without a reason.
- Do claims such as created, saved, tested, committed, published or synchronized match the actual resulting artifact or state? A successful tool response alone is insufficient. Use observed paths, links and identifiers rather than inventing them.
- Do calculations, units and comparisons support the conclusion? Look for the strongest plausible counterexample or missing dependency. Recalculate when a material uncertainty remains; narrow or qualify unsupported claims.
- Does the proposed action serve the user's objective? For material custom work, check whether a suitable existing solution was actually considered or inspected. Do not claim that search occurred if it did not. Preserve needed verification while removing unnecessary process or scope.
- When reporting a test or model, establish the frame before the numbers: state the question it tested, the material conditions/assumptions, what was and was not measured, and why that measurement matters to the current decision. Do not assume the reader shares the test's scope; results without this frame can create a false conclusion even when the calculation is correct.
- Does the wording preserve state and authority? `Independently reviewed` is not `Owner-approved`. A later interpretation correction must preserve the original preregistered result in its proper scope and narrow the unsupported conclusion rather than silently overwrite either one.
- Is the wording clear about the outcome, limitations and next necessary action? Remove unsupported confidence, repetition and promises of background work that has not been scheduled.

Correct discovered errors before sending. Stop when material claims have adequate support and remaining uncertainty is explicit. A simple answer needs a brief consistency check; a consequential conclusion may need tools or the independent review required by the project. Do not create a new approval gate, launch agents, browse, or rerun tests solely to tick this checklist.

Keep the routine review internal. Report corrections, evidence or limitations when they affect the user's decision; do not append a ceremonial “self-check passed” block. Author self-review is not independent validation and does not guarantee correctness. Do not imply that installation creates a technical interceptor or guarantees invocation in every future session.
