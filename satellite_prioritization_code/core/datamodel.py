# core/datamodel.py
from datetime import datetime

class DataNode:
    def __init__(self, id, region, event_type, quality, cloud_cover, size_mb, timestamp, visibility_windows):
        self.id = id
        self.region = region
        self.event_type = event_type

        if not (0.0 <= quality <= 1.0):
            raise ValueError("Quality must be between 0.0 and 1.0")
        self.quality = quality

        if not (0.0 <= cloud_cover <= 1.0):
            raise ValueError("Cloud cover must be between 0.0 and 1.0")
        self.cloud_cover = cloud_cover

        if size_mb < 0:
            raise ValueError("Size must be positive")
        self.size_mb = size_mb

        self.timestamp = datetime.fromisoformat(timestamp)
        self.visibility_windows = visibility_windows  # list of (start, end) datetime tuples
        self.score = 0
        self.filtered = False
        self.reason_pruned = None
