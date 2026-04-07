# Permutations

**Difficulty:** Medium
**Pattern:** Backtracking
**LeetCode:** #46

## Problem Statement

Given an array `nums` of distinct integers, return all the possible permutations. You can return the answer in any order.

## Examples

### Example 1
**Input:** `nums = [1,2,3]`
**Output:** `[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]`

### Example 2
**Input:** `nums = [0,1]`
**Output:** `[[0,1],[1,0]]`

### Example 3
**Input:** `nums = [1]`
**Output:** `[[1]]`

## Constraints
- `1 <= nums.length <= 6`
- `-10 <= nums[i] <= 10`
- All the integers of `nums` are unique

## Hints

> 💡 **Hint 1:** At each position, try placing each unused element. Use a `used` boolean array to track which elements have been placed.

> 💡 **Hint 2:** When the current permutation has n elements, add it to results.

> 💡 **Hint 3:** Alternatively, swap elements in-place: swap nums[start] with each nums[i] (i >= start), recurse with start+1, then swap back.

## Approach

**Time Complexity:** O(n × n!)
**Space Complexity:** O(n) recursion depth

Backtracking with used array or in-place swapping. Try each unused element at each position.

## Python Implementation

```python
def permute(nums):
	result = []
	path = []
	used = [False] * len(nums)

	def backtrack():
		if len(path) == len(nums):
			result.append(path[:])
			return

		for index, value in enumerate(nums):
			if used[index]:
				continue
			used[index] = True
			path.append(value)
			backtrack()
			path.pop()
			used[index] = False

	backtrack()
	return result
```

## Step-by-Step Example

**Input:** `nums = [1, 2, 3]`

1. Start with empty path.
2. Choose `1`, then choose `2`, then choose `3` to record `[1, 2, 3]`.
3. Backtrack to `[1]`, then choose `3`, then `2` to record `[1, 3, 2]`.
4. Backtrack to top level and repeat starting with `2`, then with `3`.

**Output:** `[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]`

## Flow Diagram

```mermaid
flowchart TD
	A[start with empty path] --> B{path length == n?}
	B -- Yes --> C[record permutation]
	B -- No --> D[loop over indices]
	D --> E{used index?}
	E -- Yes --> D
	E -- No --> F[mark used and append]
	F --> G[recurse]
	G --> H[pop and unmark]
	H --> D
```

## Recursion Tree Visualization

For **Input:** `nums = [1, 2, 3]`, here is how the recursion tree unfolds with all function calls:

```mermaid
flowchart TD
    A["backtrack() len=0<br/>try index 0,1,2"] --> B["mark[0]=T, path=[1]<br/>backtrack()"]
    A --> C["mark[1]=T, path=[2]<br/>backtrack()"]
    A --> D["mark[2]=T, path=[3]<br/>backtrack()"]
    
    B --> B1["try index 1,2 unused"]
    B1 --> B2["mark[1]=T, path=[1,2]<br/>backtrack()"]
    B1 --> B3["mark[2]=T, path=[1,3]<br/>backtrack()"]
    
    B2 --> B2A["only index 2 unused<br/>mark[2]=T, path=[1,2,3]<br/>len==3, record!"]
    B3 --> B3A["only index 1 unused<br/>mark[1]=T, path=[1,3,2]<br/>len==3, record!"]
    
    C --> C1["try index 0,2 unused"]
    C1 --> C2["mark[0]=T, path=[2,1]<br/>backtrack()"]
    C1 --> C3["mark[2]=T, path=[2,3]<br/>backtrack()"]
    
    D --> D1["try index 0,1 unused"]
    D1 --> D2["mark[0]=T, path=[3,1]<br/>backtrack()"]
    D1 --> D3["mark[1]=T, path=[3,2]<br/>backtrack()"]
```

**Key insight:** Unlike subsets, at each recursion level all **unused** elements can be chosen. The `used` array prevents reuse.

## Trace Table: State at Each Recording

**Input:** `nums = [1, 2]`

| Record # | `used` Array | `path` | Depth | Notes |
|----------|--------------|--------|-------|-------|
| 1 | `[T, F]` | `[1, 2]` | 2 | Chose index 0, then index 1 |
| 2 | `[T, F]` | `[1]` | 1 | (backtrack, pop 2) |
| 2 (continue) | `[F, F]` | `[]` | 0 | (backtrack, pop 1) |
| 3 | `[F, T]` | `[2, 1]` | 2 | Chose index 1, then index 0 |

**Detailed walkthrough for `[1, 2]`:**

1. **Iteration 1**: index=0 (value 1)
   - Mark `used[0] = True`, append `1` to path → `path = [1]`
   - Recurse with `[T, F]`
     - Iteration 1: index=1 (value 2)
       - Mark `used[1] = True`, append `2` → `path = [1, 2]`
       - Recurse, depth 2 == nums.length → **record `[1, 2]`**
       - Backtrack: pop 2, mark `used[1] = False`
   - Backtrack from recursion: pop 1, mark `used[0] = False`

2. **Iteration 2**: index=1 (value 2)
   - Mark `used[1] = True`, append `2` → `path = [2]`
   - Recurse with `[F, T]`
     - Iteration 1: index=0 (value 1)
       - Mark `used[0] = True`, append `1` → `path = [2, 1]`
       - Recurse, depth 2 == nums.length → **record `[2, 1]`**
       - Backtrack: pop 1, mark `used[0] = False`
   - Backtrack from recursion: pop 2, mark `used[1] = False`

3. **Done**: Both indices exhausted at top level.

## Edge Cases

- A single-element array returns one permutation.
- Distinct elements are assumed here; duplicates require a different skip rule.
- Output size grows as `n!`, which dominates runtime quickly.
