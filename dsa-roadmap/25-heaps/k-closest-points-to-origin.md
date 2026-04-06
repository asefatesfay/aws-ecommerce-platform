# K Closest Points to Origin

**Difficulty:** Medium
**Pattern:** Top K / Heap
**LeetCode:** #973

## Problem Statement
Given an array of `points` where `points[i] = [xi, yi]`, return the `k` closest points to the origin `(0, 0)`. Distance is Euclidean. The answer may be in any order.

## Examples

### Example 1
**Input:** `points = [[1,3],[-2,2]]`, `k = 1`
**Output:** `[[-2,2]]`
**Explanation:** Distance of [1,3] = √10, distance of [-2,2] = √8. So [-2,2] is closer.

### Example 2
**Input:** `points = [[3,3],[5,-1],[-2,4]]`, `k = 2`
**Output:** `[[3,3],[-2,4]]`

## Constraints
- `1 <= k <= points.length <= 10⁴`
- `-10⁴ <= xi, yi <= 10⁴`

## Hints

> 💡 **Hint 1:** You don't need the actual distance — compare `x² + y²` directly (avoids square root).

> 💡 **Hint 2:** Use a max-heap of size k. Push `(-dist, point)`. When size exceeds k, pop the farthest point.

> 💡 **Hint 3:** Alternatively, use `heapq.nsmallest(k, points, key=lambda p: p[0]**2 + p[1]**2)` directly.

## Approach
**Time Complexity:** O(N log k)
**Space Complexity:** O(k)

Maintain a max-heap of size k storing `(-distance, point)`. The k remaining elements after processing all points are the k closest.
