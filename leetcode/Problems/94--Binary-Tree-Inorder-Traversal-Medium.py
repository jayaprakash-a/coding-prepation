# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        
        answer = []
        if root.left:
            answer += self.inorderTraversal(root.left)
            
        answer.append(root.val)
        
        if root.right:
            answer += self.inorderTraversal(root.right)
        
        
        return answer