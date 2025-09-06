from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root) -> bool:

    # helper (DFS)
    def is_valid(root, low, high) -> bool:
        if not root:
            return True

        if not (low < root.val < high):
            return False

        return is_valid(root.left, low, root.val) and is_valid(root.right, root.val, high)

    return is_valid(root, float("-inf"), float("inf"))

    # Time:  O(n)
    # Space: O(h) -> h = height of tree, worst case: n

#root = TreeNode(2, TreeNode(1), TreeNode(3))
root = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
#root = TreeNode(2, TreeNode(2), TreeNode(2))

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
print(isValidBST(root))
