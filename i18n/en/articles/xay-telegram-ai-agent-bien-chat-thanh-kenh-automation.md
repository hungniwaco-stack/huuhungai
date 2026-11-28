---
title: Building a Telegram AI agent: turning chat into an automation channel
desc: Use Telegram as a control channel for an AI agent: creating a bot, limiting users, groups and privacy mode, setup with Hermes and OpenClaw, safety rules.
min: 8
---
QUICK: Telegram is a light channel for messaging commands to an AI agent from a phone. Both Hermes and OpenClaw have guides: create a bot with @BotFather, give the token to the agent, limit who can message it and test with one message. The most important part is not the setup but permission control: a leaked token or an allowlist that is too wide means strangers can control the agent on your machine.
## Why use Telegram as a channel
Messaging is already on your phone, you do not need to open a web interface, and you can receive notifications from the agent (reports, alerts, results of scheduled tasks). The article [Setting up a Telegram AI agent: token, configuration and the first task](thiet-lap-telegram-ai-agent-token-cau-hinh-va-tac-vu-dau-tien.html) covers the first steps in detail; this article focuses on how to make it a safe automation channel, with both systems.
## Common step: create the bot
In Telegram, open **@BotFather** (check that the name is exactly `@BotFather`), send `/newbot`, set a display name and a unique username ending in `bot`. BotFather returns an API token. **This token is the key that controls the bot**: whoever has the token controls it. If it leaks, use `/token` in BotFather to generate a new one. You can also create a bot in BotFather's web interface instead of chat.
## With Hermes Agent
According to the Hermes documentation:
- **Interactive way:** run `hermes gateway setup` and choose Telegram; the wizard asks for the bot token and the allowed user IDs.
- **Manual way:** add the variables `TELEGRAM_BOT_TOKEN` and `TELEGRAM_ALLOWED_USERS` (the numeric IDs of the allowed people, separated by commas) to `~/.hermes/.env`.
- Start the gateway with `hermes gateway` (or `hermes gateway start`, `hermes gateway status`, `hermes gateway stop`). In the desktop app there is a **Create with QR** button that creates the bot, detects your ID, writes the two variables above into the profile and restarts the gateway.
- Find your user ID with @userinfobot or @get_id_bot; the ID is a number, not a username.
## With OpenClaw
According to the OpenClaw documentation:
```
openclaw channels add --channel telegram --token <bot-token>
openclaw channels status --probe
```
Or configure manually in `~/.openclaw/openclaw.json` with `channels.telegram` containing `enabled`, `botToken`, `dmPolicy: "pairing"` and `groups: { "*": { requireMention: true } }`. The `TELEGRAM_BOT_TOKEN` variable only applies to the default account, and configuration takes priority over environment variables. Then message the bot to create a pairing request and approve it:
```
openclaw pairing list telegram
openclaw pairing approve telegram <CODE>
```
The pairing code expires after 1 hour. For details on direct-message and group policy, see the [security lessons](openclaw-update-bai-hoc-ve-tich-hop-message-cron-va-bao-mat.html).
## Using it in groups
Both systems note the same thing: the bot's **Privacy Mode is on by default**, so in a group the bot only sees `/` commands, replies to it and service messages. To let it see every message, turn it off in BotFather (`/mybots`, choose the bot, Bot Settings, Group Privacy, Turn off) or make the bot a group admin; after changing the mode you must remove the bot from the group and add it again. Group IDs are negative numbers. Hermes has `telegram.require_mention` (accept only when mentioned by name, replying to the bot or matching a pattern), while OpenClaw uses `requireMention` for groups. Hermes also has `TELEGRAM_GROUP_ALLOWED_USERS` (for specific senders in a group) and `TELEGRAM_GROUP_ALLOWED_CHATS` (for all members of the listed groups).
## Safety rules
1. **Limit users.** List only your own numeric ID. Both documents warn that a wildcard allowing everyone to command the bot only suits a public bot with very limited tools.
2. **Keep the token like a password.** Do not paste it in chat, a code repository or a screenshot. Revoke it at once if you suspect a leak.
3. **An agent that takes commands from chat should have narrow permissions.** Do not give the bot permission to run commands on the machine beyond messaging unless needed.
4. **Webhooks need a secret.** Hermes requires `TELEGRAM_WEBHOOK_SECRET` in webhook mode and the gateway refuses to run without it; a local Bot API server has no extra authentication, so bind it to `127.0.0.1` and do not open port 8081 to the internet.
5. **Content in groups is untrusted data.** Other people's messages can contain instructions injected into the agent.
## Turning chat into an automation channel
Once the channel is safe, you can use it for: scheduled tasks that send reports into the chat, notifications when a long task finishes, quick commands from a phone. For how to schedule, see [Hermes AI Agent: using an agent framework to automate work](hermes-ai-agent-dung-framework-agent-de-tu-dong-hoa-cong-viec.html). For each automation, ask yourself: if this message were forged, what is the worst thing the agent would do?
