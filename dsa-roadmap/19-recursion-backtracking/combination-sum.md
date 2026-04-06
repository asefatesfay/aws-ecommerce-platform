# Combination Sum

**Difficulty:** Medium
**Pattern:** Backtracking
**LeetCode:** #39

## Problem Statement

Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations of `candidates` where the chosen numbers sum to `target`. You may return the combinations in any order. The same number may be chosen from `candidates` an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

## Examples

### Example 1
**Input:** `candidates = [2,3,6,7]`, `target = 7`
**Output:** `[[2,2,3],[7]]`

### Example 2
**Input:** `candidates = [2,3,5]`, `target = 8`
**Output:** `[[2,2,2,2],[2,3,3],[3,5]]`

## Constraints
- `1 <= candidates.length <= 30`
- `2 <= candidates[i] <= 40`
- All elements of `candidates` are distinct
- `1 <= target <= 40`

## Hints

> 💡 **Hint 1:** Backtracking with a remaining target. When remaining == 0, add the current combination to results.

> 💡 **Hint 2:** Use a start index to avoid duplicate combinations. At each step, try each candidate from start onward (allowing reuse of the same element).

> 💡 **Hint 3:** Prune: if remaining < 0, stop. Sort candidates first to enable early termination.

## Approach

**Time Complexity:** O(n^(T/M)) where T is target and M is minimum candidate
**Space Complexity:** O(T/M) recursion depth

Backtracking with start index (allowing reuse). Prune when remaining < 0. Add to results when remaining == 0.

## Python Implementation

```python
def combination_sum(candidates, target):
	candidates.sort()
	result = []
	path = []

	def backtrack(start, remaining):
		if remaining == 0:
			result.append(path[:])
			return

		for index in range(start, len(candidates)):
			value = candidates[index]
			if value > remaining:
				break
			path.append(value)
			backtrack(index, remaining - value)
			path.pop()

	backtrack(0, target)
	return result
```

## Step-by-Step Example

**Input:** `candidates = [2, 3, 6, 7]`, `target = 7`

1. Start with `remaining = 7`, `path = []`.
2. Choose `2`, recurse with `remaining = 5`, `path = [2]`.
3. Choose `2` again, recurse with `remaining = 3`, `path = [2, 2]`.
4. Choose `3`, recurse with `remaining = 0`, record `[2, 2, 3]`.
5. Backtrack until top level, then choose `7`, recurse with `remaining = 0`, record `[7]`.

**Output:** `[[2, 2, 3], [7]]`

## Flow Diagram

```mermaid
flowchart TD
	A[start remaining=target] --> B{remaining == 0?}
	B -- Yes --> C[record path]
	B -- No --> D[iterate candidates from start]
	D --> E{value > remaining?}
	E -- Yes --> F[break branch]
	E -- No --> G[append value]
	G --> H[recurse with same index]
	H --> I[pop value]
	I --> D
```

## Edge Cases

- No solution: `candidates = [5]`, `target = 3` returns `[]`.
- Reuse is allowed here, so recursive calls stay at the same index.
- Sorting enables the `break` pruning when values become too large.
