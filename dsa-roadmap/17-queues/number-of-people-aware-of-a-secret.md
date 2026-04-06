# Number of People Aware of a Secret

**Difficulty:** Medium
**Pattern:** Queue / Simulation
**LeetCode:** #2327

## Problem Statement

On day `1`, one person discovers a secret. You are given an integer `n` and two integers `delay` and `forget`. Every person who knows the secret will share it with a new person every day for the next `delay` days after discovering it. Every person who knows the secret will forget it after `forget` days. Return the number of people who know the secret at the end of day `n`. Since the answer may be very large, return it modulo `10^9 + 7`.

## Examples

### Example 1
**Input:** `n = 6`, `delay = 2`, `forget = 4`
**Output:** `5`

### Example 2
**Input:** `n = 4`, `delay = 1`, `forget = 3`
**Output:** `6`

## Constraints
- `2 <= n <= 1000`
- `1 <= delay < forget <= n`

## Hints

> 💡 **Hint 1:** Use a queue or array to track how many people discovered the secret on each day.

> 💡 **Hint 2:** On each day, the number of new people who learn the secret equals the sum of people who discovered it `delay` to `forget-1` days ago (they're still sharing).

> 💡 **Hint 3:** People who discovered it `forget` days ago no longer know it. Track the total knowing and subtract those who forget.

## Approach

**Time Complexity:** O(n × forget)
**Space Complexity:** O(forget)

Simulate day by day. Track discoveries per day. New discoveries = sum of people who discovered in the sharing window. Total = sum of people in the knowing window.
