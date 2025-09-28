def pacificAtlantic(heights):
    ROWS, COLS = len(heights), len(heights[0])
    pacific, atlantic = set(), set()

    # find cells that can reach a given ocean (visited)
    def dfs(r, c, visited, prev_height):
        if (r < 0 or r >= ROWS or c < 0 or c >= COLS
            or (r,c) in visited or heights[r][c] < prev_height):
            return
        
        visited.add((r,c))
        dfs(r, c+1, visited, heights[r][c])
        dfs(r, c-1, visited, heights[r][c])
        dfs(r+1, c, visited, heights[r][c])
        dfs(r-1, c, visited, heights[r][c])

    for c in range(COLS):
        dfs(0, c, pacific, heights[0][c])               # pacific top border cells
        dfs(ROWS-1, c, atlantic, heights[ROWS-1][c])    # atlantic bottom border cells

    for r in range(ROWS):
        dfs(r, 0, pacific, heights[r][0])               # pacific left border cells
        dfs(r, COLS-1, atlantic, heights[r][COLS-1])    # atlantic right border cells

    # find cells that can visit both oceans
    res = []
    for r in range(ROWS):
        for c in range(COLS):
            if (r,c) in pacific and (r,c) in atlantic:
                res.append([r,c])

    return res

    # Time:  O(m*n) -> size of grid
    # Space: O(m*n)

heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(pacificAtlantic(heights))