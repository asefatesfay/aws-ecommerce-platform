# Max Value of Equation

**Difficulty:** Hard
**Pattern:** Monotonic Deque
**LeetCode:** #1499

## Problem Statement

You are given an array `points` containing the coordinates of points on a 2D plane, sorted by the x-values, where `points[i] = [xi, yi]` such that `xi < xj` for all `1 <= i < j <= points.length`. You are also given an integer `k`. Return the maximum value of the equation `yi + yj + |xi - xj|` where `|xi - xj| <= k` and `1 <= i < j <= points.length`. It is guaranteed that there exists at least one pair of points that satisfy the constraint `|xi - xj| <= k`.

## Examples

### Example 1
**Input:** `points = [[1,3],[2,0],[5,10],[6,-10]]`, `k = 1`
**Output:** `4`
**Explanation:** (1,3) and (2,0): 3+0+|1-2|=4.

### Example 2
**Input:** `points = [[0,0],[3,0],[9,2]]`, `k = 3`
**Output:** `3`

## Constraints
- `2 <= points.length <= 10^5`
- `points[i].length == 2`
- `-10^8 <= xi, yi <= 10^8`
- `0 <= k <= 2 * 10^8`
- `xi < xj` for all `1 <= i < j <= points.length`

## Hints

> 💡 **Hint 1:** Since xi < xj, |xi - xj| = xj - xi. The equation becomes yi + yj + xj - xi = (yj + xj) + (yi - xi).

> 💡 **Hint 2:** For each j, maximize (yi - xi) over all valid i where xj - xi ≤ k. Use a monotonic decreasing deque of (yi - xi, xi) pairs.

> 💡 **Hint 3:** Remove from the front when xi < xj - k (out of range). The front gives the maximum (yi - xi). Add (yj - xj, xj) to the deque (maintaining decreasing order).

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(n)

Monotonic decreasing deque of (y-x) values. For each point j, query the max (y-x) within the k-window, then add the current point.
