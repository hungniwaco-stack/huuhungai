---
title: Paperclip Hermes Agent: a model for organizing work with AI
desc: Paperclip orchestrates agents like a company: org chart, heartbeat cadence, cost tracking. Connecting Hermes Agent via adapter, key settings and cautions.
min: 7
---
QUICK: Paperclip is an open-source app that orchestrates several agents in a company model (org chart, issue system, heartbeat cadence, cost tracking). Hermes Agent plugs in as an "employee" through an adapter. Nous Research's official adapter runs Hermes per task and reports results back to Paperclip. The model suits experimentation, and is not yet something to hand important work to right away.
## What Paperclip is
According to the description in the adapter repo, Paperclip is an orchestration platform with a heartbeat scheduler, an issue system, comment-based wake-ups, cost tracking, skill sync and an org chart. Agents execute through adapters to underlying runtimes such as Claude Code, Codex or Hermes Agent. Searching shows Paperclip is an open-source project under the MIT license, running on Node.js with a React interface. The idea: you are the CEO, you hand out goals, and the agents play employees who take work by rank.
A point to keep separate: Paperclip is a project of its own; Hermes is just one of the runtimes it can control.
## The official adapter
Nous Research has the `NousResearch/hermes-paperclip-adapter` repo for running Hermes as a managed employee in a Paperclip company. Requirements per the README:
- Hermes Agent installed (`pip install hermes-agent`).
- Python 3.10 or later.
- At least one model provider API key (Anthropic, OpenRouter or OpenAI).
- A Paperclip server with an adapter registry, where you register the adapter by hand.
Install the package:
```
npm install hermes-paperclip-adapter
```
Registration means you must edit the Paperclip server code yourself: import `hermes-paperclip-adapter/server` and put a `hermes_local` entry in the registry. The README says plainly that registration is manual, so do not expect one click to finish the install.
## How the adapter works
Each time work is dispatched, the adapter runs the Hermes CLI in single-query mode (the `hermes chat -q` form), Hermes handles it with tools and then exits. The adapter collects the output, pulls out token counts, session id and cost, turns them into structured records and reports the result and cost back to Paperclip. When `persistSession` is on, each run reattaches to the session with the `--resume` flag, so context, memory and tool state are kept between heartbeats.
## Main configuration fields
- `model` (default `anthropic/claude-sonnet-4`) and `provider` (auto-detected).
- `timeoutSec` (default 300) and `graceSec` (default 10).
- `toolsets`: the list of allowed tool groups, for example `terminal,file,web`. The default is all, so narrow it.
- `persistSession` (on by default), `worktreeMode` (isolation with a git worktree, off by default), `checkpoints` (file restore points, off by default).
- `promptTemplate` with variables such as `{{taskTitle}}`, `{{taskBody}}`.
- `paperclipApiUrl` default `http://127.0.0.1:3100/api`.
## Risks to weigh
- **Execution permissions.** On each run, Hermes has the same permissions as your account (a profile is not a sandbox). For an "agent" company that runs itself on a heartbeat, limit `toolsets`, turn on `worktreeMode` and `checkpoints`, and consider the Docker backend.
- **Multiplied cost.** Many agents running on a heartbeat means tokens are spent steadily even when there is nothing important to do. Set a budget and watch the cost Paperclip reports.
- **Integration stability.** There are many community-written adapters because the built-in integration is complained about for skipping some configuration; that shows this glue layer is still changing.
- **Comparisons in the README.** The table comparing Hermes with Claude Code and Codex in the README is the authors' own assessment, not independently verified.
## Do you need Paperclip
Hermes already has its own ways to coordinate: [multi-profile Kanban](thiet-lap-kanban-cho-hermes-quan-ly-quy-trinh-xay-website-bang-ai.html), subagents and Bot Mode. Paperclip is worth considering when you want an "organization" layer over several kinds of agents (not just Hermes) with a budget and a rank chart. If you only use Hermes, start with the built-in features.
## How to try it safely
1. Run Paperclip on a test machine, not a machine holding important data.
2. Register the adapter and hand out a read-only task.
3. Watch the logs, the cost and what `hermes chat -q` actually does.
4. Expand permissions step by step and keep irreversible work for a reviewer, see [Roles in Hermes Swarm: builder, reviewer and how to coordinate](cac-vai-tro-trong-hermes-swarm-builder-reviewer-va-cach-phoi-hop.html).
