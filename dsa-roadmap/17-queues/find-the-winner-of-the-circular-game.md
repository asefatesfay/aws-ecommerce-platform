# Find the Winner of the Circular Game

**Difficulty:** Medium
**Pattern:** Queue Simulation / Math (Josephus Problem)
**LeetCode:** #1823

## Problem Statement

There are `n` friends that are playing a game. The friends are sitting in a circle and are numbered from `1` to `n` in clockwise order. More formally, moving clockwise from the `i`th friend brings you to the `(i+1)`th friend for `1 <= i < n`, and moving clockwise from the `n`th friend brings you to the `1`st friend. The rules of a game are as follows: Start at the `1`st friend. Count the next `k` friends in the clockwise direction including the friend you started at. The counting wraps around the circle and may count some friends more than once. The last friend you counted leaves the circle and loses the game. If there is still more than one friend in the circle, go back to step 2 starting from the friend immediately clockwise of the friend who just lost and repeat. Otherwise, the last friend in the circle wins the game. Given the number of friends, `n`, and an integer `k`, return the winner of the game.

## Examples

### Example 1
**Input:** `n = 5`, `k = 2`
**Output:** `3`

### Example 2
**Input:** `n = 6`, `k = 5`
**Output:** `1`

## Constraints
- `1 <= k <= n <= 500`

## Hints

> 💡 **Hint 1:** Simulate with a queue. Rotate k-1 people to the back, then remove the front (the kth person).

> 💡 **Hint 2:** Repeat until one person remains. The remaining person is the winner.

> 💡 **Hint 3:** For a mathematical O(n) solution, use the Josephus problem recurrence: `f(1) = 0`, `f(n) = (f(n-1) + k) % n`. The answer is `f(n) + 1`.

## Approach

**Time Complexity:** O(n) with Josephus formula, O(nk) with simulation
**Space Complexity:** O(n)

Queue simulation or Josephus recurrence. The mathematical solution is elegant and O(n).
