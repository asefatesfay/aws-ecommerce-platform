# First Unique Number

**Difficulty:** Medium
**Pattern:** Queue + Hash Map
**LeetCode:** #1429

## Problem Statement

You have a queue of integers, you need to retrieve the first unique integer in the queue. Implement the `FirstUnique` class:
- `FirstUnique(int[] nums)` Initializes the object with the numbers in the queue.
- `int showFirstUnique()` returns the value of the first unique integer of the queue, and returns `-1` if there is no such integer.
- `void add(int value)` inserts value to the back of the queue.

## Examples

### Example 1
**Input:** `["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"]` with args `[[[2,3,5]],[],[5],[],[2],[],[3],[]]`
**Output:** `[null,2,null,2,null,3,null,-1]`

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^8`
- `1 <= value <= 10^8`
- At most `5 * 10^4` calls will be made to `showFirstUnique` and `add`

## Hints

> 💡 **Hint 1:** Use a queue to maintain insertion order and a HashMap to track frequencies.

> 💡 **Hint 2:** `showFirstUnique`: scan the front of the queue, skipping elements with frequency > 1. Return the first with frequency == 1.

> 💡 **Hint 3:** Optimize by lazily removing duplicates from the front of the queue during `showFirstUnique`.

## Approach

**Time Complexity:** O(1) amortized for add, O(n) worst case for showFirstUnique
**Space Complexity:** O(n)

Queue + frequency HashMap. Lazily remove non-unique elements from the front during showFirstUnique.
