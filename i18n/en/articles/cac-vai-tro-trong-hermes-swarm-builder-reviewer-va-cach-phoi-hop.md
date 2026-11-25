---
title: Roles in Hermes Swarm: builder, reviewer and how to coordinate
desc: Roles in Hermes Workspace's Swarm mode: orchestrator, builder, reviewer, QA, handoff by checkpoint and why a human reviewer is needed.
min: 7
---
QUICK: In this article, "Swarm" is the name of a mode in Hermes Workspace, a community project. The official Hermes Agent also has a `hermes kanban swarm` command on its Kanban board, which is a different feature. The core ideas work anywhere: separate the person who does from the person who reviews, give each role clear limits, hand off with structured reports, and send irreversible work through a reviewer.
## Where "Swarm" comes from
The official Hermes Agent documentation describes ways to coordinate several agents: subagents (`delegate_task`), a Kanban board shared between profiles and Bot Mode. The Kanban documentation also has a "Kanban Swarm" helper: the `hermes kanban swarm` command creates in one step a graph with a completed root card that serves as a shared blackboard, several worker cards running in parallel, a verifier card that waits for all workers and a synthesizer card that waits for the verifier. The Swarm mode this article describes is a different feature, from [Setting up Hermes Workspace: a working base for AI agents](thiet-lap-hermes-workspace-nen-lam-viec-cho-ai-agent.html), a web interface written by the community (repo `outsourc-e/hermes-workspace`, MIT license), not a Nous Research product. This article describes exactly what that project's documentation says, then draws out principles that also apply to the official way of working.
## The roles available
The project's `docs/swarm/ROLES.md` document lists 11 roles (presets) when adding a worker:
- **Orchestrator:** coordinates. Splits tasks among workers, writes the dispatch brief, reads workers' reports, spots drift and escalates when blocked.
- **Builder:** makes the product. Interface, backend, bug fixes, small features. The rule states plainly to submit narrow changes and avoid broad edits beyond the request.
- **Reviewer:** reviews. Checks PR readiness, naming, tests and the build. Returns only one of three verdicts: `APPROVED`, `CHANGES_REQUESTED` or `BLOCKED`.
- **Triage:** handles the PR and issue queue, records how to reproduce and writes minimal tests. Does not merge or close on its own, only prepares and asks for approval.
- **QA:** regression testing, comparing expected with actual results, and reporting what was checked, where it broke and how to reproduce it.
- **Scribe, Sage, Lab, Foundation, Mirror Integrations:** documentation and notes, research, local model experiments, infrastructure and integrations.
- **Custom:** a role you define yourself, with no default skills.
Each role has its own specification, which the documentation calls the source of truth for standing duties. A new role needs a specialty, mission, skills and default model, a specification, and a trial task with a reported result.
## Handoff by checkpoint
Workers do not report freely. The documentation describes reports as labeled fields, for example handoff status, result and next steps, with a `NEEDS_REVIEW` status when a person needs to look. The benefit is very practical: the orchestrator can read it by machine, and you can skim it and still know where the work stands.
## The human approval gate
The Swarm quickstart document sets a clear boundary: workers may prepare commits, branches, PR content, review verdicts, issues and release notes. Workers must not merge, force-push, publish, announce publicly, close issues or delete files without explicit human agreement. The project calls this boundary the Greenlight Gate.
## Doing the same with official features
You do not need Workspace to apply this model. Hermes's official Kanban board already has an equivalent flow: the builder calls `kanban_request_review`, the reviewer calls `kanban_request_changes` to send it back or `kanban_complete` to close it, and the history of rounds is recorded. For how to build that workflow, see [Setting up Kanban for Hermes: managing a website-building workflow with AI](thiet-lap-kanban-cho-hermes-quan-ly-quy-trinh-xay-website-bang-ai.html).
## Principles for designing roles
- **One task, one owner.** Two workers editing the same file will step on each other.
- **The doer does not review their own work.** The reviewer should be a different worker, ideally a different model or configuration so the same mistakes are not repeated.
- **Limits in writing.** State what a role may and may not do right in the role's instructions.
- **Irreversible work gets a person.** Merging code, publishing, deleting data, spending money: always through you.
- **Start small.** Two roles (builder and reviewer) are enough to see the value. Eleven roles is too early for most users.
## Risks to know
Several agents running in parallel raise cost with the number of workers, and one worker's error can spread to others if the handoff is loose. Hermes's subagent documentation also notes that subagents can consume most of a run's tokens. Measure cost and quality each week instead of adding roles by feel, see the measurement framework in [Evaluating AI agents through real tests: which criteria to look at](danh-gia-ai-agent-qua-bai-test-thuc-te-nhin-vao-tieu-chi-nao.html). The specific way to install Swarm mode is in [Setting up an agent swarm in Hermes Workspace step by step](thiet-lap-agent-swarm-trong-hermes-workspace-tung-buoc.html).
