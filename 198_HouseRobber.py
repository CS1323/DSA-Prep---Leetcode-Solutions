def rob(nums) -> int:

    # initialize dp states
    prev2, prev1 = 0, 0

    # Bottom-Up DP -> build up the max money accumulated at each house
    for num in nums:
        curr = max(prev1, prev2 + num)
        prev2, prev1 = prev1, curr

    return prev1

    # Time:  O(n)
    # Space: O(1)

nums = [1,2,3,1]
nums = [2,7,9,3,1]
print(rob(nums))