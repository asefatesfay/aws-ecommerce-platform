"""
random — Pseudo-random number generation.

Important: random is NOT cryptographically secure.
           Use the `secrets` module for passwords, tokens, and security.

Covered here:
  Seeding           — seed, getstate, setstate (reproducible runs)
  Integers          — randint, randrange, getrandbits
  Floats            — random, uniform, triangular, gauss, normalvariate,
                      expovariate, betavariate
  Sequences         — choice, choices (weighted), shuffle, sample
  DSA patterns      — random graph, random test data generation, randomised
                      algorithms (Quickselect, reservoir sampling)
"""

import random


# ---------------------------------------------------------------------------
# 1. Seeding — reproducible randomness
# ---------------------------------------------------------------------------

def demo_seeding():
    print("=" * 60)
    print("Seeding for reproducibility")
    print("=" * 60)

    # Any code that calls random functions after random.seed(n) is reproducible
    random.seed(42)
    run_1 = [random.randint(1, 100) for _ in range(5)]

    random.seed(42)
    run_2 = [random.randint(1, 100) for _ in range(5)]

    print("Run 1:", run_1)
    print("Run 2:", run_2)
    print("Identical:", run_1 == run_2)   # True

    # Save and restore state (useful in tests)
    state = random.getstate()
    a = random.random()
    random.setstate(state)
    b = random.random()
    print(f"\nSame state -> same value: {a:.6f} == {b:.6f} -> {a == b}")

    print()


# ---------------------------------------------------------------------------
# 2. Integer generation
# ---------------------------------------------------------------------------

def demo_integers():
    print("=" * 60)
    print("Integer generation: randint, randrange, getrandbits")
    print("=" * 60)

    random.seed(0)

    # randint(a, b) — inclusive on both ends
    dice_rolls = [random.randint(1, 6) for _ in range(10)]
    print("Dice rolls:", dice_rolls)

    # randrange(start, stop[, step]) — like range(), exclusive of stop
    even = [random.randrange(0, 20, 2) for _ in range(5)]
    print("Random even numbers [0,18]:", even)

    multiples_of_5 = [random.randrange(5, 50, 5) for _ in range(5)]
    print("Random multiples of 5:", multiples_of_5)

    # getrandbits — generate a random integer with exactly n bits
    random_id = random.getrandbits(32)
    print(f"\nRandom 32-bit ID: {random_id}")
    print(f"In hex: 0x{random_id:08X}")

    # Simulate a coin flip distribution
    random.seed(1)
    flips = [random.randint(0, 1) for _ in range(1000)]
    heads = flips.count(1)
    print(f"\n1000 coin flips: {heads} heads ({heads/10:.1f}%)")   # ~50%

    print()


# ---------------------------------------------------------------------------
# 3. Float generation
# ---------------------------------------------------------------------------

def demo_floats():
    print("=" * 60)
    print("Float generation: random, uniform, triangular, gauss")
    print("=" * 60)

    random.seed(7)

    # random() — [0.0, 1.0)
    unit = [round(random.random(), 3) for _ in range(5)]
    print("random() samples:", unit)

    # uniform(a, b) — [a, b] or [a, b)
    prices = [round(random.uniform(9.99, 99.99), 2) for _ in range(5)]
    print("Random prices [$9.99-$99.99]:", prices)

    # triangular(low, high, mode) — triangle distribution
    # Useful for simulating wait times, delivery windows
    delivery_minutes = [round(random.triangular(10, 60, 30)) for _ in range(5)]
    print("Delivery times (triangular 10-60, peak 30min):", delivery_minutes)

    # gauss(mu, sigma) — faster than normalvariate, not thread-safe
    # normalvariate(mu, sigma) — thread-safe
    heights_cm = [round(random.normalvariate(175, 8), 1) for _ in range(8)]
    print("\nSimulated heights N(175,8):", heights_cm)

    response_ms = [round(random.gauss(150, 30)) for _ in range(8)]
    print("Simulated response times gauss(150,30):", response_ms)

    # expovariate(lambd) — exponential distribution (arrival/inter-event times)
    # lambd = 1/mean, e.g. lambd=0.1 means mean=10 seconds between events
    inter_arrivals = [round(random.expovariate(0.1), 2) for _ in range(8)]
    print("\nInter-arrival times expovariate(0.1):", inter_arrivals)

    # betavariate(alpha, beta) — values in [0,1], useful for proportions
    proportions = [round(random.betavariate(2, 5), 3) for _ in range(8)]
    print("Beta(2,5) proportions:", proportions)

    print()


# ---------------------------------------------------------------------------
# 4. Sequences — choice, choices, shuffle, sample
# ---------------------------------------------------------------------------

def demo_sequences():
    print("=" * 60)
    print("Sequences: choice, choices, shuffle, sample")
    print("=" * 60)

    random.seed(99)

    # choice — pick one element uniformly
    teams = ["Alpha", "Beta", "Gamma", "Delta"]
    winner = random.choice(teams)
    print("Random winner:", winner)

    # choices — pick k elements WITH replacement, optional weights
    colours = ["red", "blue", "green"]
    weights = [5, 3, 1]   # red is 5x more likely than green
    picks = random.choices(colours, weights=weights, k=20)
    from collections import Counter
    print("Weighted choices (20 picks):", dict(Counter(picks).most_common()))
    # red should appear most

    # sample — pick k elements WITHOUT replacement (no duplicates)
    lottery_pool = list(range(1, 50))
    winning_numbers = sorted(random.sample(lottery_pool, 6))
    print(f"\nLottery numbers (6 from 1-49): {winning_numbers}")

    users = ["Alice", "Bob", "Carol", "Dave", "Eve", "Frank"]
    survey_group = random.sample(users, 3)
    print(f"Survey group (3 from {len(users)}): {survey_group}")

    # shuffle — randomise a list in place
    deck = list(range(1, 14))   # 13 cards
    random.shuffle(deck)
    print(f"\nShuffled deck (13 cards): {deck}")

    # Shuffling without modifying the original
    hand = ["A♠", "K♠", "Q♠", "J♠", "10♠"]
    shuffled_hand = random.sample(hand, len(hand))   # sample all = shuffle copy
    print(f"Original hand:  {hand}")
    print(f"Shuffled copy:  {shuffled_hand}")

    print()


# ---------------------------------------------------------------------------
# 5. DSA pattern: Reservoir Sampling (select k items from a stream)
# ---------------------------------------------------------------------------

def demo_reservoir_sampling():
    print("=" * 60)
    print("Reservoir Sampling  (uniform k from unknown-length stream)")
    print("=" * 60)

    # Classic Algorithm R — O(n) time, O(k) space
    # Used when you cannot fit the entire data stream in memory
    def reservoir_sample(stream, k: int) -> list:
        reservoir = []
        for i, item in enumerate(stream):
            if i < k:
                reservoir.append(item)
            else:
                j = random.randint(0, i)
                if j < k:
                    reservoir[j] = item
        return reservoir

    random.seed(42)
    stream = range(1, 1001)   # 1 to 1000 — pretend we can't see all at once
    sample = sorted(reservoir_sample(stream, 10))
    print(f"10 samples from stream of 1-1000: {sample}")
    # Each number has exactly 10/1000 = 1% probability of appearing

    # Verify uniformity with a large trial
    from collections import defaultdict
    counts = defaultdict(int)
    for _ in range(10_000):
        for item in reservoir_sample(range(1, 6), 3):   # 3 from 5
            counts[item] += 1

    print("\nUniformity check (3 from {1,2,3,4,5} over 10,000 trials):")
    for k in sorted(counts):
        print(f"  {k}: {counts[k]} times ({counts[k] / 10000 * 100:.1f}%)")
    # Each should appear ~60% of the time (3/5 = 60%)

    print()


# ---------------------------------------------------------------------------
# 6. DSA pattern: Randomised Quickselect — k-th smallest in O(n) average
# ---------------------------------------------------------------------------

def demo_quickselect():
    print("=" * 60)
    print("Randomised Quickselect  (k-th smallest, O(n) average)")
    print("=" * 60)

    def quickselect(arr: list, k: int) -> int:
        """Return the k-th smallest element (1-indexed) using randomised pivot."""
        if len(arr) == 1:
            return arr[0]

        pivot = random.choice(arr)
        low  = [x for x in arr if x < pivot]
        mid  = [x for x in arr if x == pivot]
        high = [x for x in arr if x > pivot]

        if k <= len(low):
            return quickselect(low, k)
        elif k <= len(low) + len(mid):
            return pivot
        else:
            return quickselect(high, k - len(low) - len(mid))

    random.seed(5)
    data = [3, 6, 8, 5, 13, 10, 2, 7, 1, 4, 9, 11, 12]
    print("Data:", sorted(data))
    for k in [1, 3, 5, 7, 10, 13]:
        result = quickselect(data[:], k)
        print(f"  {k}-th smallest = {result}")
    # 1->1, 3->3, 5->5, 7->7, 10->10, 13->13

    print()


# ---------------------------------------------------------------------------
# 7. DSA pattern: generate random test data
# ---------------------------------------------------------------------------

def demo_test_data():
    print("=" * 60)
    print("Generating random test data for DSA problems")
    print("=" * 60)

    random.seed(2024)

    # Random graph (adjacency list)
    def random_graph(n_nodes: int, edge_prob: float, weighted: bool = True) -> dict:
        import math as _math
        graph = {i: [] for i in range(n_nodes)}
        for u in range(n_nodes):
            for v in range(u + 1, n_nodes):
                if random.random() < edge_prob:
                    w = random.randint(1, 20) if weighted else 1
                    graph[u].append((v, w))
                    graph[v].append((u, w))
        return graph

    graph = random_graph(6, 0.4)
    print("Random graph (6 nodes, 40% edge prob):")
    for node, edges in graph.items():
        print(f"  {node}: {edges}")

    # Random sorted array (for binary search problems)
    sorted_arr = sorted(random.sample(range(-100, 100), 15))
    print(f"\nSorted array (15 elements): {sorted_arr}")

    # Random matrix
    matrix = [[random.randint(0, 9) for _ in range(4)] for _ in range(3)]
    print("\nRandom 3x4 matrix:")
    for row in matrix:
        print(" ", row)

    # Random string
    import string
    random_str = "".join(random.choices(string.ascii_lowercase, k=20))
    print(f"\nRandom lowercase string (len=20): {random_str}")

    # Near-sorted array (tests adaptive sorts)
    base = list(range(20))
    for _ in range(3):
        i, j = random.sample(range(20), 2)
        base[i], base[j] = base[j], base[i]
    print(f"Near-sorted array (3 swaps): {base}")

    print()


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    demo_seeding()
    demo_integers()
    demo_floats()
    demo_sequences()
    demo_reservoir_sampling()
    demo_quickselect()
    demo_test_data()
