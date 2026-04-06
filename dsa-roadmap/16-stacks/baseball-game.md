# Baseball Game

**Difficulty:** Easy
**Pattern:** Stack Simulation
**LeetCode:** #682

## Problem Statement

You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record. You are given a list of strings `operations`, where `operations[i]` is the `i`th operation you must apply to the record and is one of the following:
- An integer `x`: Record a new score of `x`.
- `"+"`: Record a new score that is the sum of the previous two scores.
- `"D"`: Record a new score that is the double of the previous score.
- `"C"`: Invalidate the previous score, removing it from the record.

Return the sum of all the scores on the record after applying all the operations.

## Examples

### Example 1
**Input:** `ops = ["5","2","C","D","+"]`
**Output:** `30`
**Explanation:** 5 → [5], 2 → [5,2], C → [5], D → [5,10], + → [5,10,15]. Sum = 30.

### Example 2
**Input:** `ops = ["5","-2","4","C","D","9","+","+"]`
**Output:** `27`

## Constraints
- `1 <= operations.length <= 1000`
- `operations[i]` is `"C"`, `"D"`, `"+"`, or a string representing an integer in the range `[-3 * 10^4, 3 * 10^4]`

## Hints

> 💡 **Hint 1:** Use a stack to maintain the current record of scores.

> 💡 **Hint 2:** For each operation: integer → push, "C" → pop, "D" → push(top*2), "+" → push(top + second_top).

> 💡 **Hint 3:** Sum all elements in the stack at the end.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(n)

Stack simulation: apply each operation to the stack. Sum the final stack.
