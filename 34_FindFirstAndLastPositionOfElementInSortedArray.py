def searchRange(nums, target):
    # binary search for starting index
    left = 0
    right = len(nums)-1
    start_index = -1

    while left <= right:
        mid = (right + left) // 2

        if nums[mid] == target:
            start_index = mid
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # binary search for ending index
    left = 0
    right = len(nums)-1
    end_index = -1

    while left <= right:
        mid = (right + left) // 2

        if nums[mid] == target:
            end_index = mid
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return [start_index, end_index]

    # Time:  O(log n)
    # Space: O(1)

nums = [5,7,7,8,8,10]
target = 8
print(searchRange(nums, target))