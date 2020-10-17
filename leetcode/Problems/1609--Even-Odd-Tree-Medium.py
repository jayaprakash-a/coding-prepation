# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        answer = []
        def traverse(node, level):
            
            if not node:
                return True
            # print('1', answer, level)
            if node.val%2 == level%2:
                return False
            if level >= len(answer):
                answer.append(node.val)
            else:
                # print(answer, level)
                if level%2 ==0:
                    if answer[level] >= node.val:
                        return False
                    answer[level] = node.val
                else:
                    if answer[level] <= node.val:
                        return False
                    answer[level] = node.val
            return traverse(node.left, level+1) and traverse(node.right, level+1)
        # print('--------------')
        return traverse(root, 0)
        