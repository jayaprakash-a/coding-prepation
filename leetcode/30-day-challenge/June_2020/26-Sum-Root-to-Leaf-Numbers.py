# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode, val=0) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return val + root.val
        left = self.sumNumbers(root.left, 10*(val+root.val))
        right = self.sumNumbers(root.right, 10*(val+root.val))
        return left+right