# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.numList = []
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.numList.append(root.val)
            self.inorder(root.right)
        
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        self.inorder(root1)
        self.inorder(root2)
        
        return sorted(self.numList)