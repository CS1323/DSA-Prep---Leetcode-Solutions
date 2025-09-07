from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowestCommonAncestor(root, p, q):

    # DFS
    while root:

        # node is larger than both p & q -> go left
        if p.val < root.val and q.val < root.val:
            root = root.left
        
        # node is smaller than both p & q -> go right
        elif p.val > root.val and q.val > root.val:
            root = root.right

        # guranteed p & q -> gurantees LCA
        else:
            return root

    # Time:  O(n) -> best case: log(n)
    # Space: O(1) -> recursive: h

node3 = TreeNode(3)
node5 = TreeNode(5)

node0 = TreeNode(0)
node4 = TreeNode(4, node3, node5)
node7 = TreeNode(7)
node9 = TreeNode(9)

node2 = TreeNode(2, node0, node4)
node8 = TreeNode(8, node7, node9)

root = TreeNode(6, node2, node8)

p = node3
q = node5

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
print(lowestCommonAncestor(root, p, q).val)
