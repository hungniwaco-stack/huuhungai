---
title: DeepSeek tutorial: understanding long context and MoE when choosing a model
desc: A plain explanation of MoE (mixture of experts) and DeepSeek's long context window, and how to use these two concepts to choose a model for real needs.
min: 7
---
QUICK: MoE (Mixture of Experts) is a way of splitting a model into many expert blocks and activating only part of them for each token, so the model is very large while the compute cost per turn is lower. A long context lets you put in a lot of text at once, but long does not mean it is all used well. Choose a model by the work you do, not by the numbers on a spec sheet.
## Two concepts, two different questions
When you read about a model such as DeepSeek, you often meet two phrases: the MoE architecture and the context length. They answer two different questions. MoE answers "how is the model organized inside to run efficiently". Long context answers "how much text can the model read at one time". Understanding both helps you avoid being swept along by big numbers.
## How MoE works
An ordinary language model uses all of its parameters for every token. An MoE model splits the computation into groups called experts. For each token, a small router picks a few suitable experts to handle it, and the rest rest.
The result is that the model's total parameters can be very large, while the number of parameters actually active per token is much smaller. According to DeepSeek's announcements when launching the V3 and R1 models, total parameters were about 671 billion while each token activated only about 37 billion. Newer versions differ: the Apr 24, 2026 announcement of DeepSeek-V4 (preview) lists V4-Pro at 1.6 trillion total parameters with 49 billion active, and V4-Flash at 284 billion total with 13 billion active; both support a 1-million-token context. DeepSeek has kept updating since: the API pricing page, read on Nov 28, 2026, shows the name `deepseek-flash` pointing to V4.1-Flash, so check the current documentation.
## What MoE means for users
- **Cost and speed:** because each token uses only part of the model, serving a very large model is cheaper than an ordinary model of the same total size.
- **Running locally is still heavy:** even though only part is active at a time, all the parameters must still sit in memory. So a large MoE model cannot run on an ordinary personal machine. The small versions you run with Ollama are usually other distilled models, see [Installing DeepSeek with Ollama: running AI models on a budget](cai-deepseek-voi-ollama-chay-mo-hinh-ai-theo-huong-tiet-kiem.html).
- **More experts is not automatically better:** quality depends on how it is trained, not only on the architecture.
## What a long context is
The context window is the amount of text the model can "see" at the same time, measured in tokens (one token is roughly part of a word). A long context lets you put in a long document, many code files or a long conversation history at once. The specific maximum length differs by version and by how you access it, so check the current documentation.
## A long context does not mean it is all used well
- **Accuracy can drop** for information in the middle of a very long text. Models often pay better attention to the beginning and end. This effect was described in the "Lost in the Middle" study (2023) on models of that time; test it on the model you use.
- **Cost and latency rise** with the amount of text you send each time.
- **Memory grows when running locally:** the longer the context, the larger the cache. A model that runs with a short context may run out of memory when you raise the length.
- **Noise:** stuffing in too much unrelated material can make answers worse.
## When you really need a long context
- Summarizing or analyzing one long document whole.
- Q&A over many closely related files.
- Keeping a very long exchange going without wanting to summarize it again.
If you only need to look things up in a large document store, the approach that is usually more effective is to find the relevant passages first and give only those passages to the model, instead of stuffing in the whole store.
## How to choose a model by need
Answer in this order:
1. **What do you need it for:** writing, reasoning, coding, summarizing documents?
2. **Is the data sensitive:** if so, consider running locally or a service with suitable commitments.
3. **Budget and speed:** do you need a fast answer, a cheap one or the highest quality?
4. **Typical text length:** how long are your documents usually.
5. **Test with real data yourself:** run a few of your tasks on a few models and compare, see [Evaluating AI agents through real tests: which criteria to look at](danh-gia-ai-agent-qua-bai-test-thuc-te-nhin-vao-tieu-chi-nao.html) for a scoring framework.
## Common misunderstandings
- "More parameters is always smarter." Not necessarily, especially with MoE, where total parameters and active parameters are two different numbers.
- "A long context replaces organizing your data." No, good organization usually gives better results than stuffing in a lot.
- "Running locally is always cheaper." Only true when you already have suitable hardware.
