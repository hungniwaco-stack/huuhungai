---
title: OpenClaw Computer Use: letting an agent operate a computer safely
desc: Computer Use and browser control in OpenClaw: how to turn them on, OS permissions, the risks the docs state, blocking configuration and a minimal safe setup.
min: 8
---
QUICK: OpenClaw lets an agent see and control the screen through the `computer` tool, and control a real browser. The documentation warns plainly: there is no confirmation for each action, macOS protection layers are only "hardening" and not an isolation boundary, and content on screen can contain injected instructions. Turn it on only when needed, use a separate browser profile and keep every control port inside a private network.
## Two different capabilities
- **Computer Use:** a `computer` tool that lets the agent see and control the screen of the machine running the Gateway or of a paired node. A model with vision controls the interface.
- **Browser control:** the agent operates a real browser, with the sign-in sessions already in the profile.
Both have a big impact: the documentation calls browser control operator access to everything that browser profile can reach.
## Platforms and how to turn on Computer Use
- **macOS:** uses Peekaboo (the default) or CUA, chosen at Dashboard, Settings, This Mac, Capabilities. It needs the Accessibility and Screen Recording permissions for OpenClaw.
- **Windows (x64, ARM64) and Linux glibc (x64, ARM64):** an optional, experimental `cua-computer` plugin.
- **The Gateway machine:** use `cua-computer` on the Gateway host; a headless Linux Gateway can use a managed virtual display.
Enable the plugin and check:
```
openclaw plugins enable cua-computer
openclaw doctor --lint --only cua-computer/driver-artifacts
```
For the agent to use this tool with the `coding` profile, it must be explicitly allowed:
```
{
  tools: {
    alsoAllow: ["computer"],
    sandbox: { tools: { alsoAllow: ["computer"] } },
  },
}
```
To block the control command outright:
```
{
  gateway: { nodes: { commands: { deny: ["computer.act"] } } },
}
```
## What the documentation says about risk
- **No confirmation for each action** on macOS. Approval happens at the pairing level: the Gateway approves the set of commands the node advertises.
- macOS's native protection layers are "hardening, not an isolation boundary".
- **Do not combine** the ask-for-confirmation exec mode with unrestricted Computer Use for a model you do not trust.
- Unrestricted CUA mode does not prevent a user account from being taken over; a process under the same user can reach the driver's socket.
- **Content on the screen is untrusted**, and may contain injected instructions (prompt injection).
- Screenshots are kept "for the model only" and are not sent into chat channels on their own, meaning they enter the model's context. The documentation does not list whether other data (such as the accessibility tree or window metadata) is sent to the provider, so assume anything on the screen may reach the model provider.
## Technical limits to know
On Windows and Linux only the main screen can be controlled; some key-holding or drag-and-drop actions are rejected; old coordinates go stale when the screen changes so the agent must capture again. macOS needs an unlocked screen; the keep-awake mode only covers one run for up to an hour.
## Browser control: the documentation's recommendations
- Use a **separate profile for the agent** (such as the default `openclaw` profile), not your everyday personal browser profile.
- For an agent running in a sandbox, keep host browser control off unless you trust it.
- Turn off browser sync and the password manager in the agent's profile if possible; keep the downloads folder isolated.
- Keep the Gateway and node machines **only inside the tailnet**, with the browser control port not exposed to the LAN, the internet or Tailscale Funnel. Pairing a node is equivalent to admin access.
- The Chrome "Existing session" mode is **not safer**: it can act as you on every page the host Chrome profile can reach.
- With the Chrome extension, choose **Selected tabs** to limit it to OpenClaw's tab group instead of All tabs.
Masking password fields, one-time codes and cards in screenshots helps reduce accidental exposure but does not replace a separate profile.
## Browser SSRF blocking
The default is strict: private, internal and special addresses are blocked unless you deliberately open them (`browser.ssrfPolicy.dangerouslyAllowPrivateNetwork`). You can block by hostname (`blockedHostnames`, and remember that `*.example.com` does not block the root domain). The documentation also states the limit plainly: this is not a network firewall, and many paths (pop-ups, Service Workers, `fetch`, subresources, tabs not yet acted on) can get around it; to block fully you must isolate outbound traffic or use a policy-enforcing proxy.
## A minimal safe setup
1. Do not turn on Computer Use if your work does not need it yet. Start with the file and web tools.
2. If you turn it on, use a separate machine or user account, not the machine holding your main data.
3. Use a separate browser profile, not signed in to important accounts.
4. Use the strongest model for an agent with this tool, because small models are easier to steer (see the [security lessons](openclaw-update-bai-hoc-ve-tich-hop-message-cron-va-bao-mat.html)).
5. Run `openclaw security audit` and read the warnings about browser control exposure.
6. Do not let the agent read untrusted content while it has screen control.
