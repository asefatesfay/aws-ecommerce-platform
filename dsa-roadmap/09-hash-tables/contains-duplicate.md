# Contains Duplicate

**Difficulty:** Easy
**Pattern:** Hash Set
**LeetCode:** #217

## Problem Statement

Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

## Examples

### Example 1
**Input:** `nums = [1, 2, 3, 1]`
**Output:** `true`

### Example 2
**Input:** `nums = [1, 2, 3, 4]`
**Output:** `false`

### Example 3
**Input:** `nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]`
**Output:** `true`

## Constraints
- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Hints

> 💡 **Hint 1:** You need to detect if any element has been seen before. What data structure gives O(1) membership testing?

> 💡 **Hint 2:** Use a HashSet. For each element, check if it's already in the set. If yes, return true. If no, add it to the set.

> 💡 **Hint 3:** Alternatively, sort the array and check adjacent elements. But that's O(n log n) — the HashSet approach is O(n).

---

## 🔴 Approach 1: Brute Force (Nested Loop)

**Mental Model:** Compare every element with every other element to find a duplicate.

**Time Complexity:** O(n²)
**Space Complexity:** O(1)

### Why the Brute Force Works

```python
def contains_duplicate_brute(nums):
    """
    Check if nums[i] == nums[j] for any i != j.
    Time: O(n²) — two nested loops
    Space: O(1) — no extra data structures
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False
```

### Tracing Brute Force: `[1, 2, 3, 1]`

```
i=0, nums[i]=1:
  j=1, nums[j]=2: 1 != 2 ✗
  j=2, nums[j]=3: 1 != 3 ✗
  j=3, nums[j]=1: 1 == 1 ✓ → RETURN True

Result: true ✓
```

**Problem with brute force:** For every element, we compare it against all remaining elements. With n=10⁵, this is 10¹⁰ comparisons—way too slow.

---

## 🟢 Approach 2: Optimal (Hash Set)

**Mental Model:** Keep track of elements you've seen. When you encounter an element already in the set, you've found a duplicate.

**Time Complexity:** O(n)
**Space Complexity:** O(n)

### Why the Optimal Approach Works

HashSet gives **O(1) lookup**. So instead of checking against all previous elements (O(n) per check), we just ask: "Have I seen this before?" and get an instant answer.

```python
def contains_duplicate(nums):
    """
    Use a HashSet to track seen elements.
    Return True at first duplicate.
    Time: O(n) — single pass
    Space: O(n) — storing up to n unique elements
    """
    seen = set()
    for num in nums:
        if num in seen:      # O(1) lookup
            return True
        seen.add(num)        # O(1) insertion
    return False
```

### Tracing Optimal: `[1, 2, 3, 1]`

```
Initial: seen = {}

num=1:
  1 in seen? No
  seen.add(1) → seen = {1}

num=2:
  2 in seen? No
  seen.add(2) → seen = {1, 2}

num=3:
  3 in seen? No
  seen.add(3) → seen = {1, 2, 3}

num=1:
  1 in seen? Yes ✓ → RETURN True

Result: true ✓
```

### Why O(1) Lookup Is So Powerful

| Operation | Array Check (linear) | Hash Set (O(1)) |
|-----------|----------------------|-----------------|
| Check if `1` in `[1,2,3,1]` | Scan elements: 1 check | Instant hash lookup |
| Check each of n elements | n × n/2 = O(n²) | n × 1 = O(n) |

---

## Comparison: Brute Force vs Optimal

| Aspect | Brute Force | Optimal |
|--------|-----------|---------|
| **Time Complexity** | **O(n²)** | **O(n)** |
| **Space Complexity** | O(1) | O(n) |
| **For n=1000** | ~500K ops | ~1K ops |
| **For n=10⁵** | ~5 billion ops (**too slow**) | ~100K ops ✓ |
| **Why it works** | Exhaustive comparison | Hash set instant lookups |
| **Trade-off** | Speed for space | Use memory to save time |

**Why optimal wins:** Linear time beats quadratic by a massive margin. The extra O(n) space is worth it for the dramatic speed improvement.

---

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(n)

Add elements to a HashSet one by one. Return true as soon as a duplicate is found (element already in set). Return false if the loop completes.

## Python Implementation

```python
def contains_duplicate(nums):
    return len(nums) != len(set(nums))
    
    # Or, as one-liner with explicit set:
    # seen = set()
    # for num in nums:
    #     if num in seen:
    #         return True
    #     seen.add(num)
    # return False
```
