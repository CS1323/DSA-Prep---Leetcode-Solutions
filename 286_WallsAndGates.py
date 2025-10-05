from collections import deque

def wallsAndGates(rooms):
    ROWS, COLS = len(rooms), len(rooms[0])

    q = deque()

    # update distances starting from each gate (BFS)
    for r in range(ROWS):
        for c in range(COLS):
            if not rooms[r][c]:
                q.append((r,c))

    while q:

        r, c = q.popleft()

        for dr,dc in [(0,1), (0,-1), (1,0), (-1,0)]:
            row, col = (r + dr), (c + dc)

            # update dist from prev position if it has NOT been seen
            if not (row < 0 or row >= ROWS or
                    col < 0 or col >= COLS or
                    rooms[row][col] != 2**31-1):
                q.append((row, col))
                rooms[row][col] = rooms[r][c] + 1

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