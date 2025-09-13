def letterCombinations(digits):
    digits_map = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl",
                  '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
    curr, res = [], []
    n = len(digits)

    def backtrack(i):
        # base case
        if len(curr) == n:
            res.append(''.join(curr)) # return combination as str - O(n) time
            return
        
        letters = digits_map[digits[i]]

        for l in letters:
            curr.append(l)  # choose
            backtrack(i+1)  # explore next digit's letters
            curr.pop()      # undo

        return    

    if digits:
        backtrack(0)
    return res

    # Time:  O(n * 4**n) -> convert to str * most letter choices**num of digits
    # Space: O(n * 4**n) -> output; O(n) -> stack + path/len(curr) 

digits = "23"
print(letterCombinations(digits))