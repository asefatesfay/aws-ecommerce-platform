"""
Sorting in Python — sorted(), list.sort(), and operator module.

Python's sort is Timsort: stable O(n log n), adaptive to partially sorted data.

Covered here:
  sorted() vs list.sort()   — return new vs in-place
  key=                      — custom sort criteria
  reverse=                  — descending order
  operator.itemgetter       — sort by dict/tuple field (faster than lambda)
  operator.attrgetter       — sort by object attribute
  operator.methodcaller     — sort using a method's return value
  Multi-key sort            — primary + secondary + tertiary keys
  Stable sort               — equal elements preserve original order
  Case-insensitive sort     — str.lower / str.casefold as keys
  Custom comparator         — functools.cmp_to_key for complex ordering
  Decorate-Sort-Undecorate  — Schwartzian transform for expensive keys
"""

import operator
from functools import cmp_to_key
from dataclasses import dataclass


# ---------------------------------------------------------------------------
# 1. sorted() vs list.sort() — immutable vs in-place
# ---------------------------------------------------------------------------

def demo_sorted_vs_sort():
    print("=" * 60)
    print("sorted()  vs  list.sort()")
    print("=" * 60)

    prices = [49.99, 12.00, 99.95, 5.50, 75.00]

    # sorted() returns a new list — original is unchanged
    ascending  = sorted(prices)
    descending = sorted(prices, reverse=True)
    print("Original:  ", prices)       # unchanged
    print("Ascending: ", ascending)
    print("Descending:", descending)

    # list.sort() mutates in place — returns None
    stock = [49.99, 12.00, 99.95, 5.50, 75.00]
    stock.sort()
    print("In-place sorted:", stock)   # [5.5, 12.0, 49.99, 75.0, 99.95]

    # sorted() works on any iterable, not just lists
    from collections import deque
    dq = deque([3, 1, 4, 1, 5, 9])
    print("Sorted deque:", sorted(dq))   # [1, 1, 3, 4, 5, 9]

    print()


# ---------------------------------------------------------------------------
# 2. key= with lambda and operator.itemgetter
# ---------------------------------------------------------------------------

def demo_key_function():
    print("=" * 60)
    print("key=  with lambda vs operator.itemgetter")
    print("=" * 60)

    employees = [
        {"name": "Carol",  "dept": "Engineering", "salary": 105_000, "years": 5},
        {"name": "Alice",  "dept": "Engineering", "salary":  95_000, "years": 8},
        {"name": "Bob",    "dept": "Marketing",   "salary":  72_000, "years": 3},
        {"name": "Dave",   "dept": "Marketing",   "salary":  68_000, "years": 7},
        {"name": "Eve",    "dept": "HR",          "salary":  80_000, "years": 2},
        {"name": "Frank",  "dept": "Engineering", "salary":  95_000, "years": 6},
    ]

    # Sort by salary descending
    by_salary = sorted(employees, key=operator.itemgetter("salary"), reverse=True)
    print("By salary (desc):")
    for e in by_salary:
        print(f"  {e['name']:6} ${e['salary']:,}")

    # operator.itemgetter is faster than lambda for large datasets
    # and is preferred in production code

    # Sort by department name (ascending)
    by_dept = sorted(employees, key=operator.itemgetter("dept"))
    print("\nBy department:")
    for e in by_dept:
        print(f"  {e['dept']:15} {e['name']}")

    # Sort tuples by second element
    scores = [("Alice", 88), ("Bob", 95), ("Carol", 72), ("Dave", 88)]
    by_score = sorted(scores, key=operator.itemgetter(1), reverse=True)
    print("\nScores (highest first):", by_score)
    # [('Bob', 95), ('Alice', 88), ('Dave', 88), ('Carol', 72)]

    print()


# ---------------------------------------------------------------------------
# 3. Multi-key sort — primary, secondary, tertiary
# ---------------------------------------------------------------------------

def demo_multi_key():
    print("=" * 60)
    print("Multi-key sort  (tuple key)")
    print("=" * 60)

    employees = [
        {"name": "Carol",  "dept": "Engineering", "salary": 105_000, "years": 5},
        {"name": "Alice",  "dept": "Engineering", "salary":  95_000, "years": 8},
        {"name": "Bob",    "dept": "Marketing",   "salary":  72_000, "years": 3},
        {"name": "Dave",   "dept": "Marketing",   "salary":  68_000, "years": 7},
        {"name": "Eve",    "dept": "HR",          "salary":  80_000, "years": 2},
        {"name": "Frank",  "dept": "Engineering", "salary":  95_000, "years": 6},
    ]

    # Sort: dept ascending, then salary descending, then years descending
    # Negate numeric fields for "descending" within a tuple key
    multi_sorted = sorted(
        employees,
        key=lambda e: (e["dept"], -e["salary"], -e["years"])
    )

    print("Sorted by dept ASC, salary DESC, years DESC:")
    for e in multi_sorted:
        print(f"  {e['dept']:15} {e['name']:6} ${e['salary']:,}  {e['years']}yr")
    # Engineering  Carol  $105,000  5yr
    # Engineering  Frank  $95,000   6yr
    # Engineering  Alice  $95,000   8yr
    # HR           Eve    $80,000   2yr
    # Marketing    Bob    $72,000   3yr
    # Marketing    Dave   $68,000   7yr

    # operator.itemgetter for multiple fields at once
    by_dept_then_name = sorted(employees, key=operator.itemgetter("dept", "name"))
    print("\nBy dept then name:")
    for e in by_dept_then_name:
        print(f"  {e['dept']:15} {e['name']}")

    print()


# ---------------------------------------------------------------------------
# 4. operator.attrgetter — sort objects by attribute
# ---------------------------------------------------------------------------

def demo_attrgetter():
    print("=" * 60)
    print("operator.attrgetter  (sort objects)")
    print("=" * 60)

    @dataclass
    class Product:
        name:     str
        category: str
        price:    float
        stock:    int

        def __repr__(self):
            return f"{self.name}(${self.price})"

    products = [
        Product("Laptop Pro",    "Electronics", 999.99, 15),
        Product("USB-C Hub",     "Electronics", 49.99,  80),
        Product("Standing Desk", "Furniture",   399.00, 8),
        Product("Office Chair",  "Furniture",   249.00, 20),
        Product("Wireless Mouse","Electronics", 29.99,  150),
        Product("Bookshelf",     "Furniture",   189.00, 12),
    ]

    # Sort by price
    by_price = sorted(products, key=operator.attrgetter("price"))
    print("By price:", by_price)
    # [Wireless Mouse($29.99), USB-C Hub($49.99), ...]

    # Sort by category then price
    by_cat_price = sorted(products, key=operator.attrgetter("category", "price"))
    print("\nBy category, then price:")
    for p in by_cat_price:
        print(f"  {p.category:12} {p.name:20} ${p.price}")

    # Sort by stock ascending (low stock first — reorder alert)
    low_stock_first = sorted(products, key=operator.attrgetter("stock"))
    print("\nLow-stock alert order:")
    for p in low_stock_first:
        alert = " ⚠" if p.stock < 15 else ""
        print(f"  stock={p.stock:3d}  {p.name}{alert}")

    print()


# ---------------------------------------------------------------------------
# 5. Stable sort — equal elements keep their relative order
# ---------------------------------------------------------------------------

def demo_stable_sort():
    print("=" * 60)
    print("Stable sort  (equal elements preserve original order)")
    print("=" * 60)

    # Multi-pass sort: first by department, then by salary within department
    # We can do this safely as two separate sorts because Python sort is stable

    employees = [
        {"name": "Carol",  "dept": "Engineering", "salary": 105_000},
        {"name": "Alice",  "dept": "Engineering", "salary":  95_000},
        {"name": "Frank",  "dept": "Engineering", "salary":  95_000},
        {"name": "Bob",    "dept": "Marketing",   "salary":  72_000},
        {"name": "Dave",   "dept": "Marketing",   "salary":  68_000},
    ]

    # Step 1: sort by salary (secondary key)
    employees.sort(key=operator.itemgetter("salary"))
    print("After salary sort:", [e["name"] for e in employees])

    # Step 2: sort by dept (primary key) — salary order is preserved within dept
    employees.sort(key=operator.itemgetter("dept"))
    print("After dept sort:  ", [e["name"] for e in employees])
    # Alice and Frank/Carol are in salary order within Engineering
    # because step 2 was stable

    # Demonstrate stability directly
    data = [("Bob", 2), ("Alice", 1), ("Carol", 1), ("Dave", 2)]
    result = sorted(data, key=operator.itemgetter(1))
    print("\nStable sort by second element:")
    print(" ", result)
    # [('Alice', 1), ('Carol', 1), ('Bob', 2), ('Dave', 2)]
    # Alice stays before Carol (both have key=1) because that was original order

    print()


# ---------------------------------------------------------------------------
# 6. Case-insensitive and locale-aware string sorting
# ---------------------------------------------------------------------------

def demo_string_sorting():
    print("=" * 60)
    print("String sorting  (case-insensitive, locale-aware)")
    print("=" * 60)

    names = ["Charlie", "alice", "Bob", "dave", "Eve", "FRANK"]

    # Default sort — uppercase letters sort before lowercase (ASCII order)
    print("Default sort:          ", sorted(names))
    # ['BOB','Charlie','Eve','FRANK','alice','dave']  — uppercase first!

    # Case-insensitive: str.lower or str.casefold
    print("Case-insensitive:      ", sorted(names, key=str.lower))
    # ['alice', 'Bob', 'Charlie', 'dave', 'Eve', 'FRANK']

    # casefold is more aggressive — handles special chars (ß -> ss, etc.)
    print("casefold sort:         ", sorted(names, key=str.casefold))

    # Sort by last word in a full name
    full_names = ["John Smith", "Anna Lee", "Bob Chen", "Mary Adams", "Tom Brown"]
    by_last_name = sorted(full_names, key=lambda n: n.split()[-1])
    print("\nSorted by last name:", by_last_name)
    # ['Mary Adams', 'Tom Brown', 'Bob Chen', 'Anna Lee', 'John Smith']

    # Sort file names that have numeric parts correctly
    files = ["file10.txt", "file2.txt", "file1.txt", "file20.txt", "file3.txt"]
    print("\nLexicographic sort:", sorted(files))
    # ['file1.txt', 'file10.txt', 'file2.txt', ...]  — 10 before 2!

    # Natural sort (numeric aware)
    import re
    def natural_key(filename):
        parts = re.split(r'(\d+)', filename)
        return [int(p) if p.isdigit() else p for p in parts]

    print("Natural sort:      ", sorted(files, key=natural_key))
    # ['file1.txt', 'file2.txt', 'file3.txt', 'file10.txt', 'file20.txt']

    print()


# ---------------------------------------------------------------------------
# 7. cmp_to_key — port a Java-style comparator to Python
# ---------------------------------------------------------------------------

def demo_cmp_to_key():
    print("=" * 60)
    print("cmp_to_key  (custom comparator / complex ordering)")
    print("=" * 60)

    # --- 7a: sort version strings ---
    versions = ["1.10.0", "1.2.3", "2.0.0", "1.9.5", "1.10.1"]

    def version_cmp(a, b):
        """Compare two semantic version strings."""
        parts_a = list(map(int, a.split(".")))
        parts_b = list(map(int, b.split(".")))
        if parts_a < parts_b:
            return -1
        if parts_a > parts_b:
            return 1
        return 0

    print("Version strings sorted:")
    print(" ", sorted(versions, key=cmp_to_key(version_cmp)))
    # ['1.2.3', '1.9.5', '1.10.0', '1.10.1', '2.0.0']

    # --- 7b: LeetCode 179 — Largest Number ---
    # Given a list of non-negative integers, arrange them to form the largest number.
    nums = [3, 30, 34, 5, 9]

    def cmp_digits(a, b):
        ab = str(a) + str(b)
        ba = str(b) + str(a)
        if ab > ba:
            return -1   # a should come first
        if ab < ba:
            return 1
        return 0

    arranged = sorted(nums, key=cmp_to_key(cmp_digits))
    result = "".join(map(str, arranged))
    print(f"\nLargest number from {nums}: {result}")   # 9534330

    print()


# ---------------------------------------------------------------------------
# 8. Decorate-Sort-Undecorate (Schwartzian transform)
# ---------------------------------------------------------------------------

def demo_schwartzian():
    print("=" * 60)
    print("Decorate-Sort-Undecorate  (expensive computed key)")
    print("=" * 60)

    # Scenario: sort filenames by the number of vowels in the name.
    # Computing vowel count is straightforward but let's say it's expensive.
    filenames = ["report.pdf", "data_analysis.csv", "readme.txt",
                 "architecture_overview.md", "api.yaml", "todo.txt"]

    def count_vowels(s: str) -> int:
        return sum(1 for c in s.lower() if c in "aeiou")

    # Without DSU: key= calls count_vowels for every comparison
    # With DSU: compute once, sort by precomputed value, strip back

    # Decorate
    decorated = [(count_vowels(f), f) for f in filenames]
    # Sort
    decorated.sort()
    # Undecorate
    result = [f for _, f in decorated]

    print("Sorted by vowel count:")
    for f in result:
        print(f"  {count_vowels(f)} vowels — {f}")
    # useful when the key is truly expensive (e.g. DB query, hash, regex match)

    print()


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    demo_sorted_vs_sort()
    demo_key_function()
    demo_multi_key()
    demo_attrgetter()
    demo_stable_sort()
    demo_string_sorting()
    demo_cmp_to_key()
    demo_schwartzian()
