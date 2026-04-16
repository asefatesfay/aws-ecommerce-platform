# Find Minimum in Rotated Sorted Array

**Difficulty:** Medium
**Pattern:** Binary Search on Rotated Array
**LeetCode:** #153
**Asked by:** Microsoft, Google, Adobe

## Problem Statement

Suppose an array of length `n` sorted in ascending order is rotated between 1 and n times. Given the rotated array `nums` of unique elements, return the minimum element. Must run in O(log n).

## Examples

### Example 1
**Input:** `nums = [3, 4, 5, 1, 2]`
**Output:** `1`
**Explanation:** Original array was `[1, 2, 3, 4, 5]`, rotated 3 times.

### Example 2
**Input:** `nums = [4, 5, 6, 7, 0, 1, 2]`
**Output:** `0`
**Explanation:** Original array was `[0, 1, 2, 4, 5, 6, 7]`, rotated 4 times.

### Example 3
**Input:** `nums = [11, 13, 15, 17]`
**Output:** `11`
**Explanation:** No rotation — minimum is at index 0.

## Constraints
- `n == nums.length`
- `1 <= n <= 5000`
- `-5000 <= nums[i] <= 5000`
- All integers are unique
- Array was originally sorted and rotated 1 to n times

## Hints

> 💡 **Hint 1:** The array has two sorted halves. The minimum is at the "pivot" — where the array transitions from the right half back to the left half.

> 💡 **Hint 2:** Compare `nums[mid]` with `nums[right]`. If `nums[mid] > nums[right]`, the minimum is in the right half. Otherwise, it's in the left half (including mid).

> 💡 **Hint 3:** The loop invariant: `nums[right]` is always >= the minimum. When `left == right`, you've found the minimum.

## Approach 1: Brute Force

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Linear scan — find the minimum directly. Doesn't satisfy the O(log n) requirement but good to state first.

```python
def find_min_brute(nums: list[int]) -> int:
    return min(nums)  # O(n) scan
```

**Why it's not enough:** The problem requires O(log n), so we need binary search.

---

## Approach 2: Binary Search — Optimal

**Time Complexity:** O(log n)
**Space Complexity:** O(1)

The array has two sorted halves. Compare `nums[mid]` with `nums[right]`:
- If `nums[mid] > nums[right]` → the right half is unsorted, minimum is in `[mid+1, right]`
- Otherwise → the left half (including mid) contains the minimum, search `[left, mid]`

### Why Compare with `nums[right]` (not `nums[left]`)?

```
If we compare with nums[left]:
  nums[mid] > nums[left] → could be either half (both sorted halves satisfy this)
  
If we compare with nums[right]:
  nums[mid] > nums[right] → MUST be in right half (the rotation point is there)
  nums[mid] <= nums[right] → minimum is in left half including mid
  
nums[right] is the reliable anchor because the minimum is always <= nums[right].
```

### Visual Trace

```
nums = [4, 5, 6, 7, 0, 1, 2]
        0  1  2  3  4  5  6

left=0, right=6, mid=3
  nums[3]=7 > nums[6]=2 → min in right half → left=4

left=4, right=6, mid=5
  nums[5]=1 <= nums[6]=2 → min in left half → right=5

left=4, right=5, mid=4
  nums[4]=0 <= nums[5]=1 → min in left half → right=4

left=4, right=4 → return nums[4]=0 ✓
```

```python
def find_min(nums: list[int]) -> int:
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1   # minimum is in right half
        else:
            right = mid      # minimum is in left half (mid could be it)
    return nums[left]
```

### Complexity Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Linear scan | O(n) | O(1) | Simple but doesn't meet requirement |
| Binary search | O(log n) | O(1) | Optimal — required by problem |

## Follow-up: Search in Rotated Sorted Array — #33 (Microsoft/Google)

Find a target value in a rotated sorted array. O(log n).

```python
def search_rotated(nums: list[int], target: int) -> int:
    """
    nums = [4,5,6,7,0,1,2], target = 0 → 4
    nums = [4,5,6,7,0,1,2], target = 3 → -1
    """
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
```

## Follow-up: With Duplicates — #154 (Adobe)

When duplicates are allowed, worst case degrades to O(n) but average is still O(log n).

```python
def find_min_with_duplicates(nums: list[int]) -> int:
    """
    nums = [2,2,2,0,1] → 0
    nums = [3,1,3,3,3] → 1
    """
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        elif nums[mid] < nums[right]:
            right = mid
        else:
            right -= 1  # can't determine which side, shrink right
    return nums[left]
```

## Typical Interview Use Cases

- Standard Microsoft/Google binary search question
- Tests understanding of binary search invariants on non-standard arrays
- Often followed by "now find a target value" (Search in Rotated Sorted Array)
