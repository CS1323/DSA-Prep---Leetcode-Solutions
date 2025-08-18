def isValid(s: str) -> bool:
    hashmap = {')':'(', ']':'[', '}':'{'}
    stk = []

    # edge case - not all are paired
    if len(s) % 2:
        return False

    # adds open brackets to stack and pops closed for validation
    for bracket in s:

        if bracket in "([{":
            stk.append(bracket)

        else:
            # includes edge case - first char is in ")]}"
            if not stk or stk.pop() != hashmap[bracket]:
                return False

    return not stk

    # Time:  O(n)
    # Space: O(n)

s = "([])"
print(isValid(s))