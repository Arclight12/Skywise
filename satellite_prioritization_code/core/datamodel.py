# core/datamodel.py
from datetime import datetime

class DataNode:
    def __init__(self, id, region, event_type, quality, cloud_cover, size_mb, timestamp, visibility_windows):
        # Security: Input length limits to prevent DoS risks
        if len(str(id)) > 255:
            raise ValueError("ID length exceeds maximum limit of 255 characters")
        if len(str(region)) > 255:
            raise ValueError("Region length exceeds maximum limit of 255 characters")
        if len(str(event_type)) > 255:
            raise ValueError("Event type length exceeds maximum limit of 255 characters")

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
