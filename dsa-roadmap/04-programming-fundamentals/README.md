# Programming Fundamentals

Before tackling DSA problems, make sure these fundamentals are solid. They come up constantly.

## Python-First Mindset

In interviews, writing clean and correct Python quickly matters more than clever one-liners.

- Prefer readability over dense syntax.
- Use built-ins (`sum`, `min`, `max`, `sorted`, `set`, `dict`) before reinventing logic.
- Be explicit about time complexity, especially when using slicing or string concatenation.

## Data Types & Overflow

- Integer overflow: in languages without arbitrary precision (Java, C++), `int` max is ~2.1 billion (2^31 - 1). Use `long` for large products/sums.
- Floating point: avoid `==` comparisons with floats. Use `abs(a - b) < 1e-9`.
- Python has arbitrary precision integers — no overflow concern.

```python
# Python int grows as needed (no fixed-width overflow)
big = 10**100

# Float comparison with tolerance
def are_close(a, b, eps=1e-9):
	return abs(a - b) < eps
```

## Arrays

- Zero-indexed in most languages
- Access: O(1), Search: O(n), Insert/Delete at end: O(1) amortized, Insert/Delete at middle: O(n)
- Know how to: reverse in-place, rotate, find max/min, two-pointer traverse

### Reverse In-Place

```python
arr = [1, 2, 3, 4, 5]
arr.reverse()
# Output: [5, 4, 3, 2, 1]
```

**Visual Example:**
```
Initial:    [1, 2, 3, 4, 5]
             ↑           ↑
Step 1:     [5, 2, 3, 4, 1]
             ↑           ↑
Step 2:     [5, 4, 3, 2, 1]  ✓
```

### Rotate Right by k

```python
def rotate_right(nums, k):
	n = len(nums)
	if n == 0:
		return nums
	k %= n
	nums[:] = nums[-k:] + nums[:-k]
	return nums

# Example: rotate [1, 2, 3, 4, 5] right by 2
# Output: [4, 5, 1, 2, 3]
```

**Visual Example (k=2):**
```
Original:     [1, 2, 3, 4, 5]
Take last 2:   [4, 5]
Take rest:     [1, 2, 3]
Combine:       [4, 5, 1, 2, 3]
```

## Strings

- Immutable in Python, Java — concatenation in a loop is O(n²); use a list/StringBuilder
- Know: character frequency counting, palindrome check, substring operations
- ASCII: 'a' = 97, 'A' = 65, '0' = 48

### Palindrome Check

```python
s = "racecar"
is_pal = s == s[::-1]
# Output: True
```

**Visual Example:**
```
Input:  r a c e c a r
         ↑           ↑
        Yes — reverse matches
```

### Efficient String Building

```python
# ❌ Bad: O(n²) due to repeated concatenation
result = ""
for ch in ["a", "b", "c"]:
    result += ch  # Slow!

# ✓ Good: O(n) — build list, then join
parts = []
for ch in ["a", "b", "c"]:
    parts.append(ch)
joined = "".join(parts)  # "abc"
```

**Complexity Comparison:**
```
String Concatenation in Loop
n    | Bad (+=)  | Good (.join)
─────┼───────────┼───────────
10   | O(n²)     | O(n) ✓
100  | 10,000 op | 100 op
1000 | 1M op     | 1000 op
```

## Hash Maps & Hash Sets

- Average O(1) insert, lookup, delete
- Use when you need fast lookup by key
- Use set when you only care about membership

### Frequency Counting

```python
nums = [1, 2, 2, 3, 3, 3]

# Frequency map
freq = {}
for x in nums:
    freq[x] = freq.get(x, 0) + 1

# Output: {1: 1, 2: 2, 3: 3}
```

**Visual Example:**
```
Input: [1, 2, 2, 3, 3, 3]

Processing:
  1 → freq = {1: 1}
  2 → freq = {1: 1, 2: 1}
  2 → freq = {1: 1, 2: 2}
  3 → freq = {1: 1, 2: 2, 3: 1}
  3 → freq = {1: 1, 2: 2, 3: 2}
  3 → freq = {1: 1, 2: 2, 3: 3}

Final: {1: 1, 2: 2, 3: 3}
```

### Membership Check

```python
nums = [1, 2, 2, 3, 3, 3]
seen = set(nums)
has_four = 4 in seen

# Output: False (4 not in set)
```

**Time Comparison:**
```
Lookup in [1, 2, 2, 3, 3, 3]

List:  O(n) — must scan all elements
Set:   O(1) — direct hash lookup ✓
```

## Sorting

- Python: `list.sort()` or `sorted()` — Timsort, O(n log n)
- Java: `Arrays.sort()` — dual-pivot quicksort for primitives, merge sort for objects
- Custom comparator: sort by second element, sort descending, etc.

### Sort by Key

```python
pairs = [("apple", 3), ("banana", 1), ("pear", 2)]

# Sort by second element
pairs.sort(key=lambda x: x[1])
# Output: [("banana", 1), ("pear", 2), ("apple", 3)]
```

**Visual Example:**
```
Input:   [("apple", 3), ("banana", 1), ("pear", 2)]

Sorted by value (second element):
Step 1:  Compare 3, 1, 2
Step 2:  Place 1 first → ("banana", 1)
Step 3:  Place 2 next → ("pear", 2)
Step 4:  Place 3 last → ("apple", 3)

Output:  [("banana", 1), ("pear", 2), ("apple", 3)]
```

### Sort Descending

```python
nums = [5, 2, 8, 1]
desc = sorted(nums, reverse=True)
# Output: [8, 5, 2, 1]
```

## Math Essentials

- Integer division: `//` in Python, `/` with integers in Java/C++
- Modulo: `%` — useful for circular indexing, digit extraction
- `abs()`, `min()`, `max()` — use liberally
- Powers: `x ** n` in Python, `Math.pow(x, n)` in Java
- `float('inf')` / `float('-inf')` in Python for sentinel values

### Integer Division & Modulo

```python
n = 17
quotient = n // 5   # 3 (divisions fit)
remainder = n % 5   # 2 (what's left)
# 5 * 3 + 2 = 17 ✓
```

**Visual Example:**
```
n = 17, divisor = 5

17 ÷ 5:
  ⌊——⌋ ⌊——⌋ ⌊——⌋ ⌊—
  1    2    3    4    5

  Full groups: 3 (quotient)
  Leftover:   2 (remainder)

17 = 5 × 3 + 2
```

### Circular Indexing

```python
arr = [10, 20, 30]
current = 2
next_i = (current + 1) % len(arr)  # 0 (wraps around)

# Output: arr[0] = 10
```

**Visual Example:**
```
arr = [10, 20, 30]
       [0]  [1]  [2]

Indices form a circle:
     [0] ← wraps
      ↑
    [2]
    [1]

(2 + 1) % 3 = 0 ✓
```

### Sentinel Values

```python
best = float("inf")
best = min(best, 42)
best = min(best, 5)
# Output: 5 (minimum found)
```

**Why Sentinel Values?**
```
Without sentinel (what if first element is smallest?):
  best = arr[0]  # Must handle separately

With sentinel (unified code):
  best = float("inf")
  for x in arr:
      best = min(best, x)  # Works for all elements
```

## Recursion Basics

Every recursive function needs:
1. **Base case** — when to stop
2. **Recursive case** — how to reduce the problem
3. **Return value** — what to pass back up

Stack depth = number of recursive calls. Deep recursion → stack overflow. Python default limit is ~1000.

### Factorial Example

```python
def factorial(n):
    if n <= 1:          # base case
        return 1
    return n * factorial(n - 1)  # recursive case

# factorial(5) = 120
```

**Visual Call Stack:**
```
factorial(5)
  5 * factorial(4)
      4 * factorial(3)
          3 * factorial(2)
              2 * factorial(1)
                  return 1
              return 2 * 1 = 2
          return 3 * 2 = 6
      return 4 * 6 = 24
  return 5 * 24 = 120
```

**Depth Progression:**
```
factorial(5) → calls factorial(4) → calls factorial(3) ...
Depth:           1                   2                    3...

Stack grows until base case (n=1), then unwinds.
Maximum depth: n
```

Tip: In Python interviews, consider iterative solutions when recursion depth can exceed ~1000.

## Visual Playbook: Subsets and Permutations

These two patterns explain why recursive branching can explode.

### Subset Generation (Include/Exclude)

**Input:** `nums = [1, 2, 3]`
**Output count:** `8` subsets (`2^3`)

```mermaid
flowchart TD
    A[Start: []] --> B{Take 1?}
    B -- Yes --> C[[1]]
    B -- No --> D[[]]

    C --> E{Take 2?}
    D --> F{Take 2?}

    E -- Yes --> G[[1,2]]
    E -- No --> H[[1]]
    F -- Yes --> I[[2]]
    F -- No --> J[[]]

    G --> K{Take 3?}
    H --> L{Take 3?}
    I --> M{Take 3?}
    J --> N{Take 3?}
```

### Permutation Generation (Pick Next Unused)

**Input:** `nums = [1, 2, 3]`
**Output count:** `6` permutations (`3!`)

```mermaid
flowchart TD
    A[Start []] --> B[Pick 1]
    A --> C[Pick 2]
    A --> D[Pick 3]

    B --> E[Pick 2]
    B --> F[Pick 3]
    E --> G[[1,2,3]]
    F --> H[[1,3,2]]

    C --> I[Pick 1]
    C --> J[Pick 3]
    I --> K[[2,1,3]]
    J --> L[[2,3,1]]

    D --> M[Pick 1]
    D --> N[Pick 2]
    M --> O[[3,1,2]]
    N --> P[[3,2,1]]
```

Key growth intuition:
- Subsets: each element has 2 choices -> `2^n`
- Permutations: choices shrink each level -> `n!`

## Common Patterns in Fundamentals

```
# Swap two elements
a, b = b, a

# Check if index is valid
if 0 <= i < len(arr) and 0 <= j < len(arr[0]):

# Iterate with index
for i, val in enumerate(arr):

# Build frequency map
from collections import Counter
freq = Counter(arr)

# Default dict
from collections import defaultdict
d = defaultdict(int)
```

### Sliding Window Template (Fixed Size k)

```python
def max_sum_k(nums, k):
    if k > len(nums):
        return None
    window = sum(nums[:k])
    best = window
    for i in range(k, len(nums)):
        window += nums[i] - nums[i - k]
        best = max(best, window)
    return best

# Example: max_sum_k([1, 3, 2, 6, -1, 4, 1, 8, 2], k=3)
# Output: 13 (window [6, -1, 4] = 9, [4, 1, 8] = 13)
```

**Visual Example (k=3):**
```
Array: [1, 3, 2, 6, -1, 4, 1, 8, 2]

Window slides right by 1 each step:

Step 1: [1, 3, 2]  → sum=6
        ↑  ↑  ↑

Step 2: [3, 2, 6]  → sum=11
           ↑  ↑  ↑

Step 3: [2, 6, -1] → sum=7
              ↑  ↑   ↑

Step 4: [6, -1, 4] → sum=9
                 ↑  ↑   ↑

Step 5: [-1, 4, 1] → sum=4
                    ↑  ↑   ↑

Step 6: [4, 1, 8]  → sum=13 ← MAX ✓
                       ↑  ↑   ↑

Step 7: [1, 8, 2]  → sum=11
                          ↑  ↑   ↑

Output: 13
```

**Complexity:**
- Traditional: O(n × k) — recompute sum each window
- Sliding: O(n) — add one, remove one ✓

## Key Built-ins to Know

| Python | Java | Purpose |
|--------|------|---------|
| `sorted()` | `Arrays.sort()` | Sort |
| `collections.deque` | `ArrayDeque` | Queue/Deque |
| `heapq` | `PriorityQueue` | Heap |
| `collections.Counter` | `HashMap` | Frequency count |
| `set()` | `HashSet` | Membership |
| `bisect` | `Collections.binarySearch` | Binary search |

## Python Interview Pitfalls

- `list.pop(0)` is O(n). Use `collections.deque` for queue operations.
- Repeated `s += ch` in loops can become O(n²). Prefer `"".join(...)`.
- Slicing like `arr[a:b]` creates a new list (O(k) time and space).
- Mutable defaults are dangerous:

```python
# Bad
def f(x, cache={}):
	cache[x] = True
	return cache

# Good
def f(x, cache=None):
	if cache is None:
		cache = {}
	cache[x] = True
	return cache
```
