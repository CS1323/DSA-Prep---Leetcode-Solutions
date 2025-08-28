from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root) -> int:
    # depth first search
    if not root:
        return 0

    left = maxDepth(root.left)
    right = maxDepth(root.right)
    
    return 1 + max(left, right)

    # Time:  O(n)
    # Space: O(h) -> h = height of tree, worst case: n

node15 = TreeNode(15)
node7 = TreeNode(7)

node9 = TreeNode(9)
node20 = TreeNode(20, node15, node7)

node3 = TreeNode(3, node9, node20)
root = node3

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
print(maxDepth(root))
