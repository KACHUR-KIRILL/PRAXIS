# PRAXIS

Working repository for PRAXIS — working name of an AI assistant that takes the online client routine off a solo cosmetology practitioner (messaging on their behalf, client cards, reminders; later content and supplier orders).

## Status

**Brief stage — drafted, not Owner-approved, not validated.**

The immediate objective is to close the unknowns that decide the MVP scope — channel feasibility, legal boundaries, existing alternatives, willingness to pay — before building anything.

## Start here

- [PRAXIS Brief v0.1](product/PRAXIS-BRIEF-v0.1.md) — current concept carrier. Status: **Draft**; Owner-facing, in the Owner's language.
- [Founder Co-Pilot: single role contract](roles/FOUNDER-COPILOT.md).
- [Response self-check skill](.agents/skills/response-self-check/SKILL.md) — used before each user-facing answer under the role contract.
- [Project brief skill](.agents/skills/project-brief/SKILL.md) — intake method that produced the brief.
- [Carrier rules](roles/FOUNDER-COPILOT.md#7-carrier-rules).
- [Project Start Protocol](standards/PROJECT-START-PROTOCOL-v0.1.md) — reused from STIMULUS; reuse log in its section 12.
- [Current PRAXIS roadmap](roadmap/PRAXIS-ROADMAP-v0.1.md).
- [U6 cost model](models/U6-UNIT-COST/README.md) — provisional model and channel cost per practitioner; not independently reviewed.
- [Codex/OpenAI-compatible entry point](AGENTS.md) and [Claude entry point](CLAUDE.md).

This README is navigation, not a second role contract or product specification.

## Current sequence

The authoritative working sequence is [PRAXIS Roadmap v0.1](roadmap/PRAXIS-ROADMAP-v0.1.md). The roadmap defines stages and dependencies; GitHub Issues in this repository are the durable task source.

The brief remains the source for product scope and unresolved hypotheses. Roadmap state is not product validation.

## Reuse provenance

Method carriers were copied or adapted from `KACHUR-KIRILL/STIMULUS` at commit `8a18eed` on 2026-09-22: the start protocol and both skills verbatim, the role contract and integrity checker adapted. No STIMULUS product content, evidence or approvals were carried over. Each adapted file states what changed.

## Local integrity checks

Use Python 3.12 (the CI version) and its standard `venv` module. Run from the repository root.

macOS/Linux:

```sh
python3.12 -m venv .venv
.venv/bin/python -m pip install -r tools/requirements.txt
.venv/bin/python -B tools/check_project.py
.venv/bin/python -B -m unittest discover -s tools -p "test_*.py" -v
```

Windows PowerShell:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r tools/requirements.txt
.\.venv\Scripts\python.exe -B tools/check_project.py
.\.venv\Scripts\python.exe -B -m unittest discover -s tools -p "test_*.py" -v
```

Repeat dependency installation when `tools/requirements.txt` changes. `.venv/` is disposable local state, ignored by Git and the checker.

The checker uses [markdown-it-py](https://markdown-it-py.readthedocs.io/en/latest/using.html) to distinguish CommonMark links from code examples. It skips `.git/`, `.codex/`, `.venv/` and `__pycache__/`, while checking project skills in `.agents/`. It checks local target existence, not section anchors, raw HTML links, external URL availability or business validity.
