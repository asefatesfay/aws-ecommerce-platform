# Number of Good Pairs

**Difficulty:** Easy
**Pattern:** Hash Map / Counting
**LeetCode:** #1512

## Problem Statement

Given an array of integers `nums`, return the number of good pairs. A pair `(i, j)` is called good if `nums[i] == nums[j]` and `i < j`.

## Examples

### Example 1
**Input:** `nums = [1, 2, 3, 1, 1, 3]`
**Output:** `4`
**Explanation:** Good pairs: (0,3), (0,4), (3,4), (2,5) → 4 pairs.

### Example 2
**Input:** `nums = [1, 1, 1, 1]`
**Output:** `6`
**Explanation:** Each pair of the four 1s is a good pair: C(4,2) = 6.

### Example 3
**Input:** `nums = [1, 2, 3]`
**Output:** `0`

## Constraints
- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 100`

## Hints

> 💡 **Hint 1:** For each element, how many good pairs does it form with previously seen equal elements?

> 💡 **Hint 2:** If you've seen a value k times before, the current occurrence forms k new good pairs (one with each previous occurrence).

> 💡 **Hint 3:** Use a HashMap to track how many times each value has been seen so far. For each element, add its current count to the total, then increment the count.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(n)

For each element, the number of new good pairs it creates equals the number of times it has appeared before. Track counts in a HashMap and accumulate.
