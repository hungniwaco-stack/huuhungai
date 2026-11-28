---
title: OMI and Obsidian for entrepreneurs: building an AI work-memory system
desc: Connect an Omi wearable to Obsidian through the community plugin obsidian-omi: requirements, install, how conversations sync, file structure and privacy.
min: 7
---
QUICK: Omi is an open-source AI wearable platform that records and transcribes conversations into queryable memories. Omi's official documentation does not mention Obsidian; syncing into Obsidian comes from community plugins such as `obsidian-omi`. Because recording other people may violate privacy and local regulations, ask for consent and control the data before using it for work.
## What Omi is
According to Omi's documentation, it is an open-source AI wearable platform: "a necklace that records conversations, transcribes them and turns them into memories you can query". There is the Omi device (CV1) and the self-built omiGlass smart glasses. The Omi app can also be used without a device, recording from a phone or the Mac app to capture meetings and screen context. The system transcribes in real time, identifies speakers, then extracts memories, action items and summaries. There is a REST API for memories, conversations and action items. The documentation page gives no information about data or privacy, and does not mention Obsidian.
## The bridge to Obsidian: a community plugin
There are several community projects connecting Omi with Obsidian. One example is `obsidian-omi` (repo `smian1/obsidian-omi`). Its README says MIT, but the LICENSE file in the repo is the 0BSD text, and the last code push was Dec 31, 2025 (checked Nov 28, 2026). Per its README:
- It syncs Omi's conversations, action items and memories into Obsidian as searchable Markdown files, with Dataview-compatible metadata.
- A conversation file can include an AI summary, action items, events and the transcript.
- There is an "Omi Hub" (a dashboard) and a "Tasks Hub" with two-way sync for action items, plus daily notes that automatically link to conversations.
The README does not state the required Obsidian version, maintenance status or privacy notes. Other similar projects may have different features; read each repo's README before installing.
## Requirements and installation (per the obsidian-omi README)
- An Omi account and the Omi app, to create a developer API key at Settings, Developer (the key starts with `omi_dev_`).
- The Dataview plugin is optional, only needed for the sample queries.
- **Manual install:** download the latest release, unzip it into the vault's `.obsidian/plugins/obsidian-omi` folder, reload Obsidian and turn on "Omi" in Community Plugins.
- **Quick start:** open Settings, Omi and enter the API key; click the brain icon to open Omi Hub; in the Sync tab click Full Resync.
- **Settings:** API key, storage folder, start date, auto-sync interval (0 is off), what to include (overview, action items, events, transcript) and daily note linking.
## File structure in the vault
Under the `Omi/` folder: `_omi-index.md` (the main index), `Memories.md` (a memory backup), `Tasks.md` (an action item backup). Conversations sit in year, month and day folders; each day has an index and optionally `overview.md`, `action-items.md`, `events.md` and `transcript.md` files. The head of a file has the date, category, duration, location, conversation count, and tags prefixed `omi/`. The plugin calls Omi's `GET /v1/dev/user/conversations` endpoint, with date filtering, pagination and incremental sync. Times use the computer's time zone; links can break if titles do not match, and re-syncing can recreate files.
## Privacy and legal: the part to think about carefully
An always-listening device is this system's biggest risk:
- **The people being recorded.** Recording conversations of customers, partners or employees may require consent under local regulations. This article is not legal advice; ask a qualified person.
- **Where the data goes.** Transcripts and summaries are processed through Omi's service and synced with an API key; I have no information about their data policy, so read the terms.
- **The API key** allows reading conversations; keep it secret like a password.
- **The Obsidian vault** now holds raw transcripts; consider disk encryption and controlled backups.
## How to use it sensibly
1. Start with a limited recording scope (for example only personal notes or meetings you host with notice given).
2. Sync only the summary and action items, and turn off raw transcripts if you do not need them.
3. Review periodically and delete sensitive content.
4. Use this vault as a library for an agent to read under control; for how Hermes handles memory, see [Building a second brain with Hermes, notes and AI Automation](xay-second-brain-voi-hermes-ghi-chu-va-ai-automation.html) and compare [Claude and Obsidian: a plugin or Claude Code for your notes system?](claude-va-obsidian-chon-plugin-hay-claude-code-cho-he-ghi-chu.html).
