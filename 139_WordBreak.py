def wordBreak(s, wordDict) -> bool:

    n = len(s)
    dp = [False] * (n+1)
    dp[0] = True
    word_set = set(wordDict)

    # Bottom-Up DP
    for i in range(1, n+1):
        for j in range(i):

            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break   # no need to check more splits

    return dp[n]

    # Time:  O(n**2 * k)    -> k = avg word len
    # Space: O(n)

s = "leetcode"
wordDict = ["leet","code"]
print(wordBreak(s, wordDict))