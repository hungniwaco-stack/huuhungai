---
title: Day one with ClawX for OpenClaw: what to check before real use
desc: ClawX is a community desktop app wrapping OpenClaw: system requirements, install, first-time setup, main features and a checklist before real use.
min: 7
---
QUICK: ClawX (repo `ValueCell-ai/ClawX`) is a community desktop app under the MIT license that puts OpenClaw into a graphical interface and embeds the OpenClaw core inside. You download a release, run the first-time wizard and choose a model provider. Before using it for real work, check the download source, the agent's permissions and Computer Use mode (off by default).
## What ClawX is, and is not
The project README describes ClawX as a desktop interface for OpenClaw agents: run agent orchestration, chat, scheduled tasks, skills and channels from a graphical app instead of the terminal. It is a community project, not a product of the OpenClaw Foundation. The project says it is built on the official OpenClaw core, embeds the runtime in the app so it does not need a separately installed OpenClaw, and tries to stay close to the original. As a result, features may lag the official version by a step. For installing the official OpenClaw, see [Installing OpenClaw](cai-openclaw-desktop-app-cach-bat-dau-voi-ai-agent-giao-dien-sach.html).
## Requirements per the README
- **Operating system:** macOS 11 or later, Windows 10 or later, or Linux (Ubuntu 20.04 or later).
- **Memory:** at least 4 GB of RAM, 8 GB recommended. **Disk:** 1 GB free.
- **Computer Use** (screen control) is only on macOS 13 or later and Windows 10 or later (x64).
## Installation
**Recommended way:** download the release for your operating system from the Releases page of the `ValueCell-ai/ClawX` repo on GitHub. A GitHub search will return many forks with the same description; use the original repo, and if in doubt, check the address of the project's website.
**Build from source** (needs Node 24.16.0 or later, or 26.1.0 or later, and pnpm 9 or later):
```
git clone https://github.com/ValueCell-ai/ClawX.git
cd ClawX
pnpm run init
pnpm dev
```
On the first run, the Setup Wizard asks for your language and region, AI provider, skill bundles and a confirmation step.
## Model providers and keys
You can connect OpenAI, Anthropic, Z.AI (GLM) and custom providers in one shared panel or right in the wizard. Credentials are stored in the operating system's keychain. Providers that support browser or device sign-in can use OAuth instead of an API key. Advanced settings are under Settings, Advanced, Developer Mode; the proxy is under Settings, Gateway, Proxy.
## Main features
- **Chat:** multiple sessions, streaming Markdown display, calling agents with `@agent`, `/skill` skill cards, preview of Markdown, `.docx`, `.pptx` and local HTML.
- **Agent management**, **multi-account channels** (including WeChat, DingTalk), and **scheduled tasks** (cron) that send results to channels.
- **Skills:** local management with built-in document-handling skills for pdf, xlsx, docx and pptx.
- **Issue report export:** creates a ZIP file with filtered configuration and diagnostic logs.
- **Voice input** in Developer Mode, through a service you configure (such as OpenAI, Groq or a custom endpoint).
## Checklist before real use
1. **Is the download source right?** Download only from the original repo and its Releases page.
2. **Computer Use is off by default, leave it that way** until you understand it clearly. The README warns that screenshots may be sent to the model provider, so avoid leaving sensitive windows inside the capture frame.
3. **Tool permissions.** The README says the `web_search` tool and some agent tools (gateway, nodes, goal) are disabled by policy, and actions with consequences or that go outward should require confirmation. Check this in practice after installing; do not just trust the description.
4. **Upgrade snapshot files contain secrets.** The README warns that upgrade snapshots contain keys, so do not share them.
5. **Try a read-only task**, for example summarizing a test folder, before handing over write or send tasks.
6. **Follow updates.** The app prompts for updates, but you need to read the release notes yourself before clicking.
## When to use ClawX
It suits people who want a graphical interface for OpenClaw and do not want to touch a terminal. If you want to use several other agents together (Claude Code, Codex...), see [Aion UI](thiet-lap-aion-ui-voi-openclaw-giao-dien-dieu-khien-agent.html). If you only need a web control panel, the official Control UI is already available.
