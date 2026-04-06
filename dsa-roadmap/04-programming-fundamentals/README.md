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

```python
arr = [1, 2, 3, 4, 5]

# Reverse in-place
arr.reverse()  # [5, 4, 3, 2, 1]

# Rotate right by k
def rotate_right(nums, k):
	n = len(nums)
	if n == 0:
		return nums
	k %= n
	nums[:] = nums[-k:] + nums[:-k]
	return nums
```

## Strings

- Immutable in Python, Java — concatenation in a loop is O(n²); use a list/StringBuilder
- Know: character frequency counting, palindrome check, substring operations
- ASCII: 'a' = 97, 'A' = 65, '0' = 48

```python
s = "racecar"

# Palindrome check
is_pal = s == s[::-1]

# Efficient string build
parts = []
for ch in ["a", "b", "c"]:
	parts.append(ch)
joined = "".join(parts)  # "abc"
```

## Hash Maps & Hash Sets

- Average O(1) insert, lookup, delete
- Use when you need fast lookup by key
- Use set when you only care about membership

```python
nums = [1, 2, 2, 3, 3, 3]

# Frequency map
freq = {}
for x in nums:
	freq[x] = freq.get(x, 0) + 1

# Membership
seen = set(nums)
has_four = 4 in seen
```

## Sorting

- Python: `list.sort()` or `sorted()` — Timsort, O(n log n)
- Java: `Arrays.sort()` — dual-pivot quicksort for primitives, merge sort for objects
- Custom comparator: sort by second element, sort descending, etc.

```python
pairs = [("apple", 3), ("banana", 1), ("pear", 2)]

# Sort by second element
pairs.sort(key=lambda x: x[1])

# Sort numbers descending
nums = [5, 2, 8, 1]
desc = sorted(nums, reverse=True)
```

## Math Essentials

- Integer division: `//` in Python, `/` with integers in Java/C++
- Modulo: `%` — useful for circular indexing, digit extraction
- `abs()`, `min()`, `max()` — use liberally
- Powers: `x ** n` in Python, `Math.pow(x, n)` in Java
- `float('inf')` / `float('-inf')` in Python for sentinel values

```python
n = 17
quotient = n // 5   # 3
remainder = n % 5   # 2

# Circular index
arr = [10, 20, 30]
next_i = (2 + 1) % len(arr)  # 0

best = float("inf")
best = min(best, 42)
```

## Recursion Basics

Every recursive function needs:
1. **Base case** — when to stop
2. **Recursive case** — how to reduce the problem
3. **Return value** — what to pass back up

Stack depth = number of recursive calls. Deep recursion → stack overflow. Python default limit is ~1000.

```python
def factorial(n):
	if n <= 1:          # base case
		return 1
	return n * factorial(n - 1)  # recursive case
```

Tip: In Python interviews, consider iterative solutions when recursion depth can exceed ~1000.

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

```python
# Sliding window template (fixed size k)
def max_sum_k(nums, k):
	if k > len(nums):
		return None
	window = sum(nums[:k])
	best = window
	for i in range(k, len(nums)):
		window += nums[i] - nums[i - k]
		best = max(best, window)
	return best
```

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
