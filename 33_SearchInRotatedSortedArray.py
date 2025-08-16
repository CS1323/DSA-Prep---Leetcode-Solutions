def search(nums, target) -> int:
    # search for minimum - condition based binary
    n = len(nums)-1
    left = 0
    right = n

    while left < right:
        mid = left + ((right - left) // 2)

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    # reduce target range
    if target <= nums[n]:
        right = n
    elif target < nums[0]: # if left > target > right
        return -1
    else:
        right = left-1
        left = 0

    # search for target - traditional binary
    while left <= right:
        mid = left + ((right - left) // 2)

        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid

    return -1

    # Time:  O(log n)
    # Space: O(1)

nums = [4,5,6,7,0,1,2]
target = 0
print(search(nums, target))
