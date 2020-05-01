class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

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

exampleTree = TreeNode(4)
exampleTree.left = TreeNode(2)
exampleTree.right = TreeNode(6)
exampleTree.left.left = TreeNode(1)
exampleTree.left.right = TreeNode(3)
exampleTree.right.left = TreeNode(5)
exampleTree.right.right = TreeNode(7)

iterator = BSTIterator(exampleTree)

while(iterator.hasNext()):
	print(iterator.next(), end='-->')
print()
