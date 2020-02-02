# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getSum(self, root, level):
        if not root:
            return 0
        if level == 0:
            return root.val
        return self.getSum(root.left, level-1) + self.getSum(root.right, level-1)
        
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if not root:
            return 0
        sumVal = 0
        if root.val%2 == 0:
            sumVal = self.getSum(root, 2)
        
        return sumVal + self.sumEvenGrandparent(root.left) + self.sumEvenGrandparent(root.right)
        