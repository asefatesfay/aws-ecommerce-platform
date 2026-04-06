# Exclusive Time of Functions

**Difficulty:** Medium
**Pattern:** Stack Simulation
**LeetCode:** #636

## Problem Statement

On a single-threaded CPU, we execute a program containing `n` functions. Each function has a unique ID between `0` and `n-1`. Function calls are stored in a call stack: when a function call starts, its ID is pushed onto the stack, and when a function call ends, its ID is popped off the stack. The function whose ID is at the top of the stack is the current function being executed. Each time a function starts or ends, we write a log with the ID, whether it started or ended, and the timestamp. Given a list `logs`, return the exclusive time of each function. The exclusive time of a function is the sum of execution times for all function calls in the program.

## Examples

### Example 1
**Input:** `n = 2`, `logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]`
**Output:** `[3,4]`
**Explanation:** Function 0 runs from 0-1 (2 units), then 6-6 (1 unit) = 3. Function 1 runs from 2-5 = 4 units.

## Constraints
- `1 <= n <= 100`
- `1 <= logs.length <= 500`
- `0 <= function_id < n`
- `0 <= timestamp <= 10^9`
- No two start events will happen at the same timestamp
- No two end events will happen at the same timestamp
- Each function has an `"end"` log for each `"start"` log

## Hints

> 💡 **Hint 1:** Use a stack to track the currently running function. Parse each log entry.

> 💡 **Hint 2:** On `start`: if the stack is non-empty, add elapsed time to the current top function. Push the new function ID and update the previous timestamp.

> 💡 **Hint 3:** On `end`: add elapsed time (including the end timestamp) to the current function. Pop it. Update the previous timestamp to `end_time + 1`.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(n)

Stack of function IDs. Track previous timestamp. On start/end, compute elapsed time and attribute it to the current top function.
