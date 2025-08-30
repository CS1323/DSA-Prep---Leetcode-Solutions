from collections import Counter
def maxNumberOfBalloons(text: str) -> int:
    balloon = {'b':1, 'a':1, 'l':2, 'o':2, 'n':1}
    text_dict = Counter(text)
    max_balloons = float("inf")

    for c in balloon:
        if c not in text_dict:
            return 0
        
        if text_dict[c] // balloon[c] < max_balloons:
            max_balloons = text_dict[c] // balloon[c]

    return max_balloons

    # Time:  O(n)
    # Space: O(1)

text = "nlaebolko"
print(maxNumberOfBalloons(text))
