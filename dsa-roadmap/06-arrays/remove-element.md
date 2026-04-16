# Remove Element

**Difficulty:** Easy
**Pattern:** Two Pointers (Read/Write)
**LeetCode:** #27

## Problem Statement

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in-place. The order of the remaining elements may be changed. Return the number of elements in `nums` that are not equal to `val`.

The judge will check the first `k` elements of `nums` (where `k` is your return value) to verify correctness. Elements beyond index `k` don't matter.

## Examples

### Example 1
**Input:** `nums = [3, 2, 2, 3]`, `val = 3`
**Output:** `2`, `nums = [2, 2, _, _]`
**Explanation:** The first 2 elements are `[2, 2]`. The underscores represent values that don't matter.

### Example 2
**Input:** `nums = [0, 1, 2, 2, 3, 0, 4, 2]`, `val = 2`
**Output:** `5`, `nums = [0, 1, 4, 0, 3, _, _, _]`
**Explanation:** 5 elements are not equal to 2. Order among them doesn't matter.

## Constraints
- `0 <= nums.length <= 100`
- `0 <= nums[i] <= 50`
- `0 <= val <= 100`

## Hints

> 💡 **Hint 1:** You need to keep all elements that are NOT equal to `val`. Think about a write pointer that only advances when you write a valid element.

> 💡 **Hint 2:** Use a single pointer `k` starting at 0. Iterate through the array; whenever `nums[i] != val`, copy `nums[i]` to `nums[k]` and increment `k`.

> 💡 **Hint 3:** The return value is `k` — the count of elements not equal to `val`. The first `k` positions of `nums` will hold those elements.

## Approach 1: Brute Force

**Time Complexity:** O(n²)
**Space Complexity:** O(n)

Build a new array excluding all occurrences of `val`, copy back.

```python
def remove_element_brute(nums: list[int], val: int) -> int:
    result = [x for x in nums if x != val]
    for i, v in enumerate(result):
        nums[i] = v
    return len(result)
```

**Downside:** Uses O(n) extra space.

---

## Approach 2: Write Pointer — Optimal

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Single pass with a write pointer. Copy every element that is NOT `val` to the front.

### Visual Trace

```
nums = [0, 1, 2, 2, 3, 0, 4, 2], val = 2

k=0
i=0: nums[0]=0 ≠ 2 → nums[0]=0, k=1
i=1: nums[1]=1 ≠ 2 → nums[1]=1, k=2
i=2: nums[2]=2 = 2 → skip
i=3: nums[3]=2 = 2 → skip
i=4: nums[4]=3 ≠ 2 → nums[2]=3, k=3
i=5: nums[5]=0 ≠ 2 → nums[3]=0, k=4
i=6: nums[6]=4 ≠ 2 → nums[4]=4, k=5
i=7: nums[7]=2 = 2 → skip

Result: nums[:5] = [0,1,3,0,4], k=5 ✓
```

```python
def remove_element(nums: list[int], val: int) -> int:
    k = 0
    for x in nums:
        if x != val:
            nums[k] = x
            k += 1
    return k
```

### Complexity Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Extra array | O(n) | O(n) | Not in-place |
| Write pointer | O(n) | O(1) | Optimal |

## Typical Interview Use Cases

- In-place removal with returned logical length
- Follow-up on unstable output ordering constraints
- Foundation for deduplication and stream-compaction patterns

