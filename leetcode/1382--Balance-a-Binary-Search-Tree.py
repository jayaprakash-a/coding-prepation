# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inOrder(self, root):
        if not root:
            return []
        arr1 = []
        arr1 += self.inOrder(root.left)
        arr1.append(root.val)
        arr1 += self.inOrder(root.right)
        
        return arr1
    
    def balance(self, nums):
        if len(nums) == 0:
            return None
        
        midIndex = len(nums)//2
        
        root = TreeNode(nums[midIndex])
        root.left = self.balance(nums[:midIndex])
        # if root.left:
        #     print(root.val, root.left.val)
        # else:
        #     print(root.val, 'left')
        root.right = self.balance(nums[midIndex+1:])
        # if root.right:
        #     print(root.val, root.right.val)
        # else:
        #     print(root.val, 'right')
        
        
        return root
        
        
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nums = self.inOrder(root)
        print(nums)
        node = self.balance(nums)
        
        return node