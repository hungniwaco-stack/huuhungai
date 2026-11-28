---
title: AI Lead Generation Agent: automating the sales pipeline
desc: Design an agent that helps find and nurture leads under control, with the legal limits on personal data and advertising messages in Vietnam.
min: 8
---
QUICK: An agent can help find, screen and draft outreach to leads, but a person must approve before sending and Vietnamese law has clear constraints on personal data and advertising. A person's name and phone number are still personal data even if found in public; trading personal data is banned (unless a law provides otherwise); advertising messages, emails and calls need prior consent.
## The sales pipeline and where an agent helps
A pipeline usually consists of: defining the target customers, finding sources, enriching information, scoring, outreach, follow-up and handing over to the salesperson. An agent is most useful in the steps that take effort but carry little risk: gathering public business information, scoring by criteria you set, drafting letters and recording into the system. The steps that are relational and involve decisions should be done by people.
## Design steps
**1. Define the ideal customer profile (ICP).** Industry, size, problem, decision maker. The more specific, the less waste.
**2. Choose lawful data sources.** Prefer people who leave their own details and lists of customers who agreed to receive information. You can research information about companies (websites, business directories), but information tied to a specific person is still personal data. Do not buy lists of personal data.
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
This is the part to read carefully. On Nov 28, 2026 I checked it against Law 91/2025/QH15 and Decree 356/2025/ND-CP as published in the Official Gazette, the consent section of Decree 330/2026/ND-CP on a government website, and Decree 91/2020/ND-CP through the digitally signed copy on a government server. It only summarizes the points relevant to finding and contacting prospects; it is not complete and it is not legal advice. **Read the original texts or ask a lawyer before deploying.**
**Personal data** (Law 91 and Decree 356, both in force from Jan 1, 2026):
- **Broad scope.** Personal data is information that identifies or helps identify a specific person. Decree 356 lists names, phone numbers, contact addresses and digital account information as basic data. So the name and phone number of a contact at a company are still personal data. In Article 19 of the Law (cases that need no consent), I did not find a specific case for data merely because it is already public.
- **Consent** must be voluntary, with the person knowing the types of data, the purposes, who processes it and their rights; it is given per purpose and must be verifiable. **Silence or no reply is not consent.** Consent must not be set by default, and in a dispute you carry the burden of proof. The Law has some cases that need no consent (Article 19).
- **Buying and selling personal data is banned,** unless a law provides otherwise (Article 7).
- **Advertising** (Article 28): processing customer data to run an advertising service business requires the customer's consent, with the customer knowing the content, method, form and frequency, and having a way to refuse. Using data to advertise must also follow the anti-spam and advertising rules. Behavioral, targeted or personalized advertising has extra conditions, for example tracking a website or app to collect data only with the person's consent.
- **Requests to stop.** When a person withdraws consent, asks for restriction or objects through the proper procedure, Decree 356 requires a response within 2 working days and action within 15 days (20 days if a processor or third party must be told to stop), extendable once by up to 15 days, except in cases that need no consent. Sending advertising itself must stop immediately (see below).
- **Sending data abroad.** Using a platform outside Vietnam to process personal data collected in Vietnam counts as a cross-border transfer (Article 20), so **a foreign AI or cloud service used by your agent may fall under it**. You then need an impact assessment dossier, sent to the competent authority within 60 days of the first transfer, apart from the exceptions in the Law and Decree 356. The relief for small businesses, startups and household businesses in Article 38 concerns Articles 21, 22 and clause 2 of Article 33, and does not mention Article 20.
- **Penalties.** The Law sets maximum fines: 10 times the revenue from the violation for trading data; 5% of the previous year's revenue for cross-border transfer violations; VND 3 billion for other violations (where the revenue-based figure is lower than VND 3 billion, the VND 3 billion maximum applies). These maximums are for organizations; for individuals they are half. Decree 330/2026/ND-CP (in force from Aug 19, 2026) sets fines per act, for example VND 30 to 50 million for one group of consent violations and VND 50 to 70 million for treating silence as consent. Check the decree for the amount that applies to your case.
**Advertising text messages, emails and calls** (Decree 91/2020). The decree defines advertising as a message, email or call introducing products or services for profit; the definition does not exclude letters written for one person or sent in small numbers, so **treat sales outreach as advertising**:
- **Prior consent is required** before sending advertising messages or emails or making advertising calls, for example the person signs up on your form, website, app or social media.
- **Do-not-call (DoNotCall) list:** you must check it, and may not make advertising calls or send sign-up or advertising messages to numbers on it. For numbers not on the list, you may send only **one first and only advertising sign-up text message**; if the person refuses or does not reply, you may not text again. This exception is written for text messages, not for email.
- **Limits,** unless agreed otherwise with the recipient: within 24 hours at most 3 texts to a number, 3 emails to an address and 1 call to a number; texts only from 7:00 to 22:00, calls from 8:00 to 17:00.
- **Advertising texts and calls require a registered sender name (brandname);** ordinary phone numbers may not be used.
- **Advertising texts and emails** must both be labeled [QC] or [AD] and offer a way to opt out. Emails must also give information about the advertiser and have a clear opt-out section at the end. When the recipient refuses you must stop immediately; keep sign-up and refusal records for at least 1 year.
The Ministry of Public Security has sought comments on a draft decree to replace Decree 91 (reported on the government portal in September 2026). As of Nov 28, 2026 my searches had not found that a replacement had been issued. Check again before you act.
## Safe design principles
- **Collect only the data necessary** for a clear purpose.
- **Prefer business information** over personal information.
- **Get consent** before sending advertising content, and keep evidence of consent.
- **Always provide a visible way to opt out,** and handle opt-out requests quickly.
- **Give users the right** to view, correct and delete their data.
- **Secure the data:** set permissions, and do not store it casually in tools with unclear policies.
- **Do not use the agent to impersonate** or to make people think they are talking to a real person when that matters.
## Technical risks of the agent
- An agent that reads web content or mail can be hit by injected malicious instructions, see [Evaluating AI agents through real tests: which criteria to look at](danh-gia-ai-agent-qua-bai-test-thuc-te-nhin-vao-tieu-chi-nao.html).
- The agent can invent details about the recipient, discrediting the letter. Always check before sending.
- Bulk sending is easily flagged as spam and damages your domain's reputation.
## How to start small
1. Choose a narrow customer group.
2. Use the agent to gather and score from public business information.
3. Review and send by hand a small number of letters with real value, **only to people who have agreed to receive them** (sending by hand or in small numbers does not remove this requirement).
4. Measure the responses, and only then automate more steps.
If you work with company data, see also the way to classify data in [How should an AI tool library be organized to be easy to use?](mot-kho-cong-cu-ai-nen-duoc-to-chuc-nhu-the-nao-de-de-dung.html).
