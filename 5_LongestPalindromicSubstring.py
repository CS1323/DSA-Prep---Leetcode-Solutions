def longestPalindrome(s: str) -> str:
    n = len(s)
    dp = [[False] * n for _ in range(n)]    # dp[i][j] is True if s[i...j] is a palindrome
    start, max_len = 0,1    # track start index and length of longest palindrome

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

            # update longest palindrome
            if dp[i][j] and j - i + 1 > max_len:
                start = i
                max_len = j - i + 1
            
    return s[start:(start + max_len)]

    # Time:  O(n**2)
    # Space: O(n**2)

s = "babad"
# s = "cbbd"
print(longestPalindrome(s))