---
title: Claude Code AI SEO with Netlify and MCP: a content publishing workflow
desc: Connect Claude Code to Netlify through MCP to publish a content site: how to add the MCP server, a safe workflow and what to control before you publish.
min: 7
---
QUICK: MCP lets Claude Code use external tools, including Netlify's MCP server for working with your site. The safe workflow is to let the AI draft and edit content in your code repository, check it in a preview build, and approve it yourself before it goes to the main site.
## What MCP and Netlify MCP are
MCP (Model Context Protocol) is a standard that lets AI tools connect to outside services. Netlify provides an MCP server that connects an agent to Netlify and its command-line tools. You can use it to let an agent work with your Netlify site instead of typing every command yourself. The exact list of tools the server offers is documented by Netlify, so read that instead of guessing.
## How to add the Netlify MCP server
According to Netlify's documentation, the recommended way is the remote server:
```
npx -y add-mcp https://mcp.netlify.com/mcp
```
This command runs interactively so you can choose which agents to configure (Claude Code is among them). For environments that must run a local server, the documentation gives an alternative:
```
npx -y add-mcp "npx -y @netlify/mcp"
```
The documentation also says the older connection at `netlify-mcp.netlify.app` still works, but new connections should use `mcp.netlify.com`. Netlify's guide for Claude Code requires Node 24 or higher and recommends `claude mcp add --transport http netlify https://mcp.netlify.com/mcp` (local server: `claude mcp add netlify -- npx -y @netlify/mcp`). Netlify also offers `npx netlify@latest init`, run in the project folder: it signs you in, installs agent skills, adds the MCP server and links the folder to a Netlify project, so know what it changes before you run it.
## A suggested content publishing workflow
1. **Keep content in a code repository** (Markdown or HTML pages) with Git to track changes.
2. **Claude Code drafts or edits the article** following the brief and the rules in `CLAUDE.md`, see [Claude Code SEO Agent: a workflow for building SEO content with AI](claude-code-seo-agent-quy-trinh-xay-noi-dung-seo-bang-ai.html).
3. **Run automatic on-page checks:** title, meta description, headings, canonical, broken links.
4. **Preview:** push to a separate branch and let Netlify build a preview (deploy preview).
5. **You approve** the content and facts on the preview.
6. **Merge into the main branch** to publish, following the process you have set.
## What to keep under control
- **Agent permissions.** Grant only what is needed. For actions that could break the site or affect costs, require confirmation before they run.
- **No self-publishing.** Pushing to the main site should be your decision, not something the agent does on its own. The Netlify CLI has `netlify deploy --prod`, which publishes straight to production, so require the agent to ask you before running it.
- **Secrets.** Access keys and environment variables should not sit in the repository or in the agent's input.
- **Authentication.** The MCP server connects with your account, so the agent's actions have real effect. Review the permissions granted in the account.
## About SEO content
A tool that publishes quickly does not make content better. Google has a policy against creating many pages only to manipulate rankings, including when AI is used, see [An AI SEO system with Claude: automate content but still edit it](he-thong-ai-seo-voi-claude-tu-dong-hoa-noi-dung-nhung-van-can-bien-tap.html). Use the speed to gain time for editing, not to publish more.
## After publishing
Monitor with Google Search Console: is the article indexed, does it have impressions yet. If not, recheck technical factors such as the canonical, `robots` and the sitemap. If you still need to install Claude Code first, see [Setting up Claude Code step by step: the foundation for AI coding](thiet-lap-claude-code-tung-buoc-nen-tang-cho-coding-bang-ai.html).
