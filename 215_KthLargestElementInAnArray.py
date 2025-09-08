import heapq

def findKthLargest(nums, k) -> int:

    min_heap = []   # size k

    for num in nums:
        
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        
        # remove min to push new num
        else:
            heapq.heappushpop(min_heap, num)

    return min_heap[0]

    # Time:  O(n log k)
    # Space: O(k)

nums = [3,2,1,5,6,4]
k = 2
print(findKthLargest(nums, k))
