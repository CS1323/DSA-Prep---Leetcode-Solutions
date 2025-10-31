def minPathSum(grid) -> int:

    ROWS, COLS = len(grid), len(grid[0])

    # intialize -> only one way to reach each cell in the first row and col
    for r in range(1, ROWS):
        grid[r][0] += grid[r-1][0]

    for c in range(1, COLS):
        grid[0][c] += grid[0][c-1]

    # DP: cost of path to current cell = value + min(from above, from left)
    for r in range(1, ROWS):
        for c in range(1, COLS):
            grid[r][c] += min(grid[r][c-1], grid[r-1][c])

    # min path sum to bottom right
    return grid[-1][-1]

    # Time:  O(m*n)
    # Space: O(1)

grid = [[1,3,1],[1,5,1],[4,2,1]]
grid = [[1,2,3],[4,5,6]]
print(minPathSum(grid))