# Matrix

Matrix problems involve 2D arrays and require careful index management. Many matrix problems are extensions of 1D array techniques.

## Key Concepts

- **In-place modification:** Modify the matrix without extra space. Common trick: use the matrix itself to store state (e.g., mark with a special value).
- **Layer-by-layer traversal:** Spiral, rotation, and boundary problems often process the matrix layer by layer.
- **Direction arrays:** Use `dirs = [(0,1),(1,0),(0,-1),(-1,0)]` for clean directional traversal.
- **Bounds checking:** Always verify `0 <= r < rows` and `0 <= c < cols`.

## Common Patterns

### Spiral Traversal
Process the outermost layer, then recurse/iterate inward. Track top, bottom, left, right boundaries.

### In-Place Rotation
For 90° rotation: transpose then reverse each row (or reverse then transpose for the other direction).

### Marking Visited
Use a separate boolean matrix, or mark in-place with a special value (e.g., 0 → -1 to distinguish "originally 0" from "set to 0").

## Problems in This Section

| Problem | Difficulty |
|---------|-----------|
| [Spiral Matrix](./spiral-matrix.md) | Medium |
| [Spiral Matrix II](./spiral-matrix-ii.md) | Medium |
| [Diagonal Traverse](./diagonal-traverse.md) | Medium |
| [Valid Sudoku](./valid-sudoku.md) | Medium |
| [Transpose Matrix](./transpose-matrix.md) | Easy |
| [Rotate Image](./rotate-image.md) | Medium |
| [Set Matrix Zeroes](./set-matrix-zeroes.md) | Medium |
| [Candy Crush](./candy-crush.md) | Medium |
| [Game of Life](./game-of-life.md) | Medium |
