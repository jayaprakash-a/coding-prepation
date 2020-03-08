# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        answer = 0
        if not root:
            return 0
        if root.val >= L and root.val <= R:
            answer += root.val
            
        answer += self.rangeSumBST(root.left, L, R)
        answer += self.rangeSumBST(root.right, L, R)
        
        return answer
        