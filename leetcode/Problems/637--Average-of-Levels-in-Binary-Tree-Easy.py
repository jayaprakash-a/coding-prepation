# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.answer = []
        self.maxLevels = 0
    def level(self, root: TreeNode, level) -> int:
        if not root:
            return
        if level > self.maxLevels:
            self.maxLevels = level
        if level < len(self.answer):
            self.answer[level] += [root.val]
        else:
            self.answer.append([root.val])
        
        self.level(root.left, level+1)
        self.level(root.right, level+1)
        
        
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        self.level(root, 0)
        average = []
        for i in range(len(self.answer)):
            average.append(sum(self.answer[i])/len(self.answer[i]))
        return average
