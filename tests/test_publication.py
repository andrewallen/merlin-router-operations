import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

SPEC = importlib.util.spec_from_file_location(
    "publication", Path(__file__).resolve().parents[1] / "tools" / "check_publication.py"
)
publication = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(publication)


class PublicationChecks(unittest.TestCase):
    def assert_detected(self, value, label):
        found = publication.scan_text("fixture.md", value)
        self.assertTrue(any(label in item for item in found), found)
        self.assertTrue(all(value not in item for item in found))

    def test_non_documentation_address_is_rejected(self):
        self.assert_detected("10" + ".9.8.7", "IPv4")

    def test_documentation_and_loopback_addresses_are_allowed(self):
        self.assertEqual(publication.scan_text("fixture.md", "192.0.2.53 198.51.100.53 203.0.113.1 127.0.0.1"), [])

    def test_mac_email_and_home_path_are_rejected(self):
        self.assert_detected(":".join(["aa", "bb", "cc", "dd", "ee", "ff"]), "MAC")
        self.assert_detected("person" + "@" + "example.net", "email")
        self.assert_detected("/" + "Users" + "/fixture/private", "filesystem")

    def test_secret_patterns_are_rejected(self):
        self.assert_detected("ghp_" + "x" * 30, "GitHub")
        self.assert_detected("-----BEGIN " + "PRIVATE KEY-----", "private key")
        self.assert_detected("PASSWORD" + "=not-a-real-secret", "credential")

    def test_denylist_is_case_insensitive_and_does_not_echo_value(self):
        found = publication.scan_text("fixture.md", "PrivateDevice", ["privatedevice"])
        self.assertEqual(found, ["fixture.md:1: private denylist match"])

    def test_unlisted_files_and_symlinks_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / ".publication-allowlist.json").write_text(json.dumps([".publication-allowlist.json", "README.md"]))
            (root / "README.md").write_text("Generic reference")
            self.assertEqual(publication.check_tree(root), [])
            (root / "private.log").write_text("not for publication")
            (root / "link.md").symlink_to(root / "README.md")
            findings = publication.check_tree(root)
            self.assertTrue(any("outside publication allowlist" in f for f in findings))
            self.assertTrue(any("symlink prohibited" in f for f in findings))

    def test_missing_allowlisted_file_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / ".publication-allowlist.json").write_text(json.dumps(["README.md"]))
            self.assertTrue(any("missing" in f for f in publication.check_tree(root)))


if __name__ == "__main__":
    unittest.main()
