from collections import defaultdict
import heapq

def connectCities(n, connections) -> int:

    # Build adjacency list
    adj_list = defaultdict(list)
    for u,v,w in connections:
        adj_list[u].append((v,w))
        adj_list[v].append((u,w))

    total_dist = 0
    visited = set()
    min_heap = [(0,1)]  # (cost, city)

    # Prim's algorithm (using min_heap)
    while min_heap:

        cost, curr_city = heapq.heappop(min_heap)

        if curr_city in visited: continue

        visited.add(curr_city)
        total_dist += cost

        # push all edges to unvisited neighbors
        for nei, edge_cost in adj_list[curr_city]:
            if nei not in visited:
                heapq.heappush(min_heap, (edge_cost, nei))
                
    # check if all cities are connected
    return total_dist if len(visited) == n else -1

    # Time:  O(e * log v)
    # Space: O(v+e)

n = 3
connections = [
  [1, 2, 5],
  [1, 3, 6],
  [2, 3, 1]
]

print(connectCities(n, connections))