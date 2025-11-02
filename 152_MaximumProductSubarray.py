def maxProduct(nums) -> int:

    curr_max = curr_min = res = nums[0] # initialize max/min product and result
    n = len(nums)

    for i in range(1, n):

        temp_max = curr_max     # store previous max before updating

        curr_max = max(nums[i], temp_max * nums[i], curr_min * nums[i])
        # update min b/c it could become max if multiplied by negative
        curr_min = min(nums[i], temp_max * nums[i], curr_min * nums[i])

        res = max(res, curr_max)    # global max product

    return res

    # Time:  O(n)
    # Space: O(1)

nums = [2,3,-2,4]
nums = [-2,0,-1]
print(maxProduct(nums))