---
title: Installing DeepSeek with Ollama: running AI models on a budget
desc: Install Ollama, download and run the DeepSeek-R1 model on a personal machine, how to pick a size by RAM and the limits to understand before using it.
min: 7
---
QUICK: Install Ollama, then run `ollama run deepseek-r1` with a size that fits your machine. The model runs right on your machine, with no per-use fee. The thing to understand correctly: the small versions on a personal machine are distilled versions, not the original large DeepSeek-R1 model.
## What running locally means and why it saves money
When you run a model with Ollama, the whole reasoning process happens on your machine. You pay no fee per question, and the content you enter does not have to be sent to an outside server for processing (you still need the internet to download the model the first time). The price you pay is hardware: the larger the model, the more memory it needs, and speed depends on your machine. "Saving money" here means no per-use bill, not that it is entirely free, because you still use electricity and hardware.
## Step 1: Install Ollama
Download the installer for Windows or macOS from the official site ollama.com. On Linux, use the install command from the instructions on that page. After installing, check:
```
ollama --version
```
## Step 2: Download and run DeepSeek-R1
```
ollama run deepseek-r1:7b
```
This command downloads the model the first time and then opens a chat window right in the terminal. Type a question and press Enter, type `/bye` to exit. The part after the colon is the model size. The Ollama library lists several sizes for DeepSeek-R1, from very small to very large, with the download size of each.
## Choose a size for your machine
A practical rule: the size shown on the model page is the minimum memory the model takes, and your machine needs more than that number to run smoothly.
- A machine with little RAM: choose the smallest version and accept simpler answers.
- A machine with a discrete graphics card with its own memory: a model that sits in the card's memory runs much faster than on the CPU.
- If the machine is slow, freezes or the fan runs at full power, try a smaller version.
You should not choose a size just because "bigger means smarter" when the machine cannot handle it, because a model that runs too slowly cannot really be used.
## How a distilled version differs from the original model
This is the point most easily misunderstood. The original DeepSeek-R1 is a very large model. The small versions on Ollama are other base models (the Qwen and Llama families) retrained by learning from R1's outputs, which is why they are called distilled versions. They carry R1's reasoning style but their ability does not match the original. So when you compare results with online services, remember you are comparing a small model with a large system.
## Useful management commands
```
ollama list        # downloaded models
ollama ps          # running models
ollama rm model-name   # delete a model to reclaim space
ollama pull model-name # download only, do not run
```
## Using it from code and other tools
Ollama runs a local server, usually at `http://localhost:11434`, for other apps to call. Many chat interfaces such as Open WebUI can connect to this address, see [Hermes Open WebUI with Docker and Ollama: an internal AI interface](hermes-open-webui-voi-docker-va-ollama-dung-giao-dien-ai-noi-bo.html). For each tool's specific configuration, see that tool's documentation.
## Reasoning models show a "thinking" section
DeepSeek-R1 is a reasoning model, so it usually produces a reasoning trace before the answer. Per Ollama's documentation, when you call the API the trace is in a separate `thinking` field, apart from the answer (`message.content`), and you can control it with the `think` field. It lets you see how the model reasons, but it also makes responses longer and slower. If you use the result in an app, take only the answer field.
## Limits and safety notes
- The model can still answer wrongly with confidence, especially with specific facts. Check important information.
- Running locally does not automatically make your data safe if your machine is shared, cloud-synced or accessed remotely.
- The Vietnamese quality of the small versions is usually lower than English. Test with a few of your real questions before relying on it.
- Consider the model's terms of use and license before using it for commercial purposes.
If you want to use a local model to run a coding tool, see also [Claude Code for free through Ollama: understanding the limits and model choices](claude-code-mien-phi-qua-ollama-hieu-dung-gioi-han-va-lua-chon-mo-hinh.html).
