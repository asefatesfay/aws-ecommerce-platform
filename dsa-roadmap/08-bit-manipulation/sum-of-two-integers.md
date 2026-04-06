# Sum of Two Integers

**Difficulty:** Medium
**Pattern:** Bit Manipulation
**LeetCode:** #371

## Problem Statement

Given two integers `a` and `b`, return the sum of the two integers without using the operators `+` and `-`.

## Examples

### Example 1
**Input:** `a = 1`, `b = 2`
**Output:** `3`

### Example 2
**Input:** `a = 2`, `b = 3`
**Output:** `5`

## Constraints
- `-1000 <= a, b <= 1000`

## Hints

> 💡 **Hint 1:** Think about how addition works at the bit level. When you add two bits: 0+0=0, 0+1=1, 1+0=1, 1+1=0 with carry 1. The sum without carry is XOR; the carry is AND shifted left.

> 💡 **Hint 2:** Compute `sum = a ^ b` (bits that don't produce a carry) and `carry = (a & b) << 1` (bits that produce a carry, shifted to the next position).

> 💡 **Hint 3:** Repeat with `a = sum` and `b = carry` until carry is 0. The final `a` is the answer. In Python, handle the 32-bit mask to avoid infinite loops with negative numbers.

## Approach

**Time Complexity:** O(1) — at most 32 iterations
**Space Complexity:** O(1)

Iteratively compute XOR (sum without carry) and AND shifted left (carry), using the carry as the new addend, until carry is 0.

### Visual Example: Carry Propagation

```
a = 5 (binary: 0101)
b = 3 (binary: 0011)
Expected: 5 + 3 = 8 (binary: 1000)

Iteration 1:
  a     = 0101 (5)
  b     = 0011 (3)
  a ^ b = 0110 (6, sum without carry)
  a & b = 0001 (1, bits that produce carry)
  carry = 0010 (shifted left)
  
  → a = 0110 (6), b = 0010 (2)

Iteration 2:
  a     = 0110 (6)
  b     = 0010 (2)
  a ^ b = 0100 (4, sum without carry)
  a & b = 0010 (2, bits that produce carry)
  carry = 0100 (shifted left)
  
  → a = 0100 (4), b = 0100 (4)

Iteration 3:
  a     = 0100 (4)
  b     = 0100 (4)
  a ^ b = 0000 (0, sum without carry)
  a & b = 0100 (4, bits that produce carry)
  carry = 1000 (shifted left)
  
  → a = 0000 (0), b = 1000 (8)

Iteration 4:
  a     = 0000 (0)
  b     = 1000 (8)
  a ^ b = 1000 (8, sum without carry)
  a & b = 0000 (0, no carry bits)
  carry = 0000 (shifted left)
  
  → a = 1000 (8), b = 0000 (0)

b = 0, loop ends
Result: a = 1000 (8) ✓
```

## Python Implementation

```python
def get_sum(a, b):
	mask = 0xFFFFFFFF
	max_int = 0x7FFFFFFF

	while b != 0:
		a, b = (a ^ b) & mask, ((a & b) << 1) & mask

	return a if a <= max_int else ~(a ^ mask)
```

## Typical Interview Use Cases

- Simulating addition with XOR and carry propagation
- Understanding fixed-width masking in Python for signed behavior
- Strong bit-level explanation problem with clear operator semantics

