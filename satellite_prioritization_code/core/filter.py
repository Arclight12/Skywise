# core/filter.py
import math
from datetime import datetime

def evaluate_node_score(node, reference):
    region_w = reference["regions"].get(node.region, 0.3)
    event_w = reference["events"].get(node.event_type, 0.2)
    quality_factor = node.quality * (1 - node.cloud_cover)
    hours_old = max(0.0, (datetime.now() - node.timestamp).total_seconds() / 3600.0)
    recency_factor = math.exp(-reference["recency_decay_rate"] * hours_old)
    base_score = (0.5 * region_w + 0.4 * event_w) * quality_factor * recency_factor
    return base_score * 100.0

def decision_tree_filter(nodes, reference, score_threshold=10.0):
    survivors = []
    for node in nodes:
        node.score = evaluate_node_score(node, reference)
        if node.score >= score_threshold:
            survivors.append(node)
        else:
            node.filtered = True
    return survivors
