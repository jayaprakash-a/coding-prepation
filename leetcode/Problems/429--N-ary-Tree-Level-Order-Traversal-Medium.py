"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""     

class Solution:
    def __init__(self):
        self.answer = []
        self.maxLevels = 0
    def level(self, root, level) -> int:
        if not root:
            return
        if level > self.maxLevels:
            maxLevels = level
        if level < len(self.answer):
            self.answer[level] += [root.val]
        else:
            self.answer.append([root.val])
        for child in root.children:
            self.level(child, level+1)
                
        
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        self.level(root, 0)
        return self.answer
