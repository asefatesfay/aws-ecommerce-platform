# Next Permutation

**Difficulty:** Medium
**Pattern:** Array Manipulation
**LeetCode:** #31

## Problem Statement

A permutation of an array of integers is an arrangement of its members into a sequence or linear order. The next permutation of an array of integers is the next lexicographically greater permutation of its integer. If no such arrangement is possible (the array is in descending order), rearrange it as the lowest possible order (ascending order).

The replacement must be in place and use only constant extra memory.

## Examples

### Example 1
**Input:** `nums = [1, 2, 3]`
**Output:** `[1, 3, 2]`

### Example 2
**Input:** `nums = [3, 2, 1]`
**Output:** `[1, 2, 3]`
**Explanation:** Already the largest permutation, so wrap around to smallest.

### Example 3
**Input:** `nums = [1, 1, 5]`
**Output:** `[1, 5, 1]`

## Constraints
- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 100`

## Hints

> 💡 **Hint 1:** To find the next permutation, you need to make the smallest possible increase. Scan from right to left to find the first element that is smaller than its right neighbor — this is the "pivot".

> 💡 **Hint 2:** Once you find the pivot at index i, find the smallest element to its right that is still larger than nums[i]. Swap them. Now the suffix (everything after index i) is in descending order.

> 💡 **Hint 3:** Reverse the suffix after index i to make it ascending (the smallest possible arrangement for that suffix). This gives the next permutation.

## Approach 1: Brute Force (Generate All Permutations)

**Time Complexity:** O(n! × n)
**Space Complexity:** O(n!)

Generate all permutations in sorted order, find the current one, return the next.

```python
from itertools import permutations

def next_permutation_brute(nums: list[int]) -> None:
    perms = sorted(set(permutations(nums)))
    idx = perms.index(tuple(nums))
    if idx + 1 < len(perms):
        result = perms[idx + 1]
    else:
        result = perms[0]
    for i, v in enumerate(result):
        nums[i] = v
```

**Downside:** O(n!) space — completely impractical for n > 10.

---

## Approach 2: Three-Step In-Place Algorithm — Optimal

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Find the rightmost "dip" (pivot), swap with the next larger element to its right, then reverse the suffix.

### Why It Works

```
To get the next permutation (smallest increase):
1. Find the rightmost position i where nums[i] < nums[i+1]
   (the "pivot" — everything to its right is in descending order)
2. Find the smallest element to the right of i that is > nums[i]
   (swap with it to make the smallest possible increase at position i)
3. Reverse the suffix after i
   (it was descending, reversing makes it ascending = smallest arrangement)

If no pivot found (array is fully descending), reverse the whole array.
```

### Visual Trace

```
nums = [1, 3, 5, 4, 2]

Step 1 — Find pivot (rightmost dip):
  Scan right to left: 2<4? No. 4<5? Yes! → pivot at i=2 (value 5)
  Wait: nums[2]=5, nums[3]=4: 5>4, not a dip.
  nums[1]=3, nums[2]=5: 3<5 → pivot at i=1 (value 3)

Step 2 — Find smallest element > nums[1]=3 to the right of i=1:
  Suffix [5,4,2]: smallest > 3 is 4 at index 3.
  Swap nums[1] and nums[3]: [1, 4, 5, 3, 2]

Step 3 — Reverse suffix after i=1 (indices 2..4):
  [5,3,2] reversed → [2,3,5]
  Result: [1, 4, 2, 3, 5] ✓
```

```python
def next_permutation(nums: list[int]) -> None:
    n = len(nums)
    i = n - 2

    # Step 1: find rightmost pivot (nums[i] < nums[i+1])
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i >= 0:
        # Step 2: find smallest element > nums[i] in suffix
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]

    # Step 3: reverse suffix after i
    left, right = i + 1, n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
```

### Complexity Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Generate all permutations | O(n! × n) | O(n!) | Completely impractical |
| Three-step in-place | O(n) | O(1) | Optimal |

## Typical Interview Use Cases

- Lexicographic permutation transitions in-place
- Reverse-suffix and pivot-swap pattern practice
- Follow-up to permutation generation/combinatorics tasks

