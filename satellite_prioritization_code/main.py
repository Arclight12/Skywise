# main.py
import pandas as pd
from datetime import datetime, timedelta
from core.datamodel import DataNode
from core.filter import decision_tree_filter
from core.reference_priority import REFERENCE_PRIORITY

from algorithms.algo1_greedy import schedule_data as greedy_schedule
from algorithms.algo2_astar import schedule_data as astar_schedule
from algorithms.algo3_simanneal import schedule_data as sa_schedule

# -------- Load dataset --------
def load_dataset(csv_path="data/satellite_data.csv"):
    df = pd.read_csv(csv_path)
    nodes = []
    for _, row in df.iterrows():
        try:
            # Input validation and type casting
            quality = float(row.quality)
            cloud_cover = float(row.cloud_cover)
            size_mb = float(row.size_mb)

            if not (0 <= quality <= 1) or not (0 <= cloud_cover <= 1) or size_mb <= 0:
                continue

            id_str = str(row.id)[:50]
            region_str = str(row.region)[:50]
            event_type_str = str(row.event_type)[:50]

            # dummy visibility window (for now)
            now = datetime.now().replace(microsecond=0)
            vw = [(now + timedelta(minutes=10), now + timedelta(minutes=60))]
            node = DataNode(
                id=id_str,
                region=region_str,
                event_type=event_type_str,
                quality=quality,
                cloud_cover=cloud_cover,
                size_mb=size_mb,
                timestamp=row.timestamp,
                visibility_windows=vw
            )
            nodes.append(node)
        except (ValueError, TypeError):
            # Skip invalid rows securely to prevent leaking info
            continue
    return nodes

if __name__ == "__main__":
    print("\n=== Intelligent Satellite Downlink Prioritization (Team Version) ===\n")

    # Step 1: Load data
    nodes = load_dataset()

    # Step 2: Filter (common for all algorithms)
    filtered_nodes = decision_tree_filter(nodes, REFERENCE_PRIORITY, score_threshold=10.0)
    print(f"Filtered Nodes: {len(filtered_nodes)} remain after pruning\n")

    # Step 3: Run all algorithms
    greedy = greedy_schedule(filtered_nodes)
    astar = astar_schedule(filtered_nodes)
    sa = sa_schedule(filtered_nodes)

    # Step 4: Save outputs
    pd.DataFrame(greedy).to_csv("outputs/greedy_schedule.csv", index=False)
    pd.DataFrame(astar).to_csv("outputs/astar_schedule.csv", index=False)
    pd.DataFrame(sa).to_csv("outputs/simanneal_schedule.csv", index=False)

    print("Schedules saved in 'outputs/' folder.")
    print("Next: Run 'comparison_plot.py' to visualize the differences.")
