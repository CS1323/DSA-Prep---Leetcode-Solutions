def exist(board, word):
    w_len = len(word)
    ROWS, COLS = len(board), len(board[0])

    def backtrack(row, col, i):
        # -- Base Cases --
        # found word
        if i == w_len:
            return True
        # out of bounds
        if (row < 0 or row >= ROWS) or (col < 0 or col >= COLS):
            return False
        # letter does not match
        if board[row][col] != word[i]:
            return False
        
        board[row][col] = None  # mark visited

        # explore 1 of 4 directions
        res = (backtrack(row, col+1, i+1) or backtrack(row+1, col, i+1) or 
               backtrack(row, col-1, i+1) or backtrack(row-1, col, i+1))

        board[row][col] = word[i]     # unmark visted

        return res

    for r in range(ROWS):
        for c in range(COLS):
            if backtrack(r,c,0): return True
    
    return False

    # Time:  O(M * 3**n) -> M = rows*cols, n = len(word)
    # Space: O(n)

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(exist(board, word))