---
title: Setting up Aion UI with OpenClaw: a control interface for agents
desc: Aion UI is an open-source desktop app that runs OpenClaw, Claude Code, Codex and other agents together: install, agent detection, MCP sync, WebUI, notes.
min: 7
---
QUICK: Aion UI (repo `iOfficeAI/AionUi`, Apache-2.0 license) is a desktop app that brings many agents into one interface: it has a built-in agent and automatically detects installed CLIs such as OpenClaw, Claude Code and Codex. Install it from a release or with `brew install aionui` on macOS. Data is stored locally in SQLite.
## What Aion UI is
The project README describes a free, open-source "Cowork" app: the agent works on your machine (reads files, writes code, browses the web, automates tasks) and you approve its actions. The app has its own built-in agent and can also run external agent CLIs in the same interface. It is a community project, not a product of the OpenClaw Foundation. For the official OpenClaw build, see [Installing OpenClaw](cai-openclaw-desktop-app-cach-bat-dau-voi-ai-agent-giao-dien-sach.html).
## Requirements
- macOS 10.15 or later, Windows 10 or later, or Linux (Ubuntu 18.04 or later, Debian 10 or later, Fedora 32 or later).
- At least 4 GB of RAM recommended, with at least 500 MB of free disk space.
## Installation
- Download the installer for your operating system from the Releases page of the `iOfficeAI/AionUi` repo.
- On macOS you can use Homebrew:
```
brew install aionui
```
The README lists no other package managers. Searching shows many forks with the same description; use the original `iOfficeAI` repo.
## Agent detection and OpenClaw
Aion UI automatically scans for CLI tools installed on your machine. The README says that if you use Claude Code, Codex, Hermes Agent or OpenClaw, the app recognizes them and lets them work alongside the built-in agent; it also lists Gemini CLI, OpenCode, Cursor Agent and about 20 other agents. A community guide also says the app has a setup assistant for OpenClaw. The number of supported agents differs between sources, so check the list in the main repo. To use OpenClaw through Aion UI, you must first install it and get it running.
## Main features according to the README
- **Multi-agent mode:** parallel sessions, each with its own context. **Team mode:** a Leader agent splits work among Teammate agents that share a workspace.
- **MCP management in one place:** you configure MCP tools and Aion UI injects or syncs them into each agent according to its capabilities.
- **Models:** more than 30 providers, including Gemini, Anthropic and OpenAI, plus local ones such as Ollama and LM Studio.
- **Scheduled tasks:** hourly, periodic or one-time, running unattended.
- **Preview pane** for more than 10 formats (PDF, Office, code, images).
- **Remote access through WebUI:** it runs as its own HTTP server, with sign-in by QR code or password, usable on a LAN, over the internet or on a server.
- **Chat channels:** Telegram, Lark (Feishu), DingTalk, WeChat; WeCom, Slack and Discord are listed as coming soon.
## Data and security
The README says all data is stored locally in a SQLite database and is not uploaded to any server. That only describes the app; the model you choose still receives the content you send. With the remote WebUI, use a strong password and prefer a private network or VPN, because this interface controls agents that can run commands on your machine.
## When to use it
It suits you if you use several agents and want one shared interface. If you only use OpenClaw, the official interface (Control UI) or [ClawX](ngay-dau-voi-clawx-openclaw-nen-kiem-tra-gi-truoc-khi-dung-that.html) may be enough. Also consider that adding another software layer adds one more thing to update and trust, so do not install all three interfaces at once.
