def uniquePathsWithObstacles(obstacleGrid) -> int:

    ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])

    # early exit when start and end are blocked
    if obstacleGrid[0][0] or obstacleGrid[ROWS-1][COLS-1]:
        return 0
    else:
        obstacleGrid[0][0] = 1  # initialize start
    
    # intialize -> only one way to reach each cell in the first row and col
    #              unless there is an obstacle
    for r in range(1, ROWS):
        obstacleGrid[r][0] = 1 if not obstacleGrid[r][0] and obstacleGrid[r-1][0] else 0
    for c in range(1, COLS):
        obstacleGrid[0][c] = 1 if not obstacleGrid[0][c] and obstacleGrid[0][c-1] else 0
    
    # DP: num of paths to current cell = from above + from left
    for r in range(1, ROWS):
        for c in range(1, COLS):

            # obstacles = 0 paths
            if obstacleGrid[r][c] == 1:
                obstacleGrid[r][c] = 0
            else:
                obstacleGrid[r][c] = obstacleGrid[r][c-1] + obstacleGrid[r-1][c]

    # total unique paths
    return obstacleGrid[ROWS-1][COLS-1]

    # Time:  O(m*n)
    # Space: O(1)

obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# obstacleGrid = [[0,1],[0,0]]
print(uniquePathsWithObstacles(obstacleGrid))