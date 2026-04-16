# Subarray Sum Equals K

**Difficulty:** Medium
**Pattern:** Prefix Sum + Hash Map
**LeetCode:** #560
**Asked by:** Google, Microsoft, Adobe, Facebook

## Problem Statement

Given an array of integers `nums` and an integer `k`, return the total number of subarrays whose sum equals `k`.

## Examples

### Example 1
**Input:** `nums = [1, 1, 1]`, `k = 2`
**Output:** `2`
**Explanation:** Subarrays `[1,1]` at indices `[0,1]` and `[1,2]` both sum to 2.

### Example 2
**Input:** `nums = [1, 2, 3]`, `k = 3`
**Output:** `2`
**Explanation:** Subarrays `[3]` (index 2) and `[1,2]` (indices 0-1) both sum to 3.

### Example 3
**Input:** `nums = [1, -1, 1, -1]`, `k = 0`
**Output:** `4`
**Explanation:** `[1,-1]`, `[-1,1]`, `[1,-1,1,-1]`, `[-1,1,-1,1]` — wait, let's count:
Subarrays summing to 0: `[1,-1]`(0-1), `[-1,1]`(1-2), `[1,-1]`(2-3), `[1,-1,1,-1]`(0-3) = 4.

## Constraints
- `1 <= nums.length <= 2 * 10^4`
- `-1000 <= nums[i] <= 1000`
- `-10^7 <= k <= 10^7`

## Hints

> 💡 **Hint 1:** A subarray sum `sum(i, j)` = `prefix[j+1] - prefix[i]`. So we need pairs where `prefix[j+1] - prefix[i] = k`, i.e., `prefix[i] = prefix[j+1] - k`.

> 💡 **Hint 2:** As you compute prefix sums left to right, for each new prefix sum `p`, check how many previous prefix sums equal `p - k`. That count is the number of subarrays ending here with sum k.

> 💡 **Hint 3:** Initialize the map with `{0: 1}` to handle subarrays starting from index 0 (where the prefix sum itself equals k).

## Approach 1: Brute Force

**Time Complexity:** O(n²)
**Space Complexity:** O(1)

Check every subarray, count those with sum == k.

```python
def subarray_sum_brute(nums: list[int], k: int) -> int:
    count = 0
    n = len(nums)
    for i in range(n):
        total = 0
        for j in range(i, n):
            total += nums[j]
            if total == k:
                count += 1
    return count
```

**Why it's slow:** O(n²) — misses the opportunity to reuse prefix sum information.

---

## Approach 2: Prefix Sum Array (O(n²) with O(n) space)

Precompute prefix sums, then check all pairs. Still O(n²) but shows the prefix sum idea.

```python
def subarray_sum_prefix(nums: list[int], k: int) -> int:
    n = len(nums)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]

    count = 0
    for i in range(n + 1):
        for j in range(i + 1, n + 1):
            if prefix[j] - prefix[i] == k:
                count += 1
    return count
```

---

## Approach 3: Hash Map — Optimal

**Time Complexity:** O(n)
**Space Complexity:** O(n)

Key insight: `sum(i..j) = prefix[j+1] - prefix[i] = k` → we need `prefix[i] = prefix[j+1] - k`. As we compute prefix sums, check how many times `running - k` has appeared before.

### Why `{0: 1}` is Needed

```
nums = [3], k = 3
Without {0:1}: running=3, look for 3-3=0 → not in map → count=0. WRONG.
With {0:1}:    running=3, look for 3-3=0 → found 1 time → count=1. CORRECT.

{0:1} represents the empty prefix (before index 0).
```

### Visual Trace

```
nums = [1, 1, 1], k = 2
prefix_count = {0: 1}

i=0: running=1. Look for 1-2=-1 → 0. count=0. Store {0:1, 1:1}
i=1: running=2. Look for 2-2=0 → 1. count=1. Store {0:1, 1:1, 2:1}
i=2: running=3. Look for 3-2=1 → 1. count=2. Store {0:1, 1:1, 2:1, 3:1}

Answer: 2 ✓  (subarrays [1,1] at [0,1] and [1,2])
```

```python
from collections import defaultdict

def subarray_sum(nums: list[int], k: int) -> int:
    prefix_count = defaultdict(int)
    prefix_count[0] = 1  # empty prefix
    running = 0
    count = 0

    for num in nums:
        running += num
        count += prefix_count[running - k]
        prefix_count[running] += 1

    return count
```

### Complexity Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute force | O(n²) | O(1) | Try all subarrays |
| Prefix array + pairs | O(n²) | O(n) | Shows prefix idea, still slow |
| Hash map | O(n) | O(n) | Optimal — one pass |

## Follow-up: Subarray Sum Divisible by K — #974 (Google)

Count subarrays whose sum is divisible by k.

```python
def subarrays_div_by_k(nums: list[int], k: int) -> int:
    """
    nums=[4,5,0,-2,-3,1], k=5 → 7
    
    Key insight: prefix[j] - prefix[i] divisible by k
    ↔ prefix[j] % k == prefix[i] % k
    """
    remainder_count = defaultdict(int)
    remainder_count[0] = 1
    running = 0
    count = 0

    for num in nums:
        running = (running + num) % k
        if running < 0:
            running += k  # handle negative remainders in Python
        count += remainder_count[running]
        remainder_count[running] += 1

    return count
```

## Follow-up: Continuous Subarray Sum — #523 (Microsoft)

Check if there's a subarray of length >= 2 whose sum is a multiple of k.

```python
def check_subarray_sum(nums: list[int], k: int) -> bool:
    """
    nums=[23,2,4,6,7], k=6 → True ([2,4] sums to 6)
    nums=[23,2,6,4,7], k=6 → True ([23,2,6,4,7] sums to 42)
    """
    # Store {remainder: first_index_where_this_remainder_appeared}
    seen = {0: -1}  # remainder 0 seen before index 0
    running = 0
    for i, num in enumerate(nums):
        running = (running + num) % k
        if running in seen:
            if i - seen[running] >= 2:  # subarray length >= 2
                return True
        else:
            seen[running] = i
    return False
```

## Typical Interview Use Cases

- Very common at Google/Microsoft — tests prefix sum + hash map pattern
- The `{0:1}` initialization is a classic interview trick
- Foundation for all "count subarrays with property" problems
