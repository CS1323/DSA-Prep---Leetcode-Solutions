def twoSum(numbers, target):
    left = 0
    right = len(numbers)-1

    while left < right:
        total = numbers[left] + numbers[right]

        if total < target:
            left += 1
        elif total > target:
            right -= 1
        else:
            return [left+1, right+1]
        
    return []

    # Time:  O(n)
    # Space: O(1)

numbers = [2, 7, 11, 15]
target = 9
print(twoSum(numbers, target))