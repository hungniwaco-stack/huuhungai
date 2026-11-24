---
title: Setting up a Telegram AI agent: token, configuration and the first task
desc: Create a Telegram bot with BotFather, get the token, limit who may message it and run a loop that receives, asks an AI model and replies, in a short script.
min: 8
---
QUICK: Create a bot through BotFather to get a token, store the token in an environment variable, run a script that receives messages with the Bot API and then calls an AI model to reply. The most important thing is not the code but the limits: only allow your own account to command the bot.
## What a Telegram AI agent is
A Telegram AI agent is a program that listens for messages sent to a Telegram bot, passes the content to an AI model (and possibly other tools), then sends the result back to the chat. Telegram provides the interface already available on phones and computers so you do not have to write an app. The part you handle yourself is the processing program running somewhere, such as a personal machine or a small server.
## Step 1: Create a bot with BotFather
1. Open Telegram and find the account `@BotFather` (with the verified mark).
2. Send the command `/newbot`.
3. Set a display name, then set a username, which must end with `bot`.
4. BotFather returns a **token**, a long string of characters. This is the key that controls the bot.
The token lets anyone who holds it control your bot. Do not paste the token in a post, a screenshot or a public code repository. If it leaks, send `/revoke` to BotFather to create a new token.
## Step 2: Store the token safely
Put the token in an environment variable instead of writing it directly in code:
```
# macOS, Linux, WSL
export TELEGRAM_BOT_TOKEN="paste-your-token"

# Windows PowerShell
$env:TELEGRAM_BOT_TOKEN = "paste-your-token"
```
## Step 3: Check the bot works
Send any message to your bot on Telegram, then call the Bot API to see incoming messages:
```
curl "https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/getMe"
curl "https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/getUpdates"
```
The `getMe` command confirms the token is right. The `getUpdates` command returns new messages, including your `chat.id` and `from.id`. Note down your `from.id`, you will use it to limit access in the next step.
## Step 4: Two ways to receive messages
- **Polling (asking continuously):** the program calls `getUpdates` itself. Easy to start, works right on a personal machine, and needs no public address.
- **Webhook:** Telegram sends messages to an HTTPS address of yours. Suits when you already have a server, but needs extra configuration.
For the first time, use polling.
## Step 5: A minimal script
The snippet below receives messages, ignores everyone outside the allowlist, calls an AI function and replies. The `ask_ai` function is where you connect the model you use; read the provider's documentation to write that part.
```
import os, time, requests

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
ALLOWED = {123456789}  # replace with your from.id
API = f"https://api.telegram.org/bot{TOKEN}"

def ask_ai(question: str) -> str:
    # Connect your AI model here and return the reply as a string.
    return "I received: " + question

offset = None
while True:
    r = requests.get(f"{API}/getUpdates", params={"timeout": 30, "offset": offset}, timeout=40).json()
    for u in r.get("result", []):
        offset = u["update_id"] + 1
        m = u.get("message")
        if not m or "text" not in m:
            continue
        if m["from"]["id"] not in ALLOWED:
            continue  # ignore strangers
        reply = ask_ai(m["text"])
        requests.post(f"{API}/sendMessage", json={"chat_id": m["chat"]["id"], "text": reply}, timeout=20)
    time.sleep(1)
```
Run it with `python file-name.py` after installing the `requests` library. Send a message to the bot and you will get the reply back. Once it works, replace the `ask_ai` function with a real model call.
## Step 6: What the first task should be
Choose a small task with low risk that is easy to check:
- Summarizing text you paste into the chat.
- Translating or rewriting a passage in another style.
- Answering questions from a short document you provide.
Do not yet let the bot send email, run commands or handle money at this stage.
## Safety: the most important part
- **Limit users.** A Telegram bot can be found and messaged by anyone. If you do not filter, strangers will command your program, and every model call cost will be billed to you.
- **Limit tools.** Give the agent only the actions it truly needs, and require your confirmation before actions that cannot be undone.
- **Be careful with content coming from outside.** Forwarded messages or web pages the agent reads may contain malicious instructions meant to trick the model.
- **In group chats**, the bot by default only receives part of the messages because of privacy mode. Change it with BotFather if needed, and think carefully before letting the bot read a whole group.
## Next steps
Once the loop of receiving, processing and replying is working, you can add conversation memory, specific tools and run the bot permanently on a small server. Add one thing at a time and test carefully before expanding.
