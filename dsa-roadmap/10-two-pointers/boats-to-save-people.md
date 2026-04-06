# Boats to Save People

**Difficulty:** Medium
**Pattern:** Two Pointers + Greedy
**LeetCode:** #881

## Problem Statement

You are given an array `people` where `people[i]` is the weight of the `i`th person, and an infinite number of boats where each boat can carry a maximum weight of `limit`. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most `limit`. Return the minimum number of boats to carry every given person.

## Examples

### Example 1
**Input:** `people = [1, 2]`, `limit = 3`
**Output:** `1`
**Explanation:** Both can share one boat (1+2=3 ≤ 3).

### Example 2
**Input:** `people = [3, 2, 2, 1]`, `limit = 3`
**Output:** `3`
**Explanation:** (1,2), (2), (3).

### Example 3
**Input:** `people = [3, 5, 3, 4]`, `limit = 5`
**Output:** `4`

## Constraints
- `1 <= people.length <= 5 * 10^4`
- `1 <= people[i] <= limit <= 3 * 10^4`

## Hints

> 💡 **Hint 1:** Sort the array. Greedy: try to pair the heaviest person with the lightest person.

> 💡 **Hint 2:** Two pointers: left at lightest, right at heaviest. If they can share a boat (sum ≤ limit), pair them (advance both). Otherwise, the heaviest goes alone (advance right only).

> 💡 **Hint 3:** Each iteration uses one boat. Count the number of iterations.

## Approach

**Time Complexity:** O(n log n) for sorting
**Space Complexity:** O(1)

Sort, then two pointers. Greedily pair the heaviest with the lightest when possible. Each step uses one boat.
