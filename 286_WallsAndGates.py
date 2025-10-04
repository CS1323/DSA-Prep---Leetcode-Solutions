def wallsAndGates(rooms):
    ROWS, COLS = len(rooms), len(rooms[0])

    def update_dist(r, c, dist):
        if (r < 0 or r >= ROWS or
            c < 0 or c >= COLS or
            rooms[r][c] < dist):
            return
         
        rooms[r][c] = dist
        update_dist(r, c+1, dist+1) # right
        update_dist(r, c-1, dist+1) # left
        update_dist(r+1, c, dist+1) # down
        update_dist(r-1, c, dist+1) # up

    # update distances starting from each gate (DFS)
    for r in range(ROWS):
        for c in range(COLS):
            if not rooms[r][c]:
                update_dist(r, c, 0)

    return

    # Time:  O(m*n) -> size of grid
    # Space: O(m*n)

rooms = [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]
wallsAndGates(rooms)
print(rooms)