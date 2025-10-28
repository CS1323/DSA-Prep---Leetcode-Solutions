def canJump(nums) -> bool:

    n = len(nums)
    goal = n-1  # start at last index

    for i in range(n-1, -1, -1):

        # move goal to the left if reachable
        if i + nums[i] >= goal:
            goal = i
    
    # reached target?
    return goal == 0 

    # Time:  O(n)
    # Space: O(1)

nums = [2,3,1,1,4]
print(canJump(nums))