# Search in Rotated Sorted Array

**Difficulty:** Medium
**Pattern:** Binary Search (Modified)
**LeetCode:** #33

## Problem Statement

There is an integer array `nums` sorted in ascending order (with distinct values). Prior to being passed to your function, `nums` is possibly rotated at an unknown pivot index `k`. Given the array `nums` after the possible rotation and an integer `target`, return the index of `target` if it is in `nums`, or `-1` if it is not in `nums`. You must write an algorithm with O(log n) runtime complexity.

## Examples

### Example 1
**Input:** `nums = [4,5,6,7,0,1,2]`, `target = 0`
**Output:** `4`

### Example 2
**Input:** `nums = [4,5,6,7,0,1,2]`, `target = 3`
**Output:** `-1`

### Example 3
**Input:** `nums = [1]`, `target = 0`
**Output:** `-1`

## Constraints
- `1 <= nums.length <= 5000`
- `-10^4 <= nums[i] <= 10^4`
- All values of `nums` are unique
- `nums` is an ascending array that is possibly rotated
- `-10^4 <= target <= 10^4`

## Hints

> 💡 **Hint 1:** In a rotated sorted array, at least one half of the array around mid is always sorted.

> 💡 **Hint 2:** Check which half is sorted: if nums[left] ≤ nums[mid], the left half is sorted. Otherwise, the right half is sorted.

> 💡 **Hint 3:** If the target is in the sorted half, search there. Otherwise, search the other half.

## Approach

**Time Complexity:** O(log n)
**Space Complexity:** O(1)

Modified binary search: determine which half is sorted, check if target is in that half, search accordingly.
