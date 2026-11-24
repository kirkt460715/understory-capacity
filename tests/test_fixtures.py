import csv
import json
import unittest
from pathlib import Path


DATA = Path(__file__).resolve().parents[1] / "data"


class FixtureContractTests(unittest.TestCase):
    def test_declared_sources_have_headers_and_records(self):
        manifest = json.loads((DATA / "manifest.json").read_text(encoding="utf-8"))
        for filename, columns in manifest["sources"].items():
            with self.subTest(source=filename):
                with (DATA / filename).open(encoding="utf-8", newline="") as source:
                    reader = csv.DictReader(source)
                    self.assertEqual(reader.fieldnames, columns)
                    self.assertGreaterEqual(sum(1 for _ in reader), 1)


if __name__ == "__main__":
    unittest.main()
