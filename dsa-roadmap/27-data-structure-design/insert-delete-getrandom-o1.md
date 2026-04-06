# Insert Delete GetRandom O(1)

**Difficulty:** Medium
**Pattern:** Hash Map + Array
**LeetCode:** #380

## Problem Statement
Design a data structure that supports insert, remove, and getRandom in average O(1) time.
- `insert(val)` — insert if not present, return true/false
- `remove(val)` — remove if present, return true/false
- `getRandom()` — return a random element with equal probability

## Examples

### Example 1
**Input:** `insert(1)` → `true`, `remove(2)` → `false`, `insert(2)` → `true`, `getRandom()` → `1 or 2`, `remove(1)` → `true`, `insert(2)` → `false`, `getRandom()` → `2`

## Constraints
- `-2³¹ <= val <= 2³¹ - 1`
- At most 2×10⁵ calls
- At least one element when `getRandom` is called

## Hints

> 💡 **Hint 1:** Use an array for O(1) random access and a hash map from value to array index for O(1) lookup.

> 💡 **Hint 2:** For `remove`: swap the element to remove with the last element in the array, update the hash map for the swapped element, then pop the last element.

> 💡 **Hint 3:** For `getRandom`: use `random.choice(array)` or `array[random.randint(0, len-1)]`.

## Approach
**Time Complexity:** O(1) average for all operations
**Space Complexity:** O(N)

Array stores values for O(1) random access. Hash map stores index of each value for O(1) lookup and swap-based deletion.
