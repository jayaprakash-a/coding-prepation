# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and t2:
            return t2
        if not t2 and t1:
            return t1
        if not t1 and not t2:
            return None
        value = 0
        if t1 and t2:
            value = t1.val+t2.val
        
        root = TreeNode(value)
        # print(root)
        root.right = self.mergeTrees(t1.right, t2.right)
        root.left = self.mergeTrees(t1.left, t2.left)
        
        return root
        