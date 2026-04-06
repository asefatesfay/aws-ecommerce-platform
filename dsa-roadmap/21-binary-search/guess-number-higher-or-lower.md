# Guess Number Higher or Lower

**Difficulty:** Easy
**Pattern:** Binary Search
**LeetCode:** #374

## Problem Statement

We are playing the Guess Game. The game is as follows: I pick a number from `1` to `n`. You have to guess which number I picked. Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess. You call a pre-defined API `int guess(int num)`, which returns three possible results: `-1` (my number is lower), `1` (my number is higher), `0` (your guess is correct). Return the number that I picked.

## Examples

### Example 1
**Input:** `n = 10`, `pick = 6`
**Output:** `6`

### Example 2
**Input:** `n = 1`, `pick = 1`
**Output:** `1`

## Constraints
- `1 <= n <= 2^31 - 1`
- `1 <= pick <= n`

## Hints

> 💡 **Hint 1:** Binary search on [1, n]. Call guess(mid).

> 💡 **Hint 2:** If guess(mid) == 0, return mid. If guess(mid) == -1, search left (right = mid - 1). If guess(mid) == 1, search right (left = mid + 1).

> 💡 **Hint 3:** Standard binary search with the API as the comparison function.

## Approach

**Time Complexity:** O(log n)
**Space Complexity:** O(1)

Standard binary search using the guess API as the comparator.
