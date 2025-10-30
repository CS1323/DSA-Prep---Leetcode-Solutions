def jump(nums) -> int:

    L = R = 0   # current jump range
    jumps = 0   # total jumps made

    while R < len(nums)-1:
        
        farthest = 0    # farthest reachable index

        for i in range(L, R+1):
            farthest = max( farthest, (i + nums[i]) )

        # update next reachable window
        L = R+1
        R = farthest

        jumps += 1

    return jumps

    # Time:  O(n)
    # Space: O(1)

nums = [2,3,1,1,4]
print(jump(nums))