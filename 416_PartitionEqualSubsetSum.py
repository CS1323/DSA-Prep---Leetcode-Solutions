def canPartition(nums) -> bool:

    # can not divide odd sum
    total_sum = sum(nums)
    if total_sum % 2 == 1:
        return False
    
    target = total_sum // 2     # desired subset sum
    dp = [False] * (target+1)
    dp[0] = True

    # Bottom-Up DP (knapsack)
    for num in nums:
        for t in range(target, num-1, -1):

            # partial sum seen
            if dp[t-num]:
                dp[t] = True

            # early exit
            if dp[target]: return True

    return dp[target]

    # Time:  O(n*target) -> target = sum of array elements divided by 2
    # Space: O(target)

nums = [1,5,11,5]
print(canPartition(nums))