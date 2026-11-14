# Merlin router operations

Practical lessons from hardening and maintaining an Asuswrt-Merlin/GNUton router with an AiMesh node, Entware and community addons.

The aim is local control, reliable recovery and fewer manual repairs after updates. Necessary external DNS, VPN, time, reputation and software-update services remain allowed. Each change should have a clear purpose, a scoped rollback and evidence that unrelated network paths still work.

This is a sanitised engineering reference. It is not a copy of a live router, a universal configuration or an unattended installer. No raw backups, device inventories, network addresses, credentials, certificates, private logs or original maintenance exports are included. Hardware-specific observations are presented as lessons to verify on another installation, not proof that another router is secure.

## Start here

| Topic | Guide |
|---|---|
| Boundaries that maintenance must preserve | [Design and invariants](docs/01-design-and-invariants.md) |
| Encrypted DNS, DNSSEC and local control | [Unbound and DNS](docs/02-unbound-and-dns.md) |
| Administrator access, credential storage and mesh | [Administration and AiMesh](docs/03-administration-and-aimesh.md) |
| Code ownership, safe writers and update review | [Permissions and updates](docs/04-permissions-and-updates.md) |
| Recovering after local faults and boot delays | [Recovery and reboot](docs/05-recovery-and-reboot.md) |
| Verified local backups and scoped rollback | [Backup and restore](docs/06-backup-and-restore.md) |
| WAN firewall, guest isolation and port mapping | [Network boundaries](docs/07-network-boundaries.md) |
| Diversion, Skynet and necessary vendor services | [Filtering and external services](docs/08-filtering-and-external-services.md) |
| Roaming, resource use and package checks | [Health and performance](docs/09-health-and-performance.md) |
| What changed, what was tested, what remains uncertain | [Decision and evidence record](docs/10-decisions-and-evidence.md) |
| Client-side encrypted off-router backups | [Backblaze B2 design](docs/11-backblaze-b2-design.md) |
| Keeping this repository safe to publish | [Publication policy](docs/12-publication-policy.md) |

The [activity ledger](docs/14-activity-ledger.md) reconciles implemented changes, investigations, superseded steps and open work. Its review boundary is 14 November 2026; it is not a live status feed. Private source records and recovery artifacts remain separate.

## Tools and examples

- [Local publication checker](tools/check_publication.py): checks the explicit publication allowlist, suspicious file types, personal-address patterns and common secret formats. It can also use a private, external denylist. It does not upload files.
- [Read-only router summary](tools/router-readonly-summary.sh): reports selected service and boundary checks without dumping NVRAM, routes, addresses or logs. Inspect it before running it on a compatible router.
- [Unbound settings example](examples/unbound-settings.conf.example): illustrative settings with reserved documentation addresses. It is deliberately unsuitable for direct deployment.
- [Change checklist](examples/change-checklist.md): a review and validation template.

Run local checks with Python 3 and a POSIX shell:

```sh
python3 tools/check_publication.py .
python3 -m unittest discover -s tests -v
sh -n tools/router-readonly-summary.sh
```

The included tools were checked locally. The router summary is a new generic adaptation; it was not deployed or used to change a router. Site-specific production scripts and third-party addon source are deliberately excluded. Public documentation cannot restore a router; private recovery material must be kept separately.

## Reading the evidence

The work behind these notes included configuration comparisons, positive and negative DNS/TLS tests, isolated failure fixtures, service recovery, one controlled main-router reboot, package verification and checks on both mesh devices. It did not include an independent internet penetration test, a full bare-device restore or exhaustive guest-client and roaming tests. Each guide keeps those distinctions visible.

Software versions and package availability change. Verify the exact installed build, architecture and current official feed before applying a recommendation. See [primary references](docs/13-references.md).

Original documentation and tools in this repository are available under the [MIT license](LICENSE). Third-party projects retain their own licenses and support boundaries.
