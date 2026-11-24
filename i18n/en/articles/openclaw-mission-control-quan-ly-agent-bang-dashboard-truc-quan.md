---
title: Mission Control for OpenClaw: community dashboards and the official Control UI
desc: Mission Control for OpenClaw is not an official product: the official Control UI compared with community dashboards, and safe remote access.
min: 7
---
QUICK: OpenClaw already has an official control panel, the Control UI, opened with `openclaw dashboard`. The "Mission Control" projects are independent community products that add a Kanban board and agent tracking. Whichever you use, keep the Gateway on loopback and reach it remotely through Tailscale Serve or a private network, never directly exposed to the internet.
## The official Control UI
The Control UI is a browser-based control panel for a running OpenClaw Gateway. Open it with:
```
openclaw dashboard
```
The command creates a one-time pairing link that expires after ten minutes. When pairing succeeds, that browser receives a per-device admin credential, so next time you open it you do not need the Gateway's shared token. The shared token is not printed to the terminal. Add `--no-open` to only print the address and `--json` to print a connection object for machines. The documentation also describes configuring providers, rotating API keys and editing MCP servers right in this interface. For first-time setup, see [Installing OpenClaw](cai-openclaw-desktop-app-cach-bat-dau-voi-ai-agent-giao-dien-sach.html).
## Community "Mission Controls"
A GitHub search shows many independent repos using this name for OpenClaw, with no single official one. According to each repo's public description:
- Some have a **Kanban board** for assigning work to agents, tracking agent status, a live activity log and scheduled tasks.
- Some are only read-only tracking boards, and some are broader control centers also used with Claude Code and Codex.
- Some repos have been archived by their owners and are read-only, so they should not be used for a new setup.
One specific example is `navjotdhanawat/openclaw-mission-control`. Its README describes a real-time dashboard with a five-column Kanban board (Inbox, Assigned, In Progress, Review, Done), agent monitoring and direct task assignment. Run it with `npx openclaw-mission-control`, then enter the Gateway address (default `ws://127.0.0.1:18789`), the authentication token and the port (default 3000). It needs Node 18 or later and a running Gateway.
## Security warning for community dashboards
The README of the repo above only asks for the Gateway token and gives no guidance on protecting the dashboard itself (it says nothing about access control for its web interface or REST API), and the default address uses `ws://` instead of `wss://`. That means if you expose the dashboard to a network, anyone who gets in can control your agents. You should:
- Run it only on your own machine (`localhost`) or behind a private network.
- Read the source code, or at least check whether the repo is still active, before putting in your Gateway token.
- Treat the Gateway token like an admin password.
## Reaching the Control UI remotely and safely
The Tailscale documentation separates two modes:
- **Serve** (`gateway.tailscale.mode: "serve"`): HTTPS only inside your Tailscale network, with the Gateway staying on loopback. Command: `openclaw gateway --tailscale serve`.
- **Funnel** (`gateway.tailscale.mode: "funnel"`): public HTTPS on the internet. The documentation says a shared password is required, and the Gateway refuses to start if the auth mode is not `password`. It also advises avoiding Funnel for browser control.
One detail to note: binding the Gateway directly to the Tailnet IP address exposes the WebSocket over plain, unencrypted HTTP, so the documentation recommends Serve to get HTTPS. There is also a Cloudflare Tunnel and Access option for people who want to publish through Cloudflare. Run `openclaw security audit` to check your configuration; for general principles, see [Installing OpenClaw](cai-openclaw-desktop-app-cach-bat-dau-voi-ai-agent-giao-dien-sach.html).
## When you need a Mission Control
If you run a few agents and only need to see their status, the Control UI is enough. Consider a community version when you really need a Kanban-style task board and accept checking the risks yourself. A more detailed look at this group of features is in [Mission Control for OpenClaw: an agent squad, task board and memory](openclaw-mission-control-squad-agent-task-board-va-memory-browser.html).
