# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        if val > root.val:
            newRoot = TreeNode(val)
            newRoot.left = root
            return newRoot        
        root.right = self.insertIntoMaxTree(root.right, val)
        return root
        