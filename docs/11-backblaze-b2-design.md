# Backblaze B2 backup design

Status: proposed follow-up. No bucket, application key, cloud schedule or cloud upload was created as part of publishing this repository.

## Keep the local backup as the first layer

Extend the existing verified snapshot workflow. Upload only completed snapshots whose contents and digests have been checked. Keep cloud failure independent from local-backup success, and do not delete the last good local snapshot because an upload failed.

Native settings and addon archives contain secrets. Encrypt on the client before upload; TLS and storage-provider encryption do not replace this. Keep the decryption secret and recovery instructions somewhere accessible if the router and USB volume are lost together.

## Two deployment choices

| Approach | Advantages | Costs and risks |
|---|---|---|
| Router encrypts and uploads verified snapshots | Autonomous while the router is running; no dependency on a sleeping computer | Cloud credentials and encryption capability live on the router; ARM package support, CPU/storage use and scheduler integration need testing |
| A local always-on host pulls snapshots, encrypts and uploads | Cloud credentials can stay off the router; more separation from a router compromise | Needs another maintained host, secure pull access and reliable availability |

An awake-only laptop can provide useful copies but is less reliable as the sole automatic route. Neither choice should modify routing, DNS, guest, VPN or mesh policy.

For already compressed full archives, deduplication savings may be limited. A simple encrypted-object upload may be easier to operate than a repository-based backup tool; a repository tool can provide managed snapshots, integrity checking and retention. Evaluate both against package support and actual restore needs.

## B2 boundary

- Use a private dedicated bucket or tightly scoped prefix.
- Create a restricted application key; do not use an account-wide master key on a router.
- Request only capabilities required by the selected client and access pattern. An upload-only claim must be tested, including listing, multipart operations and any S3 compatibility requirements.
- Keep credential files private and out of shell arguments, debug logs, Git and backup manifests that are published.
- Use generic object names that do not expose device or household identifiers.
- Apply bounded retries, overlap protection, useful local status and explicit cloud-failure reporting.

## Retention and deletion protection

A client with deletion permission can destroy its own remote backups after compromise. Consider separating routine upload credentials from retention/deletion administration. Object Lock can protect retained objects, but changes operational recovery, cost and cleanup behaviour.

Do not enable default Object Lock blindly on a tool-managed repository: lock files, pruning and object deletion may be incompatible. Similarly, do not apply an age-based bucket rule that deletes still-referenced repository objects. For independent encrypted snapshot objects, retention is simpler but still needs a restore test and cost check.

If using restic with B2, current restic documentation recommends the S3-compatible backend over its native B2 backend. Verify that advice again when implementing. Do not assume provider lifecycle handling matches ordinary filesystem deletion.

## Acceptance tests before scheduling

1. Generate or select a verified private local snapshot.
2. Encrypt and upload with the restricted credential.
3. Confirm the intended bucket/object privacy and permitted/denied operations.
4. Download to a disposable location and decrypt using the recovery procedure.
5. Compare archive digests, list members and extract representative files with metadata.
6. Simulate unavailable network, expired credentials and an overlapping run without breaking local backups.
7. Validate retention on disposable test objects before applying it to real recovery material.
8. Save private operational documentation, credential recovery and a failure/status path.

Only then enable the schedule. A successful upload alone is not a restore test.

References: [B2 application keys](https://www.backblaze.com/docs/cloud-storage-application-keys), [key capabilities](https://www.backblaze.com/docs/cloud-storage-application-key-capabilities), [Object Lock](https://www.backblaze.com/docs/cloud-storage-object-lock), and [restic repository preparation](https://restic.readthedocs.io/en/stable/030_preparing_a_new_repo.html).
