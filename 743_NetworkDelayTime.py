from collections import defaultdict
import heapq

def networkDelayTime(times, n, k) -> int:

    # Build adjacency list
    adj_list = defaultdict(list)
    for u, v, w in times:
        adj_list[u].append((v, w))
    
    dist = [float("inf")] * n
    dist[k-1] = 0

    min_heap = [(0, k)]

    # Dijkstra's algorithm
    # Process nodes in order of increasing distance
    while min_heap:

        curr_dist, node = heapq.heappop(min_heap)

        # skip outdated entries
        if curr_dist > dist[node-1]: continue

        
        for nei, weight in adj_list[node]:

            # found shorter path to neighbor
            if curr_dist + weight < dist[nei-1]:
                dist[nei-1] = curr_dist + weight
                heapq.heappush(min_heap, (dist[nei-1], nei))

    max_dist = max(dist)
    return max_dist if max_dist != float("inf") else -1

    # Time:  O(e * log v)
    # Space: O(v+e)

times = [[2,1,1],[2,3,1],[3,4,1]] 
n = 4 
k = 2

# times = [[1,2,1]] 
# n = 2
# k = 1

# times = [[1,2,1]]
# n = 2
# k = 2
print(networkDelayTime(times, n, k))