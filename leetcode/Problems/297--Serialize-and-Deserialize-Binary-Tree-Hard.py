# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def preorder(root):
            if not root:
                return ['null']
            return [str(root.val)] + preorder(root.left) + preorder(root.right)
        
        # print('[' + ','.join(preorder(root)) + ']')
        return '[' + ','.join(preorder(root)) + ']'

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        arr = data[1:-1].split(',')
        self.index = 0
        def construct():
            
            if arr[self.index] == 'null':
                self.index += 1
                return None
            root = TreeNode(int(str(arr[self.index])))
            self.index += 1
            if self.index >= len(arr):
                return root
            root.left = construct()
            root.right = construct()
            return root
        return construct()
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))