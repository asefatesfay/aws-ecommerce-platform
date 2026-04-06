# Big-O Notation

Big-O notation describes how an algorithm's runtime or space usage grows as the input size grows. It's the language of algorithm analysis.

## Why It Matters

Interviewers always ask about complexity. More importantly, understanding Big-O helps you choose the right algorithm before you write a single line of code.

## Common Complexities (fastest → slowest)

| Notation | Name | Example |
|----------|------|---------|
| O(1) | Constant | Array index access, HashMap lookup |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Single loop through array |
| O(n log n) | Linearithmic | Merge sort, heap sort |
| O(n²) | Quadratic | Nested loops, bubble sort |
| O(2^n) | Exponential | Recursive subsets, brute-force combinations |
| O(n!) | Factorial | Generating all permutations |

## Rules

### Drop Constants
O(2n) → O(n). Constants don't matter at scale.

### Drop Non-Dominant Terms
O(n² + n) → O(n²). The dominant term wins.

### Different Variables for Different Inputs
If you loop over array A (size m) then array B (size n), that's O(m + n), not O(n).

### Nested Loops
Two nested loops over the same array → O(n²). Three nested → O(n³).

### Recursive Complexity
Use the recurrence relation. Binary search: T(n) = T(n/2) + O(1) → O(log n). Merge sort: T(n) = 2T(n/2) + O(n) → O(n log n).

## Space Complexity

Space complexity counts extra memory used (not including input):
- Storing n elements → O(n)
- Recursive call stack depth d → O(d) space
- In-place algorithms → O(1) space

## Amortized Complexity

Some operations are occasionally expensive but cheap on average. Dynamic array append is O(1) amortized even though resizing is O(n), because resizing happens rarely.

## Practice: Identify the Complexity

```
for i in range(n):          # O(n)
    for j in range(n):      # O(n²) total
        print(i, j)

i = n
while i > 1:                # O(log n)
    i = i // 2
```

## Key Insight

When you see a constraint like n ≤ 10^5, the interviewer is telling you O(n log n) or O(n) is expected. Use constraints to reverse-engineer the required approach.
