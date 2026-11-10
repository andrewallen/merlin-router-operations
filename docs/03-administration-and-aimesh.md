# Administration and AiMesh

## Move local administration to HTTPS with a recovery path

Back up each device separately. Establish a working SSH session before changing the WebUI listener. Check the new HTTPS endpoint, certificate handling and actual authenticated pages before removing reliance on the old URL.

Use a trusted local CA or explicitly managed certificate trust where practical. A request made with certificate checks disabled proves reachability, not server identity. Do not describe an HTTP 200 response as a successful authenticated addon test.

Keep an administrator-only, local emergency mechanism for restoring the prior administration mode. It should not expose administration on WAN or run automatically in response to an unauthenticated packet.

## Node checks can have separate credentials

An addon may need recoverable credentials for authenticated mesh-node checks. Tightening file access can protect those credentials from other local accounts while preserving the root-run addon. It cannot protect them from a compromised administrator or root process.

Review every credential writer, including first creation, rewrite, migration and reset. A one-time `chmod` can be undone by the next rewrite. Test safe creation under a permissive parent umask and confirm native addon checks still work.

Use SSH keys where compatible, but establish and test main and node key access before disabling password login. Keep key material and recovery copies private. Never commit real certificates, keys, password hashes or session cookies.

## Check both devices

The main router and mesh node need separate service, listener, WPS, cloud-access and firmware checks. A node in access-point mode is protected by the main WAN perimeter, but it can still expose administration or unused services to the trusted LAN.

Where node file sharing is unused, assess disabling its service independently of mesh management. Verify the real service state rather than trusting an inherited NVRAM flag.

A main-router browser session can interfere with a second automated login. Confirm the reason before interpreting an authentication failure as a broken HTTPS migration or changing credentials.

## Remaining improvement

Restricting SSH and HTTPS to selected management devices can reduce exposure from a compromised trusted-LAN device. This was identified as a separate hardening option, not implemented as part of the WAN-default change. DHCP, DNS, NTP, mesh management and recovery access need their own explicit treatment.
