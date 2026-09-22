# Project Start Protocol v0.1

**Status:** Working reusable protocol — not yet proven universal  
**Evidence base:** extracted from lessons observed in BOS_OS and the initial STIMULUS setup  
**Purpose:** provide a minimal, reusable sequence for starting a new project without relying on Owner memory and without importing heavy governance by default.  
**Provenance:** copied into PRAXIS from STIMULUS `standards/PROJECT-START-PROTOCOL-v0.1.md` at commit `8a18eed` on 2026-09-22; changes are listed in section 12.

## 1. Core principle

Optimize for validated business progress, not process completeness.

A new project starts with the smallest structure needed to preserve truth, sequence, ownership and evidence. New roles, controls, automations and infrastructure are added only when a present risk, repeated workload or observed failure justifies them.

This protocol is a reusable candidate, not a universal law. Its assumptions must be revised when later projects expose missing or unnecessary steps.

## 2. Mandatory project bootstrap

Before substantive project work, establish:

1. **Project identity** — project name and repository/workspace. A new project gets its own repository/workspace; do not place a second project's truth inside an existing project's carriers, even when reusing that project's materials. Copied material records its source path, commit and date; reuse transfers structure, not approvals, evidence or contract authority.
2. **Owner** — the human decision maker for product direction, material commitments, risk acceptance and launch.
3. **Current concept** — one primary artifact describing what the project is trying to build and which claims remain hypotheses.
4. **Current sequence** — one roadmap describing stages, dependencies and exit criteria.
5. **Task source** — one execution surface for substantive tasks. For PRAXIS this is GitHub Issues in `KACHUR-KIRILL/PRAXIS`.
6. **Carrier map** — explicit locations for current concept, role contract, roadmap, models, research and project integrity checks.
7. **Agent entry points**, when agents are used — thin adapters pointing to the authoritative role contract rather than duplicating it.

Do not create parallel editable Sources of Truth.

## 3. Reusable project sequence

### P0 — Identity and control
Establish the mandatory bootstrap above.

**Exit condition:** project identity, Owner, current concept carrier, sequence carrier and task source are resolvable.

### P1 — Concept
Start from a brief: a short inspectable statement of the idea produced by an intake with the Owner, not by inference from the request. The [project brief skill](../.agents/skills/project-brief/SKILL.md) is the reusable intake method; copy it with this protocol when reusing both in another workspace.

The brief is the project's first concept carrier, not a parallel one. Expand it in place as evidence arrives, or supersede it with a named concept artifact and update the pointers in the same change.

Describe:
- what is being built;
- for whom;
- the problem or desired outcome;
- the proposed value mechanism;
- what is known;
- what is assumed;
- what remains deliberately undecided.

Do not treat implementation choices as product invariants unless the concept actually depends on them.

**Exit condition:** a current concept carrier exists — an Owner-reviewed brief is sufficient at this stage — and material uncertainties are explicit. Owner review of a brief is not validation.

### P2 — Critical unknowns
Identify the smallest set of unknowns capable of invalidating or materially changing the project before expensive implementation.

Examples may include:
- economic viability;
- regulatory feasibility;
- technical feasibility;
- data rights;
- safety;
- distribution;
- supply;
- marketplace liquidity;
- security/privacy;
- unit economics;
- customer behavior.

The protocol does not require every category for every project.

**Exit condition:** critical unknowns are named, prioritized and connected to the decisions they block.

### P3 — Validation plan
For each critical unknown, determine the cheapest credible evidence that could change the decision.

Prefer:
- existing evidence;
- focused research;
- deterministic calculation;
- manual prototype;
- narrow experiment;

before broad implementation.

Define useful success, failure and insufficient-evidence conditions before interpreting results.

**Exit condition:** each blocking unknown has a bounded validation method or is explicitly accepted as unresolved by the Owner.

### P4 — Market reality
Establish the level of market evidence needed for the current decision:
- target user/customer;
- current alternatives and substitutes;
- competitors where relevant;
- distribution path;
- willingness to use/pay where relevant;
- economic context.

Depth is proportional to the decision; research does not become an end in itself.

**Exit condition:** the MVP can be framed against a real user and real alternatives, or the project is explicitly held because market evidence is insufficient.

### P5 — MVP definition
Define the smallest real-world test that can validate or falsify the most important project hypothesis.

State:
- target user;
- behavior or outcome to observe;
- minimum product/workflow scope;
- excluded scope;
- primary metrics;
- pass/fail/insufficient-evidence criteria.

**Exit condition:** the MVP is defined as an experiment, not a miniature final platform.

### P6 — Build vs adopt
Before material custom implementation, inspect reasonable ready-made alternatives and compare actual fit, speed, total cost, control, data boundaries and maintenance.

Before adopting an external component, verify that it actually satisfies the required capability and dependency constraints.

Use existing service/library/manual process/deterministic code when rational. Build custom when a concrete gap or strategic advantage justifies it.

**Exit condition:** material implementation choices have an explicit rationale proportional to their cost and reversibility.

### P7 — Build
Build only the scope needed for the MVP and its required evidence.

Do not add future architecture solely because it may someday be useful.

**Exit condition:** the MVP can execute the intended real-world experiment and produce observable results.

### P8 — Real-world evidence
Run the experiment with real users, transactions, operations or other authoritative events appropriate to the project.

Distinguish measured results from interpretation.

**Exit condition:** enough evidence exists for the next decision, or the result is explicitly inconclusive.

### P9 — Decision and learning
Owner decides:
- continue;
- iterate;
- pivot;
- scale;
- hold;
- kill.

Update affected primary artifacts when the decision changes project truth. Do not treat evidence as a silent amendment.

## 4. Sequence discipline

Substantive work should identify the roadmap stage it serves.

Before starting a material task, check:
1. Which stage does this serve?
2. Are its required predecessors satisfied?
3. Is there a more immediate blocker?
4. Does an equivalent task already exist?
5. Is the work reversible preparation, or does it assume a decision not yet made?

If work is materially out of sequence, report that fact before proceeding. The Owner may explicitly override sequence; an override is a decision, not proof that the dependency disappeared.

## 5. Task discipline

Use one task source.

For PRAXIS:
- GitHub Issues in `KACHUR-KIRILL/PRAXIS` are the task source.
- Chat is discussion, not durable task state.
- Roadmap defines sequence and dependencies, not issue status.
- Product artifacts define product truth, not task completion.

Create an Issue when work is substantial enough to survive the current session, has a distinct deliverable, or has dependencies worth tracking. Do not create issues for trivial edits that belong to an existing task.

A substantive issue should minimally state:
- stage;
- objective;
- why now;
- relevant inputs/dependencies;
- expected artifact/result;
- completion criterion.

## 6. Change impact discipline

Before a material change to project truth or a reusable project rule, establish:

1. What is changing?
2. Which primary artifact owns that fact or rule?
3. Where else is the old value repeated, referenced or assumed?
4. Which models, decisions or conclusions depend on it?
5. Which artifacts must change now?
6. Which artifacts intentionally remain unchanged?
7. How will propagation be checked after the edit?

A mechanical search is necessary where applicable, but not sufficient for semantic dependency review.

Do not silently rewrite history. When a concept revision replaces an earlier concept, identify the superseded version and update current pointers in the same change.

## 7. Verification proportionality

Use deterministic checks for deterministic properties.

Use independent review when a conclusion materially affects:
- economic sustainability;
- financial or reward obligations;
- legal/regulatory feasibility;
- security/privacy;
- safety;
- costly or difficult-to-reverse architecture;
- material public/customer promises.

Author self-check is required but is not independent validation.

Do not create a permanent reviewer role merely because one review is needed.

## 8. Agent evals

Evals test persistent agent behavior; they do not validate the business.

Do not create a large eval suite before observing agent behavior.

Create or expand evals when:
- an agent exhibits a consequential failure;
- a repeated behavior is important enough to preserve across executor/model changes;
- a small smoke case protects a core instruction with high downside.

Business hypotheses are validated by evidence, experiments, calculations and qualified review, not by agent evals.

## 9. Machine checks

A machine check should protect a deterministic invariant or a demonstrated failure class.

A check:
- reads and reports;
- may block a dependent operation when explicitly designed to do so;
- must not silently repair the subject it checks;
- should produce reproducible failure output.

Do not add controls with no concrete failure or high-consequence invariant to protect.

## 10. Triggers for added structure

Add a specialized role when work is repeated or materially distinct enough to justify separate context, expertise or independence.

Add automation when a stable repeated process is costly enough that automation is cheaper and safer.

Add a new governance/control mechanism when an observed failure mode or clear catastrophic risk justifies it.

Add a new infrastructure component when a current workload needs it and existing options do not fit.

Do not expand project structure merely because a mature project might need the component later.

## 11. Reuse and extraction

This protocol may be reused by another project as a candidate starting point.

After each real reuse, record:
- what was missing;
- what was unnecessary;
- what was project-specific;
- what survived unchanged.

Extract a project-independent standard only after repeated use provides evidence that the structure generalizes.

## 12. Recorded reuse

### 2026-09-22 — copied into PRAXIS from STIMULUS

**Source:** STIMULUS `standards/PROJECT-START-PROTOCOL-v0.1.md` at commit `8a18eed`, together with `.agents/skills/project-brief/SKILL.md` (copied verbatim).

- **Changed:** the task-source naming in §2 item 5 and §5 now names PRAXIS; this section replaces the STIMULUS-side reuse log, which stays in the STIMULUS copy.
- **Unchanged:** everything else, including the P0–P9 sequence and the discipline sections.
- **Observed at copy time:** the protocol needed no structural change to start a different product; the STIMULUS role contract did not travel with it and was re-derived separately (see `roles/FOUNDER-COPILOT.md`, provenance section).
- **Still to record:** what turns out missing, unnecessary or project-specific as PRAXIS exercises P2 onward. Add dated entries here; do not create a separate reuse registry.

When PRAXIS materials are reused by a later project, that project copies this file, records its own entry here and leaves this history in place.
