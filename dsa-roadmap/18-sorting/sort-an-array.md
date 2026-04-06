# Sort an Array

**Difficulty:** Medium
**Pattern:** Sorting Algorithm Implementation
**LeetCode:** #912

## Problem Statement

Given an array of integers `nums`, sort the array in ascending order and return it. You must solve the problem without using any built-in functions in O(n log n) time complexity and with the smallest space complexity possible.

## Examples

### Example 1
**Input:** `nums = [5,2,3,1]`
**Output:** `[1,2,3,5]`

### Example 2
**Input:** `nums = [5,1,1,2,0,0]`
**Output:** `[0,0,1,1,2,5]`

## Constraints
- `1 <= nums.length <= 5 * 10^4`
- `-5 * 10^4 <= nums[i] <= 5 * 10^4`

## Hints

> 💡 **Hint 1:** Implement merge sort or heap sort for guaranteed O(n log n).

> 💡 **Hint 2:** Merge sort: divide in half, sort each half, merge. Heap sort: build a max-heap, then extract elements.

> 💡 **Hint 3:** Randomized quicksort also works in practice (O(n log n) expected) but has O(n²) worst case.

## Approach

**Time Complexity:** O(n log n)
**Space Complexity:** O(n) merge sort, O(1) heap sort

Implement merge sort (stable, O(n) space) or heap sort (in-place, O(1) space). Both guarantee O(n log n).
