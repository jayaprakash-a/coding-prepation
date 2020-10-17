# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ''
        answer = ''
        answer += (str(root.val) + ' ')
        answer += (self.serialize(root.left) + ' ')
        answer += (self.serialize(root.right) + ' ')
        
        return answer

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        entries = list(map(int, data.split()))
        if len(entries) == 0:
            return None
        def addNode(node, val):
            if not node:
                return TreeNode(val)
            
            if node.val >= val:
                node.left = addNode(node.left, val)
            else:
                node.right = addNode(node.right, val)
            return node
        root = TreeNode(entries[0]) 
        for i in range(1, len(entries)):
            root = addNode(root, entries[i])
        return root

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans