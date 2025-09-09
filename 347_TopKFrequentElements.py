import heapq
from collections import Counter

def topKFrequent(nums, k):
    result = []

    nums_count = Counter(nums)
    # (priority, item) = freq, num)
    nums_count = [(val, key) for key, val in nums_count.items()]

    # min heap
    for nc in nums_count:
        if len(result) < k:
            heapq.heappush(result, nc)
        else:
            heapq.heappushpop(result, nc)

    return [num for _, num in result]

    # Time:  O(n log k)
    # Space: O(n)

nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums, k))
