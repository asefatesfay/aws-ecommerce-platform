"""
bisect — Binary search and insort for sorted lists.

Key insight: bisect maintains O(log n) search in a sorted list.
Insertion via insort keeps the list sorted in O(n) (due to shifting).
Use bisect when reads are frequent and inserts are rare.
Use heapq when you need fast repeated min/max extraction.

Covered here:
  bisect_left   — index of leftmost position where value can be inserted
  bisect_right  — index of rightmost position where value can be inserted
  insort_left   — insert in sorted order (left of existing equal elements)
  insort_right  — insert in sorted order (right of existing equal elements)

Practical applications:
  - Score-to-grade mapping
  - Sorted leaderboard maintenance
  - Count elements in a range
  - Floor / ceiling lookups
  - Search in a sorted DB result without scanning
"""

import bisect


# ---------------------------------------------------------------------------
# 1. bisect_left vs bisect_right — understanding the difference
# ---------------------------------------------------------------------------

def demo_bisect_basics():
    print("=" * 60)
    print("bisect_left  vs  bisect_right")
    print("=" * 60)

    nums = [10, 20, 20, 20, 30, 40]
    target = 20

    left  = bisect.bisect_left(nums, target)
    right = bisect.bisect_right(nums, target)

    print("Sorted list: ", nums)
    print(f"bisect_left({target})  -> {left}   # index of FIRST  {target}")
    print(f"bisect_right({target}) -> {right}   # index AFTER LAST {target}")
    # bisect_left(20)  -> 1   (insert before existing 20s)
    # bisect_right(20) -> 4   (insert after  existing 20s)

    # Checking membership
    def contains(sorted_list, value):
        i = bisect.bisect_left(sorted_list, value)
        return i < len(sorted_list) and sorted_list[i] == value

    print("\nMembership checks (O(log n)):")
    for v in [10, 20, 25, 40, 50]:
        print(f"  {v} in list: {contains(nums, v)}")
    # 10: True, 20: True, 25: False, 40: True, 50: False

    print()


# ---------------------------------------------------------------------------
# 2. Score-to-grade mapping (classic bisect_right use case)
# ---------------------------------------------------------------------------

def demo_grade_mapping():
    print("=" * 60)
    print("Score-to-grade mapping")
    print("=" * 60)

    # Boundary scores for grades F, D, C, B, A
    breakpoints = [60, 70, 80, 90]
    grades      = ["F", "D", "C", "B", "A"]

    def letter_grade(score: int) -> str:
        """Return letter grade for a numeric score."""
        index = bisect.bisect_right(breakpoints, score)
        return grades[index]

    test_scores = [45, 60, 61, 75, 80, 85, 92, 100]
    print("Score -> Grade:")
    for score in test_scores:
        print(f"  {score:3d}  ->  {letter_grade(score)}")
    # 45  -> F
    # 60  -> D   (score of exactly 60 is the boundary for D)
    # 61  -> D
    # 75  -> C
    # 80  -> B
    # 85  -> B
    # 92  -> A
    # 100 -> A

    # Tax bracket lookup (same pattern)
    income_brackets = [10_000, 40_000, 85_000, 165_000, 215_000]
    tax_rates        = [0.10,  0.12,   0.22,   0.24,   0.32,   0.35]

    def tax_rate(income: int) -> float:
        return tax_rates[bisect.bisect_right(income_brackets, income)]

    print("\nTax rate lookups:")
    for income in [5_000, 15_000, 60_000, 100_000, 200_000, 250_000]:
        print(f"  ${income:>10,}  ->  {tax_rate(income) * 100:.0f}%")

    print()


# ---------------------------------------------------------------------------
# 3. Sorted leaderboard with insort
# ---------------------------------------------------------------------------

def demo_sorted_leaderboard():
    print("=" * 60)
    print("Sorted leaderboard  (insort_right)")
    print("=" * 60)

    leaderboard = []   # keeps scores ascending

    def add_score(score: int) -> None:
        bisect.insort_right(leaderboard, score)

    def rank_of(score: int) -> int:
        """1-based rank (position from the top)."""
        # number of scores strictly greater than this score
        return len(leaderboard) - bisect.bisect_right(leaderboard, score)

    def top_n(n: int) -> list:
        return leaderboard[-n:][::-1]   # last n in descending order

    player_scores = [
        ("Alice",  1500),
        ("Bob",    1200),
        ("Carol",  1800),
        ("Dave",   1350),
        ("Eve",    1800),
        ("Frank",  950),
    ]

    for player, score in player_scores:
        add_score(score)
        rank = rank_of(score)
        print(f"  {player:6} scored {score} -> rank #{rank + 1}")

    print("\nFinal leaderboard (ascending):", leaderboard)
    print("Top 3 players:", top_n(3))   # [1800, 1800, 1500]

    # Update a score (remove old, insert new)
    old_score = 1200  # Bob's old score
    new_score = 1650  # Bob improved

    idx = bisect.bisect_left(leaderboard, old_score)
    if leaderboard[idx] == old_score:
        leaderboard.pop(idx)
    bisect.insort_right(leaderboard, new_score)

    print("After Bob's update:", leaderboard)

    print()


# ---------------------------------------------------------------------------
# 4. Count elements in a range in O(log n)
# ---------------------------------------------------------------------------

def demo_range_count():
    print("=" * 60)
    print("Count elements in a range  (O(log n))")
    print("=" * 60)

    # Sorted list of response times (milliseconds)
    response_times = sorted([
        120, 45, 310, 89, 200, 55, 430, 70, 185, 95,
        260, 38, 500, 140, 75, 320, 110, 400, 60, 170,
    ])

    def count_in_range(sorted_list, lo, hi):
        """Count elements where lo <= x <= hi in O(log n)."""
        left  = bisect.bisect_left(sorted_list, lo)
        right = bisect.bisect_right(sorted_list, hi)
        return right - left

    print("Response times:", response_times)
    print()
    print("SLA analysis:")
    print(f"  Under 100ms  (fast):   {count_in_range(response_times, 0, 99)}")
    print(f"  100–300ms    (normal): {count_in_range(response_times, 100, 300)}")
    print(f"  Over 300ms   (slow):   {count_in_range(response_times, 301, 10000)}")

    total = len(response_times)
    slow  = count_in_range(response_times, 301, 10000)
    print(f"  Slow request rate:     {slow / total * 100:.1f}%")

    print()


# ---------------------------------------------------------------------------
# 5. Floor and ceiling lookups
# ---------------------------------------------------------------------------

def demo_floor_ceiling():
    print("=" * 60)
    print("Floor and ceiling lookups")
    print("=" * 60)

    price_levels = [100, 200, 300, 400, 500]

    def floor_price(target: int) -> int | None:
        """Largest price <= target."""
        idx = bisect.bisect_right(price_levels, target) - 1
        return price_levels[idx] if idx >= 0 else None

    def ceil_price(target: int) -> int | None:
        """Smallest price >= target."""
        idx = bisect.bisect_left(price_levels, target)
        return price_levels[idx] if idx < len(price_levels) else None

    queries = [50, 100, 150, 350, 450, 500, 600]
    print(f"{'Query':>6}  {'Floor':>6}  {'Ceiling':>7}")
    print("-" * 24)
    for q in queries:
        print(f"  {q:4d}  ->  floor={str(floor_price(q)):>4}  ceil={str(ceil_price(q)):>4}")
    #  50  -> floor=None  ceil= 100
    # 100  -> floor= 100  ceil= 100
    # 150  -> floor= 100  ceil= 200
    # 350  -> floor= 300  ceil= 400
    # 600  -> floor= 500  ceil=None

    print()


# ---------------------------------------------------------------------------
# 6. Binary search for first/last occurrence
# ---------------------------------------------------------------------------

def demo_first_last():
    print("=" * 60)
    print("First and last occurrence of a value")
    print("=" * 60)

    # Sorted list of order IDs per customer (duplicates possible)
    order_ids = [1001, 1002, 1002, 1002, 1003, 1004, 1004, 1005]

    def first_occurrence(sorted_list: list, value: int) -> int:
        """Return index of first occurrence, or -1."""
        idx = bisect.bisect_left(sorted_list, value)
        if idx < len(sorted_list) and sorted_list[idx] == value:
            return idx
        return -1

    def last_occurrence(sorted_list: list, value: int) -> int:
        """Return index of last occurrence, or -1."""
        idx = bisect.bisect_right(sorted_list, value) - 1
        if idx >= 0 and sorted_list[idx] == value:
            return idx
        return -1

    def count_occurrences(sorted_list: list, value: int) -> int:
        return bisect.bisect_right(sorted_list, value) - bisect.bisect_left(sorted_list, value)

    print("Order IDs:", order_ids)
    for order_id in [1001, 1002, 1003, 1006]:
        first = first_occurrence(order_ids, order_id)
        last  = last_occurrence(order_ids, order_id)
        count = count_occurrences(order_ids, order_id)
        print(f"  {order_id}: first={first:2d}  last={last:2d}  count={count}")
    # 1001: first= 0  last= 0  count=1
    # 1002: first= 1  last= 3  count=3
    # 1003: first= 4  last= 4  count=1
    # 1006: first=-1  last=-1  count=0

    print()


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    demo_bisect_basics()
    demo_grade_mapping()
    demo_sorted_leaderboard()
    demo_range_count()
    demo_floor_ceiling()
    demo_first_last()
