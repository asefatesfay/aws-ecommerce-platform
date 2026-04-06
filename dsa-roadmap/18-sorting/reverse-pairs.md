# Reverse Pairs

**Difficulty:** Hard
**Pattern:** Merge Sort / BIT
**LeetCode:** #493

## Problem Statement

Given an integer array `nums`, return the number of reverse pairs in the array. A reverse pair is a pair `(i, j)` where `0 <= i < j < nums.length` and `nums[i] > 2 * nums[j]`.

## Examples

### Example 1
**Input:** `nums = [1,3,2,3,1]`
**Output:** `2`
**Explanation:** (1,4): 3 > 2*1=2. (3,4): 3 > 2*1=2.

### Example 2
**Input:** `nums = [2,4,3,5,1]`
**Output:** `3`

## Constraints
- `1 <= nums.length <= 5 * 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`

## Hints

> 💡 **Hint 1:** Use a modified merge sort. During the merge step, count reverse pairs across the two halves.

> 💡 **Hint 2:** Before merging, for each element in the right half, count how many elements in the left half are > 2 * right_element. Use two pointers since both halves are sorted.

> 💡 **Hint 3:** After counting, perform the standard merge. The total count accumulates across all merge steps.

## Approach

**Time Complexity:** O(n log n)
**Space Complexity:** O(n)

Modified merge sort: count cross-half reverse pairs during each merge step using two pointers on the sorted halves.
