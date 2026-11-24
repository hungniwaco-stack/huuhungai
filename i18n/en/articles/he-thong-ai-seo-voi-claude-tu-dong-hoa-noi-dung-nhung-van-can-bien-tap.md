---
title: An AI SEO system with Claude: automate content but still edit it
desc: Design an SEO content system with AI and accountable people: what to automate, what people must do, review gates and Google's spam risks.
min: 8
---
QUICK: Automate repetitive work such as technical checks and outlines, and keep for people the decisions on topics, adding real experience, verifying facts and final approval. Google treats creating many pages only to manipulate rankings as spam, whether the content is made by AI or by people.
## The goal of the system
A good content system with AI is not a printing press. It is a workflow that helps you do faster the work that takes effort but needs little judgment, so time goes to the part that creates value: understanding readers, having real experience and being accountable for accuracy. This article covers how to organize and govern that workflow. For the technical side using Claude Code, see [Claude Code SEO Agent: a workflow for building SEO content with AI](claude-code-seo-agent-quy-trinh-xay-noi-dung-seo-bang-ai.html).
## The risk to understand: Google's spam policy
Google's spam policy defines scaled content abuse as creating many pages with the primary purpose of manipulating search rankings, and states clearly that using generative AI tools to create many pages that add no value for users is one example. Other examples include stitching together content from many pages without adding value, and creating many nonsensical pages stuffed with keywords. The policy applies regardless of how the content is created. This means the criterion is not "whether AI is used" but "whether the page has value for readers".
## What to automate and what people must do
**Worth automating:**
- Bulk technical checks: title, description, headings, canonical, broken links.
- Grouping keywords by intent from data you provide.
- Creating briefs and outlines for you to approve.
- Drafting a rough version from an approved brief.
- Suggesting internal links, formatting and generating structured data.
**People must do:**
- Decide which article is worth writing and why.
- Add experience, examples, data and your own viewpoint.
- Verify every fact, figure and quote.
- Make the final decision to publish.
- Take responsibility when there are errors.
## Review gates
Put mandatory gates in the workflow, each with an accountable person:
1. **Topic gate:** which search intent does this article answer, and why do readers need it more than what already exists.
2. **Brief gate:** does the outline cover the readers' questions properly.
3. **Fact gate:** every claim has a source, with no figures or quotes that cannot be verified.
4. **Own-value gate:** does the article contain something only you have (experience, data, perspective).
5. **Technical gate:** the automatic on-page checks pass.
6. **Final approval gate** before publishing.
An article that fails a gate goes back to that step and is not published "just to get it done".
## Instructions for the AI, written as a file
Write the rules into the project's instruction file so the AI applies them consistently, for example:
```
- Do not invent figures, names, quotes or studies. If a fact is missing, write "needs source".
- Every claim about a product or regulation must come with an official source.
- Do not write identical content across articles; each article has its own intent.
- Propose an outline first, and write only when approved.
```
## Quantity versus quality
The speed AI brings easily turns into a reason to publish more. Do the opposite: use the time saved to make fewer articles but more carefully. One warning sign is when many articles on the site share the same heading structure, the same opening sentence and nearly the same content, with only the topic name changed. That is exactly the kind of thin content to avoid. If your site is in this state, merge, rewrite or remove some instead of adding more.
## Monitoring quality
- Use Search Console to see which articles are indexed and which are ignored.
- Measure real engagement: reading time, return rate, reader feedback.
- Periodically review and update old articles, especially those about fast-changing products.
- Keep a source log for each article to make rechecking easy.
## What to do first
If you already have many AI-generated articles, start with a small review: pick 10 articles, check each against the six gates above and record which ones fall short. The result will show you the size of the problem more clearly than any theory. For how Google views AI features in search, see [Ranking in Google AI Mode: what does the SEO process need to change?](xep-hang-trong-google-ai-mode-quy-trinh-seo-can-thay-doi-gi.html).
