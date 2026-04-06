# Last Stone Weight

**Difficulty:** Easy
**Pattern:** Max Heap
**LeetCode:** #1046

## Problem Statement
You have an array of stones where `stones[i]` is the weight of the i-th stone. Each turn, pick the two heaviest stones and smash them. If equal, both are destroyed. If not, the smaller is destroyed and the larger becomes `larger - smaller`. Return the weight of the last remaining stone, or 0 if none remain.

## Examples

### Example 1
**Input:** `stones = [2,7,4,1,8,1]`
**Output:** `1`
**Explanation:** 8,7 → 1; 4,2 → 2; 2,1 → 1; 1,1 → 0; last stone = 1.

### Example 2
**Input:** `stones = [1]`
**Output:** `1`

## Constraints
- `1 <= stones.length <= 30`
- `1 <= stones[i] <= 1000`

## Hints

> 💡 **Hint 1:** You always need the two largest elements — a max-heap is perfect for this.

> 💡 **Hint 2:** Python's `heapq` is a min-heap, so negate all values to simulate a max-heap.

> 💡 **Hint 3:** Loop: pop two elements, if different push back the difference (negated). Stop when heap has ≤ 1 element.

## Approach
**Time Complexity:** O(N log N)
**Space Complexity:** O(N)

Use a max-heap. Each iteration pop the two largest, push back the difference if non-zero. Return the last element or 0.
