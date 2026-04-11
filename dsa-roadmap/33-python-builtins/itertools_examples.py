"""
itertools — Fast, memory-efficient tools for working with iterables.

Covered here:
  chain          — concatenate multiple iterables into one
  combinations   — all k-element subsets (no repeats, order irrelevant)
  permutations   — all ordered arrangements
  product        — cartesian product (nested loops without nesting)
  combinations_with_replacement — combinations that allow repeats
  groupby        — group consecutive elements by a key
  islice         — slice an iterator without materialising it
  accumulate     — running totals / prefix sums
  cycle          — repeat an iterable forever
  takewhile      — take elements while condition is True
  dropwhile      — drop elements while condition is True
  zip_longest    — zip with a fill value when lengths differ
  starmap        — map with argument unpacking
"""

from itertools import (
    chain, combinations, permutations, product,
    combinations_with_replacement, groupby,
    islice, accumulate, cycle,
    takewhile, dropwhile, zip_longest, starmap,
)
import operator


# ---------------------------------------------------------------------------
# 1. chain — merge multiple lists / iterables without copying
# ---------------------------------------------------------------------------

def demo_chain():
    print("=" * 60)
    print("chain")
    print("=" * 60)

    # --- 1a: merge several category lists ---
    fruits      = ["apple", "banana"]
    vegetables  = ["carrot", "broccoli"]
    dairy       = ["milk", "cheese"]

    all_items = list(chain(fruits, vegetables, dairy))
    print("All grocery items:", all_items)
    # ['apple', 'banana', 'carrot', 'broccoli', 'milk', 'cheese']

    # --- 1b: chain.from_iterable — flatten one level of nesting ---
    nested_logs = [
        ["ERROR: disk full", "WARN: low memory"],
        ["INFO: server started"],
        ["ERROR: connection refused", "ERROR: timeout"],
    ]
    flat_logs = list(chain.from_iterable(nested_logs))
    print("Flat logs:", flat_logs)
    # ['ERROR: disk full', 'WARN: low memory', 'INFO: server started', ...]

    # --- 1c: iterate multiple database result sets as one stream ---
    page1 = [{"id": 1}, {"id": 2}]
    page2 = [{"id": 3}, {"id": 4}]
    page3 = [{"id": 5}]

    print("All records:")
    for record in chain(page1, page2, page3):
        print(" ", record)

    print()


# ---------------------------------------------------------------------------
# 2. combinations and permutations — team selection, test case generation
# ---------------------------------------------------------------------------

def demo_combinations_and_permutations():
    print("=" * 60)
    print("combinations and permutations")
    print("=" * 60)

    # --- 2a: choose 2 players from a squad for a doubles match ---
    squad = ["Alice", "Bob", "Carol", "Dave"]

    pairs = list(combinations(squad, 2))
    print(f"All {len(pairs)} possible doubles pairs:")
    for pair in pairs:
        print(" ", pair)
    # ('Alice', 'Bob'), ('Alice', 'Carol'), ... (6 total)

    # --- 2b: permutations — ordered podium positions (1st, 2nd, 3rd) ---
    runners = ["Alice", "Bob", "Carol"]
    podiums = list(permutations(runners, 3))
    print(f"\nAll {len(podiums)} podium arrangements:")
    for podium in podiums:
        print(f"  1st={podium[0]}, 2nd={podium[1]}, 3rd={podium[2]}")
    # 6 arrangements (3!)

    # --- 2c: generate all possible 2-char PIN prefixes from digits ---
    digits = "0123456789"
    two_digit_combos = sum(1 for _ in combinations(digits, 2))
    print(f"\nNumber of 2-digit combinations from 0-9: {two_digit_combos}")   # 45

    # --- 2d: combinations_with_replacement — pizza toppings (can repeat) ---
    toppings = ["cheese", "pepperoni", "mushroom"]
    double_toppings = list(combinations_with_replacement(toppings, 2))
    print("\nPizza 2-topping options (repeats allowed):")
    for combo in double_toppings:
        print(" ", combo)
    # includes ('cheese','cheese'), ('cheese','pepperoni'), etc.

    print()


# ---------------------------------------------------------------------------
# 3. product — cartesian product replaces nested for-loops
# ---------------------------------------------------------------------------

def demo_product():
    print("=" * 60)
    print("product")
    print("=" * 60)

    # --- 3a: all (row, col) positions in a 3x3 grid ---
    grid = list(product(range(3), range(3)))
    print("3x3 grid positions:", grid)
    # [(0,0),(0,1),(0,2),(1,0),...,(2,2)]

    # --- 3b: generate test cases for all size/colour/material combos ---
    sizes     = ["S", "M", "L"]
    colours   = ["red", "blue"]
    materials = ["cotton", "polyester"]

    variants = list(product(sizes, colours, materials))
    print(f"\nProduct variants ({len(variants)} total):")
    for v in variants:
        print(f"  size={v[0]}, colour={v[1]}, material={v[2]}")

    # --- 3c: repeat kwarg — e.g. all 2-bit binary strings ---
    binary_strings = ["".join(bits) for bits in product("01", repeat=3)]
    print("\nAll 3-bit binary strings:", binary_strings)
    # ['000', '001', '010', '011', '100', '101', '110', '111']

    print()


# ---------------------------------------------------------------------------
# 4. groupby — group sorted data by a key
# ---------------------------------------------------------------------------

def demo_groupby():
    print("=" * 60)
    print("groupby  (input must be sorted by the same key!)")
    print("=" * 60)

    # --- 4a: group employees by department ---
    employees = [
        {"name": "Alice",  "dept": "Engineering"},
        {"name": "Carol",  "dept": "Engineering"},
        {"name": "Bob",    "dept": "Marketing"},
        {"name": "Dave",   "dept": "Marketing"},
        {"name": "Eve",    "dept": "HR"},
    ]
    # Already sorted by dept; groupby requires sorted input
    for dept, members in groupby(employees, key=lambda e: e["dept"]):
        names = [m["name"] for m in members]
        print(f"  {dept}: {names}")
    # Engineering: ['Alice', 'Carol']
    # Marketing:   ['Bob', 'Dave']
    # HR:          ['Eve']

    # --- 4b: group log entries by severity level ---
    logs = [
        ("ERROR", "disk full"),
        ("ERROR", "connection refused"),
        ("INFO",  "server started"),
        ("INFO",  "request received"),
        ("WARN",  "high memory usage"),
    ]
    print("\nLogs grouped by level:")
    for level, entries in groupby(logs, key=lambda x: x[0]):
        messages = [msg for _, msg in entries]
        print(f"  {level}: {messages}")

    # --- 4c: run-length encoding using groupby ---
    data = "AAABBBCCDDDDEA"
    rle = [(key, sum(1 for _ in group)) for key, group in groupby(data)]
    print("\nRun-length encoding of", repr(data), "->", rle)
    # [('A',3),('B',3),('C',2),('D',4),('E',1),('A',1)]

    print()


# ---------------------------------------------------------------------------
# 5. islice — take a slice of a large or infinite iterator
# ---------------------------------------------------------------------------

def demo_islice():
    print("=" * 60)
    print("islice")
    print("=" * 60)

    # --- 5a: paginate a large result set (no list materialisation) ---
    def all_records():
        """Simulate a large DB cursor."""
        for i in range(1, 10_001):
            yield {"id": i, "value": i * 2}

    page_size = 5
    page_2_start = page_size   # page index 1 (0-based)

    page_2 = list(islice(all_records(), page_2_start, page_2_start + page_size))
    print("Page 2 records:", page_2)
    # [{'id':6,'value':12}, ..., {'id':10,'value':20}]

    # --- 5b: take only the first N items from a pipeline ---
    import itertools
    counter = itertools.count(start=0, step=3)   # 0, 3, 6, 9, ...
    first_ten_multiples_of_3 = list(islice(counter, 10))
    print("First 10 multiples of 3:", first_ten_multiples_of_3)
    # [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]

    # --- 5c: evenly skip over a header row ---
    csv_lines = ["name,age,city", "Alice,30,NYC", "Bob,25,LA", "Carol,35,Chicago"]
    data_rows = list(islice(csv_lines, 1, None))   # skip index 0
    print("CSV without header:", data_rows)
    # ["Alice,30,NYC", "Bob,25,LA", "Carol,35,Chicago"]

    print()


# ---------------------------------------------------------------------------
# 6. accumulate — running totals, prefix sums, running max/min
# ---------------------------------------------------------------------------

def demo_accumulate():
    print("=" * 60)
    print("accumulate")
    print("=" * 60)

    # --- 6a: running total of daily sales ---
    daily_sales = [120, 85, 200, 95, 175, 160, 140]
    cumulative  = list(accumulate(daily_sales))
    print("Daily sales:     ", daily_sales)
    print("Cumulative sales:", cumulative)
    # [120, 205, 405, 500, 675, 835, 975]

    # --- 6b: prefix sum for fast range sum queries ---
    prices = [10, 20, 30, 40, 50]
    prefix = [0] + list(accumulate(prices))
    print("\nPrices prefix sum:", prefix)

    def range_sum(l, r):
        """Sum of prices[l..r] inclusive in O(1)."""
        return prefix[r + 1] - prefix[l]

    print("Sum prices[1..3]:", range_sum(1, 3))   # 20+30+40 = 90
    print("Sum prices[0..4]:", range_sum(0, 4))   # 150

    # --- 6c: running maximum (e.g. tracking all-time high stock price) ---
    stock_prices = [100, 95, 110, 105, 115, 108, 120]
    running_high = list(accumulate(stock_prices, func=max))
    print("\nStock prices: ", stock_prices)
    print("Running high:  ", running_high)
    # [100, 100, 110, 110, 115, 115, 120]

    # --- 6d: compound interest (initializer argument) ---
    monthly_returns = [0.01, 0.02, -0.005, 0.015, 0.008]
    balance = list(accumulate(monthly_returns, func=lambda acc, r: acc * (1 + r), initial=1000))
    print("\nPortfolio balance over months:", [round(b, 2) for b in balance])
    # [1000, 1010.0, 1030.2, 1025.05, ...]

    print()


# ---------------------------------------------------------------------------
# 7. cycle and takewhile / dropwhile
# ---------------------------------------------------------------------------

def demo_cycle_and_filters():
    print("=" * 60)
    print("cycle  /  takewhile  /  dropwhile")
    print("=" * 60)

    # --- 7a: round-robin load balancer ---
    servers = ["server-A", "server-B", "server-C"]
    server_cycle = cycle(servers)
    requests = [f"req-{i}" for i in range(7)]

    print("Load balancing 7 requests across 3 servers:")
    for req in requests:
        server = next(server_cycle)
        print(f"  {req} -> {server}")
    # req-0->server-A, req-1->server-B, req-2->server-C, req-3->server-A, ...

    # --- 7b: repeating a colour palette for chart series ---
    palette  = cycle(["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"])
    series   = ["Revenue", "Cost", "Profit", "Tax", "Net"]
    assigned = {name: next(palette) for name in series}
    print("\nChart colour assignments:", assigned)

    # --- 7c: takewhile — process a sorted list up to a threshold ---
    bids = [500, 480, 460, 430, 400, 320, 250]   # sorted descending
    high_bids = list(takewhile(lambda b: b >= 400, bids))
    print("\nBids at or above 400:", high_bids)   # [500, 480, 460, 430, 400]

    # --- 7d: dropwhile — skip leading zeros in a price series ---
    series_with_zeros = [0, 0, 0, 5, 12, 8, 0, 3]
    active_prices = list(dropwhile(lambda x: x == 0, series_with_zeros))
    print("Prices after leading zeros:", active_prices)   # [5, 12, 8, 0, 3]
    # (trailing zero is kept — only leading zeros are dropped)

    print()


# ---------------------------------------------------------------------------
# 8. zip_longest and starmap
# ---------------------------------------------------------------------------

def demo_zip_longest_and_starmap():
    print("=" * 60)
    print("zip_longest  /  starmap")
    print("=" * 60)

    # --- 8a: merge two sales lists of different lengths ---
    q3_sales = [100, 200, 150]
    q4_sales = [130, 180, 220, 95]

    print("Quarter comparison (missing Q3 values filled with 0):")
    for q3, q4 in zip_longest(q3_sales, q4_sales, fillvalue=0):
        diff = q4 - q3
        print(f"  Q3={q3:3d}  Q4={q4:3d}  diff={diff:+d}")
    # Q3=100  Q4=130  diff=+30
    # Q3=200  Q4=180  diff=-20
    # Q3=150  Q4=220  diff=+70
    # Q3=  0  Q4= 95  diff=+95

    # --- 8b: starmap — apply a function to each tuple in a list ---
    discount_rules = [
        (1000, 0.05),   # (order_value, discount_rate)
        (500,  0.03),
        (200,  0.00),
    ]
    discounts = list(starmap(lambda val, rate: val * rate, discount_rules))
    print("\nDiscount amounts:", discounts)   # [50.0, 15.0, 0.0]

    # --- 8c: starmap with operator for clean arithmetic ---
    pairs = [(10, 3), (20, 4), (15, 5)]
    print("Powers:", list(starmap(operator.pow, pairs)))    # [1000, 160000, 759375]
    print("Quotients:", list(starmap(operator.truediv, pairs)))  # [3.33, 5.0, 3.0]

    print()


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    demo_chain()
    demo_combinations_and_permutations()
    demo_product()
    demo_groupby()
    demo_islice()
    demo_accumulate()
    demo_cycle_and_filters()
    demo_zip_longest_and_starmap()
