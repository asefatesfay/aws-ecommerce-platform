# Find in Mountain Array

**Difficulty:** Hard
**Pattern:** Binary Search (Multiple)
**LeetCode:** #1095

## Problem Statement

You may recall that an array `arr` is a mountain array if and only if: `arr.length >= 3`, there exists some `i` with `0 < i < arr.length - 1` such that `arr[0] < arr[1] < ... < arr[i-1] < arr[i] > arr[i+1] > ... > arr[arr.length - 1]`. Given a mountain array `mountainArr`, return the minimum index such that `mountainArr.get(index) == target`. If such an index does not exist, return `-1`. You cannot access the mountain array directly. You may only access the array using a `MountainArray` interface with `get(k)` and `length()` methods.

## Examples

### Example 1
**Input:** `array = [1,2,3,4,5,3,1]`, `target = 3`
**Output:** `2`

### Example 2
**Input:** `array = [0,1,2,4,2,1]`, `target = 3`
**Output:** `-1`

## Constraints
- `3 <= mountain_arr.length() <= 10^4`
- `0 <= target <= 10^9`
- `0 <= mountain_arr.get(index) <= 10^9`

## Hints

> 💡 **Hint 1:** Three binary searches: (1) find the peak index, (2) search the ascending left side, (3) search the descending right side.

> 💡 **Hint 2:** Find peak: binary search where if arr[mid] < arr[mid+1], peak is to the right; otherwise to the left or at mid.

> 💡 **Hint 3:** Search left side (ascending) first. If not found, search right side (descending). Return the minimum index found.

## Approach

**Time Complexity:** O(log n)
**Space Complexity:** O(1)

Three binary searches: find peak, search ascending half, search descending half. Return minimum valid index.
