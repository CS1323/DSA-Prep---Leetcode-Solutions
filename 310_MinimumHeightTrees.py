from collections import defaultdict, deque

def findMinHeightTrees(n, edges):

    # base case
    if n == 1:
        return [0]

    adj_list = defaultdict(list)
    in_degree = defaultdict(int)

    # Build adjacency list and degree counts
    for u,v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
        in_degree[u] += 1
        in_degree[v] += 1

    # Initialize queue with leaf nodes
    q = deque()
    for i in range(n):
        if in_degree[i] == 1:
            q.append(i)

    # Trim leaves layer by layer (BFS)
    remaining_nodes = n
    while remaining_nodes > 2:

        for _ in range(len(q)):
            leaf = q.popleft()
            remaining_nodes -= 1

            for nei in adj_list[leaf]:
                in_degree[nei] -= 1

                if in_degree[nei] == 1:
                    q.append(nei)

    return list(q)  # remaining nodes = center (1 or 2)

    # Time:  O(v+e)
    # Space: O(v+e)

n = 4
edges = [[1,0],[1,2],[1,3]]
n = 6
edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
print(findMinHeightTrees(n, edges))