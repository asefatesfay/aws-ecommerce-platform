# Subarray Sums Divisible by K

**Difficulty:** Medium
**Pattern:** Prefix Sum + Hash Map (Modulo)
**LeetCode:** #974

## Problem Statement

Given an integer array `nums` and an integer `k`, return the number of non-empty subarrays that have a sum divisible by `k`.

## Examples

### Example 1
**Input:** `nums = [4, 5, 0, -2, -3, 1]`, `k = 5`
**Output:** `7`
**Explanation:** All subarrays with sum divisible by 5: [4,5,0,-2,-3,1], [5], [5,0], [5,0,-2,-3], [0], [0,-2,-3], [-2,-3].

### Example 2
**Input:** `nums = [5]`, `k = 9`
**Output:** `0`

## Constraints
- `1 <= nums.length <= 3 * 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `2 <= k <= 10^4`

## Hints

> 💡 **Hint 1:** A subarray sum is divisible by k if and only if `prefix[r] % k == prefix[l-1] % k`. So you need pairs of equal prefix sum remainders.

> 💡 **Hint 2:** Use a HashMap counting occurrences of each remainder. For each new prefix sum, its remainder tells you how many previous prefix sums had the same remainder.

> 💡 **Hint 3:** Handle negative remainders: in Python, `%` always returns non-negative. In Java/C++, use `((prefix % k) + k) % k` to ensure non-negative remainder.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(k)

Running prefix sum modulo k. HashMap counts occurrences of each remainder. For each new remainder r, add `map[r]` to the count (pairs with equal remainders), then increment `map[r]`.
