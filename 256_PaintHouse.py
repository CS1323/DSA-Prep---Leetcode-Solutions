def minCost(costs) -> int:

    n = len(costs)

    # Initialize: dp[c] = min cost to paint a house with color c
    curr = costs[0]

    # Bottom-Up DP
    for i in range(1, n):

        prev = curr.copy()

        # if curr house is painted red (0), need min cost from blue (1) or green (2)
        curr[0] = costs[i][0] + min(prev[1], prev[2])

        # if curr house is painted blue (1), need min cost from red (0) or green (2)
        curr[1] = costs[i][1] + min(prev[0], prev[2])

        # if curr house is painted green (2), need min cost from red (0) or blue (1)
        curr[2] = costs[i][2] + min(prev[0], prev[1])

    return min(curr)

    # Time:  O(n)
    # Space: O(1)

costs = [[17,2,17],[16,16,5],[14,3,19]]
# costs = [[7,6,2]]
print(minCost(costs))