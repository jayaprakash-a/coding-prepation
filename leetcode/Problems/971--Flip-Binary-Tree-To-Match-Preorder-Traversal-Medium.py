# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        self.index = 0
        answer = []
        def dfs(root):
            if not root:
                return True
            if root.val != voyage[self.index]:
                return False
            self.index += 1
            if root.left and root.left.val != voyage[self.index]:
                root.left, root.right = root.right, root.left
                answer.append(root.val)
            return dfs(root.left) and dfs(root.right)
        if dfs(root):
            return answer
        else:
            return [-1]
            