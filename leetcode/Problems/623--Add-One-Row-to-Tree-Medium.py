# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if not root and d >= 1:
            return None
        if d == 1:
            temp = TreeNode(v)
            temp.left = root
            root = temp
            return root
        elif d == 2:
            temp = root.left
            root.left = TreeNode(v)
            root.left.left = temp
            temp = root.right
            root.right = TreeNode(v)
            root.right.right = temp
            return root
        root.left = self.addOneRow(root.left, v, d-1)
        root.right = self.addOneRow(root.right, v, d-1)
        return root
