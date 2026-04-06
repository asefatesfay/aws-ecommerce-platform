# Task Scheduler

**Difficulty:** Medium
**Pattern:** Greedy / Math
**LeetCode:** #621

## Problem Statement
Given a list of tasks (characters A-Z) and a cooldown `n`, find the minimum number of intervals needed to execute all tasks. Between two same tasks, there must be at least `n` intervals.

## Examples

### Example 1
**Input:** `tasks = ["A","A","A","B","B","B"]`, `n = 2`
**Output:** `8`
**Explanation:** A → B → idle → A → B → idle → A → B

### Example 2
**Input:** `tasks = ["A","A","A","B","B","B"]`, `n = 0`
**Output:** `6`

## Constraints
- `1 <= tasks.length <= 10⁴`
- `0 <= n <= 100`

## Hints

> 💡 **Hint 1:** The most frequent task determines the minimum time. If max_freq = f, we need at least `(f-1) * (n+1) + 1` slots.

> 💡 **Hint 2:** Count how many tasks have the maximum frequency (`count_max`). The formula becomes `(f-1) * (n+1) + count_max`.

> 💡 **Hint 3:** The answer is `max(len(tasks), (f-1)*(n+1) + count_max)` — we can't do fewer than the total number of tasks.

## Approach
**Time Complexity:** O(N)
**Space Complexity:** O(1) — only 26 possible tasks

Count frequencies, find max frequency and how many tasks share it. Apply the formula: `max(total_tasks, (max_freq-1)*(n+1) + count_of_max_freq_tasks)`.
