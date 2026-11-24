---
title: OpenClaw: security lessons when connecting messaging, cron and webhooks
desc: Security lessons for connecting OpenClaw to messaging and automation: who can message, outside content, scheduled tasks, a hardened baseline and checks.
min: 9
---
QUICK: When you connect OpenClaw to messaging (Telegram, WhatsApp...) and automation (cron, webhooks, Gmail), the biggest risk is untrusted content reaching an agent that has tools. The lessons from the documentation: lock down who can message, block every tool you do not need, do not turn on flags that allow outside content, and run `openclaw security audit` regularly, especially after every update.
## Why integrations are where things leak
OpenClaw turns outside chat and events into commands for the agent. Each entry point is a path for strange content to reach the model. The security documentation lists the untrusted sources: direct messages and public groups, web pages and search results, email (including Gmail hooks), attachments, pasted logs or code, hook and cron data, and OpenResponses input URLs. Prompt injection does not need a malicious sender; content the agent reads can also carry instructions.
## Lesson 1: lock down who can message
For Telegram, the documentation describes the direct message policy `channels.telegram.dmPolicy`:
- `pairing` (default): access is granted through pairing.
- `allowlist`: only IDs in `allowFrom` can message; an empty list is rejected.
- `open`: needs `allowFrom` to contain `"*"`, so any Telegram account that finds the bot can command it. Use it only for a public bot with tightly limited tools.
- `disabled`: turns off direct messages.
For a single-owner bot, the documentation advises using `allowlist` with explicit numeric IDs instead of relying on pairing approval. Pairing approval only grants direct message access, not access in groups. For groups, all groups are blocked by default until you add them to the list, and the bot only replies when mentioned by name. A common mistake: `groupAllowFrom` is not a list of groups; group IDs (negative numbers) go in `groups`, user IDs go in `groupAllowFrom`.
## Lesson 2: automation receives untrusted content
The Automations documentation describes the built-in scheduler (`openclaw automations`, alias `openclaw cron`), along with webhooks (`POST /hooks/wake`, `/hooks/agent`, `/hooks/<name>`) and triggers from Gmail via Google Pub/Sub, and recommends using a restricted Gmail reader. An example creating a one-time reminder:
```
openclaw automations create "2027-02-01T16:00:00Z" --name "Reminder" --session main --system-event "Reminder: check the automations docs draft" --wake now --delete-after-run
```
From the security page, things to do with automation:
- For hook-driven automation, use `tools.profile: "messaging"` or stricter.
- **Keep the guardrail-bypassing flags off** in real environments: `hooks.mappings[].allowUnsafeExternalContent`, `hooks.gmail.allowUnsafeExternalContent` and the `allowUnsafeExternalContent` field in cron data.
- Restrict `exec`, `browser`, `web_fetch`, `web_search` to trusted agents or an explicit allowlist.
- Set a tight URL allowlist for OpenResponses input, or turn off URL input altogether.
## Lesson 3: separate the "reader" from the "doer"
A pattern the documentation suggests: use a read-only or tool-less agent to summarize untrusted content, then hand the summary to the main agent. But the summary is still untrusted content, and one-way sending permission does not stop the recipient from leaking data or acting on an injected request. Agent-to-agent is on by default; set an explicit allowlist or turn it off with `tools.agentToAgent.enabled: false`.
## Lesson 4: models and the limits of defense
The documentation advises using the newest-generation, best-tier model for agents with tools or that read untrusted inboxes; small and older models are much easier to steer. It cites a 2026 study with attack success rates from 0.5% to 8.5% depending on the model, but states plainly that this is a static result, and adaptive attackers still succeeded at high rates according to the report. In other words, the measures above reduce risk but do not remove it.
## A sample hardened baseline
The "hardened baseline" page gives a sample configuration that keeps the Gateway local, uses pairing and restricts tools. The main parts:
```
{
  gateway: { mode: "local", bind: "loopback", auth: { mode: "token", token: "set-a-long-random-token" } },
  session: { dmScope: "per-channel-peer" },
  tools: {
    profile: "messaging",
    deny: ["group:automation", "group:runtime", "group:fs", "sessions_spawn", "sessions_send"],
    fs: { workspaceOnly: true },
    exec: { security: "deny", ask: "always" },
    elevated: { enabled: false },
    sessions: { visibility: "agent" },
    agentToAgent: { enabled: false },
  },
  channels: { whatsapp: { dmPolicy: "pairing", groups: { "*": { requireMention: true } } } },
}
```
The documentation advises turning tools back on selectively for each trusted agent instead of loosening globally, and considering running the assistant with a separate phone number, not a personal one. It also states plainly that controls such as `toolsBySender` are "defense in depth", not isolation for adversarial multiple users; when parties do not trust each other, use separate Gateways, ideally separate users or machines.
## Regular checks
```
openclaw security audit
openclaw security audit --deep
openclaw security audit --fix
```
The command checks inbound access, cross-agent session access, tool risk, exec configuration drift, network exposure, browser control exposure, local disk hygiene, plugins and policy drift. `--deep` tries live Gateway checks; `--fix` only applies safe, narrow fixes (turning open group policy into an allowlist, tightening file permissions to 600 and folders to 700). The order the documentation suggests: lock down inbound access first, then fix public network exposure right away, then browser control, file permissions and plugins.
## After every update
Take a verified backup before a major update, then run `openclaw doctor`, `openclaw gateway status --deep` and `openclaw channels status --probe` (see [An OpenClaw learning path: how to keep up with new AI agent tools](lo-trinh-hoc-openclaw-cach-theo-kip-cong-cu-ai-agent-moi.html)). Rerun the audit because defaults and configuration key names can change. For tools that control the screen and browser, see [OpenClaw Computer Use: letting an agent operate a computer safely](openclaw-computer-use-cho-agent-thao-tac-may-tinh-sao-cho-an-toan.html).
