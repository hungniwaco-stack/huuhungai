---
title: Claude Code for free through Ollama: understanding the limits and model choices
desc: How to run Claude Code with another model through Ollama per the official docs: launch command, environment variables, model choice and the limits to know.
min: 7
---
QUICK: Claude Code can use a model run through Ollama instead of an Anthropic model. The quickest way is the command `ollama launch claude`. It costs nothing per use when run locally, but you trade for quality, tool-calling ability and some features that may be weaker, so "free" needs to be understood correctly.
## How it works
Ollama supports an interface compatible with the Anthropic Messages API. Because of that, Claude Code, which calls Anthropic's API, can be pointed at a different server with environment variables. The software you use is still Claude Code, but the "brain" behind it is the model you choose in Ollama. This is the official way Ollama documents.
## Installing Claude Code and Ollama
Install Claude Code following the guide in [Setting up Claude Code step by step: the foundation for AI coding](thiet-lap-claude-code-tung-buoc-nen-tang-cho-coding-bang-ai.html), and install Ollama from ollama.com. Ollama's documentation gives the Claude Code install command as:
```
# macOS, Linux
curl -fsSL https://claude.ai/install.sh | bash

# Windows (PowerShell)
irm https://claude.ai/install.ps1 | iex
```
## Method 1: Quick launch
Once you have Ollama, a single command starts Claude Code with Ollama:
```
ollama launch claude
```
The command will guide you through choosing a model. The documentation also gives a non-interactive way for scripts, with the `--model` and `--yes` flags, where `--yes` must be used together with `--model`.
## Method 2: Manual configuration for a model running on your machine
Set three environment variables and then run Claude Code with the model name:
```
export ANTHROPIC_AUTH_TOKEN=ollama
export ANTHROPIC_API_KEY=""
export ANTHROPIC_BASE_URL=http://localhost:11434
claude --model model-name
```
The `ANTHROPIC_AUTH_TOKEN` variable only needs to have a value; Ollama does not check it. On Windows PowerShell, use `$env:NAME = "value"` instead of `export`.
## Method 3: Use Ollama's cloud models
You can also use cloud models (names with the suffix `:cloud`) through Ollama without downloading them to your machine. The documentation also describes connecting directly to `https://ollama.com` with an Ollama API key, set in the `ANTHROPIC_AUTH_TOKEN` variable. With this method the model does not run on your machine, so terms of use, limits and costs are set by the service. Check Ollama's pricing page before relying on it.
## Choosing a model: two required conditions
Ollama's documentation states two requirements for a locally run model:
- **Tool calling support.** Claude Code works by calling tools (reading files, editing files, running commands). A model that does not support this can only chat.
- **A context window of at least 64,000 tokens.** A large project needs a large context so the agent can read enough code.
For a large project, set the context length to 64,000 or more. A weak machine struggles to meet both conditions at once, which is why many people see slow or poor results.
## What "free" means and does not mean
- **True:** running a model locally has no per-token fee, and content does not have to be sent to an outside service for processing.
- **Not quite:** you use electricity, hardware and time. A large model needs a powerful machine.
- **Cloud models:** may have limits or fees, depending on your Ollama plan.
- **Different quality:** a small model running on a personal machine is usually weaker than top models at complex coding, and results will differ from using Claude.
## Limits and notes per Ollama's documentation
- Web search provided by the hosted service and some advanced tool controls are **not fully supported** when connecting directly to the cloud. Basic chat and file editing work with compatible models.
- **Claude's settings can override environment variables.** If you change the address or credentials, update them in Claude's configuration files too, then run `/status` to check the connection.
- Claude Code still asks permission for most actions. A fully automatic mode needs allow rules or the permission-skipping flag, and that flag should only be used in an isolated environment.
## When this approach is worth it
- You want to try Claude Code without configuring a subscription, or work with source code that cannot be sent out.
- The work is simple and clear, such as small fixes, explaining code and writing tests.
- You accept being slower and having to check more carefully.
If you need the highest quality for complex work, use Anthropic's models. To build a working environment that does not depend on the network at all, see [Claude Code local: setting up an offline environment for AI coding](claude-code-local-thiet-lap-moi-truong-offline-cho-lap-trinh-bang-ai.html).
