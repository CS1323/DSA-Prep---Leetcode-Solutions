def majorityElement(nums) -> int:
    ans = 0
    count = 0

    # Boyer-Moore Majority Vote Algorithm
    for n in nums:

        if not count:
            ans = n
            count += 1
        elif n == ans:
            count += 1
        else:
            count -= 1

    return ans

    # Time:  O(n)
    # Space: O(1)

nums = [3,2,3]
print(majorityElement(nums))
