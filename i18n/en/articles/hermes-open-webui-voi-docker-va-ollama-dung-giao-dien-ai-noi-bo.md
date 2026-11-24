---
title: Hermes Open WebUI with Docker and Ollama: an internal AI interface
desc: Build a chat interface for Hermes Agent: run a model with Ollama, turn on Hermes's API server and connect Open WebUI in Docker, per the official docs.
min: 9
---
QUICK: Hermes Agent is Nous Research's agent, not a model. To get a web-style chat interface, you run a model with Ollama, point Hermes at Ollama, turn on Hermes's API server (port 8642 by default), then connect Open WebUI running in Docker to that API server.
## The three components and how they connect
- **Ollama** runs the language model on your machine.
- **Hermes Agent** is the automation agent (with memory, skills and tools). It uses the model Ollama provides. Hermes has a built-in **API server** following the OpenAI-compatible standard.
- **Open WebUI** is a chat interface running in Docker. It connects to Hermes's API server as if it were an OpenAI service.
The flow is: browser, to Open WebUI, to Hermes's API server, to Ollama. The difference from the usual way of using Open WebUI is that Open WebUI **does not talk directly to Ollama** but goes through Hermes, so you chat with the agent (with tools and memory) and not just the bare model.
## Machine requirements
According to Nous Research's guide to running Hermes locally with Ollama:
- At least 8 GB of RAM for a model of about 3 billion parameters, and 32 GB or more for models of 27 billion parameters and up.
- At least 5 GB of free disk for one model, and 30 GB or more if you use several models.
- An NVIDIA graphics card with 8 GB or more of memory is optional but noticeably faster.
- Docker is needed for Open WebUI.
Hermes supports Linux, macOS, WSL2 and Windows. See the official installation page for the way that suits your operating system.
## Step 1: Install Ollama and download a model that supports tools
```
curl -fsSL https://ollama.com/install.sh | sh
ollama --version
curl http://localhost:11434/api/tags
```
The first command is for Linux (on Windows and macOS, download the installer from ollama.com). The last command confirms Ollama is running. For agent work, the model must be able to call tools. Hermes's guide points to the model `gemma4:31b` as the only option in their list that calls tools reliably, while the smaller models they list can only chat and cannot run tools:
```
ollama pull gemma4:31b
```
## Step 2: Raise the context length to 64,000 tokens
According to Hermes's documentation, Ollama defaults to a 2048-token context, while Hermes needs at least 64,000 tokens to use tools. Create a version of the model with a larger context using a Modelfile:
```
cat > Modelfile << 'EOF'
FROM gemma4:31b
PARAMETER num_ctx 64000
EOF
ollama create gemma4-64k -f Modelfile
```
From here on use the name `gemma4-64k` in place of `gemma4:31b`.
## Step 3: Install and configure Hermes
Install Hermes following the official guide (for example on Linux, macOS or WSL2):
```
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
hermes setup
```
When the setup wizard asks, choose **Custom Endpoint** and enter:
- Base URL: `http://localhost:11434/v1`
- API Key: leave blank or enter `no-key`
- Model: `gemma4-64k`
Or edit the file `~/.hermes/config.yaml` directly:
```
model:
  default: "gemma4-64k"
  provider: "custom"
  base_url: "http://localhost:11434/v1"
```
Test with the `hermes` command to make sure the agent can answer before going to the next step.
## Step 4: Turn on Hermes's API server
```
hermes config set API_SERVER_ENABLED true
hermes config set API_SERVER_KEY your-secret-key
hermes gateway
```
Replace `your-secret-key` with a long, hard-to-guess string. When it runs correctly, you will see a line saying the API server is listening at `http://127.0.0.1:8642`. Check with:
```
curl -s http://127.0.0.1:8642/health
curl -s -H "Authorization: Bearer your-secret-key" http://127.0.0.1:8642/v1/models
```
The first command must return an `ok` status. The second must list a model named `hermes-agent`.
## Step 5: Run Open WebUI in Docker
```
docker run -d -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:8642/v1 \
  -e OPENAI_API_KEY=your-secret-key \
  -e ENABLE_OLLAMA_API=false \
  --add-host=host.docker.internal:host-gateway \
  -v open-webui:/app/backend/data \
  --name open-webui \
  --restart always \
  ghcr.io/open-webui/open-webui:main
```
`OPENAI_API_KEY` must exactly match `API_SERVER_KEY` and must not be blank. `ENABLE_OLLAMA_API=false` hides the default Ollama connection, which otherwise shows up empty in the model list. The first startup takes about 15 to 30 seconds. On PowerShell, write the command on one line.
## Step 6: Open the interface
Go to `http://localhost:3000` and create an account. The first account is the administrator, so create it yourself right away. Choose `hermes-agent` in the model list and start chatting.
If you want to configure through the interface instead of environment variables: go to Admin Settings, the Connections section, add an OpenAI connection with the URL `http://host.docker.internal:8642/v1` and the key `API_SERVER_KEY`.
## Ports used
- Hermes API server: port `8642`.
- Open WebUI: port `3000` on your machine, mapped to port 8080 in the container.
On Linux without Docker Desktop, if `host.docker.internal` does not resolve, keep the `--add-host` flag as above, or use `--network=host` with the address `http://localhost:8642/v1`.
## Security: the points the documentation stresses
- **Tools run on the server hosting the API server.** Terminal, file, browser and MCP run right where Hermes runs, not on the user's laptop. Anyone who can reach the chat interface can command the agent, so control accounts tightly.
- **The API server listens only on `127.0.0.1` by default.** Changing the listen address changes who can access it, so think carefully.
- **Environment variables only take effect on Open WebUI's first startup.** After that, changes must be made through the admin interface, or delete the volume and start over.
- Do not expose port 3000 or 8642 to the internet without suitable HTTPS and authentication.
## Common errors
- **`/health` does not respond:** restart the gateway with `hermes gateway stop && hermes gateway`.
- **`/v1/models` returns 401:** the key in the call does not match `API_SERVER_KEY`.
- **`hermes-agent` is not in the list:** check the key and the connection address in the Connections section.
- **The agent cannot run tools or prints raw JSON:** the model does not support tool calling, or the context is still too small. Redo Step 2.
- **The first response takes very long:** the model is processing the system prompt and the tools, especially on CPU only. Keeping the model loaded in memory helps.
## Read next
If you are new to Ollama, see [Installing DeepSeek with Ollama: running AI models on a budget](cai-deepseek-voi-ollama-chay-mo-hinh-ai-theo-huong-tiet-kiem.html). To weigh local against cloud, see [Ollama and Hermes: when does a local AI agent beat the cloud?](ollama-va-hermes-khi-nao-local-ai-agent-tot-hon-cloud.html).
This article was rewritten on 2026-11-15 following the official documentation of Hermes Agent and Open WebUI. Commands and interfaces may change by version, so check the documentation before following along.
