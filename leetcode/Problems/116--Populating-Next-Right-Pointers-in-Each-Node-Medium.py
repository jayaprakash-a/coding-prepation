"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        def assign(r1, r2):
            if not r1:
                return
            r1.next = r2
            
            assign(r1.left, r1.right)
            if r2:
                assign(r1.right, r2.left)
                assign(r2.left, r2.right)
                assign(r2.right, None)
        assign(root.left, root.right)
        return root