"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    # Recursive solution
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        answer = [root.val]
        for child in root.children:
            answer += self.preorder(child)
        return answer
    # Iterative solution
    def preorder(self, root):
        if not root:
            return []
        nodes = [root]
        answer = []
        
        while(len(nodes)!=0):
            node = nodes.pop()
            answer.append(node.val)
            nodes += node.children[::-1]
        return answer