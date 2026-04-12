# Monotonic Stack

## What is it?
A stack that maintains elements in **monotonically increasing or decreasing order**. When a new element violates the order, elements are popped until the order is restored. Each element is pushed and popped at most once → O(N) total.

## Visual Example — Next Greater Element
```
nums = [2, 1, 5, 3, 6, 4]
Find next greater element for each position.

Process each element, maintain decreasing stack:

i=0, val=2: stack=[], push 2.  stack=[2]
i=1, val=1: 1<2, push 1.       stack=[2,1]
i=2, val=5: 5>1, pop 1 → NGE[1]=5
            5>2, pop 2 → NGE[0]=5
            push 5.             stack=[5]
i=3, val=3: 3<5, push 3.       stack=[5,3]
i=4, val=6: 6>3, pop 3 → NGE[3]=6
            6>5, pop 5 → NGE[2]=6
            push 6.             stack=[6]
i=5, val=4: 4<6, push 4.       stack=[6,4]

Remaining in stack have no NGE → -1
Result: [5, 5, 6, 6, -1, -1]
```

## Key Insight
- **Decreasing stack** → find next GREATER element
- **Increasing stack** → find next SMALLER element
- Elements waiting in stack haven't found their answer yet

## Implementation

```python
def next_greater_element(nums):
    """
    For each element, find the next greater element to its right.
    O(N) time — each element pushed/popped at most once.
    """
    n = len(nums)
    result = [-1] * n
    stack = []  # stores indices, values are decreasing

    for i in range(n):
        # Current element is greater than stack top → it's the NGE
        while stack and nums[stack[-1]] < nums[i]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)

    return result


def next_smaller_element(nums):
    """Find next smaller element for each position."""
    n = len(nums)
    result = [-1] * n
    stack = []  # increasing stack

    for i in range(n):
        while stack and nums[stack[-1]] > nums[i]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)

    return result


def daily_temperatures(temperatures):
    """
    LeetCode #739: Days until warmer temperature.
    Same as next greater element, but return distance.
    """
    result = [0] * len(temperatures)
    stack = []

    for i, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            idx = stack.pop()
            result[idx] = i - idx
        stack.append(i)

    return result


def largest_rectangle_histogram(heights):
    """
    LeetCode #84: Largest rectangle in histogram.
    Monotonic increasing stack — when we pop, we found the right boundary.
    Left boundary is the new stack top.
    """
    stack = []
    max_area = 0
    heights = heights + [0]  # sentinel to flush remaining bars

    for i, h in enumerate(heights):
        start = i
        while stack and heights[stack[-1]] > h:
            idx = stack.pop()
            width = i - (stack[-1] + 1 if stack else 0)
            max_area = max(max_area, heights[idx] * width)
            start = idx
        stack.append(start)

    return max_area


def sum_subarray_minimums(arr):
    """
    LeetCode #907: Sum of subarray minimums.
    For each element, find how many subarrays it's the minimum of.
    Use monotonic stack to find left and right boundaries.
    """
    MOD = 10**9 + 7
    n = len(arr)
    left = [0] * n   # distance to previous smaller element
    right = [0] * n  # distance to next smaller or equal element
    stack = []

    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        left[i] = i - stack[-1] if stack else i + 1
        stack.append(i)

    stack = []
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()
        right[i] = stack[-1] - i if stack else n - i
        stack.append(i)

    return sum(arr[i] * left[i] * right[i] for i in range(n)) % MOD
```

## Example Usage
```python
print(next_greater_element([2, 1, 5, 3, 6, 4]))
# [5, 5, 6, 6, -1, -1]

print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))
# [1, 1, 4, 2, 1, 1, 0, 0]

print(largest_rectangle_histogram([2, 1, 5, 6, 2, 3]))
# 10 (rectangle of height 5, width 2 at indices 2-3)
```

## When to Use
- "Next greater/smaller element"
- "Previous greater/smaller element"
- "Largest rectangle in histogram"
- "Sum/count of subarray min/max"
- "Remove elements to maintain order"
- "Stock span problems"

## LeetCode Problems

| Problem | Difficulty | Pattern |
|---------|-----------|---------|
| Daily Temperatures (#739) | Medium | Next greater (decreasing stack) |
| Next Greater Element I (#496) | Easy | Next greater |
| Next Greater Element II (#503) | Medium | Circular array, next greater |
| Largest Rectangle in Histogram (#84) | Hard | Increasing stack, area |
| Trapping Rain Water (#42) | Hard | Can use monotonic stack |
| Sum of Subarray Minimums (#907) | Medium | Left/right boundaries |
| Sum of Subarray Ranges (#2104) | Medium | Min and max boundaries |
| Remove K Digits (#402) | Medium | Increasing stack |
| 132 Pattern (#456) | Medium | Decreasing stack |
| Online Stock Span (#901) | Medium | Decreasing stack |
| Buildings With an Ocean View (#1762) | Medium | Decreasing stack |
| Maximum Width Ramp (#962) | Medium | Stack + two pointers |
| Shortest Unsorted Continuous Subarray (#581) | Medium | Stack or two-pass |
