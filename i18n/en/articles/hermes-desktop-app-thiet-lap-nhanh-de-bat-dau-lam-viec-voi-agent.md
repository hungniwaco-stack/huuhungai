---
title: Hermes Desktop App: quick setup to start working with the agent
desc: Hermes Desktop: install on Windows, macOS or Linux, connect locally or remotely, the main features, updating, uninstalling and the security warnings to know.
min: 7
---
QUICK: Hermes Desktop is the desktop app for Hermes Agent, sharing configuration, keys, sessions, skills and memory with the command-line version. Install with a downloaded package, choose a model provider on the first run and then chat. By default it runs a local gateway on your machine.
## What Desktop is
According to the documentation, Hermes Desktop is a native app for macOS, Windows and Linux, built around the very same agent as the CLI version and the gateway. This means what you set up in the terminal shows up in the app and vice versa. It is not a second agent.
## Installation
- **macOS (Apple Silicon chips):** open the DMG file and drag `Hermes.app` into Applications.
- **Windows:** open the `.appinstaller` file with Windows App Installer.
- **Already installed Hermes by command line:** run `hermes desktop`; the app uses your existing configuration, keys, sessions and skills.
The Desktop package has no build prerequisites. Download from the official Hermes Agent home page. If you have nothing yet, see [Installing Hermes Agent simply: a guide for non-technical people](cai-hermes-agent-don-gian-huong-dan-cho-nguoi-khong-chuyen-ky-thuat.html).
## The first run
The app may install the agent core into the `HERMES_HOME` folder. The welcome screen takes you to your first message as quickly as possible, and you may choose "Choose provider later" if you do not want to configure a provider yet. Interface choice: Basic starts in Simple mode, Elite starts in Advanced mode.
## Three kinds of connection
In Settings, the Gateways section:
- **Local (default):** the app runs `hermes gateway ensure` for the profile in use. The gateway keeps running after you quit the app.
- **Remote gateway:** enter the address of a `hermes serve` backend that you run yourself (for example in the form `http://<host>:9119`) and then sign in. The app does not start that backend itself.
- **Hermes Cloud:** sign in and choose an agent in your account, with no address needed.
About signing in: username and password should only be used on a trusted network; OAuth through Nous Portal is recommended for anything facing the internet.
## Main features
- **Chat:** streaming responses, tool activity display, drag-and-drop attachments, a preview pane on the right, find in page (Ctrl or Cmd + F), a message queue.
- **Status bar:** a per-session YOLO toggle, a context usage meter, options to show cache hits and tokens per second.
- **Model selection:** right in the compose box. The default model is set in Settings, Model, Main model and then Apply. Subagents have their own section at Settings, Model, Subagents.
- **Coding tools:** a file browser, a terminal (Ctrl + `), a Git view (Ctrl or Cmd + G), worktrees (Ctrl or Cmd + Shift + B).
- **Other:** Artifacts, a memory graph, Quick Entry with a global shortcut (default Ctrl or Cmd + Shift + Space), voice, HUD mode (a floating bar that stays on top).
- **Bot Mode:** each profile appears as a bot with its own chat and scheduled tasks.
- **Management panels:** skills, cron, profiles, messaging, providers.
- **Webapp:** turn it on with `hermes config set webapp.enabled true`, restart the gateway with `hermes gateway restart`, then run `hermes webapp` to open the workspace in the browser.
## Updating and uninstalling
The app checks for new versions in the background and offers one-click updates. Anonymous GitHub queries are rate-limited by network address; the app can use `GITHUB_TOKEN`, `GH_TOKEN` or a GitHub CLI sign-in session to relax the limit. With a remote gateway, "Update now" updates the backend first and then the app.
Uninstalling is at Settings, About, Danger zone, with three levels: remove only the interface, remove the interface and the agent but keep data, or remove everything.
## Warnings to know
- **The Webapp has server-level permissions:** a signed-in user can run commands under the account running Hermes. Do not expose it outside without a sign-in provider.
- **Plain HTTP** loses features that need a secure context such as the microphone, clipboard reading and notifications (loopback addresses are exempt).
- **Desktop plugins do not run in a sandbox**, they have the app's full permissions. Install only plugins you trust.
- **Switching the model mid-session** loses the cache, and the next turn may cost more.
- A remote backend must be kept running by you, and on Linux minimizing to the system tray needs a suitable tray component.
## How to use Desktop sensibly
Start in local mode, with one profile, in a test folder. Once you are comfortable, try Bot Mode and Kanban, see [Hermes AI course: understanding multi-agent, profiles and fallback chains](hermes-ai-course-hieu-multi-agent-profile-va-fallback-chain.html).
