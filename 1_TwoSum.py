def twoSum(nums, target):
    nums_seen = {}

    for index, num in enumerate(nums):
        complement = target - num

        # check hashmap if complement is there
        if complement in nums_seen:
            return [nums_seen[complement], index]
        
        nums_seen[num] = index

    return [] # No solution found

    # Time:  O(n)
    # Space: O(n)

nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))