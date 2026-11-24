---
title: Claude and Obsidian: a plugin or Claude Code for your notes system?
desc: Comparing AI plugins in Obsidian with running Claude Code on a whole notes vault: when to use which, how to prepare, protecting your data and sample tasks.
min: 7
---
QUICK: Use an AI plugin when you want Q&A or writing right inside each note. Use Claude Code when you need to work on many notes at once, such as finding duplicate notes, adding properties, grouping or building a table of contents. Before letting AI edit the vault, back it up with Git.
## What an Obsidian vault really is
An Obsidian vault is just a folder of Markdown files (`.md`) on your machine, with a few configuration folders. This very feature makes Claude Code usable right away: it reads and writes files in the folder as it would in a code project, with no separate connection to Obsidian. You can open the vault in Obsidian to read as normal while Claude Code works in the same folder.
## Two approaches
- **An AI plugin in Obsidian:** sits right in the notes interface. Suits Q&A about the open note, rewriting a paragraph, summarizing. Convenient for small actions, but usually works only within the range you select.
- **Claude Code running on the vault folder:** works on the whole folder tree. Suits bulk tasks that have rules and need rechecking, but requires a terminal.
The name and features of each plugin change constantly and depend on the developer, so look at the description, the reviews and the permissions the plugin asks for yourself before installing.
## When to choose which
- **Choose a plugin** if your work is writing, quick questions and editing text one note at a time.
- **Choose Claude Code** if your work is reorganizing: bulk renaming, adding property headers to hundreds of notes, finding notes that say the same thing, creating summary notes by topic.
- **Using both** is perfectly normal: a plugin for daily work, Claude Code for periodic cleanup.
## Preparation before letting Claude Code work on the vault
1. **Back up with Git.** Initialize Git in the vault folder and commit the current state. You review every change with `git diff` and undo if the AI edits wrongly.
```
cd path/to/vault
git init
git add -A
git commit -m "Backup before using AI"
```
1. **Exclude folders you do not want the AI to touch.** Use deny rules in `.claude/settings.json` for private folders.
2. **Write a CLAUDE.md** describing the vault's conventions so the AI works your way:
```
# Personal notes vault
- Notes are Markdown files, named in the form "Topic - Main idea".
- Each note has a properties section (frontmatter) with: tags, created.
- Internal links use the syntax [[Note name]].
- Do not edit the "Private-diary" and "Passwords" folders.
- Always propose a plan first, and edit only when I agree.
```
For installation instructions for Claude Code, see [Setting up Claude Code step by step](thiet-lap-claude-code-tung-buoc-nen-tang-cho-coding-bang-ai.html).
## Sample tasks for Claude Code
Start in plan-only mode and test on a small subfolder:
- "List the notes missing the tags property, change nothing yet."
- "Propose pairs of notes with similar content so I can decide on merging."
- "Create a table-of-contents note for the Projects folder, linking to each note with wiki syntax."
- "Standardize file names to the convention in CLAUDE.md, show me the rename list before doing it."
## Risks to know
- **Bulk edits are very easy to get wrong.** A wrong renaming rule can break links between notes. Always read the plan and use `git diff`.
- **Syncing across several devices.** If the vault sits in a cloud-synced folder, bulk changes can cause conflicts. Do it when other devices are not editing.
- **Privacy.** The content of files Claude Code can read is sent off for processing. Do not let it read notes that contain passwords, customer data or sensitive information.
- **Do not let the AI "rewrite" your notes** when it is not needed. Personal notes lose value if they lose your own voice.
## Where to start
If you use nothing yet, try a plugin for daily writing. When the vault is big enough that you want to "clean house", move to Claude Code with a Git backup. This approach raises the level of trust gradually without betting all your notes from the start.
