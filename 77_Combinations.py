def combine(n: int, k: int):
    curr, res = [], []

    def backtrack(start):
        # base case
        if len(curr) == k:
            res.append(curr.copy())
            return
        
        for i in range(start, n+1):
            curr.append(i)  # choose
            backtrack(i+1)  # explore with next int
            curr.pop()      # undo

        return

    backtrack(1)    # range starts at 1
    return res

    # Time:  O(k * C(n,k)) -> k * (n! / [k! * (n-k)!])
    # Space: O(k * C(n,k)) -> k * (n! / [k! * (n-k)!])

n = 4
k = 2
print(combine(n,k))