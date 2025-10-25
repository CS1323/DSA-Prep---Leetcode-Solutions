def uniquePaths(m: int, n: int) -> int:

    # initialize rows -> only one way to reach each cell in the first row and col
    prev = [1] * n
    curr = [1] * n

    # DP: num of paths to current cell = from above + from left
    for _ in range(1,m):
        for c in range(1,n):
            curr[c] = prev[c] + curr[c-1]

        prev = curr

    # total unique paths
    return curr[-1]

    # Time:  O(m*n)
    # Space: O(n)

m = 3
n = 7
print(uniquePaths(m,n))