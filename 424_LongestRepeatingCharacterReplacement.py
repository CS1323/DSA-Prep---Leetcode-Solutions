def characterReplacement(s: str, k: int) -> int:
    left = 0
    freq_chars = {}
    max_char_count = 0
    max_window_length = 0

    # sliding window for substring
    for right in range(len(s)):
        
        if s[right] in freq_chars:
            freq_chars[s[right]] = freq_chars[s[right]] + 1
        else:
            freq_chars[s[right]] = 1
        
        max_char_count = max(max_char_count, freq_chars[s[right]])

        # shrink from left if replacements exceed k
        while (right-left+1) - max_char_count > k:
            freq_chars[s[left]] = freq_chars[s[left]] - 1

            if freq_chars[s[left]] <= 0:
                del freq_chars[s[left]]
            left += 1

        max_window_length = max(max_window_length, right-left+1)

    return max_window_length

    # Time:  O(n)
    # Space: O(1) -> 26 characters = max size of hashmap

s = "AABABBA"
k = 1
print(characterReplacement(s,k))