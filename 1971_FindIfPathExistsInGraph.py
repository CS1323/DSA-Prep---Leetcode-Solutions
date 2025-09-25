from collections import defaultdict, deque

def validPath(n, edges, source, destination) -> bool:

    # create adjacency list (undirected)
    adj_list = defaultdict(list)
    for u,v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)

    # BFS
    seen = set()
    q = deque([source])

    while q:
        node = q.popleft()

        # found path
        if node == destination: 
            return True
        
        seen.add(node)

        # continue search w/unseen nodes
        for nei in adj_list[node]: 
            if nei not in seen:
                q.append(nei)

    return False

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