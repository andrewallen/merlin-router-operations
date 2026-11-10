# Design and invariants

Treat a router as several independent traffic paths. A successful query from the administrator's laptop does not establish that every path is correct.

```text
Trusted clients -> local DNS frontend and filtering -> local Unbound -> authenticated encrypted upstream
Router services -> existing router resolver path
Guest clients   -> separate guest policy and intentional external resolver path
VPN clients     -> selected tunnel and its existing DNS policy
Mesh node       -> local administration and backhaul through the main router
```

The diagram describes policy, not a packet-capture finding or a complete firewall diagram. Some addons operate in the frontend while others maintain separate resolver policy data; inspect actual integration rather than assuming every blocklist is processed at the same point.

## Preserve explicit boundaries

- Keep router-originated DNS unchanged when hardening the client resolver.
- Keep guest routing, isolation and its intentional DNS exception unchanged.
- Keep selected VPN policies, tunnel DNS and deliberate destination exceptions unchanged.
- Preserve an intentional, documented DNS fallback. Recovery must respect the selected mode.
- Keep local HTTPS, mesh management and required node checks working.
- Keep AiProtection enabled when that is an explicit requirement. Do not claim all external vendor activity has been removed.
- Treat IPv6 consistently. If unused, verify its runtime addresses, forwarding and firewall state instead of relying on one GUI switch.

Record these as pre-change assertions. Save private configuration snapshots and hashes, then compare after a change. Use hashes to avoid displaying secret-bearing settings.

## Local control does not mean no external connections

Encrypted upstream DNS, software updates, time synchronisation, VPN peers and reputation services may be necessary. Decide which external services are intentional. Identify process ownership and configuration before blocking traffic.

Local administration and local filtering can coexist with those services. A blocklist cannot make a root-compromised router trustworthy, and a VPN does not make the router's administration surface safe.

## Scope one change at a time

Separate persistent settings, generated runtime configuration and observed behaviour. A firmware setting may recreate a deleted runtime rule. A package update may replace a locally patched script. A service may retain an old library until restarted.

Prefer a supported persistent setting over another recurring repair script. Where a local patch is necessary, scope it to exact reviewed versions and document the reason, validation and removal path.
