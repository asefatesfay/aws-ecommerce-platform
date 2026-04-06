# Range Addition

**Difficulty:** Medium
**Pattern:** Difference Array
**LeetCode:** #370

## Problem Statement

You have an integer array of length `n` initialized with all 0s. You are given `k` update operations. Each operation is represented as a triplet `[startIndex, endIndex, inc]` which increments each element of subarray `nums[startIndex...endIndex]` (inclusive) with `inc`. Return the modified array after all `k` operations were executed.

## Examples

### Example 1
**Input:** `length = 5`, `updates = [[1,3,2],[2,4,3],[0,2,-2]]`
**Output:** `[-2,0,3,5,3]`

## Constraints
- `1 <= length <= 10^5`
- `0 <= k <= 10^4`
- `0 <= startIndex <= endIndex < length`
- `-1000 <= inc <= 1000`

## Hints

> 💡 **Hint 1:** Applying each update naively is O(n) per update → O(nk) total. Can you do better?

> 💡 **Hint 2:** Use a difference array. For each update [start, end, inc]: add `inc` at index `start` and subtract `inc` at index `end+1`.

> 💡 **Hint 3:** After all updates, compute the prefix sum of the difference array. This gives the final values. Total time: O(n + k).

## Approach

**Time Complexity:** O(n + k)
**Space Complexity:** O(n)

Difference array: mark the start and end+1 of each range update. Compute prefix sum to get final values. This is the inverse of prefix sum — difference array enables O(1) range updates.
