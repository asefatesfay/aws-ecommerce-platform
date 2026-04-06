# Container With Most Water

**Difficulty:** Medium
**Pattern:** Two Pointers (Opposite Ends)
**LeetCode:** #11

## Problem Statement

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i`th line are `(i, 0)` and `(i, height[i])`. Find two lines that together with the x-axis form a container, such that the container contains the most water. Return the maximum amount of water a container can store. You may not slant the container.

## Examples

### Example 1
**Input:** `height = [1, 8, 6, 2, 5, 4, 8, 3, 7]`
**Output:** `49`
**Explanation:** Lines at index 1 (height 8) and index 8 (height 7). Width = 7, height = min(8,7) = 7. Area = 49.

### Example 2
**Input:** `height = [1, 1]`
**Output:** `1`

## Constraints
- `n == height.length`
- `2 <= n <= 10^5`
- `0 <= height[i] <= 10^4`

## Hints

> 💡 **Hint 1:** The area is `min(height[left], height[right]) * (right - left)`. You want to maximize this.

> 💡 **Hint 2:** Start with the widest possible container (left=0, right=n-1). To potentially increase the area, you must increase the minimum height. Moving the taller pointer inward can only decrease width without helping height.

> 💡 **Hint 3:** Always move the pointer pointing to the shorter line inward. This is the only way to potentially find a taller minimum height that compensates for the reduced width.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Two pointers from both ends. At each step, compute the area and update the maximum. Move the pointer with the smaller height inward (the taller one can't help by moving).
