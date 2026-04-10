# 28. Greedy Algorithms

## Overview

Greedy algorithms build a solution step by step by taking the best-looking choice **right now**.

The key question is not "does this feel smart locally?" The key question is:

**Can I prove this local choice never blocks a globally optimal answer later?**

When that is true, greedy often gives an elegant `O(n)` or `O(n log n)` solution.

---

## The Two Properties You Need

### 1) Greedy Choice Property

There exists a local decision rule (for example, pick smallest end time, pick largest reachable jump, pick cheapest valid action) that can be part of some global optimum.

### 2) Optimal Substructure

After making that greedy choice, the remaining problem is the same type of problem on a smaller input.

If both properties hold, greedy is usually safe.

---

## How to Identify Greedy Problems

Use this quick checklist:

1. Can the problem be solved by repeatedly making one local decision?
2. If I commit to a local best choice, does the rest remain a smaller version of the same problem?
3. Can I argue that any optimal solution can be transformed to include my local choice (exchange argument)?

Strong greedy signals in problem statements:

- "maximum number of intervals/tasks/events"
- "minimum number of jumps/stops/resources"
- "can you reach"
- "schedule with no overlap"
- "merge / select / cover with minimum"

Common ingredients:

- Sorting by one key (end time, start time, cost, ratio)
- One pass with a running best/farthest
- Heap for "best available option so far"

---

## Greedy Proof Strategies (Simple Version)

### A) Exchange Argument

Show that if an optimal solution does not use your greedy choice, you can swap one choice and keep it optimal.

### B) Stay-Ahead Argument

Show that after each step, greedy is at least as good as any other strategy so far.

### C) Cut Property (for some graph problems)

Show that best edge crossing a cut is always safe to take.

---

## Common Traps (When Greedy Fails)

Greedy is often wrong when:

1. Future choices strongly depend on exact earlier choices.
2. Local best can create irreversible bad structure later.
3. Problem asks for counting all ways (usually DP/combinatorics territory).

Classic failure example:

- Coin system `[1, 3, 4]`, amount `6`
- Greedy picks `4 + 1 + 1` (3 coins)
- Optimal is `3 + 3` (2 coins)

So not all coin change problems are greedy-safe.

---

## Strategy Template (Use in Interviews)

1. Propose local rule in one sentence.
2. Pick sort key or data structure (array scan / heap).
3. Dry-run tiny input manually.
4. State why this local decision is safe (exchange/stay-ahead).
5. Implement and check edge cases.

---

## Learning Path: Simple to Complex

This order is intentional. Each step reuses the previous intuition.

1. Assign Cookies (sorting + two pointers)
2. Lemonade Change (local feasibility)
3. Jump Game (farthest reachable frontier)
4. Jump Game II (layered frontier)
5. Interval Scheduling / Erase Overlap (sort by end)
6. Minimum Number of Arrows to Burst Balloons (interval greedy variant)
7. Gas Station (prefix deficit insight)
8. Task Scheduler (count-frequency formula)
9. Candy (two-pass greedy)
10. Minimum Number of Refueling Stops (heap + deferred greedy)

---

## Worked Examples: Easiest to Harder

### Example 1: Assign Cookies (Easy)

**Problem:** Each child has greed factor `g[i]`; each cookie has size `s[j]`. A child is satisfied if cookie size >= greed. Maximize satisfied children.

**Greedy rule:** Give the smallest possible cookie that can satisfy the current least-greedy child.

**Why it works:** Using a larger cookie on an easier child can only hurt harder children later.

```python
def find_content_children(g, s):
	g.sort()
	s.sort()

	i = j = 0
	while i < len(g) and j < len(s):
		if s[j] >= g[i]:
			i += 1  # this child is satisfied
		j += 1      # cookie j is used (or discarded)

	return i

print(find_content_children([1, 2, 3], [1, 1]))      # 1
print(find_content_children([1, 2], [1, 2, 3]))      # 2
print(find_content_children([2, 3, 4], [1, 1, 5]))   # 1
```

**Complexity:** Time `O(n log n + m log m)`, Space `O(1)` extra (excluding sort internals)

**Brute Force vs Greedy:**

1. Brute force idea: try all assignments of cookies to children and keep the maximum satisfied count.
2. Why brute force is expensive: matching combinations blow up quickly (combinatorial/exponential search).
3. Why greedy compresses it: sorting both lists and matching smallest valid pairs eliminates backtracking.
4. Key takeaway: once a small cookie can satisfy the current smallest greed, saving larger cookies is always at least as good.

---

### Example 2: Lemonade Change (Easy)

**Problem:** Customers pay with 5, 10, 20 in order. Each lemonade costs 5. Return whether you can always give correct change.

**Greedy rule:** For a 20 bill, prefer giving `10 + 5` (instead of three 5s) to preserve more 5s for future 10-bill changes.

```python
def lemonade_change(bills):
	five = ten = 0

	for bill in bills:
		if bill == 5:
			five += 1
		elif bill == 10:
			if five == 0:
				return False
			five -= 1
			ten += 1
		else:  # bill == 20
			if ten > 0 and five > 0:
				ten -= 1
				five -= 1
			elif five >= 3:
				five -= 3
			else:
				return False

	return True

print(lemonade_change([5, 5, 5, 10, 20]))          # True
print(lemonade_change([5, 5, 10, 10, 20]))         # False
print(lemonade_change([5, 5, 5, 5, 20, 20, 20]))   # False
```

**Complexity:** Time `O(n)`, Space `O(1)`

**Brute Force vs Greedy:**

1. Brute force idea: at each `$20` payment, try all valid ways to make change (`10+5` or `5+5+5`) recursively.
2. Why brute force is expensive: each branching decision doubles states in long sequences.
3. Why greedy compresses it: always prioritize `10+5`, which preserves more `$5` bills for future `$10` payments.
4. Key takeaway: not all valid change choices are equally future-safe; greedy chooses the most flexible inventory state.

---

### Example 3: Jump Game (Medium)

**Problem:** `nums[i]` is max jump length from `i`. Can you reach last index?

**Greedy rule:** Track farthest index reachable so far. If current index exceeds farthest, you're stuck.

```python
def can_jump(nums):
	farthest = 0

	for i, jump in enumerate(nums):
		if i > farthest:
			return False
		farthest = max(farthest, i + jump)

	return True

print(can_jump([2, 3, 1, 1, 4]))  # True
print(can_jump([3, 2, 1, 0, 4]))  # False
print(can_jump([0]))              # True
```

**Complexity:** Time `O(n)`, Space `O(1)`

**Brute Force vs Greedy:**

1. Brute force idea: DFS from index `i` to every reachable index `i+1..i+nums[i]`.
2. Why brute force is expensive: many repeated reachability branches create exponential behavior.
3. Why greedy compresses it: the only thing that matters at step `i` is global farthest reachable index so far.
4. Key takeaway: for reachability (yes/no), you do not need exact path history, only frontier coverage.

---

### Example 4: Jump Game II (Medium)

**Problem:** Minimum jumps to reach the last index.

**Greedy idea:** Treat reachable range as a layer. While scanning current layer, compute next layer's farthest reach. When layer ends, make one jump.

```python
def jump_game_ii(nums):
	jumps = 0
	current_end = 0
	farthest = 0

	for i in range(len(nums) - 1):
		farthest = max(farthest, i + nums[i])
		if i == current_end:
			jumps += 1
			current_end = farthest

	return jumps

print(jump_game_ii([2, 3, 1, 1, 4]))  # 2
print(jump_game_ii([2, 3, 0, 1, 4]))  # 2
print(jump_game_ii([1, 1, 1, 1]))     # 3
```

**Complexity:** Time `O(n)`, Space `O(1)`

**Brute Force vs Greedy:**

1. Brute force idea: recursively try every jump length from each index and take minimum depth.
2. Why brute force is expensive: explores many overlapping paths to the same indices.
3. Why greedy compresses it: process indices in layers and jump exactly when current layer ends.
4. Key takeaway: this is BFS-level counting without an explicit queue; frontier boundaries give minimum jumps.

---

### Example 5: Non-Overlapping Intervals (Medium)

**Problem:** Remove minimum intervals so remaining intervals do not overlap.

**Greedy rule:** Sort by end time. Keep the interval that ends earliest; remove overlaps.

```python
def erase_overlap_intervals(intervals):
	intervals.sort(key=lambda x: x[1])

	removed = 0
	prev_end = intervals[0][1]

	for start, end in intervals[1:]:
		if start < prev_end:
			removed += 1
		else:
			prev_end = end

	return removed

print(erase_overlap_intervals([[1, 2], [2, 3], [3, 4], [1, 3]]))  # 1
print(erase_overlap_intervals([[1, 2], [1, 2], [1, 2]]))          # 2
print(erase_overlap_intervals([[1, 2], [2, 3]]))                  # 0
```

**Complexity:** Time `O(n log n)`, Space `O(1)` extra

**Brute Force vs Greedy:**

1. Brute force idea: try all subsets of intervals, keep the largest non-overlapping subset.
2. Why brute force is expensive: subset enumeration is `2^n`.
3. Why greedy compresses it: sort by end time, keep earliest-finishing compatible interval each time.
4. Key takeaway: finishing earlier leaves maximum room for future intervals, so this local choice is globally safe.

---

### Example 6: Minimum Number of Arrows to Burst Balloons (Medium)

**Problem:** Each balloon is an interval `[start, end]`. One arrow at position `x` bursts all balloons with `start <= x <= end`. Min arrows needed.

**Greedy rule:** Sort by end and shoot arrow at current end whenever next balloon starts after it.

```python
def find_min_arrow_shots(points):
	points.sort(key=lambda x: x[1])

	arrows = 1
	arrow_pos = points[0][1]

	for start, end in points[1:]:
		if start > arrow_pos:
			arrows += 1
			arrow_pos = end

	return arrows

print(find_min_arrow_shots([[10,16], [2,8], [1,6], [7,12]]))  # 2
print(find_min_arrow_shots([[1,2], [3,4], [5,6], [7,8]]))     # 4
print(find_min_arrow_shots([[1,2], [2,3], [3,4], [4,5]]))     # 2
```

**Complexity:** Time `O(n log n)`, Space `O(1)` extra

---

### Example 7: Gas Station (Medium)

**Problem:** Circular route, `gas[i]` fuel at station `i`, `cost[i]` to go to next. Return starting index if possible, else `-1`.

**Greedy insight:**

- If total gas < total cost, impossible.
- If running tank becomes negative at `i`, any start in that segment fails; next start is `i + 1`.

```python
def can_complete_circuit(gas, cost):
	if sum(gas) < sum(cost):
		return -1

	start = 0
	tank = 0

	for i in range(len(gas)):
		tank += gas[i] - cost[i]
		if tank < 0:
			start = i + 1
			tank = 0

	return start

print(can_complete_circuit([1,2,3,4,5], [3,4,5,1,2]))  # 3
print(can_complete_circuit([2,3,4], [3,4,3]))          # -1
print(can_complete_circuit([5], [4]))                  # 0
```

**Complexity:** Time `O(n)`, Space `O(1)`

---

### Example 8: Task Scheduler (Medium)

**Problem:** Tasks are letters. Same task needs cooldown `n` units before repeating. Minimum total time.

**Greedy counting formula:**

- Let `max_freq` = highest task frequency
- Let `max_count` = number of tasks with frequency `max_freq`
- Minimum slots needed by frame logic:

$$
(max\_freq - 1) \cdot (n + 1) + max\_count
$$

Answer is max of that and total tasks.

```python
from collections import Counter


def least_interval(tasks, n):
	freq = Counter(tasks)
	max_freq = max(freq.values())
	max_count = sum(1 for v in freq.values() if v == max_freq)

	frame = (max_freq - 1) * (n + 1) + max_count
	return max(frame, len(tasks))


print(least_interval(["A","A","A","B","B","B"], 2))  # 8
print(least_interval(["A","A","A","B","B","B"], 0))  # 6
print(least_interval(["A","A","A","A","B","C","D"], 2))  # 10
```

**Complexity:** Time `O(k)` where `k = len(tasks)`, Space `O(1)` for fixed alphabet (or `O(U)` unique tasks)

---

### Example 9: Candy (Hard)

**Problem:** Each child has rating. Give at least one candy each. Higher-rated child than neighbor must get more candies. Min total candies.

**Greedy strategy:** Two passes.

1. Left-to-right to satisfy left neighbor rule.
2. Right-to-left to satisfy right neighbor rule.

```python
def candy(ratings):
	n = len(ratings)
	candies = [1] * n

	for i in range(1, n):
		if ratings[i] > ratings[i - 1]:
			candies[i] = candies[i - 1] + 1

	for i in range(n - 2, -1, -1):
		if ratings[i] > ratings[i + 1]:
			candies[i] = max(candies[i], candies[i + 1] + 1)

	return sum(candies)

print(candy([1, 0, 2]))        # 5  -> [2,1,2]
print(candy([1, 2, 2]))        # 4  -> [1,2,1]
print(candy([1, 3, 4, 5, 2]))  # 11 -> [1,2,3,4,1]
```

**Complexity:** Time `O(n)`, Space `O(n)`

---

### Example 10: Minimum Number of Refueling Stops (Hard)

**Problem:** Start with `startFuel`, target distance. Stations are `[position, fuel]`. Minimum stops to reach target.

**Greedy + heap idea:**

- Move forward as far as possible.
- Add all reachable station fuels to max-heap.
- Refuel only when needed, taking largest fuel seen so far.

This is greedy because when forced to refuel, choosing largest available fuel gives maximal future reach.

```python
import heapq


def min_refuel_stops(target, start_fuel, stations):
	max_heap = []
	fuel = start_fuel
	i = 0
	stops = 0

	while fuel < target:
		while i < len(stations) and stations[i][0] <= fuel:
			heapq.heappush(max_heap, -stations[i][1])
			i += 1

		if not max_heap:
			return -1

		fuel += -heapq.heappop(max_heap)
		stops += 1

	return stops


print(min_refuel_stops(1, 1, []))  # 0
print(min_refuel_stops(100, 10, [[10,60],[20,30],[30,30],[60,40]]))  # 2
print(min_refuel_stops(100, 1, [[10,100]]))  # -1
```

**Complexity:** Time `O(n log n)`, Space `O(n)`

---

## Pattern-to-Problem Mapping

| Pattern | Recognition Clue | Typical Move |
|---|---|---|
| Sort + choose earliest finish | interval overlap / max non-overlap | sort by end time, pick if compatible |
| Running frontier | reachability / min jumps | track farthest or current layer end |
| Local feasibility accounting | bills/resources in sequence | maintain counts, prefer more flexible change |
| Two-pass correction | constraints from both sides | left pass + right pass with max merge |
| Deferred best-choice with heap | choose best among seen options later | push candidates, pop max when forced |

---

## Greedy vs DP: Quick Decision Rule

Use greedy first when:

1. You can describe one local rule with a clear safety argument.
2. The algorithm naturally needs only current summary state.

Use DP instead when:

1. Multiple future-dependent choices compete and local choices can backfire.
2. State history matters in many dimensions.

---

## Practice Set (Simple to Complex)

### Foundation

1. Assign Cookies
2. Lemonade Change
3. Best Time to Buy and Sell Stock II

### Core Medium

1. Jump Game
2. Jump Game II
3. Gas Station
4. Non-overlapping Intervals
5. Minimum Number of Arrows to Burst Balloons
6. Partition Labels

### Advanced Greedy

1. Task Scheduler
2. Candy
3. Queue Reconstruction by Height
4. Minimum Number of Refueling Stops
5. Course Schedule III

---

## Final Checklist Before You Submit a Greedy Solution

1. State your greedy rule in one sentence.
2. Explain briefly why that choice is safe.
3. Validate on edge cases:
   - empty/single element
   - all equal
   - strictly increasing/decreasing
   - impossible case
4. Confirm time complexity (often `O(n)` or `O(n log n)`).
