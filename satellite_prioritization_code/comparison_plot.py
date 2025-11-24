# comparison_plot.py
import pandas as pd
import matplotlib.pyplot as plt

# Load original data
df_original = pd.read_csv("data/satellite_data.csv")

# Load results
df_g = pd.read_csv("outputs/greedy_schedule.csv")
df_a = pd.read_csv("outputs/astar_schedule.csv")
df_s = pd.read_csv("outputs/simanneal_schedule.csv")

# Create figure with 3 subplots (one for each algorithm)
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
fig.suptitle('Satellite Downlink Prioritization - Algorithm Comparison', fontsize=16, fontweight='bold')

algorithms = [
    ('Greedy', df_g, '#FF6B6B'),
    ('A* Search', df_a, '#4ECDC4'),
    ('Simulated Annealing', df_s, '#95E1D3')
]

for idx, (name, df, color) in enumerate(algorithms):
    ax = axes[idx]
    
    # Get scheduled and unscheduled nodes
    scheduled = df[df['Start'].notna()]
    unscheduled = df[df['Start'].isna()]
    
    # Create bar chart showing priority scores
    all_nodes = list(df['Node ID'])
    scores = list(df['Score'])
    colors_list = [color if pd.notna(df.iloc[i]['Start']) else '#CCCCCC' 
                   for i in range(len(df))]
    
    bars = ax.bar(range(len(all_nodes)), scores, color=colors_list, edgecolor='black', alpha=0.8)
    
    # Customize plot
    ax.set_title(f'{name}\n({len(scheduled)}/{len(df)} nodes scheduled)', 
                 fontweight='bold', fontsize=12)
    ax.set_xlabel('Satellite Image ID', fontweight='bold')
    ax.set_ylabel('Priority Score', fontweight='bold')
    ax.set_xticks(range(len(all_nodes)))
    ax.set_xticklabels(all_nodes, rotation=45, ha='right')
    ax.grid(True, alpha=0.3, axis='y')
    
    # Add total value text
    total_value = scheduled['Score'].sum() if len(scheduled) > 0 else 0
    ax.text(0.5, 0.95, f'Total Value: {total_value:.1f}', 
            transform=ax.transAxes, ha='center', va='top',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8),
            fontweight='bold', fontsize=10)
    
    # Add legend
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor=color, edgecolor='black', label='Scheduled'),
        Patch(facecolor='#CCCCCC', edgecolor='black', label='Not Scheduled')
    ]
    ax.legend(handles=legend_elements, loc='upper right', fontsize=9)

plt.tight_layout()
plt.savefig('outputs/prioritization_comparison.png', dpi=300, bbox_inches='tight')
print("\nVisualization saved as 'outputs/prioritization_comparison.png'")
plt.show()
