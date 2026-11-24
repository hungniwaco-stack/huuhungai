---
title: OpenClaw and ByteRover: upgrading long-term memory for agents
desc: ByteRover is an external memory layer for OpenClaw: plugin install, setup, Context Engine, experimental Memory Flush and warnings about third-party scripts.
min: 7
---
QUICK: ByteRover is a third-party product that adds a structured memory layer to OpenClaw, installed with the `@byterover/byterover` plugin or a setup script. Add it only when OpenClaw's built-in memory is not enough for you. The accuracy figures are published by the vendor itself, and the Memory Flush feature is still experimental.
## What ByteRover is
According to ByteRover's documentation, it is a long-term memory system for OpenClaw agents that helps the agent remember across sessions. It is not an OpenClaw feature but a separate product. Before adding it, understand OpenClaw's built-in memory in [Long-term memory for OpenClaw](thiet-lap-bo-nho-dai-han-cho-openclaw-khi-nao-can-va-lam-sao-kiem-soat.html): Markdown files, semantic lookup and dreaming. Many people will find that enough.
## Two main components
- **Context Engine:** retrieves relevant knowledge before each agent response and stores what it learns after each turn. It requires OpenClaw v2026.3.22 or later.
- **Memory Flush (experimental):** before context is compacted, the agent reviews the session for architectural decisions, bugs it fixed and repeated patterns, then runs `brv curate` to store them. The documentation page marks this feature as experimental and behavior may change.
There is also a ClawHub skill named `byterover`.
## Requirements
Node.js, and the `openclaw` command-line tool on your `PATH`. The setup script installs `brv` (ByteRover's CLI) if it is missing and installs the `byterover` skill automatically.
## Installing per the documentation
- **Quick install with a script:**
```
curl -fsSL https://byterover.dev/openclaw-setup.sh | sh
```
- **Plugin only:**
```
openclaw plugins install @byterover/byterover
```
- Skill (the script installs it automatically): `npx clawhub@latest install byterover --force`.
The script checks prerequisites, backs up your config, then asks whether to turn on each feature (Context Engine, Memory Flush) and updates `AGENTS.md` and `TOOLS.md` with ByteRover commands. After that, connect a model provider for ByteRover:
```
brv providers connect byterover
brv providers connect <llm-provider>
brv providers list
```
The `byterover` provider is free but needs you to sign in to a ByteRover account; other providers need your own API key.
## Warnings before installing
1. **Do not run a "download then run" command right away.** The `curl ... | sh` command runs code from the internet with your privileges. Open the script address and read it first, or use the plugin-only method through `openclaw plugins install`.
2. **Cross-check the domain.** When I checked, an old blog page on `byterover.dev` redirected (301) to `byterover.ai`. The current documentation still uses `byterover.dev` for the install command. Verify the official domain yourself from ByteRover's documentation page before running anything.
3. **OpenClaw's skill policy.** Installing skills from a third-party source may trigger warnings; the `openclaw skills` documentation describes install confirmation warnings, and `--force` does not override a block result.
4. **Where the data goes.** The documentation page I read does not say whether data is stored locally or in the cloud, and another summary says the data is local-first and may be pushed to the cloud when needed. Ask or read the policy before putting in source code or customer data.
## Accuracy figures
One source says the ByteRover team published a LongMemEval-S score of 92.8%. That is a vendor-published number that I did not independently verify, and the aggregator sites that repeat it are often of low quality. Do not use it to decide; measure on your own real work.
## How to test in a controlled way
1. Back up OpenClaw's config and working folder.
2. Try it on a secondary agent, not one running important work.
3. Turn on only the Context Engine first; leave Memory Flush (experimental) for later.
4. Compare with the built-in memory on the same few questions about the past: does it remember correctly, remember too much or remember wrongly.
5. If there is no clear improvement, remove the plugin. Adding a memory layer adds one more thing to update and trust.
