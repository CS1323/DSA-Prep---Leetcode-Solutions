import heapq

def lastStoneWeight(stones) -> int:

    # max heap
    stones = [-s for s in stones]   # n
    heapq.heapify(stones)           # n

    # diff of two heaviest stones until one or none remain
    while len(stones) > 1:          # n
        stone1 = heapq.heappop(stones)  # log n
        stone2 = heapq.heappop(stones)  # log n
        if stone1 != stone2:
            heapq.heappush(stones, stone1-stone2)  # log n
        
    # return 0 if no stones remain
    return -stones[0] if stones else 0

    # Time:  O(n log n)
    # Space: O(n)

stones = [2,7,4,1,8,1]
print(lastStoneWeight(stones))
