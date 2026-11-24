---
title: Hermes WebUI: build a chat interface for your agent in a few steps
desc: Install Hermes WebUI, a community web interface for Hermes Agent: requirements, bootstrap or Docker, setting a password, safe remote access and known limits.
min: 7
---
QUICK: Hermes WebUI (repo `nesquena/hermes-webui`) is a community web interface, not a Nous Research product. Install it with `python3 bootstrap.py` or Docker and open `http://127.0.0.1:8787`. By default there is no password and it listens only on your machine; if you expose it to a network you must set a password and should go through an SSH tunnel or Tailscale.
## Do not confuse three things
- **Hermes WebUI** (this article): a community project by the author `nesquena`, a three-pane interface with sessions, chat and a working file panel.
- **The official dashboard (`hermes dashboard`):** made by Nous Research, used to manage configuration, sessions, keys and cron.
- **Open WebUI:** a standalone chat app that connects to Hermes's API server, see [Hermes Open WebUI with Docker and Ollama: an internal AI interface](hermes-open-webui-voi-docker-va-ollama-dung-giao-dien-ai-noi-bo.html).
The Hermes WebUI author states clearly that this is an independent project, not affiliated with or endorsed by Nous Research. There is also [Hermes Workspace](thiet-lap-hermes-workspace-nen-lam-viec-cho-ai-agent.html), another community interface.
## Requirements
- Hermes Agent installed (the bootstrap script will try to install it with the official installer if it is missing).
- Python 3.11 or later.
- Linux, macOS or WSL2. Native Windows is not supported by the bootstrap script; the README points to a Windows guide written by the community.
- Docker if you install with a container.
## Method 1: bootstrap (recommended by the README)
```
git clone https://github.com/nesquena/hermes-webui.git hermes-webui
cd hermes-webui
python3 bootstrap.py
```
The bootstrap script detects or installs Hermes Agent, creates a Python environment, starts the server, waits for `/health`, opens the browser (unless you add `--no-browser`) and runs the first-time setup wizard.
## Method 2: run in the background with ctl.sh
Suited to virtual machines or a homelab:
```
./ctl.sh start
./ctl.sh status
./ctl.sh logs --lines 100
./ctl.sh restart
./ctl.sh stop
```
The PID file is written to `~/.hermes/webui.pid` and the log to `~/.hermes/webui.log`.
## Method 3: Docker
```
git clone https://github.com/nesquena/hermes-webui
cd hermes-webui
cp .env.docker.example .env
docker compose up -d
```
Then open `http://localhost:8787`. The README also has a prebuilt image at `ghcr.io/nesquena/hermes-webui` and two- and three-container compose files. Note one known limitation: in the two-container setup, tools run in the WebUI container, not the agent container.
## Checking
```
curl http://127.0.0.1:8787/health
```
The default port is 8787 and the default listen address is `127.0.0.1`. You can change them with the `HERMES_WEBUI_PORT` and `HERMES_WEBUI_HOST` variables.
## Password and remote access
- Password authentication is **off by default**. Turn it on with the `HERMES_WEBUI_PASSWORD` variable or in Settings. You can add passkeys (WebAuthn) and optional OIDC sign-in.
- Sessions use an HTTP-only cookie valid for 24 hours.
- To use it from another machine, the README prefers **Tailscale Serve** (keeping the WebUI on loopback behind HTTPS available only inside your private network). Another simple way is an SSH tunnel:
```
ssh -N -L 8787:127.0.0.1:8787 user@host
```
- Exposing it directly (`HERMES_WEBUI_HOST=0.0.0.0` with a password) is considered only a last resort.
Because this interface controls an agent that can run commands on your machine, treat it as a door into your server, not just a web page.
## Main features according to the README
Streaming responses, tool and subagent cards, search, pinning and archiving sessions, Markdown or JSON import and export, a file tree with preview and editing, Git branch badges, a profile switcher, panels for Tasks (cron), Skills, Memory and Profiles, and voice input. The interface works on phones.
## Known limits
- The WebUI is tightly coupled to Hermes Agent's internals. The README advises upgrading the WebUI and Hermes Agent together, because mismatched version combinations are not tested.
- Some features depend on the backend, for example `/goal` returns a 501 code with a certain adapter.
- The README notes that a stable API boundary is still being worked on.
## When to use it
If you want to chat with the agent from a phone or another machine without using the desktop app, and accept one more community component to keep updated. If you only need administration, the official dashboard is enough.
