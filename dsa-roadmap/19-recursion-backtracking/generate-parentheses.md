# Generate Parentheses

**Difficulty:** Medium
**Pattern:** Backtracking
**LeetCode:** #22

## Problem Statement

Given `n` pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

## Examples

### Example 1
**Input:** `n = 3`
**Output:** `["((()))","(()())","(())()","()(())","()()()"]`

### Example 2
**Input:** `n = 1`
**Output:** `["()"]`

## Constraints
- `1 <= n <= 8`

## Hints

> 💡 **Hint 1:** Track the count of open and close parentheses used so far.

> 💡 **Hint 2:** You can add `(` if open < n. You can add `)` if close < open (there's an unmatched open bracket).

> 💡 **Hint 3:** When the string has length 2n, add it to results. This naturally generates only valid combinations.

## Approach

**Time Complexity:** O(4^n / √n) — the nth Catalan number
**Space Complexity:** O(n) recursion depth

Backtracking with open/close counters. Add `(` when open < n, add `)` when close < open. Collect when length == 2n.

## Python Implementation

```python
def generate_parenthesis(n):
	result = []

	def backtrack(path, open_used, close_used):
		if len(path) == 2 * n:
			result.append(''.join(path))
			return

		if open_used < n:
			path.append('(')
			backtrack(path, open_used + 1, close_used)
			path.pop()

		if close_used < open_used:
			path.append(')')
			backtrack(path, open_used, close_used + 1)
			path.pop()

	backtrack([], 0, 0)
	return result
```

## Step-by-Step Example

**Input:** `n = 2`

1. Start with empty string.
2. Add `(` because open count is less than `2`.
3. Add another `(`, then only `)` is allowed twice, producing `(())`.
4. Backtrack to `(` and instead add `)`, then add `(`, then `)` to produce `()()`.

**Output:** `["(())", "()()"]`

## Flow Diagram

```mermaid
flowchart TD
	A[start path open=0 close=0] --> B{length == 2n?}
	B -- Yes --> C[record string]
	B -- No --> D{open < n?}
	D -- Yes --> E[append open bracket]
	E --> F[recurse]
	F --> G[pop]
	D -- No --> H{close < open?}
	G --> H
	H -- Yes --> I[append close bracket]
	I --> J[recurse]
	J --> K[pop]
```

## Edge Cases

- `n = 1` returns only `"()"`.
- A close bracket can never be added when `close_used == open_used`.
- The recursion generates only valid strings, so no cleanup pass is needed.
