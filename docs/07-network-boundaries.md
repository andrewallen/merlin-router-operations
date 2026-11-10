# Network boundaries

## Traffic to the router differs from traffic through it

The input firewall protects local services. The forwarding firewall controls routed packets. Normal forwarding does not require exposing SSH or HTTPS to every client. A service listening on all addresses is not necessarily internet-accessible if the input firewall blocks it, but it is still worth checking the effective boundaries.

Do not infer protection from a chain's default policy alone. Follow jumps, earlier accepts, final drops and NAT. Check IPv4 and IPv6 separately and inspect active port mappings, DMZ, triggers and remote-management exceptions.

## A broad WAN-to-LAN allowance

One inspected firmware configuration had:

```text
fw_wl_enable_x=1
filter_wl_default_x=ACCEPT
filter_wllist=<empty>
filter_wl_icmp_x=<empty>
```

This generated an unconditional forwarding allowance from the WAN interface to the trusted LAN bridge. It was not needed to accept ordinary replies: established/related traffic was already accepted earlier. Explicit DNAT mappings were also accepted earlier.

The scoped fix changed `filter_wl_default_x` to `DROP`. The main firewall remained enabled. The exact firmware source, generated rules and live chain order were checked before the change. The broad allowance had no observed counter hits during the investigation; that does not prove it had never been used.

This was a policy weakness, not a demonstrated internet exploit. Carrier-grade NAT reduces normal direct IPv4 reachability but is not a replacement for a restrictive firewall. No independent external penetration test was performed.

On another build, inspect the source and actual chain order first. An earlier accept can defeat a later drop. A broad drop inserted before legitimate guest or VPN handling can break those services. Deleting only the live rule does not fix its persistent generator.

## UPnP, NAT-PMP and Tailscale

An empty current mapping table is not evidence that mapping is unused. Compare leases, available logs and prior snapshots, then identify the requesting devices and applications. UDP port numbers can suggest an application but do not prove ownership.

Tailscale may benefit from automatic mapping for direct connections. Disabling it can lead to relay use and different latency or throughput. Distinguish that from the router's own VPN client tunnels.

The scoped adjustment retained UPnP/NAT-PMP, secure mode and the third-party mapping restriction. It raised the external-port minimum from 1 to 1024, leaving the permitted internal range unchanged. A live NAT-PMP request for a lower external port was assigned 1024 instead; an allowed high-port request succeeded. Temporary test mappings were removed.

This does not prevent an infected permitted device from exposing its own high-port service. A device allowlist offers a stronger boundary but needs a reliable inventory, DHCP/private-MAC treatment and application tests. No device allowlist was deployed in this step.

## Guest isolation

Check the guest subnet, bridge membership, input rules, forward rules, DNS redirection, wireless client-isolation state and mesh synchronisation. Interface numbering on a node does not tell you whether an interface is trusted or guest.

With YazFi, an ASUS intranet-access flag can be deliberately enabled while YazFi implements separate isolation. Judge the effective bridge and firewall, not that flag in isolation. In the ebtables broute table, `DROP` has routing semantics; do not mistake it for an ordinary filter-table drop.

The inspected guest policy allowed internet access while blocking guest-to-trusted, trusted-to-guest and guest-to-VPN forwarding. Router DHCP, NTP and ICMP were deliberate exceptions; administration was rejected. Wireless client isolation was confirmed in the driver. Guest and main WiFi credentials were distinct.

Those observations establish configured steady-state isolation. They do not prove every possible bypass is absent. Test from real guest clients, including client-to-client traffic and behaviour during boot or addon restarts. A firewall restart can temporarily remove addon rules until the existing hook restores them.
