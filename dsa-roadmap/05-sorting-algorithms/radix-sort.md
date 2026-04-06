# Radix Sort

**Type:** Non-comparison, digit-by-digit sort
**Stable:** Yes

## Concept

Sort integers digit by digit, from least significant digit (LSD) to most significant digit (MSD), using a stable sort (typically Counting Sort) at each digit position. Because each pass is stable, the relative order from previous passes is preserved.

## How It Works

For d-digit numbers with digits in base b:

1. For each digit position (from LSD to MSD):
   - Use Counting Sort to sort by that digit only
   - Stability ensures previously sorted digits remain in order
2. After processing all d digits, the array is fully sorted

**Example with base 10:**
Input: [170, 45, 75, 90, 802, 24, 2, 66]
After ones digit: [170, 90, 802, 2, 24, 45, 75, 66]
After tens digit: [802, 2, 24, 45, 66, 170, 75, 90]
After hundreds digit: [2, 24, 45, 66, 75, 90, 170, 802]

## Complexity

| Case | Time | Space |
|------|------|-------|
| All cases | O(d × (n + b)) | O(n + b) |

Where d = number of digits, b = base (radix), n = number of elements.

For fixed-width integers: d = O(log_b(max_value)), so total is O(n × log_b(max_value)).

With b = n: O(n × log_n(max_value)) which approaches O(n) for bounded integers.

## When to Use

- Sorting integers or strings of fixed length
- When keys have a natural digit/character decomposition
- Large datasets where O(n log n) comparison sorts are too slow
- Sorting strings lexicographically (MSD Radix Sort)

## LSD vs MSD Radix Sort

- **LSD (Least Significant Digit):** Process right-to-left. Simpler, naturally iterative. Good for fixed-length keys.
- **MSD (Most Significant Digit):** Process left-to-right. Can short-circuit early. Better for variable-length strings.

## Key Insight

Radix Sort achieves linear time by exploiting the structure of integer representation. The catch: it only works for keys that can be decomposed into digits/characters. It's not a general-purpose sort.

## Interview Relevance

Radix Sort appears in "Maximum Gap" (LeetCode 164) where it enables O(n) sorting. Understanding it helps recognize when linear-time sorting is possible.
