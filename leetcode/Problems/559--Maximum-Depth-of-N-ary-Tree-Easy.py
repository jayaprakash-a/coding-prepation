"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        answer = 0
        for child in root.children:
            answer = max(self.maxDepth(child), answer)
        return answer+1