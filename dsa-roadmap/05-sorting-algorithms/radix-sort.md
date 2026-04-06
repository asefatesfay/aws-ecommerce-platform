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

### Visual Example (base 10)

```
Input: [170, 45, 75, 90, 802, 24, 2, 66]

Pass 1 (Sort by ones digit):
  One's: 0  1  2  3  4  5  6  7  8  9
         ↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓
  [170][__][2,802][__][24,45][75][66][__][90][__]
  After: [170, 90, 802, 2, 24, 45, 75, 66]

Pass 2 (Sort by tens digit on above):
  Ten's: 0  1  2  3  4  5  6  7  8  9
         ↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓
  [802,2][__][24][__][45][66][__][170,75][__][90]
  After: [802, 2, 24, 45, 66, 170, 75, 90]

Pass 3 (Sort by hundreds digit on above):
  Hundred's: 0  1     2     3  4  5  6  7  8  9
             ↓  ↓     ↓     ↓  ↓  ↓  ↓  ↓  ↓  ↓
  [2,24,45,66,75,90][170][__][__][__][__][__][__][802][__]
  After: [2, 24, 45, 66, 75, 90, 170, 802] ✓
```

## Complexity

| Case | Time | Space |
|------|------|-------|
| All cases | O(d × (n + b)) | O(n + b) |

Where d = number of digits, b = base (radix), n = number of elements.

## Python Implementation

```python
def radix_sort(nums):
   if not nums:
      return []
   if any(x < 0 for x in nums):
      raise ValueError("radix_sort example assumes non-negative integers")

   arr = nums[:]
   exp = 1
   max_val = max(arr)

   while max_val // exp > 0:
      count = [0] * 10

      for x in arr:
         digit = (x // exp) % 10
         count[digit] += 1

      for i in range(1, 10):
         count[i] += count[i - 1]

      out = [0] * len(arr)
      for x in reversed(arr):
         digit = (x // exp) % 10
         count[digit] -= 1
         out[count[digit]] = x

      arr = out
      exp *= 10

   return arr

# Example
result = radix_sort([170, 45, 75, 90, 802, 24, 2, 66])
# Output: [2, 24, 45, 66, 75, 90, 170, 802]
```

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

## Typical Interview Use Cases

- Non-negative integer sorting with bounded digit count
- Linear-time sorting alternatives to comparison sorts
- Problems where sorting cost must beat O(n log n)
