def findMin(nums) -> int:
    left = 0
    right = len(nums)-1

    # binary search
    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
            
    return nums[left]

    # Time:  O(log n)
    # Space: O(1)

nums = [4,5,6,7,0,1,2]
print(findMin(nums))