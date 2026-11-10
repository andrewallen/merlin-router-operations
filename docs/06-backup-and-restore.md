# Backup and restore

## Backups contain secrets

Native configuration exports, JFFS, Entware state and addon configuration can contain administrator credentials, WiFi keys, VPN material, certificates, device inventories and history. Keep directories private and files administrator-readable only. File permissions are not encryption.

On-device backup protects against many editing mistakes. It does not protect against USB failure, theft, fire or a root attacker deleting the same storage. Off-router encrypted copies are a separate layer.

## A verified snapshot workflow

1. Confirm the expected USB filesystem is mounted, time is plausible and enough space is available.
2. Acquire a non-overlapping backup lock.
3. Create a private destination and save native settings plus relevant JFFS and USB/Entware content.
4. Exclude swap, transient state and backups themselves. Avoid recursive backup growth.
5. Check archive readability, required members and native settings-file presence.
6. Record cryptographic digests and only then write a completion marker.
7. Apply retention only after a new snapshot is verified.
8. Preserve failure logs and leave the previous good snapshot intact.

A live archive is not an atomic image of running databases. Quiesce or use application-aware export where consistency requires it. A marker is meaningful only when the current workflow owns it, writes it last and checks the files it covers.

## Test extraction and metadata

Extract representative files into a disposable directory. Compare content and verify ownership, modes, exclusions and necessary configuration. Check that daemon-owned mutable state remains usable after restoration. Runtime sockets should be recreated by services, not restored as archived endpoints.

The original local-backup work included archive checks and representative extraction/metadata tests. These are useful evidence, but they do not prove that a replacement router can be fully restored.

## Prefer scoped rollback for maintenance

Keep exact old settings or files and a rollback that restores only the changed component. Restoring an old full NVRAM or JFFS image to undo one setting can overwrite later work.

For an administration or firewall change, an automatic rollback timer can protect a remote session. Arm it only after verifying the backup. Confirm the change after actual access and policy checks; otherwise restore the prior scoped settings. The timer and confirmation file must remain administrator-controlled.

Package rollback may require exact old packages and compatible dependencies. Restoring an old script may also require changing the reviewed update-guard baseline. Record both, without treating obsolete security settings as a preferred long-term state.

## Scheduling

Use the router's existing scheduler and a small number of named jobs. Check startup and USB-mount hooks for duplicate registrations. Fixed local-time schedules, such as an LED window, should not acquire unrelated daily jobs from an addon migration. Document timezone and daylight-saving behaviour privately where relevant.
