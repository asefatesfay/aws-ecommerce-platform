# Queue Reconstruction by Height

**Difficulty:** Medium
**Pattern:** Greedy — Sort + Insert
**LeetCode:** #406

## Problem Statement
People are described as `[h, k]` where `h` is height and `k` is the number of people in front with height ≥ h. Reconstruct the queue.

## Examples

### Example 1
**Input:** `people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]`
**Output:** `[[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]`

## Constraints
- `1 <= people.length <= 2000`
- `0 <= hi <= 10⁶`
- `0 <= ki < people.length`

## Hints

> 💡 **Hint 1:** Sort by height descending, then by k ascending for ties.

> 💡 **Hint 2:** After sorting, insert each person at index `k` in the result list. Taller people are already placed, so inserting at position `k` is correct.

> 💡 **Hint 3:** Since we process tallest first, shorter people inserted later don't affect the k-count of taller people already placed.

## Approach
**Time Complexity:** O(N²) due to list insertions
**Space Complexity:** O(N)

Sort descending by height (ascending by k for ties). Insert each person at index k — taller people already placed satisfy the height constraint.
