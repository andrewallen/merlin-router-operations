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
