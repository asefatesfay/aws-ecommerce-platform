# Kth Largest Element in an Array

**Difficulty:** Medium
**Pattern:** Quickselect / Heap
**LeetCode:** #215

## Problem Statement

Given an integer array `nums` and an integer `k`, return the `k`th largest element in the array. Note that it is the `k`th largest element in the sorted order, not the `k`th distinct element. Can you solve it without sorting?

## Examples

### Example 1
**Input:** `nums = [3,2,1,5,6,4]`, `k = 2`
**Output:** `5`

### Example 2
**Input:** `nums = [3,2,3,1,2,4,5,5,6]`, `k = 4`
**Output:** `4`

## Constraints
- `1 <= k <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Hints

> 💡 **Hint 1:** Sorting gives O(n log n). A min-heap of size k gives O(n log k). Quickselect gives O(n) average.

> 💡 **Hint 2:** Quickselect: partition the array around a pivot. If the pivot ends up at position n-k (0-indexed from left), it's the answer. Otherwise, recurse into the appropriate half.

> 💡 **Hint 3:** For the heap approach: maintain a min-heap of size k. For each element, if it's larger than the heap's minimum, replace the minimum. The heap's minimum at the end is the kth largest.

## Approach

**Time Complexity:** O(n) average with quickselect, O(n log k) with heap
**Space Complexity:** O(1) quickselect, O(k) heap

Quickselect: partition-based selection. Only recurse into one side. Average O(n), worst case O(n²) without randomization.
