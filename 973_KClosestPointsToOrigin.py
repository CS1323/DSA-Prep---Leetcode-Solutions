import heapq, math

def kClosest(points, k):
    dist_heap = [] # max heap

    for x,y in points:
        d = x**2 + y**2 # calc distance from origin

        if len(dist_heap) < k:
            heapq.heappush(dist_heap, (-d, x, y))

        else:
            heapq.heappushpop(dist_heap, (-d, x, y))

    return [[x,y] for _, x, y in dist_heap]

    # Time:  O(n log k)
    # Space: O(k)

points = [[1,3],[-2,2]]
k = 1 
print(kClosest(points, k))
