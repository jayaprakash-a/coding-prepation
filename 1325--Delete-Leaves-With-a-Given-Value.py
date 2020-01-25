# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        
        
        newRoot = self.removeNodes(root, target)
        
        return newRoot
        # while(isEqual(newRoot, root)):
            # newRoot = removeNodes
            
    
    
    
    def removeNodes(self, root: TreeNode, target: int) -> TreeNode:
        if root == None:
            return None
        if root.left == None and root.right == None and root.val == target:
            return None
        
        root.left = self.removeNodes(root.left, target)
        
        # if root.left
        root.right = self.removeNodes(root.right, target)
        
        if root.left == None and root.right == None and root.val == target:
            return None
        return root
        