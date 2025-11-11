def minFallingPathSum(matrix) -> int:
    
    prev = matrix[0]    # initialize prev row
    n = len(matrix)

    # Bottom-Up DP
    for row in range(1, n):
        for col in range(n):

            # add curr cell's val with prev row's min falling sum 
            matrix[row][col] += min(prev[col],
                                    prev[col-1] if col-1 >= 0 else float("inf"),
                                    prev[col+1] if col+1 < n  else float("inf")
            )

        prev = matrix[row]

    return min(prev)

    # Time:  O(n*n)
    # Space: O(n)

matrix = [[2,1,3],
          [6,5,4],
          [7,8,9]]
print(minFallingPathSum(matrix))