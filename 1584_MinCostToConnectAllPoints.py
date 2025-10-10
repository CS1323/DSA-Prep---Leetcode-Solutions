import heapq

def minCostConnectPoints(points) -> int:

    n = len(points)
    total_dist = 0
    visited = set()
    min_heap = [(0, 0)]     # (dist, point_index)

    # Prim's algorithm to create a Minimum Spanning Tree (MST)
    while len(visited) < n:
        dist, i = heapq.heappop(min_heap)

        if i in visited: continue

        total_dist += dist
        visited.add(i)

        # Push edges from this new point to all unvisited points
        for j in range(n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            new_dist = abs(x1 - x2) + abs(y1 - y2)
            heapq.heappush(min_heap, (new_dist, j))

    return total_dist

    # Time:  O(n**2 log n)
    # Space: O(n**2)

points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
points = [[3,12],[-2,5],[-4,1]]
print(minCostConnectPoints(points))