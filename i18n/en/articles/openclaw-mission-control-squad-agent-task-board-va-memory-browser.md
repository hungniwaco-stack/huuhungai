---
title: Mission Control for OpenClaw: an agent squad, task board and memory
desc: Agent squads, task boards and memory browsers in OpenClaw dashboards: real features, how to build an agent team per the docs and the risks of delegating work.
min: 7
---
QUICK: In this article, "squad", "task board" and "memory browser" are three groups of features often seen in dashboards for OpenClaw. The official counterparts are multi-agent routing, the **Workboard** plugin (a Kanban-style task board, bundled but disabled by default) and OpenClaw's memory system. Understand each layer before combining them.
## Three concepts, three different sources
- **Agent squad:** the official documentation talks about multi-agent routing: boundaries between agents, channel accounts and the "bindings" that route a conversation to a particular agent. Each agent can separate sessions by agent, workspace or sender.
- **Task board:** OpenClaw has an official **Workboard** plugin that adds an optional Kanban-style board to the Control UI, with work cards, assignment to agents and a link back to the run session. It is bundled but disabled by default; enable it with `openclaw plugins enable workboard`. The documentation says Workboard is intentionally small, for the work of one Gateway, and does not replace GitHub Issues, Linear or Jira. Community dashboards have their own boards too, for example `navjotdhanawat/openclaw-mission-control` has five columns (Inbox, Assigned, In Progress, Review, Done), priorities from Low to Urgent and groups work into "missions".
- **Memory browser:** many community dashboards have a memory browser. The OpenClaw documentation index also lists a Knowledge plugin, described as an evidence-backed Markdown vault with an explorer in the Control UI; I have not read that plugin closely. OpenClaw's own memory (structure, search, provenance, deletion) has separate documentation, see [Setting up long-term memory for OpenClaw: when it is needed and how to control it](thiet-lap-bo-nho-dai-han-cho-openclaw-khi-nao-can-va-lam-sao-kiem-soat.html).
For an overview of dashboards and safe access, see [Mission Control for OpenClaw: community dashboards and the official Control UI](openclaw-mission-control-quan-ly-agent-bang-dashboard-truc-quan.html).
## Multi-agent routing in OpenClaw
According to the official documentation index, there are separate pages: Multi-agent routing (agent boundaries, channel accounts, bindings), Agent bindings (routing accounts and conversations to agents), Multi-user mode (session ownership when several people share one agent) and Broadcast groups (bounded group flows across channels). Each page has plenty of configuration detail that I have not read, so this article gives no syntax. Open those pages when you build the team.
One important note from the security page: OpenClaw assumes one trust boundary per Gateway, meaning one operator or one group of people who trust each other, and it is not an adversarial multi-tenant boundary. For users who do not trust each other, the documentation advises separate Gateways, credentials and, ideally, separate operating system users or machines for each party. An agent with a messaging tool can send across conversations and providers by default.
## How to organize a small agent team
1. **Start with one agent that runs well** before adding a second.
2. **Split by clear roles**, for example one agent drafts and one reviews, each with its own tools and permissions (the documentation has pages on tool policy and per-agent profiles).
3. **Hand out work through a single place.** Whether you use Workboard or a community dashboard, use only one task board to avoid double assignment.
4. **Irreversible actions go through a person**: sending messages, merging code, deleting data, spending money.
5. **Measure** time, cost and the number of reworks, using the framework in [Evaluating AI agents through real tests: which criteria to look at](danh-gia-ai-agent-qua-bai-test-thuc-te-nhin-vao-tieu-chi-nao.html).
## Risks to know
- A task board lets you assign work quickly, but it also increases how often agents run and the token cost.
- A community dashboard may have control over agents. The README of the repo I read gives no guidance on protecting the dashboard itself, so do not expose it to the internet.
- An agent that reads outside content (web pages, messages) can be hit by injected instructions; the OpenClaw documentation has a separate page on prompt injection.
## When you need an agent team
When a task is long, multi-step and has a person reviewing in the middle. If it has not reached that level, one agent with good skills is usually enough. For a similar role-design framework on the Hermes side, see [Roles in Hermes Swarm: builder, reviewer and how to coordinate](cac-vai-tro-trong-hermes-swarm-builder-reviewer-va-cach-phoi-hop.html).
