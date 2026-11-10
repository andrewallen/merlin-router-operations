# Health and performance

## Measure before tuning

Capture a bounded sample of CPU, memory, storage, temperature, uptime, critical processes, recent errors and mesh reachability on both devices. Free memory alone can mislead: reclaimable cache and actual memory pressure matter. Load average is not the same as CPU utilisation.

Look for out-of-memory events, crashes, USB disconnects and filesystem errors. Identify the failing component before adding a watchdog or reboot schedule. Frequent monitoring can itself become a material workload on a small router.

## Roaming needs correlated evidence

Client deauthentication logs can reflect ordinary roaming, power saving, weak signal or a fault. Cumulative retry counters are not end-to-end packet-loss rates. A mesh backhaul ping tests only one part of a client's path.

To investigate a real dropout, capture the affected client, time, association on both nodes, signal quality, channel/radar events, retries and connectivity. Avoid publishing client identifiers in an issue or report. Consider changes to thresholds, channel width or backhaul only after there is a repeatable observation and a rollback.

The original investigations did not establish one definitive cause of all intermittent roaming dropouts. Removing an unrelated addon or seeing healthy mesh pings did not prove that roaming was fixed.

## DHCP reservations are operational tools

Reserve addresses for permanent devices, infrastructure and clients referenced by special rules. Avoid reserving every transient or unidentified client. Reconcile existing reservations, leases and private MAC addresses before editing.

A reservation improves predictability; it is not device authentication or network isolation. After changing a VPN client's address or policy, verify the actual source-based route and tunnel DNS rather than relying on its display name.

## Package checks need fresh metadata

A local package index may lag the official feed. Compare the architecture-specific index, package archive digest and installed versions. A package release-suffix change may fix packaging rather than an upstream vulnerability; inspect the maintainer change.

After a shared-library update, inspect process mappings under both symlinked and canonical storage paths. Restart required consumers with maintenance descriptors closed. Verify actual runtime library use, not just the package database.

Firmware, Entware and addons have different release channels. A newly published firmware beta for another model is not an applicable update. Updating Entware does not patch firmware-linked services, the kernel or wireless drivers.

## Expect restart hooks

A firewall restart can reapply FlexQoS, flush connection tracking, restart port mapping and trigger YazFi reauthentication. Inspect the final state after asynchronous hooks finish. Document brief service effects and compare classification rules separately from routing and security rules.

One observed VPN hook appended a duplicate NAT rule for disabled IPv6. IPv6 filter policies remained restrictive and no active IPv6 path was established. Such differences should be explicitly accounted for, not hidden by broad normalisation or advertised as a newly fixed issue.
