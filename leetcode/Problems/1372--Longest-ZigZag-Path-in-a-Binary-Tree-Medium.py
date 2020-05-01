# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findPath(self, root):
        
        if not root:
            return [-1, -1, -1]
        
        left = self.findPath(root.left)
        right = self.findPath(root.right)
        
        return [1+left[1], 1+right[0], max(1+left[1], 1+right[0], left[2], right[2])]
        
    def longestZigZag(self, root: TreeNode) -> int:
        
        return self.findPath(root)[2]	