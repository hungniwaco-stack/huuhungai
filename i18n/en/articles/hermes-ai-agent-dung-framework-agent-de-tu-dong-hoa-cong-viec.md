---
title: Hermes AI Agent: using an agent framework to automate work
desc: Use Hermes Agent to automate work: cron, messaging bots, subagents, the Kanban board and safety rules. Choose the right tool for each kind of job.
min: 7
---
QUICK: Hermes gives you four building blocks for automation: scheduled tasks (cron), messaging bots, subagents that run in parallel and a Kanban board that coordinates several profiles. Start with one small, repeatable, easy-to-verify task, then expand. Do not automate work you have not mastered doing by hand.
## How an agent differs from a script and a workflow
A script does exactly the steps you write. A workflow tool connects fixed steps. An agent like Hermes takes a goal, then chooses tools, reads results and adjusts. In exchange, results are less predictable and use more tokens. The rule for choosing: work with a fixed process that rarely changes uses a script; work that needs reading, synthesis and small decisions uses an agent; work that cannot tolerate mistakes needs an added human review step.
## The four main blocks
**1. Scheduled tasks (cron).** According to the architecture documentation, a cron task is an agent task: at the set time, the scheduler creates a fresh agent with no history, loads the attached skills, runs it and sends the result to a destination platform such as Telegram. Suited to morning reports, periodic checks and news summaries. Because the agent starts from empty, the task's prompt must carry enough context.
**2. Messaging bots (gateway).** A long-running process connects the agent to more than 25 platforms such as Telegram, Discord, Slack, WhatsApp, Signal and email. Set up with `hermes gateway setup`, check with `hermes gateway status`. Remember to limit the list of people allowed to message it, because the bot has real permissions on the machine.
**3. Subagents (`delegate_task`).** Creates child agents with clean context that run in parallel for independent work such as researching several sources or reading many files. By default up to 10 subagents per batch, one level deep, at most 250 iterations each. Only the final summary returns to the parent. A subagent cannot ask you questions.
**4. The Kanban board.** A durable work queue on SQLite, with each task assigned to a profile (see [Setting up Kanban for Hermes](thiet-lap-kanban-cho-hermes-quan-ly-quy-trinh-xay-website-bang-ai.html)). Suited to work that is long, multi-step and needs tracking and retries.
## Which to choose
- Work that repeats on a schedule: cron.
- You want to give commands from your phone: gateway.
- One big job split into several independent parts, needing results now: subagents.
- Many sequential tasks, with a person reviewing, running for hours: Kanban.
## A safe adoption workflow
1. **Pick one small task.** For example summarizing the inbox in the morning, checking broken links, preparing a draft report.
2. **Do it by hand a few times**, and write down the criteria for "correct".
3. **Give it to the agent in read-only mode**, and compare with the manual version.
4. **Add write permission step by step.** Posting, sending, deleting and payments still go through you.
5. **Measure** accuracy, time, cost and the number of interventions, using the framework in [Evaluating AI agents through real tests](danh-gia-ai-agent-qua-bai-test-thuc-te-nhin-vao-tieu-chi-nao.html).
6. **Review periodically**, because models and tools change.
## Security and control
- Hermes has an approval mode for dangerous commands and several terminal backends, including Docker. For agents that run automatically, consider running in Docker to limit file scope. The profile documentation states clearly that a profile is not a sandbox: on the local backend, the agent has the same file permissions as your account.
- Keep API keys in `~/.hermes/.env`, not in prompts or the code repository.
- With small models run locally, check carefully because they may say they did something without calling a tool; the memory documentation warns about this too.
## Cost
An agent runs many steps with many tools, so tokens rise quickly, especially with subagents. Set a limit on the provider account and watch the Analytics board. If you need to reduce cost, see the local option in [Ollama and Hermes: when local beats cloud](ollama-va-hermes-khi-nao-local-ai-agent-tot-hon-cloud.html).
## Where to start
Installation and the first conversation: [Installing Hermes Agent simply: a guide for non-technical people](cai-hermes-agent-don-gian-huong-dan-cho-nguoi-khong-chuyen-ky-thuat.html). Once a single task runs well, then consider multiple agents, see [Hermes AI course: understanding multi-agent, profiles and fallback chains](hermes-ai-course-hieu-multi-agent-profile-va-fallback-chain.html).
