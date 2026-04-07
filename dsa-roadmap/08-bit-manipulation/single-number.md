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

---

## 🔴 Approach 1: Brute Force (Hash Map / Frequency Counting)

**Mental Model:** Count how many times each element appears, then find the one that appears exactly once.

**Time Complexity:** O(n)
**Space Complexity:** O(n) — storing frequencies in a hash map

### Why the Brute Force Works

```python
def single_number_brute(nums):
    """
    Count frequencies of each element.
    Return the element that appears exactly once.
    Time: O(n) — iterate through all elements
    Space: O(n) — hash map stores up to n elements
    """
    freq = {}
    
    # Count occurrences of each number
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    
    # Find the number that appears exactly once
    for num, count in freq.items():
        if count == 1:
            return num
```

### Tracing Brute Force: `[4, 1, 2, 1, 2]`

```
Step 1: Count frequencies
  freq = {}
  
  num=4: freq[4] = 1 → freq = {4: 1}
  num=1: freq[1] = 1 → freq = {4: 1, 1: 1}
  num=2: freq[2] = 1 → freq = {4: 1, 1: 1, 2: 1}
  num=1: freq[1] = 2 → freq = {4: 1, 1: 2, 2: 1}
  num=2: freq[2] = 2 → freq = {4: 1, 1: 2, 2: 2}

Step 2: Find element with count == 1
  Check 4: count=1 ✓ → RETURN 4

Result: 4 ✓
```

**Problem with brute force:** We use O(n) extra space. For a problem with constraint "use constant extra space", this violates the requirement.

---

## 🟢 Approach 2: Optimal (XOR with O(1) Space)

**Mental Model:** Use XOR's cancellation property: `a ^ a = 0` and `a ^ 0 = a`. When you XOR all numbers, pairs cancel to 0, leaving only the single element.

**Time Complexity:** O(n)
**Space Complexity:** O(1) — only one variable to track the result

### Why the Optimal Approach Works

XOR truth table:
```
0 ^ 0 = 0   (both off → off)
0 ^ 1 = 1   (one on → on)
1 ^ 0 = 1   (one on → on)
1 ^ 1 = 0   (both on → off) ← cancellation!
```

Key properties:
- **Commutative:** `a ^ b = b ^ a`
- **Associative:** `(a ^ b) ^ c = a ^ (b ^ c)`
- **Self-cancellation:** `a ^ a = 0`
- **Identity:** `a ^ 0 = a`

When you XOR all elements together:
1. All paired elements (`1 ^ 1 = 0`, `2 ^ 2 = 0`) cancel out
2. The single unpaired element survives (`0 ^ 4 = 4`)

```python
def single_number(nums):
    """
    XOR all elements together.
    Pairs cancel to 0, single element remains.
    Time: O(n) — single pass
    Space: O(1) — only result variable
    """
    result = 0
    for num in nums:
        result ^= num
    return result
```

### Tracing Optimal: `[4, 1, 2, 1, 2]`

```
Step-by-step XOR operations:

result = 0

Step 1: process 4
  result = 0 ^ 4 = 4
  Binary: 000 ^ 100 = 100

Step 2: process 1
  result = 4 ^ 1 = 5
  Binary: 100 ^ 001 = 101

Step 3: process 2
  result = 5 ^ 2 = 7
  Binary: 101 ^ 010 = 111

Step 4: process 1 (duplicate!)
  result = 7 ^ 1 = 6
  Binary: 111 ^ 001 = 110
  ← This looks wrong... let me recalculate

Actually, let me use a cleaner approach. XOR is commutative & associative:
  (4 ^ 1 ^ 2 ^ 1 ^ 2)
= 4 ^ (1 ^ 1) ^ (2 ^ 2)
= 4 ^ 0 ^ 0
= 4 ✓

Bit-by-bit breakdown:
  Position 2 (4s): 1 ^ 0 ^ 0 ^ 0 ^ 0 = 1 ✓
  Position 1 (2s): 0 ^ 0 ^ 1 ^ 0 ^ 1 = 0 (cancels)
  Position 0 (1s): 0 ^ 1 ^ 0 ^ 1 ^ 0 = 0 (cancels)
  
  Result: 100 = 4 ✓
```

### Visual: Why XOR Cancels Pairs

```
Array: [2, 2, 1]

Element 2 appears twice:
  2 in binary: 010
  2 in binary: 010
  2 ^ 2 =      000 ← completely cancels to zero

Element 1 appears once:
  1 in binary: 001
  (no pair)

When we XOR all:
  2 ^ 2 ^ 1
= 0 ^ 1        (the two 2's cancel)
= 1 ✓

Result: 1 ✓
```

### Why This Works: Position-by-Position Thinking

At each bit position, count how many 1's appear:
- **For paired elements:** Each pair contributes exactly two 1's at a position → XOR (`1^1=0`)
- **For single element:** Contributes one 1 at its positions → survives in the result

```
Input: [4, 1, 2, 1, 2]
        [100, 001, 010, 001, 010]

Position 2 (value 4): count of 1's = 1 (from 4 only)    → 1 ^ 0 ^ 0 ^ 0 ^ 0 = 1 ✓
Position 1 (value 2): count of 1's = 2 (from 2 and 2)   → 0 ^ 0 ^ 1 ^ 0 ^ 1 = 0 (even, cancels)
Position 0 (value 1): count of 1's = 2 (from 1 and 1)   → 0 ^ 1 ^ 0 ^ 1 ^ 0 = 0 (even, cancels)

Result: 100 = 4 ✓
```

---

## Comparison: Brute Force vs Optimal

| Aspect | Brute Force (Hash Map) | Optimal (XOR) |
|--------|-------------|---------|
| **Time Complexity** | O(n) | O(n) |
| **Space Complexity** | **O(n)** | **O(1)** |
| **Extra Data Structures** | Hash map | None |
| **For n=30,000** | Uses ~30K entries in memory | Uses 1 variable |
| **Problem Constraint** | **Violates O(1) space** | **Satisfies all constraints** |
| **Interview Viability** | Acceptable first attempt | **Preferred — elegant & optimal** |

**Why optimal wins:** Both solve the problem in linear time, but XOR does it with zero extra space by exploiting bit-manipulation properties. This demonstrates deeper algorithmic thinking.

---

## The XOR Insight: Why It's Clever

The reason this works hinges on **parity**:
- XOR counts "odd occurrences" at each bit position
- When an element appears **exactly twice**, both bits flip from 1→0 (back to off)
- When an element appears **once**, its bit stays on
- Result: only the single element's bits remain

This is why the problem specifically requires "all elements appear exactly twice except one". If elements appeared 3 times, XOR wouldn't work—we'd need a different bit trick.

---

## Python Implementation

```python
def single_number(nums):
    result = 0
    for x in nums:
        result ^= x
    return result
```

### One-Liner (Advanced)

```python
def single_number(nums):
    from functools import reduce
    return reduce(lambda a, b: a ^ b, nums)
```

## Typical Interview Use Cases

- XOR cancellation when all duplicates appear exactly twice
- O(1) extra-space alternative to hash-map counting
- Core entry point for many bit-manipulation interview patterns

