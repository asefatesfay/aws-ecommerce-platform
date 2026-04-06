# Trapping Rain Water

**Difficulty:** Hard
**Pattern:** Two Pointers
**LeetCode:** #42

## Problem Statement

Given `n` non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

## Examples

### Example 1
**Input:** `height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]`
**Output:** `6`
**Explanation:** 6 units of water are trapped.

### Example 2
**Input:** `height = [4, 2, 0, 3, 2, 5]`
**Output:** `9`

## Constraints
- `n == height.length`
- `1 <= n <= 2 * 10^4`
- `0 <= height[i] <= 10^5`

## Hints

> 💡 **Hint 1:** Water at position i is determined by `min(max_left[i], max_right[i]) - height[i]`. Precomputing these arrays gives an O(n) solution with O(n) space.

> 💡 **Hint 2:** For O(1) space, use two pointers. Maintain `left_max` and `right_max` as you go. The key insight: if `left_max < right_max`, the water at the left pointer is determined by `left_max` (the right side is guaranteed to be at least `right_max`).

> 💡 **Hint 3:** Process the side with the smaller max. If `left_max <= right_max`, process left: add `left_max - height[left]` to result, advance left. Otherwise process right similarly.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Two pointers with running left_max and right_max. Always process the side with the smaller max — that side's water level is fully determined by its own max (the other side is at least as tall).
