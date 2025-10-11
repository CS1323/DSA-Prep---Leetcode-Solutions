import heapq

def minCostConnectPoints(points) -> int:

    n = len(points)
    dist = [float("inf")] * n   # min distance
    visited = [False] * n
    node, edges = 0, 0
    total_dist = 0

    # Prim's algorithm to create a Minimum Spanning Tree (MST)
    while edges < n-1:
        visited[node] = True
        nextNode = -1

        # update min distance for all unvisited nodes
        for i in range(n):

            # skip nodes currently in MST
            if visited[i]: continue

            # compute Manhattan distance
            x1, y1 = points[i]
            x2, y2 = points[node]
            curr_dist = abs(x1 - x2) + abs(y1 - y2)

            # keep smallest edge connecting this node to the MST
            dist[i] = min(dist[i], curr_dist)
            
            # track next node w/smallest connection cost
            if nextNode == -1 or dist[i] < dist[nextNode]:
                nextNode = i

        # add new edge
        total_dist += dist[nextNode]
        node = nextNode
        edges += 1

    return total_dist

    # Time:  O(n**2)
    # Space: O(n)

points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
points = [[3,12],[-2,5],[-4,1]]
print(minCostConnectPoints(points))