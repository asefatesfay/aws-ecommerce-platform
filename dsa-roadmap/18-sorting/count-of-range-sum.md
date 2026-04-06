# Count of Range Sum

**Difficulty:** Hard
**Pattern:** Merge Sort / Prefix Sum
**LeetCode:** #327

## Problem Statement

Given an integer array `nums` and two integers `lower` and `upper`, return the number of range sums that lie in `[lower, upper]` inclusive. Range sum `S(i, j)` is defined as the sum of the elements in `nums` between indices `i` and `j` inclusive, where `i <= j`.

## Examples

### Example 1
**Input:** `nums = [-2,5,-1]`, `lower = -2`, `upper = 2`
**Output:** `3`
**Explanation:** Range sums: S(0,0)=-2, S(2,2)=-1, S(0,2)=2.

### Example 2
**Input:** `nums = [0]`, `lower = 0`, `upper = 0`
**Output:** `1`

## Constraints
- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `-10^5 <= lower <= upper <= 10^5`
- The answer is guaranteed to fit in a 32-bit integer

## Hints

> 💡 **Hint 1:** Build a prefix sum array. S(i,j) = prefix[j+1] - prefix[i]. You need pairs where lower ≤ prefix[j+1] - prefix[i] ≤ upper.

> 💡 **Hint 2:** Use modified merge sort on the prefix sum array. During merge, count pairs (i from left half, j from right half) where the difference is in [lower, upper].

> 💡 **Hint 3:** Since both halves are sorted, use two pointers to count valid pairs efficiently during each merge step.

## Approach

**Time Complexity:** O(n log n)
**Space Complexity:** O(n)

Prefix sum + modified merge sort. Count valid prefix sum pairs during merge steps.
