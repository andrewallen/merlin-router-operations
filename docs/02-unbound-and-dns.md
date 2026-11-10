# Unbound and DNS

## Privacy and validation

Authenticated DNS over TLS protects queries between Unbound and the upstream resolver. Configure an authentication name and a maintained CA bundle; encryption without certificate and hostname verification is insufficient.

The upstream resolver can still see queries. Devices can also use their own encrypted DNS, VPNs or application resolvers. DNSSEC validates signed DNS data; it does not encrypt queries or validate every unsigned answer. No setting guarantees that nobody can see all DNS activity.

The reviewed design retained DNSSEC, authenticated TLS forwarding and `forward-first: no`. That setting prevents this forwarding zone from silently falling back to ordinary recursive resolution when the configured upstream fails. The administrator's separate, explicit fallback remains a distinct operational decision with its own privacy properties.

For an IPv4-only installation, `do-ip6: no` controls Unbound's IPv6 transport. It does not remove AAAA answers or disable IPv6 across the router. Verify the wider network separately.

## Separate code, configuration and state

Keep privileged configuration administrator-owned and non-writable by the resolver account. Keep the DNSSEC trust anchor, logs and other mutable state in narrowly scoped daemon-writable locations. A writable trust anchor is required for normal maintenance; making the entire configuration directory daemon-owned is not required.

Privilege-drop and chroot behaviour matter. Test reloads after startup, not only parsing as root. Configuration that root can read may become inaccessible after privilege drop.

## Secure the control channel

A loopback listener is reachable by local processes. An unauthenticated control channel can therefore weaken separation between an unprivileged process and the resolver.

Where supported, use a Unix socket with restrictive parent-directory traversal permissions. Check effective daemon UID/GID, socket creation, root client access and addon compatibility. If TCP control is required, configure appropriate authentication and access restrictions. Do not assume that turning off TCP control has secured every local integration.

Tests used in the original work included status, statistics, reload, log reopening, cache operations, daemon restart and recreation of the socket. The obsolete TCP control endpoint was checked for absence.

## Patch the right component

Distinguish upstream source releases, package recipes and published binary packages. A newer recipe is not proof that the configured architecture's binary feed contains a patched build.

Check package version, release suffix, feed URL, architecture and archive digest. Review linked dependencies and determine which running processes still map replaced libraries. Restart only the required consumers, taking care not to pass maintenance lock descriptors into long-lived daemons.

An interim community build creates provenance, update and rollback obligations. Prefer returning to a maintained official package once its actual published binary is suitable. A clean upstream version string alone does not establish complete vulnerability coverage; vendor backports and package patches must be checked.

## Validate both success and refusal

1. Parse Unbound and frontend configuration.
2. Resolve an ordinary name through the existing frontend.
3. Check a DNSSEC-valid response and a deliberately invalid signed domain.
4. Check a valid TLS hostname and verify that an incorrect hostname is refused.
5. Confirm encrypted upstream connections without capturing private query contents.
6. Confirm filtering, private control access and local recovery health.
7. Compare router resolver, guest and VPN paths with their private baseline.

Do not restart a healthy resolver repeatedly because a remote feed returns an HTTP error. Upstream failures, validation failures and local daemon failures are different events.
