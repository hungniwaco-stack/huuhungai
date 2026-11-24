---
title: Setting up Claude Code step by step: the foundation for AI coding
desc: Install Claude Code, sign in, create CLAUDE.md, choose a permission mode and hand over a safe first task on a real project, step by step.
min: 7
---
QUICK: Install Claude Code with one command, sign in, open a terminal in the project folder, run `/init` to create the `CLAUDE.md` file, then hand over a small task in plan-only mode. Installation is very short; the parts that need care are access permissions and how you hand out work.
## What Claude Code is and who should use it
Claude Code is a coding assistant that runs right in the terminal. Unlike a chatbot that only answers in a chat window, it can read your project, edit files, run commands and check the results, but every important action needs your permission. It suits people who build websites, automation or internal tools and want to hand repetitive work to AI while keeping control. You do not need to be a strong coder, but you need to be able to read the changes it proposes, or have someone review them before they go to a real environment.
## Preparation before installing
- **Account:** a paid Claude plan, or an API key from the Anthropic Console. Costs and limits change over time, so see the official pricing page instead of trusting an old figure.
- **Git:** strongly recommended. Having the project in a Git repository lets you review and undo every change with a single command. On Windows, install Git for Windows or use WSL.
- **A small project to try:** do not start with a client project that is live.
## Step 1: Install
Choose one of the ways below. Always take the command from Anthropic's official documentation, because install commands can change by version.
```
# macOS, Linux or WSL
curl -fsSL https://claude.ai/install.sh | bash

# Windows (PowerShell)
irm https://claude.ai/install.ps1 | iex

# Or through npm (needs Node.js 18 or later)
npm install -g @anthropic-ai/claude-code
```
Open a new terminal window and check:
```
claude --version
claude doctor
```
The first command prints the version number, the second diagnoses common installation problems. Run install scripts only from the exact official domain, and do not run scripts from a source you cannot verify.
## Step 2: Open it in the project and sign in
```
cd path/to/your-project
claude
```
The first time you run it, Claude Code opens the browser for you to sign in with a Claude account, or lets you choose to use an API key. Always run the `claude` command in the project folder, not in the root of a drive or the user folder, because then it may scan unrelated files.
## Step 3: Create CLAUDE.md so it understands the project
Type `/init`. Claude Code reads the project and creates a `CLAUDE.md` file at the root, where it records what it needs to remember each time a session starts. This is the file most worth spending time on. A short, useful version usually has:
```
# Project: a small online shop website
- Run locally: npm run dev (port 3000)
- Test: npm test
- Main source is in the src/ folder
- Do not edit the dist/ folder or the .env file
- Interface wording: English, concise
```
This is only an illustrative example; replace it with the real information of your project. Keep it short, specific and updated when conventions change.
## Step 4: Understand the permission modes before handing out work
This is the part that decides how safely you use Claude Code. By default, it asks you before editing files or running commands. During a session, you can press `Shift+Tab` to switch between modes, including a mode that auto-accepts file edits and a **plan** mode (only analyzes and proposes a plan, changing nothing). While you are new, prefer the default or plan mode, and avoid modes that skip all confirmations.
To block it from reading sensitive files, create a `.claude/settings.json` file in the project:
```
{
  "permissions": {
    "deny": ["Read(./.env)", "Read(./secrets/**)"]
  }
}
```
The content of files Claude Code reads is sent off for the model to process, so do not leave API keys, passwords or customer data within its reach.
## Step 5: Hand over the first task
Start with a risk-free task, and only then move to one that edits files:
1. **Read and understand:** "Read the project and explain the folder structure. Do not edit any file."
2. **Plan:** turn on plan mode and ask "Propose a plan to add a contact button to the home page, list the files to be edited, wait for my approval."
3. **Carry out and check:** approve the plan, let it do the work, then review it yourself with `git diff` before keeping the change.
Hand over one clear task at a time. Use `/clear` when you switch to different work so the conversation does not get mixed, and `/compact` when a session has grown too long. Decide for yourself when to commit, and do not let unreviewed changes pile up.
## Common errors
- **`claude: command not found`:** open a new terminal after installing. If it still fails, check that the folder holding the command is in your PATH, or run `claude doctor`.
- **Cannot sign in:** check that you are using the right type of account (a Claude plan or an API key) and sign in again.
- **It reads too many unrelated files:** usually from running in the wrong folder; exit and run again in the project folder.
- **The result is not what you wanted:** describe it more specifically, include examples, and split the work instead of handing over one request that is too large.
## Checklist after installing
- `claude --version` runs and sign-in succeeds.
- The project is in Git and the current state is committed.
- A short `CLAUDE.md` that fits the project.
- Reading of sensitive files is blocked with `permissions.deny`.
- You have tried a read-only task and a task in plan mode before letting it edit files.
## Quick questions
**Do I need to know programming?** Not required, but you need to be able to read the changes or have someone check for you. Do not put results into a real environment without understanding what it did.
**Where does my data go?** The content of the files and commands Claude Code handles is sent to Anthropic for the model to reply. See the official data policy and remove sensitive files from its scope as in Step 4.
**How is it different from ordinary chat?** Claude Code works directly in the project folder and can run commands, while chat only replies in text. See also [Claude's working modes: how do chat, code and collaboration differ?](cac-che-do-lam-viec-cua-claude-chat-code-va-cong-tac-khac-nhau-ra-sao.html).
## Read next
- [Claude Code for free through Ollama: understanding the limits and model choices](claude-code-mien-phi-qua-ollama-hieu-dung-gioi-han-va-lua-chon-mo-hinh.html)
- [Claude Code AI SEO with Netlify and MCP: a content publishing workflow](claude-code-ai-seo-voi-netlify-va-mcp-workflow-xuat-ban-noi-dung.html)
- [Claude's working modes: how do chat, code and collaboration differ?](cac-che-do-lam-viec-cua-claude-chat-code-va-cong-tac-khac-nhau-ra-sao.html)
*Claude Code's commands and interface change with each version. Check the official Anthropic documentation before following along.*
