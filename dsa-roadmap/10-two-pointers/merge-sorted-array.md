# Merge Sorted Array

**Difficulty:** Easy
**Pattern:** Two Pointers (Merge from Back)
**LeetCode:** #88

## Problem Statement

You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively. Merge `nums2` into `nums1` as one sorted array in-place. `nums1` has a length of `m + n`, with the last `n` elements set to 0 as placeholders.

## Examples

### Example 1
**Input:** `nums1 = [1,2,3,0,0,0]`, `m = 3`, `nums2 = [2,5,6]`, `n = 3`
**Output:** `[1,2,2,3,5,6]`

### Example 2
**Input:** `nums1 = [1]`, `m = 1`, `nums2 = []`, `n = 0`
**Output:** `[1]`

## Constraints
- `nums1.length == m + n`
- `nums2.length == n`
- `0 <= m, n <= 200`
- `-10^9 <= nums1[i], nums2[j] <= 10^9`

## Hints

> 💡 **Hint 1:** Merging from the front would require shifting elements. Merging from the back avoids this — the back of nums1 is empty space.

> 💡 **Hint 2:** Use three pointers: p1 at index m-1 (last real element of nums1), p2 at index n-1 (last element of nums2), and p at index m+n-1 (write position).

> 💡 **Hint 3:** Compare nums1[p1] and nums2[p2]. Place the larger at position p and advance the corresponding pointer and p. Continue until p2 < 0 (remaining nums1 elements are already in place).

## Approach

**Time Complexity:** O(m + n)
**Space Complexity:** O(1)

Merge from the back: compare the largest unplaced elements from each array and place the larger one at the end of nums1. Work backward until nums2 is exhausted.
