# Permutations II

**Difficulty:** Medium
**Pattern:** Backtracking (with Duplicates)
**LeetCode:** #47

## Problem Statement

Given a collection of numbers, `nums`, that might contain duplicates, return all possible unique permutations in any order.

## Examples

### Example 1
**Input:** `nums = [1,1,2]`
**Output:** `[[1,1,2],[1,2,1],[2,1,1]]`

### Example 2
**Input:** `nums = [1,2,3]`
**Output:** `[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]`

## Constraints
- `1 <= nums.length <= 8`
- `-10 <= nums[i] <= 10`

## Hints

> 💡 **Hint 1:** Sort the array. Use a `used` boolean array.

> 💡 **Hint 2:** Skip duplicates: if `nums[i] == nums[i-1]` and `used[i-1] == false`, skip nums[i]. This ensures duplicates are used in order.

> 💡 **Hint 3:** The condition `used[i-1] == false` means the previous duplicate was not used in the current path (it was backtracked), so using nums[i] now would create a duplicate permutation.

## Approach

**Time Complexity:** O(n × n!)
**Space Complexity:** O(n)

Sort + backtracking with used array. Skip duplicate values when the previous identical value is not in the current path.
