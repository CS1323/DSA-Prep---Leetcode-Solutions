from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root):
    # depth first search
    if not root:
        return

    invertTree(root.left)
    invertTree(root.right)
    root.left, root.right = root.right, root.left
    
    return root

    # Time:  O(n)
    # Space: O(h) -> h = height of tree, worst case: n

node1 = TreeNode(1)
node3 = TreeNode(3)
node6 = TreeNode(6)
node9 = TreeNode(9)

node2 = TreeNode(2, node1, node3)
node7 = TreeNode(7, node6, node9)

node4 = TreeNode(4, node2, node7)
root = node4

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
root = invertTree(root)
display(root)
