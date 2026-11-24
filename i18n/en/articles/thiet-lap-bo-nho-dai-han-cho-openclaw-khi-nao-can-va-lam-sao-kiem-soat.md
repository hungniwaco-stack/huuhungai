---
title: Setting up long-term memory for OpenClaw: when it is needed and how to control it
desc: OpenClaw long-term memory per the official docs: MEMORY.md and USER.md, lookup, dreaming, management commands, per-session deletion and the limits to know.
min: 8
---
QUICK: OpenClaw stores memory as plain Markdown files in the agent's workspace, and the model only remembers what is written to disk. There are core files (`MEMORY.md`, `USER.md`), daily notes, semantic lookup and a background "dreaming" process that automatically promotes eligible entries into core memory. Control it with `openclaw memory ...`, and remember that memory does not replace the approval mechanism.
## How OpenClaw's memory works
The documentation states plainly: the model only remembers what is saved to disk, with no hidden state. By default the files live in `~/.openclaw/workspace`.
- **`USER.md`** (optional): stable preferences, communication style, the project context you are working on, written as instructions. Loaded at session start, with its own small budget.
- **`MEMORY.md`**: long-term facts and decisions, not a personal profile. Loaded at session start.
- **`memory/YYYY-MM-DD.md`**: daily notes and raw context. Today's and yesterday's notes are loaded when you type a bare `/new` or `/reset`. Searchable but not included in every turn.
- **`DREAMS.md`** (optional): a "dreaming" journal for people to review.
When you ask the agent to remember something, it writes to the appropriate file. Before context compaction, a silent "flush" turn reminds the agent to save important context, appending only the new part to the daily note. Memory imported from Codex, Claude Code and Hermes (Control UI, Settings, Import Memory) goes to `memory/imports/<source>/` and is not merged into `MEMORY.md` automatically.
## The memory tiers
The architecture page divides it into five tiers:
- **Instructions:** `AGENTS.md` and instruction files, always loaded, written only by people.
- **Curated core:** `MEMORY.md`, `USER.md`, loaded at session start if the provenance is eligible, with a budget.
- **Episodic:** daily notes and session transcripts, included only when recalled.
- **Prospective:** standing intents and scheduled tasks, run only when triggered.
- **Review:** `DREAMS.md`, never loaded, meant for people to read.
Each memory entry carries provenance (`owner`, `agent`, `untrusted`, `system`). Content of unknown origin is treated as `untrusted` or `system`, never as `owner`. Cron tasks, heartbeats and subagents do not create long-term memory candidates.
## Lookup
The tools of the default memory plugin (`memory-core`): `memory_search` (semantic search, even when the words differ), `memory_get` (read a file or a range of lines) and `intent` (episodic intents). Search combines vector and keyword search and uses OpenAI embeddings by default. If you only want keyword search, set `memory.search.provider: "none"`. Remember that sending content to an embedding provider means sending data out; the documentation does not state exactly what they receive.
## Dreaming: self-consolidating memory
Dreaming is on by default and runs in the background in three phases: Light, REM and Deep. Only the Deep phase promotes entries into `MEMORY.md`, through two gates: a check using weighted rules (excluding `untrusted` and `system` candidates before scoring), then a bounded model turn to merge, replace and remove duplicates. Each write saves the previous original and writes a summary to `DREAMS.md`. Turn it off with `plugins.entries.memory-core.config.dreaming.enabled: false`; turn off the pre-compaction flush with `agents.defaults.compaction.memoryFlush.enabled: false`.
## Management commands
```
openclaw memory status
openclaw memory search "keyword"
openclaw memory index --force
openclaw memory reset
openclaw doctor
```
`memory reset` deletes derived data and keeps the memory files intact; run `openclaw memory index` to rebuild. Check whether a part of `MEMORY.md` is cut for exceeding the budget with `/context list` or `/context detail`.
## Deleting and controlling the source
To delete memory generated from a session:
```
openclaw sessions --agent <agent-id> --limit all --json
openclaw memory forget --agent <agent-id> --session <id-or-key> --dry-run --json
openclaw memory forget --agent <agent-id> --session <id-or-key> --json
```
The first command lists sessions, the second only previews (deleting nothing), and the third deletes at once without asking for confirmation. You can exclude a source from future loading with `memoryPolicy.excludeSessions`, for example excluding sessions from a Gmail hook. Note the limits:
- `forget` does not delete the original session transcript, only memory entries that can be traced back through provenance.
- Hand-written notes, or notes from before provenance tracking, may not be found this way.
- An entry merged from several sessions is deleted whole, even if you chose only one session.
- Copies elsewhere (backups, exports, other plugins' stores) are outside the scope of cleanup.
- An empty preview does not prove that no related information remains.
## Important limits
- If `MEMORY.md` exceeds the budget, the file on disk stays intact but the version put into context is truncated.
- Automatic lookup has a one-second preparation budget; if time runs out, the reply continues without that candidate.
- Sessions are indexed asynchronously, so a turn that just finished can only be found after a short while.
- A session running in a sandbox without workspace write permission skips the flush.
- **Memory does not enforce policy.** For hard control, use approvals, sandboxes and scheduled tasks.
## When it is needed and when it is not
It is needed when the agent must remember preferences, project conventions and decisions across many sessions. It is not needed when you only use the agent for one-off work. Treat `MEMORY.md` as a document you can read and edit: open it periodically and delete wrong or outdated entries. For a comparison with the Hermes approach, see [Building a second brain with Hermes, notes and AI Automation](xay-second-brain-voi-hermes-ghi-chu-va-ai-automation.html). For an external memory plugin such as ByteRover, see [OpenClaw and ByteRover: upgrading long-term memory for agents](openclaw-va-byterover-nang-cap-bo-nho-dai-han-cho-agent.html).
