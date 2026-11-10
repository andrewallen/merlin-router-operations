#!/bin/sh
# Generic read-only summary. Run locally on a compatible router as its admin.
# No raw NVRAM, device list, addresses, routes, keys or logs are printed.
# Inspect before use. Missing commands/services are reported without repair.
set -u
PATH=/opt/sbin:/opt/bin:/usr/sbin:/usr/bin:/sbin:/bin
export PATH

has_command() { command -v "$1" >/dev/null 2>&1; }

flag_equals() {
    label=$1
    key=$2
    expected=$3
    if ! has_command nvram; then
        printf '%s: unavailable\n' "$label"
    elif [ "$(nvram get "$key")" = "$expected" ]; then
        printf '%s: expected\n' "$label"
    else
        printf '%s: review\n' "$label"
    fi
}

printf '%s\n' 'Selected configuration checks (not a security attestation)'
flag_equals 'IPv4 firewall enabled' fw_enable_x 1
flag_equals 'WAN WebUI disabled' misc_http_x 0
flag_equals 'IPv6 disabled when intentionally unused' ipv6_service disabled
flag_equals 'WPS disabled' wps_enable 0
flag_equals 'UPnP secure mode' upnp_secure 1
flag_equals 'WAN-to-LAN default drop when legacy filter is enabled' filter_wl_default_x DROP
flag_equals 'Low external automatic-mapping ports excluded' upnp_min_port_ext 1024

for process in dnsmasq unbound httpds cfg_server cfg_client miniupnpd dcd; do
    if has_command pidof && pidof "$process" >/dev/null 2>&1; then
        printf '%s: running\n' "$process"
    else
        printf '%s: not observed (may be appropriate for this device role)\n' "$process"
    fi
done

if has_command iptables; then
    printf 'Forward-rule count: '
    iptables -S FORWARD 2>/dev/null | awk 'END { print NR }'
    printf 'Active automatic NAT mapping-rule count: '
    iptables -t nat -S VUPNP 2>/dev/null | awk '/^-A / {n++} END {print n+0}'
    if iptables -S YazFiFORWARD >/dev/null 2>&1; then
        printf '%s\n' 'YazFi forward chain: present (not a complete isolation test)'
    else
        printf '%s\n' 'YazFi forward chain: not observed'
    fi
fi

if has_command ip6tables; then
    for chain in INPUT FORWARD OUTPUT; do
        if ip6tables -S "$chain" 2>/dev/null | grep -q "^-P $chain DROP$"; then
            printf 'IPv6 %s policy: drop\n' "$chain"
        else
            printf 'IPv6 %s policy: review or unavailable\n' "$chain"
        fi
    done
fi

printf '%s\n' 'No settings, files, mappings or services changed.'
