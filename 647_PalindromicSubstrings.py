def countSubstrings(s: str) -> int:

    n = len(s)
    dp = [[False] * n for _ in range(n)]    # dp[i][j] is True if s[i...j] is a palindrome
    count = 0   # counts num of palindromes

    # Bottom-Up DP: i goes backwards so dp[i+1][j-1] is already computed
    for i in range(n-1, -1, -1):
        for j in range(i, n):

            # update table
            if i == j:      # len(substring) == 1 
                dp[i][j] = True
            elif j == i+1:  # len(substring) == 2
                dp[i][j] = (s[i] == s[j])
            else:           # len(substring) >= 3
                dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]

            # palindrome counter
            if dp[i][j]:
                count += 1 

    return count

    # Time:  O(n**2)
    # Space: O(n**2)

s = "abc"
s = "aaa"
print(countSubstrings(s))