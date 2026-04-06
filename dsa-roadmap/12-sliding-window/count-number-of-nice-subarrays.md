# Count Number of Nice Subarrays

**Difficulty:** Medium
**Pattern:** Sliding Window / Prefix Sum
**LeetCode:** #1248

## Problem Statement

Given an array of integers `nums` and an integer `k`, return the number of nice subarrays. A nice subarray is a subarray that contains exactly `k` odd numbers.

## Examples

### Example 1
**Input:** `nums = [1, 1, 2, 1, 1]`, `k = 3`
**Output:** `2`
**Explanation:** [1,1,2,1] and [1,2,1,1] each contain exactly 3 odd numbers.

### Example 2
**Input:** `nums = [2, 4, 6]`, `k = 1`
**Output:** `0`

### Example 3
**Input:** `nums = [2, 2, 2, 1, 2, 2, 1, 2, 2, 2]`, `k = 2`
**Output:** `16`

## Constraints
- `1 <= nums.length <= 50000`
- `1 <= nums[i] <= 10^5`
- `1 <= k <= nums.length`

## Hints

> 💡 **Hint 1:** Use the "at most k" trick: count(exactly k) = count(at most k) - count(at most k-1).

> 💡 **Hint 2:** For "at most k odd numbers", use a variable sliding window. Track the count of odd numbers. Shrink when count > k.

> 💡 **Hint 3:** Alternatively, replace each number with 1 (odd) or 0 (even) and use prefix sum + HashMap to count subarrays with sum exactly k (same as "Subarray Sum Equals K").

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1) with sliding window, O(n) with prefix sum

Either the "at most k" sliding window trick or prefix sum with HashMap. Both give O(n).
