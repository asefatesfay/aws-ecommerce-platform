# Non-overlapping Intervals

**Difficulty:** Medium
**Pattern:** Greedy Intervals
**LeetCode:** #435

## Problem Statement
Given an array of intervals, return the minimum number of intervals you need to remove to make the rest non-overlapping.

## Examples

### Example 1
**Input:** `intervals = [[1,2],[2,3],[3,4],[1,3]]`
**Output:** `1`
**Explanation:** Remove [1,3] and the rest are non-overlapping.

### Example 2
**Input:** `intervals = [[1,2],[1,2],[1,2]]`
**Output:** `2`

## Constraints
- `1 <= intervals.length <= 10⁵`
- `-5×10⁴ <= starti < endi <= 5×10⁴`

## Hints

> 💡 **Hint 1:** This is equivalent to finding the maximum number of non-overlapping intervals (then answer = total - max_non_overlapping).

> 💡 **Hint 2:** Sort by end time. Greedily keep intervals that end earliest — they leave the most room for future intervals.

> 💡 **Hint 3:** Track the end time of the last kept interval. If the next interval starts before that end, skip it (remove it). Otherwise, keep it and update the end time.

## Approach
**Time Complexity:** O(N log N)
**Space Complexity:** O(1)

Sort by end time. Greedily select intervals that don't overlap with the previously selected one. Count removals = total - selected.
