# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isUni(self, root, val):
        if not root:
            return True
        return self.isUni(root.right, val) and self.isUni(root.left, val) and root.val == val

    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isUni(root, root.val)
