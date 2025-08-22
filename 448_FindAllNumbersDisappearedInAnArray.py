def findDisappearedNumbers(nums):
    nums_set = set(nums)
    missing = []

    # add nums not in set
    for n in range(1, len(nums)+1):

        if n not in nums_set:
            missing.append(n)

    return missing

    # Time:  O(n)
    # Space: O(n)

nums = [4,3,2,7,8,2,3,1]
print(findDisappearedNumbers(nums))