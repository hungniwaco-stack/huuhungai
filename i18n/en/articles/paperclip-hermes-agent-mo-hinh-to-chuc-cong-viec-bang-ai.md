---
title: Paperclip Hermes Agent: a model for organizing work with AI
desc: Paperclip orchestrates agents like a company: org chart, heartbeat cadence, cost tracking. Connecting Hermes Agent via adapter, key settings and cautions.
min: 7
---
QUICK: Paperclip is an open-source app that orchestrates several agents in a company model (org chart, issue system, heartbeat cadence, cost tracking). Hermes Agent plugs in as an "employee" through an adapter. Paperclip's documentation now says the `hermes_local` adapter is built in with no plugin to install, so the earlier manual registration is no longer the main route. The model suits experimentation, and is not yet something to hand important work to right away.
## What Paperclip is
According to the description in the adapter repo, Paperclip is an orchestration platform with a heartbeat scheduler, an issue system, comment-based wake-ups, cost tracking, skill sync and an org chart. Agents execute through adapters to underlying runtimes such as Claude Code, Codex or Hermes Agent. Searching shows Paperclip is an open-source project under the MIT license, running on Node.js with a React interface. The idea: you are the CEO, you hand out goals, and the agents play employees who take work by rank.
A point to keep separate: Paperclip is a project of its own; Hermes is just one of the runtimes it can control.
## The official adapter
**Update, Nov 28, 2026:** per Paperclip's documentation, `hermes_local` is a built-in adapter that runs Hermes Agent on the same machine as Paperclip. An earlier version of this article told you to install an npm package and edit server code, following the README of the `NousResearch/hermes-paperclip-adapter` repo (last code push in April 2026). Follow Paperclip's current documentation. Requirements:
- Hermes Agent installed on the same machine with the official installer, see [Installing Hermes Agent](cai-hermes-agent-don-gian-huong-dan-cho-nguoi-khong-chuyen-ky-thuat.html). Paperclip's environment test suggests `pip install hermes-agent`, but do not just follow it: Hermes's updating page lists pip or PyPI package installs on Python 3.11 to 3.13 as unsupported and recommends the official installer or a packaged build. When I checked on Nov 28, 2026, the latest release on PyPI was 0.19.0 (July 20), while GitHub already had v0.23.4.
- Paperclip's documentation says Python 3.10 or later, but current Hermes code declares 3.11 or later, and the Hermes installer provisions a suitable Python version itself.
- A model configured for Hermes, usually in `~/.hermes/config.yaml`. The documentation advises leaving the adapter's `model` field empty if Hermes already works.
- A current Paperclip server.
If Hermes runs on another machine with its API server enabled, Paperclip also has the `hermes_gateway` adapter (built in since v2026.626.0). It needs the API address and Hermes's `API_SERVER_KEY`. The documentation asks you to prefer HTTPS or a private network such as a VPN for any non-local address.
## How the adapter works
Each time work is dispatched, the adapter runs the Hermes CLI in single-query mode (the `hermes chat -q` form), Hermes handles it with tools and then exits. The adapter collects the output, pulls out token counts, session id and cost, turns them into structured records and reports the result and cost back to Paperclip. When `persistSession` is on, each run reattaches to the session with the `--resume` flag, so context, memory and tool state are kept between heartbeats.
## Main configuration fields
- `model` (optional, defaults to Hermes's own setting) and `provider` (default `auto`).
- `timeoutSec` (default 1800; the older README says 300) and `graceSec` (default 10).
- `toolsets`: the list of allowed tool groups, for example `terminal,file,web`. The default is all, so narrow it.
- `persistSession` (on by default), `worktreeMode` (isolation with a git worktree, off by default), `checkpoints` (file restore points, off by default).
- `promptTemplate` with variables such as `{{taskTitle}}`, `{{taskBody}}`.
- `paperclipApiUrl`: an optional API address override. When unset, the adapter uses `PAPERCLIP_API_URL`.
## Risks to weigh
- **Execution permissions.** On each run, Hermes has the same permissions as your account (a profile is not a sandbox). For an "agent" company that runs itself on a heartbeat, limit `toolsets`, turn on `worktreeMode` and `checkpoints`, and consider the Docker backend.
- **Multiplied cost.** Many agents running on a heartbeat means tokens are spent steadily even when there is nothing important to do. Set a budget and watch the cost Paperclip reports.
- **Integration stability.** Installation and defaults have changed between the older README and the current documentation, so check the documentation for the version you run.
- **Comparisons in the README.** The table comparing Hermes with Claude Code and Codex in the adapter repo's README is the authors' own assessment, not independently verified.
## Do you need Paperclip
Hermes already has its own ways to coordinate: [multi-profile Kanban](thiet-lap-kanban-cho-hermes-quan-ly-quy-trinh-xay-website-bang-ai.html), subagents and Bot Mode. Paperclip is worth considering when you want an "organization" layer over several kinds of agents (not just Hermes) with a budget and a rank chart. If you only use Hermes, start with the built-in features.
## How to try it safely
1. Run Paperclip on a test machine, not a machine holding important data.
2. Create an agent that uses `hermes_local`, set narrow `toolsets` and hand out a read-only task.
3. Watch the logs, the cost and what `hermes chat -q` actually does.
4. Expand permissions step by step and keep irreversible work for a reviewer, see [Roles in Hermes Swarm: builder, reviewer and how to coordinate](cac-vai-tro-trong-hermes-swarm-builder-reviewer-va-cach-phoi-hop.html).
