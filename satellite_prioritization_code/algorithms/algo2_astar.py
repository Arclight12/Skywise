# algorithms/algo2_astar.py
"""👉 Tips for Member 2:

The A* algorithm explores multiple possibilities rather than just picking the highest score greedily.
They can tweak the heuristic() and weighting factor (0.5) to test different trade-offs.
If they want, they can print how many states were expanded to discuss efficiency."""




import heapq
from datetime import datetime, timedelta
import math

def heuristic(remaining_nodes):
    """Heuristic: estimate total value still possible (sum of remaining scores)."""
    return sum(n.score for n in remaining_nodes)

def schedule_data(filtered_nodes, bandwidth_mb_per_minute=3.0):
    """
    Simplified A* scheduler.
    Treat each partial schedule as a node in search space.
    Goal: maximize total transmitted value under bandwidth constraints.
    """
    start_time = datetime.now().replace(microsecond=0)

    # Initial state: no data transmitted
    start_state = {
        "scheduled": [],         # list of (node, start, end)
        "remaining": filtered_nodes.copy(),
        "current_time": start_time,
        "value": 0.0             # total transmitted score
    }

    # Priority queue for A*
    frontier = []
    heapq.heappush(frontier, (-start_state["value"], start_state))  # max heap (negated value)

    best_schedule = []
    best_value = 0.0

    while frontier:
        neg_value, state = heapq.heappop(frontier)
        total_value = -neg_value

        if total_value > best_value:
            best_value = total_value
            best_schedule = state["scheduled"]

        if not state["remaining"]:
            continue  # nothing left to schedule

        # Explore next nodes (branch)
        for node in list(state["remaining"]):
            # Calculate earliest feasible slot
            for (ws, we) in node.visibility_windows:
                start = max(state["current_time"], ws)
                duration = timedelta(minutes=math.ceil(node.size_mb / bandwidth_mb_per_minute))
                end = start + duration
                if end <= we:
                    new_remaining = [n for n in state["remaining"] if n.id != node.id]
                    new_scheduled = state["scheduled"] + [(node, start, end)]
                    new_value = state["value"] + node.score
                    est_value = new_value + heuristic(new_remaining) * 0.5  # weight heuristic
                    new_state = {
                        "scheduled": new_scheduled,
                        "remaining": new_remaining,
                        "current_time": end,
                        "value": new_value
                    }
                    heapq.heappush(frontier, (-est_value, new_state))
                    break  # one slot per node is enough

    # Format the best schedule
    formatted = []
    for node, s, e in best_schedule:
        formatted.append({
            "Node ID": node.id,
            "Region": node.region,
            "Event": node.event_type,
            "Score": round(node.score, 2),
            "Size (MB)": node.size_mb,
            "Start": s.isoformat(),
            "End": e.isoformat()
        })
    return formatted
