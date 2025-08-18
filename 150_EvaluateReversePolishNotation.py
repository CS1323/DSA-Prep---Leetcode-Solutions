def evalRPN(tokens) -> int:
    stk = []

    for t in tokens:

        if t not in "+-*/":
            stk.append(int(t))
        
        else:
            a, b = stk.pop(), stk.pop()

            if t == '+':
                stk.append(a + b)
            elif t == '-':
                stk.append(b - a)
            elif t == '*':
                stk.append(a * b)
            elif t == '/':
                stk.append(int(b / a))
        
    return stk[0]

    # Time:  O(n)
    # Space: O(n)

tokens = ["2","1","+","3","*"]
print(evalRPN(tokens))