def numDecodings(s: str) -> int:

    n = len(s)

    # invalid if empty or starts with '0'
    if n == 0 or s[0] == '0':
        return 0
    
    prev2 = prev1 = 1   # base cases: dp[0] and dp[1]

    # Bottom-Up DP
    for i in range(2, n+1):

        curr = 0    # ways to decode up to i chars

        # valid single digit
        if s[i-1] != '0':
            curr += prev1

        # valid two-digit number
        if '10' <= s[i-2:i] <= '26':
            curr += prev2

        # shift window
        prev2 = prev1
        prev1 = curr

    # total ways
    return prev1

    # Time:  O(n)
    # Space: O(1)

s = "226"
print(numDecodings(s))