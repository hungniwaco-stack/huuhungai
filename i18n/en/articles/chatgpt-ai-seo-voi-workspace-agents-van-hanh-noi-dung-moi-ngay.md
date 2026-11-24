---
title: ChatGPT AI SEO with Workspace Agents: running content day to day
desc: Design a workspace agent in ChatGPT for repetitive content work: how to create it, schedules, skills, approval before writes and why an editor is still needed.
min: 8
---
QUICK: A workspace agent in ChatGPT (for Business, Enterprise, Edu) can run on a schedule, use connected apps and skills you add. Use it for the repetitive part of the content workflow (gathering, outlining, checking) and let a person approve the write actions. Google treats creating many pages only to manipulate rankings as spam, even when AI does it.
## What a workspace agent is
According to OpenAI's cookbook on learn.chatgpt.com, a workspace agent is an agent you build once to run a repeating workflow from start to finish: read from connected apps, do the work, then send the result. It requires a ChatGPT Business, Enterprise or Edu workspace with access to workspace agents. By default a new agent is only for you until you share it.
For SEO content, Google's policy against manipulation and how to set review gates are already discussed in [An AI SEO system with Claude: automate content but still edit it](he-thong-ai-seo-voi-claude-tu-dong-hoa-noi-dung-nhung-van-can-bien-tap.html); this article only covers the ChatGPT tooling side.
## How to build an agent (following OpenAI's example)
The cookbook walks through building an agent that prepares for sales meetings. The steps, usable as a template for other work:
1. **Open the builder:** go to Agents, Create, Create agent. To start from a template, choose Browse templates.
2. **Describe the workflow:** enter a prompt, look at the plan, choose "Build this agent" and check that the draft includes the right apps.
3. **Configure the apps:** for each app choose the account type. "End-user account" means each person connects their own account; "Agent-owned account" uses one shared service account. Turn on only the actions you need (for example read-only).
4. **Add skills:** upload an existing skill (following the open agent skills standard) or use the built-in skill builder, so the workflow is consistent.
5. **Turn on Memory:** give the agent a persistent folder to store notes and outputs, kept separate for each user.
6. **Preview and publish:** test in Preview, choose Create to publish, and Update to publish later changes.
## Running on a schedule
In the published agent, choose Automations, choose the ChatGPT channel, set the time (for example weekdays at 16:00), enter the instructions and choose "Add automation". Scheduled runs use the published version and run on behalf of the person who created the schedule.
## Approval and safety
- By default the agent **asks before taking write actions**; approval is configured separately from turning on the action.
- Turn off actions for sharing, deleting and unrelated writes.
- Check file creation and email sending before trusting scheduled sending, and watch the first scheduled run closely.
- If you use a shared service account, anyone who can run the agent can use the actions enabled through that account; check what content that account can access.
- A workspace's policy may block reading the calendar, creating files or sending email; when writing is restricted, the agent may return a summary right in ChatGPT.
## Applying it to daily content operations
Following the prompt structure in the example (schedule and filter, the work for each item, how to send the results), a content workflow could include:
1. **Schedule:** each morning check the list of approved topics.
2. **Each topic:** gather the specified sources, make an outline and a rough draft saved to a shared folder.
3. **Send the result:** a summary email with links to the drafts.
I am inferring this pattern from the sales meeting example; OpenAI gives no SEO example. Treat this as a design suggestion, not a documented feature.
## Boundaries to keep
- The agent drafts and runs technical checks; **a person decides topics, adds real experience, verifies facts and clicks publish**.
- Do not let the agent publish to the site or send outward on its own.
- Do not write many near-identical pages that only change the keyword. Use the time saved to make fewer articles but more carefully.
- Record the source for every claim and have a person recheck.
## Measuring effectiveness
Track the number of articles that pass the review gate, the time the editor spends per article, the number of factual errors caught, and articles indexed in Search Console. For the general framework, see [Evaluating AI agents through real tests: which criteria to look at](danh-gia-ai-agent-qua-bai-test-thuc-te-nhin-vao-tieu-chi-nao.html). For working with several agents and sharing within a team, see [Workspace Agents in ChatGPT: sharing and handing off work to teammates](workspace-agents-trong-chatgpt-handoff-tac-vu-giua-nhieu-agent.html).
