# Car Fleet

**Difficulty:** Medium
**Pattern:** Stack / Sorting
**LeetCode:** #853

## Problem Statement

There are `n` cars going to the same destination along a one-lane road. The destination is `target` miles away. You are given two integer array `position` and `speed`, both of length `n`, where `position[i]` is the position of the `i`th car and `speed[i]` is the speed of the `i`th car (in miles per hour). A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed. The faster car will slow down to match the slower car's speed. A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet. Return the number of car fleets that will arrive at the destination.

## Examples

### Example 1
**Input:** `target = 12`, `position = [10,8,0,5,3]`, `speed = [2,4,1,1,3]`
**Output:** `3`

### Example 2
**Input:** `target = 10`, `position = [3]`, `speed = [3]`
**Output:** `1`

## Constraints
- `n == position.length == speed.length`
- `1 <= n <= 10^5`
- `0 < target <= 10^6`
- `0 < speed[i] <= 10^6`
- `0 <= position[i] < target`
- All values of `position` are unique

## Hints

> 💡 **Hint 1:** Sort cars by position in descending order (closest to target first). Compute the time each car would take to reach the target: `time = (target - position) / speed`.

> 💡 **Hint 2:** Use a stack. Process cars from closest to farthest. If a car's time is ≤ the time of the car ahead (top of stack), it catches up and joins that fleet — don't push it.

> 💡 **Hint 3:** If a car's time is > the top of the stack, it forms a new fleet — push it. The stack size at the end is the number of fleets.

## Approach

**Time Complexity:** O(n log n) for sorting
**Space Complexity:** O(n)

Sort by position descending. Stack of arrival times. A car joins the fleet ahead if its time ≤ stack top; otherwise it starts a new fleet.
