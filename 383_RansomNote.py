from collections import Counter
def canConstruct(ransomNote: str, magazine: str) -> bool:
    letters = Counter(magazine) # count letters from magazine
    
    # check if magazine has needed letters
    for c in ransomNote:
        if c not in letters:
            return False
        else:
            letters[c] -= 1
            
            if letters[c] <= 0:
                del letters[c]

    return True

    # Time:  O(n)
    # Space: O(n)

ransomNote = "a"
magazine = "b"
print(canConstruct(ransomNote, magazine))
