from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest(root, k) -> int:
    stk = []

    # DFS
    while stk or root:
        # push all left children (find min)
        while root:
            stk.append(root)
            root = root.left

        # visit node
        root = stk.pop()
        k -= 1
        if not k: return root.val

        # go right
        root = root.right

    return -1

    # Time:  O(h+k) -> k = stops after k nodes
    # Space: O(h) -> h = height of tree, worst case: n

#node11 = TreeNode(11, TreeNode(7), TreeNode(2))

#node8 = TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(1)))
#node4 = TreeNode(4, node11)

k = 3
root = TreeNode(3, TreeNode(1, right=TreeNode(2)), TreeNode(4))

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
print(kthSmallest(root, k))
