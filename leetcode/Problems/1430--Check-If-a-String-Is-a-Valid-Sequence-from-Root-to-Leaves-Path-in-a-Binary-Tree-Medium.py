# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        if not root:
            if len(arr) != 0:
                return False

        
        if len(arr) == 0:
            return False
        if root.val != arr[0]:
            return False
        elif root.val == arr[0] and not root.left and not root.right and len(arr) == 1:
            return True
        left = self.isValidSequence(root.left, arr[1:])

        right = self.isValidSequence(root.right, arr[1:])
        
        return left or right