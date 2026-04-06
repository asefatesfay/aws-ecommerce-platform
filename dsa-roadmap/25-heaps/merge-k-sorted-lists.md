# Merge k Sorted Lists

**Difficulty:** Hard
**Pattern:** K-Way Merge (Heap)
**LeetCode:** #23

## Problem Statement
Given an array of `k` linked lists, each sorted in ascending order, merge all the lists into one sorted linked list and return it.

## Examples

### Example 1
**Input:** `lists = [[1,4,5],[1,3,4],[2,6]]`
**Output:** `[1,1,2,3,4,4,5,6]`

### Example 2
**Input:** `lists = []`
**Output:** `[]`

## Constraints
- `k == lists.length`, `0 <= k <= 10⁴`
- `0 <= lists[i].length <= 500`
- `-10⁴ <= lists[i][j] <= 10⁴`

## Hints

> 💡 **Hint 1:** Use a min-heap of size k. Initialize it with the head node of each non-empty list.

> 💡 **Hint 2:** Each heap entry should store `(node.val, index, node)` — the value for comparison, a tiebreaker index, and the node itself.

> 💡 **Hint 3:** Pop the minimum, add it to the result, then push that node's `next` into the heap (if it exists). Repeat until the heap is empty.

## Approach
**Time Complexity:** O(N log k) where N = total nodes, k = number of lists
**Space Complexity:** O(k) for the heap

Min-heap of size k — always extract the global minimum and advance that list's pointer.
