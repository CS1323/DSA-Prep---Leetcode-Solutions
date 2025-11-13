def minCost(costs) -> int:

    n = len(costs)

    # Initialize DP array: dp[i][c] = min cost to paint house i with color c
    dp = [[float("inf")] * 3 for _ in range(n)]
    dp[0] = costs[0]    # base case: initialize first house with given costs

    # Bottom-Up DP
    for i in range(1, n):

        # if curr house is painted red (0), need min cost from blue (1) or green (2)
        dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2])

        # if curr house is painted blue (1), need min cost from red (0) or green (2)
        dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2])

        # if curr house is painted green (2), need min cost from red (0) or blue (1)
        dp[i][2] = costs[i][2] + min(dp[i-1][0], dp[i-1][1])

    return min(dp[-1])

    # Time:  O(n)
    # Space: O(n)

costs = [[17,2,17],[16,16,5],[14,3,19]]
# costs = [[7,6,2]]
print(minCost(costs))