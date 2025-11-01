def maxSubArray(nums) -> int:

    curr_sum = max_sum = nums[0]
    n = len(nums)

    for i in range(1, n):
        curr_sum = max(nums[i], curr_sum + nums[i]) # start new or continue subarray
        max_sum = max(max_sum, curr_sum)            # update max sum seen so far

    return max_sum

    # Time:  O(n)
    # Space: O(1)

nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [5,4,-1,7,8]
print(maxSubArray(nums))