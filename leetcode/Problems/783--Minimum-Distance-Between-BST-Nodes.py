# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.traversal = []
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.traversal.append(root.val)
            self.inorder(root.right)
    def minDiffInBST(self, root: TreeNode) -> int:
        self.inorder(root)
        minDiff = self.traversal[-1] - self.traversal[0]
        for i in range(len(self.traversal)-1):
            if self.traversal[i+1]-self.traversal[i] < minDiff:
                minDiff = self.traversal[i+1]-self.traversal[i]
        
        return minDiff
        