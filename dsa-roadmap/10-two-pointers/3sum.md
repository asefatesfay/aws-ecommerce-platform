# 3Sum

**Difficulty:** Medium
**Pattern:** Two Pointers + Sorting
**LeetCode:** #15

## Problem Statement

Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`. Notice that the solution set must not contain duplicate triplets.

## Examples

### Example 1
**Input:** `nums = [-1, 0, 1, 2, -1, -4]`
**Output:** `[[-1,-1,2],[-1,0,1]]`

### Example 2
**Input:** `nums = [0, 1, 1]`
**Output:** `[]`

### Example 3
**Input:** `nums = [0, 0, 0]`
**Output:** `[[0,0,0]]`

## Constraints
- `3 <= nums.length <= 3000`
- `-10^5 <= nums[i] <= 10^5`

## Hints

> 💡 **Hint 1:** Sort the array first. This enables two-pointer and easy duplicate skipping.

> 💡 **Hint 2:** Fix the first element with an outer loop (index i). For the remaining subarray, use two pointers to find pairs that sum to `-nums[i]`.

> 💡 **Hint 3:** Skip duplicates: if `nums[i] == nums[i-1]`, skip (same first element). After finding a valid triplet, skip duplicate values for both left and right pointers before continuing.

---

## 🔴 Approach 1: Brute Force (Triple Nested Loop)

**Mental Model:** Try every possible triplet `(i, j, k)` where `i < j < k` and check if their sum equals zero.

**Time Complexity:** O(n³)
**Space Complexity:** O(1) (excluding output)

### Why the Brute Force Works

```python
def three_sum_brute(nums):
    """
    Try every possible triplet combination.
    Time: O(n³) — three nested loops
    Space: O(1) — no extra structures
    """
    result = []
    n = len(nums)
    
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    if triplet not in result:  # avoid duplicates
                        result.append(triplet)
    
    return [list(t) for t in result]
```

### Tracing Brute Force: `[-1, 0, 1, 2, -1, -4]`

```
i=0 (nums[i]=-1):
  j=1 (nums[j]=0):
    k=2 (nums[k]=1): -1 + 0 + 1 = 0 ✓ → add [-1, 0, 1]
    k=3 (nums[k]=2): -1 + 0 + 2 = 1 ✗
    k=4 (nums[k]=-1): -1 + 0 + (-1) = -2 ✗
    k=5 (nums[k]=-4): -1 + 0 + (-4) = -5 ✗
  j=2 (nums[j]=1):
    k=3, 4, 5 ... (checking all)
  ... and so on for all combinations

Result after dedup: [[-1, 0, 1], [-1, -1, 2], ...]
```

**Problem with brute force:** With n=3000, we have 3000³ ≈ 27 billion comparisons. Plus duplicate checking adds overhead. This is far too slow.

---

## 🟢 Approach 2: Optimal (Sort + Two Pointers)

**Mental Model:** 
1. Sort the array so we can use two pointers
2. Fix one element as the "first" of the triplet
3. Use two pointers on the remaining sorted elements to find the other two
4. Skip duplicates at each level to avoid duplicate triplets

**Time Complexity:** O(n²)
**Space Complexity:** O(1) (excluding output)

### Why the Optimal Approach Works

By sorting, we can:
- Use **two pointers** to find pairs in O(n) instead of checking all O(n²) combinations
- **Skip duplicates** naturally by comparing with previous/next elements
- **Get early termination** when values are too large (sum > 0)

```python
def three_sum(nums):
    """
    Sort first, then use two pointers for each fixed element.
    Time: O(n²) — sort O(n log n) + outer loop O(n) × two pointers O(n)
    Space: O(1) — only pointer variables
    """
    nums.sort()
    result = []
    n = len(nums)
    
    for i in range(n - 2):
        # Early termination: if smallest remaining numbers are positive, no triplet possible
        if nums[i] > 0:
            break
        
        # Skip duplicate first elements
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        # Two pointers on the rest
        left, right = i + 1, n - 1
        target = -nums[i]
        
        while left < right:
            current_sum = nums[left] + nums[right]
            
            if current_sum == target:
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicate left values
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # Skip duplicate right values
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1  # Need larger sum
            else:
                right -= 1  # Need smaller sum
    
    return result
```

### Tracing Optimal: `[-1, 0, 1, 2, -1, -4]`

```
Step 1: Sort
  nums = [-4, -1, -1, 0, 1, 2]
  Indices: 0   1   2  3  4  5

Step 2: Fix each first element
  
  i=0, nums[i]=-4, target=4:
    left=1 (-1), right=5 (2): -1 + 2 = 1 < 4 → left++
    left=2 (-1), right=5 (2): -1 + 2 = 1 < 4 → left++
    left=3 (0), right=5 (2): 0 + 2 = 2 < 4 → left++
    left=4 (1), right=5 (2): 1 + 2 = 3 < 4 → left++
    left=5, right=5: exit (left >= right)
    No triplets with -4
  
  i=1, nums[i]=-1, target=1:
    left=2 (-1), right=5 (2): -1 + 2 = 1 == 1 ✓
      → Add [-1, -1, 2]
      → Skip duplicates
      left=3 (0), right=4 (1)
    left=3 (0), right=4 (1): 0 + 1 = 1 == 1 ✓
      → Add [-1, 0, 1]
      left=4, right=3: exit
  
  i=2, nums[i]=-1:
    Skip! (i > 0 and nums[2] == nums[1])
  
  i=3, nums[i]=0:
    left=4 (1), right=5 (2): 1 + 2 = 3 > 0 → right--
    left=4, right=4: exit
    No triplets with 0

Result: [[-1, -1, 2], [-1, 0, 1]] ✓
```

### Why Sorting + Two Pointers Works

After sorting, the array is structured: smaller ← → larger

When `left + right < target`: need a larger sum → move left pointer right (toward larger values)
When `left + right > target`: need a smaller sum → move right pointer left (toward smaller values)

This gives **linear search** for finding valid pairs, not quadratic.

---

## Comparison: Brute Force vs Optimal

| Aspect | Brute Force | Optimal |
|--------|-----------|---------|
| **Time Complexity** | **O(n³)** | **O(n²)** |
| **Space Complexity** | O(1) | O(1) |
| **For n=100** | ~1M ops | ~10K ops |
| **For n=3000** | **~27 billion ops (too slow)** | ~9M ops ✓ |
| **Algorithm** | Try all triplets | Sort + two pointers |
| **Duplicate Handling** | Post-process (expensive) | Built-in with sorting |

**Why optimal wins:** Sorting enables two-pointer technique, saving an entire dimension of complexity (n³ → n²).

---

## Approach

**Time Complexity:** O(n²)
**Space Complexity:** O(1) extra (output not counted)

Sort, then for each element as the first of the triplet, use two pointers on the remaining sorted subarray to find pairs summing to the negation. Skip duplicates at each level.

## Python Implementation

```python
def three_sum(nums):
    nums.sort()
    result = []
    n = len(nums)
    
    for i in range(n - 2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left, right = i + 1, n - 1
        target = -nums[i]
        
        while left < right:
            current_sum = nums[left] + nums[right]
            
            if current_sum == target:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    
    return result
```
