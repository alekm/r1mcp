# DPSK Service

## `autoNotificationsEnabled` mails the passphrase in clear on every update

A pool-level flag on `/dpskServices/{poolId}`. While it is true, **updating a
passphrase sends that passphrase to the resident in plaintext**, over both email
and SMS, to whatever contact sits on the passphrase record. There is no
per-request suppression — the caller cannot opt out of it for a single write.

The stock templates interpolate the value directly. Scope
`dpsk.passphrase.notification.email`, template
`dpsk.passphrase.notification.default.en_us.email`:

> Personal Password: `${passphrase}`

The `…en_us.sms` template under scope `dpsk.passphrase.notification.sms` does the
same. **Read the flag before any passphrase write**, and treat a rotation on a
pool with it enabled as an action that discloses a secret over an unencrypted
channel.

Verified 2026-09-04 by reading the tenant's own message templates, which is
read-only and mails nobody — do that rather than sending to a test mailbox. The
pool checked had the flag `false`, so this is the template text plus the flag
semantics, not an observed delivery. Templates are tenant data and can be
customized, so this is a per-tenant check, not a one-time fact.

## `passphrases/query` hands back plaintext passphrases you did not ask for

Every row from `POST /dpskServices/{poolId}/passphrases/query` carries the
**`passphrase` value itself**, alongside `createdDate`, `devices`, `email`, `id`,
`identityGroupId`, `identityId`, `isReferenced`, `phoneNumber` and `username`.

So any sweep of a pool pulls every resident's secret into whatever is holding the
response — 108 rows in a single page on the tenant this was verified against.
Pin `fields` to the columns you actually need when you only want metadata, and do
not log, cache or echo the raw response. Note that `fields` is silently dropped
if the endpoint does not recognize a name (GENERAL.md §3), so check what came
back rather than assuming the projection applied.

## Passphrase length is 8-63, and the two failures look nothing alike

Verified 2026-09-04 against a pool declaring `passphraseLength: 8`:

| Submitted | HTTP | Activity | Stored |
|---|---|---|---|
| 7 chars, or empty | **400** `DPSK-032` | — | unchanged |
| 8 chars (exactly the pool minimum) | 202 | SUCCESS | verbatim |
| 9, 16, 32, 63 chars | 202 | SUCCESS | verbatim |
| **64, 65, 100, 200 chars** | **202** | **FAIL** `DPSK-10032` | **unchanged** |

Below the minimum is a synchronous 400 you cannot miss. **Over-length is a 202
that resolves to an activity `FAIL` and leaves the old value in place** — the
trap in GENERAL.md §1, on the write you are most likely to be making.

The maximum of 63 is documented nowhere. The pool declares `passphraseLength` as
a minimum and no maximum at all; the bound surfaces only in the activity's
`errors[].message`, as `"Size must be between 8 and 63"`. There is no silent
substitution at either bound — a value that is accepted is stored verbatim.

## `PATCH` on a passphrase preserves the bound devices

Changing the value does not unbind anything. Verified by binding two MACs to a
throwaway passphrase, `PATCH`ing with `{ passphrase }` alone, polling the
activity to `SUCCESS` and re-reading the device list: both still bound, and the
read-back matched the submitted value exactly.

A rotation is a value change, not a re-onboarding — so it does not need to be
paired with re-adding devices.
