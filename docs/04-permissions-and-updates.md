# Permissions and updates

## Protect the code that runs as root

Administrator-only write access matters for scripts, sourced modules, startup files, shared WebUI assets, package databases and available-package indexes. A directory that lets another account replace a file defeats restrictive permissions on the current file.

Do not apply one recursive mode to an entire USB volume. Runtime logs, sockets, trust anchors and daemon state have different requirements. Scope ownership and modes by purpose; do not follow unexpected symlinks. Skip metadata writes where ownership and modes already match.

Common targets examined during the work included amtm, Entware metadata, shared addon libraries, generated WebUI pages, shell history and credential/configuration writers. Package installers and addon updaters were checked to ensure that root could still operate normally after tightening.

## Fix writers as well as current files

A safe current mode does not prove safe recreation. Review temporary-file creation, rename/publish operations, migrations and inherited umasks. Scope an umask change to the writer so a sourced addon does not unexpectedly change the interactive caller's behaviour.

Use harmless disposable fixtures to test creation under deliberately permissive defaults. Where a boundary matters, test access using a real unprivileged UID/GID rather than inferring it from a listing.

## Updates are a review boundary

The local update guard used this model:

```text
prepare -> verified private backup + policy baseline
native update -> addon/package performs its own update
finish -> identify exact replacement code
         known reviewed original: apply reviewed local hardening
         known hardened code: verify it
         unfamiliar code: leave untouched and flag review
         compare protected policies and run service tests
```

An exact hash match identifies bytes, not trustworthiness. The approval manifest must be created from reviewed source. Never label a new hash as approved just to clear a warning, and never patch an unfamiliar version by line number or broad text substitution.

Scheduled checks should avoid racing active installers. Recovery, update and permission processes must coordinate locks, and daemons must not inherit those lock descriptors. Otherwise a successful restart can leave future maintenance blocked.

## Use maintained trust material

Certificate verification should use a maintained trust store compatible with the runtime. Check both successful validation and refusal of the wrong hostname. Avoid global certificate bypasses and insecure redirects, including in helper download paths outside the main updater.

Keep the last known-good blocklist if a download or validation fails. A failed refresh should not replace a usable list with an empty or partial file.

## Post-update checks

Verify package versions, dependencies and retained packages; look for processes mapping deleted libraries; check actual generated and served pages; run the existing guard; compare DNS, guest and VPN policy. A regenerated page can have different permissions from its source template.

Do not export the site's manifests or patched third-party trees into a public reference repository. They can reveal local state and create licensing or compatibility problems. This repository documents the design rather than supplying a universal repair overlay.
