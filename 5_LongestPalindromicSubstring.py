def longestPalindrome(s: str) -> str:
    n = len(s)

    def get_palindrome(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1

        return left+1, right-1

    start, end = 0,0
    for i in range(n):

        # odd length palindrome
        odd_left, odd_right = get_palindrome(i,i)

        if end - start + 1 < odd_right - odd_left + 1:
            start, end = odd_left, odd_right 

        # even length palindrome
        even_left, even_right = get_palindrome(i,i+1)

        if end - start + 1 < even_right - even_left + 1:
            start, end = even_left, even_right

    return s[start:end+1]

    # Time:  O(n**2)
    # Space: O(1)

s = "babad"
print(longestPalindrome(s))