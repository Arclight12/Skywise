# core/datamodel.py
from datetime import datetime

class DataNode:
    def __init__(self, id, region, event_type, quality, cloud_cover, size_mb, timestamp, visibility_windows):
        # Security Enhancement: Validate and sanitize string inputs to prevent excessive memory/DoS
        self.id = id
        self.region = region
        self.event_type = event_type

        # Enforce length limits instead of destructive character stripping
        # Cast to str to accommodate IDs passed as integers or UUIDs during length check
        if len(str(self.id)) > 255 or (self.region and len(str(self.region)) > 255) or (self.event_type and len(str(self.event_type)) > 255):
            # Fail securely without exposing internal values or stack traces
            raise ValueError("Input exceeds maximum allowed length")

        self.quality = quality
        self.cloud_cover = cloud_cover
        self.size_mb = size_mb
        self.timestamp = datetime.fromisoformat(timestamp)
        self.visibility_windows = visibility_windows  # list of (start, end) datetime tuples
        self.score = 0
        self.filtered = False
        self.reason_pruned = None
