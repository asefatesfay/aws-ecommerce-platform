# Number of Visible People in a Queue

**Difficulty:** Hard
**Pattern:** Monotonic Stack
**LeetCode:** #1944

## Problem Statement

There are `n` people standing in a queue, and they numbered from `0` to `n - 1` in left to right order. You are given an array `heights` of distinct integers where `heights[i]` represents the height of the `i`th person. A person can see another person to their right in the queue if everybody in between is shorter than both of them. More formally, the `i`th person can see the `j`th person if `i < j` and `min(heights[i], heights[j]) > max(heights[i+1], heights[i+2], ..., heights[j-1])`. Return an array `answer` of length `n` where `answer[i]` is the number of people the `i`th person can see to their right in the queue.

## Examples

### Example 1
**Input:** `heights = [10,6,8,5,11,9]`
**Output:** `[3,1,2,1,1,0]`

### Example 2
**Input:** `heights = [5,1,2,3,10]`
**Output:** `[4,1,1,1,0]`

## Constraints
- `n == heights.length`
- `1 <= n <= 10^5`
- `1 <= heights[i] <= 10^5`
- All integers in `heights` are unique

## Hints

> 💡 **Hint 1:** Use a monotonic decreasing stack. Process from right to left.

> 💡 **Hint 2:** For each person i, they can see all people that get popped from the stack (shorter people between them and the next taller person), plus the next taller person (if any).

> 💡 **Hint 3:** Count pops as visible people. If the stack is non-empty after all pops, add 1 more (the first person taller than i).

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(n)

Monotonic decreasing stack processed right to left. Each pop represents a visible person. The remaining stack top (if any) is also visible.
