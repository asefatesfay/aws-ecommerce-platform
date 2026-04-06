# Minimum Number of Refueling Stops

**Difficulty:** Hard
**Pattern:** Greedy + Max Heap
**LeetCode:** #871

## Problem Statement
A car starts at position 0 with `startFuel`. There are stations at positions with fuel amounts. Return the minimum number of refueling stops to reach `target`, or -1 if impossible.

## Examples

### Example 1
**Input:** `target = 100`, `startFuel = 10`, `stations = [[10,60],[20,30],[30,30],[60,40]]`
**Output:** `2`

### Example 2
**Input:** `target = 1`, `startFuel = 1`, `stations = []`
**Output:** `0`

## Constraints
- `1 <= target, startFuel <= 10⁹`
- `0 <= stations.length <= 500`

## Hints

> 💡 **Hint 1:** Use a max-heap to store fuel amounts of stations you've passed but not yet used.

> 💡 **Hint 2:** Drive as far as possible. When you run out of fuel, greedily refuel from the largest available station (top of max-heap).

> 💡 **Hint 3:** Each time you refuel from the heap, increment the stop count. If the heap is empty and you still can't reach the target, return -1.

## Approach
**Time Complexity:** O(N log N)
**Space Complexity:** O(N)

Greedy with max-heap: collect all reachable stations' fuel, then greedily use the largest fuel amounts when needed.
