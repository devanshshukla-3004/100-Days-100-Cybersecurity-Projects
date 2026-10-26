import unittest
from webvulnscan import analyze_response, validate_url

class WebVulnScanTests(unittest.TestCase):
    def test_rejects_invalid_schemes(self):
        for url in ("file:///etc/passwd", "ftp://example.com", "example.com"):
            with self.subTest(url=url), self.assertRaises(ValueError):
                validate_url(url)

    def test_rejects_embedded_credentials(self):
        with self.assertRaises(ValueError):
            validate_url("https://user:password@example.com")

    def test_http_flags_unencrypted_transport(self):
        report = analyze_response("http://example.test", 200, {})
        self.assertTrue(any(x["category"] == "Unencrypted transport" for x in report["findings"]))
        self.assertFalse(any(x["evidence"] == "strict-transport-security" for x in report["findings"]))

    def test_https_flags_missing_headers(self):
        report = analyze_response("https://example.test", 200, {})
        evidence = {x["evidence"] for x in report["findings"]}
        self.assertIn("content-security-policy", evidence)
        self.assertIn("strict-transport-security", evidence)

    def test_detects_server_disclosure(self):
        report = analyze_response("https://example.test", 200, {"Server": "ExampleServer/1.2"})
        self.assertTrue(any("ExampleServer/1.2" in x["evidence"] for x in report["findings"]))

if __name__ == "__main__":
    unittest.main()
