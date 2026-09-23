# core/datamodel.py
from datetime import datetime

class DataNode:
    def __init__(self, id, region, event_type, quality, cloud_cover, size_mb, timestamp, visibility_windows):
        self.id = id
        self.region = region
        self.event_type = event_type

        # 🛡️ Sentinel: Validate numeric bounds to prevent out of bound data
        self.quality = float(quality)
        if not (0.0 <= self.quality <= 1.0):
            raise ValueError("Quality must be between 0.0 and 1.0")

        self.cloud_cover = float(cloud_cover)
        if not (0.0 <= self.cloud_cover <= 1.0):
            raise ValueError("Cloud cover must be between 0.0 and 1.0")

        self.size_mb = float(size_mb)
        if self.size_mb <= 0.0:
            raise ValueError("Size (MB) must be strictly positive")

        self.timestamp = datetime.fromisoformat(str(timestamp))
        self.visibility_windows = visibility_windows  # list of (start, end) datetime tuples
        self.score = 0
        self.filtered = False
        self.reason_pruned = None
