# Majority Element

**Difficulty:** Easy
**Pattern:** Boyer-Moore Voting / Hash Map
**LeetCode:** #169

## Problem Statement

Given an array `nums` of size `n`, return the majority element. The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.

## Examples

### Example 1
**Input:** `nums = [3, 2, 3]`
**Output:** `3`

### Example 2
**Input:** `nums = [2, 2, 1, 1, 1, 2, 2]`
**Output:** `2`

## Constraints
- `n == nums.length`
- `1 <= n <= 5 * 10^4`
- `-10^9 <= nums[i] <= 10^9`
- The majority element always exists

## Hints

> 💡 **Hint 1:** The brute force is O(n²). A HashMap counting frequencies gives O(n) time and O(n) space. Can you do O(1) space?

> 💡 **Hint 2:** Think about the Boyer-Moore Voting Algorithm. The majority element appears more than n/2 times, so it "outvotes" all other elements combined.

> 💡 **Hint 3:** Maintain a candidate and a count. When count is 0, set the current element as the new candidate. If the current element matches the candidate, increment count; otherwise decrement. The final candidate is the majority element.

## Approach 1: Brute Force (Hash Map)

**Time Complexity:** O(n)
**Space Complexity:** O(n)

Count frequencies, return the element with count > n/2.

```python
from collections import Counter

def majority_element_brute(nums: list[int]) -> int:
    counts = Counter(nums)
    return max(counts, key=counts.get)
```

**Downside:** O(n) extra space. Can we do O(1)?

---

## Approach 2: Sort

**Time Complexity:** O(n log n)
**Space Complexity:** O(1) (in-place sort)

The majority element always occupies the middle index after sorting.

```python
def majority_element_sort(nums: list[int]) -> int:
    nums.sort()
    return nums[len(nums) // 2]
```

**Why it works:** If an element appears > n/2 times, it must occupy index n//2 after sorting.

---

## Approach 3: Boyer-Moore Voting — Optimal

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Maintain a candidate and a vote count. The majority element's votes can never be fully cancelled by minority elements.

### Visual Trace

```
nums = [2, 2, 1, 1, 1, 2, 2]

i=0, x=2: count=0 → candidate=2, count=1
i=1, x=2: x==candidate → count=2
i=2, x=1: x≠candidate → count=1
i=3, x=1: x≠candidate → count=0
i=4, x=1: count=0 → candidate=1, count=1
i=5, x=2: x≠candidate → count=0
i=6, x=2: count=0 → candidate=2, count=1

Final candidate: 2 ✓
```

```python
def majority_element(nums: list[int]) -> int:
    candidate = None
    count = 0
    for x in nums:
        if count == 0:
            candidate = x
            count = 1
        elif x == candidate:
            count += 1
        else:
            count -= 1
    return candidate
```

### Complexity Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Hash map | O(n) | O(n) | Simple, extra space |
| Sort | O(n log n) | O(1) | Modifies array |
| Boyer-Moore | O(n) | O(1) | Optimal |

## Typical Interview Use Cases

- Majority threshold > n/2 with guaranteed existence
- Core example for cancellation/invariant proof techniques
- Stepping stone to n/3 and generalized voting variants

