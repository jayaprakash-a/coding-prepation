# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        
        root = TreeNode(preorder[0])
        
        left = []
        right = []        
        for i in range(1, len(preorder)):
            if preorder[i] >= preorder[0]:
                right.append(preorder[i])
            else:
                left.append(preorder[i])
        root.left = self.bstFromPreorder(left)
        root.right = self.bstFromPreorder(right)
        
        return root
            