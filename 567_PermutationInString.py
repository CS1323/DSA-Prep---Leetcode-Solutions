def checkInclusion(s1: str, s2: str) -> bool:
    s1_length = len(s1)
    s2_length = len(s2)

    # edge case
    if s1_length > s2_length:
        return False
    
    s1_chars_seen = [0] * 26
    s2_chars_seen = [0] * 26
    
    # initialize arrays for comparison
    for i in range(s1_length):
        s1_chars_seen[ord(s1[i]) - ord('a')] += 1
        s2_chars_seen[ord(s2[i]) - ord('a')] += 1

    # first check
    if s1_chars_seen == s2_chars_seen:
        return True

    # fixed sliding window
    for i in range(s1_length, s2_length):

        s2_chars_seen[ord(s2[i]) - ord('a')] += 1
        s2_chars_seen[ord(s2[i - s1_length]) - ord('a')] -= 1

        if s1_chars_seen == s2_chars_seen:
            return True

    return False

    # Time:  O(n)
    # Space: O(1)

s1 = "ab"
s2 = "eidbaooo"
print(checkInclusion(s1, s2))