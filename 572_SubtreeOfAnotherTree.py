from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSubtree(root, subRoot) -> bool:

    # helper to check equivalency (DFS)
    def checkSubtree(p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False

        return checkSubtree(p.left, q.left) and checkSubtree(p.right, q.right)

    # traversal (DFS)
    if not root:
        return False

    if checkSubtree(root, subRoot):
        return True

    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)
    
    # Time:  O(n*m) -> n = nodes in root, m = nodes in subRoot
    # Space: O(h) -> h = height of tree, worst case: n

#node11 = TreeNode(11, TreeNode(7), TreeNode(2))

#node8 = TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(1)))
#node4 = TreeNode(4, node11)

#node5 = TreeNode(5, node4, node8)
subRoot = TreeNode(4, TreeNode(1), TreeNode(2))
node4 = TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0)))

root = TreeNode(3, node4, TreeNode(5))

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
print(isSubtree(root, subRoot))
