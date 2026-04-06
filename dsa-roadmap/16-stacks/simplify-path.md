# Simplify Path

**Difficulty:** Medium
**Pattern:** Stack
**LeetCode:** #71

## Problem Statement

Given a string `path`, which is an absolute path (starting with a slash `'/'`) to a file or directory in a Unix-style file system, convert it to the simplified canonical path. In a Unix-style file system, a period `'.'` refers to the current directory, a double period `'..'` refers to the directory up a level, and any multiple consecutive slashes (i.e. `'//'`) are treated as a single slash `'/'`. The canonical path should have the following format: the path starts with a single slash `'/'`, any two directories are separated by a single slash `'/'`, the path does not end with a trailing `'/'`, the path only contains the directories on the path from the root directory to the target file or directory.

## Examples

### Example 1
**Input:** `path = "/home/"`
**Output:** `"/home"`

### Example 2
**Input:** `path = "/../"`
**Output:** `"/"`

### Example 3
**Input:** `path = "/home//foo/"`
**Output:** `"/home/foo"`

## Constraints
- `1 <= path.length <= 3000`
- `path` consists of English letters, digits, period `'.'`, slash `'/'` or `'_'`
- `path` is a valid absolute Unix path

## Hints

> 💡 **Hint 1:** Split the path by `'/'`. Process each component.

> 💡 **Hint 2:** Use a stack. For each component: skip empty strings and `'.'`. For `'..'`, pop from the stack (if non-empty). For anything else, push onto the stack.

> 💡 **Hint 3:** Join the stack with `'/'` and prepend `'/'` for the result.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(n)

Split by `/`, process components with a stack. Skip empty/`.`, pop on `..`, push directory names. Join with `/`.
