# Activity ledger

Reconciled through 14 November 2026 against available private change records, investigations, test results and operational decisions. This is a sanitised historical ledger, not an inventory, deployment manifest or live health dashboard. Supporting exports and repeated snapshots are grouped with their underlying activity; individual DNS queries and terminal commands are not public activities.

**Implemented** means a persistent change was applied with the stated tests. **Investigated** means evidence was gathered, without implying a fix. **Superseded** identifies an intermediate state replaced by later work. **Deferred** means considered but not implemented. **Open** identifies an unresolved finding or unperformed acceptance test. No status certifies every device, feature or future boot.

References remain stable when statuses change. Exact affected versions, private source mappings, backup locations and rollback instructions belong in the separate private record. Public ledger updates should retain corrected conclusions and identify which later activity supersedes them.

## Administration, security and maintenance

| Reference | Activity and status | Validation, limits and guide |
|---|---|---|
| OPS-01 | **Investigated:** both-node security, software and configuration assessments | Configuration, listeners, processes, source and boundary reviews; no claim of a comprehensive penetration test. [Administration](03-administration-and-aimesh.md), [boundaries](07-network-boundaries.md). |
| OPS-02 | **Implemented:** privileged code/configuration permission hardening and safe writers | Scoped ownership, unprivileged refusal and creation/update fixtures; includes amtm modules, SSH-key tooling, wireless reporting and shared WebUI libraries. [Permissions](04-permissions-and-updates.md). |
| OPS-03 | **Implemented:** protect recoverable addon credentials without breaking mesh checks | File permissions and addon write paths assessed; authenticated main/node checks exercised. Recoverable storage remains a trust consideration, not password hashing. [Administration](03-administration-and-aimesh.md). |
| OPS-04 | **Implemented:** local HTTPS administration with access recovery | Certificate/reachability and authenticated addon checks; frontend login/session behaviour investigated. No public certificate or access details. [Administration](03-administration-and-aimesh.md). |
| OPS-05 | **Implemented:** disable unused supported remote/cloud access | Supported startup refusal and local management checks; required protection services preserved. [External services](08-filtering-and-external-services.md). |
| OPS-06 | **Implemented:** disable WPS on both nodes | Runtime flags, addon/node access and later regression checks. No assertion of WPA3 or protected-management-frame coverage. [Administration](03-administration-and-aimesh.md). |
| OPS-07 | **Implemented:** remove unused knock addon | Startup, jobs, code/listeners and protected-path checks; unrelated roaming problem not attributed to this removal. [External services](08-filtering-and-external-services.md). |
| OPS-08 | **Implemented:** remove unused node file-sharing exposure | Follow-up node service/security review and preserved mesh access. [Administration](03-administration-and-aimesh.md). |
| OPS-09 | **Implemented:** exact-version addon/update protection and subsequent re-review | Known/unknown code paths, native amtm integration, certificate-hardening re-review after Diversion updates and later policy enrollment. Unknown future code still needs review. [Updates](04-permissions-and-updates.md). |
| OPS-10 | **Implemented:** reviewed Entware/addon maintenance and wireless-report updates | Package/archive/dependency checks, required consumer restarts and both-node regression checks. Not an evergreen all-software-current claim. [Health](09-health-and-performance.md). |
| OPS-11 | **Implemented:** fixed LED schedule and maintenance startup integration | Scheduler/startup inspection; exact household timing remains private. [Updates](04-permissions-and-updates.md). |
| OPS-12 | **Implemented:** persistent WAN-default correction | Matching-build source and effective rules checked; no independent external port scan. [Boundaries](07-network-boundaries.md). |
| OPS-13 | **Implemented:** minimum external automatic-mapping ports with required mapping retained | Positive/negative NAT-PMP tests and cleanup; client inventory and remote application testing remain incomplete. [Boundaries](07-network-boundaries.md). |
| OPS-14 | **Investigated:** outbound vendor services; retain required protection daemon | Process/socket and supported-setting assessment; no unsupported recurring kill job or vendor-connection-free claim. [External services](08-filtering-and-external-services.md). |
| OPS-15 | **Investigated:** reported kernel vulnerability applicability and package/backport boundaries | Matching implementation/version/source assessment supported no specific workaround at the time; not vendor certification or proof of general kernel safety. Reassess for changed firmware/advisories. [Patching](02-unbound-and-dns.md). |

## Filtering and client paths

| Reference | Activity and status | Validation, limits and guide |
|---|---|---|
| OPS-16 | **Implemented:** OISD Big general filtering | Native list update, normal/blocked resolution and preservation checks. No complete advertising or telemetry elimination promise. [Filtering](08-filtering-and-external-services.md). |
| OPS-17 | **Implemented:** Diversion download certificate verification | Main/helper paths, invalid certificate/plain HTTP refusal and last-good-data tests; later addon replacements re-reviewed under OPS-09. [Filtering](08-filtering-and-external-services.md). |
| OPS-18 | **Implemented:** selected Skynet hardening and retained filtering | Active rule/ipset and preservation checks; IP filtering is distinct from domain filtering and cannot inspect ultimate destinations inside a relay. [Filtering](08-filtering-and-external-services.md). |
| OPS-19 | **Implemented:** selected DHCP reservations and streaming-client VPN policies | Lease/policy/source-route checks; unidentified/transient devices deliberately not all reserved. Address reservations are not authentication. [Health](09-health-and-performance.md). |
| OPS-20 | **Implemented:** selected TV local DNS while preserving its VPN data path | Local resolution/filtering and tunnel tests; user confirmed normal app use at the relevant stage. [DNS](02-unbound-and-dns.md). |
| OPS-21 | **Implemented:** HaGeZi Samsung hosted subscription | Feed-to-generated-rule comparisons, positive/blocked tests and preserved policy. Not every television feature tested. [Filtering](08-filtering-and-external-services.md). |
| OPS-22 | **Investigated and closed with scope limits:** TV streaming failures | List pause, individual exceptions and provider-DNS trials did not resolve tested failures; temporary non-VPN traffic did. Temporary exceptions removed and Samsung list restored. Supports an exit/location-path explanation, not a universal streaming diagnosis. [Filtering](08-filtering-and-external-services.md). |
| OPS-23 | **Implemented:** local filtered DNS across selected router-managed WireGuard paths | Native tunnel DNS overrides removed; policy/data routes preserved. Live DNS evidence for active clients; unassigned tunnels and every client not individually exercised. [DNS](02-unbound-and-dns.md). |
| OPS-24 | **Investigated:** representative client DNS enforcement and encrypted bypasses | Wired/node/main Wi-Fi samples and hardcoded-external-DNS translation; controlled node tests. Candidate relay IPs are not proof of query contents. Browser preference access was denied; no circumvention. [DNS](02-unbound-and-dns.md). |
| OPS-25 | **Implemented:** main-network Private Relay discovery block | Two documented names, UDP/TCP and A/AAAA/HTTPS negative tests; normal Apple services, node paths, isolated fallback generation and user browsing/notice confirmation. Guest/router exceptions and VPN routes retained. Native frontend restart also restarted firmware DNS proxy. [Policy](08-filtering-and-external-services.md). |
| OPS-26 | **Investigated:** guest boundaries and intentional resolver bypass | Bridge/rule/driver and configuration comparisons; external resolver positive test. Exhaustive live guest-client and transition testing remains open under NEXT-02. [Boundaries](07-network-boundaries.md). |

## Resolver reliability and provider decisions

| Reference | Activity and status | Validation, limits and guide |
|---|---|---|
| OPS-27 | **Implemented:** authenticated upstream DoT, DNSSEC and explicit fallback | Valid/invalid DNSSEC and TLS tests, frontend and socket checks. Only the upstream leg is encrypted by this design. [DNS](02-unbound-and-dns.md). |
| OPS-28 | **Implemented:** protected configuration/state split and local control socket | Ownership, privilege-drop, reload/control operations and socket recreation. [DNS](02-unbound-and-dns.md). |
| OPS-29 | **Implemented:** bounded local recovery, boot ordering and explicit intent | Fixtures, controlled local faults and an earlier controlled main-router reboot. Later revisions not covered by that reboot; no separate node reboot or full restore. [Recovery](05-recovery-and-reboot.md). |
| OPS-30 | **Superseded:** interim Unbound package while official feed lagged | Provenance/architecture/rollback review; replaced by verified official package under OPS-31. No recommendation to keep pinning the interim binary. [Patching](02-unbound-and-dns.md). |
| OPS-31 | **Implemented:** return to official Unbound package | Published binary/feed/archive checks and runtime library/service validation. Later package state checked during maintenance; source release alone does not prove binary availability or complete patch coverage. [Patching](02-unbound-and-dns.md). |
| OPS-32 | **Investigated / targeted action completed:** detached log and upstream retry-state incident | Log reopened and infrastructure cache cleared. DNS had already recovered before intervention; cause and recovery attribution remain unknown. [Recovery](05-recovery-and-reboot.md). |
| OPS-33 | **Implemented, initial gaps superseded:** log rotation repair and upstream monitoring | Initial interactive result did not establish cron success; OPS-35 corrected that. Negative probes alone were insufficient; positive record coverage and deadlines added later. [Recovery](05-recovery-and-reboot.md). |
| OPS-34 | **Implemented:** narrow automatic upstream retry-state repair | Repeated-condition checks, direct verified upstream success, locking, budgets, gates and failure fixtures. No induced production upstream outage or live automatic repair was needed. Later pending confirmation improved under OPS-35. [Recovery](05-recovery-and-reboot.md). |
| OPS-35 | **Implemented:** collector cron repair, DNS record correction and monitor completion | Actual cron validation, private temporary state, database error propagation, command/run deadlines, signed A/AAAA/HTTPS tests, stale warning and pending repair status. Repaired broad IPv6-address filtering while transport stayed IPv4-only. [DNS](02-unbound-and-dns.md), [recovery](05-recovery-and-reboot.md). |
| OPS-36 | **Investigated / decision implemented:** upstream comparison and Quad9 selection | Bounded Cloudflare/Quad9/AdGuard non-filtering benchmark; verified Quad9 DoT migration, matching recovery assertions and preservation checks. Intermittent failures remain open under NEXT-01. [DNS](02-unbound-and-dns.md). |
| OPS-37 | **Deferred:** replace upstream DoT with DoH | Additional forwarding service and operational dependencies not justified by observed benefit. No installation or transport change. [DNS](02-unbound-and-dns.md). |
| OPS-38 | **Deferred:** encrypted DNS between clients and router | Local frontend, certificate/client compatibility and failure-policy options assessed. No listener or client profile deployed; preserve Diversion before Unbound if revisited. [DNS](02-unbound-and-dns.md). |
| OPS-39 | **Investigated:** recurring both-node health/performance and roaming checks | Resource, kernel log, mesh and protected-policy samples. Weak-signal events remain; healthy short pings do not establish roaming reliability. [Health](09-health-and-performance.md). |
| OPS-40 | **Implemented locally / cloud deferred:** verified backups and scoped rollback | Private archives, hashes and representative extraction tests. No bare-device restore or B2 upload established. [Backups](06-backup-and-restore.md), [B2](11-backblaze-b2-design.md). |
| OPS-41 | **Implemented:** sanitised public engineering reference and consolidated ledger | Explicit allowlist, private reconciliation, publication tests, changed-tree/history/metadata review and remote read-back. Public documentation is not a deployable backup. [Publication](12-publication-policy.md). |

## Open work and acceptance criteria

These references track work without implying authorisation to change the router. Priorities depend on symptoms and recovery requirements.

| Reference | Status and next work | Completion evidence required |
|---|---|---|
| NEXT-01 | **Open:** intermittent encrypted upstream failures and one domain-specific AAAA failure | Bounded, correlated direct/local observations; distinguish provider/path/tool faults and record impact. Do not infer causality from a subsequent passing probe. |
| NEXT-02 | **Open:** guest isolation tests from real clients | Intended permitted/denied traffic, both nodes where applicable, and addon restart/boot transitions with recovery available. |
| NEXT-03 | **Open:** user-visible roaming investigation | Correlate the affected client's incident time with both-node association, signal/backhaul and channel events before any tuning. |
| NEXT-04 | **Open:** safe SSH key staging, then possible password restrictions | Both-node key access, dependent addon checks and tested local recovery before restrictions. |
| NEXT-05 | **Open:** optional management-device restrictions and mapping allowlist | Reliable client inventory, necessary service/mesh exceptions and recovery tests; avoid broad firewall edits first. |
| NEXT-06 | **Open:** independent device tunnel, Private Relay and browser-DNS coverage | Identify unknown devices privately, inspect intended per-device settings where authorised and test actual paths. Private Relay block does not enforce all encrypted DNS. Direct-query timeout causality remains unproven. |
| NEXT-07 | **Open:** post-revision reboot and restore coverage | Controlled startup checks for later changes, and a separate documented restore drill. Existing backup and earlier reboot evidence do not complete these tasks. |
| NEXT-08 | **Deferred / next design task:** encrypted B2 backups | Select upload host and restricted credentials; test upload, denied operations, download/decrypt, extraction, failures, retention and recovery-key access before scheduling. No cloud resources created. |
| NEXT-09 | **Ongoing:** exact-platform patch and addon review | Fresh architecture-specific published binaries, exact-model firmware support and reviewed addon changes. Do not treat Entware updates as kernel/driver patches. |

## Keeping the ledger useful

For each future activity, record its reference, purpose, status, components, preserved boundaries, validation, rollback availability and unresolved follow-up. Reconcile the private evidence before marking completion. Do not publish raw commands, household identifiers, schedules, deployment paths, credentials or logs. Investigations that result in no change still belong here; temporary experiments must have a recorded final disposition.
