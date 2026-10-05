# core/datamodel.py
from datetime import datetime

class DataNode:
    def __init__(self, id, region, event_type, quality, cloud_cover, size_mb, timestamp, visibility_windows):
        # Security: Enforce input length limits to prevent resource exhaustion (DoS) via massive strings.
        # Length limits are preferred over destructive stripping to preserve valid characters.
        if len(str(id)) > 255 or len(str(region)) > 255 or len(str(event_type)) > 255:
            raise ValueError("Invalid input length")

        self.id = id
        self.region = region
        self.event_type = event_type
        self.quality = quality
        self.cloud_cover = cloud_cover
        self.size_mb = size_mb
        self.timestamp = datetime.fromisoformat(timestamp)
        self.visibility_windows = visibility_windows  # list of (start, end) datetime tuples
        self.score = 0
        self.filtered = False
        self.reason_pruned = None
