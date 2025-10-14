def findCheapestPrice(n, flights, src, dst, k) -> int:

    # Bellman-Ford algorithm
    cost = [float("inf")] * n
    cost[src] = 0

    # Relax all edges up to k+1 times
    for _ in range(k+1):
        temp_cost = cost.copy() # Use previous iteration's costs

        for u, v, w in flights: # u = from_city, v = to_city, w = flight_price 
            
            if cost[u] == float("inf"): continue    # skip unreachable nodes

            if cost[u] + w < temp_cost[v]:
                temp_cost[v] = cost[u] + w  # relax edge

        cost = temp_cost    # Use previous iteration's costs

    # Return min cost if reachable
    return cost[dst] if cost[dst] != float("inf") else -1

    # Time:  O(k * e)   -> up to k+1 rounds, we relax all edges once per round
    # Space: O(v)       -> cost to reach each node

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