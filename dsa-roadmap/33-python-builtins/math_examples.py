"""
math — Mathematical functions for real numbers.
statistics — Descriptive statistics for numeric data (Python 3.4+).

Covered here (math):
  Constants       — pi, e, tau, inf, nan
  Rounding        — ceil, floor, trunc, fabs
  Powers & logs   — sqrt, pow, exp, log, log2, log10
  Combinatorics   — factorial, comb, perm
  Trigonometry    — sin, cos, tan, asin, acos, atan, atan2, degrees, radians, hypot
  Number theory   — gcd, lcm, isclose, isfinite, isinf, isnan, copysign
  Miscellaneous   — prod (3.8+), dist (3.8+), fsum (exact floating sum)

Covered here (statistics):
  Central tendency — mean, fmean, geometric_mean, harmonic_mean, median, mode, multimode
  Spread           — variance, stdev, pvariance, pstdev
  Quantiles        — quantiles, median_low, median_high, median_grouped
  Correlation      — correlation, covariance, linear_regression (3.10+)
  Distributions    — NormalDist
"""

import math
import statistics


# ---------------------------------------------------------------------------
# 1. Constants
# ---------------------------------------------------------------------------

def demo_constants():
    print("=" * 60)
    print("math constants")
    print("=" * 60)

    print(f"pi    = {math.pi}")       # 3.141592653589793
    print(f"e     = {math.e}")        # 2.718281828459045
    print(f"tau   = {math.tau}")      # 6.283185307179586  (2*pi)
    print(f"inf   = {math.inf}")      # inf
    print(f"-inf  = {-math.inf}")     # -inf
    print(f"nan   = {math.nan}")      # nan

    # Guard checks
    print("\nisfinite(3.14):", math.isfinite(3.14))       # True
    print("isinf(math.inf):", math.isinf(math.inf))      # True
    print("isnan(math.nan):", math.isnan(math.nan))       # True
    print("isnan(0.0):     ", math.isnan(0.0))            # False

    print()


# ---------------------------------------------------------------------------
# 2. Rounding and absolute value
# ---------------------------------------------------------------------------

def demo_rounding():
    print("=" * 60)
    print("Rounding: ceil, floor, trunc, fabs")
    print("=" * 60)

    values = [3.2, 3.7, -3.2, -3.7, 0.0]
    print(f"{'value':>8}  {'ceil':>6}  {'floor':>6}  {'trunc':>6}  {'fabs':>6}")
    for v in values:
        print(f"  {v:6.1f}  {math.ceil(v):>6}  {math.floor(v):>6}  "
              f"{math.trunc(v):>6}  {math.fabs(v):>6.1f}")

    # ceil vs floor for e-commerce quantity rounding
    order_weight_kg = 7.3
    boxes_needed    = math.ceil(order_weight_kg / 3)   # each box holds 3 kg
    print(f"\n{order_weight_kg} kg ÷ 3 kg per box -> {boxes_needed} boxes needed")

    # fsum for accurate floating-point summation
    prices = [0.1, 0.2, 0.3]
    naive      = sum(prices)
    accurate   = math.fsum(prices)
    print(f"\nsum({prices})  = {naive}")       # 0.6000000000000001  (float error)
    print(f"fsum({prices}) = {accurate}")      # 0.6

    print()


# ---------------------------------------------------------------------------
# 3. Powers, roots, and logarithms
# ---------------------------------------------------------------------------

def demo_powers_and_logs():
    print("=" * 60)
    print("Powers, roots, logarithms")
    print("=" * 60)

    # sqrt
    print(f"sqrt(144)     = {math.sqrt(144)}")       # 12.0
    print(f"sqrt(2)       = {math.sqrt(2):.6f}")     # 1.414214

    # Integer square root (no float rounding)
    print(f"isqrt(143)    = {math.isqrt(143)}")       # 11
    print(f"isqrt(144)    = {math.isqrt(144)}")       # 12

    # pow — uses float; use ** for exact integer exponentiation
    print(f"pow(2, 10)    = {math.pow(2, 10)}")       # 1024.0
    print(f"pow(2, -1)    = {math.pow(2, -1)}")       # 0.5

    # exp and log
    print(f"\nexp(1)        = {math.exp(1):.6f}")      # e^1 = 2.718282
    print(f"exp(0)        = {math.exp(0)}")            # 1.0
    print(f"log(math.e)   = {math.log(math.e)}")      # 1.0  (natural log)
    print(f"log(100, 10)  = {math.log(100, 10)}")     # 2.0
    print(f"log2(1024)    = {math.log2(1024)}")        # 10.0
    print(f"log10(1000)   = {math.log10(1000)}")       # 3.0

    # DSA: number of digits in an integer
    n = 1_234_567
    digits = math.floor(math.log10(n)) + 1
    print(f"\n# digits in {n}: {digits}")   # 7

    # DSA: minimum number of bits to represent n
    n = 255
    bits = math.floor(math.log2(n)) + 1
    print(f"Bits to represent {n}: {bits}")   # 8

    # hypot — Euclidean distance without overflow risk
    x, y = 3, 4
    dist = math.hypot(x, y)
    print(f"\nhypot({x},{y}) = {dist}")   # 5.0

    # 3D distance
    dist_3d = math.dist((1, 2, 3), (4, 6, 3))
    print(f"dist((1,2,3),(4,6,3)) = {dist_3d}")   # 5.0

    print()


# ---------------------------------------------------------------------------
# 4. Combinatorics — factorial, comb, perm
# ---------------------------------------------------------------------------

def demo_combinatorics():
    print("=" * 60)
    print("Combinatorics: factorial, comb, perm")
    print("=" * 60)

    print("Factorials:")
    for n in range(8):
        print(f"  {n}! = {math.factorial(n)}")

    # comb(n, k) — "n choose k", useful for probability and combinations
    print("\nCombinations C(n,k) [order doesn't matter]:")
    print(f"  C(10,2) = {math.comb(10, 2)}")    # 45  lottery pairs
    print(f"  C(52,5) = {math.comb(52, 5)}")    # 2598960  poker hands
    print(f"  C(6,6)  = {math.comb(6,  6)}")    # 1

    # perm(n, k) — ordered arrangements
    print("\nPermutations P(n,k) [order matters]:")
    print(f"  P(10,3) = {math.perm(10, 3)}")    # 720  top-3 podium from 10 runners
    print(f"  P(5,5)  = {math.perm(5,  5)}")    # 120  = 5!

    # DSA: Pascal's triangle row using comb
    n = 6
    row = [math.comb(n, k) for k in range(n + 1)]
    print(f"\nPascal's triangle row {n}: {row}")   # [1,6,15,20,15,6,1]

    print()


# ---------------------------------------------------------------------------
# 5. Number theory — gcd, lcm, isclose, copysign
# ---------------------------------------------------------------------------

def demo_number_theory():
    print("=" * 60)
    print("Number theory: gcd, lcm, isclose, copysign")
    print("=" * 60)

    print(f"gcd(48, 18)   = {math.gcd(48, 18)}")       # 6
    print(f"gcd(100, 75)  = {math.gcd(100, 75)}")      # 25
    print(f"gcd(7, 13)    = {math.gcd(7, 13)}")        # 1  (coprime)

    # gcd with multiple arguments (Python 3.9+)
    print(f"gcd(48,36,24) = {math.gcd(48, 36, 24)}")   # 12

    print(f"\nlcm(4, 6)    = {math.lcm(4, 6)}")         # 12
    print(f"lcm(3, 5, 7) = {math.lcm(3, 5, 7)}")       # 105

    # Fraction simplification
    numerator, denominator = 18, 48
    g = math.gcd(numerator, denominator)
    print(f"\n{numerator}/{denominator} simplified = {numerator//g}/{denominator//g}")

    # isclose — safe floating-point equality
    a = 0.1 + 0.2
    b = 0.3
    print(f"\n0.1 + 0.2 == 0.3:          {a == b}")              # False
    print(f"isclose(a, b):             {math.isclose(a, b)}")    # True
    print(f"isclose(1.0, 1.001, rtol=1e-2): {math.isclose(1.0, 1.001, rel_tol=1e-2)}")

    # copysign — apply sign of one number to another
    print(f"\ncopysign(5, -3)  = {math.copysign(5, -3)}")   # -5.0
    print(f"copysign(-5, 3)  = {math.copysign(-5, 3)}")    # 5.0

    print()


# ---------------------------------------------------------------------------
# 6. Trigonometry
# ---------------------------------------------------------------------------

def demo_trigonometry():
    print("=" * 60)
    print("Trigonometry")
    print("=" * 60)

    angles_deg = [0, 30, 45, 60, 90, 180, 270, 360]
    print(f"{'deg':>6}  {'sin':>8}  {'cos':>8}  {'radians':>10}")
    for deg in angles_deg:
        rad = math.radians(deg)
        print(f"  {deg:4d}  {math.sin(rad):>8.4f}  {math.cos(rad):>8.4f}  {rad:>10.4f}")

    # atan2 — angle from origin to point (handles all quadrants)
    print("\natan2 examples:")
    for point in [(1, 1), (-1, 1), (-1, -1), (1, -1), (3, 4)]:
        x, y = point
        angle = math.degrees(math.atan2(y, x))
        print(f"  atan2({y},{x}) = {angle:.2f}°")

    print()


# ---------------------------------------------------------------------------
# 7. math.prod and math.perm for DSA shortcuts
# ---------------------------------------------------------------------------

def demo_math_shortcuts():
    print("=" * 60)
    print("math.prod  (Python 3.8+) and other DSA shortcuts")
    print("=" * 60)

    # math.prod — product of an iterable
    print("prod([1,2,3,4,5])    =", math.prod([1, 2, 3, 4, 5]))   # 120
    print("prod([1,2,3], start=10)=", math.prod([1, 2, 3], start=10))  # 60

    # Useful for computing permutations manually
    # P(10,3) = 10 * 9 * 8
    p = math.prod(range(10, 7, -1))
    print("P(10,3) =", p)   # 720

    # pow with modulo — fast modular exponentiation
    # pow(base, exp, mod) is O(log exp) — crucial for DSA
    print("\nModular exponentiation:")
    print("pow(2, 100, 10**9+7) =", pow(2, 100, 10**9 + 7))   # 976371285
    # Built-in pow with 3 args is faster than math.pow for this

    # Check if n is a perfect square
    def is_perfect_square(n: int) -> bool:
        if n < 0:
            return False
        root = math.isqrt(n)
        return root * root == n

    for n in [0, 1, 4, 9, 15, 16, 25, 26]:
        print(f"  is_perfect_square({n:2d}) = {is_perfect_square(n)}")

    print()


# ---------------------------------------------------------------------------
# 8. statistics — descriptive statistics
# ---------------------------------------------------------------------------

def demo_statistics_basics():
    print("=" * 60)
    print("statistics — central tendency and spread")
    print("=" * 60)

    response_times = [120, 145, 98, 210, 135, 155, 102, 190, 125, 175,
                      140, 108, 95, 230, 160, 115, 185, 145, 165, 130]

    print("Response times (ms):", sorted(response_times))
    print()

    # Central tendency
    print(f"mean             = {statistics.mean(response_times):.2f}")
    print(f"fmean            = {statistics.fmean(response_times):.2f}")   # faster, float output
    print(f"geometric_mean   = {statistics.geometric_mean(response_times):.2f}")
    print(f"harmonic_mean    = {statistics.harmonic_mean(response_times):.2f}")
    print(f"median           = {statistics.median(response_times)}")
    print(f"median_low       = {statistics.median_low(response_times)}")
    print(f"median_high      = {statistics.median_high(response_times)}")

    # Mode
    votes = [3, 1, 2, 3, 3, 1, 2, 1, 3, 2, 2]
    print(f"\nmode ({votes})    = {statistics.mode(votes)}")
    print(f"multimode        = {statistics.multimode([1,1,2,2,3])}")   # [1,2]

    # Spread
    print(f"\nvariance         = {statistics.variance(response_times):.2f}")
    print(f"stdev            = {statistics.stdev(response_times):.2f}")
    print(f"pvariance        = {statistics.pvariance(response_times):.2f}")
    print(f"pstdev           = {statistics.pstdev(response_times):.2f}")

    print()


# ---------------------------------------------------------------------------
# 9. statistics — quantiles, correlation, linear regression
# ---------------------------------------------------------------------------

def demo_statistics_advanced():
    print("=" * 60)
    print("statistics — quantiles, correlation, regression")
    print("=" * 60)

    scores = [45, 50, 55, 60, 63, 67, 70, 72, 75, 78,
              80, 82, 85, 87, 90, 92, 94, 96, 98, 100]

    # Quartiles (4 equal parts)
    q = statistics.quantiles(scores, n=4)
    print(f"Quartiles of exam scores: Q1={q[0]}, Q2={q[1]}, Q3={q[2]}")
    iqr = q[2] - q[0]
    print(f"IQR = {iqr}")

    # Deciles
    deciles = statistics.quantiles(scores, n=10)
    print(f"10th percentile: {deciles[0]}")
    print(f"90th percentile: {deciles[8]}")

    # Correlation and covariance
    ad_spend    = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550]
    revenue     = [120, 180, 195, 280, 310, 350, 420, 440, 510, 560]

    corr = statistics.correlation(ad_spend, revenue)
    cov  = statistics.covariance(ad_spend, revenue)
    print(f"\nAd spend vs Revenue:")
    print(f"  Correlation  = {corr:.4f}")   # close to 1.0 (strong positive)
    print(f"  Covariance   = {cov:.2f}")

    # Linear regression
    slope, intercept = statistics.linear_regression(ad_spend, revenue)
    print(f"  y = {slope:.4f}x + {intercept:.4f}")
    predicted_600 = slope * 600 + intercept
    print(f"  Predicted revenue at $600 spend: ${predicted_600:.2f}")

    # NormalDist — model a normal distribution
    heights = statistics.NormalDist(mu=175.0, sigma=8.0)   # cm
    print(f"\nHeight distribution N(175, 8):")
    print(f"  P(height < 183) = {heights.cdf(183):.4f}")    # ~84%
    print(f"  P(height > 167) = {1 - heights.cdf(167):.4f}")
    print(f"  P(160 < h < 190) = {heights.cdf(190) - heights.cdf(160):.4f}")
    print(f"  95th percentile  = {heights.inv_cdf(0.95):.2f} cm")
    print(f"  z-score of 183   = {heights.zscore(183):.2f}")

    print()


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    demo_constants()
    demo_rounding()
    demo_powers_and_logs()
    demo_combinatorics()
    demo_number_theory()
    demo_trigonometry()
    demo_math_shortcuts()
    demo_statistics_basics()
    demo_statistics_advanced()
