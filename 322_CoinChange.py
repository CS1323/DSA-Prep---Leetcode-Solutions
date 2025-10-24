def coinChange(coins, amount) -> int:

    dp = [float("inf")] * (amount+1)    # stores all sub-amounts
    dp[0] = 0   # base case

    # Bottom-Up DP
    for a in range(1, amount+1):    # outer -> build up each sub-amount
        for coin in coins:          # inner -> try each coin

            if coin <= amount:
                dp[a] = min(dp[a], (dp[a - coin] + 1) )

    return dp[amount] if dp[amount] != float("inf") else -1

    # Time:  O(n*m) -> n = amount, m = len(coins)
    # Space: O(n)

coins = [1,2,5]
amount = 11
print(coinChange(coins, amount))