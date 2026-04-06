# Candy

**Difficulty:** Hard
**Pattern:** Greedy — Two Pass
**LeetCode:** #135

## Problem Statement
There are `n` children in a line, each with a rating. Give each child at least 1 candy. Children with higher ratings than their neighbors must get more candies. Return the minimum total candies needed.

## Examples

### Example 1
**Input:** `ratings = [1,0,2]`
**Output:** `5`
**Explanation:** [2,1,2] — child 0 gets 2 (higher than child 1), child 2 gets 2 (higher than child 1).

### Example 2
**Input:** `ratings = [1,2,2]`
**Output:** `4`
**Explanation:** [1,2,1] — child 1 gets 2 (higher than child 0), child 2 gets 1 (equal to child 1, no constraint).

## Constraints
- `n == ratings.length`
- `1 <= n <= 2×10⁴`
- `0 <= ratings[i] <= 2×10⁴`

## Hints

> 💡 **Hint 1:** Do two passes. Left-to-right: if `ratings[i] > ratings[i-1]`, give `candies[i] = candies[i-1] + 1`.

> 💡 **Hint 2:** Right-to-left: if `ratings[i] > ratings[i+1]`, give `candies[i] = max(candies[i], candies[i+1] + 1)`.

> 💡 **Hint 3:** The two passes handle left-neighbor and right-neighbor constraints independently. Taking the max ensures both are satisfied.

## Approach
**Time Complexity:** O(N)
**Space Complexity:** O(N)

Two-pass greedy: left pass satisfies left-neighbor constraint, right pass satisfies right-neighbor constraint. Sum the final candy array.
