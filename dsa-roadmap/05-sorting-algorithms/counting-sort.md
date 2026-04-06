# Counting Sort

**Type:** Non-comparison, integer sort
**Stable:** Yes

## Concept

Instead of comparing elements, count the occurrences of each distinct value. Use these counts to determine the correct position of each element in the output array. Works only for integer keys within a known, bounded range.

## How It Works

Given array with values in range [0, k]:

1. Create a count array of size k+1, initialized to 0
2. Count occurrences: for each element x, increment count[x]
3. Compute prefix sums: count[i] += count[i-1] — now count[i] = number of elements ≤ i
4. Build output: iterate input right-to-left, place each element at position count[x]-1, decrement count[x]

The right-to-left iteration in step 4 is what makes it stable.

### Visual Example

```
Input: [4, 2, 2, 8, 3, 3, 1], range [1, 8]

Step 1: Count occurrences
  count[1]=1, count[2]=2, count[3]=2, count[4]=1, count[8]=1
  count = [0, 1, 2, 2, 1, 0, 0, 0, 1]

Step 2: Prefix sum (cumulative)
  count = [0, 1, 3, 5, 6, 6, 6, 6, 7]
  │ means: ≤ 1 go to index 1, ≤ 2 go to indices 1-3, etc.

Step 3: Build output (right-to-left for stability)
  Process 1: place at index count[1]-1=0 → out[0]=1
  Process 3: place at index count[3]-1=4 → out[4]=3
  Process 3: place at index count[3]-1=3 → out[3]=3 (count[3]-- )
  Process 8: place at index count[8]-1=6 → out[6]=8
  … etc
  
Output: [1, 2, 2, 3, 3, 4, 8] ✓
```

## Complexity

| Case | Time | Space |
|------|------|-------|
| All cases | O(n + k) | O(n + k) |

Where k is the range of input values.

## Python Implementation

```python
def counting_sort(nums):
	if not nums:
		return []

	min_val = min(nums)
	max_val = max(nums)
	offset = -min_val
	k = max_val - min_val + 1

	count = [0] * k
	for x in nums:
		count[x + offset] += 1

	for i in range(1, k):
		count[i] += count[i - 1]

	out = [0] * len(nums)
	for x in reversed(nums):  # right-to-left keeps stability
		idx = x + offset
		count[idx] -= 1
		out[count[idx]] = x

	return out

# Example
result = counting_sort([4, 2, 2, 8, 3, 3, 1])
# Output: [1, 2, 2, 3, 3, 4, 8]
```

## When to Use

- Integer keys in a small, known range (k is not much larger than n)
- When stability is required and keys are integers
- As a subroutine in Radix Sort
- Sorting characters (k = 26 for lowercase letters)

## When NOT to Use

- Large range k (e.g., sorting 32-bit integers — k = 4 billion)
- Non-integer keys
- When memory is constrained and k >> n

## Key Insight

Counting Sort breaks the O(n log n) lower bound for comparison sorts because it doesn't compare elements — it exploits the structure of integer keys. The trade-off is the O(k) space requirement.

## Example

Input: [4, 2, 2, 8, 3, 3, 1], range [1, 8]
Count: [0, 1, 2, 2, 1, 0, 0, 0, 1] (indices 0-8)
After prefix sum: [0, 1, 3, 5, 6, 6, 6, 6, 7]
Output built right-to-left: [1, 2, 2, 3, 3, 4, 8]

## Typical Interview Use Cases

- Integer arrays with small value range
- Frequency-based reordering questions
- Stable subroutine inside Radix Sort
