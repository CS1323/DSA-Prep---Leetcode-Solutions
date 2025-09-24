from collections import defaultdict

def validPath(n, edges, source, destination) -> bool:

    adj_list = defaultdict(list)
    seen = set()

    # create adjacency list (undirected)
    for u,v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)

    # helper (DFS)
    def dfs(node):

        # found path
        if node == destination:
            return True
        
        seen.add(node)
        
        # continue search w/unseen nodes
        for nei in adj_list[node]:
            if nei not in seen and dfs(nei):
                return True

        return False

    return dfs(source)

    # Time:  O(v+e) -> v=vertices, e=edges
    # Space: O(v+e)

n = 3
edges = [[0,1],[1,2],[2,0]]
source = 0
destination = 2

# n = 6
# edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
# source = 0
# destination = 5

print(validPath(n, edges, source, destination))