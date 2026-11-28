---
title: Claude's working modes: how do chat, code and collaboration differ?
desc: Telling Claude's working modes apart: chat, Claude Code and file collaboration. What each does, which work it suits and how they differ in access permissions.
min: 6
---
QUICK: Use chat for Q&A, writing and analysis. Use Claude Code when you need to work directly in a code folder. For multi-step, non-coding work on files and apps, you used to pick Cowork; since Sep 16, 2026 Anthropic has been merging Cowork into chat, so depending on your account you may no longer need to choose. The closer it gets to your files, the more you need to watch access permissions.
## Update: chat and Cowork are merging
On Sep 16, 2026, Anthropic announced that Cowork and chat were merging into one Claude. According to the official help article (read on Nov 28, 2026), the new experience is rolling out gradually to Pro, Max and Ultra plans; on Team and Enterprise plans it is available where "Chat and Cowork unified" is turned on. In this experience you do not pick a mode: what you could previously do only in Cowork is available from any conversation. The Code tab is where it was.
If your message box still shows the two "Chat" and "Cowork" options, your account has not moved over yet. The comparison below still helps you understand three kinds of work and the permissions that come with them: for people who have the new experience, chat and collaboration are two ways of using the same conversation.
## Why tell them apart
The same model, but three working modes that differ greatly in what it can do with your machine and data. Choosing the wrong mode both slows the work down and can create unnecessary risk. This article helps you choose the right mode for each kind of work.
## Mode 1: Chat
This is the familiar conversation window. You type a question or paste content, and Claude answers in text. Depending on the version, you can attach documents and images, create content such as drafts or source code right in the conversation, and organize long work by project.
- **Suits:** Q&A, drafting, summarizing documents, analyzing ideas, learning a new topic.
- **Permissions:** usually only works with what you put into the conversation. It does not read or edit files on your machine on its own. In the merged experience the scope is wider: Claude can work with folders on your computer (through Claude Desktop), browse the web and use apps you have connected, see Mode 3.
- **Risk:** low, mostly the sensitive data you paste in yourself.
## Mode 2: Claude Code
Claude Code is a coding assistant that works directly in your project folder, usually through a terminal. It reads code, edits files, runs commands and checks results. How often it asks you depends on the permission mode, and recent versions may start in a mode that runs many actions on its own, see [Setting up Claude Code step by step: the foundation for AI coding](thiet-lap-claude-code-tung-buoc-nen-tang-cho-coding-bang-ai.html).
- **Suits:** writing and fixing code, building small websites, automating with scripts, working on many files at once, and also text folders such as a notes vault.
- **Permissions:** read and write in the folder you open, run commands with the permissions you grant.
- **Risk:** medium to high if you grant broad permissions. Use Git and plan-only mode when starting out.
See the step-by-step guide at [Setting up Claude Code step by step: the foundation for AI coding](thiet-lap-claude-code-tung-buoc-nen-tang-cho-coding-bang-ai.html).
## Mode 3: Collaboration on files and apps
This is the mode for non-coding work, where Claude works with files and apps on your machine to finish a multi-step task, such as organizing documents, consolidating data or drafting a report from several sources.
- **Suits:** office and knowledge work with many files, needing consolidation or bulk processing.
- **Permissions:** access to the folders and apps you allow.
- **Risk:** similar to Claude Code. Open only the folder you need and check the result before using it.
According to the help article for the merged experience, Claude reaches local files, the built-in browser and computer use only while Claude Desktop is open. The permission setting in the message box has two levels: Auto (rolling out as the default on Pro, Max, Ultra and Team), where Claude keeps working without asking about each step and automated safety checks run before most actions; and Manual (the default on Enterprise, except the Cowork side panel in Chrome), where Claude asks before it acts. By default Claude asks before permanently deleting files, but that protection does not cover computer use. For work with real consequences, such as sending messages or changing important files, stay close and review. Features are still changing, so see the current description.
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
An effective way is usually to combine them: use chat to think and plan, use Claude Code or the collaboration mode to carry out the work on files, then go back to chat to review and adjust. To judge whether an agent that works on files can be trusted, see [Evaluating AI agents through real tests: which criteria to look at](danh-gia-ai-agent-qua-bai-test-thuc-te-nhin-vao-tieu-chi-nao.html).
