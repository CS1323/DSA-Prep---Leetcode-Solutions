def generateParenthesis(n):
    curr, res = [], []

    def backtrack(open_count, close_count):
        # base case
        if open_count == close_count == n:
            res.append("".join(curr))
            return
        
        # add '('
        if open_count < n:
            curr.append('(')                        # choose
            backtrack(open_count+1, close_count)    # explore
            curr.pop()                              # undo

        # add ')' when there's '('
        if close_count < open_count:
            curr.append(')')                        # choose
            backtrack(open_count, close_count+1)    # explore
            curr.pop()                              # undo

        return

    backtrack(0, 0)
    return res

    # Time:  O(n * C(n)) -> C(n) = nth Catalan number = (2n)! / ((n + 1)! * n!)
    # Space: O(n * C(n))

n = 3
print(generateParenthesis(n))