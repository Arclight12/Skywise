# algorithms/algo3_simanneal.py

"""👉 Tips for Member 3:

They can adjust max_iter or cooling_rate to tune how long and how aggressively the algorithm explores.

Try printing best_value over iterations to visualize improvement."""


import random, math
from datetime import datetime, timedelta

def compute_total_value(schedule):
    """Compute total 'value' (sum of scores) for the schedule."""
    return sum(item["Score"] for item in schedule if item["Start"] is not None)

def generate_initial_schedule(nodes, bandwidth_mb_per_minute=3.0):
    """Generate a simple initial schedule (greedy order)."""
    shuffled = nodes.copy()
    random.shuffle(shuffled)
    current_time = datetime.now().replace(microsecond=0)
    schedule = []
    for node in shuffled:
        ws, we = node.visibility_windows[0]
        start = max(current_time, ws)
        duration = timedelta(minutes=math.ceil(node.size_mb / bandwidth_mb_per_minute))
        end = start + duration
        if end <= we:
            current_time = end
            schedule.append({
                "Node ID": node.id,
                "Region": node.region,
                "Event": node.event_type,
                "Score": round(node.score, 2),
                "Size (MB)": node.size_mb,
                "Start": start.isoformat(),
                "End": end.isoformat()
            })
    return schedule

def schedule_data(filtered_nodes, bandwidth_mb_per_minute=3.0, max_iter=2000, temp_start=100, cooling_rate=0.99):
    """
    Simulated Annealing Scheduler.
    Randomly swaps nodes to search for a better schedule.
    """
    current_schedule = generate_initial_schedule(filtered_nodes, bandwidth_mb_per_minute)
    current_value = compute_total_value(current_schedule)
    best_schedule = current_schedule.copy()
    best_value = current_value
    temperature = temp_start

    for i in range(max_iter):
        new_schedule = current_schedule.copy()
        # Randomly swap two tasks
        a, b = random.sample(range(len(new_schedule)), 2)
        new_schedule[a], new_schedule[b] = new_schedule[b], new_schedule[a]

        new_value = compute_total_value(new_schedule)
        delta = new_value - current_value

        if delta > 0 or math.exp(delta / max(1, temperature)) > random.random():
            current_schedule = new_schedule
            current_value = new_value
            if new_value > best_value:
                best_schedule = new_schedule
                best_value = new_value

        temperature *= cooling_rate

    return best_schedule
