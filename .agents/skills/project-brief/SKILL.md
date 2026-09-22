---
name: project-brief
description: Turn a raw project idea into a short decision-ready brief before any concept, roadmap, economic model, market research or build work. Use when a new project starts, when an existing project's premise is restated from scratch, or when an idea arrives without a named owner, user, problem or falsification condition. Runs the intake, separates facts, assumptions, hypotheses and owner decisions, and records what can be reused instead of rebuilt.
---

# Project brief

A brief is the first artifact of a new project: a short inspectable statement of what is being attempted, for whom, on which assumptions, and what would show that it is wrong.

This skill is the intake **method** for P0 and P1 of the [Project Start Protocol](../../../standards/PROJECT-START-PROTOCOL-v0.1.md), which owns the stage definitions and exit conditions. Follow the authoritative role contract of the project being served. This skill adds no authority, grants no tools, and does not carry one project's role contract, approvals or evidence into another project.

## When to use

Use at the start of a new project, before a concept, roadmap, model, research plan, architecture or repository scaffolding exists. Use again only when the premise itself is being restated, not for each new task inside a running project.

Do not use it to re-summarize a project that already has an authoritative concept carrier; extend that carrier instead.

## What a brief is not

A brief is not validation, not market evidence, not a plan, not an architecture and not an approval to build. It records what the Owner asserts and what remains unknown, so the next stage can be chosen deliberately. A well-written brief can still describe an unviable project; that is a successful brief.

## 1. Establish identity and authority first

Before substantive questions, resolve:

- **Project name** (working name is enough) and the **repository/workspace** it will live in. A new project gets its own workspace. Do not write a second project's truth into an existing project's carriers, even when reusing that project's materials.
- **Owner** — the human who decides product direction, material commitments, risk acceptance and launch.
- **Relationship to existing projects** — independent, derivative, or a component of one. Reused material is copied with its source path, commit and date recorded; reuse does not transfer approvals, evidence or contract authority.
- **Task source** for the new project, once it has one.

If the workspace is not yet decided, continue the intake and keep the brief local until the Owner decides. Do not create repositories, external accounts or public artifacts as part of an intake.

## 2. Run the intake in one batch

Ask the Owner directly, in one batch, in the Owner's language. Keep it to the questions whose answers change the next decision; ten is usually enough. `Unknown` is a valid answer and becomes a P2 unknown, not a gap to fill with plausible text.

1. **Idea** — what is being built, in one or two sentences, without the implementation.
2. **User** — who is the first specific user, and who pays. If they differ, name both.
3. **Problem or desired outcome** — from that user's side, and how they handle it today.
4. **Value mechanism** — why this produces the outcome better than the current alternative for that user.
5. **Money** — where revenue comes from, or that there is none yet; any unit economics the Owner already assumes.
6. **Scale and geography** — intended market, jurisdictions, and whether a regulated domain is involved.
7. **Constraints** — budget, time, people, technology, data, legal, and anything the Owner has already fixed.
8. **Non-goals** — what the project deliberately will not do, and what is deliberately left undecided.
9. **Killer assumptions** — what must be true for this to work at all; what would make the Owner stop.
10. **Reuse** — which existing solutions, repositories, components or services the Owner already expects to use.
11. **Next decision** — which decision this brief must enable, and by when.

Ask follow-ups only where an answer is ambiguous enough to change the next decision. An intake is not an interview marathon: an idea has to survive contact with evidence, not with a questionnaire.

## 3. Keep the truth state separated

Record every material statement under exactly one label:

- **Fact** — supported by an inspected source or observation; record source and date.
- **Assumption** — used provisionally; record who supplied it.
- **Hypothesis** — testable; record the condition that would falsify it.
- **Decision** — record the decision maker, date and rationale.
- **Unknown** — explicit, and routed to P2.

An Owner-supplied mutable fact (a rate, a market term, a partner rule, a regulation) is a lead, not external evidence. Verify it against a dated primary source before it becomes a fixed input, or keep it labelled as an assumption and show how the conclusion depends on it. Enthusiasm, a competitor's marketing page and a model's fluent summary are none of these labels.

Do not resolve a missing answer by writing a reasonable-sounding one. An invented assumption in a brief propagates into every later model.

## 4. Scan for reuse before designing anything

Before proposing new structure, inspect what already exists — in the Owner's other repositories, in ready-made services and libraries, and in ordinary deterministic code or manual process.

For each candidate, check the actual requirement against actual fit, speed, total cost, control, data boundaries and maintenance, in proportion to the decision. Verify that the component really provides the capability before adopting it; a familiar name is not a capability check. Record what is reused, from which source and commit, and what is deliberately built instead.

Reusable material typically includes the start protocol, repository layout, integrity checks, working-method skills and role-contract structure. Product truth, economic parameters, approvals and evidence are project-specific and never reused.

## 5. Write the brief

One artifact, in the new project's workspace, Owner-facing language. Suggested structure:

```
# <Project> — Brief v0.1
Status: Draft (not validated) | Date | Owner | Workspace

1. Idea in one or two sentences
2. First user and who pays
3. Problem / desired outcome and today's alternative
4. Proposed value mechanism
5. Money and scale
6. Constraints
7. Non-goals and deliberately undecided
8. Facts (source + date)
9. Assumptions (who supplied)
10. Hypotheses (with falsification condition)
11. Killer assumptions and stop conditions
12. Reuse candidates (source + commit) and what is built instead
13. Open unknowns, prioritized, routed to P2
14. The decision this brief enables and the immediate next step
```

Mark the status honestly: `Draft`, `Owner-reviewed` or `Owner-approved` are three different states, and none of them is `validated`.

## 6. Close the stage

The brief satisfies P1 when the idea, user, problem, value mechanism and material uncertainties are explicit and the Owner has reviewed it. It becomes the project's first concept carrier: expand it in place as evidence arrives, or supersede it with a named concept artifact and update the pointers in the same change.

Then continue with P2 — critical unknowns — rather than with architecture, tooling or agent infrastructure.

## Limits

The brief records assertions, not evidence. Owner review is not validation, and an approved brief is not a viable business. This skill does not authorize research spending, external contact, repository creation or build work, and it does not replace the independent verification the project's contract requires for consequential conclusions.
