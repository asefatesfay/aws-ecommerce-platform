# Missing Ranges

**Difficulty:** Easy
**Pattern:** Array / Linear Scan
**LeetCode:** #163

## Problem Statement

You are given an inclusive range `[lower, upper]` and a sorted unique integer array `nums`, where all elements are within the inclusive range. A number `x` is considered missing if `x` is in `[lower, upper]` and `x` is not in `nums`.

Return the shortest sorted list of ranges that exactly covers all the missing numbers. Each range `[a, b]` in the list should be output as:
- `"a->b"` if `a != b`
- `"a"` if `a == b`

## Examples

### Example 1
**Input:** `nums = [0, 1, 3, 50, 75]`, `lower = 0`, `upper = 99`
**Output:** `["2", "4->49", "51->74", "76->99"]`

### Example 2
**Input:** `nums = [-1]`, `lower = -1`, `upper = -1`
**Output:** `[]`
**Explanation:** No missing numbers.

## Constraints
- `-10^9 <= lower <= upper <= 10^9`
- `0 <= nums.length <= 100`
- `lower <= nums[i] <= upper`
- All values in `nums` are unique

## Hints

> 💡 **Hint 1:** Think of the gaps between consecutive elements (and between the boundaries and the first/last elements). Each gap that is more than 1 wide represents a missing range.

> 💡 **Hint 2:** Add sentinel values: treat `lower - 1` as a virtual element before the array and `upper + 1` as a virtual element after. Then check gaps between consecutive pairs.

> 💡 **Hint 3:** For each consecutive pair (prev, curr), if curr - prev > 1, there's a missing range from prev+1 to curr-1. Format it as a single number or a range accordingly.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1) (excluding output)

Iterate through the array with a "previous" pointer initialized to `lower - 1`. For each element (and finally `upper + 1`), check if the gap between previous+1 and current-1 is non-empty, and if so, add it to the result.
