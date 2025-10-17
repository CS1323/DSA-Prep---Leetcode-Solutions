def minCostClimbingStairs(cost) -> int:

    n = len(cost)   # num of stairs
    
    # Base cases -> start at step 0 or 1
    prev2, prev1 = cost[0], cost[1]
    
    # Bottom-Up DP: build up the min cost to reach each step
    for i in range(2, n):
        curr = cost[i] + min(prev1, prev2)
        prev2, prev1 = prev1, curr

    # can reach the top either from the last or second-to-last step
    return min(prev1, prev2)

    # Time:  O(n)
    # Space: O(1)

cost = [10,15,20]
cost = [1,100,1,1,1,100,1,1,100,1]
print(minCostClimbingStairs(cost))