# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def isValidBST(self, root: TreeNode) -> bool:
        
        def inorder(root):
            if not root:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)
        
        answer = inorder(root)
        
        for i in range(len(answer)-1):
            if answer[i] >= answer[i+1]:
                return False
        return True