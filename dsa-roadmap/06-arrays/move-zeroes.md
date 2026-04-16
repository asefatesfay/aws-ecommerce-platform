# Move Zeroes

**Difficulty:** Easy
**Pattern:** Two Pointers (Read/Write)
**LeetCode:** #283

## Problem Statement

Given an integer array `nums`, move all `0`s to the end of it while maintaining the relative order of the non-zero elements. You must do this in-place without making a copy of the array.

## Examples

### Example 1
**Input:** `nums = [0, 1, 0, 3, 12]`
**Output:** `[1, 3, 12, 0, 0]`
**Explanation:** The non-zero elements 1, 3, 12 maintain their relative order and are moved to the front. The two zeros are moved to the end.

### Example 2
**Input:** `nums = [0]`
**Output:** `[0]`

## Constraints
- `1 <= nums.length <= 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`

## Hints

> 💡 **Hint 1:** Think about maintaining a "write position" — a pointer that tracks where the next non-zero element should go.

> 💡 **Hint 2:** Use two pointers: one scans through the array (read pointer), one tracks the next available position for non-zero elements (write pointer). When the read pointer finds a non-zero, place it at the write pointer position.

> 💡 **Hint 3:** After placing all non-zero elements, fill the remaining positions from the write pointer to the end with zeros.

## Approach 1: Brute Force

**Time Complexity:** O(n²)
**Space Complexity:** O(n)

Create a new array, copy non-zeros, then fill zeros. Or use Python's built-in filter.

```python
def move_zeroes_brute(nums: list[int]) -> None:
    non_zeros = [x for x in nums if x != 0]
    zeros = [0] * (len(nums) - len(non_zeros))
    result = non_zeros + zeros
    for i in range(len(nums)):
        nums[i] = result[i]
```

**Downside:** Uses O(n) extra space. The problem requires in-place.

---

## Approach 2: Swap Variant (O(n), O(1) space)

Swap each non-zero element with the element at the write pointer. Fewer writes than the fill approach.

```python
def move_zeroes_swap(nums: list[int]) -> None:
    write = 0
    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write], nums[read] = nums[read], nums[write]
            write += 1
```

**Tradeoff:** More swaps than the write+fill approach when there are many zeros, but avoids the separate fill loop.

---

## Approach 3: Write + Fill — Optimal

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Write all non-zeros to the front, then fill the rest with zeros. Minimizes total writes.

### Visual Trace

```
Input: [0, 1, 0, 3, 12]

write=0
read=0: nums[0]=0 → skip
read=1: nums[1]=1 → nums[0]=1, write=1  → [1, 1, 0, 3, 12]
read=2: nums[2]=0 → skip
read=3: nums[3]=3 → nums[1]=3, write=2  → [1, 3, 0, 3, 12]
read=4: nums[4]=12 → nums[2]=12, write=3 → [1, 3, 12, 3, 12]

Fill from write=3: nums[3]=0, nums[4]=0 → [1, 3, 12, 0, 0] ✓
```

```python
def move_zeroes(nums: list[int]) -> None:
    write = 0
    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write] = nums[read]
            write += 1
    while write < len(nums):
        nums[write] = 0
        write += 1
```

### Complexity Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Extra array | O(n) | O(n) | Simple but not in-place |
| Swap | O(n) | O(1) | In-place, more swaps |
| Write + fill | O(n) | O(1) | Optimal — fewest writes |

## Typical Interview Use Cases

- In-place filtering with stable relative order
- Read/write pointer warm-up for two-pointer array questions
- Any "move all X to end" variant

