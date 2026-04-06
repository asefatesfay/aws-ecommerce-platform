# Online Stock Span

**Difficulty:** Medium
**Pattern:** Monotonic Stack
**LeetCode:** #901

## Problem Statement

Design an algorithm that collects daily price quotes for some asset and returns the span of that asset's price for the current day. The span of the asset's price today is defined as the maximum number of consecutive days (starting from today and going backward) for which the stock price was less than or equal to today's price. Implement the `StockSpanner` class with a `next(int price)` method that returns the span of the stock's price given that today's price is `price`.

## Examples

### Example 1
**Input:** `["StockSpanner","next","next","next","next","next","next","next"]` with prices `[[],[100],[80],[60],[70],[60],[75],[85]]`
**Output:** `[null,1,1,1,2,1,4,6]`

## Constraints
- `1 <= price <= 10^5`
- At most `10^4` calls will be made to `next`

## Hints

> 💡 **Hint 1:** Use a monotonic decreasing stack of (price, span) pairs.

> 💡 **Hint 2:** When a new price comes in, pop all stack entries with price ≤ current price. Accumulate their spans into the current span.

> 💡 **Hint 3:** Push (current_price, accumulated_span) onto the stack. Return the accumulated span.

## Approach

**Time Complexity:** O(1) amortized per call
**Space Complexity:** O(n)

Monotonic decreasing stack of (price, span) pairs. Merge spans of smaller-or-equal prices into the current span.
