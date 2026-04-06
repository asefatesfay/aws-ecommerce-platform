# Buildings With an Ocean View

**Difficulty:** Medium
**Pattern:** Monotonic Stack
**LeetCode:** #1762

## Problem Statement

There are `n` buildings in a line. You are given an integer array `heights` of size `n` that represents the heights of the buildings in the line. The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without obstructions. Formally, a building has an ocean view if all the buildings to its right have a smaller height. Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.

## Examples

### Example 1
**Input:** `heights = [4,2,3,1]`
**Output:** `[0,2,3]`
**Explanation:** Building 0 (height 4) sees ocean. Building 1 (height 2) is blocked by 3. Building 2 (height 3) sees ocean. Building 3 (height 1) sees ocean.

### Example 2
**Input:** `heights = [4,3,2,1]`
**Output:** `[0,1,2,3]`

## Constraints
- `1 <= heights.length <= 10^5`
- `1 <= heights[i] <= 10^8`

## Hints

> 💡 **Hint 1:** Scan from right to left. Track the maximum height seen so far.

> 💡 **Hint 2:** A building has an ocean view if its height is greater than all buildings to its right (i.e., greater than the current maximum).

> 💡 **Hint 3:** Collect indices with ocean views (in reverse order), then reverse the result.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(n)

Scan right to left, tracking the running maximum. A building has an ocean view if it's taller than the current maximum. Collect and reverse.
