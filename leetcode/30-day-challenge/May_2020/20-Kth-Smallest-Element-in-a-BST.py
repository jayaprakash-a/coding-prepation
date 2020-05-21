# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def inorder(self, root):
        if not root:
            return []
        answer = []
        answer += self.inorder(root.left)
        answer += [root.val]
        answer += self.inorder(root.right)
        
        return answer
        
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        order = self.inorder(root)
        return order[k-1]