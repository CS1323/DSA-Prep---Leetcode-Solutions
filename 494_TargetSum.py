def findTargetSumWays(nums, target) -> int:

    total_sum = sum(nums)
    # can not be odd -> invalid subset sum
    if ((target + total_sum) % 2 == 1) or (abs(target) > total_sum):
        return 0

    # derived subset sum target
    P = (target + total_sum) // 2 

    # dp[s] = number of ways to reach sum s
    dp = [0] * (P+1)
    dp[0] = 1   # base case: one way to make sum 0 (choose nothing)

    # Bottom-Up DP
    for num in nums:
        for s in range(P, num-1, -1):

            dp[s] += dp[s-num]

    return dp[P]

    # Time:  O(n*P)
    # Space: O(P)

nums = [1,1,1,1,1]
target = 3
print(findTargetSumWays(nums, target))