import heapq

class KthLargest:

    def __init__(self, k, nums):
        self.k = k
        self.heap = []  # min heap (size k)

        for val in nums: self.add(val)  # kth largest at top of heap

    def add(self, val: int) -> int:

        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        else:
            heapq.heappushpop(self.heap, val)

        return self.heap[0]

    # Time:  O(n log k)
    # Space: O(k)

kthLargest = KthLargest(3, [4, 5, 8, 2])
print(kthLargest.add(3))    # return 4
print(kthLargest.add(5))    # return 5
print(kthLargest.add(10))   # return 5
print(kthLargest.add(9))    # return 8
print(kthLargest.add(4))    # return 8