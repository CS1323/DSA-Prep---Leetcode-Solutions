from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node):

    old_to_new = {} # refers old node to new/copied node

    # helper (DFS)
    def clone(node):
        if node in old_to_new:
            return old_to_new[node]
        
        copy = Node(node.val)
        old_to_new[node] = copy

        for nei in node.neighbors:
            copy.neighbors.append(clone(nei))

        return copy

    return clone(node) if node else None

    # Time:  O(v+e) -> v=vertices, e=edges
    # Space: O(v)   -> extra for hashmap and stack, O(v+e) for output

def display(start, num_vertices):
    seen = set([start.val])
    q = deque([start])
    res = [0] * num_vertices

    while q:
        node = q.popleft()
        neighbors = []

        for nei in node.neighbors:
            neighbors.append(nei.val)

            if nei.val not in seen:
                seen.add(nei.val)
                q.append(nei)

        res[node.val-1] = neighbors
    
    print(res)

adjList = [[2,4],[1,3],[2,4],[1,3]]

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4, [node1, node3])

node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]

display(node1, 4)

display(cloneGraph(node1), 4)