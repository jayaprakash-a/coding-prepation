# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSimilarTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p == None and q == None:
            return True
        elif p == None and q:
            return False
        elif q == None and p:
            return False
        
        if p.val == q.val:
            return self.isSimilarTree(p.left, q.right) and self.isSimilarTree(p.right, q.left)
        
        else:
            return False
        
    def isSymmetric(self, root: TreeNode) -> bool:
        
        
        if not root:
            return True
        
        return self.isSimilarTree(root.left, root.right) 
        
        
        
        
        
       