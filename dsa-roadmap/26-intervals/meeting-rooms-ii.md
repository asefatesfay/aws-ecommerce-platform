# Meeting Rooms II

**Difficulty:** Medium
**Pattern:** Intervals — Min Heap / Sweep Line
**LeetCode:** #253

## Problem Statement
Given an array of meeting time intervals `intervals[i] = [starti, endi]`, return the minimum number of conference rooms required.

## Examples

### Example 1
**Input:** `intervals = [[0,30],[5,10],[15,20]]`
**Output:** `2`

### Example 2
**Input:** `intervals = [[7,10],[2,4]]`
**Output:** `1`

## Constraints
- `1 <= intervals.length <= 10⁴`
- `0 <= starti < endi <= 10⁶`

## Hints

> 💡 **Hint 1:** Sort by start time. Use a min-heap to track end times of ongoing meetings.

> 💡 **Hint 2:** For each meeting, if the earliest-ending meeting has already ended (heap top ≤ current start), reuse that room (pop and push new end). Otherwise, open a new room (just push).

> 💡 **Hint 3:** The heap size at any point = number of rooms currently in use. The answer is the maximum heap size reached.

## Approach
**Time Complexity:** O(N log N)
**Space Complexity:** O(N)

Sort by start, use a min-heap of end times. For each meeting, free rooms that ended before it starts, then add the new meeting's end time.
