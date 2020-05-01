# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode, val=0) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return val+root.val
        left = self.sumNumbers(root.left, 10*(val+root.val))
        right = self.sumNumbers(root.right, 10*(val+root.val))
        return left+right