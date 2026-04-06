# Set Mismatch

**Difficulty:** Easy
**Pattern:** Bit Manipulation / Math / Hash Map
**LeetCode:** #645

## Problem Statement

You have a set of integers `s`, which originally contains all the numbers from `1` to `n`. Unfortunately, due to some error, one of the numbers in `s` got duplicated to another number in the set, which results in the repetition of one number and loss of another number. You are given an integer array `nums` representing the data status of this set after the error. Find the number that occurs twice and the number that is missing and return them in the form of an array `[duplicate, missing]`.

## Examples

### Example 1
**Input:** `nums = [1, 2, 2, 4]`
**Output:** `[2, 3]`
**Explanation:** 2 is duplicated, 3 is missing.

### Example 2
**Input:** `nums = [1, 1]`
**Output:** `[1, 2]`

## Constraints
- `2 <= nums.length <= 10^4`
- `1 <= nums[i] <= n`

## Hints

> 💡 **Hint 1:** Use a frequency array or HashMap to count occurrences. The duplicate has count 2, the missing has count 0.

> 💡 **Hint 2:** For an O(1) space approach: use the array itself as a marker. For each value v, negate nums[v-1]. If you try to negate an already-negative number, that index+1 is the duplicate.

> 💡 **Hint 3:** After marking, scan for the positive value — its index+1 is the missing number. Restore the array if needed.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1) with index-marking approach, O(n) with HashMap

Index-marking: use sign of nums[v-1] to track visited values. The duplicate is found when you try to mark an already-marked position. The missing is the index with a positive value after all marking.
