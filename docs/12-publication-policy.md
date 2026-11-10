# Publication policy

This repository is assembled in a new directory using an explicit file allowlist. It is not created by copying a private working directory and attempting to redact it afterwards.

## Excluded material

- Router exports, NVRAM, JFFS/USB archives and package rollback bundles.
- Passwords, password hashes, SSH/VPN keys, certificates, cookies, tokens and cloud credentials.
- Actual WAN/LAN addresses, MAC addresses, SSIDs, device names, hostnames and household schedules.
- DHCP leases, reservations, VPN peer inventories, routing/firewall dumps and query logs.
- Screenshots, terminal recordings, private source manifests and original maintenance reports.
- Personal names, email addresses, local home paths, account identifiers and conversation transcripts.

GitHub necessarily displays the account that owns a public repository and may associate publication with its authenticated account. Sanitising files does not make the hosting account anonymous. Initial Git author/committer metadata uses a generic project identity rather than a local personal Git configuration.

## Before publishing

1. Review every allowlisted file, including comments and links.
2. Run the publication checker and its regression tests.
3. Scan against an external private denylist of known site identifiers; do not copy that list into the repository.
4. Check staged paths, binaries, symlinks, commit author/committer metadata and complete Git history.
5. Confirm that no source working-directory history or private artifacts were imported.
6. Publish only the reviewed tree, then verify remote visibility and the published commit.

The checker is a guardrail, not a complete data-loss prevention system. It detects selected patterns and known terms, not every secret or identifying detail. Passing it is not a security attestation.

## Future contributions

Use reserved documentation addresses and generic roles. Describe the class of problem, supported fix, validation and limitations. Keep raw evidence private. Avoid screenshots of router pages even when obvious passwords are masked: titles, hostnames, device lists and URLs can still identify a household.

If a secret is published, revoke or rotate it promptly. Deleting it in a later commit does not remove it from Git history, caches or existing clones. A public repository is never an appropriate location for real backup material, even if encrypted.
