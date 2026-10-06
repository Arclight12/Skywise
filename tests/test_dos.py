import sys
import unittest
from datetime import datetime, timedelta

import os
# Adjust path to import satellite_prioritization_code
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'satellite_prioritization_code'))

from core.datamodel import DataNode

class TestDataNodeSecurity(unittest.TestCase):
    def setUp(self):
        self.now = datetime.now()
        self.vw = [(self.now, self.now + timedelta(minutes=10))]

    def test_valid_node_creation(self):
        node = DataNode(
            id="img_1",
            region="coastal",
            event_type="flood",
            quality=0.9,
            cloud_cover=0.1,
            size_mb=35,
            timestamp="2025-11-28T19:40:00",
            visibility_windows=self.vw
        )
        self.assertEqual(node.id, "img_1")

    def test_dos_long_string_blocked(self):
        long_id = "A" * 1000
        with self.assertRaisesRegex(ValueError, "ID exceeds maximum length"):
            DataNode(
                id=long_id,
                region="coastal",
                event_type="flood",
                quality=0.9,
                cloud_cover=0.1,
                size_mb=35,
                timestamp="2025-11-28T19:40:00",
                visibility_windows=self.vw
            )

    def test_invalid_timestamp_not_leaked(self):
        with self.assertRaisesRegex(ValueError, "Invalid timestamp format"):
            DataNode(
                id="img_1",
                region="coastal",
                event_type="flood",
                quality=0.9,
                cloud_cover=0.1,
                size_mb=35,
                timestamp="not-a-valid-timestamp",
                visibility_windows=self.vw
            )

if __name__ == '__main__':
    unittest.main()
