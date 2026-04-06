# Create Maximum Number

**Difficulty:** Hard
**Pattern:** Monotonic Stack / Greedy
**LeetCode:** #321

## Problem Statement

You are given two integer arrays `nums1` and `nums2` of lengths `m` and `n` respectively. `nums1` and `nums2` represent the digits of two numbers. You are also given an integer `k`. Create the maximum number of length `k <= m + n` from digits of the two numbers. The relative order of the digits from the same array must be preserved. Return an array of the `k` digits representing the answer.

## Examples

### Example 1
**Input:** `nums1 = [3,4,6,5]`, `nums2 = [9,1,2,5,8,3]`, `k = 5`
**Output:** `[9,8,6,5,3]`

### Example 2
**Input:** `nums1 = [6,7]`, `nums2 = [6,0,4]`, `k = 5`
**Output:** `[6,7,6,0,4]`

## Constraints
- `m == nums1.length`, `n == nums2.length`
- `1 <= m, n <= 500`
- `0 <= nums1[i], nums2[i] <= 9`
- `1 <= k <= m + n`

## Hints

> 💡 **Hint 1:** Try all splits: take i digits from nums1 and k-i digits from nums2 (for valid i values). For each split, find the maximum subsequence of each array.

> 💡 **Hint 2:** To find the maximum subsequence of length t from an array, use a monotonic decreasing stack (same as "Remove K Digits" but keeping t elements).

> 💡 **Hint 3:** Merge the two maximum subsequences into the overall maximum using a greedy merge (like merge sort, but when elements are equal, look ahead to break ties).

## Approach

**Time Complexity:** O((m+n)³) in the worst case
**Space Complexity:** O(k)

Try all valid splits. For each split, extract max subsequences using monotonic stack, then merge greedily. Return the best result.
