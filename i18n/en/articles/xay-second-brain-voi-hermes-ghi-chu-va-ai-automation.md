---
title: Building a second brain with Hermes, notes and AI Automation
desc: Build a second brain with Hermes Agent: the MEMORY.md and USER.md memory, finding old sessions, the Obsidian skill, limits and how to keep notes trustworthy.
min: 7
---
QUICK: Hermes has two layers of "remembering": the agent's short notes (`MEMORY.md`, `USER.md`) with character limits, and finding whole old sessions with `session_search`. Your long note library should live somewhere separate, such as Obsidian, with the agent reading and writing through the `obsidian` skill. Do not expect the built-in memory to replace a second brain.
## How a second brain and the agent's memory differ
A second brain is your knowledge store: notes, documents and ideas, usually long and structured. The agent's memory is compact and only holds what the agent needs to know to work well with you. Mixing these two up is why many people are disappointed. A sensible way: the note library is the source of truth, and the agent's memory holds only instructions and preferences.
## Layer 1: Hermes's short memory
According to the memory documentation:
- `MEMORY.md` holds the agent's notes: facts about the environment, conventions, lessons. Limited to 2,200 characters.
- `USER.md` holds a profile of you: preferences and communication style. Limited to 1,375 characters.
- Both live in `~/.hermes/memories/`. If you exceed the limit the tool reports an error and the agent must condense.
- Memory is loaded into the prompt **once at the start of a session** (a frozen snapshot) to keep the cache. What the agent writes during a session is saved immediately but only shows up in the next session.
- The memory tool has three operations: add, patch a single passage, delete. There is no separate read operation.
- Content is scanned: prompt injection patterns, credential theft, SSH backdoors and hidden characters are blocked.
What to save: preferences, facts about the environment, your corrections, project conventions, and requests like "remember this". What to skip: easily looked-up facts, raw data, and things that only matter within one session.
You can turn on write approval: `/memory approval on` to approve each entry before it is saved, with the commands `/memory pending`, `approve` and `reject`.
## Layer 2: finding old sessions
`session_search` searches the CLI and messaging sessions stored in `~/.hermes/state.db` using FTS5 full-text search. It returns the original messages directly, without summarizing and without using a model call. Suited to questions like "how did we discuss X last week".
## Layer 3: a real note library, for example Obsidian
The bundled skill catalog has `obsidian` with the description "read, search, create and edit notes in an Obsidian vault", preinstalled into `~/.hermes/skills/`. If it is missing it can be restored with `hermes skills reset obsidian --restore`. There is also `apple-notes` (macOS, needs the memo command-line tool) and `grounded-citations`, which helps attach verifiable sources to answers. The catalog has no ready-made Notion or shared wiki skill.
A suggested workflow:
1. Choose **one** vault folder as the source of truth and write its path into `MEMORY.md`.
2. Set conventions in the agent's notes: which folder is used for what, how to name things, when editing is allowed.
3. Let the agent work **in read-only mode** for the first few weeks: summarizing, finding links, suggesting.
4. Allow writing only to a separate "inbox" folder. You review and then move items into the main vault.
5. Back up the vault with Git or an offline copy before letting the agent edit.
## Limits to know
- **Frozen per session:** what was just saved is not visible in the running session.
- **No automatic tidying:** when memory is full, the agent must condense it by hand.
- **Per profile:** a different profile has a different memory store.
- **Weak models:** a small model running locally may say it saved something when it did not actually call the tool. Check by looking at the file.
- **Approval covers only two tools:** the memory tool and skills. The file and terminal tools can still edit directly, so set folder permissions carefully.
- **External memory:** there are external memory providers such as Honcho and Mem0 through plugins; I have not read them closely so I do not assess them here.
## Automation around a second brain
Once the foundation is steady, you can use scheduled tasks to summarize new notes each morning, or a messaging bot to capture ideas quickly from your phone (see [Hermes AI Agent: using an agent framework to automate work](hermes-ai-agent-dung-framework-agent-de-tu-dong-hoa-cong-viec.html)). The same idea using Claude is in [Claude and Obsidian: a plugin or Claude Code for your notes system?](claude-va-obsidian-chon-plugin-hay-claude-code-cho-he-ghi-chu.html).
## Privacy
Personal notes are sensitive data. If you use a cloud model, the content the agent reads is sent to the provider. Consider a local model for a private vault, see [Hermes and Gemma: a local AI agent stack for private data](hermes-va-gemma-stack-ai-agent-local-cho-du-lieu-rieng-tu.html).
