# Daily Temperatures

**Difficulty:** Medium
**Pattern:** Monotonic Stack
**LeetCode:** #739

## Problem Statement

Given an array of integers `temperatures` represents the daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the `i`th day to get a warmer temperature. If there is no future day for which this is possible, keep `answer[i] == 0` instead.

## Examples

### Example 1
**Input:** `temperatures = [73,74,75,71,69,72,76,73]`
**Output:** `[1,1,4,2,1,1,0,0]`

### Example 2
**Input:** `temperatures = [30,40,50,60]`
**Output:** `[1,1,1,0]`

### Example 3
**Input:** `temperatures = [30,60,90]`
**Output:** `[1,1,0]`

## Constraints
- `1 <= temperatures.length <= 10^5`
- `30 <= temperatures[i] <= 100`

## Hints

> 💡 **Hint 1:** For each day, you need the next day with a higher temperature. This is the "next greater element" pattern.

> 💡 **Hint 2:** Use a monotonic decreasing stack of indices. When you find a temperature higher than the stack's top, the current day is the "next warmer day" for the top.

> 💡 **Hint 3:** Pop all indices from the stack whose temperatures are less than the current temperature. For each popped index i, `answer[i] = current_index - i`. Push the current index.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(n)

Monotonic decreasing stack of indices. When a warmer day is found, resolve all cooler days waiting on the stack.
