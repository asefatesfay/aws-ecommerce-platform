# Programming Fundamentals

Before tackling DSA problems, make sure these fundamentals are solid. They come up constantly.

## Data Types & Overflow

- Integer overflow: in languages without arbitrary precision (Java, C++), `int` max is ~2.1 billion (2^31 - 1). Use `long` for large products/sums.
- Floating point: avoid `==` comparisons with floats. Use `abs(a - b) < 1e-9`.
- Python has arbitrary precision integers — no overflow concern.

## Arrays

- Zero-indexed in most languages
- Access: O(1), Search: O(n), Insert/Delete at end: O(1) amortized, Insert/Delete at middle: O(n)
- Know how to: reverse in-place, rotate, find max/min, two-pointer traverse

## Strings

- Immutable in Python, Java — concatenation in a loop is O(n²); use a list/StringBuilder
- Know: character frequency counting, palindrome check, substring operations
- ASCII: 'a' = 97, 'A' = 65, '0' = 48

## Hash Maps & Hash Sets

- Average O(1) insert, lookup, delete
- Use when you need fast lookup by key
- Use set when you only care about membership

## Sorting

- Python: `list.sort()` or `sorted()` — Timsort, O(n log n)
- Java: `Arrays.sort()` — dual-pivot quicksort for primitives, merge sort for objects
- Custom comparator: sort by second element, sort descending, etc.

## Math Essentials

- Integer division: `//` in Python, `/` with integers in Java/C++
- Modulo: `%` — useful for circular indexing, digit extraction
- `abs()`, `min()`, `max()` — use liberally
- Powers: `x ** n` in Python, `Math.pow(x, n)` in Java
- `float('inf')` / `float('-inf')` in Python for sentinel values

## Recursion Basics

Every recursive function needs:
1. **Base case** — when to stop
2. **Recursive case** — how to reduce the problem
3. **Return value** — what to pass back up

Stack depth = number of recursive calls. Deep recursion → stack overflow. Python default limit is ~1000.

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

## Key Built-ins to Know

| Python | Java | Purpose |
|--------|------|---------|
| `sorted()` | `Arrays.sort()` | Sort |
| `collections.deque` | `ArrayDeque` | Queue/Deque |
| `heapq` | `PriorityQueue` | Heap |
| `collections.Counter` | `HashMap` | Frequency count |
| `set()` | `HashSet` | Membership |
| `bisect` | `Collections.binarySearch` | Binary search |
