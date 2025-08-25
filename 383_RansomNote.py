def canConstruct(ransomNote: str, magazine: str) -> bool:
    letters = {}

    # count letters from magazine
    for c in magazine:
        if c not in letters:
            letters[c] = 1
        else:
            letters[c] += 1

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
