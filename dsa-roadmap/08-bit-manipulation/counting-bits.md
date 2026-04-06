# Counting Bits

**Difficulty:** Easy
**Pattern:** Bit Manipulation / Dynamic Programming
**LeetCode:** #338

## Problem Statement

Given an integer `n`, return an array `ans` of length `n + 1` such that for each `i` (0 <= i <= n), `ans[i]` is the number of `1`'s in the binary representation of `i`.

## Examples

### Example 1
**Input:** `n = 2`
**Output:** `[0, 1, 1]`
**Explanation:** 0→0 bits, 1→1 bit, 2→1 bit.

### Example 2
**Input:** `n = 5`
**Output:** `[0, 1, 1, 2, 1, 2]`
**Explanation:** 0→0, 1→1, 2→1, 3→2, 4→1, 5→2.

## Constraints
- `0 <= n <= 10^5`

## Hints

> 💡 **Hint 1:** You could call a popcount function for each number, but that's O(n log n). Can you use previously computed results?

> 💡 **Hint 2:** Notice that `i` and `i >> 1` (i divided by 2) differ by at most one bit — the lowest bit. So `popcount(i) = popcount(i >> 1) + (i & 1)`.

> 💡 **Hint 3:** Build the answer array from 0 to n using this recurrence: `ans[i] = ans[i >> 1] + (i & 1)`. Each answer depends only on a previously computed value.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(n) for the output array

DP with the recurrence `ans[i] = ans[i >> 1] + (i & 1)`. Right-shifting removes the lowest bit, and we add back whether that bit was set.

## Python Implementation

```python
def count_bits(n):
	ans = [0] * (n + 1)
	for i in range(1, n + 1):
		ans[i] = ans[i >> 1] + (i & 1)
	return ans
```

## Typical Interview Use Cases

- DP over binary representations
- Reusing smaller subproblems via right shift
- Common precursor to bitmask DP and subset-state reasoning

