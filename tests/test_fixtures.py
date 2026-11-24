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
                    rows = list(reader)
                    self.assertTrue(rows)
                    for row in rows:
                        self.assertNotIn(None, row)
                        self.assertNotIn(None, row.values())

    def records(self, filename):
        with (DATA / filename).open(encoding="utf-8", newline="") as source:
            return list(csv.DictReader(source))

    def test_approved_use_and_alternatives_reference_valid_parcels(self):
        parcels = {row["parcel_id"] for row in self.records("parcels.csv")}
        applications = {row["application_id"] for row in self.records("applications.csv")}
        for row in self.records("approved_use.csv") + self.records("candidate_areas.csv"):
            self.assertIn(row["parcel_id"], parcels)
            self.assertIn(row["application_id"], applications)
        events = [row for row in self.records("approval_events.csv") if row["application_id"] == "A-14"]
        self.assertEqual({row["event_type"] for row in events}, {"签发", "确认取消"})


if __name__ == "__main__":
    unittest.main()
