---
title: Running local models for OpenClaw: runtimes, configuration and risks
desc: Running local models for OpenClaw: choosing a runtime, custom provider config, context and tool-calling needs, checking each layer and small-model risks.
min: 8
---
QUICK: For OpenClaw to use a model running on your machine, you choose a runtime (llama.cpp, LM Studio, Ollama, vLLM...), declare it as a custom provider and check that the model can call tools. The documentation lists the runtime `ds4` for DeepSeek V4 Flash on macOS Metal. The main risk: a small model breaks multi-step work and has no safety filters like a cloud service.
## What "local gateway" means here
Two things are easy to confuse: the **OpenClaw Gateway** (the orchestration process, on port 18789 by default) and the **local model server** (llama.cpp, LM Studio...). This article is about how OpenClaw uses a model server running on your own machine. To use a model through the cloud, see [DeepSeek, OpenClaw and Ollama Cloud: connecting models to an agent](deepseek-openclaw-va-ollama-cloud-ket-noi-mo-hinh-voi-agent.html).
## Choosing a runtime
OpenClaw's "Local models" page lists the runtimes to use:
- **ds4:** DeepSeek V4 Flash running locally on macOS Metal, with OpenAI-style tool calling.
- **llama.cpp:** model chosen by hardware, a verified download, a server managed by OpenClaw.
- **LM Studio:** easy first-time setup, with a model-loading interface and the native Responses API.
- **Ollama:** a command-line workflow, a model library, a systemd service.
- **vLLM, SGLang, MLX:** high-throughput serving with OpenAI-compatible endpoints.
- **LiteLLM and custom proxies:** any gateway with an OpenAI-style `/v1/chat/completions`.
## The easiest way: a local server managed by OpenClaw
Install the llama.cpp plugin, run `openclaw onboard` and choose **Managed local server**. Before downloading, the setup shows the Gateway host, the model, the download size and the backend, then verifies one real tool call before changing the default model. It checks RAM, GPU memory and disk instead of guessing; the sample recipes use a 64K context, and the smallest recipe needs at least 8 GiB of machine memory. The documentation states plainly that this minimum "does not guarantee it will fit or be fast".
## Declaring a custom provider manually
For an existing server, use `models.providers`. An example from the documentation (LM Studio, JSON5 syntax):
```
{
  agents: {
    defaults: {
      model: { primary: "lmstudio/my-local-model" },
      models: { "lmstudio/my-local-model": { alias: "Local" } },
    },
  },
  models: {
    providers: {
      lmstudio: {
        baseUrl: "http://localhost:1234/v1",
        apiKey: "${LM_API_TOKEN}",
        api: "openai-completions",
        timeoutSeconds: 300,
        models: [
          { id: "my-local-model", name: "Local Model", reasoning: false, input: ["text"],
            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },
            contextWindow: 200000, maxTokens: 8192 },
        ],
      },
    },
  },
}
```
The main fields: `baseUrl` (with `/v1`), `apiKey` (may reference an environment variable), `api` (`openai-completions`, `openai-responses`, `anthropic-messages`) and `models[]` (at least `id` is needed). For a server without authentication set `auth: "none"` (only with `openai-completions`). Default ports: LM Studio `http://localhost:1234/v1`, vLLM `http://127.0.0.1:8000/v1`, SGLang `http://127.0.0.1:30000/v1`, llama.cpp for example `http://127.0.0.1:8080/v1`. Ollama is recognized at `http://127.0.0.1:11434` when you enable it with `OLLAMA_API_KEY`, for example the model `ollama/llama3.3`. Set `contextWindow` and `maxTokens` to the model's real limits.
## Context and tool calling
- Leave room for the whole prompt, tools, history and output. A model that answers short questions can still break an agent turn.
- Check that the server's chat template and parser support tool calling; if not, tools show up as text, JSON, XML or an empty `tool_calls` array.
- A warning when context drops below 20% of the window, a hard block below 10%.
- For the comparison of Hermes's context requirement: 64K tokens, see [Ollama and Hermes: when does a local AI agent beat the cloud?](ollama-va-hermes-khi-nao-local-ai-agent-tot-hon-cloud.html).
## When the model loads but the agent is still broken
The documentation suggests checking layer by layer: first the transport, then tool use and the context budget. There are commands `openclaw infer model run --local` and `--gateway` to separate where the error lies. A few other notes: the first model load causes a startup delay; the provider's `timeoutSeconds` cannot extend the agent's wait time, and if `agents.defaults.timeoutSeconds` is lower you must raise both; on WSL2 with Ollama and NVIDIA, autostart can reload the model at boot and pin memory, causing the virtual machine to restart repeatedly.
## Important risks
- A small or heavily quantized model can break multi-step work even if it passes a simple text test. Choose the largest version your hardware can handle.
- The documentation states plainly that local models **lack the safety filters of a cloud provider**. Keep tool permissions narrow, keep context compaction on and apply prompt injection defenses (see the [security lessons](openclaw-update-bai-hoc-ve-tich-hop-message-cron-va-bao-mat.html)).
- A "lean" mode that removes optional tools for a weak model is an advanced troubleshooting trick, not a default.
## Combining local and cloud
Set a cloud model as primary, with a local model and another cloud model as fallbacks, or reverse the order to prefer local, using `models.mode: "merge"` to keep cloud models as fallbacks. Remember that falling back to the cloud makes data leave the machine.
