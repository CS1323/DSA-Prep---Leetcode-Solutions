def longestCommonSubsequence(text1: str, text2: str) -> int:

    m, n = len(text1), len(text2)

    # dp[i][j] = LCS length between text1[:i] and text2[:j]
    dp = [ [0] * (n+1) for _ in range(m+1) ]
    
    # Bottom-Up DP
    for i in range(1, m+1):
        for j in range(1, n+1):

            # Case 1: Characters match  -> extend the subsequence
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1

            # Case 2: Characters differ -> skip one and take the max
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]

    # Time:  O(m*n)   -> m = len(text1) 
    # Space: O(m*n)   -> n = len(text2) 

text1 = "abcde" 
text2 = "ace" 

text1 = "abcd"
text2 = "acbd"

print(longestCommonSubsequence(text1, text2))