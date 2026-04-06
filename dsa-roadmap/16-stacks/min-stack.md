# Min Stack

**Difficulty:** Medium
**Pattern:** Stack Design
**LeetCode:** #155

## Problem Statement

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time. Implement the `MinStack` class:
- `MinStack()` initializes the stack object.
- `void push(int val)` pushes the element `val` onto the stack.
- `void pop()` removes the element on the top of the stack.
- `int top()` gets the top element of the stack.
- `int getMin()` retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.

## Examples

### Example 1
**Input:** `["MinStack","push","push","push","getMin","pop","top","getMin"]` with args `[[],[-2],[0],[-3],[],[],[],[]]`
**Output:** `[null,null,null,null,-3,null,0,-2]`

## Constraints
- `-2^31 <= val <= 2^31 - 1`
- Methods `pop`, `top` and `getMin` operations will always be called on non-empty stacks
- At most `3 * 10^4` calls will be made to `push`, `pop`, `top`, and `getMin`

## Hints

> 💡 **Hint 1:** Use two stacks: one for the actual values and one for the minimums.

> 💡 **Hint 2:** The min stack stores the current minimum at each level. When pushing, push to min stack if the new value is ≤ current min (or if min stack is empty).

> 💡 **Hint 3:** When popping, also pop from the min stack if the popped value equals the current min. `getMin()` just peeks the min stack.

## Approach

**Time Complexity:** O(1) for all operations
**Space Complexity:** O(n)

Two stacks: main stack and min stack. Min stack tracks the minimum at each depth level.
