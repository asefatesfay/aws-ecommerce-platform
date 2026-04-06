# Move Zeroes

**Difficulty:** Easy
**Pattern:** Two Pointers (Read/Write)
**LeetCode:** #283

## Problem Statement

Given an integer array `nums`, move all `0`s to the end of it while maintaining the relative order of the non-zero elements. You must do this in-place without making a copy of the array.

## Examples

### Example 1
**Input:** `nums = [0, 1, 0, 3, 12]`
**Output:** `[1, 3, 12, 0, 0]`
**Explanation:** The non-zero elements 1, 3, 12 maintain their relative order and are moved to the front. The two zeros are moved to the end.

### Example 2
**Input:** `nums = [0]`
**Output:** `[0]`

## Constraints
- `1 <= nums.length <= 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`

## Hints

> 💡 **Hint 1:** Think about maintaining a "write position" — a pointer that tracks where the next non-zero element should go.

> 💡 **Hint 2:** Use two pointers: one scans through the array (read pointer), one tracks the next available position for non-zero elements (write pointer). When the read pointer finds a non-zero, place it at the write pointer position.

> 💡 **Hint 3:** After placing all non-zero elements, fill the remaining positions from the write pointer to the end with zeros.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Use a write pointer starting at 0. Scan through the array; whenever a non-zero element is found, place it at the write pointer and advance both pointers. After the scan, fill everything from the write pointer onward with zeros.
