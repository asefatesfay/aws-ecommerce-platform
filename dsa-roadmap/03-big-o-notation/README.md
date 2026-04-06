# Big-O Notation

Big-O notation describes how an algorithm's runtime or space usage grows as the input size grows. It's the language of algorithm analysis.

## Why It Matters

Interviewers always ask about complexity. More importantly, understanding Big-O helps you choose the right algorithm before you write a single line of code.

## Common Complexities (fastest → slowest)

| Notation | Name | Example |
|----------|------|---------|
| O(1) | Constant | Array index access, HashMap lookup |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Single loop through array |
| O(n log n) | Linearithmic | Merge sort, heap sort |
| O(n²) | Quadratic | Nested loops, bubble sort |
| O(2^n) | Exponential | Recursive subsets, brute-force combinations |
| O(n!) | Factorial | Generating all permutations |

## Python Examples for Each Notation

### O(1) - Constant

```python
def first_item(nums):
    return nums[0] if nums else None
```

### O(log n) - Logarithmic

```python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

### O(n) - Linear

```python
def contains_value(nums, target):
    for num in nums:
        if num == target:
            return True
    return False
```

### O(n log n) - Linearithmic

```python
def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged
```

### O(n^2) - Quadratic

```python
def has_duplicate_pair(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False
```

### O(2^n) - Exponential

```python
def count_subsets(n):
    # Each element can be either included or excluded.
    if n == 0:
        return 1
    return count_subsets(n - 1) + count_subsets(n - 1)
```

### O(n!) - Factorial

```python
def permutations(nums):
    if len(nums) <= 1:
        return [nums]

    result = []
    for i in range(len(nums)):
        rest = nums[:i] + nums[i + 1 :]
        for p in permutations(rest):
            result.append([nums[i]] + p)
    return result
```

## Growth Intuition (Approximate Operation Counts)

These rough values help build intuition for how fast each complexity grows.

| n | O(1) | O(log n) | O(n) | O(n log n) | O(n^2) | O(2^n) | O(n!) |
|---|------|----------|------|------------|--------|--------|-------|
| 10 | 1 | 3 | 10 | 33 | 100 | 1,024 | 3,628,800 |
| 20 | 1 | 4 | 20 | 86 | 400 | 1,048,576 | 2.43e18 |
| 100 | 1 | 7 | 100 | 664 | 10,000 | 1.27e30 | 9.33e157 |

Assume log base 2 and round to nearby integers for readability.

## Rules

### Drop Constants
O(2n) → O(n). Constants don't matter at scale.

### Drop Non-Dominant Terms
O(n² + n) → O(n²). The dominant term wins.

### Different Variables for Different Inputs
If you loop over array A (size m) then array B (size n), that's O(m + n), not O(n).

### Nested Loops
Two nested loops over the same array → O(n²). Three nested → O(n³).

### Recursive Complexity
Use the recurrence relation. Binary search: T(n) = T(n/2) + O(1) → O(log n). Merge sort: T(n) = 2T(n/2) + O(n) → O(n log n).

## Space Complexity

Space complexity counts extra memory used (not including input):
- Storing n elements → O(n)
- Recursive call stack depth d → O(d) space
- In-place algorithms → O(1) space

## Amortized Complexity

Some operations are occasionally expensive but cheap on average. Dynamic array append is O(1) amortized even though resizing is O(n), because resizing happens rarely.

## Practice: Identify the Complexity

```
for i in range(n):          # O(n)
    for j in range(n):      # O(n²) total
        print(i, j)

i = n
while i > 1:                # O(log n)
    i = i // 2
```

## Key Insight

When you see a constraint like n ≤ 10^5, the interviewer is telling you O(n log n) or O(n) is expected. Use constraints to reverse-engineer the required approach.
