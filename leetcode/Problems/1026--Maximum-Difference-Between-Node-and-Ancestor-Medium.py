# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def helper(root, minVal, maxVal, currentMax):
            if not root:
                return currentMax
            
            answer = max(abs(root.val-minVal), abs(root.val-maxVal), currentMax)
            left = helper(root.left, min(root.val, minVal), max(root.val, maxVal), answer)
            right = helper(root.right, min(root.val, minVal), max(root.val, maxVal), answer)
            
            return max(answer, left, right)
        return helper(root, root.val, root.val, 0)
            