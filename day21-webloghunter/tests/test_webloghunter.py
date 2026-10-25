import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from webloghunter import parse_line, analyze

class WebLogHunterTests(unittest.TestCase):
    def test_parses_combined_access_log(self):
        e = parse_line('192.0.2.1 - - [26/Oct/2026:10:15:00 +0000] "GET / HTTP/1.1" 200 123 "-" "test"', 1)
        self.assertIsNotNone(e)
        self.assertEqual(e.status, 200)
        self.assertEqual(e.ip, "192.0.2.1")
    def test_ignores_unparseable_line(self):
        self.assertIsNone(parse_line("not an access log", 1))
    def test_detects_encoded_sqli(self):
        e = parse_line('198.51.100.2 - - [26/Oct/2026:10:15:00 +0000] "GET /?q=union%20select%20x HTTP/1.1" 400 1 "-" "x"', 1)
        self.assertTrue(any(f.rule_id == "WEB_SQLI" for f in analyze([e])))
    def test_auth_failure_burst_threshold(self):
        rows = [parse_line(f'203.0.113.5 - - [26/Oct/2026:10:15:0{i} +0000] "POST /login HTTP/1.1" 401 1 "-" "x"', i+1) for i in range(5)]
        self.assertTrue(any(f.rule_id == "WEB_AUTH_FAILURE_BURST" for f in analyze(rows, threshold=5)))

if __name__ == "__main__":
    unittest.main()
