def tribonacci(n: int) -> int:

    dp = [1] * (n+1)
    dp[0] = 0   # base case: T(0)=0, T(1)=1, T(2)=1

    for i in range(3, n+1):

        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    return dp[n]

    # Time:  O(n)
    # Space: O(n)

n = 25
print(tribonacci(n))