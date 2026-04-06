# Merge Intervals

**Difficulty:** Medium
**Pattern:** Intervals — Sort and Merge
**LeetCode:** #56

## Problem Statement
Given an array of `intervals` where `intervals[i] = [starti, endi]`, merge all overlapping intervals and return an array of the non-overlapping intervals that cover all the intervals in the input.

## Examples

### Example 1
**Input:** `intervals = [[1,3],[2,6],[8,10],[15,18]]`
**Output:** `[[1,6],[8,10],[15,18]]`
**Explanation:** [1,3] and [2,6] overlap → merged to [1,6].

### Example 2
**Input:** `intervals = [[1,4],[4,5]]`
**Output:** `[[1,5]]`
**Explanation:** [1,4] and [4,5] are considered overlapping.

## Constraints
- `1 <= intervals.length <= 10⁴`
- `intervals[i].length == 2`
- `0 <= starti <= endi <= 10⁴`

## Hints

> 💡 **Hint 1:** Sort intervals by start time. Then two adjacent intervals overlap if `intervals[i].start <= result.last.end`.

> 💡 **Hint 2:** Maintain a result list. For each interval, if it overlaps with the last result interval, extend the end. Otherwise, add it as a new interval.

> 💡 **Hint 3:** The merge condition is `current.start <= last.end`. The merged end is `max(last.end, current.end)`.

## Approach
**Time Complexity:** O(N log N) for sorting
**Space Complexity:** O(N) for output

Sort by start, then linearly scan — extend the last interval's end if overlap, otherwise append new interval.
