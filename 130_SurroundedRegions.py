def solve(board):
    ROWS, COLS = len(board), len(board[0])

    def capture(r, c):

        if (r < 0 or r >= ROWS or
            c < 0 or c >= COLS or
            board[r][c] != 'O'):
            return
        
        board[r][c] = 'S'
        capture(r, c+1)
        capture(r, c-1)
        capture(r+1, c)
        capture(r-1, c)

    # (DFS) Capture unsurrounded regions (O -> S)
    for r in range(ROWS):
        for c in range(COLS):
            if ((r in [0, ROWS-1] or c in [0, COLS-1]) 
                and board[r][c] == 'O'):
                capture(r, c)

    for r in range(ROWS):
        for c in range(COLS):

            # Capture surrounded regions (O -> X)
            if board[r][c] == 'O':
                board[r][c] = 'X'

            # Uncapture unsurrounded regions (S -> O)
            elif board[r][c] == 'S':
                board[r][c] = 'O'
            
    return

    # Time:  O(m*n) -> size of grid
    # Space: O(m*n)

board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
solve(board)
print(board)
