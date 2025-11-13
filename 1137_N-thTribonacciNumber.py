def tribonacci(n: int) -> int:

    # base cases: T(0)=0, T(1)=1, T(2)=1
    prev = [0, 1, 1]

    # Bottom-Up DP
    for i in range(3, n+1):

        curr = sum(prev)
        prev[i % 3] = curr

    return prev[n % 3]

    # Time:  O(n)
    # Space: O(1)

n = 25
print(tribonacci(n))