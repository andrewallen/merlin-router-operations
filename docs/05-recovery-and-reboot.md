# Recovery and reboot

## Respect administrator intent

Store explicit resolver intent separately from process health. Supported modes can distinguish normal Unbound operation from an intentional fallback. Missing or invalid intent should produce a clear status, not an invented DNS direction.

A supervisor must not restart a deliberately stopped service when fallback or a maintenance pause is selected. It must not silently choose a public resolver or reboot the router to conceal repeated failures.

## Avoid startup deadlocks

Encrypted DNS needs correct time. Time synchronisation may itself depend on startup order and existing resolver paths. A DNS init script that blocks the Entware sequence while waiting for time can prevent the later time service from starting.

Exit promptly when USB, Entware or time is not ready. Retry later through a bounded supervisor. Do not consume the restart budget while prerequisites are unavailable.

## Detect local failures locally

A local-only canary can distinguish a dead resolver from a broken external upstream. Check the expected process identity, listener, valid configuration and frontend integration. Validate a PID before signalling it.

Use repeated failure confirmation, boot grace, cooldowns and an hourly restart cap. A running but unresponsive daemon deserves different handling from a missing daemon. Invalid configuration should block a restart and surface an actionable error.

Frontend repair should require explicit intent and recognised hooks. Regenerating DNS configuration can briefly affect shared DNS/DHCP, so it needs a tighter policy than simply restarting one resolver.

## Test recovery at different levels

| Test | What it establishes |
|---|---|
| Isolated fixtures with stubbed service actions | Control flow, pause/mode handling, prerequisites, cooldown and rate limits |
| Controlled resolver stop | Actual local daemon recovery and socket recreation |
| Controlled frontend integration failure | Actual repair of a recognised generated configuration |
| Controlled main-router reboot | Startup ordering and service return on that device |
| Full bare-device restore | Disaster recovery; not established by the other tests |

The original work included the first four categories at different maintenance stages. It did not include a full bare-device restore or a separate controlled reboot of the mesh node. No single test guarantees that rebooting fixes hardware failure or persistent compromise.

Keep a status file and useful local logs. Avoid external notifications unless explicitly configured. A healthy message should say which path was tested and which mode is selected.

## Upstream failures require a separate recovery policy

A targeted repair reopened a detached log and cleared infrastructure retry state. A successful lookup had already occurred before intervention; the original outage's resolution cannot be credited to that manual repair. The initial cause remains unknown.

Subsequent monitoring combines local validation tests, direct certificate-checked upstream probes and infrastructure retry state. Local negative answers can reuse cached denial proofs. Direct probes establish the tested upstream path, not attribution of a specific client query. Include signed positive record types, per-probe results and a separate stale-completion warning so a single generic healthy label does not hide reduced redundancy or a stuck monitor.

The narrow automatic action requires repeated confirmation that both known upstream retry states are exhausted while local DNS works and at least one authenticated direct upstream query succeeds. Recheck expected mode, process identity, configuration, time, storage, pause/disable gates and shared locking immediately before action. Record an attempt before clearing infrastructure retry state; budget-write failure prevents action. Apply cooldowns and a rolling cap, counting failed attempts too. Runtime budgets stored in RAM reset at reboot; they are not durable cross-reboot rate limits.

This action does not flush ordinary answer caches, restart services, switch providers, activate fallback or reboot. A general upstream outage, certificate failure or validation-only failure does not qualify for this repair. After a reset, report pending until a later full check and new upstream activity confirm progress. Resolver-wide counters do not prove the exact transaction of one probe.

## Collector, log rotation and real scheduler tests

A collector can work interactively but fail under cron because inherited library overrides select firmware libraries for Entware programs. Clear inherited library overrides in the relevant helper, retain intended executable selection, and test in the actual cron environment. An early interactive success was superseded by a later cron failure and repair; retain that correction in the evidence record.

Serialize collector and recovery work where needed. Use private per-run temporary state, propagate database errors, bound individual operations and the whole run, and release locks after deadlines. Check helper availability on the actual firmware: a common temporary-file utility was absent in this deployment. Validate the replacement using private directory creation and unpredictable names.

Check that the visible log inode is the one held by the validated daemon. Reopen only a recognised detached log, rather than reopening every minute. A collector completion message should represent actual completion, not merely dispatch. Tests exercised SQL failure, overlap, stale status, command/run deadlines, repair gates and pending confirmation using isolated fixtures. Actual cron collection and healthy scheduled probes passed. The later monitoring revisions and provider migration have not had a new controlled reboot test.
