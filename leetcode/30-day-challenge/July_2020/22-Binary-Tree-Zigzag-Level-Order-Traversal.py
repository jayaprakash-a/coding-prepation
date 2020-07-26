# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:       
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        answer = []
        def levelTraversal(root, level) -> int:
            if not root:
                return

            if level < len(answer):
                answer[level] += [root.val]
            else:
                answer.append([root.val])
            levelTraversal(root.left, level+1)
            levelTraversal(root.right, level+1)
        levelTraversal(root, 0)
        for i in range(1, len(answer), 2):
            answer[i] = answer[i][::-1]
        return answer
        

        