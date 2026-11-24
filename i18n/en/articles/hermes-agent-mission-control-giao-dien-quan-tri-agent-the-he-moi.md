---
title: Hermes Agent Mission Control: a new generation of agent management interfaces
desc: Mission Control for Hermes Agent: no official version, only community projects. The official dashboard compared with community ones and how to choose safely.
min: 6
---
QUICK: Hermes Agent has no Nous Research product called "Mission Control". The name is used by many independent community projects for agent tracking boards. If you only need to view sessions, costs and logs, the official web dashboard (`hermes dashboard`) is already available. Use a community version only when you need something it has that the official one lacks.
## What Mission Control is, and is not
When you search "Hermes Agent Mission Control" on GitHub you will find a series of independent repos, not a single project. A search on 2026-11-15 showed, according to the repos' own descriptions:
- A real-time activity board for a team of Hermes bots, reading the state database in read-only mode.
- A locally run control board that shows sessions, agents, usage and tools.
- A plugin that adds a Mission Control tab to Hermes's own dashboard, installed with `hermes plugins install`.
- A board for Hermes Desktop that shows tool calls, subagents, tokens, cache hits, cost and loop alerts, read-only and running locally.
- A self-hosted dashboard template that talks to the agent through an intermediate database.
## What the official version already has
The Hermes documentation describes the Web Dashboard as a browser-based management panel, run with:
```
hermes dashboard
```
By default it serves on port 9119 at the address `127.0.0.1`. The main sections include:
- **Status:** version, gateway status, running sessions, memory and disk warnings.
- **Chat:** the Hermes terminal embedded in the browser.
- **Config and API Keys:** edit `config.yaml`, manage keys (displayed masked).
- **Sessions, Logs, Analytics:** search sessions, view live logs, track tokens and cost by day and by model.
- **Cron, Profiles, Skills, MCP:** scheduled tasks, profiles, skills and MCP servers.
- **Kanban:** a task board across profiles (see [Setting up Kanban for Hermes](thiet-lap-kanban-cho-hermes-quan-ly-quy-trinh-xay-website-bang-ai.html)).
That means most "manage and monitor" needs are already met without installing anything more.
## When a community version is worth considering
- You run many bots at once and want an overview screen in a "team lineup" style.
- You need cost alerts, loop alerts or a subagent chart that the official version does not show the way you want.
- You accept checking the source code and updating it yourself.
## Checklist before installing a community board
1. **Read-only or write access?** A read-only board is much safer. If there are buttons that control the agent, understand exactly what they call.
2. **What data does it read?** Sessions and memory can contain private information. Does the data leave the machine?
3. **Network port.** Keep it on `127.0.0.1` only. The official documentation states that when the dashboard is on at a non-loopback address, there must be a login, because it can read secret keys and run agent commands.
4. **License and last update.** An abandoned project breaks when Hermes changes its data structure.
5. **Does it depend on the Hermes version?** Many projects read internal state files directly and may break after an update.
## General security warning
Any kind of dashboard is a door into your agent. Do not expose it to the internet with a simple password. The official documentation recommends Nous Portal (OAuth) sign-in for internet exposure, with username and password reserved for trusted networks or VPN. If you only need to view remotely, use an SSH tunnel or private network instead of opening a port.
## Instead of installing more
If the goal is to understand what the agent is doing, start with the official board, and look at the logs and token counts. Add tools only when you can name the specific thing that is missing. Alternative chat interfaces are also available in [Hermes WebUI](hermes-webui-dung-giao-dien-chat-cho-agent-trong-vai-buoc.html) and [Hermes Workspace](thiet-lap-hermes-workspace-nen-lam-viec-cho-ai-agent.html).
