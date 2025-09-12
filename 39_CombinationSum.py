def combinationSum(candidates, target):
    candidates.sort()
    curr, res = [], []

    def backtrack(start, total):
        # base case - sum matches target
        if total == target:
            res.append(curr.copy())
            return
        
        for i in range(start, len(candidates)):
            # break early - no need to check larger nums
            if total + candidates[i] > target:
                break

            curr.append(candidates[i])          # choose
            backtrack(i, total + candidates[i]) # explore - reuse allowed
            curr.pop()                          # undo
        return

    backtrack(0, 0)
    return res

    # Time:  O( 2**(t/m) ) -> t = target, m = min(candidates)
    # Space: O(t/m) -> auxiliary (extra) space

candidates = [2,3,6,7]
target = 7
print(combinationSum(candidates, target))
