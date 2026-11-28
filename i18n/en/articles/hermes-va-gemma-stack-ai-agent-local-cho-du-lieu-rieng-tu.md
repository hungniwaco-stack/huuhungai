---
title: Hermes and Gemma: a local AI agent stack for private data
desc: Build a local AI agent with Hermes, Ollama and Gemma for private data: machine requirements, configuration and where data can still leave your machine.
min: 7
---
QUICK: Hermes Agent combined with Ollama and a Gemma model running on your machine lets the reasoning stay on the machine, so it suits sensitive data. But "private" is only true for the model part. Web search tools, messaging bots and cloud fallbacks can still send data out, so you need to review each exit.
## Why choose a local stack
When the model runs with Ollama on your machine, the content you give it is not sent to any model provider. That is the main reason to choose it: customer records, internal documents, unpublished source code. The second benefit is no per-use fee (though you still spend on hardware and electricity).
## Gemma in Hermes's guide
Nous Research's "Run Hermes Locally with Ollama" guide uses the Gemma model `gemma4:31b` as its example for agent work. They say it is the only model in their list that calls tools reliably, while the smaller models can only chat. The hardware levels the documentation gives: about 32 GB of RAM or more for models of 27 billion parameters and up; 8 GB of RAM for a model of about 3 billion; at least 5 GB of free disk, and 30 GB if you try several models.
The installation steps, configuring the `http://localhost:11434/v1` endpoint and raising the context to 64,000 tokens are described in detail in [A free local AI agent with Hermes and Ollama: when to use it](ai-agent-local-mien-phi-voi-hermes-va-ollama-khi-nao-nen-dung.html). Two points to remember: Hermes requires a minimum context of 64,000 tokens and the model must support tool calling.
## Review the data paths that can leave the machine
Look at the agent as software with many exits:
1. **The fallback model.** If you configure `fallback_providers` to a cloud service, then when the local model fails that turn's content will be sent out. For sensitive data, drop the cloud fallback or only allow a fallback to a server of your own.
2. **Web search and extraction tools.** A search query is a form of data leaving the machine. Turn off the web toolset or enable it only for public work.
3. **Messaging channels.** If you chat with the agent through Telegram or Discord, the content passes through that platform. Message from the local app if you need to be fully sealed.
4. **Auxiliary tasks.** The documentation says auxiliary tasks such as looking at images and compressing context use the main model by default, but can be configured separately. Check the configuration to be sure they do not point out to another service.
5. **MCP and plugins.** An MCP server can call outside services. Install only what you understand.
6. **Logs and memory on disk.** Sessions, memory and logs are stored in `~/.hermes/`. This data sits on your machine, but if the machine is backed up to the cloud it goes along too. Consider disk encryption.
## Limits of this approach
- **Quality.** A model that can run on a personal machine is usually smaller than a top model, and more likely to err on multi-step tasks.
- **Speed.** The documentation warns that the first response can stay silent for a long time on CPU only or with little graphics card memory.
- **Easy to misconfigure.** On machines with little VRAM, Ollama defaults to a small context; if you forget to raise it, tools will fail or the model will print tool commands as text.
- **The agent's permissions.** Even running locally, the agent still has your account's permissions (a profile is not a sandbox). If you hand it sensitive data, consider running the terminal backend in Docker and mounting only the folder needed.
## A practical model: classify data
The easiest way to be both private and usable is to split by sensitivity:
- Sensitive data: a local profile, no cloud fallback, web tools off.
- Public data: a profile that uses the cloud, with a stronger model.
These two profiles are kept separate by creating separate profiles (see [Hermes AI Course: understanding multi-agent, profiles and fallback chains](hermes-ai-course-hieu-multi-agent-profile-va-fallback-chain.html)). A fuller local-versus-cloud comparison framework is in [Ollama and Hermes: when does a local AI agent beat the cloud?](ollama-va-hermes-khi-nao-local-ai-agent-tot-hon-cloud.html).
## Check before you trust
Before handing over real data, run a trial task with fake data and watch the process's network traffic to confirm there are no unintended outbound connections. For data under legal constraints, ask the person in charge of compliance first; this article is not legal advice.
