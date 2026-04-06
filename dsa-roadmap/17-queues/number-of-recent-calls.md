# Number of Recent Calls

**Difficulty:** Easy
**Pattern:** Queue
**LeetCode:** #933

## Problem Statement

You have a `RecentCounter` class which counts the number of recent requests within a certain time frame. Implement the `RecentCounter` class:
- `RecentCounter()` Initializes the counter with zero recent requests.
- `int ping(int t)` Adds a new request at time `t`, where `t` represents some time in milliseconds, and returns the number of requests that has happened in the past `3000` milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range `[t - 3000, t]`.

It is guaranteed that every call to `ping` uses a strictly larger value of `t` than the previous call.

## Examples

### Example 1
**Input:** `["RecentCounter","ping","ping","ping","ping"]` with args `[[],[1],[100],[3001],[3002]]`
**Output:** `[null,1,2,3,3]`

## Constraints
- `1 <= t <= 10^9`
- Each test case will call `ping` with strictly increasing values of `t`
- At most `10^4` calls will be made to `ping`

## Hints

> 💡 **Hint 1:** Use a queue to store timestamps of recent pings.

> 💡 **Hint 2:** On each ping, add the new timestamp to the queue. Then remove all timestamps from the front that are older than `t - 3000`.

> 💡 **Hint 3:** The queue size after cleanup is the answer.

## Approach

**Time Complexity:** O(1) amortized
**Space Complexity:** O(3000) = O(1)

Queue of timestamps. Add new timestamp, remove outdated ones from front. Return queue size.
