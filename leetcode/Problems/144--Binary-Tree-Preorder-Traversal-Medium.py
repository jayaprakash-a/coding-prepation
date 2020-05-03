class Solution:
    def __init__(self):
        self.answer = []
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root:
            self.answer.append(root.val)
           
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)

        return self.answer
        