# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.sumVals = {}
    def levelSums(self, root: TreeNode, level) -> int:
        if not root:
            return
        if level not in self.sumVals.keys():
            self.sumVals[level] = root.val
        else:
            self.sumVals[level] += root.val
        
        self.levelSums(root.left, level+1)
        self.levelSums(root.right, level+1)
        
        
    def maxLevelSum(self, root):
        self.levelSums(root, 1)
        maxVal = max(self.sumVals.values())
        for i in range(1, max(self.sumVals.keys())):
            if self.sumVals[i] == maxVal:
                return i
        return