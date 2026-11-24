---
title: Claude Code local: setting up an offline environment for AI coding
desc: Set up an AI coding environment that runs locally with Claude Code and Ollama: preparation, raising the context, step-by-step checks and what offline means.
min: 7
---
QUICK: To work almost offline, you install Claude Code and Ollama in advance, download a model that supports tool calling with a context of at least 64,000 tokens, then point Claude Code at Ollama on your machine. Installing and downloading the model still need the internet; only afterward can it run without a network, and some features such as web search will not work.
## What "offline" really means
This is where it is easy to misunderstand. Running locally means the model reasons on your machine, so code content does not leave to be processed. But:
- You still need the internet when **installing** tools and **downloading** the model.
- Features that need the network, such as web search, will not work.
- You should check for yourself whether the tools make any other background network connections (updates, telemetry), because this depends on the version and configuration.
If your requirement is absolutely no outbound connection, verify it by monitoring network traffic instead of trusting the name.
## Step 1: Prepare the hardware
The larger the model, the more memory it needs. Nous Research's guide to running agents locally gives a reference: about 8 GB of RAM for a model of about 3 billion parameters and 32 GB or more for models of 27 billion parameters and up, while an NVIDIA graphics card with 8 GB or more of its own memory is noticeably faster. Compare against the sizes listed on each model's page in the Ollama library.
## Step 2: Install the components (while you still have a network)
1. Install Claude Code, see [Setting up Claude Code step by step: the foundation for AI coding](thiet-lap-claude-code-tung-buoc-nen-tang-cho-coding-bang-ai.html).
2. Install Ollama from ollama.com and check:
```
ollama --version
```
1. Download the model you choose:
```
ollama pull model-name
```
Choose a model that **supports tool calling**, because Claude Code works through tools. Ollama's documentation requires a context of at least 64,000 tokens for this.
## Step 3: Raise the context length
The Hermes Agent guide notes that Ollama defaults to a very short context (2048 tokens), not enough to use tools. You can create a version of the model with a larger context using a Modelfile:
```
cat > Modelfile << 'EOF'
FROM model-name
PARAMETER num_ctx 64000
EOF
ollama create model-name-64k -f Modelfile
```
The default value may differ by Ollama version, so check with `ollama show model-name`. The longer the context, the more memory it uses, so choose just enough.
## Step 4: Point Claude Code at Ollama
The quick way per Ollama's documentation:
```
ollama launch claude
```
Or set environment variables manually:
```
export ANTHROPIC_AUTH_TOKEN=ollama
export ANTHROPIC_API_KEY=""
export ANTHROPIC_BASE_URL=http://localhost:11434
claude --model model-name-64k
```
After it runs, use `/status` in Claude Code to be sure it is connected to the right place. The documentation notes that Claude's configuration files can override environment variables.
## Step 5: Check in order
1. Disconnect the network (or turn on airplane mode) and ask a simple question. If it answers, the local path works.
2. Hand over a read-only task: "Explain the structure of this folder, do not edit files."
3. Hand over a small change in plan-only mode and then review it.
4. Run the project's test commands again to be sure the change broke nothing.
## Keep the model ready
Ollama can unload a model from memory after a period of not being used, making the next question slow. Hermes's guide describes how to keep the model loaded longer with the `keep_alive` parameter or the `OLLAMA_KEEP_ALIVE` variable. Use `ollama ps` to see which model is loaded.
## What you will not have
- Web search and features that need an online service.
- Quality on par with top models. A small local model is usually weaker at multi-step work and large codebases.
- Speed like a cloud service, especially on CPU only.
## Security and safety
Running locally does not make the agent safer when it comes to editing files. Keep the same habits: the project in Git, start in plan-only mode, block reading secret files with deny rules, and do not use the flag that skips all permissions outside an isolated environment. See also [Claude Code for free through Ollama: understanding the limits and model choices](claude-code-mien-phi-qua-ollama-hieu-dung-gioi-han-va-lua-chon-mo-hinh.html).
