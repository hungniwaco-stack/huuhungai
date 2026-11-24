---
title: Installing Hermes Agent simply: a guide for non-technical people
desc: Install Hermes Agent without technical skills: download the desktop app on Windows or macOS, choose a model provider, hold a first chat and fix common errors.
min: 6
---
QUICK: The easiest way is to download Hermes Desktop for Windows or macOS (Apple Silicon chips), install it like ordinary software, choose a model provider and type your first question. No command line is needed. If you want to use a terminal, a single install command is enough.
## What Hermes Agent is
Hermes Agent is Nous Research's open-source agent. It is not a language model but software that orchestrates models: it takes a request, chooses tools (read files, run commands, search the web), remembers information across sessions and can message through Telegram and Discord. You still need a language model for it to "think", either from a paid provider or running on your own machine.
## Preparation
- A machine running Windows, macOS (Apple Silicon only, Intel Macs are not supported) or Linux.
- A stable network connection.
- A way to use a model: a Nous Portal account, a ChatGPT or Codex plan, or an Anthropic or OpenRouter API key. Hermes recommends Nous Portal as the simplest choice.
- The model must have a context of at least 64,000 tokens, otherwise Hermes refuses right at startup.
## Method 1: install the desktop app (recommended for newcomers)
The official documentation recommends this for Windows and macOS.
1. Go to the Hermes Agent home page (`hermes-agent.nousresearch.com`) and download the desktop installer. Make sure you are on the right domain; the documentation has a separate page about the official domain to avoid fake versions.
2. Windows: open the `.appinstaller` file with Windows App Installer. macOS: open the DMG file and drag `Hermes.app` into the Applications folder.
3. Open the app. The first time, it may install the agent's core automatically. Follow the welcome screen.
4. Choose a model provider. If you do not want to yet, you can choose "Choose provider later" and come back afterward.
5. Choose the interface. Basic mode starts in a simple form, Elite mode starts in an advanced form.
For details on the app's features, see [Hermes Desktop App: quick setup to start working with the agent](hermes-desktop-app-thiet-lap-nhanh-de-bat-dau-lam-viec-voi-agent.html).
## Method 2: install with one command
If you are comfortable with a terminal:
```
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```
This command is for Linux, macOS and WSL2. On Windows (PowerShell):
```
iex (irm https://hermes-agent.nousresearch.com/install.ps1)
```
After installing, reopen the terminal and type `hermes`. If there is a problem, run `hermes doctor` to diagnose and `hermes config check` to check the configuration.
## Choosing a model provider
Run `hermes model` to choose through a question-and-answer screen. The first four options the documentation suggests:
- **Nous Portal:** one subscription, little configuration.
- **OpenAI Codex:** uses the ChatGPT or Codex plan you already have.
- **Anthropic:** Claude through OAuth or an API key. Note that a Claude Pro plan cannot sign in to Hermes; a Max plan can only use the extra usage credit you buy.
- **OpenRouter:** many models through one key.
Secret keys are stored in `~/.hermes/.env`, and other settings are in `~/.hermes/config.yaml`. Do not share these two files.
## The first conversation
Use something easy to verify, for example ask it to summarize a folder you specify and say what the main files are. Signs it is working well: the status bar shows the right model, Hermes answers without errors, uses tools when needed and remembers the thread of conversation across several turns. To return to a previous session, type `hermes --continue`.
## Common errors
- **Empty replies or strange errors:** usually a wrong provider, model or key. Run `hermes model` again.
- **The messaging bot runs but does not respond:** the token or the allowed-user list is incomplete; run `hermes gateway setup` then `hermes gateway status`.
- **Cannot continue an old session:** you may be in a different profile; see `hermes sessions list`.
The troubleshooting order the documentation suggests: `hermes doctor`, `hermes model`, `hermes setup`, `hermes sessions list`, `hermes --continue`, `hermes gateway status`.
## Staying safe when you are new
The agent can run commands and read files on your machine, so do not give it a folder with important data until you are familiar with it. Start in a separate test folder. To run entirely on your machine without per-use fees, see [A free local AI agent with Hermes and Ollama: when to use it](ai-agent-local-mien-phi-voi-hermes-va-ollama-khi-nao-nen-dung.html).
