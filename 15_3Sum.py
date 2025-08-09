def threeSum(nums):
    result = []
    nums_length = len(nums)
    nums.sort() # Time: O(n*log n), Space: O(log n)

    # iterate through nums up to the last 3 (need >= 3 elements)
    # Time: O(n)
    for i in range(nums_length-2):

        # if num is positive (won't decrease)
        if nums[i] > 0:
            break
        # skip duplicate values
        elif i > 0 and nums[i] == nums[i-1]:
            continue

        left, right = i+1, nums_length-1  # pointers

        # search for the additional 2 nums 
        # Time: O(n)
        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicates for left
                while left < right and nums[left] == nums[left + 1]:
                    left += 1

                # Skip duplicates for right
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif total < 0:
                left += 1

            else:
                right -= 1

    return result

    # Time:  O(n*log n) + O(n^2) = O(n^2)
    # Space: O(n^2) from result, otherwise O(log n) for sorting

nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))