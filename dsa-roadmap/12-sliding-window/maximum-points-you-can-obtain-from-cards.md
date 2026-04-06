# Maximum Points You Can Obtain from Cards

**Difficulty:** Medium
**Pattern:** Sliding Window (Fixed) — Complement
**LeetCode:** #1423

## Problem Statement

There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array `cardPoints`. In one step, you can take one card from the beginning or from the end of the row. You have to take exactly `k` cards. Your score is the sum of the points of the cards you have taken. Return the maximum score you can obtain.

## Examples

### Example 1
**Input:** `cardPoints = [1, 2, 3, 4, 5, 6, 1]`, `k = 3`
**Output:** `12`
**Explanation:** Take the three rightmost cards: 6+5+4=15? No — take 1,6,5 from right: 1+6+5=12. Or 1,2,3 from left: 6. Best is 12.

### Example 2
**Input:** `cardPoints = [2, 2, 2]`, `k = 2`
**Output:** `4`

### Example 3
**Input:** `cardPoints = [9, 7, 7, 9, 7, 7, 9]`, `k = 7`
**Output:** `55`

## Constraints
- `1 <= cardPoints.length <= 10^5`
- `1 <= cardPoints[i] <= 10^4`
- `1 <= k <= cardPoints.length`

## Hints

> 💡 **Hint 1:** You take k cards from the two ends. The remaining n-k cards form a contiguous subarray in the middle.

> 💡 **Hint 2:** Maximizing the sum of k cards from the ends = minimizing the sum of the middle n-k cards.

> 💡 **Hint 3:** Find the minimum sum subarray of length n-k using a fixed sliding window. Subtract it from the total sum.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Total sum minus minimum sum of the middle window of size n-k. Use a fixed sliding window to find the minimum middle sum.
