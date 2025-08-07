def lengthOfLongestSubstring(s) -> int:
    left = 0
    unique_chars = set() # keep track of unique characters seen
    longest_substring_count = 0

    # sliding window for substring
    for right in range(len(s)):
        
        while s[right] in unique_chars:
            unique_chars.remove(s[left])
            left += 1

        unique_chars.add(s[right])
        longest_substring_count = max(longest_substring_count, len(unique_chars))
        
    return longest_substring_count

    # Time:  O(n)
    # Space: O(min(n,m)) -> m = 128 ASCII characters

s = "pwwkew"
print(lengthOfLongestSubstring(s))