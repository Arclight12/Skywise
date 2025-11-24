
# 🌍 Intelligent Downlink Prioritization for Earth Observation Satellites

### *A Comparative Study of Classical AI Algorithms for Data Classification and Scheduling*

---

## 📘 Overview

Earth Observation (EO) satellites capture **massive volumes of imagery and sensor data** every day — far more than what can be transmitted to Earth in real time due to **limited bandwidth and visibility windows**.
This creates a need for an **intelligent prioritization and scheduling system** that can decide:

* Which data is **important enough** to transmit first
* How to **schedule** those transmissions efficiently

Our project implements an **AI-inspired decision system** that performs both **classification** and **scheduling**, using classical algorithms instead of machine learning models.

---

## 🧠 The Original Idea (and Why We “PCA’d” It)

Initially, the project was conceptualized as a **machine learning–based system**:

* The plan was to train an **AI model** capable of learning from past satellite data to classify and prioritize new data intelligently.
* This would have involved deep learning models that interpret spatial, temporal, and contextual importance.

However, after feedback from our faculty guide, we were advised to **simplify the scope** to a level that uses **concepts we’ve learned in class**, while still maintaining the intelligence of the original idea.

So, just like applying **PCA (Principal Component Analysis)** to reduce a complex dataset into its most important features,
we **dimensionally reduced** our original concept from a full ML system into **algorithmic components** that simulate intelligent behavior using classical AI techniques —
namely, **Tree-based Filtering** and **Heuristic Search Algorithms**.

This approach preserves the logical essence of the ML design (decision-making + optimization) while keeping it implementation-friendly and educational.

---

## ⚙️ System Architecture

Our system works in **two stages**, reflecting how an AI model might first classify and then optimize actions.

### **1️⃣ Stage 1: Tree-Based Filtering (Classification)**

This common module simulates the “learning” and “decision” stage of an AI system.

* Each incoming satellite data point (e.g., an image) is evaluated based on:

  * **Region importance** (e.g., disaster-prone or coastal areas)
  * **Event type** (e.g., flood, fire, storm)
  * **Cloud cover**
  * **Image quality**
  * **Recency** (how old the data is)

* Using these features, a **decision tree** evaluates each data node’s usefulness.
  Low-value or redundant data is **pruned using alpha–beta pruning**, leaving only high-importance data for scheduling.

This stage answers:
📸 *“Which data is worth sending?”*

---

### **2️⃣ Stage 2: Scheduling (Optimization)**

After filtering, we have a set of valuable data points.
The next challenge is to decide **in what order to transmit them**, considering:

* Bandwidth limits
* Energy consumption
* Ground station visibility windows

This is where we use **three different algorithms** — each implemented by one team member.

| Algorithm               | Approach           | Description                                                                                                                    |
| ----------------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| **Greedy (Heuristic)**  | Deterministic      | Picks the highest-score data first and assigns the earliest available slot (fast and straightforward).                         |
| **A* Search**           | Graph-based search | Explores possible schedules as paths in a state space, guided by a heuristic that estimates total mission value.               |
| **Simulated Annealing** | Probabilistic      | Starts with a random schedule and iteratively improves it by controlled randomization, mimicking thermal annealing in physics. |

This stage answers:
🕒 *“When and in what order should data be sent?”*

---

## 🧩 Project Structure

```
satellite_prioritization_project/
│
├── data/
│   └── satellite_data.csv          # Common input dataset
│
├── core/
│   ├── datamodel.py                # Defines DataNode class (data structure)
│   ├── filter.py                   # Common tree-based filtering logic
│   └── reference_priority.py       # Reference importance weights
│
├── algorithms/
│   ├── algo1_greedy.py             # Greedy / heuristic scheduling (Kalidas)
│   ├── algo2_astar.py              # A* search-based scheduling
│   └── algo3_simanneal.py          # Simulated annealing scheduling
│
├── outputs/
│   ├── greedy_schedule.csv
│   ├── astar_schedule.csv
│   └── simanneal_schedule.csv
│
├── main.py                         # Runs filtering + all 3 algorithms
└── comparison_plot.py              # Plots and compares results visually
```

---

## 🚀 How It Works (Step-by-Step)

1. **Load Data**

   * A dataset of satellite observations (`data/satellite_data.csv`) is loaded.
   * Each entry contains metadata like region, event type, quality, etc.

2. **Filter Data (Common Step)**

   * The `filter.py` module assigns each data point a **score** (0–100).
   * Low-value entries are pruned.

3. **Schedule (Algorithm-Specific)**

   * Each member’s algorithm independently schedules the filtered data.
   * Output is saved as CSV in the `outputs/` folder.

4. **Compare & Analyze**

   * `comparison_plot.py` plots and compares all three scheduling strategies.
   * Helps visualize differences in prioritization and performance.

---

## 📈 Example Comparison Graph

```
↑ Priority Score
│
│      ● Greedy
│    ▲ A*
│  ■ Simulated Annealing
│
└──────────────→ Transmission Order
```

The chart reveals how each algorithm prioritizes data differently.
For example, A* may achieve a more balanced schedule, while greedy might favor high-score data immediately.

---

## 👨‍💻 Team Roles

| Member       | Role      | Contribution                                               |
| ------------ | --------- | ---------------------------------------------------------- |
| **Kalidas**  | Team Lead | Base setup, greedy scheduling, integration & visualization |
| **Aadarsh** | Developer | Implemented A* scheduling algorithm                        |
| **Vishnu S** | Developer | Implemented Simulated Annealing scheduling algorithm       |

All members contributed to code integration, testing, and analysis.

---

## 🎯 Objectives Achieved

* ✅ Translated a **complex AI concept** into a classical algorithmic simulation
* ✅ Demonstrated the difference between **deterministic, search-based, and probabilistic** methods
* ✅ Implemented modular, comparable algorithms using a shared data pipeline
* ✅ Produced quantitative and visual comparisons for analysis

---

## 🧩 Future Enhancements

* Integrate an actual **ML model** to learn weights or heuristic values automatically.
* Incorporate **real satellite metadata** (e.g., from NASA Earth Data or ISRO open datasets).
* Extend scheduling logic to consider **energy optimization** and **multi-satellite networks**.
* Deploy the system as a **simulation dashboard** for educational or research use.

---

## 🧠 Key Concepts Used

* **Heuristic Search** (A*, Greedy, Simulated Annealing)
* **Alpha–Beta Pruning** (Tree-based filtering)
* **Scheduling Optimization**
* **AI-inspired Decision Logic**
* **Feature-driven Evaluation without ML**

---

## 🪐 In Short

> This project began as an **AI model idea** for intelligent satellite downlink management.
>
> Through guided simplification, we **converted** that concept into a **classical AI simulation** —
> applying heuristic algorithms, search optimization, and pruning techniques to emulate intelligent decision-making.
>
> The result is a clean, modular system that blends **AI logic, optimization, and teamwork** —
> demonstrating how algorithmic thinking can achieve near-intelligent behavior even without machine learning.

---

## 📸 Sample Output Snapshot

| Node ID | Region  | Event  | Score | Size (MB) | Start | End   |
| ------- | ------- | ------ | ----- | --------- | ----- | ----- |
| img_1   | coastal | flood  | 92.3  | 30        | 10:00 | 10:10 |
| img_2   | river   | fire   | 88.7  | 25        | 10:15 | 10:22 |
| img_3   | urban   | normal | 60.4  | 40        | 10:30 | 10:40 |

---

## 🧩 License

This project is open for educational and research use.
All algorithms are original implementations by the team.

---
