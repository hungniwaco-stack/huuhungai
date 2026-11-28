---
title: A free local AI agent with Hermes and Ollama: when to use it
desc: Run Hermes Agent with an Ollama model on your machine to avoid per-use fees: steps from the official docs, the real limits and when it is worth it.
min: 8
---
QUICK: Hermes Agent is Nous Research's open-source agent and can use a model run by Ollama on your machine, so there is no per-use charge. The conditions are a capable machine, a model that can call tools and a context of at least 64,000 tokens. If one of the three is missing, the agent will be slow or only able to chat.
## What Hermes Agent is, briefly
According to the official documentation, Hermes Agent is Nous Research's agent, described as self-improving: it creates skills from experience, keeps memory across sessions, and has scheduled tasks and subagents. It is not a language model but software that orchestrates models. Hermes works with many model providers (Nous Portal, OpenRouter, OpenAI and any endpoint) and can connect to messaging platforms such as Telegram and Discord.
## What "free local" means
When the model runs with Ollama on your machine, you pay no per-token fees. But "free" here only means no per-use bill. You still spend on hardware and electricity, and if the machine is not powerful enough, the experience will be so poor it is unusable.
## Requirements per the Hermes documentation
The "Run Hermes Locally with Ollama" guide gives these minimums:
- RAM: 8 GB for a model of about 3 billion parameters, 32 GB or more for models of 27 billion parameters and up.
- Free disk: 5 GB minimum, 30 GB or more if you use several models.
- A 4-core CPU minimum, 8 cores or more recommended.
- An NVIDIA card with 8 GB or more of its own memory is optional but makes it noticeably faster.
## Setup steps
1. **Install Ollama and check:**
```
curl -fsSL https://ollama.com/install.sh | sh
ollama --version
curl http://localhost:11434/api/tags
```
1. **Download a model.** The guide recommends `gemma4:31b` for agent work, because they say it is the only model in their list that calls tools reliably. The smaller models in the guide can only chat.
```
ollama pull gemma4:31b
```
1. **Configure Hermes.** Run `hermes setup`, choose Custom Endpoint and enter the Base URL `http://localhost:11434/v1`, leave the API key blank (or `no-key`), and set the model name. Or edit `~/.hermes/config.yaml`:
```
model:
  default: "gemma4:31b"
  provider: "custom"
  base_url: "http://localhost:11434/v1"
```
1. **Raise the context.** Hermes needs at least 64,000 tokens to use tools. The Hermes guide says Ollama defaults to 2048 tokens, but Ollama's documentation now says the default depends on VRAM (4k, 32k or 256k). Either way, set at least 64,000 explicitly. The guide shows how to create a Modelfile with `PARAMETER num_ctx 64000` and then `ollama create`. Then use the new model name in the configuration.
2. **Run:** type `hermes`.
## Common problems (per the documentation)
- **The first response stays silent for a long time:** the model is processing the system prompt and the tool list, especially on CPU only. Keeping the model loaded in memory reduces this.
- **The model prints tool JSON as text instead of running it:** the server running the model has not parsed the tool call correctly.
- **Context length errors:** redo the context-raising step.
- **Slow because of too little RAM:** the model is too large for the machine, so choose a smaller one.
## When to use this approach
- Sensitive data you do not want to send to an outside service.
- You already have a capable machine and want to avoid per-use costs.
- The work is simple to moderate and you accept slower results.
- You want to learn, experiment and understand how agents work.
## When not to
- A weak machine or no graphics card, but you need fast responses.
- Work that needs high accuracy or many complex steps, where a small model easily errs.
- You need the agent to run stably for many users at once.
The Hermes documentation also describes how to configure a fallback to a cloud provider when the local model cannot cope. This combination is discussed in detail in [Ollama and Hermes: when does a local AI agent beat the cloud?](ollama-va-hermes-khi-nao-local-ai-agent-tot-hon-cloud.html). If you want a web chat interface, see [Hermes Open WebUI with Docker and Ollama: an internal AI interface](hermes-open-webui-voi-docker-va-ollama-dung-giao-dien-ai-noi-bo.html).
