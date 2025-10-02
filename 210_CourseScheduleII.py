from collections import defaultdict, deque

def findOrder(numCourses, prerequisites):

    processed = 0
    in_degree = defaultdict(int)
    res = []

    # create adjacency list
    adj_list = defaultdict(list)
    for u,v in prerequisites:
        adj_list[v].append(u)
        in_degree[u] += 1

    # queue starts with courses having no prerequisites
    q = deque([c for c in range(numCourses) if not in_degree[c]])

    # BFS Topological Sort (Kahn's Algorithm)
    while q:
        node = q.popleft()
        res.append(node)
        processed += 1

        for nei in adj_list[node]:
            in_degree[nei] -= 1
            if not in_degree[nei]: 
                q.append(nei)

    return res if processed == numCourses else []

    # Time:  O(v+e)
    # Space: O(v+e)

numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print(findOrder(numCourses, prerequisites))
