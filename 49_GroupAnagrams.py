from collections import defaultdict

def groupAnagrams(strs):
    anagrams_dict = defaultdict(list)

    for string in strs:  # n

        count = [0] * 26
        for c in string: # m
            count[ord(c) - ord('a')] += 1
        key = tuple(count)
        
        anagrams_dict[key].append(string)
        
    return list(anagrams_dict.values())

    # Time:  O(n*m)
    # Space: O(n*m) "all of the chars"

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))
