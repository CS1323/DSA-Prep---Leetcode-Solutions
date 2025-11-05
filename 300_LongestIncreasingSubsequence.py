def lengthOfLIS(nums) -> int:

    n = len(nums)
    tails = [nums[0]]   # base case: element alone -> length 1

    # Bottom-Up DP
    for i in range(1, n):

        # increase subsequence
        if nums[i] > tails[-1]:
            tails.append(nums[i])

        # smaller value
        elif nums[i] < tails[-1]:

            left = 0
            right = len(tails)-1

            # Binary Search to find which tail value to update
            while left < right:
                mid = left + ((right - left) // 2)

                if tails[mid] < nums[i]:
                    left = mid + 1
                else:
                    right = mid

            tails[left] = nums[i]

    return len(tails)

    # Time:  O(n log n)
    # Space: O(n)

nums = [10,9,2,5,3,7,101,18]
# nums = [0,1,0,3,2,3]
# nums = [7,7,7,7,7,7,7]
print(lengthOfLIS(nums))