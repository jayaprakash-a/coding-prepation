# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class FindElements:

    def __init__(self, root: TreeNode):
        self.vals = set()
        self.vals.add(0)
        root.val = 0
        if root.left:
            root.left.val = 2*root.val+1
            self.vals.add(2*root.val+1)
            root.left = self.recover(root.left)
            
        if root.right:
            root.right.val = 2*root.val+2
            self.vals.add(2*root.val+2)
            root.right = self.recover(root.right)
            
        
        self.root = root
        # self.printTree(self.root)

    def find(self, target: int) -> bool:
        return target in self.vals
    
    def printTree(self, root):
        if root:
            print(root.val, end =" ")
        else:
            return
        self.printTree(root.left)
        self.printTree(root.right)
            
    
    def recover(self, root):
        if root == None:
            return root
        
        
        if root.left:
            root.left.val = 2*root.val+1
            self.vals.add(2*root.val+1)
            root.left = self.recover(root.left)
            
        if root.right:
            root.right.val = 2*root.val+2
            self.vals.add(2*root.val+2)
            root.right = self.recover(root.right)
            
        
        return root
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)