# Two Sum

**Difficulty:** Easy
**Pattern:** Hash Map / Complement Lookup
**LeetCode:** #1
**Asked by:** Google, Microsoft, Adobe, Amazon

## Problem Statement

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers that add up to `target`. You may assume exactly one solution exists, and you may not use the same element twice.

## Examples

### Example 1
**Input:** `nums = [2, 7, 11, 15]`, `target = 9`
**Output:** `[0, 1]`
**Explanation:** `nums[0] + nums[1] = 2 + 7 = 9`

### Example 2
**Input:** `nums = [3, 2, 4]`, `target = 6`
**Output:** `[1, 2]`
**Explanation:** `nums[1] + nums[2] = 2 + 4 = 6`

### Example 3
**Input:** `nums = [3, 3]`, `target = 6`
**Output:** `[0, 1]`

## Constraints
- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- Exactly one valid answer exists

## Hints

> 💡 **Hint 1:** For each number, you need to find `target - num`. How can you check if that complement exists in O(1)?

> 💡 **Hint 2:** Use a hash map to store `{value → index}` as you iterate. Before storing each number, check if its complement is already in the map.

> 💡 **Hint 3:** You only need one pass — check for the complement first, then store the current number. This handles the case where both numbers are the same (e.g., [3,3], target=6).

## Approach 1: Brute Force

**Time Complexity:** O(n²)
**Space Complexity:** O(1)

Check every pair of elements.

```python
def two_sum_brute(nums: list[int], target: int) -> list[int]:
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
```

**Why it's slow:** For n=10,000 elements, this does ~50 million comparisons.

---

## Approach 2: Sort + Two Pointers (O(n log n), O(n) space)

Sort a copy with original indices, then use two pointers. Works when you need the values but not the original indices.

```python
def two_sum_sort(nums: list[int], target: int) -> list[int]:
    indexed = sorted(enumerate(nums), key=lambda x: x[1])
    left, right = 0, len(indexed) - 1
    while left < right:
        s = indexed[left][1] + indexed[right][1]
        if s == target:
            return sorted([indexed[left][0], indexed[right][0]])
        elif s < target:
            left += 1
        else:
            right -= 1
    return []
```

---

## Approach 3: Hash Map — Optimal

**Time Complexity:** O(n)
**Space Complexity:** O(n)

Single pass. For each element, check if its complement is already stored.

### Visual Trace

```
nums = [2, 7, 11, 15], target = 9

i=0: num=2, complement=7. seen={} → not found. Store {2:0}
i=1: num=7, complement=2. seen={2:0} → found! Return [0, 1] ✓
```

```python
def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}  # value → index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

### Complexity Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute force | O(n²) | O(1) | Fine for n < 1000 |
| Sort + two pointers | O(n log n) | O(n) | Loses original indices |
| Hash map | O(n) | O(n) | Best overall |

## Follow-up Variants (Common in Interviews)

**Two Sum II (sorted array) — #167:** Use two pointers from both ends instead of a hash map. O(n) time, O(1) space.

```python
def two_sum_sorted(numbers: list[int], target: int) -> list[int]:
    left, right = 0, len(numbers) - 1
    while left < right:
        s = numbers[left] + numbers[right]
        if s == target:
            return [left + 1, right + 1]  # 1-indexed
        elif s < target:
            left += 1
        else:
            right -= 1
    return []
```

**3Sum — #15 (Google/Microsoft favorite):** Fix one element, use two pointers for the rest.

```python
def three_sum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # skip duplicates
        left, right = i + 1, len(nums) - 1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif s < 0:
                left += 1
            else:
                right -= 1
    return result
```

## Typical Interview Use Cases

- Warm-up question at Google/Microsoft/Adobe — expected to solve in under 5 minutes
- Foundation for 3Sum, 4Sum, Two Sum variants
- Tests hash map fluency and edge case awareness (duplicates, negative numbers)
