# Detailed Trace: Satellite Scheduling with Real Data

## Part 1: What is a "Slot"?

A **slot** is an available **time window** when a satellite can transmit data.

### Visibility Window (Set Once)
Every satellite image has a **visibility window** — the time period when the satellite is above the ground station and can downlink data:

```python
# In main.py:
now = datetime.now().replace(microsecond=0)
vw = [(now + timedelta(minutes=10), now + timedelta(minutes=60))]
```

**For your data (Nov 28, 2025, ~20:43:28)**:
- All nodes have the same visibility window: **20:43:28 to 21:13:28** (50 minutes total)
- After 21:13:28, NO nodes can transmit (satellite is gone)

### Time Slot (Allocated During Scheduling)
A **slot** is a chunk of time **allocated to one node** during that visibility window.

**Example**:
```
Visibility Window: 20:43:28 ──────────────────────── 21:13:28 (50 min)

Slot 1 (img_16, 40 MB @ 3 MB/min):
         20:43:28 ────────────── 20:57:28 (14 min)

Slot 2 (img_11, 37 MB @ 3 MB/min):
                     20:57:28 ──────────── 21:10:28 (12.3 min)

Slot 3 (img_1, 35 MB @ 3 MB/min):
                                 21:10:28 ──────────── 21:22:28 (12 min)
                                 ^^^ EXCEEDS visibility window! ✗
```

---

## Part 2: Concrete Trace with Real Data

### Setup (Actual Execution)
- **Bandwidth**: 3 MB/min (fixed)
- **Current time**: 2025-11-28 15:24:33 (when algorithms run - `datetime.now()`)
- **Visibility window**: 15:24:33 to 15:54:33 (30 minutes available = 50 min in code, but only 30 min shown in outputs)
- **Available nodes** (filtered: 19 total, top 5 by score):
  - img_16: 72.56, 40 MB → ⌈40/3⌉ = 14 min to download
  - img_11: 71.16, 37 MB → ⌈37/3⌉ = 13 min
  - img_1: 68.85, 35 MB → ⌈35/3⌉ = 12 min
  - img_7: 68.17, 38 MB → ⌈38/3⌉ = 13 min
  - img_17: 63.37, 44 MB → ⌈44/3⌉ = 15 min

---

## Algorithm 1: GREEDY (Actual Results)

**Strategy**: Sort by score (highest first), try to fit each node.

**ACTUAL OUTPUT**:
```
img_16: 72.56, 40MB, 15:24:33 → 15:38:33 ✓ SCHEDULED (14 min)
img_11: 71.16, 37MB, (blank) ✗ NOT SCHEDULED
img_1: 68.85, 35MB, (blank) ✗ NOT SCHEDULED
img_7: 68.17, 38MB, (blank) ✗ NOT SCHEDULED
... (all others not scheduled)
```

**Why only 1 node?**

Looking at the greedy code:

```python
def schedule_data(filtered_nodes, bandwidth_mb_per_minute=3.0):
    current_time = datetime.now().replace(microsecond=0)
    candidates = sorted(filtered_nodes, key=lambda n: n.score, reverse=True)
    schedule = []
    allocated_intervals = []

    for node in candidates:
        slot = find_earliest_slot(node, current_time, bandwidth_mb_per_minute, allocated_intervals)
        # ↑ current_time is NEVER updated after a node is scheduled!
```

**Trace**:
```
current_time = 15:24:33 (fixed!)
allocated_intervals = []

Iter 1 - img_16 (40 MB):
  find_earliest_slot(img_16, 15:24:33, 3.0, [])
  → start = max(15:24:33, 15:24:33) = 15:24:33
  → duration = 14 min
  → end = 15:38:33
  → is 15:38:33 <= 15:54:33? YES ✓
  → conflicts with []? NO ✓
  ✅ SCHEDULE: (15:24:33, 15:38:33)
  allocated_intervals = [(15:24:33, 15:38:33)]
  current_time STAYS 15:24:33 ⚠️

Iter 2 - img_11 (37 MB):
  find_earliest_slot(img_11, 15:24:33, 3.0, [(15:24:33, 15:38:33)])
  → start = max(15:24:33, 15:24:33) = 15:24:33  (SAME!)
  → duration = 13 min
  → end = 15:37:33
  → Check conflicts with [(15:24:33, 15:38:33)]:
    - Does (15:24:33, 15:37:33) overlap (15:24:33, 15:38:33)? 
    - YES! 15:24:33 is within [15:24:33, 15:38:33) ✗
  → conflict = True
  → return None
  ❌ NOT SCHEDULED

Iter 3-19 - All same issue:
  current_time still 15:24:33, all conflict with img_16
  ❌ NOT SCHEDULED
```

**Root cause**: The greedy algorithm **doesn't advance current_time** after scheduling each node. This is a **bug** in the greedy implementation!

---

## Algorithm 2: A* (Actual Results)

**Strategy**: Explore partial schedules using priority queue; return best complete schedule.

**ACTUAL OUTPUT**:
```
img_16: 72.56, 40MB, 15:24:33 → 15:38:33 ✓ SCHEDULED (14 min)
img_11: 71.16, 37MB, 15:38:33 → 15:51:33 ✓ SCHEDULED (13 min)
img_1:  68.85, 35MB, 15:51:33 → 16:03:33 ✓ SCHEDULED (12 min)
img_8:  53.83, 33MB, 16:03:33 → 16:14:33 ✓ SCHEDULED (11 min)
```

**Total scheduled time**: 14 + 13 + 12 + 11 = 50 minutes = **exactly fills visibility window**

**Why 4 nodes?**

A* explores many paths and picks the one with highest total value. It updates `current_time` after each node:

```
Start state: scheduled=[], remaining=[all 19 nodes], value=0, current_time=15:24:33

Explore path 1: Add img_16
  scheduled=[img_16], remaining=[18 nodes], value=72.56
  current_time=15:38:33  ← UPDATED!
  
  Explore sub-path 1a: Add img_11
    scheduled=[img_16, img_11], value=72.56+71.16=143.72
    current_time=15:51:33  ← UPDATED!
    
    Explore sub-sub-path: Add img_1
      scheduled=[img_16, img_11, img_1], value=143.72+68.85=212.57
      current_time=16:03:33  ← UPDATED!
      
      Explore sub-sub-sub-path: Add img_8
        scheduled=[img_16, img_11, img_1, img_8], value=212.57+53.83=266.4
        current_time=16:14:33  ← UPDATED!
        
        Try to add img_7 (38 MB):
          Would end at 16:28:33
          Visibility window ends at 15:54:33
          ✗ Can't fit! (But A* doesn't enforce this check)
          
        Best path found: [img_16, img_11, img_1, img_8] with value=266.4
```

**Key**: A* adds nodes **during search**, updates time, and explores further down the tree until it can't add more.

---

## Algorithm 3: Simulated Annealing (Actual Results)

**Strategy**: Start with random schedule, swap items, accept improvements or sometimes worse moves.

**ACTUAL OUTPUT**:
```
img_3:  47.9, 28MB, 15:24:33 → 15:34:33 ✓ (10 min)
img_16: 72.56, 40MB, 15:34:33 → 15:48:33 ✓ (14 min)
img_15: 15.71, 27MB, 15:48:33 → 15:57:33 ✓ (9 min)
img_19: 31.37, 23MB, 15:57:33 → 16:05:33 ✓ (8 min)
img_18: 24.62, 26MB, 16:05:33 → 16:14:33 ✓ (9 min)
```

**Total scheduled**: 10 + 14 + 9 + 8 + 9 = 50 minutes

**Why different nodes than A*?**

Simulated Annealing is **stochastic** (random). It:
1. Generates a random full schedule initially
2. Swaps items repeatedly
3. Accepts improvements, and occasionally worse solutions to escape local optima
4. Returns the best found

**This run found**: `[img_3, img_16, img_15, img_19, img_18]` with total value = 47.9+72.56+15.71+31.37+24.62 = 192.25

**A* found**: `[img_16, img_11, img_1, img_8]` with total value = 72.56+71.16+68.85+53.83 = 266.4

**Why is A*'s value higher?** A* greedily picks the highest-score items first, while Sim Ann happened to find a suboptimal local optimum (5 lower-score items instead of 4 high-score items).
