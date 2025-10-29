def jump(nums) -> int:

    n = len(nums)
    # dp[i] = min jumps needed to reach the end from index i
    dp = [float("inf")] * n
    dp[-1] = 0  # 0 jumps needed at end

    # Bottom-Up DP
    for i in range(n-2, -1, -1):
        # farthest index we can jump to from i within bounds
        end = min( n, (i + nums[i] + 1) )

        # try every reachable index from i and take the min jumps
        for j in range(i+1, end):
            dp[i] = min( dp[i], (1 + dp[j]) )

    return dp[0]    # min jumps needed

# Time:  O(n**2)
# Space: O(n)

nums = [2,3,1,1,4]
print(jump(nums))