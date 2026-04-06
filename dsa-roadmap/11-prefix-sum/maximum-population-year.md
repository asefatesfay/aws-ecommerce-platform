# Maximum Population Year

**Difficulty:** Easy
**Pattern:** Difference Array / Prefix Sum
**LeetCode:** #1854

## Problem Statement

You are given a 2D integer array `logs` where each `logs[i] = [birthi, deathi]` indicates the birth and death years of the `i`th person. The population of some year `x` is the number of people alive during year `x`. The `i`th person is alive during years `birthi` through `deathi - 1`. Return the earliest year with the maximum population.

## Examples

### Example 1
**Input:** `logs = [[1993,1999],[2000,2010]]`
**Output:** `1993`
**Explanation:** Max population is 1 (only one person alive at any time). Earliest year is 1993.

### Example 2
**Input:** `logs = [[1950,1961],[1960,1971],[1970,1981]]`
**Output:** `1960`

## Constraints
- `1 <= logs.length <= 100`
- `1950 <= birthi < deathi <= 2050`

## Hints

> 💡 **Hint 1:** Use a difference array over the year range [1950, 2050]. For each person, increment at birth year and decrement at death year.

> 💡 **Hint 2:** Compute the prefix sum of the difference array to get the population for each year.

> 💡 **Hint 3:** Find the year with the maximum population (earliest if tied).

## Approach

**Time Complexity:** O(n + Y) where Y is the year range (100 years)
**Space Complexity:** O(Y)

Difference array: +1 at birth, -1 at death. Prefix sum gives population per year. Find the maximum.
