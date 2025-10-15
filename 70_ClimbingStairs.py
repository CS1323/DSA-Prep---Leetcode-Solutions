def climbStairs(n: int) -> int:

    # Store previously computed results (base cases)
    memo = {1:1, 2:2}

    # helper function for Top-Down DP
    def climb(n):
        # return cached result if already computed
        if n in memo:
            return memo[n]
        
        memo[n] = climb(n-1) + climb(n-2)
        return memo[n]

    return climb(n)

    # Time:  O(n)
    # Space: O(n)

n = 4
print(climbStairs(n))