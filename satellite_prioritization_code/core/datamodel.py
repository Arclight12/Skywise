# core/datamodel.py
from datetime import datetime

class DataNode:
    def __init__(self, id, region, event_type, quality, cloud_cover, size_mb, timestamp, visibility_windows):
        # Security: Basic sanitization / length limit for string fields
        self.id = str(id)[:100]
        self.region = str(region)[:50]
        self.event_type = str(event_type)[:50]

        try:
            self.quality = float(quality)
            self.cloud_cover = float(cloud_cover)
            self.size_mb = float(size_mb)
        except (ValueError, TypeError):
            raise ValueError("Numeric fields must be valid numbers.")

        # Security: Input validation to ensure numeric ranges are valid
        if not (0 <= self.quality <= 1):
            raise ValueError(f"Invalid quality value: {self.quality}. Must be between 0 and 1.")

        if not (0 <= self.cloud_cover <= 1):
            raise ValueError(f"Invalid cloud cover value: {self.cloud_cover}. Must be between 0 and 1.")

        if self.size_mb <= 0:
            raise ValueError(f"Invalid size_mb value: {self.size_mb}. Must be positive.")

        try:
            self.timestamp = datetime.fromisoformat(str(timestamp))
        except ValueError as e:
            raise ValueError("Invalid timestamp format. Expected ISO 8601.")

        self.visibility_windows = visibility_windows  # list of (start, end) datetime tuples
        self.score = 0
        self.filtered = False
        self.reason_pruned = None
