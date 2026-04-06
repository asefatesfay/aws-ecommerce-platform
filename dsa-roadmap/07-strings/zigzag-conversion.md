# Zigzag Conversion

**Difficulty:** Medium
**Pattern:** String Simulation
**LeetCode:** #6

## Problem Statement

The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number of rows like this (with 3 rows):

```
P   A   H   N
A P L S I I G
Y   I   R
```

And then read line by line: `"PAHNAPLSIIGYIR"`. Write the code that will take a string and make this conversion given a number of rows.

## Examples

### Example 1
**Input:** `s = "PAYPALISHIRING"`, `numRows = 3`
**Output:** `"PAHNAPLSIIGYIR"`

### Example 2
**Input:** `s = "PAYPALISHIRING"`, `numRows = 4`
**Output:** `"PINALSIGYAHRPI"`
**Explanation:** Rows: P I N / A L S I G / Y A H R / P I

### Example 3
**Input:** `s = "A"`, `numRows = 1`
**Output:** `"A"`

## Constraints
- `1 <= s.length <= 1000`
- `s` consists of English letters, ',' and '.'
- `1 <= numRows <= 1000`

## Hints

> 💡 **Hint 1:** Simulate the zigzag by assigning each character to a row. Use a variable to track the current row and a direction (going down or going up).

> 💡 **Hint 2:** Start at row 0, going down. When you reach the last row, reverse direction (go up). When you reach row 0 again, reverse direction (go down). Each character goes into its current row's bucket.

> 💡 **Hint 3:** After processing all characters, concatenate all row buckets in order to get the result.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(n)

Maintain numRows string builders. Simulate the zigzag traversal, appending each character to the appropriate row's builder. Concatenate all builders at the end.

## Python Implementation

```python
def convert(s, num_rows):
	if num_rows == 1 or num_rows >= len(s):
		return s

	rows = ["" for _ in range(num_rows)]
	row = 0
	direction = 1

	for ch in s:
		rows[row] += ch
		if row == 0:
			direction = 1
		elif row == num_rows - 1:
			direction = -1
		row += direction

	return "".join(rows)
```

## Typical Interview Use Cases

- Row-based string simulation
- Direction flipping while traversing structured output
- Good example of converting a visual pattern into state transitions

