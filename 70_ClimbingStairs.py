def climbStairs(n: int) -> int:

    # Base cases:
    # 1 way to climb 1 step (1)
    # 2 ways to climb 2 steps (1+1, 2)
    if n <= 2:
        return n

    # Bottom-Up DP
    dp = [0] * (n+1)    # store results
    dp[1], dp[2] = 1, 2

    for i in range(3, n+1): 
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

    # Time:  O(n)
    # Space: O(n)

n = 4
print(climbStairs(n))