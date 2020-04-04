# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root, value = 0) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 2*value+root.val
        l1 = self.sumRootToLeaf(root.left, 2*value+root.val)
        l2 = self.sumRootToLeaf(root.right, 2*value+root.val)
        
        return l1+l2
        