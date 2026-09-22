# Competitor and alternative scan — 2026-09-22

**Question (brief U4, assumption A4):** which products already automate, for beauty / aesthetic / cosmetology practitioners, (a) AI replies to client DMs on Instagram / WhatsApp / Telegram, (b) booking and reminders, (c) client card / CRM and treatment history, (d) social content generation including AI avatars, (e) supplier ordering?

**Evidence standard — read first.** Desk research by a delegated agent (Claude Sonnet, medium effort), retrieved 2026-09-22. Direct fetches of vendor sites were blocked by the session's network proxy; **all rows come from web-search summaries of vendor pages and third-party reviews, not from reading the pages.** Prices are as quoted in those summaries and must be confirmed on the vendor's own pricing page before use in any calculation; UNKNOWN means no published figure was found. No product was tested hands-on. Coverage of Ukraine and Kazakhstan is partial.

## 1. United States

| Product | Type | Covers | Channels | Price as found | Segment | AI persona as the practitioner |
| --- | --- | --- | --- | --- | --- | --- |
| Zenoti (zenoti.com) | vertical suite | b, c, e; a partial | phone AI receptionist; Instagram/Google booking is link-based, not a DM conversation | from ~$400/mo, quote-based | clinic, multi-location | no — branded receptionist |
| Boulevard (joinblvd.com) | vertical suite | b, c, e | web/phone; no native AI DM agent | ~$175–500+/mo per location | clinic, upscale solo | no |
| Mangomint (mangomint.com) | vertical suite | b, c; a partial (two-way texting add-on) | SMS | ~$120/mo + $10/user | solo to small clinic | no |
| Vagaro (vagaro.com) | vertical suite | b, c, e; a partial (web chat receptionist); d partial (text only) | web chat, booking; IG/WA not confirmed | core plan UNKNOWN; phone add-on via third party ~$109/mo | solo to clinic | no |
| GlossGenius (glossgenius.com) | vertical suite | b, c; d partial (text generation) | SMS/calls via third-party add-ons; sources conflict on a built-in AI receptionist | from ~$24/mo | solo-focused | no |
| AI Receptionist for Med Spas (aireceptionistmedspa.com) | vertical AI layer | a, b; writes into Vagaro/Mindbody/Boulevard | Instagram DM, WhatsApp, SMS, calls | from ~$199/mo | solo and small clinic | branded virtual front desk |
| AI Beauty Bot (ai-beauty.bot) | vertical AI layer | a, b; c partial (remembers history, syncs to connected CRM) | WhatsApp, Instagram, Telegram, Viber | ~$79 / $149 / $219 per mo | solo and small clinic | branded "salon administrator" |
| Podium — Avery AI Employee (podium.com) | horizontal, markets to niche | a, c | calls, text, web chat; IG/WA unconfirmed | UNKNOWN (quote only) | clinic, multi-location | no |

## 2. Russian-speaking markets (UA / KZ / RU)

| Product | Type | Covers | Channels | Price as found | Markets | AI persona |
| --- | --- | --- | --- | --- | --- | --- |
| YCLIENTS (yclients.com) | vertical suite | b, c; e partial (inventory); a via marketplace add-ons | native booking; WhatsApp/Telegram bots via third-party apps | ~412–686 ₽/mo solo; ~4,971 ₽/mo team | Russia; limited CIS reach post-2022 | no native |
| Altegio (alteg.io) — YCLIENTS' international line | vertical suite | b, c, e partial; a via native chatbot and marketplace | WhatsApp, Telegram, Instagram, Viber | UNKNOWN; Ukraine pricing stated as lower | Ukraine, Kazakhstan, Armenia, Cyprus, Serbia, Hungary, UAE, Brazil | no native |
| DIKIDI Business (dikidi.net) | vertical suite | b, c | WhatsApp/Telegram/SMS reminders | free tier; paid from ~450 ₽/mo | Russia, Ukraine, Kazakhstan, CIS | no |
| Salonbot (salonbot.ru) | vertical AI layer | a, b; c via CRM integration | WhatsApp, Telegram | UNKNOWN (14-day trial) | Russia | branded "AI-администратор" |
| Salebot (salebot.pro) | horizontal builder | a; c | Telegram, VK, WhatsApp, Instagram, Avito, MAX | free tier; paid from ~1,299–2,999 ₽/mo | Russia/CIS | configurable, no out-of-box persona |
| Say-Say (say-say.ru) | YCLIENTS integration layer | a | WhatsApp/Telegram inside YCLIENTS | ~5,000 ₽/mo | Russia | no |
| Arnica | vertical | a, b, c | WhatsApp booking bot | UNKNOWN | Russia | partial (booking-only bot) |

Ukraine-specific tools named but not price-verified: EasyWeek, RO App, Appointer, ProcessFather. Kazakhstan-specific vendors beyond Altegio were not identified.

## 3. AI avatar / talking-head content tools

| Tool | Function | Price as found | Fit for a non-technical solo user |
| --- | --- | --- | --- |
| HeyGen | avatar video, lip-sync, translation | free tier with watermark; ~$29/mo creator; ~$99/mo pro | high |
| Synthesia | avatar video | free tier; ~$29/mo starter; ~$89/mo creator | high |
| D-ID | avatar talking head, API-first | from ~$6/mo | medium |
| Captions (Mirage) | mobile-first avatar / digital twin for social | free tier; paid ~$10–25/mo (sources disagree) | high |
| Arcads | stock AI-actor UGC-style ad clips | ~$77–110/mo | medium (not a personal-brand avatar) |

## 4. Closest competitors (agent's verdict)

1. **AI Beauty Bot** — closest feature match to "DMs + client memory + reminders": native AI across WhatsApp / Instagram / Telegram / Viber, solo pricing. Does not own the client record (plugs into Altegio, Vagaro and similar), generate content or order from suppliers.
2. **Zenoti** — the only suite found with a native, non-add-on AI receptionist plus full CRM/booking/inventory. Not confirmed for conversational AI inside Instagram DMs; no avatar content; positioned and priced for multi-location clinics.
3. **Altegio / YCLIENTS ecosystem** — strong native client card, booking and reminders in the first test markets. DM-AI is always a bolted-on marketplace app; no content generation; supplier ordering unconfirmed beyond inventory.

No product in either market was found combining (a)–(e) natively, and none was found marketing an AI persona that speaks as the *individual* practitioner — every AI front desk found is a branded "salon assistant".

## 5. Not covered / could not verify

- No vendor page read directly; pricing and feature claims are secondary-sourced.
- No hands-on testing; supplier-ordering claims not verified end-to-end for any product.
- Pure horizontal DM builders (ManyChat, Tidio, Chatfuel) excluded from the tables by design.
- Ukraine and Kazakhstan coverage partial; currencies left as published, no FX conversion.

## 6. What this means for the brief (Co-Pilot reading, not a decision)

- Assumption A4 ("no ready product closes this set") is **partly wrong as stated**: DM automation with booking, reminders and client memory exists at solo prices in both markets (AI Beauty Bot, Salonbot, Altegio add-ons). What was *not* found is the combination with a practitioner-voice persona, content generation and supplier ordering in one product.
- Positioning therefore shifts from "nothing exists" to "existing tools are branded front desks bolted onto a CRM; the gap is the practitioner's own voice plus the rest of the routine in one place" — a hypothesis to test, not a finding.
- The price anchor for an AI DM layer at solo scale is roughly $79–219/mo (AI Beauty Bot tiers, secondary-sourced). The brief's $400–500/mo assumption must be justified by covering materially more of the routine, or revised.
- Build-vs-adopt (P6) has concrete candidates to inspect for the CRM substrate (Altegio in UA/KZ; Vagaro, Mangomint, GlossGenius in the US) before any custom client-card implementation.
