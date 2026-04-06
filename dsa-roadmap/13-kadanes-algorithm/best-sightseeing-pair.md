# Best Sightseeing Pair

**Difficulty:** Medium
**Pattern:** Kadane's / Running Maximum
**LeetCode:** #1014

## Problem Statement

You are given an integer array `values` where `values[i]` represents the value of the `i`th sightseeing spot. Two sightseeing spots `i` and `j` with `i < j` have a combined score of `values[i] + values[j] + i - j`. Return the maximum score of a pair of sightseeing spots.

## Examples

### Example 1
**Input:** `values = [8, 1, 5, 2, 6]`
**Output:** `11`
**Explanation:** i=0, j=2: 8+5+0-2=11.

### Example 2
**Input:** `values = [1, 2]`
**Output:** `2`

## Constraints
- `2 <= values.length <= 5 * 10^4`
- `1 <= values[i] <= 1000`

## Hints

> 💡 **Hint 1:** Rewrite the score as `(values[i] + i) + (values[j] - j)`. For a fixed j, you want to maximize `values[i] + i` for all i < j.

> 💡 **Hint 2:** Scan left to right. Maintain the maximum `values[i] + i` seen so far. At each j, the best score ending at j is `max_left + values[j] - j`.

> 💡 **Hint 3:** Update `max_left` after computing the score at j (since i < j strictly).

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Single pass: track the running maximum of `values[i] + i`. At each position j, compute `max_left + values[j] - j` and update the global maximum.
