# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:
	
	def __init__(self, root):		
		self.pointers = []		
		if not root:
			return
		
		temp = root
		while(temp):
			self.pointers.append(temp)
			temp = temp.left

	def next(self):
		
		current = self.pointers.pop()
		temp = current.right
		while(temp):
			self.pointers.append(temp)
			temp = temp.left

		return current.val

	def hasNext(self):

		return len(self.pointers) > 0

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        iterator = BSTIterator(root)
        
        newRoot = TreeNode(iterator.next())
        temp = newRoot
        
        while(iterator.hasNext()):
            temp.right = TreeNode(iterator.next())
            temp = temp.right
        
        return newRoot