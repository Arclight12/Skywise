# core/datamodel.py
from datetime import datetime

class DataNode:
    def __init__(self, id, region, event_type, quality, cloud_cover, size_mb, timestamp, visibility_windows):
        # 🛡️ Sentinel: Enforce length limits to prevent DoS via resource exhaustion, without destructive stripping.
        if len(str(id)) > 255:
            raise ValueError("ID length exceeds 255 characters limit.")
        if len(str(region)) > 100:
            raise ValueError("Region length exceeds 100 characters limit.")
        if len(str(event_type)) > 100:
            raise ValueError("Event type length exceeds 100 characters limit.")

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
