# core/datamodel.py
from datetime import datetime

class DataNode:
    def __init__(self, id, region, event_type, quality, cloud_cover, size_mb, timestamp, visibility_windows):
        self.id = id
        self.region = region
        self.event_type = event_type
        # Security: Validate and sanitize input bounds to prevent DoS or unexpected calculation behavior
        self.quality = max(0.0, min(1.0, float(quality)))
        self.cloud_cover = max(0.0, min(1.0, float(cloud_cover)))
        self.size_mb = max(0.0, float(size_mb))

        # Security: Safe timestamp parsing
        try:
            self.timestamp = datetime.fromisoformat(str(timestamp))
        except ValueError:
            raise ValueError("Invalid timestamp format")
        self.visibility_windows = visibility_windows  # list of (start, end) datetime tuples
        self.score = 0
        self.filtered = False
        self.reason_pruned = None
