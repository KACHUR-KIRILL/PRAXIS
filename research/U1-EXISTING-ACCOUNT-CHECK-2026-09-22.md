# U1 — can the agent answer in the practitioner's existing accounts? — 2026-09-22

**Question (Owner, 2026-09-22, Issue #1):** can the agent reply inside the practitioner's *existing* Telegram, WhatsApp and Instagram accounts rather than through a separate bot? If only a separate bot is possible, the main pain is not removed. Sub-questions set by the Owner: Telegram Business — what it requires, is Premium needed; WhatsApp API on the practitioner's current number without disabling their app; Instagram — Meta app review timelines.

**Evidence standard — read first.** Executor: Founder Co-Pilot session, 2026-09-22. The session's egress proxy blocked `telegram.org`, `core.telegram.org`, `developers.facebook.com`, `business.whatsapp.com` and `facebook.com` for both direct fetch and the fetch tool. Three evidence levels are used and marked per row:

- **A — primary source read.** Telegram's own TDLib API schema and client code on GitHub, read in full at a pinned commit.
- **B — official page, search excerpt only.** Titles and excerpts of pages on Meta's or Telegram's own domains returned by web search; the page itself was not opened. Stronger than third-party reporting, weaker than reading the page.
- **C — secondary.** Carried over from [CHANNEL-POLICY-CHECK-2026-09-22.md](CHANNEL-POLICY-CHECK-2026-09-22.md).

Nothing here is legal advice.

## 1. Answer in one table

| Channel | Agent in the existing account? | Conditions that matter for the MVP | Evidence |
| --- | --- | --- | --- |
| Telegram | **Yes** — Telegram Business lets a bot act inside the practitioner's own account, in private chats the practitioner selects | Bot may send only in chats with an incoming message in the last 24 hours, so reminders cannot come from the practitioner's account; Premium requirement contradictory | A (mechanics, 24 h rule); B, contradictory (Premium) |
| WhatsApp | **Yes, conditionally** — "Coexistence" keeps the same number working in the WhatsApp Business app and the Cloud API at once | Practitioner must use the **WhatsApp Business app** (not personal WhatsApp), version ≥ 2.24.17; we must be a Meta Tech Provider / Solution Partner; companion devices are unlinked at onboarding; AI use is constrained by the Business Solution Terms | B |
| Instagram | **Yes** — the API acts inside the practitioner's own Instagram professional account | Account must be Professional (Business/Creator); serving accounts we do not own needs Advanced Access = App Review + Business Verification, once per app; Meta states an average of about 24 hours for App Review; Business Verification time not found | B; C |

**Reading:** the separate-bot-only outcome that would leave the main pain unsolved was **not** found on any of the three channels. Every channel has a condition that changes the MVP: the 24-hour reply rule on Telegram, account type and partner status on WhatsApp, and Meta review on Instagram and WhatsApp.

## 2. Telegram

**Source A:** `tdlib/td` at commit `ea97bcdd3a15523c58ddfe772b4547187cf5bbeb`, file `td/generate/scheme/td_api.tl` (sha256 `bc998a2c…037d0`), and `td/telegram/BusinessManager.cpp` at the same commit. TDLib is Telegram's official client library; the schema comments are Telegram's API documentation.

| Finding | Evidence | Quote / location |
| --- | --- | --- |
| A bot can be connected to a user account and act in its private chats | A | `setBusinessConnectedBot` — "Adds or changes business bot that is connected to the current user account"; `businessConnectedBot` — "Describes a business bot connected to an account" |
| The practitioner chooses which chats the bot may access: existing, new, contacts, non-contacts, listed chats, exclusions | A | `businessRecipients` — `select_existing_chats`, `select_new_chats`, `select_contacts`, `select_non_contacts`, `chat_ids`, `excluded_chat_ids`, `exclude_selected` |
| **The bot may send only into chats that had an incoming message in the last 24 hours** | A | `businessBotRights.can_reply` — "True, if the bot can send and edit messages in the private chats that had incoming messages in the last 24 hours" |
| The practitioner can pause the bot per chat and take over | A | `businessBotManageBar.is_bot_paused` — "Use toggleBusinessConnectedBotChatIsPaused to change the value" |
| Messages sent by the bot are marked as sent by a business bot | A | `message.sender_business_bot_user_id` — "If non-zero, the user identifier of the business bot that sent this message" |
| Connecting a bot is listed as a Business feature, and Business features are listed as a Premium feature | A (schema) | `businessFeatureBots` — "The ability to connect a bot to the account"; `premiumFeatureBusiness` — "The ability to use Business features" |
| The client library itself does not check Premium before connecting a bot; any gate is server-side | A | `BusinessManager::set_business_connected_bot` sends `account.updateConnectedBot` with no Premium check |
| "Connecting a business bot does not require Telegram Premium" | B | search excerpt attributed to `core.telegram.org/api/bots/connected-business-bots` and related pages; page not opened |
| The official Hermes plugin for Telegram Business lists "A Telegram **Business** subscription on your personal account" as a requirement | A (third-party code, maintained by Nous Research, not by Telegram) | `NousResearch/hermes-telegram-business` @`98c60af`, README, Requirements; added 2026-09-22 |
| Premium price per country | not found | the Premium FAQ says prices vary by region and payment method |

**Premium — unresolved, leaning towards required.** The schema groups bot connection under Premium-linked Business features and the Hermes plugin README requires a Business subscription; an official-page excerpt says Premium is not required; enforcement is server-side and not visible in code. **Cheapest decisive check:** connect a test bot (from @BotFather) to a Telegram account without Premium in Settings → Telegram Business → Chatbots, if that menu is reachable without Premium. About 10 minutes, no cost, no third parties.

**Consequences for the MVP:**
- Replies to clients in the practitioner's own account: feasible.
- **Reminders are not possible from the practitioner's account** once 24 hours have passed since the client's last message. Options: a separate PRAXIS bot the client starts once (for example, via a link in the booking confirmation), the practitioner sending them manually, or asking the client to reply. Unofficial userbot automation is excluded by contract §5.
- The practitioner's clients see messages from the practitioner's account; AI disclosure (Owner decision, brief §15) has to be in the message text, since the sender marker is not a disclosure a client reliably sees.

## 3. WhatsApp — same number, app keeps working ("Coexistence")

| Finding | Evidence | Page |
| --- | --- | --- |
| Embedded Signup can onboard a business "using their existing WhatsApp Business app account and phone number" ("Coexistence") | B | [Onboard WhatsApp Business app users](https://developers.facebook.com/documentation/business-messaging/whatsapp/embedded-signup/onboarding-business-app-users) |
| After onboarding the business "can still send messages on a one-to-one basis using the WhatsApp Business app, and WhatsApp keeps messaging history between both apps in sync" | B | same |
| Requires WhatsApp **Business** app version 2.24.17 or higher | B | same |
| The integrator must already be a Solution Partner or Tech Provider | B | same |
| Fixed throughput of 20 messages/second for numbers used in both | B | same |
| History must be synchronized within 24 hours of onboarding, otherwise the business is offboarded and must repeat the flow | B | same |
| On onboarding "all companion apps will be unlinked"; supported companion apps can be re-linked; unsupported companion clients see placeholder text | B | same |
| Users in Cuba, Iran, North Korea, Syria and the Crimea, Donetsk and Luhansk regions of Ukraine cannot receive Business Platform messages | B | Cloud API support pages |
| General-purpose AI assistants are prohibited as the primary functionality; a business may retain an AI provider as a third-party service provider, and Business Solution Data may not train general models | B | [WhatsApp Business Solution Terms](https://www.whatsapp.com/legal/business-solution-terms) |
| 24-hour service window; business-initiated messages need approved templates; per-message pricing | C | channel policy check §2 |

**Not found:** which countries are eligible for Coexistence (none of the excerpts named UA or KZ as excluded or included, apart from the sanctioned Ukrainian regions above); whether a practitioner on personal WhatsApp can switch to the Business app without losing chats; how long Tech Provider onboarding and its App Review take.

**Consequences:** feasible without disabling the practitioner's app, if they use or switch to the WhatsApp Business app and we complete Meta partner onboarding first. Reminders need paid templates. The agent must be a business-specific assistant, which the MVP already is.

## 4. Instagram

| Finding | Evidence | Page |
| --- | --- | --- |
| The Instagram API with Instagram Login lets an app send and receive messages for Instagram Business and Creator accounts | B | [Overview of the Instagram API](https://developers.facebook.com/docs/instagram-platform/overview/) |
| Serving professional accounts we do not own requires Advanced Access, which requires App Review and Business Verification | B | [App Review for Instagram API](https://developers.facebook.com/documentation/instagram-platform/app-review) |
| "The average turnaround time for App Review is about 24 hours"; actual time varies | B | Meta App Review pages |
| Developer-forum threads report reviews taking much longer | B (forum, not policy) | [Why App Review is taking so long?](https://developers.facebook.com/community/threads/320400731958800/) |
| 24-hour messaging window; `HUMAN_AGENT` tag for humans only | C | channel policy check §1 |

**Not found:** Business Verification duration; number of review rounds typical for a messaging app. Meta's "24 hours on average" is a stated average, not a planning figure; a rejection adds a full cycle.

**Consequences:** the agent works inside the practitioner's own professional account (switching from a personal account is a general-knowledge step, not verified here; for a non-technical user it bears on assumption A7). Review and verification happen once per app, not per practitioner, but must be complete before the first practitioner outside our own test accounts.

## 5. What this changes (Co-Pilot reading, not a decision)

1. **The main pain is addressable on all three channels.** The Owner's stop condition for U1 ("only a separate bot") is not triggered by this evidence.
2. **Telegram remains the fastest first channel** — no Meta review, and the existing-account mode is in the official API. It needs the 10-minute Premium check and a reminder design around the 24-hour rule.
3. **Reminders are the part of the MVP most affected.** On Telegram they need a second bot or a manual step; on WhatsApp paid templates; on Instagram only within 24 hours.
4. **Which channel the practitioners' clients actually use is still unknown.** The U3 offer conversations can collect it at no extra cost (see the U3 test design).
5. Before a Meta channel is built: open the Meta pages above from an unrestricted network and confirm the B rows.

## 6. Limitations

- Telegram rows at level A come from the API schema and client code, which describe capabilities, not Terms of Service; the Telegram Business ToS (`telegram.org/tos/business`) was not read.
- All Meta rows are level B: official-domain search excerpts, pages not opened. Excerpts can be stale or cut mid-sentence.
- No account was connected and no message was sent; nothing here is demonstrated in practice.
