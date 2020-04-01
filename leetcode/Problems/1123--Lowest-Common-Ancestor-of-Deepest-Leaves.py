# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        
        # depth = self.depth(root)
        # print(depth)
        # self.answer = None
        # self.depthval = 0
        
        
        return self.getNode(root)
        
    
    def getNode(self, root):
        if not root:
            return None

        leftDepth, rightDepth = self.depth(root.left), self.depth(root.right)
        if leftDepth == rightDepth:
            return root
        elif leftDepth < rightDepth:
            return self.getNode(root.right)
        else:
            return self.getNode(root.left)
    
    def depth(self, root):
        if not root:
            return 0
        return max(self.depth(root.left), self.depth(root.right))+1
        