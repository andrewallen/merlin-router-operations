# Primary references

Use the exact source tag and current documentation relevant to the installed system. Links below are references, not commands to fetch and execute remote code.

| Project or topic | Primary source |
|---|---|
| Asuswrt-Merlin firmware | [Project and source](https://github.com/RMerl/asuswrt-merlin.ng) |
| GNUton firmware | [Project and releases](https://github.com/gnuton/asuswrt-merlin.ng) |
| Firewall generation for the build reviewed during the work | [Tagged firewall source](https://github.com/gnuton/asuswrt-merlin.ng/blob/3004.388.11_1-gnuton1/release/src/router/rc/firewall.c) |
| Service and UPnP configuration generation for that build | [Tagged services source](https://github.com/gnuton/asuswrt-merlin.ng/blob/3004.388.11_1-gnuton1/release/src/router/rc/services.c) |
| Entware packages | [Source recipes](https://github.com/Entware/Entware), [official feed root](https://bin.entware.net/) |
| Unbound configuration | [Official manual](https://unbound.docs.nlnetlabs.nl/en/latest/manpages/unbound.conf.html) |
| Unbound releases and advisories | [NLnet Labs Unbound](https://nlnetlabs.nl/projects/unbound/about/) |
| YazFi behaviour | [Project documentation](https://github.com/AMTM-OSR/YazFi) |
| Diversion | [Project website](https://diversion.ch/) |
| OISD list | [Project website](https://oisd.nl/) |
| ASUS security settings | [Official guidance](https://www.asus.com/support/faq/1039292/) |
| Packet filtering | [Netfilter packet-filtering HOWTO](https://www.netfilter.org/documentation/HOWTO/packet-filtering-HOWTO-6.html) |
| Tailscale and firewall trade-offs | [Official documentation](https://tailscale.com/docs/integrations/firewalls) |
| Backblaze B2 access control | [Application keys](https://www.backblaze.com/docs/cloud-storage-application-keys) |
| Backblaze key capabilities | [Capability reference](https://www.backblaze.com/docs/cloud-storage-application-key-capabilities) |
| Backblaze immutability | [Object Lock](https://www.backblaze.com/docs/cloud-storage-object-lock) |
| restic backends and B2 considerations | [Repository preparation](https://restic.readthedocs.io/en/stable/030_preparing_a_new_repo.html) |

The local change records behind this repository are intentionally not published. Product names identify the software being discussed, not an endorsement or an affiliation.

## Additional DNS and filtering references

- [Quad9 services](https://docs.quad9.net/services/) and [privacy policy](https://quad9.net/privacy/policy/).
- [Unbound downstream DoH support](https://unbound.docs.nlnetlabs.nl/en/latest/topics/privacy/dns-over-https.html).
- [HaGeZi blocklists and device-specific lists](https://github.com/hagezi/dns-blocklists).
- [Apple Private Relay network guidance](https://developer.apple.com/icloud/prepare-your-network-for-icloud-private-relay/) and [privacy architecture](https://support.apple.com/en-gb/102602).
- [DNS privacy considerations, RFC 9076](https://www.rfc-editor.org/rfc/rfc9076.html), [DoT, RFC 7858](https://www.rfc-editor.org/rfc/rfc7858.html) and [DoH, RFC 8484](https://www.rfc-editor.org/rfc/rfc8484.html).
- [dnsmasq configuration reference](https://thekelleys.org.uk/dnsmasq/docs/dnsmasq-man.html).
