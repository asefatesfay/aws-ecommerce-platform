# Largest Rectangle in Histogram

**Difficulty:** Hard
**Pattern:** Monotonic Stack
**LeetCode:** #84

## Problem Statement

Given an array of integers `heights` representing the histogram's bar height where the width of each bar is `1`, return the area of the largest rectangle in the histogram.

## Examples

### Example 1
**Input:** `heights = [2,1,5,6,2,3]`
**Output:** `10`
**Explanation:** The largest rectangle has area 10 (bars of height 5 and 6, width 2).

### Example 2
**Input:** `heights = [2,4]`
**Output:** `4`

## Constraints
- `1 <= heights.length <= 10^5`
- `0 <= heights[i] <= 10^4`

## Hints

> 💡 **Hint 1:** For each bar, the largest rectangle using that bar as the shortest bar extends left and right until it hits a shorter bar. You need the "previous smaller" and "next smaller" indices for each bar.

> 💡 **Hint 2:** Use a monotonic increasing stack. When you pop a bar (because the current bar is shorter), the current bar is its "next smaller" and the new stack top is its "previous smaller". Compute the area.

> 💡 **Hint 3:** Add sentinel bars of height 0 at both ends to ensure all bars are eventually popped and processed.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(n)

Monotonic increasing stack. When a bar is popped, compute the rectangle area using the popped bar's height and the distance between the new stack top and the current index.
