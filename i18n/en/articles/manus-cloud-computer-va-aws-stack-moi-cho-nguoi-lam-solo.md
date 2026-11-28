---
title: Manus Cloud Computer and the AWS partnership: two different things
desc: Manus Cloud Computer is Manus's always-on cloud machine; AWS is its infrastructure partner. Two different things: what is confirmed and what is not.
min: 7
---
QUICK: "Manus Cloud Computer" and "Manus with AWS" are two separate pieces of information. Cloud Computer is a Manus product announced on Apr 30, 2026: a persistent Ubuntu machine that runs 24/7. AWS announced in December 2025 that Manus chose AWS as its strategic cloud provider. I found no source saying Cloud Computer runs on AWS. Also, in August 2026 Manus separated from Meta and deleted some users' data, which is worth knowing before you entrust long-term work to it.
## Two pieces of information to keep apart
**1. The AWS partnership (Dec 3, 2025).** AWS's press release says Manus, a general-purpose AI agent, chose AWS as its strategic cloud provider. The services named include Amazon Bedrock, Firecracker (AWS's open-source lightweight virtualization technology), Amazon Aurora Serverless, Amazon EKS, AWS Glue and Amazon MSK; E2B is mentioned for cluster orchestration but the release does not describe it as an AWS service.
**2. Cloud Computer (Apr 30, 2026, per Manus's post).** Manus describes it as a dedicated cloud machine that runs bots, Python scripts and software around the clock; TestingCatalog also reported it. AWS's press release does not mention Cloud Computer at all.
## What is confirmed about Cloud Computer
According to Manus's launch post and its FAQ:
- Runs Ubuntu Linux, accessed through SSH or a web terminal.
- **Persistent:** unlike Manus's earlier temporary sandboxes, it keeps files and the environment between sessions.
- Example uses: long-running Slack and Discord bots, databases, scheduled reports, and hosted tools such as WordPress and Metabase. You can choose the region and storage capacity.
- There are Basic (simple Python scripts), Standard (active websites and APIs) and Advanced (team databases) plans; the post does not state prices.
- There is no graphical desktop interface at present; it is command-line only.
- The post does not say it runs on AWS or any particular provider; AWS is mentioned only as a traditional way of renting servers.
- **If you stop paying:** per Manus's FAQ, the persistent environment closes and its working files are deleted; delivered outputs such as reports and spreadsheets stay in your chat history. Keep your own backup.
**Update, Nov 28, 2026: Manus has separated from Meta.** Per its official notice, Meta acquired Manus on Dec 29, 2025. As part of the separation, to comply with regulatory requirements in some places, data that certain users created from that date was deleted on Aug 23 and 24, 2026; affected users were told in advance so they could back it up and restore it later. Manus says this was not a security incident, and that data is stored in the US and Singapore. On Sep 1, Manus announced it had resumed independent operations. An earlier version of this article did not mention this.
## The figures in AWS's press release, and who says them
AWS's press release (not attributed to a specific speaker) states: a $90 million revenue run rate four months after Manus launched its subscription plan, about a 60% reduction in development and operations staffing requirements, a 70% increase in overall operating efficiency, a 68% reduction in compute cost, tens of thousands of sandbox instances managed with three operations staff, about 125 milliseconds to launch each sandbox and about 5 MiB of memory per sandbox. This is a press release published by AWS about a customer, promoting its own platform; treat it as a claim rather than an independent assessment, and these numbers describe Manus's infrastructure, not your experience.
## Should a "solo operator" use it
An always-on cloud machine is useful for things like running a small bot, a scheduled report or hosting an internal tool that you do not want to leave a laptop on 24/7 for. Consider:
1. **Cost and plans:** there was no price in the sources I read; see Manus's price list.
2. **Data:** a cloud machine holds your files and environment; read the data policy, and do not leave keys or customer data there if you do not understand how it is protected.
3. **Security:** Manus says the machine is isolated from your personal computer and team access is controlled; still use public-key SSH, keep the system updated and turn on a firewall.
4. **Provider dependence:** running a service long term on a third party's platform needs a backup and migration plan. The August 2026 data deletion above is a concrete example.
5. **Compared with renting your own server:** an ordinary VPS also keeps files and runs 24/7; Cloud Computer may be more convenient for people who are not technical, but I have no price comparison data.
If you run a self-hosted agent, the way to keep control is in [Installing the OpenClaw Desktop App: how to start with a clean-interface AI agent](cai-openclaw-desktop-app-cach-bat-dau-voi-ai-agent-giao-dien-sach.html) and the [security lessons](openclaw-update-bai-hoc-ve-tich-hop-message-cron-va-bao-mat.html).
