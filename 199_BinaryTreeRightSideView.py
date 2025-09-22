from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(root):

    right_side = [] # result

    # helper (DFS)
    def dfs(root, depth):
        # base case
        if not root:
            return
        
        # first node seen at depth is on right side
        if depth == len(right_side):
            right_side.append(root.val)

        dfs(root.right, depth + 1)
        dfs(root.left, depth + 1)
        return 

    dfs(root, 0)
    return right_side

    # Time:  O(n)
    # Space: O(h) -> h = height of tree, worst case: n

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
