# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.maxVal = 0
    def getSum(self, root):
        if not root:
            return 0
        left = max(0, self.getSum(root.left))
        right = max(0, self.getSum(root.right))
        
        self.maxVal = max(self.maxVal, root.val+left+right )
        
        return max(left, right) + root.val
    
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.maxVal = root.val
        self.getSum(root)
        return self.maxVal