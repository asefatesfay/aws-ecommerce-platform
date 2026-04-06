# Course Schedule II

**Difficulty:** Medium
**Pattern:** Topological Sort (BFS/DFS)
**LeetCode:** #210

## Problem Statement
There are `numCourses` courses labeled 0 to n-1. `prerequisites[i] = [a, b]` means you must take course b before a. Return the ordering of courses to finish all, or an empty array if impossible (cycle exists).

## Examples

### Example 1
**Input:** `numCourses = 2`, `prerequisites = [[1,0]]`
**Output:** `[0,1]`

### Example 2
**Input:** `numCourses = 4`, `prerequisites = [[1,0],[2,0],[3,1],[3,2]]`
**Output:** `[0,2,1,3]` or `[0,1,2,3]`

### Example 3
**Input:** `numCourses = 2`, `prerequisites = [[1,0],[0,1]]`
**Output:** `[]` (cycle)

## Constraints
- `1 <= numCourses <= 2000`
- `0 <= prerequisites.length <= numCourses × (numCourses - 1)`

## Hints

> 💡 **Hint 1:** Build an adjacency list and compute in-degrees for each node.

> 💡 **Hint 2:** Kahn's algorithm (BFS): start with all nodes with in-degree 0. Process each, decrement neighbors' in-degrees. Add neighbors with in-degree 0 to queue.

> 💡 **Hint 3:** If the result contains all courses, return it. Otherwise a cycle exists — return [].

## Approach
**Time Complexity:** O(V + E)
**Space Complexity:** O(V + E)

Kahn's topological sort: BFS from zero-in-degree nodes. If all nodes are processed, return the order; otherwise a cycle exists.
