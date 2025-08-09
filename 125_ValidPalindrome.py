def isPalindrome(s) -> bool:
    left = 0
    right = len(s)-1

    while left < right:
        
        # skip special characters
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1

    return True

    # Time:  O(n)
    # Space: O(1)

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))