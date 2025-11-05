def lengthOfLIS(nums) -> int:

    n = len(nums)
    dp = [1] * n    # dp[i] = length of LIS ending at index i (base case: each element alone -> length 1)

    # Bottom-Up DP
    for i in range(n):
        for j in range(i):

            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j]+1) # choose the best prev subsequence and add current element

    return max(dp)

    # Time:  O(n**2)
    # Space: O(n)

nums = [10,9,2,5,3,7,101,18]
# nums = [0,1,0,3,2,3]
# nums = [7,7,7,7,7,7,7]
print(lengthOfLIS(nums))