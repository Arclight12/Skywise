# core/datamodel.py
from datetime import datetime

class DataNode:
    def __init__(self, id, region, event_type, quality, cloud_cover, size_mb, timestamp, visibility_windows):
        # Security Enhancement: Enforce length limits to prevent DoS via resource exhaustion
        if len(str(id)) > 255:
            raise ValueError("ID exceeds maximum length of 255 characters")
        if len(str(region)) > 255:
            raise ValueError("Region exceeds maximum length of 255 characters")
        if len(str(event_type)) > 255:
            raise ValueError("Event type exceeds maximum length of 255 characters")
        if len(str(timestamp)) > 50:
            raise ValueError("Timestamp exceeds maximum length of 50 characters")

        self.id = str(id)
        self.region = str(region)
        self.event_type = str(event_type)
        self.quality = float(quality)
        self.cloud_cover = float(cloud_cover)
        self.size_mb = float(size_mb)

        try:
            self.timestamp = datetime.fromisoformat(str(timestamp))
        except ValueError as e:
            # Security Enhancement: Do not leak the original raw string in the exception message
            raise ValueError("Invalid timestamp format")

        self.visibility_windows = visibility_windows  # list of (start, end) datetime tuples
        self.score = 0
        self.filtered = False
        self.reason_pruned = None
