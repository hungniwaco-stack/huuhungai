---
title: Setting up Kanban for Hermes: managing a website-building workflow with AI
desc: Use Hermes's Kanban board to coordinate profiles building a website: tasks, dependencies, review and send-back loops, error handling, with official commands.
min: 9
---
QUICK: Hermes's Kanban is a durable task board stored in `~/.hermes/kanban.db`, with each task assigned to a profile; a dispatcher in the gateway picks up ready tasks and runs workers. For a website-building workflow, you split the work into tasks with dependencies (design, build, test) and add a review loop so the reviewer can send work back when it is not up to standard.
## What Hermes's Kanban is
The documentation describes it as a shared task board for all Hermes profiles. Each task is a row in `~/.hermes/kanban.db`, and each worker runs as its own process with its own profile identity. Unlike `delegate_task` (a blocking function call), Kanban is a queue where every handoff is visible and editable.
The states: `triage`, `todo`, `ready`, `running`, `blocked`, `review`, `done`, `archived`.
## Requirements
- Hermes Agent with at least one profile as a worker. Create profiles following [Hermes AI Course: understanding multi-agent, profiles and fallback chains](hermes-ai-course-hieu-multi-agent-profile-va-fallback-chain.html).
- A running gateway, because the dispatcher is embedded in the gateway by default. Without a gateway, ready tasks will sit waiting.
- Git, if you use worktree folders for coding tasks.
## Minimum setup
```
hermes kanban init
hermes gateway start
hermes kanban create "Build the home page" --assignee builder
hermes kanban watch
hermes kanban list
```
The first `hermes kanban` command also initializes the board automatically. For a drag-and-drop interface, run `hermes dashboard` (port 9119) and open the Kanban tab. For a separate project you can create a separate board: `hermes kanban boards create board-name --name "Display name" --switch`.
## Applying it to a website-building workflow
Suppose there are three profiles: `designer`, `builder` and `reviewer`. A chain of tasks with dependencies, following the pattern in Hermes's guide:
```
DESIGN=$(hermes kanban create "Design the home page layout" --assignee designer --tenant website --json | jq -r .id)
BUILD=$(hermes kanban create "Build the home page from the layout" --assignee builder --tenant website --parent $DESIGN --json | jq -r .id)
hermes kanban create "Test the interface and speed" --assignee reviewer --tenant website --parent $BUILD
```
Only the first task is in the `ready` state, and the later ones stay in `todo` until the parent task is done. The dispatcher runs every 60 seconds by default; the "Nudge dispatcher" button in the interface runs one pass immediately.
Workers do not type `hermes kanban` commands. They use the `kanban_*` toolset that is granted automatically: read the task (`kanban_show`), report progress (`kanban_heartbeat`) and finish with a summary (`kanban_complete`). The parent task's summary and metadata are passed to the child task, so ask workers to write the handoff clearly.
## The review and send-back loop
The guide describes two styles; do not mix them:
- **The same card:** the builder calls `kanban_request_review`, the reviewer calls `kanban_request_changes` to send it back or `kanban_complete` to close it. The run history is recorded as `review_requested`, `changes_requested`, then `completed`.
- **A separate review card:** the review is a child task of the build task; once the builder finishes, the review card runs.
Use `kanban_block` only for genuine external obstacles (missing access, a product decision needed), not for ordinary review comments. For a finished task that later turns up a bug, do not reopen it: create a new child task of it, with new evidence such as the error log.
## Error handling and safety
- **Assigning to a profile that does not exist** fails silently; the dispatcher automatically blocks the task after the set number of failures (default 2). Use `--max-retries` to change it.
- **A worker dies midway:** the dispatcher detects it, reclaims the task and puts it back to `ready` for a new attempt.
- **Concurrency limits:** `kanban.max_in_progress` and `kanban.max_in_progress_per_profile`.
- **One machine:** the documentation says Kanban is designed for a single machine and a trusted local-user model. Do not run the dispatcher in the gateway and a separate process at the same time on the same database, because they will fight over tasks.
- **Exposure to the network:** the dashboard's plugin routes have no authentication when called from localhost; the documentation advises not to open `--host 0.0.0.0` on a shared machine.
- **Temporary folders:** scratch workspaces are deleted when done, keeping only files declared as deliverables.
## Suggestions for adoption
Start with two tasks chained together (build then review) in a test folder. Once it works, add profiles. Measure time, cost and the number of times work is sent back. Publishing to the real site should still be your click, following the principle in [Roles in Hermes Swarm: builder, reviewer and how to coordinate](cac-vai-tro-trong-hermes-swarm-builder-reviewer-va-cach-phoi-hop.html).
