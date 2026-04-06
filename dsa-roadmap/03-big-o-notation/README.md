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

**Concept:** Access operation has fixed cost regardless of input size.

```python
def first_item(nums):
    return nums[0] if nums else None
```

**Example:**
- Input: `[10, 20, 30, 40]`
- Output: `10` (accessed immediately)
- Operations: 1 (always)

**Visual:** No growth — flat line
```
Time/Space
    |
  1 |————————————
    |
    +——————————————→ n (input size)
```

---

### O(log n) - Logarithmic

**Concept:** Problem space is halved each step (e.g., binary search).

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

**Example:**
- Input: `nums = [1, 3, 5, 7, 9, 11]`, `target = 7`
- Operations: ~2.6 (log₂ 6)
- Output: `3` (index where 7 is found)

**Visual:** Slow growth
```
Time
    |     ╱
  n |    ╱
    |   ╱
  1 |__╱
    +——————————————→ n
```

---

### O(n) - Linear

**Concept:** Work grows proportionally with input size.

```python
def contains_value(nums, target):
    for num in nums:
        if num == target:
            return True
    return False
```

**Example:**
- Input: `[2, 5, 8, 12]`, `target = 8`
- Operations: 3
- Output: `True`

**Visual:** Straight diagonal line
```
Time
    |\
  n | \
    |  \
  1 |___\
    +——————————————→ n
```

---

### O(n log n) - Linearithmic

**Concept:** Divide-and-conquer (split n, process log n levels).

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

**Example:**
- Input: `[5, 3, 8, 1]`
- Output: `[1, 3, 5, 8]`
- Operations: 4 × log₂(4) = 8

---

### O(n²) - Quadratic

**Concept:** Nested loops over input (compare all pairs).

```python
def has_duplicate_pair(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False
```

**Example:**
- Input: `[1, 2, 1, 5]`
- Operations: C(4,2) = 6 pairs checked
- Output: `True` (1 appears twice)

**Visual:** Steep growth
```
Time
    |        ╱╱
    |      ╱╱
    |    ╱╱
    |  ╱╱
  1 |╱╱
    +——————————————→ n
```

---

### O(2^n) - Exponential

**Concept:** Work doubles with each added element (all subsets).

```python
def count_subsets(n):
    # Each element can be either included or excluded.
    if n == 0:
        return 1
    return count_subsets(n - 1) + count_subsets(n - 1)
```

**Example:**
- Input: `n = 3`
- Subsets: {}, {1}, {2}, {3}, {1,2}, {1,3}, {2,3}, {1,2,3} (8 total)
- Output: `8` (2³)

**Visual:** Explosive growth
```
Time
    |               ╱╱
    |            ╱╱
    |         ╱╱
    |      ╱╱
  1 |___╱╱
    +——————————————→ n
```

---

## Complexity Comparison Chart

```
Input Size (n) | O(1)  | O(log n) | O(n)  | O(n log n) | O(n²) | O(2^n)
───────────────┼──────┼──────────┼───────┼────────────┼───────┼────────
10             | 1    | 3        | 10    | 33         | 100   | 1024
100            | 1    | 7        | 100   | 664        | 10K   | 2^100
1000           | 1    | 10       | 1K    | 10K        | 1M    | 2^1000
```
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
