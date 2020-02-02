# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumTree(self, root):
        if not root:
            return 0
        return root.val + self.sumTree(root.right) + self.sumTree(root.left)
    def maxProductSum(self, root):
        if not root:
            return 0
        rootSum = root.val + self.maxProductSum(root.right) + self.maxProductSum(root.left)
        # print(root.val, rootSum)
        if  abs((self.sumVal)/2 - rootSum) < self.diff:
            
            self.diff = abs((self.sumVal)/2 - rootSum)
            self.answer = rootSum
            # print('update', self.answer, self.diff)
        return rootSum
        
    def maxProduct(self, root: TreeNode) -> int:
        self.sumVal = self.sumTree(root)
        self.diff = self.sumVal
        self.answer = 0
        _ = self.maxProductSum(root)
        
        modVal = 10**9 + 7
        return ((self.answer%modVal) * ((self.sumVal-self.answer)%modVal))%modVal
        