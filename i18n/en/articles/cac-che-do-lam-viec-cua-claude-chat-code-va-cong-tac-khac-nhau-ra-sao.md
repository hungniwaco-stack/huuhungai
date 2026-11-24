---
title: Claude's working modes: how do chat, code and collaboration differ?
desc: Telling Claude's working modes apart: chat, Claude Code and file collaboration. What each does, which work it suits and how they differ in access permissions.
min: 6
---
QUICK: Use chat for Q&A, writing and analysis inside a conversation. Use Claude Code when you need to work directly in your code folder. Use the collaboration mode when you want Claude to work with files and apps on your machine for non-coding work. The closer it gets to your files, the more you need to watch access permissions.
## Why tell them apart
The same model, but three working modes that differ greatly in what it can do with your machine and data. Choosing the wrong mode both slows the work down and can create unnecessary risk. This article helps you choose the right mode for each kind of work.
## Mode 1: Chat
This is the familiar conversation window. You type a question or paste content, and Claude answers in text. Depending on the version, you can attach documents and images, create content such as drafts or source code right in the conversation, and organize long work by project.
- **Suits:** Q&A, drafting, summarizing documents, analyzing ideas, learning a new topic.
- **Permissions:** usually only works with what you put into the conversation. It does not read or edit files on your machine on its own.
- **Risk:** low, mostly the sensitive data you paste in yourself.
## Mode 2: Claude Code
Claude Code is a coding assistant that works directly in your project folder, usually through a terminal. It reads code, edits files, runs commands and checks results, with important actions needing your permission.
- **Suits:** writing and fixing code, building small websites, automating with scripts, working on many files at once, and also text folders such as a notes vault.
- **Permissions:** read and write in the folder you open, run commands with the permissions you grant.
- **Risk:** medium to high if you grant broad permissions. Use Git and plan-only mode when starting out.
See the step-by-step guide at [Setting up Claude Code step by step](thiet-lap-claude-code-tung-buoc-nen-tang-cho-coding-bang-ai.html).
## Mode 3: Collaboration on files and apps
This is the mode for non-coding work, where Claude works with files and apps on your machine to finish a multi-step task, such as organizing documents, consolidating data or drafting a report from several sources.
- **Suits:** office and knowledge work with many files, needing consolidation or bulk processing.
- **Permissions:** access to the folders and apps you allow.
- **Risk:** similar to Claude Code. Open only the folder you need and check the result before using it.
The name and features of this mode change with each version, so see the current description in the Claude app you are using.
## Quick selection table
```
What you need                                   Mode to use
----------------------------------------------  ----------------
Ask a question, request a draft, summarize text Chat
Fix code, add a feature, run tests              Claude Code
Tidy up or reorganize a whole notes folder      Claude Code
Consolidate many documents into a report        Collaboration
Learn a topic, ask about a document you paste   Chat
```
## Selection principles
- **Start from the mode with the least permission that is enough.** Anything you can do in chat does not need access granted to your machine.
- **Switch to a mode with permissions when the work needs real files**, and when you do, have a backup.
- **One folder, one task.** Open only the relevant folder, not the whole drive.
- **Always check results** before using them, especially for important files.
## Data and privacy
In every mode, content you give Claude or let it read is processed by the service. Check the provider's current data policy, and do not put in passwords, access keys or sensitive customer data if you do not need to.
## Combining the modes
An effective way is usually to combine them: use chat to think and plan, use Claude Code or the collaboration mode to carry out the work on files, then go back to chat to review and adjust. To judge whether an agent that works on files can be trusted, see [Evaluating AI agents through real tests](danh-gia-ai-agent-qua-bai-test-thuc-te-nhin-vao-tieu-chi-nao.html).
