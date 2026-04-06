# Find the Most Competitive Subsequence

**Difficulty:** Medium
**Pattern:** Monotonic Stack/Queue / Greedy
**LeetCode:** #1673

## Problem Statement

Given an integer array `nums` and a positive integer `k`, return the most competitive subsequence of `nums` of size `k`. An array's subsequence is a resulting sequence obtained by erasing some (possibly zero) elements of the array. We define that a subsequence `a` is more competitive than a subsequence `b` (of the same length) if in the first position where `a` and `b` differ, subsequence `a` has a number less than the corresponding number in `b`. In other words, the most competitive subsequence is the lexicographically smallest one.

## Examples

### Example 1
**Input:** `nums = [3,5,2,6]`, `k = 2`
**Output:** `[2,6]`

### Example 2
**Input:** `nums = [2,4,3,3,5,4,9,6]`, `k = 4`
**Output:** `[2,3,3,4]`

## Constraints
- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^9`
- `1 <= k <= nums.length`

## Hints

> 💡 **Hint 1:** Use a monotonic increasing stack. You want the lexicographically smallest subsequence of length k.

> 💡 **Hint 2:** For each element, pop from the stack if the top is larger than the current element AND there are enough remaining elements to fill k positions.

> 💡 **Hint 3:** The condition to pop: `stack.size() + remaining_elements > k` (we can afford to remove the top). Push the current element if stack size < k.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(k)

Monotonic increasing stack with size limit k. Greedily pop larger elements when we can still fill k positions.
