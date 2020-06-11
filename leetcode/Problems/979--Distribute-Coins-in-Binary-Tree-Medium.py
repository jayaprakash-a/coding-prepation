# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# [No of nodes in subtree, No of coins in subtree]
class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.answer = 0
        def dfs(root):
            if not root:
                return [0, 0]
            left = dfs(root.left)
            right = dfs(root.right)
            # answer = left[2] + right[2]
            self.answer += abs(left[0] - left[1])
            self.answer += abs(right[0] - right[1])
            return [left[0]+right[0]+1, left[1]+right[1]+root.val]
        dfs(root)
        return self.answer