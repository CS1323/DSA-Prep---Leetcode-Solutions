def maxAreaOfIsland(grid) -> int:
    ROWS, COLS = len(grid), len(grid[0])
    max_area = 0     # max area of an island
    
    # helper - traversal
    def dfs(r, c):
        # base cases - out of bounds OR water
        if (r < 0 or r >= ROWS or
                c < 0 or c >= COLS or 
                grid[r][c] == 0):
            return 0

        grid[r][c] = 0  # seen
        curr_area = 1   # count cell

        curr_area += dfs(r, c+1) # right
        curr_area += dfs(r, c-1) # left
        curr_area += dfs(r+1, c) # down
        curr_area += dfs(r-1, c) # up

        return curr_area

    # count islands
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1:
                max_area = max(dfs(r, c), max_area)

    return max_area

    # Time:  O(m*n) -> size of grid
    # Space: O(m*n)

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(maxAreaOfIsland(grid))