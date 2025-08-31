from collections import Counter

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t): return False

    s_count = Counter(s)
    t_count = Counter(t)

    return s_count == t_count

    # Time:  O(n)
    # Space: O(n)

s = "anagram"
t = "nagaram"
print(isAnagram(s,t))
