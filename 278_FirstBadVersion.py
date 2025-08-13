# given API
def isBadVersion(version: int) -> bool:
    bad = 4     # change for the respective test case
    return (version >= bad)

# leetcode problem
def firstBadVersion(n: int) -> int:
    left = 1
    right = n

    # binary search - condition based
    while left < right:
        mid = left + ((right-left) // 2) # to avoid overflow

        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1

    return left

    # Time:  O(log n)
    # Space: O(1)

n = 5
print(firstBadVersion(n))