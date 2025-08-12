def sortedSquares(nums):
    left = 0
    right = len(nums) - 1
    result = []

    # two pointers
    while left <= right:

        if abs(nums[left]) > abs(nums[right]):
            result.append(nums[left] ** 2)
            left += 1
        else:
            result.append(nums[right] ** 2)
            right -= 1

    result.reverse()

    return result

    # Time: O(n)
    # Space: O(1) "not using extra space" -> O(n)

nums = [-4,-1,0,3,10]
print(sortedSquares(nums))