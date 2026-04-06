# Bucket Sort

**Type:** Non-comparison, distribution sort
**Stable:** Yes (if stable sort used within buckets)

## Concept

Distribute elements into a number of buckets based on their value range, sort each bucket individually (usually with Insertion Sort), then concatenate the buckets. Works best when input is uniformly distributed over a range.

## How It Works

Given n elements in range [min, max]:

1. Create n empty buckets
2. Assign each element to a bucket: `bucket_index = (element - min) / (max - min) * (n - 1)`
3. Sort each bucket (Insertion Sort works well for small buckets)
4. Concatenate all buckets in order

### Visual Example

```
Input: [0.5, 0.2, 0.8, 0.1, 0.9], n=5 buckets, range [0, 1]

Bucket assignment:
  0.5 → bucket 2   Bucket[0]: [0.1]
  0.2 → bucket 1   Bucket[1]: [0.2]
  0.8 → bucket 4   Bucket[2]: [0.5]
  0.1 → bucket 0   Bucket[3]: []
  0.9 → bucket 4   Bucket[4]: [0.8, 0.9]

After sorting buckets individually:
  Bucket[0]: [0.1]       (1 element)
  Bucket[1]: [0.2]       (1 element)
  Bucket[2]: [0.5]       (1 element)
  Bucket[3]: []          (empty)
  Bucket[4]: [0.8, 0.9]  (sorted)

Concatenate: [0.1, 0.2, 0.5, 0.8, 0.9] ✓
```

## Complexity

| Case | Time | Space |
|------|------|-------|
| Best / Average (uniform) | O(n + k) | O(n + k) |
| Worst (all in one bucket) | O(n²) | O(n) |

Where k is the number of buckets.

## Python Implementation

```python
def bucket_sort(nums):
	if len(nums) <= 1:
		return nums[:]

	min_val = min(nums)
	max_val = max(nums)

	if min_val == max_val:
		return nums[:]

	n = len(nums)
	buckets = [[] for _ in range(n)]

	for x in nums:
		idx = int((x - min_val) * (n - 1) / (max_val - min_val))
		buckets[idx].append(x)

	out = []
	for b in buckets:
		out.extend(sorted(b))

	return out

# Example
result = bucket_sort([0.5, 0.2, 0.8, 0.1, 0.9])
# Output: [0.1, 0.2, 0.5, 0.8, 0.9]
```

## When to Use

- Input is uniformly distributed over a known range
- Sorting floating-point numbers in [0, 1)
- When average-case O(n) is acceptable and distribution is known
- As a generalization of Counting Sort for non-integer keys

## When NOT to Use

- Skewed distributions (most elements cluster in one bucket → degrades to O(n²))
- Unknown or highly variable distributions
- When worst-case guarantee is needed

## Key Insight

The efficiency of Bucket Sort depends entirely on how evenly elements are distributed across buckets. With uniform distribution and n buckets for n elements, each bucket has O(1) elements on average, making the per-bucket sort O(1) and total sort O(n).

## Comparison with Counting Sort

Counting Sort is a special case of Bucket Sort where each bucket holds exactly one distinct value. Bucket Sort generalizes this to ranges of values and works for non-integers.

## Typical Interview Use Cases

- Uniformly distributed floats (often in [0, 1))
- Distribution-sort discussions and assumption-based optimization
- Conceptual follow-up when Counting Sort range is too large
