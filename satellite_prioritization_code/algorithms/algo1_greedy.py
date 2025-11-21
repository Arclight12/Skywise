# algorithms/algo1_greedy.py
import math
from datetime import datetime, timedelta

def find_earliest_slot(node, current_time, bandwidth_mb_per_minute, schedule):
    for (ws, we) in node.visibility_windows:
        if we <= current_time:
            continue
        start_candidate = max(ws, current_time)
        duration_min = math.ceil(node.size_mb / max(1e-6, bandwidth_mb_per_minute))
        end_candidate = start_candidate + timedelta(minutes=duration_min)
        # Check for overlap with existing intervals
        conflict = False
        for (s, e) in schedule:
            if not (end_candidate <= s or start_candidate >= e):
                conflict = True
                break
        if not conflict and end_candidate <= we:
            return (start_candidate, end_candidate)
    return None

def schedule_data(filtered_nodes, bandwidth_mb_per_minute=3.0):
    """Greedy best-first scheduling based on score."""
    current_time = datetime.now().replace(microsecond=0)
    candidates = sorted(filtered_nodes, key=lambda n: n.score, reverse=True)
    schedule = []
    allocated_intervals = []

    for node in candidates:
        slot = find_earliest_slot(node, current_time, bandwidth_mb_per_minute, allocated_intervals)
        if slot:
            s, e = slot
            allocated_intervals.append((s, e))
            schedule.append({
                "Node ID": node.id,
                "Region": node.region,
                "Event": node.event_type,
                "Score": round(node.score, 2),
                "Size (MB)": node.size_mb,
                "Start": s.isoformat(),
                "End": e.isoformat()
            })
        else:
            schedule.append({
                "Node ID": node.id,
                "Region": node.region,
                "Event": node.event_type,
                "Score": round(node.score, 2),
                "Size (MB)": node.size_mb,
                "Start": None,
                "End": None
            })
    return schedule
