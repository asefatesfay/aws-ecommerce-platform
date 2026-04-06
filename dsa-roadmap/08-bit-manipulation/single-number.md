# Single Number

**Difficulty:** Easy
**Pattern:** Bit Manipulation / XOR
**LeetCode:** #136

## Problem Statement

Given a non-empty array of integers `nums`, every element appears twice except for one. Find that single one. You must implement a solution with linear runtime complexity and use only constant extra space.

## Examples

### Example 1
**Input:** `nums = [2, 2, 1]`
**Output:** `1`

### Example 2
**Input:** `nums = [4, 1, 2, 1, 2]`
**Output:** `4`

### Example 3
**Input:** `nums = [1]`
**Output:** `1`

## Constraints
- `1 <= nums.length <= 3 * 10^4`
- `-3 * 10^4 <= nums[i] <= 3 * 10^4`
- Every element appears exactly twice except for one element which appears exactly once

## Hints

> 💡 **Hint 1:** A HashMap counting frequencies works but uses O(n) space. Can you do it with O(1) space?

> 💡 **Hint 2:** Think about XOR. What happens when you XOR a number with itself? What about XOR with 0?

> 💡 **Hint 3:** XOR all elements together. Since `a ^ a = 0` and `a ^ 0 = a`, all pairs cancel out and only the single element remains.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

XOR all elements together. Pairs cancel to 0, and the single element XORed with 0 gives itself.

### Visual Example: XOR Cancellation

```
Input: [2, 2, 1]

XOR Truth Table:
  0 ^ 0 = 0
  0 ^ 1 = 1
  1 ^ 0 = 1
  1 ^ 1 = 0  ← pairs cancel to 0

Step-by-step XOR:
  2 in binary: 010
  2 in binary: 010
  1 in binary: 001

result = 0
result ^= 2:  000 ^ 010 = 010 (result = 2)
result ^= 2:  010 ^ 010 = 000 (result = 0, pair cancelled!)
result ^= 1:  000 ^ 001 = 001 (result = 1) ← single element remains

Output: 1 ✓

Key Insight:
  2 ^ 2 = 0  (pair cancels)
  0 ^ 1 = 1  (single element survives)
  Result: 1
```

### Visual Example: Binary Bit Cancellation

```
Input: [4, 1, 2, 1, 2]

Binary representation:
  4: 100
  1: 001
  2: 010
  1: 001
  2: 010

XOR all bits position-wise:

Position 2 (4s): 1 ^ 0 ^ 0 ^ 0 ^ 0 = 1 ✓
Position 1 (2s): 0 ^ 0 ^ 1 ^ 0 ^ 1 = 0 (cancels)
Position 0 (1s): 0 ^ 1 ^ 0 ^ 1 ^ 0 = 0 (cancels)

Result: 100 = 4 ✓

Why it works: Each bit position has exactly two 1's from pairs,
except position 2 which has one 1 from the single element 4.
```

## Python Implementation

```python
def single_number(nums):
	result = 0
	for x in nums:
		result ^= x
	return result
```

## Typical Interview Use Cases

- XOR cancellation when all duplicates appear exactly twice
- O(1) extra-space alternative to hash-map counting
- Core entry point for many bit-manipulation interview patterns

