from collections import deque

def orangesRotting(grid) -> int:
    ROWS, COLS = len(grid), len(grid[0])
    q = deque()
    fresh_count = 0     # num of fresh oranges
    minutes = 0         # minutes elapsed

    # count fresh and enqueue rotten
    for r in range(ROWS):
        for c in range(COLS):

            if grid[r][c] == 1:
                fresh_count += 1

            if grid[r][c] == 2:
                q.append((r,c))

    # BFS
    while q and fresh_count > 0:

        # process all oranges in this minute
        for _ in range(len(q)):
            r,c = q.popleft()

            # rot neighboring oranges in directions R,L,D,U
            for row_change, col_change in [(0,1), (0,-1), (1,0), (-1,0)]:
                row, col = (r + row_change), (c + col_change)
        
                if (0 <= row < ROWS and 0 <= col < COLS and grid[row][col] == 1):
                    grid[row][col] = 2
                    fresh_count -= 1
                    q.append((row, col))
                
        minutes += 1         

    return minutes if not fresh_count else -1

    # Time:  O(m*n) -> size of grid
    # Space: O(m*n)

grid = [[2,1,1],[1,1,0],[0,1,1]]
print(orangesRotting(grid))