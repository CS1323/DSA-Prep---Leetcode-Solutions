def longestOnes(nums, k) -> int:
    left = 0        # left index
    max_ones = 0    # result
    num_zeroes = 0  # num of zeroes seen

    # sliding window
    for right in range(len(nums)):
        if nums[right] == 0:
            num_zeroes += 1

        # shrink from left if zeroes seen exceeds k
        while num_zeroes > k:
            if nums[left] == 0:
                num_zeroes -= 1

            left += 1

        # update max consecutive ones
        curr_ones = right - left + 1
        if curr_ones > max_ones:
            max_ones = curr_ones

    return max_ones

    # Time:  O(n)
    # Space: O(1)

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(longestOnes(nums, k))