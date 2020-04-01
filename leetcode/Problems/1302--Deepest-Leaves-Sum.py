# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getHeight(self, root):
        if not root:
            return 0
        return max(self.getHeight(root.left), self.getHeight(root.right))+1
    def getSum(self, root, height):
        if not root:
            return 0
        if height == 1:
            return root.val
        
        return self.getSum(root.left, height-1) +  self.getSum(root.right, height-1)
    
    def deepestLeavesSum(self, root: TreeNode) -> int:
        height = self.getHeight(root)
        sumVal = self.getSum(root, height)
        
        return sumVal
        