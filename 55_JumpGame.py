def canJump(nums) -> bool:

    n = len(nums)
    # memoization: stores whether the end is reachable from index i
    # base case: last index can obviously reach itself
    memo = {n-1: True}

    # Top-Down DP helper function
    def can_reach(i):

        if i in memo:
            return memo[i]
        
        # try all possible jumps from current position
        for jump in range(1, nums[i] + 1):
            if can_reach(i + jump):
                memo[i] = True
                return True
            
        # if none of the jumps work
        memo[i] = False
        return False
        
    return can_reach(0) # start recursion w/first index

    # Time:  O(n**2)
    # Space: O(n)

nums = [2,3,1,1,4]
print(canJump(nums))