# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.diameter = 1
    def depth(self, root, depth) -> int:
        if not root:
            return 0
        
        rDepth = self.depth(root.right,depth+1)
        lDepth = self.depth(root.left, depth+1)
        
        if lDepth+rDepth+1 > self.diameter:
            self.diameter = lDepth+rDepth+1
            
        return max(rDepth, lDepth)+1
    
    def diameterOfBinaryTree(self, root):        
        
        self.depth(root,0)        
        return self.diameter-1
        