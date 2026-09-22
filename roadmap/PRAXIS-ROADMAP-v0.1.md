# PRAXIS Roadmap v0.1

**Status:** Working sequence  
**Owner:** Project Owner  
**Purpose:** define the current project sequence, dependencies and stage exit conditions. GitHub Issues in `KACHUR-KIRILL/PRAXIS` are the execution task source.

This roadmap applies the reusable `standards/PROJECT-START-PROTOCOL-v0.1.md` to PRAXIS. It does not itself prove that any stage is complete. Stage numbers follow the protocol's P0–P9.

## Current position

| Stage | Name | Condition | Key dependency |
| --- | --- | --- | --- |
| P0 | Identity & Control | **DONE at first commit** — repository, Owner, brief, roadmap, task source, contract, checker resolvable | — |
| P1 | Brief / Concept | **ACTIVE** — brief v0.1 drafted from the 2026-09-22 intake; awaiting Owner review | P0 |
| P2 | Critical Unknowns | **PREPARATORY** — first desk research on U1, U2 (channel policy) and U4 (alternatives) recorded in `research/` from secondary sources; primary-source confirmation, prioritization and Owner thresholds outstanding | P1 |
| P3 | Validation Plan | **BLOCKED** | P2 |
| P4 | Market Reality | **PARTIAL** — competitor scan recorded (`research/COMPETITOR-SCAN-2026-09-22.md`, secondary-sourced); willingness to pay untested | P2 |
| P5 | MVP Definition | **BLOCKED** — needs P2 results and Owner acceptance thresholds | P2–P4 |
| P6 | Build vs Adopt | **BLOCKED** | P5 |
| P7 | Build | **BLOCKED** — Owner's stated target: pilot-ready within about one month of 2026-09-22; a constraint, not a validated plan | P6 |
| P8 | Real-World Evidence | **BLOCKED** — pilot on the Owner's existing practitioner base | P7 |
| P9 | Evidence Decision: Continue / Iterate / Pivot / Scale / Hold / Kill | **BLOCKED** | P8 |

## P0 — Identity & Control
### Existing evidence
- private repository `KACHUR-KIRILL/PRAXIS`; Owner exists; root `README.md`; Founder Co-Pilot contract; platform adapters; brief as concept carrier; this roadmap; Project Start Protocol; integrity checker and CI.

### Exit criterion
Primary carriers, Owner, repository and task surface are resolvable. Met at the first commit.

## P1 — Brief / Concept
### Primary artifact
`product/PRAXIS-BRIEF-v0.1.md`

### Exit criterion
Idea, first user, problem, value mechanism and material uncertainties are explicit, and the Owner has reviewed the brief. Owner review is not validation.

## P2 — Critical Unknowns
### Objective
Name and prioritize the unknowns that can invalidate or reshape the MVP before anything is built. The brief's section 13 lists the starting set (U1–U6).

### Required outputs
- U1, U2, U4 desk research recorded in `research/` with sources and retrieval dates;
- Owner decisions on U5 (agent acceptance threshold) and on the pilot stop condition;
- a prioritized list connecting each unknown to the decision it blocks.

### Exit criterion
Critical unknowns are named, prioritized and connected to the decisions they block.

## P3 — Validation Plan
For each blocking unknown, the cheapest credible evidence: existing evidence, focused research, deterministic calculation (U6 token and channel cost per practitioner), manual prototype, narrow experiment — before broad implementation. Success, failure and insufficient-evidence conditions are defined before results are interpreted.

### Exit criterion
Each blocking unknown has a bounded validation method or is explicitly accepted as unresolved by the Owner.

## P4 — Market Reality
Target user, current alternatives and substitutes, competitors, distribution path (the Owner's existing base is the first channel), willingness to pay. Depth proportional to the MVP decision.

### Exit criterion
The MVP can be framed against a real user and real alternatives, or the project is explicitly held.

## P5 — MVP Definition
The smallest real-world test of the most important hypothesis: target user, behavior to observe, minimum scope, excluded scope, primary metric, pass/fail/insufficient criteria. Co-Pilot's standing recommendation, pending Owner decision: one channel, conversation-to-booking, client card, reminders; content generation, supplier orders, photo assessment and B2C access excluded.

Include a per-channel capability checklist (demonstrated? evidence link?) and the first eval set for agent replies — see [BOS gap scan](../research/BOS-OS-GAP-SCAN-2026-09-22.md), section 2.

### Exit criterion
The MVP is defined as an experiment, not a miniature final platform.

## P6 — Build vs Adopt
Inspect ready-made alternatives for every component (channel connectors, CRM substrate, scheduling, billing, content generation) and compare actual fit, speed, total cost, control, data boundaries and maintenance before custom implementation.

Budget real accounts and API access for every compared tool; evaluation without live access produces unknowns (BOS lesson, see the gap scan, section 5).

### Exit criterion
Material implementation choices have an explicit rationale proportional to their cost and reversibility.

## P7 — Build
Only the MVP scope and its required evidence. Before real practitioners or their clients: data minimization and access restrictions, AI disclosure where required, escalation to the practitioner for clinical questions, and recovery without losing client conversations or bookings.

Also due here, in minimal form: a prompt and context contract for the agent, an action boundary per external system, and two or three deterministic checks (gap scan, section 2). One real end-to-end conversation through a live bot comes before further scaffolding.

### Exit criterion
The MVP can run the intended pilot and produce observable results.

## P8 — Real-World Evidence
Pilot with real practitioners from the Owner's base and their real clients, under the preregistered protocol. Measured results are distinguished from interpretation.

### Exit criterion
Enough evidence exists for the Owner's decision, or the result is explicitly inconclusive.

## P9 — Evidence Decision
Owner chooses, based on evidence: continue, iterate, pivot, scale, hold or kill. Material changes update the affected primary artifacts through the change-impact discipline.

## Sequence rule
A substantive new task should identify its roadmap stage. If the requested work depends on a later blocked stage, the Founder Co-Pilot reports the sequence conflict before proceeding. The Owner may explicitly override the sequence; an override accepts the risk of working ahead of the dependency.

## Task source
GitHub Issues in `KACHUR-KIRILL/PRAXIS` are the durable task source for substantive execution work. Chat, commit messages, branch names and roadmap prose do not independently create or close tasks.
