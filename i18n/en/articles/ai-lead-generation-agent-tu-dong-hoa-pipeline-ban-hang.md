---
title: AI Lead Generation Agent: automating the sales pipeline
desc: Design an agent that helps find and nurture leads under control, with the legal limits on personal data and advertising messages in Vietnam.
min: 8
---
QUICK: An agent can help find, screen and draft outreach to leads, but a person must approve before sending and Vietnamese law has clear constraints on personal data and advertising messages. Start with public business data, get consent when sending advertising and provide a way to opt out.
## The sales pipeline and where an agent helps
A pipeline usually consists of: defining the target customers, finding sources, enriching information, scoring, outreach, follow-up and handing over to the salesperson. An agent is most useful in the steps that take effort but carry little risk: gathering public business information, scoring by criteria you set, drafting letters and recording into the system. The steps that are relational and involve decisions should be done by people.
## Design steps
**1. Define the ideal customer profile (ICP).** Industry, size, problem, decision maker. The more specific, the less waste.
**2. Choose lawful data sources.** Public business information (websites, business directories), lists of customers who agreed to receive information, customers who leave their details themselves. Avoid buying or collecting lists of personal data of unclear origin.
**3. Enrich and score.** The agent reads public information and scores by criteria you set, noting the basis so you can check. Do not let it invent information about a company.
**4. Draft the outreach.** Personalize based on real information, without invention. All content waits for a person to approve.
**5. Send through permitted channels,** following the rules in the section below.
**6. Track and learn.** Record responses, remove people who decline, adjust the criteria.
## The role of people
- **Approve every outbound message** before sending, at least in the early phase.
- **Decide the data sources** and the outreach list.
- **Handle responses** and real conversations.
- **Take legal responsibility** for how data is collected and used.
## Legal constraints in Vietnam
This is the part to read carefully. The points below are based on sources I looked up on 2026-11-15, mainly analyses by consulting firms and the press rather than the original legal texts. **Read the official documents or ask a lawyer before deploying.**
- **Personal data.** The Personal Data Protection Law 2025 (Law No. 91/2025/QH15) takes effect from Jan 1, 2026, with Decree 356/2025/ND-CP guiding its implementation. The sources say the general principle is that processing personal data requires the data subject's consent, unless the law provides otherwise. Using data for advertising and remarketing is not banned but must meet the conditions of the law. Penalties can be very high.
- **Advertising messages, emails and calls.** Decree 91/2020/ND-CP is still cited by the sources as the document in force. Under it, sending advertising messages or making advertising calls needs the recipient's prior consent, and numbers registered on the do-not-call (DNC) list must not be contacted. The sources also mention a draft replacement decree being put out for comment, not confirmed as issued.
## Safe design principles
- **Collect only the data necessary** for a clear purpose.
- **Prefer business information** over personal information.
- **Get consent** before sending advertising content, and keep evidence of consent.
- **Always provide a visible way to opt out,** and handle opt-out requests quickly.
- **Give users the right** to view, correct and delete their data.
- **Secure the data:** set permissions, and do not store it casually in tools with unclear policies.
- **Do not use the agent to impersonate** or to make people think they are talking to a real person when that matters.
## Technical risks of the agent
- An agent that reads web content or mail can be hit by injected malicious instructions, see [Evaluating AI agents through real tests](danh-gia-ai-agent-qua-bai-test-thuc-te-nhin-vao-tieu-chi-nao.html).
- The agent can invent details about the recipient, discrediting the letter. Always check before sending.
- Bulk sending is easily flagged as spam and damages your domain's reputation.
## How to start small
1. Choose a narrow customer group.
2. Use the agent to gather and score from public business information.
3. Review and send by hand a small number of letters with real value.
4. Measure the responses, and only then automate more steps.
If you work with company data, see also the way to classify data in [How should an AI tool library be organized to be easy to use?](mot-kho-cong-cu-ai-nen-duoc-to-chuc-nhu-the-nao-de-de-dung.html).
