# BOS_OS gap scan for PRAXIS — 2026-09-22

**Question:** what does BOS_OS contain that PRAXIS lacks and would actually benefit from — in project management and working method, and in building and operating AI agents?

**Source:** `KACHUR-KIRILL/BOS_OS` at commit `432f448` (the same commit STIMULUS inspected on 2026-09-18), cloned read-only. BOS files were read as design references, not as rules. **Method:** two delegated read-only scans (Claude Sonnet, medium effort), one per question; the Co-Pilot spot-checked the load-bearing claims against the files named below. Neither scan read every file; unread areas are listed at the end.

The filter applied throughout is the PRAXIS contract: no BOS registries, amendments, gates or mandatory multi-role routing; add structure only when it prevents a present, concrete failure more cheaply than the alternatives. Lessons STIMULUS already extracted at this commit, and that PRAXIS inherited through its role contract, are not repeated here.

## 1. Adopted now

| BOS source | Practice | PRAXIS form |
| --- | --- | --- |
| `canon/ARCH-PKG-WORKORDER-001_r3.md` (Row 2: Work Order minimum fields; supersession mechanism) | A task states what is **out of scope** and names what it supersedes; the current state of work is never an asserted field | `.github/ISSUE_TEMPLATE/task.md`: the Project Start Protocol §5 fields plus "Out of scope" and "Supersedes / Superseded by". Issues remain the only task source. |
| `records/DEFECT_REGISTER.md` (r2) and its semantics `decisions/ARCH-DEC-DEFECT-001_r2.md` | One append-only log of agent defects and Owner remarks | `.github/ISSUE_TEMPLATE/defect.md` and a `defect` label. It gives the contract's third-occurrence rule (§6) something concrete to count against. No separate register file. |

## 2. Deferred to a named stage

| BOS source | Practice | Stage | PRAXIS form when it arrives |
| --- | --- | --- | --- |
| `agents/ASA-EVAL-RECORD-001_r2.md` | Eval run record: cases, MET / NOT MET / NOT EXERCISED, per-case rationale | P5–P6 | 20–30 reply cases for the client-facing agent — practitioner's tone, correct escalation of clinical questions, no medical advice, correct booking action, AI disclosure — run before every prompt or model change. Unexercised cases are never counted as passed. |
| `agents/PCC-ENGINEER-001_r4.md` (prompt and context contract), `agents/OLS-CONTEXT-PACKAGE-001_r4.md` §3–8 | Mandatory and prohibited context; check on receipt | P7 | One short contract for the agent: what every reply call receives (client card, service catalog, recent messages, booking state, escalation flags) and what it must never do (diagnose, promise unconfirmed prices, hide that it is an AI). |
| `agents/OLS-MACHINE-CHECKS-001_r31.md` §4 | Deterministic checks | P7 | Two or three cheap tests: no client data or secrets in logs; escalation fires on clinical triggers; conversation-state transitions (new lead → booked → reminder sent) behave as specified. |
| `decisions/ARCH-DEC-AUTONOMY-BOUNDARY-001` — accepted revision **r10**; r11–r15 are unaccepted drafts | Separates read-only extraction from actions that change external state; enumerates allowed side effects; secrets held as references, not values | P7 | Per external system (Telegram, then Meta channels, CRM): which actions the agent may take on a practitioner's behalf, with what credentials, and what always needs the practitioner. |
| `agents/OLS-READINESS-MATRIX-001_r6.md` | Capability demonstrated per platform, with evidence | P5 | A per-channel checklist: capability demonstrated? evidence link? — not a governed matrix. |

## 3. Rejected

| BOS source | Why not |
| --- | --- |
| `decisions/ARCH-DEC-PM-001_r2.md` — separate Program Manager role | Contradicts the single-role design; no workload justifies it. |
| `triage/` deferred-work carrier | No backlog yet; deferred ideas go into the existing Issue as the contract already says. Revisit at P6 if the backlog grows. |
| `roadmap/` item state machine | The P0–P9 table and sequence rule cover it proportionately. |
| `decisions/ARCH-DEC-SKILLS-001_r1.md`, `decisions/ARCH-DEC-WORK-VISIBILITY-001_r5.md` | Substance already in the contract (§6 skills; §3 actor claim ≠ evidence) and protocol §6. |
| `deploy/AUTOMATION_MVP.md`, `tools/mvp_*.py` — signed queue / claim / review state machine for multi-agent work | Solves BOS's internal coordination, not a client-facing agent. |
| `agents/OLS-AGENT-ARCHITECTURE-001_r4.md`, PCC / ASA gate and HOLD apparatus, canon | The governance PRAXIS is built to avoid. |

## 4. Hermes

Hermes is `NousResearch/hermes-agent`, an external open-source agent runtime and CLI, not BOS code — evidence: `audits/evidence/S2-HERMES-0e9fc2cc.zip` (`acquisition.json` pins upstream commit `0e9fc2cc…`, retrieved 2026-09-11) and `audits/evidence/S4-HERMES-M7-M10.zip`. BOS only assembled read-only evidence about it and never reached a sourcing decision. Its own security note states that the only security boundary against an adversarial LLM is the operating system; pricing and release cadence stayed unknown (`b2-pricing/finding.txt`, `b1-releases/refusal.txt`).

**Reading for PRAXIS:** not a P6 candidate for the client-facing agent — it is a developer-facing agent CLI, not a messaging agent, and its security model is weaker than a bot handling third-party client data requires. P6 compares messaging SDKs and platforms, LLM providers and CRM/booking tools instead. If the Owner meant Hermes as a harness for *our own* development work, that is a separate question, not answered here.

### Correction — 2026-09-22 (later the same day), after reading Hermes itself

The reading above rests on BOS evidence about Hermes, not on Hermes. Checked against `NousResearch/hermes-agent` at commit `28aceb3451f5a5d2a27396b2adf29231be34c482` (2026-09-22) — `README.md`, `SECURITY.md`, `gateway/`, `plugin-catalog/` — and `NousResearch/hermes-telegram-business` at `98c60afc00d36c885bb040ebe973b1aa908886c0`:

- **"Not a messaging agent" is wrong.** Hermes runs a messaging gateway ("Telegram, Discord, Slack, WhatsApp, Signal, and CLI — all from a single gateway process"), has a WhatsApp Cloud API adapter (`gateway/platforms/whatsapp_cloud.py`) next to an unofficial Baileys bridge, a cron scheduler with delivery to any platform, and an official plugin `hermes-telegram-business` (tier `official`): a Telegram Business "secretary bot" that drafts a reply to each customer message and sends it only after the owner taps Send.
- **The security point stands in a narrower form.** `SECURITY.md` §2: Hermes is "a single-tenant personal agent"; "the only security boundary against an adversarial LLM is the operating system"; whole-process wrapping (Hermes' Docker image or NVIDIA OpenShell) "is the supported posture when the agent ingests content from … multi-user channels". Serving a practitioner's clients is such a channel: supportable, but only inside a per-practitioner sandbox.
- **Isolation options exist in Hermes itself.** Terminal backends (Docker, SSH, Modal, Daytona and others) confine only shell and file tools; `SECURITY.md` §2.2 says they do not confine the agent's own process (code execution, MCP, plugins, skills). The whole-process options (Hermes' Docker image, NVIDIA OpenShell) are the ones that fit a practitioner's instance.
- **Clients must not become agent callers.** `SECURITY.md` §2.6: network adapters require an allowlist, and "within the authorized set, all callers are equally trusted". The official Telegram Business plugin avoids this: customer messages are drafted with a plain model completion (`ctx.llm.complete`, no tools) and only the owner can act on the draft. Any PRAXIS build on Hermes should keep that shape.
- **Self-learning can be switched off** (`cli-config.yaml.example`: `memory.memory_enabled`, `memory.nudge_interval`, `skills.creation_nudge_interval`). For a client-facing agent it should be off, so that behaviour changes only through reviewed releases, not through client conversations.
- **One Hermes can host many practitioners as profiles.** `website/docs/developer-guide/multiplexing-gateway.md`: one gateway process serves every profile (`gateway.multiplex_profiles`, default on); each profile has its own config, memory, sessions, skills, secrets, cron and adapters, routed by `profile_routes` (user, chat, thread) or by a dedicated bot per profile. Isolation is in-process, not OS-level: MCP discovery, terminal/sandbox environment, built-in tools and provider registries are process-global (Known limitations), and "multiplexing isolates *profiles*; it does not authenticate or authorize *end users*" (Non-goals). Delegated subagents (`tools/delegate_tool*.py`) are short-lived task helpers, not per-practitioner assistants. Routing Telegram Business messages to a profile by `business_connection_id` was not found and was not verified.
- **Coverage against the brief, by directory listing only (nothing run):** messaging adapters under `plugins/platforms/` include Telegram, WhatsApp, SMS, email and others but **no Instagram**; content tools exist for image generation, video generation and TTS (`tools/image_generation_tool.py`, `tools/video_generation_tool.py`, `tools/tts_tool.py`), with no social-media publishing or avatar tool found; memory providers under `plugins/memory/` include Honcho, which keeps a per-user "peer card" and can be self-hosted — whether gateway senders map to separate Honcho peers was not checked. A structured client card (visits, procedures, contraindications) is not a Hermes feature.
- **Revised reading:** Hermes **is a P6 candidate** for the Telegram part of the MVP, not rejected. Gaps against the MVP, from the plugin's own README: no auto-send by design, no conversation history ("each customer message is drafted in isolation"), text only; no booking, calendar or client card; one instance per practitioner. The Baileys bridge is excluded by contract §5 (unofficial WhatsApp automation). Anthropic model support was not checked. Nothing was installed or run.

## 5. Lessons from BOS evidence

- **Scaffolding is not a working system.** `deploy/AUTOMATION_MVP.md`, section "Что построено, и чем оно не является": no platform routine was created, no key provisioned, and no end-to-end run of even two tasks was carried out. For PRAXIS P7: one real end-to-end conversation through a live Telegram bot comes before more contracts, schemas or checks.
- **External-tool evaluation stalls without live access.** The Hermes evaluation could not establish pricing or releases because access was blocked. PRAXIS P6 must budget real accounts and API access for the tools it compares, or it will produce the same UNKNOWNs.
- **Process can consume the output.** Machine-check documents alone reached revision r31, and several work orders were spent on evidence packages about a tool that was never used.

## 6. Not read

Most of `decisions/` (including ORG, AIOPS, ASA and the sweep and register decisions), 202 of 204 `tasks/` files, 2 of 3 `triage/` files, `records/DIAG-RESIDUAL-BASELINE-*`, several role contracts in `agents/` (ASA-PKG r10, PCC architect / program manager / controller-auditor / counter-architect), `automation/`, `evidence/automation-mvp/` contents, and `product/competitive/` (competitors of BOS itself, not relevant to PRAXIS). The adopt/reject verdicts rest on the files named above.
