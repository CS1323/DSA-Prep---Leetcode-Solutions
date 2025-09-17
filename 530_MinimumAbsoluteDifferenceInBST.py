from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def getMinimumDifference(root) -> int:
    min_diff = float('inf')
    prev = float('inf')

    # helper - inorder DFS
    def dfs(curr):
        nonlocal min_diff, prev

        if not curr:
            return
        
        dfs(curr.left)

        # process: update min_diff
        min_diff = min(abs(prev - curr.val), min_diff)
        prev = curr.val

        dfs(curr.right)

        return

    dfs(root)
    return min_diff

    # Time: O(n)
    # Space: O(h) -> h = height of tree, worst case: n

root = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))

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
print(getMinimumDifference(root))