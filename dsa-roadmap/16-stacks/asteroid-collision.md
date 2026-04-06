# Asteroid Collision

**Difficulty:** Medium
**Pattern:** Stack Simulation
**LeetCode:** #735

## Problem Statement

We are given an array `asteroids` of integers representing asteroids in a row. For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed. Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

## Examples

### Example 1
**Input:** `asteroids = [5,10,-5]`
**Output:** `[5,10]`
**Explanation:** 10 and -5 collide → 10 survives. 5 and 10 never collide (same direction).

### Example 2
**Input:** `asteroids = [8,-8]`
**Output:** `[]`
**Explanation:** Both explode.

### Example 3
**Input:** `asteroids = [10,2,-5]`
**Output:** `[10]`

## Constraints
- `2 <= asteroids.length <= 10^4`
- `-1000 <= asteroids[i] <= 1000`
- `asteroids[i] != 0`

## Hints

> 💡 **Hint 1:** Use a stack. Process asteroids left to right.

> 💡 **Hint 2:** A collision only happens when the top of the stack is positive (moving right) and the current asteroid is negative (moving left).

> 💡 **Hint 3:** When a collision occurs: if the stack top is smaller, pop it and continue checking. If equal, pop and discard current. If stack top is larger, discard current. If no collision (or stack empty), push current.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(n)

Stack simulation: push asteroids, handling collisions when a right-moving top meets a left-moving current asteroid.
