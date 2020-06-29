# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        hl, hr = 0, 0
        l, r = root, root
        while(l):
            l = l.left
            hl += 1
        while(r):
            r = r.right
            hr += 1
        
        if hl == hr:
            return 2**(hl)-1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)