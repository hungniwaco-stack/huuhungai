---
title: OpenClaw and ByteRover: upgrading long-term memory for agents
desc: ByteRover is an external memory layer for OpenClaw: plugin install, setup, Context Engine, experimental Memory Flush and warnings about third-party scripts.
min: 7
---
QUICK: ByteRover is a third-party product that adds a structured memory layer to OpenClaw, installed with the `@byterover/byterover` plugin. Its documentation also gives a one-line install script, but when checked on Nov 28, 2026 that address redirected to the home page, so do not run it. Add ByteRover only when OpenClaw's built-in memory is not enough. The Memory Flush feature is still experimental.
## What ByteRover is
According to ByteRover's documentation, it is a long-term memory system for OpenClaw agents that helps the agent remember across sessions. It is not an OpenClaw feature but a separate product. Before adding it, understand OpenClaw's built-in memory in [Setting up long-term memory for OpenClaw: when it is needed and how to control it](thiet-lap-bo-nho-dai-han-cho-openclaw-khi-nao-can-va-lam-sao-kiem-soat.html): Markdown files, semantic lookup and dreaming. Many people will find that enough.
## Two main components
- **Context Engine:** retrieves relevant knowledge before each agent response and stores what it learns after each turn. It requires OpenClaw v2026.3.22 or later.
- **Memory Flush (experimental):** before context is compacted, the agent reviews the session for architectural decisions, bugs it fixed and repeated patterns, then runs `brv curate` to store them. The documentation page marks this feature as experimental and behavior may change.
There is also a ClawHub skill named `byterover`.
## Requirements
Node.js, and the `openclaw` command-line tool on your `PATH`. Per the documentation, the setup script installs `brv` (ByteRover's CLI) if it is missing and installs the `byterover` skill automatically.
## Installing per the documentation
- **Plugin only:**
```
openclaw plugins install @byterover/byterover
```
- Skill (the script installs it automatically): `npx clawhub@latest install byterover --force`.
**Update, Nov 28, 2026:** the documentation still tells you to download `byterover.dev/openclaw-setup.sh` and run it directly, but this address, like `byterover.dev/install.sh` (the `brv` installer), redirects with a 301 to the `byterover.ai` home page and returns an HTML page, not a script. The same paths on `byterover.ai` return 404. So do not pipe the download into `sh`; use the plugin install and check the latest documentation. I have not tested the plugin install. Per the documentation, once you have `brv`, you connect a model provider for ByteRover:
```
brv providers connect byterover
brv providers connect <llm-provider>
brv providers list
```
The `byterover` provider is free but needs you to sign in to a ByteRover account; other providers need your own API key.
## Warnings before installing
1. **Do not run a "download then run" command right away.** A `curl ... | sh` command runs code from the internet with your privileges. Always open the address and read it first: in this case what comes back is a web page, not a script.
2. **Cross-check the domain.** Some addresses on `byterover.dev` now redirect to `byterover.ai`, while the documentation is still on `docs.byterover.dev`. I found no official notice explaining this, so verify the domain yourself before running anything.
3. **OpenClaw's skill policy.** Installing skills from a third-party source may trigger warnings; the `openclaw skills` documentation describes install confirmation warnings, and `--force` does not override a block result.
4. **Where the data goes.** The documentation page I read does not say whether data is stored locally or in the cloud, and another summary says the data is local-first and may be pushed to the cloud when needed. Ask or read the policy before putting in source code or customer data.
## How to test in a controlled way
1. Back up OpenClaw's config and working folder.
2. Try it on a secondary agent, not one running important work.
3. Turn on only the Context Engine first; leave Memory Flush (experimental) for later.
4. Compare with the built-in memory on the same few questions about the past: does it remember correctly, remember too much or remember wrongly.
5. If there is no clear improvement, remove the plugin. Adding a memory layer adds one more thing to update and trust.
