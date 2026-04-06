# Median of Two Sorted Arrays

**Difficulty:** Hard
**Pattern:** Binary Search
**LeetCode:** #4

## Problem Statement

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

## Examples

### Example 1
**Input:** `nums1 = [1,3]`, `nums2 = [2]`
**Output:** `2.00000`
**Explanation:** Merged array = [1,2,3], median = 2.

### Example 2
**Input:** `nums1 = [1,2]`, `nums2 = [3,4]`
**Output:** `2.50000`
**Explanation:** Merged array = [1,2,3,4], median = (2+3)/2 = 2.5.

## Constraints
- `nums1.length == m`, `nums2.length == n`
- `0 <= m <= 1000`, `0 <= n <= 1000`
- `1 <= m + n <= 2000`
- `-10^6 <= nums1[i], nums2[i] <= 10^6`

## Hints

> 💡 **Hint 1:** Binary search on the partition point of the smaller array. The partition divides both arrays such that the left halves together have (m+n+1)/2 elements.

> 💡 **Hint 2:** For a partition at index i in nums1 and j in nums2: the partition is valid if nums1[i-1] ≤ nums2[j] and nums2[j-1] ≤ nums1[i].

> 💡 **Hint 3:** If nums1[i-1] > nums2[j], move i left. If nums2[j-1] > nums1[i], move i right. When valid, the median is computed from the boundary elements.

## Approach

**Time Complexity:** O(log(min(m,n)))
**Space Complexity:** O(1)

Binary search on the partition of the smaller array. Find the correct split where left halves of both arrays together form the lower half of the merged array.
