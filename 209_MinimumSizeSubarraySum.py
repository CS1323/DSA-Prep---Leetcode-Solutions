def minSubArrayLen(target, nums) -> int:
    nums_length = len(nums)
    left = 0
    subarray_sum = 0
    min_window_length = nums_length+1

    for right in range(nums_length):
        subarray_sum += nums[right]

        while subarray_sum >= target:
            window_length = right - left + 1
            min_window_length = min(min_window_length, window_length)
            subarray_sum -= nums[left]
            left += 1

    if min_window_length > nums_length:
        return 0

    return min_window_length


target = 7
nums = [2,3,1,2,4,3]
print(minSubArrayLen(target, nums))