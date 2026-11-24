---
title: Google Jules and the Jitro rumor: what is confirmed and what is not
desc: Jules is Google's launched asynchronous coding agent; Jitro has only appeared in leaks. What is confirmed, what is not and how to choose a tool.
min: 6
---
QUICK: Jules is a real Google product (an asynchronous coding agent that left beta on Aug 6, 2025, powered by Gemini 2.5). Jitro, according to the sources I found, is so far only a name in leaks and speculation, and I found no official announcement from Google. So "how do they differ" cannot be answered with facts yet, only with guesses.
## What is confirmed: Jules
According to Google's official blog (posted Aug 6, 2025):
- Jules is an "asynchronous coding agent", generally available, powered by Gemini 2.5.
- During the beta, thousands of developers ran tens of thousands of tasks, producing more than 140,000 code improvements shared publicly.
- Changes at launch: a polished interface and hundreds of bugs fixed, reuse of earlier setup so new tasks run faster, GitHub issues integration, multimodal support, and planning using the thinking ability of Gemini 2.5 Pro.
- Plans: introductory access, with Jules in Google AI Pro getting 5 times the limits and Jules in Google AI Ultra 20 times. Exact limits are listed at `jules.google`.
That blog does not describe how Jules works internally (such as the use of virtual machines), nor does it make any privacy or data security claims. Many third-party guides describe Jules cloning your repository into a cloud virtual machine and working asynchronously; I could not confirm that from the official page, so check `jules.google` before handing over important code.
## What is not confirmed: Jitro
Search results show Jitro mentioned as an internal name for the next generation of Jules, based on leaks. The descriptions (all from third-party blogs, with dates that do not match each other):
- A design oriented around **goals** rather than step-by-step instructions.
- Possibly a persistent workspace, inferred from the names of leaked tools.
- One report speculates the agent might work out for itself what to change in the code to improve a metric; the report itself states this is speculation.
The official Google pages I read do not mention Jitro at all. I found no launch announcement, timing or availability. So any feature comparison between Jitro and Jules right now is speculation, and this article does not offer a comparison table.
## How to read news about unreleased tools
- Separate official announcements from leaks and speculative posts. For how to read rumors, see [Rumored new GPT models: how to read leaked information](tin-don-mo-hinh-gpt-moi-nen-doc-thong-tin-ro-ri-nhu-the-nao.html).
- Do not change your workflow because of a code name.
- Wait for official documentation, then try it on a non-critical repository.
## Choosing an agentic coding tool now
If you want to try Google's asynchronous agent, Jules is the real thing. When evaluating any coding agent, ask:
1. Where does it run (your machine or the cloud) and where does your code go?
2. Can it write to the main branch? Start with a separate branch and review changes before merging.
3. What are the limits and costs by plan?
4. Are the results measurable: how many tasks accepted, how many reworked?
For a measurement framework, see [Evaluating AI agents through real tests](danh-gia-ai-agent-qua-bai-test-thuc-te-nhin-vao-tieu-chi-nao.html). For coding agents that run on your machine, see [Setting up Claude Code step by step](thiet-lap-claude-code-tung-buoc-nen-tang-cho-coding-bang-ai.html).
