# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        # print('c1', root.val)
        
        
        answer = self.sumOfLeftLeaves(root.right)
        # print('c2', root.val, answer)
        if root.left and not root.left.left and not root.left.right:
            answer += root.left.val
        else:
            answer += self.sumOfLeftLeaves(root.left)

        return answer
        