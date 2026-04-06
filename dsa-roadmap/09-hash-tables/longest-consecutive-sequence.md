# Longest Consecutive Sequence

**Difficulty:** Medium
**Pattern:** Hash Set
**LeetCode:** #128

## Problem Statement

Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence. You must write an algorithm that runs in O(n) time.

## Examples

### Example 1
**Input:** `nums = [100, 4, 200, 1, 3, 2]`
**Output:** `4`
**Explanation:** The longest consecutive sequence is [1, 2, 3, 4], length 4.

### Example 2
**Input:** `nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]`
**Output:** `9`

## Constraints
- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Hints

> 💡 **Hint 1:** Sorting would give O(n log n). For O(n), use a HashSet for O(1) lookups.

> 💡 **Hint 2:** For each number, only start counting a sequence if it's the beginning of a sequence — i.e., `num - 1` is NOT in the set. This avoids redundant work.

> 💡 **Hint 3:** When you find a sequence start, count upward (num+1, num+2, ...) as long as the next number is in the set. Track the maximum length found.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(n)

Add all numbers to a HashSet. For each number that is a sequence start (num-1 not in set), count the length of the sequence starting there. Return the maximum length.
