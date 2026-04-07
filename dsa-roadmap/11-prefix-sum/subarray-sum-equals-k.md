# Subarray Sum Equals K

**Difficulty:** Medium
**Pattern:** Prefix Sum + Hash Map
**LeetCode:** #560

## Problem Statement

Given an array of integers `nums` and an integer `k`, return the total number of subarrays whose sum equals to `k`.

## Examples

### Example 1
**Input:** `nums = [1, 1, 1]`, `k = 2`
**Output:** `2`
**Explanation:** [1,1] at indices (0,1) and (1,2).

### Example 2
**Input:** `nums = [1, 2, 3]`, `k = 3`
**Output:** `2`
**Explanation:** [3] and [1,2].

## Constraints
- `1 <= nums.length <= 2 * 10^4`
- `-1000 <= nums[i] <= 1000`
- `-10^7 <= k <= 10^7`

## Hints

> 💡 **Hint 1:** A subarray sum from index l to r equals `prefix[r] - prefix[l-1]`. You want this to equal k, so you need `prefix[r] - k` to have appeared as a prefix sum before.

> 💡 **Hint 2:** Use a HashMap to count how many times each prefix sum has been seen. Initialize with `{0: 1}` (empty prefix sum of 0 appears once).

> 💡 **Hint 3:** For each index, compute the running prefix sum. Add `map[prefix_sum - k]` to the count (number of valid left endpoints). Then increment `map[prefix_sum]`.

---

## 🔴 Approach 1: Brute Force (All Subarrays)

**Mental Model:** Check every possible subarray `[l, r]` and compute its sum. Count how many equal k.

**Time Complexity:** O(n²)
**Space Complexity:** O(1)

### Why the Brute Force Works

```python
def subarray_sum_brute(nums, k):
    """
    For each starting position l, check all ending positions r.
    Compute subarray sum and check if it equals k.
    Time: O(n²) — two nested loops
    Space: O(1) — no extra structures
    """
    count = 0
    n = len(nums)
    
    for l in range(n):
        subarray_sum = 0
        for r in range(l, n):
            subarray_sum += nums[r]  # Extend subarray
            if subarray_sum == k:
                count += 1
    
    return count
```

### Tracing Brute Force: `[1, 1, 1]`, `k = 2`

```
l=0:
  r=0: sum = 1, 1 != 2 ✗
  r=1: sum = 1 + 1 = 2, 2 == 2 ✓ → count = 1
  r=2: sum = 2 + 1 = 3, 3 != 2 ✗

l=1:
  r=1: sum = 1, 1 != 2 ✗
  r=2: sum = 1 + 1 = 2, 2 == 2 ✓ → count = 2

l=2:
  r=2: sum = 1, 1 != 2 ✗

Result: count = 2 ✓ (subarrays: [1,1] at 0-1 and [1,1] at 1-2)
```

**Problem with brute force:** O(n²) is too slow for n=20,000. We're recomputing sums inefficiently.

---

## 🟢 Approach 2: Optimal (Prefix Sum + Hash Map)

**Mental Model:** Use the prefix sum **difference formula**: 
- If `prefix[r] - prefix[l-1] = k`, then the subarray `[l, r]` sums to k
- Rearranged: `prefix[l-1] = prefix[r] - k`
- So for each `prefix[r]`, count how many times `prefix[r] - k` has been seen

**Time Complexity:** O(n)
**Space Complexity:** O(n)

### Why the Optimal Approach Works

Key insight: Instead of checking all subarrays, use a **running prefix sum** and a **hash map** to count valid left endpoints instantly.

```python
def subarray_sum(nums, k):
    """
    Use prefix sum and hash map.
    For each position r, count how many previous positions l make sum[l:r+1] == k.
    Time: O(n) — single pass
    Space: O(n) — hash map stores prefix sums
    """
    prefix_sum = 0
    prefix_count = {0: 1}  # Base case: empty prefix sum is 0
    result = 0
    
    for num in nums:
        prefix_sum += num
        
        # How many times have we seen (prefix_sum - k)?
        # If we have, those are valid left endpoints for subarrays ending here
        if prefix_sum - k in prefix_count:
            result += prefix_count[prefix_sum - k]
        
        # Record this prefix sum
        prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1
    
    return result
```

### Tracing Optimal: `[1, 1, 1]`, `k = 2`

```
Initial: prefix_sum = 0, prefix_count = {0: 1}, result = 0

Index 0, num=1:
  prefix_sum = 0 + 1 = 1
  prefix_sum - k = 1 - 2 = -1
  -1 in prefix_count? No
  result = 0
  prefix_count[1] = 1 → {0: 1, 1: 1}

Index 1, num=1:
  prefix_sum = 1 + 1 = 2
  prefix_sum - k = 2 - 2 = 0
  0 in prefix_count? Yes, count = 1 ✓
  result = 0 + 1 = 1
  prefix_count[2] = 1 → {0: 1, 1: 1, 2: 1}

Index 2, num=1:
  prefix_sum = 2 + 1 = 3
  prefix_sum - k = 3 - 2 = 1
  1 in prefix_count? Yes, count = 1 ✓
  result = 1 + 1 = 2
  prefix_count[3] = 1 → {0: 1, 1: 1, 2: 1, 3: 1}

Result: 2 ✓
```

### Visual: Understanding Prefix Sum Difference

```
Array: [1, 1, 1], k = 2

Prefix sums:
  Index:  -1    0    1    2
  Value:   0    1    2    3
  Prefix:  0   [1]  [1,1] [1,1,1]

For a subarray sum from index l to r:
  subarray_sum[l, r] = prefix[r] - prefix[l-1]

  Example: subarray [1,1] at indices 0-1:
  sum = prefix[1] - prefix[-1] = 2 - 0 = 2 ✓

When we're at index r=1 (prefix=2), we ask:
  "For sum to equal k=2, what prefix_sum do we need before this?"
  prefix[l-1] = prefix[r] - k = 2 - 2 = 0
  "Have we seen 0 before?" Yes! (at the start, {0: 1})
  "So there's 1 subarray ending here that sums to 2" ✓
```

### Why Hash Map Matters

Without it, we'd need to check all previous prefixes for each current position (O(n²) again).
With it, O(1) lookup tells us instantly how many times a target prefix appeared.

---

## Comparison: Brute Force vs Optimal

| Aspect | Brute Force | Optimal |
|--------|-----------|---------|
| **Time Complexity** | **O(n²)** | **O(n)** |
| **Space Complexity** | O(1) | O(n) |
| **For n=100** | ~5K ops | ~100 ops |
| **For n=20,000** | **~400M ops (slow)** | ~20K ops ✓ |
| **Algorithm** | Try all subarrays | Running prefix + hash map |
| **Key Technique** | Brute enumeration | Prefix difference lookup |

**Why optimal wins:** Hash map lets us do in O(n) what would otherwise be O(n²). The space trade-off is well worth it.

---

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(n)

Running prefix sum with a HashMap counting occurrences. For each prefix sum p, add the count of (p - k) from the map to the answer, then record p in the map.

## Python Implementation

```python
def subarray_sum(nums, k):
    prefix_sum = 0
    prefix_count = {0: 1}
    result = 0
    
    for num in nums:
        prefix_sum += num
        if prefix_sum - k in prefix_count:
            result += prefix_count[prefix_sum - k]
        prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1
    
    return result
```
