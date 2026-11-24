---
title: Setting up Hermes Workspace: a working base for AI agents
desc: Install Hermes Workspace, a community web interface for Hermes Agent: requirements, four install methods, variables, ports, remote security and checks.
min: 8
---
QUICK: Hermes Workspace (repo `outsourc-e/hermes-workspace`, MIT license) is a community web interface that sits in front of Hermes Agent. It needs Node.js 22, pnpm and a running Hermes gateway on port 8642. Running locally is simple; exposing it beyond your network requires setting a password.
## What Workspace is and is not
Hermes Workspace is a web app written by the community (version 2.3.0 when I read it), not a Nous Research product. The README describes it as the interface while Hermes Agent is the brain, with the two talking over HTTP. Main features: streaming chat with tool display, memory management, a skills browser, an MCP page, a file browser with the Monaco editor, a terminal, a multi-agent control board, Conductor and Swarm modes, interface themes, and installation as a progressive web app (PWA). It also has a "portable mode" that works with any OpenAI-compatible server, in which case only chat works.
## Requirements
- Node.js 22 or later and pnpm.
- A Hermes Agent gateway or an OpenAI-compatible server. It does not pin a specific Hermes version; the README recommends the latest.
- Python 3.11 or later if you want to run the Hermes gateway locally.
- Docker and Docker Compose if you use the Docker method.
## Ports
- `3000`: the Workspace interface (change with the `PORT` variable).
- `8642`: the Hermes gateway (chat, models, tasks).
- `9119`: the Hermes dashboard (sessions, skills, config, MCP).
## Enable the API server on the Hermes side
The gateway side needs `API_SERVER_ENABLED=true` (required). If you want access from another machine, add `API_SERVER_HOST=0.0.0.0` together with `API_SERVER_KEY` for authentication. The README says the gateway refuses to start if you open `0.0.0.0` without a key. This is also how [Hermes Open WebUI with Docker and Ollama: an internal AI interface](hermes-open-webui-voi-docker-va-ollama-dung-giao-dien-ai-noi-bo.html) connects.
## Method 1: one-line install (macOS, Linux)
```
curl -fsSL https://raw.githubusercontent.com/outsourc-e/hermes-workspace/main/install.sh | bash
hermes gateway run
cd ~/hermes-workspace && pnpm dev
```
The last two commands run in two different terminals. Before running a downloaded script, open and read it.
## Method 2: attach to an existing Hermes
```
git clone https://github.com/outsourc-e/hermes-workspace.git
cd hermes-workspace
pnpm install
cp .env.example .env
echo 'HERMES_API_URL=http://127.0.0.1:8642' >> .env
echo 'HERMES_DASHBOARD_URL=http://127.0.0.1:9119' >> .env
pnpm dev
```
## Method 3: Docker Compose
```
cp .env.example .env
docker compose up
```
There is also a prebuilt image `ghcr.io/outsourc-e/hermes-workspace:latest` (port 3000) for platforms such as Coolify, Easypanel, Dokploy and Unraid.
## Method 4: Windows
The README has a PowerShell script that runs through WSL: `.\scripts\start-hermes-workspace.ps1` (add `-Restart` to restart). The project also has a separate Windows guide in the docs folder.
## Main environment variables
- `HERMES_API_URL`: the gateway address, default `http://127.0.0.1:8642`.
- `HERMES_DASHBOARD_URL`: the dashboard address, default `http://127.0.0.1:9119`.
- `HERMES_API_TOKEN`: the gateway token, which must match `API_SERVER_KEY` on the Hermes side.
- `HERMES_PASSWORD`: the interface password; **required** when not listening on `127.0.0.1`.
You can set the address at runtime in Settings, Connection.
## Checking
```
curl http://127.0.0.1:8642/health
curl http://127.0.0.1:9119/api/status
```
The first command should return a healthy status. If it is not up, check that the gateway is running and `API_SERVER_ENABLED` is on.
## Using a local model
The README explains how to point `HERMES_API_URL` at Ollama (`OLLAMA_ORIGINS=* ollama serve`, then `HERMES_API_URL=http://127.0.0.1:11434 pnpm dev`). In this mode without the gateway (portable), sessions, memory and skills show "Not Available". For full functionality you must go through the Hermes gateway.
## Security warnings from the README
- Opening `0.0.0.0` without `HERMES_PASSWORD` makes Workspace refuse to run.
- `COOKIE_SECURE=0` sends the session cookie over plain HTTP; use it only on a trusted LAN.
- `GATEWAY_ALLOW_ALL_USERS=true` removes the allowed-user list on the gateway.
- `TRUST_PROXY=1` only when behind a proxy that sanitizes forwarded headers.
- `HERMES_ALLOW_INSECURE_REMOTE=1` turns off the safeguard when exposed to the outside; the README does not recommend it.
The interface has a terminal and a file editor, which means anyone who gets in controls your machine. Remote access should go through Tailscale or a VPN.
## Next steps
To run several workers at once, see [Setting up an agent swarm in Hermes Workspace step by step](thiet-lap-agent-swarm-trong-hermes-workspace-tung-buoc.html). For a more architectural view, see [Hermes Agent Workspace: a developer's view of architecture and performance](hermes-agent-workspace-goc-nhin-developer-ve-kien-truc-va-hieu-nang.html). A lighter community interface is [Hermes WebUI: build a chat interface for your agent in a few steps](hermes-webui-dung-giao-dien-chat-cho-agent-trong-vai-buoc.html).
