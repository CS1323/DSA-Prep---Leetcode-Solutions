def subsets(nums):
    n = len(nums)
    subset, res = [], []

    def backtrack(i):
        if i >= n:
            res.append(subset.copy())
            return
        
        # DON'T pick nums[i]
        backtrack(i+1)

        # pick nums[i]
        subset.append(nums[i])
        backtrack(i+1)
        subset.pop()

    backtrack(0)
    return res

    # Time:  O(n * 2**n) -> n = copy subset, 2**n = DFS (recursion)
    # Space: O(n * 2**n) -> n = len(subset), 2**n = len(res) 

nums = [1,2,3]
print(subsets(nums))