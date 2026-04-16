# Find All Duplicates in an Array

**Difficulty:** Medium
**Pattern:** Index as Identity (Negation Trick)
**LeetCode:** #442
**Asked by:** Adobe, Microsoft, Google

## Problem Statement

Given an integer array `nums` of length `n` where all integers are in the range `[1, n]` and each integer appears once or twice, return an array of all the integers that appear twice. Must run in O(n) time and use only O(1) extra space.

## Examples

### Example 1
**Input:** `nums = [4, 3, 2, 7, 8, 2, 3, 1]`
**Output:** `[2, 3]`

### Example 2
**Input:** `nums = [1, 1, 2]`
**Output:** `[1]`

### Example 3
**Input:** `nums = [1]`
**Output:** `[]`

## Constraints
- `n == nums.length`
- `1 <= n <= 10^5`
- `1 <= nums[i] <= n`
- Each element appears once or twice

## Hints

> 💡 **Hint 1:** Since values are in `[1, n]`, you can use the array indices as a hash map. Use the sign of `nums[index]` as a "visited" flag.

> 💡 **Hint 2:** For each value `v`, go to index `v-1` and negate it. If it's already negative when you try to negate it, you've seen `v` before — it's a duplicate.

> 💡 **Hint 3:** Use `abs(nums[i])` to get the actual value (since you may have already negated it).

## Approach 1: Brute Force

**Time Complexity:** O(n²)
**Space Complexity:** O(n)

For each element, scan the rest of the array to count occurrences.

```python
def find_duplicates_brute(nums: list[int]) -> list[int]:
    result = []
    n = len(nums)
    for i in range(n):
        count = 0
        for j in range(n):
            if nums[j] == nums[i]:
                count += 1
        if count == 2 and nums[i] not in result:
            result.append(nums[i])
    return result
```

---

## Approach 2: Hash Map / Set

**Time Complexity:** O(n)
**Space Complexity:** O(n)

Count occurrences with a hash map, return those with count == 2.

```python
from collections import Counter

def find_duplicates_hashmap(nums: list[int]) -> list[int]:
    return [num for num, cnt in Counter(nums).items() if cnt == 2]
```

**Downside:** Uses O(n) extra space. The problem asks for O(1) space.

---

## Approach 3: Index Negation — Optimal

**Time Complexity:** O(n)
**Space Complexity:** O(1) extra

Since values are in `[1, n]`, use the array itself as a hash map. For each value `v`, negate `nums[v-1]`. If it's already negative when you visit it, `v` is a duplicate.

### Visual Trace

```
nums = [4, 3, 2, 7, 8, 2, 3, 1]
idx:    0  1  2  3  4  5  6  7

i=0: val=|4|=4 → go to idx 3. nums[3]=7>0 → negate → [4,3,2,-7,8,2,3,1]
i=1: val=|3|=3 → go to idx 2. nums[2]=2>0 → negate → [4,3,-2,-7,8,2,3,1]
i=2: val=|-2|=2 → go to idx 1. nums[1]=3>0 → negate → [4,-3,-2,-7,8,2,3,1]
i=3: val=|-7|=7 → go to idx 6. nums[6]=3>0 → negate → [4,-3,-2,-7,8,2,-3,1]
i=4: val=|8|=8 → go to idx 7. nums[7]=1>0 → negate → [4,-3,-2,-7,8,2,-3,-1]
i=5: val=|2|=2 → go to idx 1. nums[1]=-3<0 → DUPLICATE! Add 2.
i=6: val=|-3|=3 → go to idx 2. nums[2]=-2<0 → DUPLICATE! Add 3.
i=7: val=|-1|=1 → go to idx 0. nums[0]=4>0 → negate.

Result: [2, 3] ✓
```

```python
def find_duplicates(nums: list[int]) -> list[int]:
    result = []
    for i in range(len(nums)):
        idx = abs(nums[i]) - 1
        if nums[idx] < 0:
            result.append(idx + 1)   # already visited → duplicate
        else:
            nums[idx] = -nums[idx]   # mark as visited
    return result
```

### Complexity Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute force | O(n²) | O(n) | Count per element |
| Hash map | O(n) | O(n) | Simple but uses extra space |
| Index negation | O(n) | O(1) | Optimal — uses array as hash map |

## Related: Find All Numbers Disappeared in an Array — #448 (Adobe)

Find all numbers in `[1, n]` that do NOT appear in the array.

```python
def find_disappeared_numbers(nums: list[int]) -> list[int]:
    """
    nums=[4,3,2,7,8,2,3,1] → [5,6]
    nums=[1,1] → [2]
    
    Same negation trick: after marking, indices with positive values
    correspond to missing numbers.
    """
    for i in range(len(nums)):
        idx = abs(nums[i]) - 1
        if nums[idx] > 0:
            nums[idx] = -nums[idx]

    # Indices that are still positive → those numbers are missing
    return [i + 1 for i in range(len(nums)) if nums[i] > 0]
```

## Related: Find the Duplicate Number — #287 (Microsoft/Google)

Array of n+1 integers where each is in `[1, n]`. Find the one duplicate. O(n) time, O(1) space, no modification allowed.

```python
def find_duplicate(nums: list[int]) -> int:
    """
    nums=[1,3,4,2,2] → 2
    nums=[3,1,3,4,2] → 3
    
    Floyd's cycle detection: treat array as a linked list
    where nums[i] points to nums[nums[i]].
    The duplicate creates a cycle.
    """
    slow = fast = nums[0]
    # Phase 1: find meeting point inside cycle
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    # Phase 2: find cycle entry (= duplicate)
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow
```

## Typical Interview Use Cases

- Adobe frequently asks this exact problem
- Tests "index as identity" / negation trick — a key O(1) space technique
- Often paired with "Find Disappeared Numbers" or "Find Duplicate" in the same session
