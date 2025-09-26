def numIslands(grid) -> int:
    ROWS, COLS = len(grid), len(grid[0])
    islands = 0     # num of islands
    
    # helper - traversal
    def dfs(r, c):
        # base cases - out of bounds OR water
        if (r < 0 or r >= ROWS or
            c < 0 or c >= COLS or 
            grid[r][c] == '0'):
            return

        else:
            grid[r][c] = '0'    # seen
            dfs(r, c+1) # right
            dfs(r, c-1) # left
            dfs(r+1, c) # down
            dfs(r-1, c) # up

    # count islands
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == '1':
                islands += 1
                dfs(r, c)

    return islands

    # Time:  O(m*n) -> size of grid
    # Space: O(m*n)

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
# grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
print(numIslands(grid))