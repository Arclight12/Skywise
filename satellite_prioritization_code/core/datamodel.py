# core/datamodel.py
from datetime import datetime

def _sanitize_csv_string(val):
    if not isinstance(val, str):
        return val
    # Prevent CSV injection by escaping formulas
    if val and val[0] in ('=', '+', '-', '@', '\t', '\r'):
        return f"'{val}"
    return val

class DataNode:
    def __init__(self, id, region, event_type, quality, cloud_cover, size_mb, timestamp, visibility_windows):
        self.id = _sanitize_csv_string(id)
        self.region = _sanitize_csv_string(region)
        self.event_type = _sanitize_csv_string(event_type)

        # Validate numerical ranges
        self.quality = max(0.0, min(1.0, float(quality)))
        self.cloud_cover = max(0.0, min(1.0, float(cloud_cover)))
        self.size_mb = max(0.1, float(size_mb))

        self.timestamp = datetime.fromisoformat(timestamp)
        self.visibility_windows = visibility_windows  # list of (start, end) datetime tuples
        self.score = 0
        self.filtered = False
        self.reason_pruned = None
