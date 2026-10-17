# core/datamodel.py
from datetime import datetime

class DataNode:
    def __init__(self, id, region, event_type, quality, cloud_cover, size_mb, timestamp, visibility_windows):
        # Security: Prevent resource exhaustion by enforcing maximum length limits on input fields.
        # Safe casting to string handles integers or UUIDs.
        if len(str(id)) > 255:
            raise ValueError("id exceeds maximum length of 255 characters")
        if len(str(region)) > 255:
            raise ValueError("region exceeds maximum length of 255 characters")
        if len(str(event_type)) > 255:
            raise ValueError("event_type exceeds maximum length of 255 characters")

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
