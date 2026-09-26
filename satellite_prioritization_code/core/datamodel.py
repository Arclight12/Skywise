# core/datamodel.py
from datetime import datetime

class DataNode:
    def __init__(self, id, region, event_type, quality, cloud_cover, size_mb, timestamp, visibility_windows):
        self.id = id
        self.region = region
        self.event_type = event_type

        # Security: Input validation
        quality_f = float(quality)
        cloud_cover_f = float(cloud_cover)
        size_mb_f = float(size_mb)

        if not (0.0 <= quality_f <= 1.0):
            raise ValueError("Quality must be between 0.0 and 1.0")
        if not (0.0 <= cloud_cover_f <= 1.0):
            raise ValueError("Cloud cover must be between 0.0 and 1.0")
        if size_mb_f <= 0:
            raise ValueError("Size must be positive")

        self.quality = quality_f
        self.cloud_cover = cloud_cover_f
        self.size_mb = size_mb_f
        self.timestamp = datetime.fromisoformat(timestamp)
        self.visibility_windows = visibility_windows  # list of (start, end) datetime tuples
        self.score = 0
        self.filtered = False
        self.reason_pruned = None
