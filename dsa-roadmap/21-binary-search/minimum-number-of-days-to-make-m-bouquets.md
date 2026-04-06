# Minimum Number of Days to Make m Bouquets

**Difficulty:** Medium
**Pattern:** Binary Search on Answer
**LeetCode:** #1482

## Problem Statement

You are given an integer array `bloomDay`, an integer `m` and an integer `k`. You want to make `m` bouquets. To make a bouquet, you need to use `k` adjacent flowers from the garden. The garden consists of `n` flowers, the `i`th flower will bloom in the `bloomDay[i]` and then can be used in exactly one bouquet. Return the minimum number of days you need to wait to be able to make `m` bouquets from the garden. If it is impossible to make `m` bouquets return `-1`.

## Examples

### Example 1
**Input:** `bloomDay = [1,10,3,10,2]`, `m = 3`, `k = 1`
**Output:** `3`

### Example 2
**Input:** `bloomDay = [1,10,3,10,2]`, `m = 3`, `k = 2`
**Output:** `-1`

## Constraints
- `bloomDay.length == n`
- `1 <= n <= 10^5`
- `1 <= bloomDay[i] <= 10^9`
- `1 <= m <= 10^6`
- `1 <= k <= n`

## Hints

> 💡 **Hint 1:** If m*k > n, it's impossible. Binary search on the number of days.

> 💡 **Hint 2:** For a given day d, count how many bouquets can be made: scan the array, count consecutive bloomed flowers (bloomDay[i] ≤ d), and divide each run by k.

> 💡 **Hint 3:** If bouquets ≥ m, day d is feasible (try fewer days). Otherwise, try more days.

## Approach

**Time Complexity:** O(n log(max_bloomDay))
**Space Complexity:** O(1)

Binary search on days [1, max(bloomDay)]. Check feasibility by counting bouquets possible on that day.
