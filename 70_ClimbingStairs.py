def climbStairs(n: int) -> int:

    # Base cases:
    # 1 way to climb 1 step (1)
    # 2 ways to climb 2 steps (1+1, 2)
    if n <= 2:
        return n

    # Bottom-Up DP
    prev1, prev2 = 1, 2 # ways to reach (n-2) and (n-1)

    for _ in range(3, n+1): 
        curr = prev1 + prev2
        prev1, prev2 = prev2, curr

    return curr

    # Time:  O(n)
    # Space: O(1)

n = 4
print(climbStairs(n))