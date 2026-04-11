# 33. Python Built-in Tools for DSA

Python ships with a set of modules that remove the need to write many common low-level structures from scratch.
Knowing these well makes your interview code shorter, faster, and more readable.

---

## What Is Covered

| File | Module(s) | Key Tools |
|------|-----------|-----------|
| `collections_examples.py` | `collections` | `Counter`, `defaultdict`, `deque`, `namedtuple`, `OrderedDict`, `ChainMap` |
| `functools_examples.py` | `functools` | `lru_cache`, `cache`, `reduce`, `partial`, `wraps`, `total_ordering` |
| `itertools_examples.py` | `itertools` | `chain`, `combinations`, `permutations`, `product`, `groupby`, `islice`, `accumulate`, `cycle` |
| `heapq_examples.py` | `heapq` | min-heap, max-heap, `nlargest`, `nsmallest`, merge sorted streams |
| `bisect_examples.py` | `bisect` | `bisect_left`, `bisect_right`, `insort`, score grading, range counts |
| `sorting_examples.py` | `sorted`, `operator` | multi-key sort, `itemgetter`, `attrgetter`, stable sort, custom comparators |

---

## How to Use This Section

1. Run each file directly: `python collections_examples.py`
2. Every example prints its output so you can verify behaviour at a glance.
3. Read the comment block above each function before reading the code.
4. After reading, close the file and try to reproduce the same output from memory.

---

## Quick Cheat Sheet

```
When you need...                    Use...
--------------------------------    -------------------------------------------
count occurrences                   Counter(iterable)
group items by key                  defaultdict(list)
running tally / frequency map       defaultdict(int)
fast append/pop from both ends      deque
named tuple records                 namedtuple
memoize expensive functions         lru_cache / cache
combine iterables lazily            itertools.chain
all pairs / combinations            itertools.combinations / product
running total                       itertools.accumulate
sorted insertion into a list        bisect.insort
k largest / k smallest              heapq.nlargest / nsmallest
priority queue                      heapq (min-heap by default)
multi-key or custom sort            sorted(items, key=...) with operator.itemgetter
```
