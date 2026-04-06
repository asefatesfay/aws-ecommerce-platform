# Moving Average from Data Stream

**Difficulty:** Easy
**Pattern:** Queue / Sliding Window
**LeetCode:** #346

## Problem Statement

Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window. Implement the `MovingAverage` class:
- `MovingAverage(int size)` Initializes the object with the size of the window `size`.
- `double next(int val)` Returns the moving average of the last `size` values of the stream.

## Examples

### Example 1
**Input:** `["MovingAverage","next","next","next","next"]` with args `[[3],[1],[10],[3],[5]]`
**Output:** `[null,1.0,5.5,4.66667,6.0]`

## Constraints
- `1 <= size <= 1000`
- `-10^5 <= val <= 10^5`
- At most `10^4` calls will be made to `next`

## Hints

> 💡 **Hint 1:** Use a queue of fixed size. Maintain a running sum.

> 💡 **Hint 2:** When adding a new value: if the queue is full, remove the oldest value from the front and subtract it from the sum. Add the new value to the back and to the sum.

> 💡 **Hint 3:** Return sum / queue.size() as the moving average.

## Approach

**Time Complexity:** O(1) per call
**Space Complexity:** O(size)

Fixed-size queue with running sum. Evict oldest when full, add new, return sum/size.
