# core/reference_priority.py

REFERENCE_PRIORITY = {
    "regions": {
        "coastal": 0.9,
        "urban": 0.8,
        "forest": 0.5,
        "agriculture": 0.4,
        "mountain": 0.3,
        "river": 0.85
    },
    "events": {
        "flood": 1.0,
        "fire": 0.95,
        "urban_change": 0.7,
        "storm": 0.9,
        "normal": 0.2
    },
    "recency_decay_rate": 0.15
}
