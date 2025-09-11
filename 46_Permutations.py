def permute(nums):
    n = len(nums)
    curr, res = [], []

    def backtrack():
        # base case
        if len(curr) == n:
            res.append(curr.copy())
            return

        # explore choices
        for num in nums:
            if num not in curr:
                curr.append(num)    # choose
                backtrack()         # explore
                curr.pop()          # undo

        return

    backtrack()
    return res

    # Time:  O(n! * n) -> num of perm * num of choices
    # Space: O(n! * n) -> length of output

nums = [1,2,3]
print(permute(nums))
