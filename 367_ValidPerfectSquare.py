def isPerfectSquare(num: int) -> bool:
    left = 1
    right = num

    # binary search
    while left <= right:
        mid = left + ((right - left) // 2)
        square = mid * mid

        if square < num:
            left = mid + 1
        elif square > num:
            right = mid - 1
        else:
            return True

    return False

    # Time:  O(log n)
    # Space: O(1)

num = 16
print(isPerfectSquare(num))
