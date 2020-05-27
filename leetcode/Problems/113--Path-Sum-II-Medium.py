# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        self.answer = []
        def dfs(root, arr, val):            
            if not root:
                return
            arr = list(arr)
            arr += [root.val]
            val -= root.val
            if val == 0 and not root.right and not root.left:
                self.answer.append(arr)
            if root.left:
                dfs(root.left, arr, val)
            if root.right:
                dfs(root.right, arr, val)
            return
        dfs(root, [], sum)
        return self.answer
                