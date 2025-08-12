def reverseString(s) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    s_length = len(s)

    for i in range(s_length//2):
        s[i], s[-i-1] = s[-i-1], s[i]

    return

    # Time:  O(n)
    # Space: O(1)

s = ["h","e","l","l","o"]
reverseString(s)
print(s)