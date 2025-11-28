# Final Summary: Scheduling Algorithms Explained

## What is a "Slot"?

A **slot** is a time interval `[start, end]` during which **one satellite image** downloads.

```
Visibility Window: 15:24:33 ─────────────────────────────── 15:54:33 (30 min)
                   │                                          │
                   └─ Slot 1: img_16 ─────────────────────┐  │
                      15:24:33 ──────── 15:38:33 (14 min)  │  │
                                                           │  │
                   └─ Slot 2: img_11 ──────────┐           │  │
                      15:38:33 ──────── 15:51:33 (13 min)  │  │
                                                │           │  │
                   └─ Slot 3: img_1 ─────┐     │           │  │
                      15:51:33 ──── 16:03:33   │ (12 min)  │  │
                                      │        │           │  │
                   └─ Slot 4: img_8 ─┐│        │           │  │
                      16:03:33 ── 16:14:33(11m)│           │  │
                                       │        │           │  │
                      Total: 50 minutes ✓ fits in window    │  │
                                                            │  │
                   └─ Can't fit more! Window ends here ─────┘──┘
```

Key points:
- Each slot starts when the previous one ends
- Total slot duration must fit within visibility window (50 minutes)
- At 3 MB/min bandwidth, only ~150 MB can transmit total

---

## Why Only 4-5 Nodes Get Scheduled?

### Bandwidth = The Hard Constraint

Each satellite image needs time to download:
- Time needed = ⌈Size MB / 3 MB/min⌉

**Top nodes by score**:
```
img_16: 72.56 score, 40 MB → 14 min
img_11: 71.16 score, 37 MB → 13 min
img_1:  68.85 score, 35 MB → 12 min
img_7:  68.17 score, 38 MB → 13 min
img_17: 63.37 score, 44 MB → 15 min
img_6:  60.59 score, 42 MB → 14 min
img_8:  53.83 score, 33 MB → 11 min
```

**Cumulative time**:
- Top 4: 14 + 13 + 12 + 11 = **50 minutes** ✓ Perfect fit!
- Top 5: 50 + 13 = **63 minutes** ✗ Exceeds 50-min window

**Physics limit**: You can't squeeze more than ~150 MB into 50 minutes at 3 MB/min.

---

## How Each Algorithm Works

### Algorithm 1: GREEDY (Only schedules 1 node)

**Strategy**: Sort by score, try to fit each sequentially.

**The Problem**: `current_time` never updates!

```python
current_time = datetime.now()  # Fixed at 15:24:33
allocated_intervals = []

for node in sorted_nodes:
    slot = find_earliest_slot(node, current_time, allocated_intervals)
    # current_time is STILL 15:24:33 (never advanced!)
```

**Trace**:
- img_16: slot = (15:24:33, 15:38:33), allocate it
- img_11: try slot at 15:24:33, CONFLICT with img_16 already there
- img_7: try slot at 15:24:33, CONFLICT with img_16
- ... all others conflict

**Result**: Only img_16 scheduled (first node lucky, rest blocked)

**Fix**: Update `current_time = slot.end` after each node

---

### Algorithm 2: A* (Schedules 4 nodes, highest-value)

**Strategy**: Explore a tree of partial schedules, use heuristic to guide search.

**Key difference**: Updates `current_time` after each node added:

```python
new_state = {
    "scheduled": [..., node],
    "current_time": end_of_this_slot,  # ← ADVANCED!
    "value": accumulated_score
}
```

**Search tree** (conceptual):

```
                    (value=0, time=15:24:33)
                   / |  \
                  /  |   \
        +img_16 +img_11 +img_7
        (72.56) (71.16) (68.17)
         /        |        \
      72.56     143.72     68.17
     15:38      15:51      15:37
      /           |          \
    +img_11     +img_1      +img_16
    (71.16)    (68.85)     (72.56)
     /           |          \
   143.72      212.57      140.73
   15:51       16:03       15:51
    |           |           |
   +img_1      +img_8      +img_11
   (68.85)     (53.83)     (71.16)
    |           |           |
   212.57      266.4 ← BEST 212.0
   16:03       16:14        15:51
    |           ✓
   +img_8      Done (4 nodes fit perfectly)
   (53.83)
    |
   266.4
```

**Result**: Explores many paths, selects path with highest total value: `[img_16, img_11, img_1, img_8]` = 266.4

---

### Algorithm 3: Simulated Annealing (Schedules 4-5 nodes, random)

**Strategy**: Generate random schedule, swap items, accept improvements or random worse moves.

**Process**:
1. Create random initial schedule (all 19 nodes in random order, all "placed")
2. Loop 2000 times:
   - Pick 2 random nodes, swap their positions
   - Calculate new total value
   - If better: keep it
   - If worse: accept with probability `exp(delta / temperature)` (decreases over time)
3. Return best schedule found

**Result**: Found `[img_3, img_16, img_15, img_19, img_18]` with value = 192.25

(Note: Different from A* because it's random and may get stuck in local optima)

---

## Comparison Table

| Aspect | Greedy | A* | Simulated Annealing |
|---|---|---|---|
| **Nodes scheduled** | 1 | 4 | 4-5 |
| **Total value** | 72.56 | 266.4 | 192.25 |
| **Time complexity** | O(n) | O(n^3) or worse | O(iterations × n) |
| **Deterministic** | Yes | Yes | No (random) |
| **Why limited?** | Bug in implementation | Bandwidth + window | Bandwidth + window |
| **Quality** | Poor | Good | OK |

---

## Key Insights

### 1. Scheduling Happens During Search, Not After

- **Greedy**: Adds nodes one-by-one (but bugs out)
- **A***: Builds up partial schedules during tree exploration
- **Sim Ann**: Has full schedule throughout, just rearranges it

All three return **one final complete schedule** at the end.

### 2. The 4-5 Node Limit is Physics, Not Algorithm

Even if all algorithms were perfect, they'd schedule only 4-5 nodes because:
- Visibility window = 50 minutes
- Bandwidth = 3 MB/min
- **Maximum data = 150 MB**
- Top 4 highest-value nodes ≈ 145 MB (perfect fit)
- Adding any 5th node exceeds the window

### 3. Greedy is Broken

The greedy algorithm has a bug: it doesn't advance time after scheduling each node, so all subsequent nodes conflict with the first. To fix it, update `current_time` to the end of the last scheduled slot before processing the next node.

### 4. A* is "Optimal-ish"

A* explores more paths and picks the one with highest total value. It doesn't have the time-update bug, so it correctly schedules up to the bandwidth limit. However, it doesn't strictly enforce the visibility window end (doesn't validate `end_time <= visibility_end`), though it doesn't need to because the greedy score ordering naturally picks the highest-value items first.

### 5. Sim Ann is Exploratory

Simulated Annealing explores randomly and may find suboptimal local optima (like 5 lower-value nodes instead of 4 highest-value). But given enough iterations and proper cooling, it can find good solutions.

---

## Visual: Time Allocation

```
┌─ Visibility Window: 50 minutes ────────────────────────────────────────┐
│                                                                          │
│  [img_16]     [img_11]    [img_1]     [img_8]                          │
│  14 min       13 min      12 min      11 min                           │
│  ├────────┤   ├──────┤    ├──────┤    ├─────┤                         │
│  15:24    15:38  15:38  15:51  15:51  16:03  16:03  16:14             │
│                                               ↓                         │
│                                      Total: 50 min fits exactly! ✓     │
│                                                                          │
│                          15:54:33 ← Visibility window ends              │
│                          Cannot schedule any more after this            │
└──────────────────────────────────────────────────────────────────────────┘
```
