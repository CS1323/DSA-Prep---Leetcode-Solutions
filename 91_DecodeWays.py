def numDecodings(s: str) -> int:

    n = len(s)
    if n == 0 or s[0] == '0':
        return 0
    
    dp = [0] * (n+1)
    dp[0] = 1   # empty string
    dp[1] = 1   # valid char

    # Bottom-Up DP
    for i in range(2, n+1):

        # prev character
        if s[i-1] != '0':
            dp[i] += dp[i-1]

        # prev 2 characters
        if '10' <= s[i-2:i] <= '26':
            dp[i] += dp[i-2]

    return dp[n]

    # Time:  O(n)
    # Space: O(n)

s = "226"
print(numDecodings(s))