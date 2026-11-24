---
title: Workspace Agents in ChatGPT: sharing and handing off work to teammates
desc: Share and hand off work with ChatGPT workspace agents: chat and edit permissions, team folders, Slack, account types and what the docs omit on multi-agent.
min: 7
---
QUICK: The OpenAI documentation I could read describes how to **share and hand off an agent to people** ("Can chat" and "Can edit" permissions, team folders, Slack, personal or shared accounts), but it does not describe a mechanism for one agent to delegate work directly to another. So "handoff between multiple agents" should be understood as handoff through people, through memory and through output products, with human checkpoints.
## What I found, and what I did not
I read OpenAI's workspace agent cookbook on learn.chatgpt.com. It covers building an agent, running it on a schedule, sharing and approvals. I found no page describing this agent calling another agent or automatically handing tasks off between agents. OpenAI's help pages and launch announcements returned a 403 error when I loaded them, so that information may be there and I could not read it. This article only covers what I read.
## Sharing an agent with teammates
In the builder, choose **Share**. Admins control whether users can share.
- **Can chat:** teammates can run the agent.
- **Can edit:** teammates can update the draft and publish versions.
- An eligible managed workspace can grant permission to a group.
- People with build permission can duplicate the agent.
- If posting to a directory is allowed, the agent can appear in Agents, Team directory.
- Each teammate connects their own Google Calendar and Gmail and creates their own run schedule.
## Two account types when handing off
For each app you choose how to authenticate:
- **End-user account:** each person connects their own account and the agent only sees what that person sees. Safer for wide sharing.
- **Agent account (shared):** one service account, and whoever runs the agent can use the actions enabled through that account. The cookbook warns you to check what content this account can access.
Slack needs shared authentication for all app connections, so OpenAI's example uses a ChatGPT channel so each user uses their own account. Enabling Slack is also configured by admins, and the ChatGPT Agents app in Slack has its own help page that I could not read.
## Handoff through memory and output products
An agent can turn on **Memory**, a persistent folder for notes and outputs, kept separate for each user. In the example, the agent saves a summary into the team's SharePoint folder and then emails a link. This pattern is a practical way to hand off: agent A writes its product to one place, and a person or another agent reads from there. It is a working method, not a feature for calling agents directly.
## Keeping people in the loop
- By default an agent asks before taking write actions; approval is configured separately from the enabled action.
- Schedules use the published version and run on behalf of the person who created the schedule.
- Test with your own account before sharing, compare the output with what a person would produce and add a sample to the skill's files.
## If you need several agents to coordinate
Design it like a process with clear handover points: one job per agent, outputs written to a shared place, and a person reviewing at irreversible points (sending, deleting, publishing). For role and structured-handoff ideas in another system, see [Roles in Hermes Swarm](cac-vai-tro-trong-hermes-swarm-builder-reviewer-va-cach-phoi-hop.html) and [Hermes Kanban](thiet-lap-kanban-cho-hermes-quan-ly-quy-trinh-xay-website-bang-ai.html). For designing one agent for content work, see [ChatGPT AI SEO with Workspace Agents](chatgpt-ai-seo-voi-workspace-agents-van-hanh-noi-dung-moi-ngay.html).
