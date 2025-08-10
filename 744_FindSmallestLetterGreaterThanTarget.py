def nextGreatestLetter(letters, target) -> str:
    left = 0
    right = len(letters)-1
    next_greatest = letters[0]

    # binary search
    while left <= right:
        mid = (left + right) // 2

        if letters[mid] > target:
            next_greatest = letters[mid]
            right = mid - 1
        else:
            left = mid + 1

    return next_greatest

    # Time:  O(log n)
    # Space: O(1)

letters = ["c","f","j"]
target = "a"
print(nextGreatestLetter(letters, target))