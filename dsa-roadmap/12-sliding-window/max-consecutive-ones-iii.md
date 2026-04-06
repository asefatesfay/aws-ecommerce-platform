# Max Consecutive Ones III

**Difficulty:** Medium
**Pattern:** Sliding Window (Variable)
**LeetCode:** #1004

## Problem Statement

Given a binary array `nums` and an integer `k`, return the maximum number of consecutive `1`s in the array if you can flip at most `k` `0`s.

## Examples

### Example 1
**Input:** `nums = [1,1,1,0,0,0,1,1,1,1,0]`, `k = 2`
**Output:** `6`
**Explanation:** Flip the two 0s at indices 3 and 4 (or 4 and 10) to get 6 consecutive 1s.

### Example 2
**Input:** `nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1,0]`, `k = 3`
**Output:** `10`

## Constraints
- `1 <= nums.length <= 10^5`
- `nums[i]` is either `0` or `1`
- `0 <= k <= nums.length`

## Hints

> 💡 **Hint 1:** Rephrase: find the longest subarray with at most k zeros.

> 💡 **Hint 2:** Variable sliding window. Track the count of zeros in the current window. Expand right; when zero count exceeds k, shrink from the left.

> 💡 **Hint 3:** Track the maximum window size seen when zero count ≤ k.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Variable window tracking zero count. Expand right; shrink left when zeros > k. Maximum window size is the answer.
