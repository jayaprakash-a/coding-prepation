# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode, left_or_right = 0) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            if left_or_right == -1:
                return root.val
            else:
                return 0
        return self.sumOfLeftLeaves(root.left, -1) + self.sumOfLeftLeaves(root.right, 1)