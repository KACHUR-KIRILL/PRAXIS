# Messaging channel policy check — 2026-09-22

**Question (brief U1, U2):** what is officially permitted for a third-party service that reads and sends direct messages on behalf of a solo cosmetology practitioner on Instagram, WhatsApp, Telegram and Facebook Messenger; what would block an AI agent that answers clients automatically; and where must the client be told they are talking to an AI?

**Evidence standard — read first.** Desk research by a delegated agent (Claude Sonnet, medium effort), retrieved 2026-09-22. The session's network proxy blocked direct fetches of every primary-source domain attempted (developers.facebook.com, business.whatsapp.com, core.telegram.org, eur-lex.europa.eu, leginfo.legislature.ca.gov, adilet.zan.kz). **All findings come from web-search summaries of those sources, not from reading the pages.** Treat every row as a lead to confirm against the primary page before it becomes a design input, and none of the legal rows as legal advice. Items the agent could not verify are listed at the end.

## 1. Instagram DMs

| Attribute | Finding |
| --- | --- |
| Product and prerequisites | Instagram Messaging API (Graph API). Practitioner needs an Instagram Professional account (Business/Creator). The newer "Instagram API with Instagram Login" path reportedly needs no linked Facebook Page; the older path does. Messaging on behalf of *other* businesses' accounts needs Advanced Access: Meta App Review plus Business Verification, once per app. |
| AI replies | Permitted. Meta recommends bot-identity disclosure wording. |
| Messaging window | 24-hour free-form window after the user's last message. Outside it, only `HUMAN_AGENT` (genuine humans only, 7 days) and one-time opt-in notifications; other re-engagement tags reported deprecated 2026-04-27. |
| Pricing | No per-message fee reported. |
| Suspension risk | Using `HUMAN_AGENT` for bot replies; scraping; automating a personal (non-professional) account. |
| Scale | Review is per app, not per practitioner; each practitioner still needs a Professional account and grants access through Business Manager. |

## 2. WhatsApp

| Attribute | Finding |
| --- | --- |
| Product and prerequisites | WhatsApp Business Platform (Cloud API), directly or through a Meta-authorized BSP. Needs a WhatsApp Business Account, a dedicated number and Meta Business Manager; Business Verification needed to exceed the default 250 unique customers / 24 h tier. |
| AI replies | Reported permitted only for structured tasks (booking, FAQ, order status) with a human-escalation path. Secondary reporting (TechCrunch, 2025-10-18) says Meta banned general-purpose / open-domain AI chatbots on the platform: new registrations from 2025-10-15, all accounts from 2026-01-15. **Meta's own policy wording not read.** |
| Messaging window and templates | 24-hour service window free-form; business-initiated messages outside it need a pre-approved template (marketing / utility / authentication). |
| Pricing | Per-message billing by category and country since 2025-07-01 (illustrative secondary figures ~$0.01 utility to ~$0.06+ marketing; rate card not read). 1,000 free service conversations per WABA per month reported; service-window replies reported to become billable from 2026-10-01. |
| Suspension risk | Unofficial clients (Baileys, WPPConnect, modified apps) explicitly violate terms — permanent, non-appealable bans reported. |
| Scale | Tiers per phone number (250 → 1,000 → 10,000 → …) gated by verification and usage consistency; adequate for dozens of low-volume solo businesses. |

## 3. Telegram

| Attribute | Finding |
| --- | --- |
| Product and prerequisites | Bot API via @BotFather: free, instant, no review or business verification. "Telegram Business" lets a bot reply *as* a personal/business account; historically gated behind a Premium/Business subscription — **current gating unverified, secondary sources conflict.** |
| AI replies | No platform restriction reported; external law still applies. |
| Messaging window | None; a bot may message anyone who started a chat with it. |
| Pricing | Free at MVP volumes. |
| Suspension risk | Userbot automation of a personal account (MTProto) is against terms; risk of number restriction. |
| Scale | ~30 msg/s broadcast, 1 msg/s per chat — ample. |

## 4. Facebook Messenger

| Attribute | Finding |
| --- | --- |
| Product and prerequisites | Messenger Platform (Graph API). Needs a business Page; messaging other businesses' Page conversations needs App Review (`pages_messaging`) plus Business Verification, once per app. |
| AI replies | Permitted, disclosure recommended. |
| Messaging window | Same 24-hour window and tag rules as Instagram. |
| Pricing | No per-message charge reported. |
| Suspension risk | Automated abuse of `HUMAN_AGENT`, scraping, Page policy violations. |

## 5. Constraints most likely to reshape a one-month MVP (agent's ranking)

1. App Review plus Business Verification lead time on Instagram / Messenger / WhatsApp — days to weeks — and every practitioner must hold a Professional account / Page / WABA, not a personal profile, before any on-behalf messaging works.
2. WhatsApp's reported ban on general-purpose AI chatbots forces a narrowly scoped conversation design (booking, FAQ, status) from day one.
3. Re-engagement tag deprecation on Instagram / Messenger (2026-04-27) limits "follow up after 24 h" automation there; reminders need WhatsApp templates or opt-in capture designed in from the start.
4. WhatsApp template pre-approval and a pricing model still changing during the build.
5. Every fast shortcut (unofficial WhatsApp libraries, browser automation, Telegram userbots) is exactly what gets accounts permanently banned.

## 6. AI-disclosure obligations (secondary-sourced; not legal advice)

- **EU** — AI Act (Reg. (EU) 2024/1689) Art. 50(1): systems interacting with natural persons must inform them they are dealing with AI unless obvious from context; reported applicable from 2026-08-02. The provider carries the design duty; the practitioner as deployer faces the client, so disclosure must reach the client either way.
- **US federal** — no enacted general bot-disclosure statute found; bills pending; FTC guidance recommends clear disclosure.
- **California** — B&P Code §17941 (SB 1001, in force since 2019-07-01): unlawful to use a bot to mislead a Californian about its artificial identity to induce a commercial transaction; safe harbor with clear, conspicuous disclosure. Directly relevant to a booking bot. SB 243 (companion chatbots, 2026-01-01) probably does not reach a booking/FAQ bot — unverified.
- **Utah** — AI Policy Act (2024, amended 2025): disclosure on request generally; proactive disclosure for "regulated occupations" — whether cosmetology/esthetics counts is **unverified**.
- **Ukraine** — no binding AI-specific disclosure statute found; EU-aligned law reported as planned for 2026 drafting. Existing consumer-protection duties not exhaustively checked.
- **Kazakhstan** — Law No. 230-VIII "On Artificial Intelligence" (adopted 2025-11-17, reported in force 2026-01-18): businesses using chatbots must inform clients of automated personal-data processing, the right to object and the rights-protection procedure; fines scale by business size. **Article number unverified**; primary text unreachable.

## 7. Could not verify

- Meta's own policy text for the WhatsApp general-purpose-AI restriction and its exact scope.
- The current WhatsApp per-country per-message rate card.
- Current Telegram Business gating for bot-reply-on-behalf-of-account.
- The Kazakh law's article number for the chatbot-disclosure clause.
- Whether Utah's regulated-occupation duty covers cosmetology/esthetics.
- Ukraine: any incidental disclosure duty in existing consumer or e-commerce law.

## 8. What this means for the brief (Co-Pilot reading, not a decision)

- The "one channel first" recommendation is reinforced: Telegram has no onboarding gate; Instagram and WhatsApp each need Meta review and per-practitioner business identities, which alone can consume much of a one-month window.
- The agent's role must be scoped to structured tasks with escalation to the practitioner — required by WhatsApp's reported policy and prudent everywhere else.
- AI disclosure to the client should be treated as a default product behavior, not a per-jurisdiction toggle: Kazakhstan (a first test market) reportedly requires it now; the EU from 2026-08-02; California for commercial bots.
- Before any Meta channel is built, read the primary developer pages and confirm the rows above; before launch in any jurisdiction, obtain qualified legal review (contract §4).
