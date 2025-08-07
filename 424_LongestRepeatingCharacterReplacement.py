def characterReplacement(s: str, k: int) -> int:
    left = 0
    freq_chars = [0] * 26  # Only uppercase English letters
    max_char_count = 0
    max_window_length = 0

    # sliding window for substring
    for right in range(len(s)):

        index = ord(s[right]) - ord('A')
        freq_chars[index] += 1            
        max_char_count = max(max_char_count, freq_chars[index])

        # shrink from left if replacements exceed k
        while (right-left+1) - max_char_count > k:
            freq_chars[ord(s[left]) - ord('A')] -= 1
            left += 1

        max_window_length = max(max_window_length, right-left+1)

    return max_window_length

    # Time:  O(n)
    # Space: O(1) -> 26 characters = max size of hashmap

s = "AABABBA"
k = 1
print(characterReplacement(s,k))