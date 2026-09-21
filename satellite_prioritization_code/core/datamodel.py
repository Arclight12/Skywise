# core/datamodel.py
from datetime import datetime

class DataNode:
    def __init__(self, id, region, event_type, quality, cloud_cover, size_mb, timestamp, visibility_windows):
        # CSV Injection prevention (sanitize string inputs)
        self.id = str(id).lstrip("=+-@ ")
        self.region = str(region).lstrip("=+-@ ")
        self.event_type = str(event_type).lstrip("=+-@ ")

        # Input validation
        if not (0.0 <= quality <= 1.0):
            raise ValueError("Quality must be between 0.0 and 1.0")
        if not (0.0 <= cloud_cover <= 1.0):
            raise ValueError("Cloud cover must be between 0.0 and 1.0")
        if size_mb <= 0:
            raise ValueError("Size (MB) must be greater than 0")

        self.quality = quality
        self.cloud_cover = cloud_cover
        self.size_mb = size_mb
        self.timestamp = datetime.fromisoformat(timestamp)
        self.visibility_windows = visibility_windows  # list of (start, end) datetime tuples
        self.score = 0
        self.filtered = False
        self.reason_pruned = None
