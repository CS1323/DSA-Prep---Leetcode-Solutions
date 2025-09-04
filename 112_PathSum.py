from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root, targetSum) -> bool:
    # DFS
    if not root:
        return False
   
    targetSum -= root.val
    
    # check path's sum at leaf nodes
    if not root.left and not root.right:
        return targetSum == 0
     
    return hasPathSum(root.left, targetSum) or hasPathSum(root.right, targetSum)
    
    # Time:  O(n)
    # Space: O(h) -> h = height of tree, worst case: n

node11 = TreeNode(11, TreeNode(7), TreeNode(2))

node8 = TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(1)))
node4 = TreeNode(4, node11)

node5 = TreeNode(5, node4, node8)
root = node5

#root = TreeNode(1, TreeNode(2), TreeNode(3))

targetSum = 22

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
print(hasPathSum(root, targetSum))
