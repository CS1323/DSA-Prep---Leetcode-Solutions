# Disjoint Set Union (DSU) / Union-Find
class DSU:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.size = [1] * (n+1)

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        # already connected
        if pu == pv:
            return False
        
        # union by size
        if self.size[pu] < self.size[pv]:
            pu, pv = pv, pu
        self.size[pu] += self.size[pv]
        self.parent[pv] = pu
        return True

# Kruskal's algorithm using DSU
def connectCities(n, connections) -> int:

    # sort all edges by cost (smallest first)
    connections.sort(key=lambda x: x[2])

    dsu = DSU(n)    
    total_dist = 0

    # connect cities and add cost
    for u, v, dist in connections:
        if dsu.union(u, v):
            total_dist += dist
            n -= 1  # num of separate components
    
    # return total cost if all cities are connected
    return total_dist if n == 1 else -1

    # Time:  O(e log e)
    #   - Sorting edges: O(e log e)
    #   - Union-Find operations: O(e * α(n)) ≈ O(e)
    # Space: O(v+e)
    #   - DSU arrays: O(n)
    #   - Sorted edges: O(e)

n = 3
connections = [
  [1, 2, 5],
  [1, 3, 6],
  [2, 3, 1]
]

print(connectCities(n, connections))