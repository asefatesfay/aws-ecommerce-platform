# Magnetic Force Between Two Balls

**Difficulty:** Medium
**Pattern:** Binary Search on Answer
**LeetCode:** #1552

## Problem Statement

In the universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put in his new invented basket. Rick has `n` empty baskets, the `i`th basket is at position `position[i]`, and Morty has `m` balls. Rick wants to put all `m` balls into the baskets such that the minimum magnetic force between any two balls is maximum. The magnetic force between two different balls at positions `x` and `y` is `|x - y|`. Given the integer array `position` and the integer `m`, return the required force.

## Examples

### Example 1
**Input:** `position = [1,2,3,4,7]`, `m = 3`
**Output:** `3`
**Explanation:** Place balls at 1, 4, 7. Min force = 3.

### Example 2
**Input:** `position = [5,4,3,2,1,1000000000]`, `m = 2`
**Output:** `999999999`

## Constraints
- `2 <= n <= 10^5`
- `1 <= position[i] <= 10^9`
- All integers in `position` are distinct
- `2 <= m <= position.length`

## Hints

> 💡 **Hint 1:** Binary search on the minimum force. Sort positions first.

> 💡 **Hint 2:** For a given minimum force f, greedily place balls: place the first ball at position[0], then place each subsequent ball at the first position that is at least f away from the last placed ball.

> 💡 **Hint 3:** If you can place all m balls, f is feasible (try larger). Otherwise, try smaller.

## Approach

**Time Complexity:** O(n log(max_position))
**Space Complexity:** O(1)

Sort positions. Binary search on minimum force. Check feasibility with greedy placement.
