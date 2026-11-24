---
title: Installing the OpenClaw Desktop App: how to start with a clean-interface AI agent
desc: Install OpenClaw on Windows, macOS or Linux: the desktop app, one-line install, onboarding steps, opening the Control UI and checking the Gateway runs well.
min: 7
---
QUICK: According to the official documentation, you can install OpenClaw with the desktop app (Windows Hub, the macOS menu bar app) or one install command. Then run onboarding, open the Control UI with `openclaw dashboard` and send a first message. The Gateway listens on port 18789 by default, and needs Node 24.16 or later, or Node 26.
## What OpenClaw is
OpenClaw is an open-source, self-hosted gateway that connects chat apps to AI agents. You run one Gateway process on your own machine, which is the source of truth for sessions, routing and channel connections. The project is maintained by the OpenClaw Foundation under the MIT license. This article is about how to install and run it the first time per the official documentation, not about community interfaces such as [Day one with ClawX for OpenClaw: what to check before real use](ngay-dau-voi-clawx-openclaw-nen-kiem-tra-gi-truoc-khi-dung-that.html) or [Setting up Aion UI with OpenClaw: a control interface for agents](thiet-lap-aion-ui-voi-openclaw-giao-dien-dieu-khien-agent.html).
## Requirements
- **Node:** 24.16.0 or later on the 24.x branch, or 26.1.0 or later. The documentation strongly recommends 24.22.1 or later, or 26.12.1 or later, for security reasons, and recommends Node 26.
- **Operating system:** macOS, Linux or Windows. On Windows you can use the native Windows Hub app, the PowerShell installer or a Gateway running in WSL2.
- **Model key:** a provider API key, or an existing Claude Code or Codex CLI sign-in (onboarding can reuse it).
- `pnpm` is only needed when you build from source.
## Method 1: the desktop app
- **Windows Hub (recommended on Windows):** x64 and arm64 installers are on OpenClaw's GitHub releases page, including setup, system tray status, chat and node mode. There is also a fallback Tauri app for Windows, the file `OpenClaw-<version>-windows-x86_64.exe` in the regular releases.
- **macOS:** download `OpenClaw-<version>.dmg` (preferred) or `.zip` from the releases page, install and open **OpenClaw.app** (a menu bar app).
Download from the project's official releases page on GitHub, and avoid copies.
## Method 2: the one-line installer (recommended in the documentation)
macOS, Linux and WSL2:
```
curl -fsSL https://openclaw.ai/install.sh | bash
```
Windows PowerShell:
```
iwr -useb https://openclaw.ai/install.ps1 | iex
```
To install without running onboarding right away, add `-- --no-onboard` (bash) or `-NoOnboard` (PowerShell). Other methods include `npm install -g openclaw@latest`, pnpm, bun, Docker, Podman, Nix or building from source; each has its own page in the documentation. To try it quickly without installing, there is the command `npx openclaw@latest`.
## Onboarding
The installer runs the wizard automatically. There are two choices:
- **Quick start:** automatically detects the AI access you already have, checks it with one real completion, saves the configuration and opens the web control panel. If no route works, it switches to manual provider setup.
- **Custom setup:** goes through all the options.
Quick start asks "Keep OpenClaw running in the background?". If you choose yes, the Gateway is installed as a background service; if no, the Gateway runs in the terminal until you press Ctrl+C. The configuration is saved either way. Change settings later with `openclaw configure`. If you installed with npm, the onboarding command is `openclaw onboard --install-daemon`.
## Checking after installing
```
openclaw --version
openclaw doctor
openclaw gateway status
```
`gateway status` must show the Gateway listening on port 18789. If the Gateway is not running: `openclaw gateway install` then `openclaw gateway start`. The `start` command waits until the Gateway passes its health check, and does not restart a Gateway that is already running.
## Open the interface and send a test message
```
openclaw dashboard
```
This command opens the Control UI in the browser with a one-time pairing link that expires after ten minutes. If the interface loads, you send the first message in the chat box and confirm there is an AI reply. Add `--no-open` if you only want to print the address in the terminal.
## When something goes wrong
`openclaw triage` runs read-only checks and creates a diagnostic prompt with keys, tokens and raw logs filtered out. Nothing leaves the machine until you choose an agent to handle it. `openclaw doctor` gives the same findings for you to read yourself. The Troubleshooting page arranges fixes by symptom.
## Safety notes when you are new
The Gateway controls an agent that can do real work on your machine, so keep it listening on loopback and use the default pairing mechanism for strangers who message it. The security documentation also has the command `openclaw security audit` to check your configuration. When you need remote access, see [Mission Control for OpenClaw: community dashboards and the official Control UI](openclaw-mission-control-quan-ly-agent-bang-dashboard-truc-quan.html). Update the version with `openclaw update` and take a backup before a major update, as described in [An OpenClaw learning path: how to keep up with new AI agent tools](lo-trinh-hoc-openclaw-cach-theo-kip-cong-cu-ai-agent-moi.html).
