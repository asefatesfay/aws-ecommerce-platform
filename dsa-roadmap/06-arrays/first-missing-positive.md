# First Missing Positive

**Difficulty:** Hard
**Pattern:** Index as Identity / Cyclic Sort
**LeetCode:** #41

## Problem Statement

Given an unsorted integer array `nums`, return the smallest missing positive integer. You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

## Examples

### Example 1
**Input:** `nums = [1, 2, 0]`
**Output:** `3`

### Example 2
**Input:** `nums = [3, 4, -1, 1]`
**Output:** `2`

### Example 3
**Input:** `nums = [7, 8, 9, 11, 12]`
**Output:** `1`

## Constraints
- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`

## Hints

> 💡 **Hint 1:** The answer must be in the range [1, n+1] where n is the array length. Why? Because with n elements, the worst case is [1, 2, ..., n], making the answer n+1.

> 💡 **Hint 2:** Use the array itself as a hash map. The value x (if 1 ≤ x ≤ n) should be at index x-1. Rearrange elements to their "correct" positions by swapping.

> 💡 **Hint 3:** After rearranging, scan the array. The first index i where nums[i] != i+1 means i+1 is the missing positive. If all positions are correct, return n+1.

## Approach 1: Brute Force (Sorting + Set)

**Time Complexity:** O(n log n)
**Space Complexity:** O(n)

Sort the array, scan for the first missing positive.

```python
def first_missing_positive_sort(nums: list[int]) -> int:
    seen = set(nums)
    i = 1
    while i in seen:
        i += 1
    return i
```

**Downside:** O(n) extra space for the set. The problem requires O(1).

---

## Approach 2: Cyclic Sort (Index as Identity) — Optimal

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Key insight: the answer is in `[1, n+1]`. Use the array itself as a hash map — value `x` belongs at index `x-1`. Swap elements to their correct positions, then scan for the first mismatch.

### Why the Answer is in [1, n+1]

```
With n elements, the best case is [1,2,...,n] → answer is n+1.
Any other arrangement means some value in [1,n] is missing → answer ≤ n.
So we only need to check positions 0..n-1.
```

### Visual Trace

```
nums = [3, 4, -1, 1]
        0  1   2  3

Cyclic sort (place each value at its correct index):
i=0: nums[0]=3, correct=2. nums[0]≠nums[2] → swap → [-1,4,3,1]
i=0: nums[0]=-1, not in [1,4] → i++
i=1: nums[1]=4, correct=3. nums[1]≠nums[3] → swap → [-1,1,3,4]
i=1: nums[1]=1, correct=0. nums[1]≠nums[0] → swap → [1,-1,3,4]
i=1: nums[1]=-1, not in [1,4] → i++
i=2: nums[2]=3, correct=2. nums[2]==nums[2] → i++
i=3: nums[3]=4, correct=3. nums[3]==nums[3] → i++

After sort: [1, -1, 3, 4]

Scan: i=0: nums[0]=1==1 ✓. i=1: nums[1]=-1≠2 → return 2 ✓
```

```python
def first_missing_positive(nums: list[int]) -> int:
    n = len(nums)
    i = 0

    # Place each value at its correct index
    while i < n:
        x = nums[i]
        correct = x - 1
        if 1 <= x <= n and nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            i += 1

    # Find first position where value doesn't match
    for i, x in enumerate(nums):
        if x != i + 1:
            return i + 1

    return n + 1
```

### Complexity Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Set | O(n) | O(n) | Simple but uses extra space |
| Sort + scan | O(n log n) | O(1) | Modifies array, too slow |
| Cyclic sort | O(n) | O(1) | Optimal |

## Typical Interview Use Cases

- O(n) + O(1) constraints forcing index-as-hash/cyclic placement
- Missing smallest positive / first missing index-style questions
- Strong example of in-place value-to-index mapping

