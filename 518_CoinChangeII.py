def change(amount, coins) -> int:

    dp = [0] * (amount+1)   # num of ways to get amount t
    dp[0] = 1

    # Bottom-Up DP
    for coin in coins:
        for t in range(coin, amount+1):
            
            dp[t] += dp[t-coin]

    return dp[amount]

    # Time:  O(n*t) -> target amount
    # Space: O(t)

amount = 5
coins = [1,2,5]
print(change(amount, coins))