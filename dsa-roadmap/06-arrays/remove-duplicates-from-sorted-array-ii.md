# Remove Duplicates from Sorted Array II

**Difficulty:** Medium
**Pattern:** Two Pointers (Read/Write)
**LeetCode:** #80

## Problem Statement

Given an integer array `nums` sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. Return the number of elements `k` in the modified array. The first `k` elements should hold the result.

## Examples

### Example 1
**Input:** `nums = [1, 1, 1, 2, 2, 3]`
**Output:** `5`, `nums = [1, 1, 2, 2, 3, _]`
**Explanation:** Each element appears at most twice. 1 appears twice, 2 appears twice, 3 appears once.

### Example 2
**Input:** `nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]`
**Output:** `7`, `nums = [0, 0, 1, 1, 2, 3, 3, _, _]`

## Constraints
- `1 <= nums.length <= 3 * 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` is sorted in non-decreasing order

## Hints

> 💡 **Hint 1:** This is a generalization of "Remove Duplicates I". Instead of allowing 1 occurrence, you allow 2. Think about how to adapt the write pointer logic.

> 💡 **Hint 2:** Use a write pointer `k` starting at 2 (the first two elements are always valid). For each element at index i ≥ 2, compare it with the element at position `k-2` (two positions behind the write pointer).

> 💡 **Hint 3:** If `nums[i] != nums[k-2]`, the current element is safe to include (it can't be a third duplicate). Write it to position `k` and advance `k`. This works because the array is sorted.

## Approach 1: Brute Force

**Time Complexity:** O(n)
**Space Complexity:** O(n)

Count occurrences with a Counter, rebuild the array keeping at most 2 of each.

```python
from collections import Counter

def remove_duplicates_brute(nums: list[int]) -> int:
    result = []
    for num, cnt in sorted(Counter(nums).items()):
        result.extend([num] * min(cnt, 2))
    for i, v in enumerate(result):
        nums[i] = v
    return len(result)
```

**Downside:** O(n) extra space.

---

## Approach 2: Write Pointer with k-2 Lookback — Optimal

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Start write pointer at 2 (first two elements always valid). For each new element, compare it with `nums[k-2]` — if different, it can't be a third duplicate.

### Why `k-2` Works

```
In a sorted array, if nums[i] == nums[k-2], then:
  nums[k-2] == nums[k-1] == nums[i]
  → nums[i] would be the 3rd occurrence → skip it.

If nums[i] != nums[k-2], it's safe to include
  (it's either a new value or only the 2nd occurrence).
```

### Visual Trace

```
nums = [1, 1, 1, 2, 2, 3]

k=2 (first two elements [1,1] are always valid)
i=2: nums[2]=1 == nums[k-2]=nums[0]=1 → skip (3rd occurrence of 1)
i=3: nums[3]=2 ≠ nums[k-2]=nums[1]=1 → nums[2]=2, k=3
i=4: nums[4]=2 ≠ nums[k-2]=nums[2]=2? No, 2==2 → skip? 
     Wait: nums[k-2]=nums[1]=1 ≠ 2 → nums[3]=2, k=4
     (k was 3 after previous step, so k-2=1, nums[1]=1 ≠ 2 → include)
i=5: nums[5]=3 ≠ nums[k-2]=nums[2]=2 → nums[4]=3, k=5

Result: nums[:5] = [1,1,2,2,3], k=5 ✓
```

```python
def remove_duplicates(nums: list[int]) -> int:
    n = len(nums)
    if n <= 2:
        return n
    k = 2
    for i in range(2, n):
        if nums[i] != nums[k - 2]:
            nums[k] = nums[i]
            k += 1
    return k
```

### Generalization: Keep at Most `m` Duplicates

```python
def remove_duplicates_k(nums: list[int], m: int) -> int:
    """Keep at most m occurrences of each element."""
    k = 0
    for num in nums:
        if k < m or nums[k - m] != num:
            nums[k] = num
            k += 1
    return k
# m=1 → Remove Duplicates I
# m=2 → Remove Duplicates II
```

### Complexity Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Counter + rebuild | O(n) | O(n) | Not in-place |
| Write pointer (k-2) | O(n) | O(1) | Optimal |

## Typical Interview Use Cases

- Variant where each value can appear at most twice
- Extending sorted-array dedupe from 1 copy to k copies
- Pointer logic proofs using local window checks

