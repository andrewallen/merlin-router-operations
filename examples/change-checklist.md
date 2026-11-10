# Change record template

## Purpose and boundaries

- State the concrete problem and proposed result.
- List the exact component and supported persistent setting or reviewed files.
- Record which paths must remain unchanged: router DNS, guest, VPN, local administration, mesh, protection services and intentional fallback.
- Keep real identifiers and evidence in a private record outside this repository.

## Before changing anything

- Confirm exact device role, build, architecture and current state.
- Create and verify a private backup.
- Prepare a scoped rollback and establish management access.
- Record configuration hashes, relevant runtime rules and baseline probes privately.
- Check native restart hooks and expected temporary service effects.

## Apply and validate

- Apply the smallest persistent change.
- Wait for asynchronous addon hooks; inspect final rules rather than the first snapshot.
- Check intended success and intended refusal.
- Compare unrelated settings and policies. Explain every excluded dynamic difference.
- Test both devices where relevant.
- Remove test mappings, temporary data and maintenance pauses.
- Confirm or roll back; do not leave an unreviewed partial result.

## Report

- State what changed, why, what passed and what was not tested.
- Record brief service effects and any remaining concern.
- Keep restore locations and credentials private.
- Update approved code baselines only after exact-source review.
