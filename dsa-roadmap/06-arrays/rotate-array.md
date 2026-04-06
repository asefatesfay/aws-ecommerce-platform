# Rotate Array

**Difficulty:** Medium
**Pattern:** Array Manipulation / Reversal
**LeetCode:** #189

## Problem Statement

Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative. Do it in-place with O(1) extra space.

## Examples

### Example 1
**Input:** `nums = [1, 2, 3, 4, 5, 6, 7]`, `k = 3`
**Output:** `[5, 6, 7, 1, 2, 3, 4]`
**Explanation:** Rotate right by 1: [7,1,2,3,4,5,6]. By 2: [6,7,1,2,3,4,5]. By 3: [5,6,7,1,2,3,4].

### Example 2
**Input:** `nums = [-1, -100, 3, 99]`, `k = 2`
**Output:** `[3, 99, -1, -100]`

## Constraints
- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `0 <= k <= 10^5`

## Hints

> 💡 **Hint 1:** First, handle the case where k ≥ n by taking k = k % n. Rotating by n is the same as not rotating.

> 💡 **Hint 2:** There's an elegant O(1) space solution using three reversals. Think about what happens when you reverse the entire array, then reverse parts of it.

> 💡 **Hint 3:** Reverse the entire array, then reverse the first k elements, then reverse the remaining n-k elements. This achieves the rotation in three O(n) passes with O(1) space.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Use the three-reversal trick: reverse the entire array, then reverse the first k elements, then reverse the last n-k elements. The key insight is that reversing the whole array and then reversing the two halves separately achieves the rotation.
