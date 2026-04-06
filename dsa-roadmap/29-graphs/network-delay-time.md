# Network Delay Time

**Difficulty:** Medium
**Pattern:** Dijkstra's Shortest Path
**LeetCode:** #743

## Problem Statement
Given a network of `n` nodes and directed weighted edges `times[i] = [ui, vi, wi]`, find the time for all nodes to receive a signal sent from node `k`. Return -1 if not all nodes can be reached.

## Examples

### Example 1
**Input:** `times = [[2,1,1],[2,3,1],[3,4,1]]`, `n = 4`, `k = 2`
**Output:** `2`

### Example 2
**Input:** `times = [[1,2,1]]`, `n = 2`, `k = 2`
**Output:** `-1`

## Constraints
- `1 <= k <= n <= 100`
- `1 <= times.length <= 6000`
- `0 <= wi <= 100`

## Hints

> 💡 **Hint 1:** This is a single-source shortest path problem. Use Dijkstra's algorithm from node k.

> 💡 **Hint 2:** Use a min-heap of `(distance, node)`. Start with `(0, k)`. Relax edges greedily.

> 💡 **Hint 3:** The answer is the maximum shortest distance among all nodes. If any node is unreachable (distance = infinity), return -1.

## Approach
**Time Complexity:** O((V + E) log V)
**Space Complexity:** O(V + E)

Dijkstra from node k. Track shortest distances to all nodes. Return max distance if all reachable, else -1.
