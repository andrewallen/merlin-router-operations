# Decision and evidence record

This summarises categories of work without retaining live addresses, exact device inventories, schedules, secret-bearing output or deployment identifiers. It is a historical record, not a current health attestation for any router.

| Area | Decision or implementation | Evidence and limits |
|---|---|---|
| DNS transport | Authenticated encrypted upstream DNS, DNSSEC and no automatic plaintext recursive fallback | Valid and invalid DNSSEC/TLS tests; frontend queries; upstream sockets |
| Resolver permissions | Separate administrator-owned configuration from mutable daemon state | Ownership, reload and restoration checks |
| Control channel | Restrict local resolver control using a protected Unix socket | Control operations, TCP-listener absence, restart/socket recreation |
| Local recovery | Explicit intent, bounded retries, prerequisite checks and recognised frontend repair | Isolated fixtures, controlled resolver/frontend failure tests |
| Boot robustness | Avoid blocking time service behind encrypted-DNS startup | Controlled main-router reboot and automatic service return; node not separately rebooted |
| Backups | Verified private local snapshots before retention; scoped rollback for maintenance | Archive checks, digests and representative extraction/metadata tests; no bare-device restore |
| Privileged addon code | Remove unnecessary write access and repair unsafe writers | Scoped permissions, creation fixtures and real unprivileged write-refusal tests |
| Updates | Exact-version review guard; unfamiliar replacements require review | Known-original and unfamiliar-code fixture paths; post-update policy comparisons |
| Local administration | HTTPS with tested local access and emergency recovery | Reachability, certificate checks and authenticated main/node addon workflows at relevant stages |
| Cloud access | Disable unused supported remote/cloud tunnel path | Native startup refusal; local administration and required vendor protection retained |
| Download trust | Remove insecure helper paths and validate maintained trust store | Positive and negative certificate tests; last-good-list preservation |
| Blocking | General-purpose OISD Big list and existing Skynet protection | Native update, ordinary/blocking DNS tests and active network rules; no promise of complete ad/telemetry elimination |
| Unused services | Remove unused knock addon; disable unused node file sharing; disable WPS | Hooks, jobs, listeners, relevant runtime flags and node health checks |
| DHCP and VPN | Reserve selected permanent/special-policy devices; verify chosen tunnel paths | Before/after leases/policy and source-route checks; no public inventory retained |
| Official packages | Evaluate interim build, then return to a verified official package | Architecture/feed/version/archive checks and runtime dependency/service validation |
| Schedules | Fixed LED timing and named maintenance jobs | Scheduler/startup inspection; no public household schedule retained |
| WAN default | Replace broad WAN-to-LAN allowance using its persistent firmware setting | Exact-build source, generated/live rules, zero observed old-rule counter hits and protected-path regression checks |
| Automatic mapping | Keep Tailscale-compatible mapping; exclude low external ports | Live NAT-PMP low/high-port tests and cleanup; no remote Tailscale session test |
| Guest | Preserve independent routing/DNS and effective isolation | Bridge, firewall and driver checks; no exhaustive two-client or transition testing |
| Roaming | Observe and correlate before tuning | Mesh/service samples and radio/log inspection; no universal root cause established |

## Open recommendations

- Restrict trusted-LAN administration to selected management devices after establishing a safe recovery route.
- Complete a reliable automatic-mapping client inventory before applying a device allowlist.
- Test guest boundaries from actual clients, including addon restart and boot transitions.
- Capture a user-visible roaming incident with correlated evidence from both nodes.
- Track exact-model firmware support and patch coverage independently of Entware.
- Add encrypted off-router backups and perform a documented restore drill.
- Establish tested key access and update dependent checks before reducing password authentication.

## Evidence discipline

A configuration comparison proves preservation of the compared configuration. A live probe proves the sampled path worked at that time. An isolated fixture proves the exercised control flow. A successful reboot proves one startup sequence on one device. None of these alone proves an absence of vulnerabilities or complete disaster recoverability.

Private raw evidence and recovery material are intentionally outside this repository. Reproducing the work requires fresh local baselines, exact-source review and site-specific tests.
