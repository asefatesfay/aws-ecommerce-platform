# Find Minimum in Rotated Sorted Array

**Difficulty:** Medium
**Pattern:** Binary Search (Modified)
**LeetCode:** #153

## Problem Statement

Suppose an array of length `n` sorted in ascending order is rotated between `1` and `n` times. Given the sorted rotated array `nums` of unique elements, return the minimum element of this array. You must write an algorithm that runs in O(log n) time.

## Examples

### Example 1
**Input:** `nums = [3,4,5,1,2]`
**Output:** `1`

### Example 2
**Input:** `nums = [4,5,6,7,0,1,2]`
**Output:** `0`

### Example 3
**Input:** `nums = [11,13,15,17]`
**Output:** `11`

## Constraints
- `n == nums.length`
- `1 <= n <= 5000`
- `-5000 <= nums[i] <= 5000`
- All the integers of `nums` are unique
- `nums` is sorted and rotated between 1 and n times

## Hints

> 💡 **Hint 1:** The minimum is at the "rotation point" — where the array transitions from large to small values.

> 💡 **Hint 2:** Compare nums[mid] with nums[right]. If nums[mid] > nums[right], the minimum is in the right half (left = mid + 1). Otherwise, it's in the left half including mid (right = mid).

> 💡 **Hint 3:** Continue until left == right. That's the minimum.

## Approach

**Time Complexity:** O(log n)
**Space Complexity:** O(1)

Binary search comparing mid with right boundary. Narrow toward the rotation point.
