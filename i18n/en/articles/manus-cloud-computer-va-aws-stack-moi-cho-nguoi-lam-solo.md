---
title: Manus Cloud Computer and the AWS partnership: two different things
desc: Manus Cloud Computer is Manus's always-on cloud machine; AWS is its infrastructure partner. Two different things: what is confirmed and what is not.
min: 7
---
QUICK: "Manus Cloud Computer" and "Manus with AWS" are two separate pieces of information. Cloud Computer is a Manus product (launched Apr 30, 2026, according to press): a persistent Ubuntu machine that runs 24/7. AWS announced in December 2025 that Manus chose AWS as its strategic cloud provider. I found no source saying Cloud Computer runs on AWS, so this article does not merge the two into one "stack".
## Two pieces of information to keep apart
**1. The AWS partnership (Dec 3, 2025).** AWS's press release says Manus, a general-purpose AI agent, chose AWS as its strategic cloud provider. The services named include Amazon Bedrock, Firecracker (AWS's open-source lightweight virtualization technology), Amazon Aurora Serverless, Amazon EKS, AWS Glue and Amazon MSK; E2B is mentioned for cluster orchestration but the release does not describe it as an AWS service.
**2. Cloud Computer (Apr 30, 2026, per TestingCatalog).** This news site, citing a Manus post as its source, reports that it is a persistent, always-on cloud machine for running bots, scripts and software continuously. AWS's press release does not mention Cloud Computer at all.
## What is confirmed about Cloud Computer
According to the TestingCatalog article (a news site whose articles are AI-assisted and reviewed by editors):
- Runs Ubuntu Linux, accessed through SSH or a web terminal.
- **Persistent:** unlike Manus's earlier temporary sandboxes, it keeps files and the environment between sessions.
- Example uses: long-running Slack and Discord bots, databases, scheduled reports, and hosted tools such as WordPress and Metabase. You can choose the region and storage capacity.
- There are Basic, Standard and Advanced plans by need; the article does not state prices.
- There is no graphical desktop interface yet (the article says this directly).
- The article does not say it runs on AWS or any particular provider.
I have not read Manus's original post, so check the Manus page before deciding.
## The figures in AWS's press release, and who says them
AWS's press release (not attributed to a specific speaker) states: annual recurring revenue of $90 million four months after Manus launched its subscription plan, about 60% fewer development and operations staff, a 70% increase in overall operating efficiency, a 68% reduction in compute cost, tens of thousands of sandbox instances managed with three operations staff, about 125 milliseconds to launch each sandbox and about 5 MiB of memory per sandbox. This is a press release published by AWS about a customer, promoting its own platform; treat it as a claim rather than an independent assessment, and these numbers describe Manus's infrastructure, not your experience.
## Should a "solo operator" use it
An always-on cloud machine is useful for things like running a small bot, a scheduled report or hosting an internal tool that you do not want to leave a laptop on 24/7 for. Consider:
1. **Cost and plans:** there was no price in the sources I read; see Manus's price list.
2. **Data:** a cloud machine holds your files and environment; read the data policy, and do not leave keys or customer data there if you do not understand how it is protected.
3. **Security:** the article mentions environment isolation and team access control; use public-key SSH, keep the system updated and turn on a firewall.
4. **Provider dependence:** running a service long term on a third party's platform needs a backup and migration plan.
5. **Compared with renting your own server:** an ordinary VPS also keeps files and runs 24/7; Cloud Computer may be more convenient for people who are not technical, but I have no price comparison data.
If you run a self-hosted agent, the way to keep control is in [Installing OpenClaw](cai-openclaw-desktop-app-cach-bat-dau-voi-ai-agent-giao-dien-sach.html) and the [security lessons](openclaw-update-bai-hoc-ve-tich-hop-message-cron-va-bao-mat.html).
