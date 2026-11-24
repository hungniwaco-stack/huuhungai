---
title: Kimi Agent Swarm: when should you use many agents at once?
desc: Moonshot AI's Kimi Agent Swarm: how it works, the published limits, work suited to parallel runs, high credit cost and how to verify the speed figures yourself.
min: 7
---
QUICK: Moonshot AI's Agent Swarm lets a main agent create and coordinate many subagents that run in parallel and then merge the results. It suits big work that can be split up, such as bulk information gathering. Kimi's help page says the feature is in Beta, costs several times the credits of a normal agent task, and the speed figures are published by Moonshot itself.
## What Agent Swarm is
According to Kimi's help page, Agent Swarm is Moonshot AI's "scale-out" architecture: it coordinates many subagents without predefined roles or a hand-designed workflow. A main agent creates and directs subagents that work in parallel and then merges the results; the page describes this as a "self-designed organization", with the AI itself deciding when to parallelize and how to assign work. The feature carries a [Beta] label.
## How to use it
- **Web:** go to `kimi.com/agent-swarm`.
- **Mobile and tablet:** open the Kimi app and choose the K3 Swarm model on the model switch above the chat box.
- Describe the task clearly and send it. Follow progress in real time (task list, subagent creation, reasoning, tool calls, pages visited). When done, preview, download or share the result (it can be a code project, a folder of intermediate files, data analysis, a Word document, PDF, Markdown or PPT).
- Eligibility: the page says it is for members of the Moderato, Allegretto and Allegro plans.
## Published limits
According to the help page (the K2.6 upgrade): up to 300 subagents at the same time, more than 4,000 tool calls in one task, and parallel flows up to 4,000 steps. The model names on the page are K2.5 (launched Jan 27, 2026, when Agent Swarm appeared), K2.6 (released and open-sourced Apr 20, 2026) and the page says Agent Swarm now runs on K3 (K3 Swarm). Third-party sources give different subagent ceilings for each version (100 versus 300), so do not rely on one figure when planning.
## The performance numbers, and who published them
These are claims by Moonshot AI on its own page, not independently verified:
- 4.5 times faster than running sequentially with a single agent.
- A reduction of at least 3 to 4.5 times in critical steps in large-scale search.
- On the BrowseComp test, accuracy rises from 15.9% (one agent) to 33.3%.
The page explains that "critical steps" are the time of the slowest subagent at each stage, added up across stages. Treat these as vendor claims and measure on your own work.
## Which work suits a swarm
The page lists: large-scale information retrieval, bulk downloads, reading more than 100 documents, writing more than 100,000 Chinese characters, complex coding (interfaces, code review, multi-file refactoring) and office automation. The page has no section on when **not** to use it. General reasoning (not from the page): work with tightly dependent steps, or work that needs one unified line of reasoning, benefits little from parallelization; test before you trust it.
## Cost
The page says Agent Swarm tasks use relatively many credits, about several times a normal agent task, depending on complexity and the number of subagents. Try small work first to learn the burn rate.
## Data and privacy
The page has no note on data or privacy and only points to the Terms and Policy in the footer. Read them before putting in sensitive documents.
## How to decide whether to use many agents
1. Can the work be split into independent parts?
2. Is a cost several times higher worth the time saved?
3. Can each subagent's result be checked?
4. Have you tried the single-agent version on the same task?
For how to think about roles and handoff when using many agents in another system, see [Roles in Hermes Swarm: builder, reviewer and how to coordinate](cac-vai-tro-trong-hermes-swarm-builder-reviewer-va-cach-phoi-hop.html); to use Kimi through OpenClaw see [OpenClaw and Kimi: configuring Moonshot, Kimi Coding and Ollama Cloud](openclaw-va-kimi-dung-agent-stack-voi-mo-hinh-mo.html); for a measurement framework see [Evaluating AI agents through real tests: which criteria to look at](danh-gia-ai-agent-qua-bai-test-thuc-te-nhin-vao-tieu-chi-nao.html).
