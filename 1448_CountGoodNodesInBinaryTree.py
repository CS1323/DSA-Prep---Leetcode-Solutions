from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def goodNodes(root) -> int:
    max_path_val = root.val  # largest value seen in path
    count = 0

    # helper (DFS)
    def countGood(node, max_path_val):
        nonlocal count

        # base case - empty node
        if not node:
            return
        
        # count good node
        if node.val >= max_path_val:
            count += 1
            max_path_val = node.val

        countGood(node.left, max_path_val)
        countGood(node.right, max_path_val)
        return
    
    countGood(root, max_path_val)
    return count

    # Time:  O(n)
    # Space: O(h) -> h = height of tree, worst case: n

node1 = TreeNode(1, TreeNode(3))
# node3 = TreeNode(3, TreeNode(4), TreeNode(2))
node4 = TreeNode(4, TreeNode(1), TreeNode(5))

root = TreeNode(3, node1, node4)

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
print(goodNodes(root))
