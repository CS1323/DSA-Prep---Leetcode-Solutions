def fib(n: int) -> int:

    # base cases
    if n <= 1:
        return n

    # Bottom-Up DP
    prev, curr = 0, 1   # (n-2), (n-1)

    for _ in range(2, n+1):
        prev, curr = curr, prev + curr

    return curr

    # Time:  O(n)
    # Space: O(1)

n = 2
print(fib(n))