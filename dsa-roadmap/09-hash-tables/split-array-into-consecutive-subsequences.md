# Split Array into Consecutive Subsequences

**Difficulty:** Medium
**Pattern:** Hash Map / Greedy
**LeetCode:** #659

## Problem Statement

You are given an integer array `nums` that is sorted in non-decreasing order. Determine if it is possible to split `nums` into one or more subsequences such that both of the following conditions are true:
- Each subsequence is a consecutive increasing sequence (i.e., each integer is exactly 1 more than the previous integer).
- All subsequences have a length of 3 or more.

## Examples

### Example 1
**Input:** `nums = [1, 2, 3, 3, 4, 5]`
**Output:** `true`
**Explanation:** [1,2,3] and [3,4,5].

### Example 2
**Input:** `nums = [1, 2, 3, 3, 4, 4, 5, 5]`
**Output:** `true`
**Explanation:** [1,2,3,4,5] and [3,4,5].

### Example 3
**Input:** `nums = [1, 2, 3, 4, 4, 5]`
**Output:** `false`

## Constraints
- `1 <= nums.length <= 10^4`
- `-1000 <= nums[i] <= 1000`
- `nums` is sorted in non-decreasing order

## Hints

> 💡 **Hint 1:** Use two HashMaps: `freq` (remaining count of each number) and `tail` (count of subsequences ending at each number).

> 💡 **Hint 2:** For each number n: first try to append it to an existing subsequence ending at n-1 (decrement tail[n-1], increment tail[n]). If no such subsequence exists, try to start a new one using n, n+1, n+2 (requires freq[n+1] > 0 and freq[n+2] > 0).

> 💡 **Hint 3:** If neither option is possible for some number, return false. Process numbers in order.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(n)

Greedy with two maps: prefer extending existing subsequences over starting new ones. For each number, extend an existing tail if possible; otherwise start a new length-3 subsequence.
