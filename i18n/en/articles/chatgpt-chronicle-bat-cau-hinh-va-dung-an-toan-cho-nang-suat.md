---
title: ChatGPT Computer History (formerly Chronicle): turning it on and using it safely
desc: Chronicle has been replaced by Computer History in ChatGPT on macOS: turning it on and off, data recorded, storage, deleting it and the risks.
min: 7
---
QUICK: According to OpenAI's documentation, Chronicle (a research preview) has been replaced by **Computer History**, a rebuilt system and not just a rename. It turns your activity in apps and web pages into memories for ChatGPT and Codex, is only in the ChatGPT app for macOS, and is off by default. It does not take screenshots or record audio, but memories are stored as unencrypted files and web page content can carry injected instructions.
## What Chronicle is now
OpenAI's current documentation page says Computer History "replaces the earlier Chronicle research preview", and describes it as a rebuilt system, not a rename. So the way to turn it on, the section names and the limits you may read in older articles about "Chronicle" may be out of date. This article describes Computer History according to the documentation on the day I read it (2026-11-16).
## Who can use it
- The ChatGPT app for **macOS**. Off by default for Pro, Business and Enterprise users.
- Pro users can turn it on themselves. For Business and Enterprise, an administrator must grant permission first, then each member chooses to turn it on.
- **Memories** must be on. It does not work with API keys or Amazon Bedrock.
- Available in supported regions, which the documentation says include the EEA, Switzerland and the United Kingdom. The page lists no plans other than those above.
Some older articles say the original Chronicle was only for Pro users on macOS and excluded the EU, UK and Switzerland; those sources do not agree with each other and do not match the current documentation, so trust OpenAI's documentation.
## How to turn it on, pause and turn it off
- **Turn on:** Settings, Integrations, Computer history, Turn on. Turn on Memories if asked, choose which apps and websites may contribute, and follow macOS's permission dialogs.
- **Pause and resume:** in Settings or from the ChatGPT icon on the macOS menu bar (the Computer History menu).
- **Turn off:** choose "Turn off Computer History" to stop collection. Note that pausing does not immediately stop a summary already in progress.
## What it records
- Interaction events such as clicks, keystrokes, shortcuts, app switches, along with context that macOS provides through the accessibility system.
- It does **not** take screenshots, does **not** record the microphone and does **not** capture system audio.
- Private browsing is never included.
- It does not need the Screen Recording permission, but macOS may show a dialog for app and website sources.
Since there are no screenshots or audio, it relies on events and accessibility text, so the quality of the memories depends on whether the app provides that text. Summarizing also uses tokens.
## Where the data is stored and how it is handled
- Event files are stored temporarily on your Mac in the ChatGPT App Group and deleted after **48 hours**.
- Memories are Markdown files normally located at `$CODEX_HOME/memories/extensions/skysight/` (usually `~/.codex/memories/extensions/skysight/`). **This feature does not encrypt** those files.
- OpenAI processes the event files on its servers to create memories; it says it does not keep them after processing unless required by law, and does not use them for training.
- Memory content can be used in chat, and chat content can be used to improve models if your data control settings allow it.
## Reviewing and deleting
Open Settings, Computer history, History to see a timeline by date and time. You can open the memory files in Finder, delete individual entries, or delete the last 10 minutes, one hour, one day or the entire history. Deleting removes both the events and the related memories and **cannot be undone**.
## Risks the documentation states
- **Prompt injection:** content from apps and web pages can carry malicious instructions, and ChatGPT or Codex may follow them.
- **Unencrypted memory files** can be read by other programs running under the same macOS user, and may contain sensitive information.
- **Other people:** turn it off when talking with others unless you have their explicit prior consent.
- Consider pausing or excluding apps that hold health, financial or personal data.
## How to use it safely
1. Turn it on only when you have a specific need for "screen memory", and choose only a few apps.
2. Exclude password managers, banking, sensitive email and messaging apps.
3. Open History periodically to see what it recorded, and delete entries you do not want.
4. Encrypt the Mac's disk (FileVault) because memories are stored unencrypted.
5. On a work machine, ask the administrator about the policy before turning it on.
For principles of data governance and agent permissions, see also how OpenClaw handles memory in [Setting up long-term memory for OpenClaw: when it is needed and how to control it](thiet-lap-bo-nho-dai-han-cho-openclaw-khi-nao-can-va-lam-sao-kiem-soat.html).
