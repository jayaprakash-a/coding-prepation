# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    value = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        root.right = self.bstToGst(root.right)
        # if root.right:
        #     root.val += (root.right.val)
        self.value = self.value+ root.val
        root.val = self.value
        # if root.left:
        #     root.left.val += root.val
        
        root.left = self.bstToGst(root.left)
        
        return root
    
        