# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        if root.val == val:
            return root
        ans1 = self.searchBST(root.right, val)
        ans2 = self.searchBST(root.left, val)
        
        if not ans1 and not ans2:
            return None
        if not ans1:
            return ans2
        return ans1
        