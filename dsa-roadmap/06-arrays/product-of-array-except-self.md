# Product of Array Except Self

**Difficulty:** Medium
**Pattern:** Prefix/Suffix Products
**LeetCode:** #238

## Problem Statement

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`. The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer. You must write an algorithm that runs in O(n) time and without using the division operation.

## Examples

### Example 1
**Input:** `nums = [1, 2, 3, 4]`
**Output:** `[24, 12, 8, 6]`
**Explanation:** answer[0] = 2*3*4=24, answer[1] = 1*3*4=12, answer[2] = 1*2*4=8, answer[3] = 1*2*3=6.

### Example 2
**Input:** `nums = [-1, 1, 0, -3, 3]`
**Output:** `[0, 0, 9, 0, 0]`

## Constraints
- `2 <= nums.length <= 10^5`
- `-30 <= nums[i] <= 30`
- The product of any prefix or suffix fits in a 32-bit integer

## Hints

> 💡 **Hint 1:** For each position i, the answer is (product of all elements to the left of i) × (product of all elements to the right of i).

> 💡 **Hint 2:** Precompute a prefix product array and a suffix product array. Then answer[i] = prefix[i-1] * suffix[i+1].

> 💡 **Hint 3:** To achieve O(1) extra space (excluding output), do two passes over the output array: first fill it with prefix products (left to right), then multiply in suffix products (right to left) using a running variable.

## Approach 1: Brute Force (Division)

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Compute total product, divide by each element. Fails when zeros are present.

```python
from math import prod

def product_except_self_brute(nums: list[int]) -> list[int]:
    total = prod(nums)
    # Fails if any element is 0 (division by zero)
    return [total // x for x in nums]
```

**Problems:** Division not allowed per problem constraints; fails with zeros.

---

## Approach 2: Prefix + Suffix Arrays

**Time Complexity:** O(n)
**Space Complexity:** O(n)

Build explicit prefix and suffix product arrays, multiply them.

```python
def product_except_self_arrays(nums: list[int]) -> list[int]:
    n = len(nums)
    prefix = [1] * n
    suffix = [1] * n

    for i in range(1, n):
        prefix[i] = prefix[i - 1] * nums[i - 1]
    for i in range(n - 2, -1, -1):
        suffix[i] = suffix[i + 1] * nums[i + 1]

    return [prefix[i] * suffix[i] for i in range(n)]
```

---

## Approach 3: Two-Pass with Running Variable — Optimal

**Time Complexity:** O(n)
**Space Complexity:** O(1) extra

Use the output array itself to store prefix products, then multiply in suffix products using a running variable.

### Visual Trace

```
nums = [1, 2, 3, 4]

Pass 1 (prefix into output):
  out[0]=1 (prefix=1), prefix=1
  out[1]=1 (prefix=1), prefix=2
  out[2]=2 (prefix=2), prefix=6
  out[3]=6 (prefix=6), prefix=24
  out = [1, 1, 2, 6]

Pass 2 (multiply suffix from right):
  i=3: out[3]*=suffix(1)=6,  suffix*=4=4
  i=2: out[2]*=suffix(4)=8,  suffix*=3=12
  i=1: out[1]*=suffix(12)=12, suffix*=2=24
  i=0: out[0]*=suffix(24)=24, suffix*=1=24
  out = [24, 12, 8, 6] ✓
```

```python
def product_except_self(nums: list[int]) -> list[int]:
    n = len(nums)
    out = [1] * n

    prefix = 1
    for i in range(n):
        out[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        out[i] *= suffix
        suffix *= nums[i]

    return out
```

### Complexity Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Division | O(n) | O(1) | Fails with zeros, not allowed |
| Prefix + suffix arrays | O(n) | O(n) | Clear but uses extra space |
| Two-pass running variable | O(n) | O(1) | Optimal |

## Typical Interview Use Cases

- Prefix/suffix decomposition without division
- O(1) auxiliary-space follow-up handling
- Core pattern reused in many left-right accumulation problems

