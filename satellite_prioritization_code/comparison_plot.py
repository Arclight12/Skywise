# comparison_plot.py
import pandas as pd
import matplotlib.pyplot as plt

# Load results
df_g = pd.read_csv("outputs/greedy_schedule.csv")
df_a = pd.read_csv("outputs/astar_schedule.csv")
df_s = pd.read_csv("outputs/simanneal_schedule.csv")

plt.figure(figsize=(8,5))
plt.plot(df_g["Score"], label="Greedy", marker='o')
plt.plot(df_a["Score"], label="A*", marker='s')
plt.plot(df_s["Score"], label="Simulated Annealing", marker='^')
plt.title("Comparison of Scheduling Algorithms")
plt.xlabel("Transmission Order")
plt.ylabel("Priority Score")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
