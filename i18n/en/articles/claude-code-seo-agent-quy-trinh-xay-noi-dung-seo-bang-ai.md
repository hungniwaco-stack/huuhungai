---
title: Claude Code SEO Agent: a workflow for building SEO content with AI
desc: A workflow for using Claude Code to support SEO content: the rules file, from brief to on-page checks, quality gates and limits to avoid thin content.
min: 8
---
QUICK: Claude Code helps SEO in the repetitive-operations part: creating briefs from data you provide, checking titles, meta, headings and links in bulk, and generating structured data. It does not replace keyword research with real data or human editing. Bulk-generated content with no value of its own can be treated by Google as spam.
## What Claude Code can and cannot do for SEO
If your website's content sits in a folder (Markdown files, HTML or a code project), Claude Code can work on the whole folder: reading many articles at once, detecting repeated errors, fixing in bulk by rule and creating new files. That is the laborious, error-prone part when done by hand.
But there are things it cannot do without data from you: knowing which keywords have search volume, how competitors rank, which content is really useful to your readers. Search volume numbers must come from a keyword research tool or Search Console, and must not be left for the AI to guess.
## Step 1: Write a rules file for the content project
Write the constraints into `CLAUDE.md` so every article keeps the same standard:
```
# SEO content project
- Language: English. Tone: clear, practical, no exaggeration.
- Do not invent figures, quotes, names or studies. If a fact is missing, write "needs source".
- Each article has: a title, its own meta description, one h1, h2s in order, at least 2 internal links.
- Each article answers one specific search intent, without mixing several topics.
- When creating a new article, propose an outline and wait for my approval before writing.
```
This is an example; adjust it to your brand.
## Step 2: Keyword and intent research with real data
Use the keyword research tool you already have and data from Google Search Console to choose topics. Once you have a list, give it to Claude Code as a file (CSV or Markdown) and ask it to:
- Group keywords with the same search intent.
- Point out clusters that may overlap and should be merged into one article.
- Suggest an article structure for each group.
The search volume and difficulty numbers are still your data; the AI only sorts and analyzes.
## Step 3: Brief and outline
For each article, create a brief file with the search intent, the questions readers need answered, the points that must be included, trustworthy reference sources and planned internal links. Approving the brief before writing is the step that saves the most time, because fixing an outline is far cheaper than fixing a whole article.
## Step 4: Controlled drafting
Let the AI write a draft from the approved brief, but treat it only as a rough version. The most valuable part of a good SEO article is usually what the AI does not already have: real experience, your own examples, your own data, a well-founded viewpoint. Add those in the editing step.
## Step 5: Bulk on-page checks
This is something Claude Code does very effectively. Ask it to check the whole folder against clear criteria:
- Each page has exactly one `h1` and headings in a sensible order.
- Titles and meta descriptions are present and not duplicated between pages.
- There is a canonical tag, internal links are not broken, and images have descriptive attributes.
- Structured data (JSON-LD) is valid.
You can also ask it to write a small script to recheck periodically, for example title length:
```
import glob, re

for path in glob.glob("content/*.html"):
    s = open(path, encoding="utf-8").read()
    t = re.search(r"<title>(.*?)</title>", s, re.S)
    if not t:
        print("Missing title:", path)
    elif len(t.group(1).strip()) > 70:
        print("Title too long:", path, len(t.group(1).strip()))
```
Title length is only a guide: Google truncates by display width, not by character count, so do not treat the number as a hard rule.
## Step 6: Edit, verify and publish
Before publishing, a real person needs to reread: check each fact, add sources, delete filler, and ask one question: does this article help readers more than what already exists online. After publishing, monitor with Search Console to see which articles are indexed and have impressions.
## Limits to keep to avoid risk
- **Do not create bulk content with no value of its own.** Google has a policy against scaled content made only to manipulate rankings, whether created by AI or people. Quality and usefulness are the criteria.
- **Do not invent facts.** A model can write very confidently about something false. Every figure, product name and quote must be verified.
- **Do not copy other people's content** while only changing the wording.
- **Do not rely entirely on AI for experience and expertise**, because that is what makes your article different.
- **Keep a person ultimately accountable** for each published article.
## Quick checklist
- A `CLAUDE.md` with clear content rules.
- Keywords and intent taken from real data.
- Each article has a brief approved before writing.
- Automatic on-page checks and human editing.
- Every fact verified and sourced.
If you want to publish directly from the project, see also [Claude Code AI SEO with Netlify and MCP: a content publishing workflow](claude-code-ai-seo-voi-netlify-va-mcp-workflow-xuat-ban-noi-dung.html). If you need to install Claude Code first, see [Setting up Claude Code step by step: the foundation for AI coding](thiet-lap-claude-code-tung-buoc-nen-tang-cho-coding-bang-ai.html).
