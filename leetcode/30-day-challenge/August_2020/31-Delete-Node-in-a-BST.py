# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
            return root
        elif root.val < key:            
            root.right = self.deleteNode(root.right, key)            
            return root        
        elif root.val == key:
            if not root.left and not root.right:
                return None
            elif root.right and not root.left:
                return root.right
            elif root.left and not root.right:
                return root.left
            else:
                temp = root.right
                # parent = temp
                while(temp.left):
                    temp = temp.left
                root.val = temp.val
                root.right = self.deleteNode(root.right, temp.val) 
                return root