# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root:
            return None
        
        def depth(parent, root, val, level):
            if not root:
                return (None, level)
            if root:
                if root.val != val:
                    left = depth(root, root.left, val, level+1)
                    right = depth(root, root.right, val, level+1)
                    if left[0]:
                        return left
                    elif right[0]:
                        return right
                    else:
                        return (None, level)
                else:
                    return (parent, level)
        
        xd, yd = depth(None, root, x, 0), depth(None, root, y, 0)
        return xd[0] != yd[0] and xd[1] == yd[1]