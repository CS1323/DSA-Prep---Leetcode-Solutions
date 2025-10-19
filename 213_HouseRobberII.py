def rob(nums) -> int:
    
    # Bottom-Up DP helper -> standard House Robber
    def rob_linear(nums):
        prev2 = prev1 = 0

        # decide whether to rob this house or skip it
        for num in nums:
            curr = max(prev1, prev2 + num)
            prev2, prev1 = prev1, curr

        return prev1    # max money accumulated

    # - nums[0] -> handles case when only one house exists
    # - rob_linear(nums[1:])  -> skip first house
    # - rob_linear(nums[:-1]) -> skip last house
    return max(nums[0], rob_linear(nums[1:]), rob_linear(nums[:-1]))

    # Time:  O(n)
    # Space: O(1)

nums = [2,3,2]
nums = [1,2,3,1]
nums = [1,2,3]
print(rob(nums))