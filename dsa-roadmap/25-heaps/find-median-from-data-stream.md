# Find Median from Data Stream

**Difficulty:** Hard
**Pattern:** Two Heaps
**LeetCode:** #295

## Problem Statement
Design a data structure that supports adding integers and finding the median of all elements added so far.
- `addNum(num)` — adds an integer to the data structure
- `findMedian()` — returns the median of all elements

## Examples

### Example 1
**Input:** `["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]` `[[],[1],[2],[],[3],[]]`
**Output:** `[null,null,null,1.5,null,2.0]`
**Explanation:** After [1,2] median is 1.5; after [1,2,3] median is 2.0.

### Example 2
**Input:** `addNum(6), addNum(10), addNum(2), findMedian()`
**Output:** `6.0`

## Constraints
- `-10⁵ <= num <= 10⁵`
- At most 5×10⁴ calls to `addNum` and `findMedian`

## Hints

> 💡 **Hint 1:** Maintain two heaps: a max-heap for the lower half and a min-heap for the upper half. The median is always at the tops of these heaps.

> 💡 **Hint 2:** Keep the heaps balanced — their sizes should differ by at most 1. After each insertion, rebalance if needed.

> 💡 **Hint 3:** If both heaps have equal size, median = (max_heap.top + min_heap.top) / 2. If one is larger, median = that heap's top.

## Approach
**Time Complexity:** O(log N) per `addNum`, O(1) for `findMedian`
**Space Complexity:** O(N)

Use a max-heap (lower half) and min-heap (upper half). Always push to max-heap first, then rebalance by moving the max-heap's top to min-heap if needed.
