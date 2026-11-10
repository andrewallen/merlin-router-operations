#!/usr/bin/env python3
"""Check a deliberately assembled public tree. No network access or uploads."""
import argparse
import ipaddress
import json
from pathlib import Path
import re
import sys


PATTERNS = {
    "MAC address": re.compile(r"(?i)\b(?:[0-9a-f]{2}:){5}[0-9a-f]{2}\b"),
    "email address": re.compile(r"\b[A-Za-z0-9_.+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
    "personal filesystem path": re.compile(r"(?:/[U]sers/|/[h]ome/|[A-Z]:\\[U]sers\\)"),
    "private key": re.compile(r"-----BEGIN (?:[A-Z]+ )*PRIVATE KEY-----"),
    "GitHub credential": re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})\b"),
    "cloud access identifier": re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b"),
    "JWT-like value": re.compile(r"\beyJ[A-Za-z0-9_-]{12,}\.[A-Za-z0-9_-]{12,}\.[A-Za-z0-9_-]{12,}\b"),
    "credential assignment": re.compile(
        r"(?im)^\s*(?:export\s+)?(?:[A-Za-z0-9_]*(?:password|passwd|secret|token|access_key|wpa_psk))\s*[:=]\s*[^\s#]+"
    ),
}
IPV4 = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
SAFE_NETWORKS = tuple(ipaddress.ip_network(n) for n in (
    "192.0.2.0/24", "198.51.100.0/24", "203.0.113.0/24", "127.0.0.0/8"
))
ALLOWED_SUFFIXES = {".md", ".py", ".sh", ".json", ".example"}


def scan_text(name, text, deny_terms=()):
    """Return location/category only; never echo the matched sensitive value."""
    findings = []
    for line_number, line in enumerate(text.splitlines(), 1):
        for label, pattern in PATTERNS.items():
            if pattern.search(line):
                findings.append(f"{name}:{line_number}: {label}")
        for match in IPV4.finditer(line):
            try:
                address = ipaddress.ip_address(match.group())
            except ValueError:
                continue
            if not any(address in network for network in SAFE_NETWORKS):
                findings.append(f"{name}:{line_number}: non-documentation IPv4 address")
        if any(term.casefold() in line.casefold() for term in deny_terms if term):
            findings.append(f"{name}:{line_number}: private denylist match")
    return findings


def check_tree(root, deny_terms=()):
    manifest = root / ".publication-allowlist.json"
    expected = set(json.loads(manifest.read_text(encoding="utf-8")))
    findings = []
    actual = set()
    for path in root.rglob("*"):
        relative = path.relative_to(root)
        if ".git" in relative.parts or "__pycache__" in relative.parts:
            continue
        name = relative.as_posix()
        if path.is_symlink():
            findings.append(f"{name}: symlink prohibited")
            continue
        if not path.is_file():
            continue
        actual.add(name)
        if name not in expected:
            findings.append(f"{name}: outside publication allowlist")
        if path.suffix not in ALLOWED_SUFFIXES and name not in {"LICENSE", ".gitignore"}:
            findings.append(f"{name}: prohibited file type")
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            findings.append(f"{name}: non-text file prohibited")
            continue
        findings.extend(scan_text(name, content, deny_terms))
    findings.extend(f"{name}: allowlisted file missing" for name in sorted(expected - actual))
    return findings


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=".")
    parser.add_argument("--deny-file", type=Path, help="Private UTF-8 terms, one per line; must be outside the public tree")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    terms = ()
    if args.deny_file:
        deny_path = args.deny_file.resolve()
        if deny_path == root or root in deny_path.parents:
            parser.error("Private denylist must remain outside the public tree")
        terms = tuple(line.strip() for line in deny_path.read_text().splitlines() if line.strip())
    try:
        findings = check_tree(root, terms)
    except (OSError, ValueError, TypeError) as error:
        print(f"CHECK FAILED: {type(error).__name__}", file=sys.stderr)
        return 2
    if findings:
        print("\n".join(findings))
        print(f"FAIL: {len(findings)} publication finding(s)")
        return 1
    print("PASS: allowlist, text-only content and configured privacy checks")
    print("Manual review and complete Git-history inspection remain required.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
