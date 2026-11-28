---
title: A skill tree for AI agents: why agents need to learn by capability
desc: What skills are for AI agents, why to split capabilities into small skills, how to write a good SKILL.md file and how to arrange them into a capability tree.
min: 8
---
QUICK: Instead of stuffing every instruction into one long prompt, many agent systems use skills: each skill is a folder holding instructions for one specific capability, loaded only when needed. This makes the agent more consistent, easier to maintain and saves context. A "skill tree" is how you arrange them from basic to advanced.
## The problem skills solve
A general-purpose agent needs to know many procedures: writing reports, checking websites, processing invoices, drafting emails. If you stuff everything into one giant instruction, the context is used up, the agent gets distracted and each part is hard to fix. Skills split that knowledge into independent units, each with one clear job.
## What a skill is
According to Anthropic's engineering article on Agent Skills, a skill is a folder with a `SKILL.md` file that starts with YAML metadata containing a name and a description, followed by detailed instructions, and it can include reference files or scripts. This is how it works in tools like Claude Code. An example of a minimal structure:
```
skill-name/
  SKILL.md
  references/
    detailed-rules.md
```
And the head of the `SKILL.md` file:
```
---
name: check-page-seo
description: Check the title, meta, headings and canonical of an HTML page. Use when the user asks for a technical SEO review of a page.
---

# Check a page's SEO
(the steps, rules and examples)
```
Under the Agent Skills specification (agentskills.io), `name` has at most 64 characters, only lowercase letters, numbers and hyphens, cannot start or end with a hyphen or contain two hyphens in a row; `description` has at most 1,024 characters. Anthropic says that on Dec 18, 2025 it published Agent Skills as an open standard for use across platforms.
## Loading in parts: why skills save context
Anthropic calls the core principle progressive disclosure:
1. At startup, the agent loads only the **name and description** of every skill.
2. When a skill fits the task at hand, the agent then loads the **full content** of `SKILL.md`.
3. The accompanying reference files are loaded only when the instructions mention them.
Because of this you can have a great many skills without filling the context. It also explains why **the description matters most**: the agent relies on it to decide whether to use a skill.
## How to write a good skill
- **A description that says when to use it,** including the situations and the keywords a user might say, not just what the skill does.
- **One skill, one job.** A skill that is too broad is hard to use and hard to fix.
- **Specific instructions with examples,** with the steps and the criteria for being done.
- **Split long detail into reference files** so the body of `SKILL.md` stays compact.
- **State the limits and what must not be done.**
- **Test with real situations** and fix the description when the agent picks the wrong skill.
## From skills to a "capability tree"
A skill tree is a way of organizing: foundational skills at the bottom, advanced skills that rely on them above.
```
Foundation:     read files, normalize text, write logs
   |
Intermediate:   check a page's SEO, summarize documents, extract invoice data
   |
Advanced:       a whole-site SEO report, an end-to-end invoice processing workflow
```
The benefit: you build gradually by level of trust, can test each tier, and know where the weak point is when the agent goes wrong.
## Agents that learn skills themselves
Some agents can create skills from experience. The official Hermes Agent documentation describes it as a self-improving agent that creates skills from experience and keeps memory across sessions. This is convenient, but review the skills the agent creates: they may contain errors or overly broad permissions, and you should check them as you would source code.
## Governing skills
- **Assign an owner** for each important skill.
- **Record versions** and the reason for changes.
- **Check security:** a skill can contain scripts, so use skills only from trusted sources and read them before installing.
- **Review periodically,** removing skills no longer used, as in managing a tool library in [How should an AI tool library be organized to be easy to use?](mot-kho-cong-cu-ai-nen-duoc-to-chuc-nhu-the-nao-de-de-dung.html).
## When to use skills
When you repeat the same workflow many times and want the agent to do it your way. You do not need a skill for one-off work. To choose work worth automating and to evaluate agents, see [Evaluating AI agents through real tests: which criteria to look at](danh-gia-ai-agent-qua-bai-test-thuc-te-nhin-vao-tieu-chi-nao.html).
