
# 🚀 Max Profit Problem – Mars Land Development

## 1️⃣ Problem Overview

You are **Mr. X**, owner of a large strip of land on Mars. Your mission: **maximize profit** by strategically building properties.

You have **three types of properties**:

| Property            | Build Time (units) | Earning Rate (per remaining time unit) |
| ------------------- | ------------------ | -------------------------------------- |
| **Theatre**         | 5                  | $1500                                  |
| **Pub**             | 4                  | $1000                                  |
| **Commercial Park** | 10                 | $3000                                  |

**Constraints:**

* Only **one property can be built at a time** (no parallel construction).
* A property **starts earning only after it is completed**.
* Total available time (`n`) is provided as input.

**Goal:** Determine the combination of properties that **maximizes earnings** within the available time.

---

## 2️⃣ Key Insights

* **Early completion = higher profit**

  > A building that finishes early will earn for more remaining time units.

* **Choice matters**

  > Picking which building to construct at each step affects total earnings.

* **Dynamic Programming fits naturally**

  > By breaking the problem into smaller subproblems (profit achievable for smaller time units), we can efficiently find the optimal solution.

---

## 3️⃣ Step-by-Step Approach

### Step 1: Understand Earnings

A building starts earning **after construction**:

```text
Profit = (time left after completion) × earning rate
```

---

### Step 2: Manual Example

**Example:** n = 7

| Building        | Time Needed | Time Left | Profit          |
| --------------- | ----------- | --------- | --------------- |
| Theatre         | 5           | 2         | 2 × 1500 = 3000 |
| Pub             | 4           | 3         | 3 × 1000 = 3000 |
| Commercial Park | 10          | —         | Cannot build    |

✅ **Maximum earnings = $3000**

> Achievable with either Theatre or Pub.

---

### Step 3: Dynamic Programming (DP) Approach

We define a DP table:

* `dp[t]` = **maximum profit achievable** with `t` total time units.

**Transition formula:**

```text
dp[t] = max(
    dp[t - build_time_of_building] + (remaining_time × earning_rate)
)
```

> This ensures at every step we choose the **best building**.

---

### Step 4: Dry Run Example (n = 13)

| Time Left (t) | Max Earnings | Best Building |
| ------------- | ------------ | ------------- |
| 0–3           | 0            | None          |
| 4             | 0            | None          |
| 5             | 1000         | Pub           |
| 6             | 2000         | Pub           |
| 7             | 3000         | Theatre/Pub   |
| 8             | 4500         | Theatre       |
| 9             | 6000         | Theatre/Pub   |
| 10            | 8500         | Theatre       |
| 11            | 11000        | Theatre       |
| 12            | 13500        | Theatre       |
| 13            | 16500        | Theatre       |

---

### Step 5: Reconstruct Building Sequence

1. Start at `t = n`.
2. Pick the building that gives **maximum profit** at that time.
3. Subtract its build time → move to remaining time.
4. Repeat until no time is left.

**Example (n = 13):**

```
t = 13 → Theatre → finish at t = 8
t = 8  → Theatre → finish at t = 3
t = 3  → cannot fit any building → stop
```

✅ **Result:**

* T = 2, P = 0, C = 0
* **Total earnings = $16,500**

---

## 6️⃣ Why This Approach Works

* Considers **all possible choices at every time unit** → no better combination is missed.
* **DP prevents recalculating** subproblems → efficient.
* Tracing back the DP table gives the **exact sequence of buildings** for maximum profit.

---

## 7️⃣ Summary

This problem demonstrates a **real-world resource optimization** scenario:

* Strategic planning of construction
* Maximizing earnings under **time constraints**
* Using **Dynamic Programming** to solve efficiently

---

### Optional Visual (Recommended for README)

You could add a **diagram or flowchart** showing:

```
Total Time -> Choose Best Building -> Subtract Build Time -> Repeat
```
