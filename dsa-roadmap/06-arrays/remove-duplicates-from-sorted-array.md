# Remove Duplicates from Sorted Array

**Difficulty:** Easy
**Pattern:** Two Pointers (Read/Write)
**LeetCode:** #26

## Problem Statement

Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. Return the number of unique elements `k`. The first `k` elements of `nums` should hold the unique elements in order.

## Examples

### Example 1
**Input:** `nums = [1, 1, 2]`
**Output:** `2`, `nums = [1, 2, _]`
**Explanation:** Two unique elements: 1 and 2.

### Example 2
**Input:** `nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]`
**Output:** `5`, `nums = [0, 1, 2, 3, 4, _, _, _, _, _]`
**Explanation:** Five unique elements: 0, 1, 2, 3, 4.

## Constraints
- `1 <= nums.length <= 3 * 10^4`
- `-100 <= nums[i] <= 100`
- `nums` is sorted in non-decreasing order

## Hints

> 💡 **Hint 1:** Since the array is sorted, all duplicates of a value are adjacent. You only need to keep the first occurrence of each value.

> 💡 **Hint 2:** Use a write pointer `k` starting at 1 (the first element is always unique). Scan from index 1; whenever `nums[i] != nums[i-1]`, it's a new unique value — write it to position `k`.

> 💡 **Hint 3:** The condition `nums[i] != nums[k-1]` (comparing with the last written value) is equivalent and slightly cleaner. Advance `k` each time you write.

## Approach 1: Brute Force

**Time Complexity:** O(n)
**Space Complexity:** O(n)

Collect unique elements into a set, sort, copy back.

```python
def remove_duplicates_brute(nums: list[int]) -> int:
    unique = sorted(set(nums))
    for i, v in enumerate(unique):
        nums[i] = v
    return len(unique)
```

**Downside:** Uses O(n) extra space. The problem requires O(1).

---

## Approach 2: Write Pointer — Optimal

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Since the array is sorted, duplicates are adjacent. Keep a write pointer; advance it only when a new unique value is found.

### Visual Trace

```
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

k=1 (first element always kept)
i=1: nums[1]=0 == nums[0]=0 → skip
i=2: nums[2]=1 ≠ nums[1]=0 → nums[1]=1, k=2
i=3: nums[3]=1 == nums[2]=1 → skip
i=4: nums[4]=1 == nums[2]=1 → skip
i=5: nums[5]=2 ≠ nums[2]=1 → nums[2]=2, k=3
i=6: nums[6]=2 == nums[3]=2 → skip
i=7: nums[7]=3 ≠ nums[3]=2 → nums[3]=3, k=4
i=8: nums[8]=3 == nums[4]=3 → skip
i=9: nums[9]=4 ≠ nums[4]=3 → nums[4]=4, k=5

Result: nums[:5] = [0,1,2,3,4], k=5 ✓
```

```python
def remove_duplicates(nums: list[int]) -> int:
    if not nums:
        return 0
    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[k - 1]:
            nums[k] = nums[i]
            k += 1
    return k
```

### Complexity Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Set + sort | O(n log n) | O(n) | Not in-place |
| Write pointer | O(n) | O(1) | Optimal |

## Typical Interview Use Cases

- Sorted array deduplication with O(1) extra space
- Building intuition for write-pointer correctness invariants
- Basis for "keep at most k duplicates" generalization

