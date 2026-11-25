---
title: Setting up an agent swarm in Hermes Workspace step by step
desc: Set up Swarm Mode in Hermes Workspace step by step: requirements (Node, pnpm, tmux), adding workers from presets, a first API dispatch, checks and fixes.
min: 7
---
QUICK: Swarm Mode is a feature of Hermes Workspace (a community project) for running several persistent Hermes workers through tmux, each worker with one profile and one role. It needs Node.js 22, pnpm, git, tmux and at least one Hermes profile. You add workers from presets, dispatch work through the interface or the API, and workers send checkpoints back to the Reports section.
## Before you start
The Swarm Mode in this article is not part of the official Hermes Agent (Hermes has its own helper, the `hermes kanban swarm` command on the Kanban board). It lives in [Setting up Hermes Workspace: a working base for AI agents](thiet-lap-hermes-workspace-nen-lam-viec-cho-ai-agent.html), a community web interface (repo `outsourc-e/hermes-workspace`, MIT license). Install and run Workspace normally first, then turn on Swarm. For an explanation of the roles, see [Roles in Hermes Swarm: builder, reviewer and how to coordinate](cac-vai-tro-trong-hermes-swarm-builder-reviewer-va-cach-phoi-hop.html).
## Requirements per the Swarm Quickstart
- Node.js 22 or later.
- pnpm and git.
- tmux, recommended. Workspace still displays if tmux is missing, but a worker's session will run once and then be dropped, not persistent.
- At least one Hermes Agent profile configured under `~/.hermes/profiles/`.
## Step 1: install and run Workspace
```
git clone https://github.com/outsourc-e/hermes-workspace.git
cd hermes-workspace
pnpm install
pnpm dev
```
Open the address printed in the terminal, usually `http://localhost:3000` (some versions use port 3002, so follow the terminal). For Workspace to connect to Hermes Agent, you need the gateway running with the API server enabled; details are in [Setting up Hermes Workspace: a working base for AI agents](thiet-lap-hermes-workspace-nen-lam-viec-cho-ai-agent.html).
## Step 2: prepare profiles for workers
On the first run, Workspace scans `~/.hermes/profiles/`. Each worker has a folder named by the worker id, which may contain `MEMORY.md`, `SOUL.md`, `USER.md`, `memory/IDENTITY.md`, `runtime.json` and a `skills/` folder. A worker that is in the list but has no matching profile is shown as "roster-only", and you must create or import a profile before expecting memory, skill loading or a tmux launch.
## Step 3: add workers
1. Open Swarm Mode and choose Add Swarm.
2. Choose a role preset: Orchestrator, Builder, Reviewer, Triage, Lab, Sage, Scribe, Foundation, QA, Mirror Integrations or Custom. A preset pre-fills the role, specialty, mission, system prompt, skills and default model.
3. Set the worker id, display name, model, specialty, mission and skills.
4. Save, then start the session from the worker card or from the Runtime view.
The documentation advises choosing a close preset instead of Custom, unless you deliberately create a new lane. Starting with two workers (Builder and Reviewer) is enough to try it.
## Step 4: dispatch the first task
Use the `POST /api/swarm-dispatch` endpoint. An example from the documentation, dispatching a task that does not edit files:
```
curl -X POST http://localhost:3000/api/swarm-dispatch -H 'Content-Type: application/json' -d '{"workerIds":["swarm7"],"prompt":"Write a short checkpoint explaining what you can see in your current workspace. Do not modify files.","timeoutSeconds":240,"waitForCheckpoint":true}'
```
Replace `swarm7` with your worker id. A successful response has a `missionId`, a list of dispatches and each worker's result with its status (for example `delivery` is `tmux`, `checkpointStatus` is `checkpointed`).
## Step 5: check
- The worker appears in the list.
- The profile exists at `~/.hermes/profiles/<worker id>/`.
- Runtime mode can attach to tmux or open a shell, or a log stream.
- The `tmux ls` command shows a session named `swarm-<worker id>`.
- A checkpoint appears in the Reports section after a refresh.
## Fixing errors per the documentation
- **The card exists but the TUI will not attach:** run `tmux ls`; if `swarm-<worker id>` is missing, restart or cycle the worker.
- **A dispatch reports a timeout:** it only means no new checkpoint arrived in time, not necessarily a failure. Check Runtime, the `runtime.json` file, the chat transcript and Reports before retrying.
- **Wrong role, model or skills:** fix the configuration and restart the session; do not change it while work is in progress.
## Safety boundaries
The documentation states clearly that workers may prepare commits, branches, PR content, review conclusions and release notes, but must not merge, force push, publish, announce publicly, close issues or delete files without someone's agreement. Keep to this principle, and put each worker in its own working folder so they do not step on each other.
## Cost and expectations
Each worker is an agent running separately, so token cost rises with the number of workers. Hand out small tasks with checkable results, measure time and cost, and only then increase the number.
