from collections import defaultdict
import heapq

def findCheapestPrice(n, flights, src, dst, k) -> int:

    # Build adjacency list
    adj_list = defaultdict(list)
    for u,v,w in flights:
        adj_list[u].append((v,w))

    min_heap = [(0, src, 0)]    # (cost, city, stops)
    best = {(src, 0): 0}        # (city, stops) -> cost

    # Dijkstra's algorithm with stop constraint
    while min_heap:

        cost, city, stops = heapq.heappop(min_heap)

        # early exit when destination reached
        if city == dst: return cost

        # stop limit
        if stops > k: continue

        # explore neighbors 
        for nei, price in adj_list[city]:
            new_cost = cost + price

            # found lower price/cheaper path to neighbor
            if ( (nei, stops+1) not in best) or (new_cost < best[(nei, stops+1)]):
                best[(nei, stops+1)] = new_cost
                heapq.heappush(min_heap, (new_cost, nei, stops+1))

    return -1

    # Time:  O(e * log v)
    # Space: O(v*k + e)

n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0 
dst = 3
k = 1

# n = 3
# flights = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0
# dst = 2
# k = 1

# n = 3
# flights = [[0,1,100],[1,2,100],[0,2,500]] 
# src = 0 
# dst = 2 
# k = 0

# n = 4
# flights = [[0,1,100],[1,2,100],[2,3,500]] 
# src = 0 
# dst = 3 
# k = 1

flights = [[0,1,100],[0,2,500],[1,2,100],[1,3,600],[2,3,100]]
n, src, dst, k = 4, 0, 3, 1
print(findCheapestPrice(n, flights, src, dst, k))