# Merge Intervals

**Difficulty:** Medium
**Pattern:** Sorting + Greedy Merge
**LeetCode:** #56
**Asked by:** Google, Microsoft, Adobe, Amazon

## Problem Statement

Given an array of intervals where `intervals[i] = [start_i, end_i]`, merge all overlapping intervals and return an array of the non-overlapping intervals that cover all the intervals in the input.

## Examples

### Example 1
**Input:** `intervals = [[1,3],[2,6],[8,10],[15,18]]`
**Output:** `[[1,6],[8,10],[15,18]]`
**Explanation:** `[1,3]` and `[2,6]` overlap → merged to `[1,6]`.

### Example 2
**Input:** `intervals = [[1,4],[4,5]]`
**Output:** `[[1,5]]`
**Explanation:** `[1,4]` and `[4,5]` are considered overlapping (they touch at 4).

### Example 3
**Input:** `intervals = [[1,4],[0,4]]`
**Output:** `[[0,4]]`

## Constraints
- `1 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= start_i <= end_i <= 10^4`

## Hints

> 💡 **Hint 1:** Sort intervals by start time. After sorting, overlapping intervals are always adjacent.

> 💡 **Hint 2:** Two intervals `[a,b]` and `[c,d]` overlap if `c <= b` (the next interval starts before the current one ends). When they overlap, merge to `[a, max(b,d)]`.

> 💡 **Hint 3:** Maintain a `current` interval. For each new interval: if it overlaps with current, extend current's end. Otherwise, push current to result and start a new current.

## Approach 1: Brute Force

**Time Complexity:** O(n² log n)
**Space Complexity:** O(n)

Check every pair of intervals for overlap and merge repeatedly until stable.

```python
def merge_brute(intervals: list[list[int]]) -> list[list[int]]:
    changed = True
    while changed:
        changed = False
        result = []
        used = [False] * len(intervals)
        for i in range(len(intervals)):
            if used[i]:
                continue
            a, b = intervals[i]
            for j in range(i + 1, len(intervals)):
                if used[j]:
                    continue
                c, d = intervals[j]
                if c <= b and a <= d:  # overlap
                    a, b = min(a, c), max(b, d)
                    used[j] = True
                    changed = True
            result.append([a, b])
        intervals = result
    return intervals
```

**Why it's slow:** Multiple passes, O(n²) comparisons per pass.

---

## Approach 2: Sort + Linear Merge — Optimal

**Time Complexity:** O(n log n) — dominated by sort
**Space Complexity:** O(n) — output

After sorting by start time, overlapping intervals are always adjacent. One linear pass merges them.

### Key Insight

```
After sorting by start:
  [1,3], [2,6], [8,10], [15,18]

Two intervals [a,b] and [c,d] overlap when c <= b.
When they overlap, merge to [a, max(b,d)].

Why max(b,d)? One interval might be fully contained:
  [1,10] and [2,5] → merge to [1,10], not [1,5]
```

### Visual Trace

```
intervals = [[1,3],[2,6],[8,10],[15,18]]
After sort: [[1,3],[2,6],[8,10],[15,18]]  (already sorted)

merged = [[1,3]]

[2,6]:   start=2 <= merged[-1][1]=3 → overlap! merged[-1][1] = max(3,6)=6 → [[1,6]]
[8,10]:  start=8 > merged[-1][1]=6 → no overlap. Append → [[1,6],[8,10]]
[15,18]: start=15 > merged[-1][1]=10 → no overlap. Append → [[1,6],[8,10],[15,18]]

Result: [[1,6],[8,10],[15,18]] ✓
```

```python
def merge(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)  # extend
        else:
            merged.append([start, end])               # new interval

    return merged
```

### Complexity Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute force | O(n² log n) | O(n) | Repeated passes |
| Sort + merge | O(n log n) | O(n) | Optimal — sort is the bottleneck |

## Follow-up: Insert Interval — #57 (Google)

Insert a new interval into a sorted, non-overlapping list of intervals and merge if necessary.

```python
def insert(intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
    """
    intervals=[[1,3],[6,9]], new_interval=[2,5] → [[1,5],[6,9]]
    intervals=[[1,2],[3,5],[6,7],[8,10],[12,16]], new_interval=[4,8] → [[1,2],[3,10],[12,16]]
    """
    result = []
    i = 0
    n = len(intervals)

    # Add all intervals that end before new_interval starts
    while i < n and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1

    # Merge all overlapping intervals with new_interval
    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1
    result.append(new_interval)

    # Add remaining intervals
    while i < n:
        result.append(intervals[i])
        i += 1

    return result
```

## Follow-up: Non-Overlapping Intervals — #435 (Microsoft)

Find the minimum number of intervals to remove to make the rest non-overlapping.

```python
def erase_overlap_intervals(intervals: list[list[int]]) -> int:
    """
    [[1,2],[2,3],[3,4],[1,3]] → 1 (remove [1,3])
    [[1,2],[1,2],[1,2]] → 2
    """
    intervals.sort(key=lambda x: x[1])  # sort by END time (greedy)
    count = 0
    prev_end = float('-inf')
    for start, end in intervals:
        if start >= prev_end:
            prev_end = end  # keep this interval
        else:
            count += 1      # remove this interval (it overlaps)
    return count
```

## Typical Interview Use Cases

- Very common at Google/Microsoft/Adobe — appears in almost every interview loop
- Tests sorting + greedy thinking
- Foundation for calendar problems, meeting rooms, interval scheduling
