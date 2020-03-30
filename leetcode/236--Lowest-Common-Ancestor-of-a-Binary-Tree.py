# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.answer = None
    def lca(self, root, p, q):
        if not root:
            return False
        answer = None
        if root.val == p.val or root.val == q.val:  
            answer = True
        
        left = self.lca(root.left, p, q)
        right = self.lca(root.right, p, q)

        if (left and right) or (left and answer) or (right and answer):
            self.answer = root
        return (left or right or answer)
            
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.lca(root, p, q)
        return self.answer
        
            