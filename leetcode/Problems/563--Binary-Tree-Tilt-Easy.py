# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        def helper(root):
            if not root:
                return 0, 0
            
            left, right = helper(root.left), helper(root.right)

            return (abs(left[1]-right[1])+left[0]+right[0], left[1]+right[1]+root.val)
        
        return helper(root)[0]