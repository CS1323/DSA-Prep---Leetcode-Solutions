import math

def minEatingSpeed(piles, h) -> int:
    left = 1
    right = max(piles)

    # binary search - condition based
    while left < right:
        # eating speed
        k = left + ((right - left) // 2)

        # sum total hours given eating speed
        hours = 0
        for p in piles:
            hours += math.ceil(p/k)

        # update minimum k
        if hours <= h:
            right = k
        else:
            left = k + 1

    return right 

    # Time:  O( n * log(m) ) -> m = max(piles)
    # Space: O(1)

piles = [3, 6, 7, 11]
h = 8
print(minEatingSpeed(piles, h))
