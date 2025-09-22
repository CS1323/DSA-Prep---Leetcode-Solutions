from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(root):

    # base case
    if not root:
        return []
    
    q = deque([root])
    right_side = [] # result

    # BFS
    while q:

        for _ in range(len(q)):
            node = q.popleft()

            if node.left: q.append(node.left)
            if node.right: q.append(node.right)

        # last node added to queue will be on right side
        right_side.append(node.val) 

    return right_side

    # Time:  O(n)
    # Space: O(n) -> if balanced tree, queue hold ~n/2 nodes

node2 = TreeNode(2, right=TreeNode(5))
node3 = TreeNode(3, right=TreeNode(4))
root = TreeNode(1, left=node2, right=node3)

def pre_order(node, vals):
    if not node:
        return
    vals.append(str(node.val))
    pre_order(node.left, vals)
    pre_order(node.right, vals)

def breadth_first(root):
    queue = deque()
    queue.append(root)
    vals = []

    while queue:
        node = queue.popleft()
        vals.append(str(node.val))

        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)

    return vals

def display(root):
    #vals = []
    #pre_order(root, vals)
    vals = breadth_first(root)
    print(" -> ".join(vals))

display(root)
print(rightSideView(root))
