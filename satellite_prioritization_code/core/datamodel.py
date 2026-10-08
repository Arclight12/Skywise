# core/datamodel.py
from datetime import datetime

class DataNode:
    def __init__(self, id, region, event_type, quality, cloud_cover, size_mb, timestamp, visibility_windows):
        # Security (Sentinel): Enforce length limits on string inputs to prevent resource exhaustion (DoS)
        # We avoid destructive character stripping to preserve valid characters like spaces/hyphens
        if len(str(id)) > 100 or len(str(region)) > 100 or len(str(event_type)) > 100:
            raise ValueError("Input field length exceeds maximum allowed limit")

        self.id = str(id)
        self.region = str(region)
        self.event_type = str(event_type)
        self.quality = quality
        self.cloud_cover = cloud_cover
        self.size_mb = size_mb
        self.timestamp = datetime.fromisoformat(timestamp)
        self.visibility_windows = visibility_windows  # list of (start, end) datetime tuples
        self.score = 0
        self.filtered = False
        self.reason_pruned = None
