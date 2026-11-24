---
title: Hermes AI Course: understanding multi-agent, profiles and fallback chains
desc: Explains three Hermes concepts: profiles, multi-agent (subagents, Kanban, Bot Mode) and fallback chains, with commands and configuration from the official docs.
min: 8
---
QUICK: A profile is a separate Hermes folder (config, keys, memory, skills). Multi-agent means several profiles or subagents coordinating through subagents, Kanban or Bot Mode. A fallback chain is a list of backup models for when the main model fails. These three are independent, and you can use each separately.
## Profiles: the foundation of everything
According to the documentation, a profile is a separate Hermes folder under `~/.hermes/profiles/`. Each profile has its own: `config.yaml`, `.env` (keys and tokens), `SOUL.md` (personality and instructions), memory, sessions, skills, cron tasks, state database and gateway state.
The main commands:
```
hermes profile create coder
hermes profile create work --clone
hermes profile use coder
hermes -p coder chat
hermes profile delete coder
```
- `create coder` creates an empty profile with bundled skills, inheriting the current API keys and model.
- `--clone` copies config, keys, `SOUL.md`, skills and selected memory; sessions and cron start empty.
- `use` sets the default profile for the following `hermes` commands; `-p` applies to a single command only.
Each profile also gets a shortcut command: if you create the profile `coder`, you type `coder chat` as you would `hermes -p coder chat`.
**An important limit:** a profile is not a sandbox. The documentation states clearly that it does not isolate the agent from the system; on the local backend, the agent has file permissions like your account. `SOUL.md` steers the model but does not impose boundaries. And never let two processes share one profile.
## Multi-agent: three ways to coordinate
**Subagents (`delegate_task`).** The parent hands work to a child with clean context, and the child returns a summary. Suited to short-term parallel work. By default 10 children per batch.
**Kanban.** A durable task board for multiple profiles. Each task has an assignee (a profile name); the dispatcher runs in the gateway, every 60 seconds picks up ready tasks and launches a worker with exactly that profile. Suits long, multi-step work. See [Setting up Kanban for Hermes: managing a website-building workflow with AI](thiet-lap-kanban-cho-hermes-quan-ly-quy-trinh-xay-website-bang-ai.html).
**Bot Mode.** Turns a profile into a named "bot" with its own role, model, memory, skills and avatar, available in the desktop app. Bots can message each other with the `message_agent` tool, or group from two to six bots in one chat room. By default a bot-to-bot exchange is limited to four messages to avoid loops.
The core difference: a subagent is a blocking function call, while Kanban is a task queue where every handoff is visible and editable.
## Fallback chain: model backup
When the main provider fails, Hermes switches to a fallback provider in the middle of a session, keeping the history. Configure it in `~/.hermes/config.yaml`:
```
fallback_providers:
  - provider: openrouter
    model: fallback-model-name
```
Each entry needs both `provider` and `model`. For a self-hosted endpoint, add `base_url` and optionally `key_env`.
Trigger conditions: 429 errors and server errors (500, 502, 503) after retries, authentication errors (401, 403) and not-found errors (404) switch immediately, or empty and repeatedly wrong responses. A characteristic: the fallback only applies for that turn, and the next message returns to the main model; within one turn it triggers at most once.
Manage it with commands:
```
hermes fallback
hermes fallback list
hermes fallback check
hermes fallback check --live
```
`check` statically checks that each entry has a valid key and configuration, and `--live` sends a minimal request for each entry. The command exits with code 1 if any entry is not ready, so it can be used in CI.
**The cost:** switching providers loses the prompt cache, so that turn rereads the whole history at full price. In addition, credential pools rotate several keys of the same provider and are tried before the fallback.
## Putting the three concepts together
A practical way to organize: create a few profiles by role (for example a drafter and a reviewer), each profile pinning a model and having its own fallback, then use Kanban to pass work between them. The decisions you must make yourself are which role uses a cheap model, which needs a strong model, and which tasks pause for a reviewer.
## Common mistakes
- Using many agents when one is enough. Start with one profile.
- Turning on a cloud fallback for sensitive data, which makes data leave the machine (see [Ollama and Hermes: when does a local AI agent beat the cloud?](ollama-va-hermes-khi-nao-local-ai-agent-tot-hon-cloud.html)).
- Letting two gateways share one bot token: the documentation says the second gateway is blocked.
For coordination by role, see also [Roles in Hermes Swarm: builder, reviewer and how to coordinate](cac-vai-tro-trong-hermes-swarm-builder-reviewer-va-cach-phoi-hop.html).
