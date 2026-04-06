# Time Needed to Buy Tickets

**Difficulty:** Easy
**Pattern:** Queue Simulation
**LeetCode:** #2073

## Problem Statement

There are `n` people in a line queuing to buy tickets, where the `0`th person is at the front of the line and the `(n - 1)`th person is at the back of the line. You are given a 0-indexed integer array `tickets` of length `n` where the number of tickets that the `i`th person would like to buy is `tickets[i]`. Each person takes exactly 1 second to buy a ticket. A person can only buy 1 ticket at a time and has to go back to the end of the line (in a round-robin fashion) after buying a ticket if they still need more. Return the time taken for the person at position `k` to finish buying all their tickets.

## Examples

### Example 1
**Input:** `tickets = [2,3,2]`, `k = 2`
**Output:** `6`

### Example 2
**Input:** `tickets = [5,1,1,1]`, `k = 0`
**Output:** `8`

## Constraints
- `n == tickets.length`
- `1 <= n <= 100`
- `1 <= tickets[i] <= 100`
- `0 <= k < n`

## Hints

> 💡 **Hint 1:** You can simulate the queue, but there's a mathematical shortcut.

> 💡 **Hint 2:** For each person i before k (i <= k): they buy min(tickets[i], tickets[k]) tickets before k finishes. For each person i after k (i > k): they buy min(tickets[i], tickets[k]-1) tickets.

> 💡 **Hint 3:** Sum these up for the total time.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Mathematical: for each person, compute how many rounds they complete before person k finishes. Sum all contributions.
