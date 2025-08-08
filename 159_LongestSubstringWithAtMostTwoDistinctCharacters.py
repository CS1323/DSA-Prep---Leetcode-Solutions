def lengthOfLongestSubstring(s) -> int:
    left = 0
    char_freq = {}
    max_window_length = 0

    # sliding window for substring
    for right in range(len(s)):

        if s[right] in char_freq:
            char_freq[s[right]] += 1
        else:
            char_freq[s[right]] = 1

        # shrink from left if more than 2 distinct characters
        while len(char_freq) > 2:
            char_freq[s[left]] -= 1

            if char_freq[s[left]] <= 0:
                del char_freq[s[left]]

            left += 1

        max_window_length = max(right-left+1, max_window_length)

    return max_window_length

    # Time:  O(n)
    # Space: O(1)

s = "ccaabbb"
print(lengthOfLongestSubstring(s))