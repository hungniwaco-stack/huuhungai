---
title: Hermes Agent Workspace: a developer's view of architecture and performance
desc: Hermes Agent from a developer's view: the agent loop, gateway, SQLite sessions, prompt assembly, context compression and why Workspace is only an interface.
min: 8
---
QUICK: Hermes Agent consists of one agent loop shared by the CLI, the messaging gateway and cron; a tool registry; session storage in SQLite with full-text search; and prompt assembly in stable layers to take advantage of the cache. Hermes Workspace is an outside interface layer that talks over HTTP. The documentation pages I checked do not publish latency or throughput measurements, so do not trust any performance figure without a source.
## The main components
According to Hermes's architecture documentation:
- **The agent loop (`AIAgent`):** chooses the provider, builds the prompt, runs tools, retries, switches to fallbacks, compresses context and saves the session. There are three API-call modes.
- **The toolset:** a central registry with more than 70 tools in about 28 groups. The terminal tool has six built-in backends: local, Docker, SSH, Daytona, Modal and Vercel Sandbox, plus backends through plugins.
- **The gateway:** a long-running process with more than 25 messaging platform adapters. It handles session routing, authorization (allowlists, direct-message pairing), slash commands, hooks, the cron heartbeat and background maintenance.
- **Session storage:** SQLite with FTS5. Sessions have parent-child relationships when compressed, are split by platform and are written atomically.
- **Prompt assembly:** layers in a stable order, context, then the parts that change often.
- **Context compression:** summarizes the middle turns when context passes a threshold. The configuration page gives the default `compression.threshold: 0.50`, meaning compression at 50% of the context limit.
- **The provider runtime:** turns `(provider, model)` into an API mode, a key and an address for more than 18 providers, including OAuth and key pools.
- **Skills and cron:** bundled skills are always available, optional skills must be installed; a cron task runs with a fresh agent with no history and then sends the result to the destination platform.
## Data flow
Three entry points use the same core:
- **CLI:** the command-line interface calls the conversation loop, through prompt building, the API call, tool running, then saving to the session database.
- **Gateway:** a message from a platform becomes an event, passes the permission check and session key resolution, goes to the agent with the history and then is answered through the same adapter.
- **Cron:** when the time comes, it creates a fresh agent, loads skills, sends the response and calculates the next run.
What a developer should take away: the same core serves all three, so behavior and configuration are consistent between the terminal and the messaging bot.
## Performance-related factors actually stated
- **A stable prompt:** the system prompt does not change midway through a conversation unless you deliberately change it (for example the `/model` command), to preserve the prefix cache.
- **Prompt caching:** there is dedicated code that places cache breakpoints in Anthropic's style.
- **Switching providers costs more:** the provider fallback documentation notes that switching to another provider loses the cache, so the next turn rereads the whole history at the full input price.
- **Memory frozen per session:** memory notes are loaded once at the start of a session for the same purpose of preserving the cache.
What the pages I read do not say: latency, throughput, comparisons with other agents. If you need those numbers, measure them on your own machine and tasks.
## Where Hermes Workspace sits
[Setting up Hermes Workspace: a working base for AI agents](thiet-lap-hermes-workspace-nen-lam-viec-cho-ai-agent.html) is a community web app that sits outside. Its README describes the interface and the agent as separate: the UI talks to Hermes Agent over HTTP, with the gateway on port 8642, the dashboard API on 9119 and the interface on port 3000. That means you can upgrade, replace or run the interface on another machine without touching the agent core. In return, the interface depends on Hermes's API endpoints, so it has "capability gates": features whose endpoints are missing on the Hermes side show up as placeholders.
## Extension points for developers
The developer documentation lists many extension points: adding tools, adding model providers, adding platform adapters, memory plugins, tool plugins, lifecycle hooks and a public API for subagents. To embed the agent in your own code, there is a guide on "using Hermes as a Python library".
## Practical advice
- Before optimizing, measure: tokens per task, cache hit rate, time and cost. The dashboard's Analytics board shows tokens and cost by day and by model.
- Avoid switching models mid-session.
- Keep context compact by splitting sessions by job; use `/new` at task boundaries.
For an overview of the agent automation framework, see [Hermes AI Agent: using an agent framework to automate work](hermes-ai-agent-dung-framework-agent-de-tu-dong-hoa-cong-viec.html).
