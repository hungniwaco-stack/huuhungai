---
title: Google Jules and the Jitro rumor: what is confirmed and what is not
desc: Google has announced Jules will shut down at the end of 2026: key dates, exporting your data, what is unconfirmed about Jitro and choosing another tool.
min: 6
---
QUICK: Update, Nov 25, 2026: Google has announced that Jules is shutting down. According to the official changelog dated Oct 29, 2026, users had until Nov 11 to finish sessions, after which Jules is read-only and will end on Dec 31, 2026. Jitro, according to the sources I found, still appears only in leaks and third-party posts.
## Update: Jules is shutting down
The "Jules Turndown" entry in the Jules changelog, dated Oct 29, 2026, says:
- Jules will wind down on Dec 31, 2026, as part of Google unifying its agentic coding efforts.
- Users had until Nov 11, 2026 to finish up sessions. After that date, Jules is read-only until the end of the year.
- Google says what was learned from Jules is shaping other products, including the Google Antigravity platform.
- You can export the data Jules holds into a folder on your machine, including account settings, environment variables, scheduled tasks, connected repositories, memories, setup scripts and every session. Code, branches and pull requests stay on GitHub.
If you use Jules, export your data before the service ends, following the instructions in that changelog entry. They ask you to install Jules Tools and then use a command-line coding agent to run the export. I have not tested this process. The exported data can include environment variables, so check it before you store or share it.
An earlier version of this article did not mention the Oct 29 notice and suggested that you try Jules. That was a mistake and it has been corrected.
## What Jules was
According to Google's official blog (posted Aug 6, 2025):
- Jules is an "asynchronous coding agent", which at that point became generally available, powered by Gemini 2.5.
- During the beta, thousands of developers ran tens of thousands of tasks, producing more than 140,000 code improvements shared publicly.
- The launch included GitHub issues integration, multimodal support and planning using the thinking ability of Gemini 2.5 Pro.
## What is not confirmed: Jitro
Search results show Jitro mentioned as the name of the next generation of Jules. The descriptions come from third-party posts and leaks:
- A design oriented around **goals** rather than step-by-step instructions.
- Possibly a persistent workspace, inferred from the names of leaked tools.
- One report speculates the agent might work out for itself what to change in the code to improve a metric; the report itself states this is speculation.
The Jules shutdown notice mentions Antigravity and does not mention Jitro. I found no official Google announcement about a Jitro launch, timing or availability. So any feature comparison between Jitro and Jules is speculation, and this article does not offer a comparison table.
## How to read news about unreleased tools
- Separate official announcements from leaks and speculative posts. For how to read rumors, see [Rumors about new AI models: how should you read leaked information?](tin-don-mo-hinh-gpt-moi-nen-doc-thong-tin-ro-ri-nhu-the-nao.html).
- Do not change your workflow because of a code name.
- Wait for official documentation, then try it on a non-critical repository.
## Choosing an agentic coding tool now
Do not start new work on Jules. When evaluating any coding agent, ask:
1. Where does it run (your machine or the cloud) and where does your code go?
2. Can it write to the main branch? Start with a separate branch and review changes before merging.
3. What are the limits and costs by plan?
4. Are the results measurable: how many tasks accepted, how many reworked?
5. If the product ends, how do you export your data and move away?
For a measurement framework, see [Evaluating AI agents through real tests: which criteria to look at](danh-gia-ai-agent-qua-bai-test-thuc-te-nhin-vao-tieu-chi-nao.html). For coding agents that run on your machine, see [Setting up Claude Code step by step: the foundation for AI coding](thiet-lap-claude-code-tung-buoc-nen-tang-cho-coding-bang-ai.html).
