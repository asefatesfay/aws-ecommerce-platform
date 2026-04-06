# Validate Stack Sequences

**Difficulty:** Medium
**Pattern:** Stack Simulation
**LeetCode:** #946

## Problem Statement

Given two integer arrays `pushed` and `popped` each with distinct values, return `true` if this could have been the result of a sequence of push and pop operations on an initially empty stack, or `false` otherwise.

## Examples

### Example 1
**Input:** `pushed = [1,2,3,4,5]`, `popped = [4,5,3,2,1]`
**Output:** `true`
**Explanation:** Push 1,2,3,4, pop 4. Push 5, pop 5. Pop 3,2,1.

### Example 2
**Input:** `pushed = [1,2,3,4,5]`, `popped = [4,3,5,1,2]`
**Output:** `false`
**Explanation:** Can't pop 1 before 2.

## Constraints
- `1 <= pushed.length <= 1000`
- `0 <= pushed[i] <= 1000`
- All values of `pushed` are unique
- `popped.length == pushed.length`
- `popped` is a permutation of `pushed`

## Hints

> 💡 **Hint 1:** Simulate the process. Use an actual stack and a pointer into the `popped` array.

> 💡 **Hint 2:** Push elements from `pushed` one by one. After each push, check if the top of the stack matches the next element to pop. If yes, pop and advance the pop pointer.

> 💡 **Hint 3:** After processing all pushes, the stack should be empty if the sequences are valid.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(n)

Simulate: push elements, greedily pop when the top matches the next expected pop. Valid if stack is empty at the end.
