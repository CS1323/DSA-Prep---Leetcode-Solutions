def numJewelsInStones(jewels: str, stones: str) -> int:
    jewels_set = set(jewels)
    jewel_count = 0

    for s in stones:
        if s in jewels_set:
            jewel_count += 1

    return jewel_count

    # Time:  O(n)
    # Space: O(n)

jewels = "aA"
stones = "aAAbbbb"
print(numJewelsInStones(jewels, stones))