# Search in Rotated Sorted Array II

**Difficulty:** Medium
**Pattern:** Binary Search (Modified, with Duplicates)
**LeetCode:** #81

## Problem Statement

There is an integer array `nums` sorted in non-decreasing order (not necessarily with distinct values). Before being passed to your function, `nums` is rotated at an unknown pivot index `k`. Given the array `nums` after the possible rotation and an integer `target`, return `true` if `target` is in `nums`, or `false` if it is not in `nums`. You must decrease the overall operation steps as much as possible.

## Examples

### Example 1
**Input:** `nums = [2,5,6,0,0,1,2]`, `target = 0`
**Output:** `true`

### Example 2
**Input:** `nums = [2,5,6,0,0,1,2]`, `target = 3`
**Output:** `false`

## Constraints
- `1 <= nums.length <= 5000`
- `-10^4 <= nums[i] <= 10^4`
- `nums` is guaranteed to be rotated at some pivot
- `-10^4 <= target <= 10^4`

## Hints

> 💡 **Hint 1:** Same as Search in Rotated Sorted Array I, but duplicates make it harder to determine which half is sorted.

> 💡 **Hint 2:** When nums[left] == nums[mid] == nums[right], you can't determine which half is sorted. In this case, just increment left and decrement right (shrink by 1 on each side).

> 💡 **Hint 3:** Otherwise, apply the same logic as the no-duplicates version.

## Approach

**Time Complexity:** O(n) worst case (all duplicates), O(log n) average
**Space Complexity:** O(1)

Modified binary search with duplicate handling: when boundaries equal mid, shrink both sides by 1.
