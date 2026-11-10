# Filtering and external services

## Diversion and Skynet serve different purposes

Diversion blocks matching DNS names in the paths that actually traverse its integration. Skynet applies network-address filtering. Neither guarantees that an application is free of advertising, telemetry or malware, and neither contains a compromised administrator.

Devices using an intentional guest resolver, VPN DNS or their own encrypted DNS may follow different filtering paths. Do not claim whole-network coverage based on one trusted-LAN DNS test. Advertising delivered from the same domains as wanted content may be difficult to block without breaking functionality.

## Blocklist changes need recovery and tests

The work included changing Diversion's general-purpose list to OISD Big, with the prior list configuration backed up and the native update path exercised. A separate device-specific list was left as a distinct decision.

Choose lists for a clear purpose, maintenance quality and acceptable false-positive rate. Record exceptions with a reason. When a home-automation device stops connecting, compare timing, DNS failures, list matches and actual routing before blaming the most recent unrelated change.

Check resource use and query behaviour after a list expansion. Keep known-good data if downloading or parsing a replacement fails. The absence of a public test domain can change over time; use an entry confirmed in the currently installed list for a blocking test.

## Download verification includes helper code

The main downloader can validate TLS while a secondary helper uses an insecure flag. Review the complete download path: list fetching, hosted-list management, metadata and hashes, redirects and updater configuration.

The reviewed hardening removed certificate bypasses and required HTTPS for the relevant helpers. Tests included a valid feed, an incorrect certificate and plain HTTP, with preservation of the prior list after failure. The exact addon version was then added to the local reviewed update policy. Blindly reapplying that patch to future versions was not permitted.

## Classify external services before disabling them

The work separated unused ASUS remote/cloud access from AiProtection, time, updates and encrypted DNS. The supported force-disable setting was used for an unused cloud tunnel, and native startup refusal was tested. Local administration and node checks were preserved.

An idle process is not proof of an active connection. An observed connection is not proof of its complete payload or purpose. Inspect process ownership, sockets, firmware wrappers and documented settings before proposing a change.

The assessment of a vendor data-collection daemon did not establish a safe, independent persistent switch that preserved required features. It was left unchanged rather than disabled through an unsupported recurring kill job. AiProtection was intentionally retained; therefore the result was not a vendor-connection-free router.

## Remove unnecessary privileged features

An unused knock addon was assessed and removed after backup, including its startup/scheduler integration. The lesson is broader than its name: unauthenticated network events must not be allowed to trigger sensitive actions without a carefully justified trust boundary. Restricting the obvious WAN route alone may leave local, tunnel or loopback entry paths.

Removal was followed by service and policy checks. It did not establish the cause of a separate WiFi-roaming problem.
